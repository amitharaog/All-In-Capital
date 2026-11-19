"""The intake pipeline, one function per box on the whiteboard.

  Define Rubrics -> Collect Info (Deck, Free Source, Scrape) -> Score the Startup
  -> Recommendation -> [human] -> Final Decision --Go--> Draft Email -> [HITL]
  -> Send Email -> Meeting Booking Agent --Yes--> Meeting Booked
                                         --No--> closed
                                         --No reply for x days--> Follow-up
  Feedback loop 1: Final Decision -> Recommendation (an override becomes a
                   correction the scorer uses on similar companies).
  Feedback loop 2: HITL on the draft -> Draft Email (edits are logged and can
                   become the template).

Each application moves through explicit stages stored in
data/pipeline/state.json with a timestamped history. A stage can only be
entered from the stage before it, so nothing skips the human steps.
"""
from __future__ import annotations

import datetime as dt
import re
from zoneinfo import ZoneInfo

from . import conflicts, corrections, emailer, scheduling, scrape, storage
from .core import APPS, DATA, FUND, decide, list_slugs, load_json, load_thesis
from .schemas import ResearchDossier, ScoreCard

IST = ZoneInfo("Asia/Kolkata")
STATE = DATA / "pipeline" / "state.json"
CONFIG = FUND / "pipeline.json"
DEFAULT_CONFIG = {"follow_up_after_days": 3, "max_follow_ups": 2, "slots_offered": 3, "min_notice_hours": 20}

# whiteboard stage names
COLLECTED, SCORED, RECOMMENDED = "INFO_COLLECTED", "SCORED", "RECOMMENDED"
GO, NO_GO, HOLD = "DECIDED_GO", "DECIDED_NO_GO", "DECIDED_HOLD"
DRAFTED, APPROVED, SENT = "EMAIL_DRAFTED", "EMAIL_APPROVED", "EMAIL_SENT"
FOLLOWED_UP, RESCHEDULING, NEEDS_HUMAN = "FOLLOWED_UP", "RESCHEDULING", "NEEDS_HUMAN"
BOOKED, DECLINED, NO_REPLY, CLOSED = "MEETING_BOOKED", "DECLINED", "CLOSED_NO_REPLY", "CLOSED"
AWAITING_REPLY = {SENT, FOLLOWED_UP, RESCHEDULING}


class StageError(RuntimeError):
    pass


def now_ist() -> dt.datetime:
    return dt.datetime.now(IST)


def config() -> dict:
    return {**DEFAULT_CONFIG, **(load_json(CONFIG) if CONFIG.exists() else {})}


def load_state() -> dict:
    return storage.read_json(STATE, {"rubric_version": None, "apps": {}})


def save_state(state: dict) -> None:
    storage.write_json(STATE, state)


def _app(state: dict, slug: str) -> dict:
    return state["apps"].setdefault(slug, {"stage": None, "history": [], "emails": [], "drafts": [],
                                           "seen_replies": [], "follow_ups": 0})


def _move(app: dict, stage: str, event: str, now: dt.datetime, by: str = "system", detail: str = "") -> None:
    app["stage"] = stage
    app["history"].append({"at": now.isoformat(timespec="minutes"), "stage": stage, "event": event, "by": by,
                           "detail": detail})


def _require(app: dict, allowed: set[str], action: str) -> None:
    if app["stage"] not in allowed:
        raise StageError(f"cannot {action} from stage {app['stage']} (needs one of {sorted(allowed)})")


def _dossier(slug: str) -> ResearchDossier:
    return ResearchDossier.model_validate(load_json(DATA / "research" / f"{slug}.json"))


# ------------------------------------------------------------------ 1. Define Rubrics

def define_rubrics(now: dt.datetime | None = None) -> dict:
    now = now or now_ist()
    t = load_thesis()
    problems = []
    for lens_id, lens in t["lenses"].items():
        w = sum(c["weight"] for c in lens["criteria"])
        if w != 100:
            problems.append(f"{lens_id} weights sum to {w}, not 100")
        ids = [c["id"] for c in lens["criteria"]]
        if len(ids) != len(set(ids)):
            problems.append(f"{lens_id} has duplicate criterion ids")
        for c in lens["criteria"]:
            for key in ("definition", "high", "low"):
                if not c.get(key):
                    problems.append(f"{c['id']} missing {key}")
    if problems:
        raise StageError("rubric invalid: " + "; ".join(problems))
    storage.write_json(FUND / "rubric_versions" / f"{t['version']}.json", t)
    state = load_state()
    state["rubric_version"] = t["version"]
    save_state(state)
    return {"version": t["version"], "lenses": {k: len(v["criteria"]) for k, v in t["lenses"].items()},
            "gates": [g["id"] for g in t["gates"]]}


# ------------------------------------------------------------------ 2. Collect Info

def collect_info(slug: str, now: dt.datetime | None = None, scrape_links: bool = True) -> dict:
    """Deck (PDF -> text), free sources (web research), scrape (links in the application)."""
    from .pipeline import ensure_dossier

    now = now or now_ist()
    state = load_state()
    if not state.get("rubric_version"):
        raise StageError("define the rubric first (python -m triage rubric)")
    app = _app(state, slug)
    sources = []
    for kind in ("deck", "form"):  # Deck
        pdf, md = APPS / slug / f"{kind}.pdf", APPS / slug / f"{kind}.md"
        if pdf.exists() and not md.exists():
            from .ingest import pdf_to_markdown

            md.write_text(pdf_to_markdown(str(pdf)), encoding="utf-8")
        if md.exists():
            sources.append(kind)
    d = ensure_dossier(slug)  # Free Source: web search / fetch research step
    sources.append(f"free sources ({sum(1 for s in d.sources if s.kind == 'web' and not s.id.startswith('X'))} web)")
    if scrape_links:  # Scrape
        res = scrape.scrape(slug)
        d = scrape.merge(slug, res)
        live = sum(1 for r in res["results"] if r.get("ok"))
        sources.append(f"scrape ({live}/{len(res['results'])} links live)")
    _move(app, COLLECTED, "collect_info", now, detail=", ".join(sources))
    save_state(state)
    return {"slug": slug, "collected": sources, "gaps": len(d.gaps), "sources": len(d.sources)}


# ------------------------------------------------------------------ 3. Score the Startup

def score_startup(slug: str, now: dt.datetime | None = None) -> ScoreCard:
    from .pipeline import ensure_card

    now = now or now_ist()
    state = load_state()
    app = _app(state, slug)
    _require(app, {COLLECTED, SCORED, RECOMMENDED}, "score")
    card = ensure_card(_dossier(slug))
    _move(app, SCORED, "score_startup", now, detail=f"{len(card.criteria)} criteria, by {card.produced_by}")
    save_state(state)
    return card


# ------------------------------------------------------------------ 4. Recommendation

def recommend(slug: str, now: dt.datetime | None = None) -> dict:
    from .pipeline import apply_overrides

    now = now or now_ist()
    state = load_state()
    app = _app(state, slug)
    _require(app, {SCORED, RECOMMENDED}, "recommend")
    d = _dossier(slug)
    card = ScoreCard.model_validate(load_json(DATA / "scores" / f"{slug}.json"))
    apply_overrides(card)
    v = decide(d, card, load_thesis(), conflicts.check(d))
    app["recommendation"] = {"recommendation": v.recommendation, "headline": v.headline,
                             "revealed": v.revealed.score_10, "attendees": v.call_attendees}
    _move(app, RECOMMENDED, "recommend", now, detail=f"{v.recommendation} ({v.revealed.score_10}/10)")
    save_state(state)
    return app["recommendation"]


# ------------------------------------------------------------------ 5. Final Decision (human) + feedback loop 1

EXPECTED = {"TAKE_CALL": "go", "PASS": "no_go", "HOLD_CONFLICT": "hold", "SCREEN_FIRST": None}


def final_decision(slug: str, decision: str, by: str, reason: str = "", tags: list[str] | None = None,
                   now: dt.datetime | None = None) -> dict:
    """Kushal's call. If it overrides the recommendation, the reason is
    required and is stored as a correction that future scoring retrieves."""
    if decision not in ("go", "no_go", "hold"):
        raise StageError("decision must be go, no_go or hold")
    now = now or now_ist()
    state = load_state()
    app = _app(state, slug)
    _require(app, {RECOMMENDED, GO, NO_GO, HOLD}, "decide")
    rec = app["recommendation"]["recommendation"]
    override = EXPECTED[rec] is not None and EXPECTED[rec] != decision
    correction = None
    if override and not reason.strip():
        raise StageError(f"decision '{decision}' overrides the recommendation {rec}: give a one-line reason, "
                         "written so it can be reused on similar companies")
    if reason.strip() and (override or rec == "SCREEN_FIRST"):
        d = _dossier(slug)
        t = sorted(set(tags or []) | corrections.tags_for(d) | {"decision_override"})
        correction = corrections.add(d.company, f"Partner decided {decision} where the system said {rec}: {reason}",
                                     by, t).model_dump()
    app["decision"] = {"decision": decision, "by": by, "reason": reason, "override": override,
                       "correction_id": correction["id"] if correction else None, "at": now.isoformat(timespec="minutes")}
    decisions = storage.read_json(DATA / "decisions.json", {})
    decisions[slug] = {"decision": {"go": "call", "no_go": "pass", "hold": "hold"}[decision], "by": by,
                       "date": now.date().isoformat(), "note": reason}
    storage.write_json(DATA / "decisions.json", decisions)
    stage = {"go": GO, "no_go": NO_GO, "hold": HOLD}[decision]
    _move(app, stage, "final_decision", now, by=by,
          detail=("override of " + rec + "; correction " + correction["id"]) if correction else f"agrees with {rec}")
    save_state(state)
    return app["decision"]


# ------------------------------------------------------------------ 6. Draft Email

def _founder(slug: str) -> tuple[str, str | None]:
    d = _dossier(slug)
    name = d.founders[0].name if d.founders else "there"
    text = (d.founder_contact or "") + " " + (APPS / slug / "form.md").read_text(encoding="utf-8")
    m = re.search(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", text)
    return name, (m.group(0) if m else None)


def _taken_slots(state: dict, exclude: str) -> set[dt.datetime]:
    taken = set()
    for s, a in state["apps"].items():
        if s != exclude and a["stage"] in AWAITING_REPLY | {DRAFTED, APPROVED}:
            taken |= {dt.datetime.fromisoformat(x) for x in a.get("offered_slots", [])}
    return taken


def _pick_slots(state: dict, slug: str, attendees: list[str], now: dt.datetime, exclude: set[str] | None = None,
                not_before: str | None = None) -> list[str]:
    cfg = config()
    earliest = now + dt.timedelta(hours=cfg["min_notice_hours"])
    if not_before:
        earliest = max(earliest, dt.datetime.fromisoformat(not_before).replace(tzinfo=IST))
    horizon = max(14, (earliest.date() - now.date()).days + 14)
    exclude = exclude or set()
    free = [s for s in scheduling.free_slots(attendees, now.date(), _taken_slots(state, slug), days=horizon)
            if s >= earliest and s.isoformat() not in exclude]
    picked, days = [], set()
    for s in free:  # spread across days first
        if s.date() not in days:
            picked.append(s)
            days.add(s.date())
        if len(picked) == cfg["slots_offered"]:
            break
    for s in free:
        if len(picked) == cfg["slots_offered"]:
            break
        if s not in picked:
            picked.append(s)
    return [s.isoformat() for s in sorted(picked)]


def draft_email(slug: str, now: dt.datetime | None = None, pass_note: bool = False, to: str | None = None) -> dict:
    now = now or now_ist()
    state = load_state()
    app = _app(state, slug)
    d = _dossier(slug)
    founder, found = _founder(slug)
    app["founder_email"] = to or app.get("founder_email") or found
    if not app["founder_email"]:
        raise StageError(f"no founder email in the {slug} application; draft again with --to <address>")
    if pass_note:
        _require(app, {NO_GO}, "draft a pass note")
        card = load_json(DATA / "scores" / f"{slug}.json")
        values = {"slug": slug, "company": d.company, "founder_first": founder.split()[0],
                  "what_would_change": card.get("what_would_change_our_view") or "clearer numbers on what decides this category"}
        kind = "pass"
    else:
        _require(app, {GO}, "draft an invite")
        attendees = app["recommendation"]["attendees"]
        slots = _pick_slots(state, slug, attendees, now)
        if not slots:
            raise StageError("no free Tue/Thu afternoon slots in the next two weeks")
        app["offered_slots"] = slots
        partners = " and ".join(a for a in attendees if a != "Riya")
        values = {"slug": slug, "company": d.company, "founder_first": founder.split()[0], "partners": partners,
                  "slots": slots}
        kind = "invite"
    msg = emailer.render(kind, **dict(values))
    draft = {"version": len(app["drafts"]) + 1, "kind": kind, **msg, "values": values, "status": "pending_review",
             "style_notes": emailer.style_notes(kind), "at": now.isoformat(timespec="minutes")}
    app["drafts"].append(draft)
    _move(app, DRAFTED, "draft_email", now, detail=f"{kind} v{draft['version']}")
    save_state(state)
    return draft


# ------------------------------------------------------------------ 7. HITL on the draft + feedback loop 2

def review_draft(slug: str, by: str, approve: bool = True, subject: str | None = None, body: str | None = None,
                 note: str = "", save_template: bool = False, now: dt.datetime | None = None) -> dict:
    now = now or now_ist()
    state = load_state()
    app = _app(state, slug)
    _require(app, {DRAFTED}, "review a draft")
    draft = app["drafts"][-1]
    original = {"subject": draft["subject"], "body": draft["body"]}
    edited = {"subject": subject or draft["subject"], "body": body or draft["body"]}
    if subject or body or note:
        fb = emailer.record_feedback(slug, draft["kind"], original, edited, note, by, draft["values"], save_template)
        draft["feedback"] = fb
    draft.update(edited)
    if approve:
        draft["status"] = "approved"
        draft["approved_by"] = by
        _move(app, APPROVED, "review_draft", now, by=by, detail="approved" + (" with edits" if original != edited else ""))
    else:
        draft["status"] = "rejected"
        back = NO_GO if draft["kind"] == "pass" else GO
        _move(app, back, "review_draft", now, by=by, detail=f"rejected: {note}")
    save_state(state)
    return draft


# ------------------------------------------------------------------ 8. Send Email

def _send(app: dict, slug: str, kind: str, subject: str, body: str, now: dt.datetime, ics: str | None = None,
          slots: list[str] | None = None) -> dict:
    to = app.get("founder_email") or _founder(slug)[1]
    prev = app["emails"][-1]["message_id"] if app["emails"] else None
    msg = emailer.build_message(to, subject, body, ics=ics, in_reply_to=prev)
    where = emailer.sender().send(slug, kind, msg)
    rec = {"kind": kind, "at": now.isoformat(timespec="minutes"), "to": to, "subject": subject,
           "message_id": msg["Message-ID"], "stored": where, "slots": slots or []}
    app["emails"].append(rec)
    app["last_sent_at"] = rec["at"]
    return rec


def send_email(slug: str, now: dt.datetime | None = None) -> dict:
    now = now or now_ist()
    state = load_state()
    app = _app(state, slug)
    _require(app, {APPROVED}, "send")
    draft = app["drafts"][-1]
    rec = _send(app, slug, draft["kind"], draft["subject"], draft["body"], now, slots=app.get("offered_slots"))
    draft["status"] = "sent"
    if draft["kind"] == "pass":
        _move(app, CLOSED, "send_email", now, detail=f"pass note sent to {rec['to']}")
    else:
        _move(app, SENT, "send_email", now, detail=f"invite sent to {rec['to']} ({emailer.sender().name})")
    save_state(state)
    return rec


# ------------------------------------------------------------------ 9. Meeting Booking Agent

def _book(app: dict, slug: str, slot_iso: str, now: dt.datetime) -> dict:
    d = _dossier(slug)
    attendees = app["recommendation"]["attendees"]
    slot = dt.datetime.fromisoformat(slot_iso)
    cal = scheduling._config()
    founder = _founder(slug)[0]
    to = app.get("founder_email")
    ics = scheduling.ics(d.company, slot, attendees, to, cal.get("emails", {}))
    link = scheduling.calendar_backend().book(d.company, slot, attendees, to)
    msg = emailer.render("confirmation", slug=slug, company=d.company, founder_first=founder.split()[0],
                         partners=" and ".join(a for a in attendees if a != "Riya"), slot_human=emailer.human_slot(slot_iso))
    _send(app, slug, "confirmation", msg["subject"], msg["body"], now, ics=ics)
    app["booking"] = {"slot": slot_iso, "attendees": attendees, "calendar": link, "at": now.isoformat(timespec="minutes")}
    return app["booking"]


def _reoffer(app: dict, state: dict, slug: str, kind: str, now: dt.datetime, not_before: str | None = None) -> dict:
    d = _dossier(slug)
    founder, _ = _founder(slug)
    already = {s for e in app["emails"] for s in e.get("slots", [])} if kind == "reschedule" else set()
    slots = _pick_slots(state, slug, app["recommendation"]["attendees"], now, exclude=already, not_before=not_before)
    if not slots:
        raise StageError("no free slots to offer")
    app["offered_slots"] = slots
    days = (now - dt.datetime.fromisoformat(app["emails"][0]["at"])).days
    msg = emailer.render(kind, slug=slug, company=d.company, founder_first=founder.split()[0], slots=slots, days=days)
    return _send(app, slug, kind, msg["subject"], msg["body"], now, slots=slots)


def _notify(slug: str, text: str, now: dt.datetime) -> None:
    """Internal note to Riya (same send backend, addressed to the desk)."""
    first = " ".join(text.splitlines()[0].split())[:80] if text else ""
    msg = emailer.build_message(emailer.FROM_ADDR, f"[triage] {slug}: {first}", text)
    emailer.sender().send("_team", slug, msg)


def booking_agent(now: dt.datetime | None = None, slugs: list[str] | None = None) -> list[dict]:
    """One pass of the agent over every application waiting on a founder.
    Run it on a schedule (e.g. hourly)."""
    now = now or now_ist()
    cfg = config()
    state = load_state()
    box = emailer.inbox()
    actions = []
    for slug, app in state["apps"].items():
        if slugs and slug not in slugs:
            continue
        if app["stage"] not in AWAITING_REPLY:
            continue
        replies = box.fetch(slug, set(app["seen_replies"]))
        if replies:
            r = replies[-1]
            app["seen_replies"] += [x["id"] for x in replies]
            from .replies import read_reply

            text = emailer.strip_quoted(r["body"])
            offered = app.get("offered_slots", [])
            read = read_reply(text, offered, now.date())
            if read.intent == "yes" and read.slot and dt.datetime.fromisoformat(read.slot) <= now:
                read.intent, read.reason = "reschedule", "chosen slot has already passed"
            app.setdefault("replies", []).append({"at": now.isoformat(timespec="minutes"), "text": text[:500],
                                                  **read.model_dump()})
            if read.intent == "yes":
                b = _book(app, slug, read.slot, now)
                _move(app, BOOKED, "booking_agent", now, detail=f"founder said yes; booked {b['slot']} ({read.method})")
            elif read.intent == "no":
                _move(app, DECLINED, "booking_agent", now, detail=f"founder declined ({read.method}): {read.reason}")
            elif read.intent == "reschedule":
                _reoffer(app, state, slug, "reschedule", now, read.not_before)
                _move(app, RESCHEDULING, "booking_agent", now, detail="founder asked for other times; new slots sent"
                      + (f" from {read.not_before}" if read.not_before else ""))
            else:
                _move(app, NEEDS_HUMAN, "booking_agent", now, detail=f"reply unclear: {read.reason}")
            _notify(slug, f"{app['stage']}: {app['history'][-1]['detail']}\n\nFounder wrote:\n{text}", now)
            actions.append({"slug": slug, "reply": read.intent, "stage": app["stage"]})
            continue
        last = dt.datetime.fromisoformat(app["last_sent_at"])
        if now - last >= dt.timedelta(days=cfg["follow_up_after_days"]):
            if app["follow_ups"] < cfg["max_follow_ups"]:
                app["follow_ups"] += 1
                _reoffer(app, state, slug, "followup", now)
                _move(app, FOLLOWED_UP, "booking_agent", now,
                      detail=f"no reply for {cfg['follow_up_after_days']} days; follow-up {app['follow_ups']} sent")
            else:
                app["offered_slots"] = []
                _move(app, NO_REPLY, "booking_agent", now,
                      detail=f"no reply after {cfg['max_follow_ups']} follow-ups; closed, Riya notified")
                _notify(slug, f"Closed with no reply after {cfg['max_follow_ups']} follow-ups.", now)
            actions.append({"slug": slug, "reply": None, "stage": app["stage"]})
    save_state(state)
    return actions


def resolve(slug: str, intent: str, by: str, slot: str | None = None, now: dt.datetime | None = None) -> dict:
    """A person reads an unclear reply and tells the agent what it meant."""
    now = now or now_ist()
    state = load_state()
    app = _app(state, slug)
    _require(app, {NEEDS_HUMAN}, "resolve")
    if intent == "yes":
        slot = slot or app["offered_slots"][0]
        _book(app, slug, slot, now)
        _move(app, BOOKED, "resolve", now, by=by, detail=f"booked {slot}")
    elif intent == "no":
        _move(app, DECLINED, "resolve", now, by=by)
    elif intent == "reschedule":
        _reoffer(app, state, slug, "reschedule", now)
        _move(app, RESCHEDULING, "resolve", now, by=by)
    else:
        raise StageError("intent must be yes, no or reschedule")
    save_state(state)
    return {"slug": slug, "stage": app["stage"]}


# ------------------------------------------------------------------ batch helpers

def run_automated(slugs: list[str] | None = None, now: dt.datetime | None = None, scrape_links: bool = True) -> list[dict]:
    """Boxes 1-4 for the whole pile: everything up to the human decision."""
    now = now or now_ist()
    define_rubrics(now)
    out = []
    for slug in slugs or list_slugs():
        state = load_state()
        if _app(state, slug)["stage"] not in (None, COLLECTED, SCORED, RECOMMENDED):
            out.append({"slug": slug, "skipped": f"already at {state['apps'][slug]['stage']}"})
            continue
        collect_info(slug, now, scrape_links)
        score_startup(slug, now)
        out.append({"slug": slug, **recommend(slug, now)})
    return out


def status() -> list[dict]:
    state = load_state()
    return [{"slug": s, "stage": a["stage"], "last": a["history"][-1] if a["history"] else None}
            for s, a in sorted(state["apps"].items())]
