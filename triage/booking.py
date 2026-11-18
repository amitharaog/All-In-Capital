"""Turn Kushal's approvals into held calendar slots, invites and emails.

Only applications with a recorded decision are touched. A 'call' gets a held
Tue/Thu afternoon slot, an .ics invite and a founder email draft; a 'pass'
gets a kind note saying what would change our view (the HopBox practice).
Nothing is sent: drafts land in runs/<date>/outbox/ for Riya to send, or the
GoogleCalendarBackend books directly once credentials are configured.
"""
from __future__ import annotations

import datetime as dt
import re

from .core import RUNS, load_json
from .pipeline import DECISIONS
from .scheduling import book_local, pass_note_draft


def _founder_email(dossier: dict) -> str | None:
    if dossier.get("founder_contact"):
        m = re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", dossier["founder_contact"])
        if m:
            return m.group(0)
    return None


def book_approved(today: dt.date | None = None) -> list[dict]:
    today = today or dt.date.today()
    run_dir = sorted(RUNS.glob("*/batch.json"))[-1].parent
    batch = load_json(run_dir / "batch.json")
    decisions = load_json(DECISIONS) if DECISIONS.exists() else {}
    by_slug = {i["dossier"]["slug"]: i for i in batch["items"]}
    out_dir = run_dir / "outbox"
    calls, results = [], []
    for slug, dec in decisions.items():
        item = by_slug.get(slug)
        if not item:
            continue
        d = item["dossier"]
        founder = (d["founders"][0]["name"] if d["founders"] else "there")
        if dec["decision"] == "call":
            calls.append({"slug": slug, "company": d["company"], "sector": d["sector"], "founder_name": founder,
                          "founder_email": _founder_email(d), "attendees": item["verdict"]["call_attendees"]})
        elif dec["decision"] == "pass":
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / f"{slug}_pass_note.txt").write_text(
                pass_note_draft(d["company"], founder, item["card"].get("what_would_change_our_view")))
            results.append({"slug": slug, "status": "pass_note_drafted"})
        else:
            results.append({"slug": slug, "status": f"no action ({dec['decision']})"})
    results = book_local(calls, out_dir, today) + results
    from .core import dump_json

    dump_json(run_dir / "bookings.json", results)
    return results
