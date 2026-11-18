"""The busywork around a yes: once Kushal approves a call, book it.

Rules from the partner notes (Meeting 5):
- Tuesday or Thursday afternoons, 30 minutes.
- Aditya joins only for deeptech.
- Kushal sees every outcome before anything is decided -> this module only
  ever runs on applications with an approved decision in data/decisions.json.

Backends:
- LocalBackend (default): picks free slots from data/fund/calendar.json,
  writes an .ics invite and a founder email draft per company.
- GoogleCalendarBackend: same slot logic against real free/busy, then inserts
  the event with a Meet link and the founder as guest. Needs a service
  account or OAuth token with calendar scope (see README). Not exercised in CI.
"""
from __future__ import annotations

import datetime as dt
import uuid
from pathlib import Path
from zoneinfo import ZoneInfo

from .core import FUND, load_json

IST = ZoneInfo("Asia/Kolkata")


def _config() -> dict:
    path = FUND / "calendar.json"
    return load_json(path) if path.exists() else {}


def candidate_slots(start: dt.date, days: int = 14, cfg: dict | None = None) -> list[dt.datetime]:
    cfg = cfg or _config()
    weekdays = cfg.get("weekdays", [1, 3])  # Mon=0 -> Tue=1, Thu=3
    first, last = cfg.get("afternoon_window", ["14:00", "17:30"])
    h1, m1 = map(int, first.split(":"))
    h2, m2 = map(int, last.split(":"))
    out = []
    for i in range(1, days + 1):
        d = start + dt.timedelta(days=i)
        if d.weekday() not in weekdays:
            continue
        t = dt.datetime(d.year, d.month, d.day, h1, m1, tzinfo=IST)
        end = dt.datetime(d.year, d.month, d.day, h2, m2, tzinfo=IST)
        while t <= end:
            out.append(t)
            t += dt.timedelta(minutes=30)
    return out


def _busy(cfg: dict) -> list[tuple[dt.datetime, dt.datetime]]:
    spans = []
    for b in cfg.get("busy", []):
        s = dt.datetime.fromisoformat(b["start"]).astimezone(IST)
        e = dt.datetime.fromisoformat(b["end"]).astimezone(IST)
        spans.append((s, e))
    return spans


def free_slots(attendees: list[str], start: dt.date, taken: set[dt.datetime], cfg: dict | None = None) -> list[dt.datetime]:
    cfg = cfg or _config()
    busy = [
        (dt.datetime.fromisoformat(b["start"]).astimezone(IST), dt.datetime.fromisoformat(b["end"]).astimezone(IST))
        for b in cfg.get("busy", [])
        if not b.get("who") or set(b["who"]) & set(attendees)
    ]
    out = []
    for s in candidate_slots(start, cfg=cfg):
        e = s + dt.timedelta(minutes=30)
        if s in taken:
            continue
        if any(s < be and e > bs for bs, be in busy):
            continue
        out.append(s)
    return out


def ics(company: str, slot: dt.datetime, attendees: list[str], founder_email: str | None, emails: dict) -> str:
    end = slot + dt.timedelta(minutes=30)
    fmt = "%Y%m%dT%H%M%S"
    lines = [
        "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//All In Capital//triage//EN", "METHOD:REQUEST",
        "BEGIN:VEVENT",
        f"UID:{uuid.uuid4()}@allincapital-triage",
        f"DTSTAMP:{dt.datetime.now(dt.timezone.utc).strftime(fmt)}Z",
        f"DTSTART;TZID=Asia/Kolkata:{slot.strftime(fmt)}",
        f"DTEND;TZID=Asia/Kolkata:{end.strftime(fmt)}",
        f"SUMMARY:All In Capital x {company} - intro call (30 min)",
        "DESCRIPTION:First call. Briefing pack: runs/<date>/report.html#" + company.lower(),
    ]
    for a in attendees:
        if emails.get(a):
            lines.append(f"ATTENDEE;CN={a};ROLE=REQ-PARTICIPANT:mailto:{emails[a]}")
    if founder_email:
        lines.append(f"ATTENDEE;CN={company} founder;ROLE=REQ-PARTICIPANT:mailto:{founder_email}")
    lines += ["END:VEVENT", "END:VCALENDAR"]
    return "\r\n".join(lines) + "\r\n"


def founder_email_draft(company: str, founder_name: str, slots: list[dt.datetime], attendees: list[str]) -> str:
    opts = "\n".join(f"  - {s.strftime('%A %d %b, %I:%M %p')} IST" for s in slots)
    who = " and ".join(a for a in attendees if a != "Riya") or "Kushal"
    return (
        f"Subject: All In Capital - 30 min intro call with {company}\n\n"
        f"Hi {founder_name.split()[0]},\n\n"
        f"Thanks for applying to All In Capital. {who} would like to take a 30-minute call about {company}.\n"
        f"We've held the first slot below for you; if it doesn't work, reply with another from the list and we'll move it:\n\n"
        f"{opts}\n\n"
        "A calendar invite for the first slot is attached.\n\n"
        "Best,\nRiya\nAll In Capital\n"
    )


def pass_note_draft(company: str, founder_name: str, what_would_change: str | None) -> str:
    change = what_would_change or "a clearer view of the numbers that decide this category"
    return (
        f"Subject: Your application to All In Capital - {company}\n\n"
        f"Hi {founder_name.split()[0]},\n\n"
        f"Thank you for sending us {company}. We're not going to take this forward right now, and we'd rather tell you why than go quiet.\n\n"
        f"What would change our view: {change}\n\n"
        "If that changes, write back and we'll take another look.\n\n"
        "Best,\nRiya\nAll In Capital\n"
    )


def book_local(approvals: list[dict], out_dir: Path, today: dt.date | None = None) -> list[dict]:
    """approvals: [{slug, company, sector, founder_name, founder_email, attendees}]"""
    cfg = _config()
    today = today or dt.date.today()
    taken: set[dt.datetime] = set()
    booked = []
    out_dir.mkdir(parents=True, exist_ok=True)
    for a in approvals:
        slots = free_slots(a["attendees"], today, taken, cfg)
        if not slots:
            booked.append({**a, "status": "no_free_slot"})
            continue
        held = slots[0]
        taken.add(held)
        alternates = [s for s in slots[1:] if s.date() != held.date()][:2] or slots[1:3]
        (out_dir / f"{a['slug']}.ics").write_text(
            ics(a["company"], held, a["attendees"], a.get("founder_email"), cfg.get("emails", {}))
        )
        (out_dir / f"{a['slug']}_email.txt").write_text(
            founder_email_draft(a["company"], a.get("founder_name") or "there", [held, *alternates], a["attendees"])
        )
        booked.append({**a, "status": "held", "slot": held.isoformat(), "alternates": [s.isoformat() for s in alternates]})
    return booked


class GoogleCalendarBackend:  # pragma: no cover - needs credentials
    """Real booking. Requires `pip install google-api-python-client google-auth`
    and GOOGLE_APPLICATION_CREDENTIALS pointing at a service account with
    domain-wide delegation (or an OAuth token file) for the fund's calendars."""

    def __init__(self, calendar_id: str, attendee_calendars: dict[str, str]):
        from google.oauth2 import service_account  # type: ignore
        from googleapiclient.discovery import build  # type: ignore
        import os

        creds = service_account.Credentials.from_service_account_file(
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
            scopes=["https://www.googleapis.com/auth/calendar"],
        )
        self.svc = build("calendar", "v3", credentials=creds)
        self.calendar_id = calendar_id
        self.attendee_calendars = attendee_calendars

    def busy(self, attendees: list[str], start: dt.datetime, end: dt.datetime) -> list[tuple[dt.datetime, dt.datetime]]:
        body = {
            "timeMin": start.isoformat(), "timeMax": end.isoformat(), "timeZone": "Asia/Kolkata",
            "items": [{"id": self.attendee_calendars[a]} for a in attendees if a in self.attendee_calendars],
        }
        res = self.svc.freebusy().query(body=body).execute()
        spans = []
        for cal in res.get("calendars", {}).values():
            for b in cal.get("busy", []):
                spans.append((dt.datetime.fromisoformat(b["start"].replace("Z", "+00:00")),
                              dt.datetime.fromisoformat(b["end"].replace("Z", "+00:00"))))
        return spans

    def book(self, company: str, slot: dt.datetime, attendees: list[str], founder_email: str | None) -> str:
        event = {
            "summary": f"All In Capital x {company} - intro call (30 min)",
            "start": {"dateTime": slot.isoformat(), "timeZone": "Asia/Kolkata"},
            "end": {"dateTime": (slot + dt.timedelta(minutes=30)).isoformat(), "timeZone": "Asia/Kolkata"},
            "attendees": [{"email": self.attendee_calendars[a]} for a in attendees if a in self.attendee_calendars]
            + ([{"email": founder_email}] if founder_email else []),
            "conferenceData": {"createRequest": {"requestId": str(uuid.uuid4())}},
        }
        ev = self.svc.events().insert(
            calendarId=self.calendar_id, body=event, conferenceDataVersion=1, sendUpdates="all"
        ).execute()
        return ev.get("htmlLink", "")
