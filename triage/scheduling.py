"""The busywork around a yes: once Kushal approves a call, book it.

Rules from the partner notes (Meeting 5):
- Tuesday or Thursday afternoons, 30 minutes.
- Aditya joins only for deeptech.
- Kushal sees every outcome before anything is decided -> this module only
  ever runs on applications with an approved decision in data/decisions.json.

Backends:
- LocalCalendar (default): free/busy and bookings in data/fund/calendar.json
  (through triage.storage, so Postgres when deployed).
- GoogleCalendarBackend: same slot logic against real free/busy, then inserts
  the event with a Meet link and the founder as guest. Needs a service
  account or OAuth token with calendar scope (see README). Not exercised in CI.
"""
from __future__ import annotations

import datetime as dt
import uuid
from pathlib import Path
from zoneinfo import ZoneInfo

from . import storage
from .core import FUND

IST = ZoneInfo("Asia/Kolkata")


def _config() -> dict:
    return storage.read_json(FUND / "calendar.json", {})


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


def free_slots(attendees: list[str], start: dt.date, taken: set[dt.datetime], cfg: dict | None = None,
               days: int = 14) -> list[dt.datetime]:
    cfg = cfg or _config()
    busy = [
        (dt.datetime.fromisoformat(b["start"]).astimezone(IST), dt.datetime.fromisoformat(b["end"]).astimezone(IST))
        for b in cfg.get("busy", [])
        if not b.get("who") or set(b["who"]) & set(attendees)
    ]
    out = []
    for s in candidate_slots(start, days=days, cfg=cfg):
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


class LocalCalendar:
    """Books into data/fund/calendar.json: the meeting becomes a busy block for
    every attendee, so later slot searches can't offer it again."""

    name = "local"

    def book(self, company: str, slot: dt.datetime, attendees: list[str], founder_email: str | None) -> str:
        cfg = _config()
        cfg.setdefault("busy", []).append({
            "who": attendees, "start": slot.isoformat(), "end": (slot + dt.timedelta(minutes=30)).isoformat(),
            "what": f"Intro call: {company}" + (f" ({founder_email})" if founder_email else ""),
        })
        storage.write_json(FUND / "calendar.json", cfg)
        return f"local calendar: {slot.isoformat()}"


def calendar_backend():
    import os

    if os.environ.get("GOOGLE_CALENDAR_ID"):  # pragma: no cover - needs credentials
        import json

        return GoogleCalendarBackend(os.environ["GOOGLE_CALENDAR_ID"],
                                     json.loads(os.environ.get("GOOGLE_ATTENDEE_CALENDARS", "{}")))
    return LocalCalendar()
