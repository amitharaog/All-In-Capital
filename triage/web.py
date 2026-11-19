"""Web app for the intake desk: the whiteboard pipeline, clickable.

Every action calls the same functions as the CLI (triage.flow), so the stage
rules, both feedback loops and the audit history are identical. State lives in
Postgres when DATABASE_URL is set (triage.storage).

Anyone with the link can read. Actions (decide, draft, review, send, run the
agent, simulate a reply, demo clock, reset) need the passcode in APP_PASSCODE.
The booking agent also runs daily from Vercel Cron (/api/cron/agent, CRON_SECRET).
"""
from __future__ import annotations

import datetime as dt
import email
import email.policy
import hashlib
import hmac
import os
from html import escape as e
from urllib.parse import quote

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse

from . import emailer, flow, storage
from .core import DATA, ROOT, load_json, load_thesis
from .report import CSS, NEXT, REC, STAGE_LABEL, _company, render_html

app = FastAPI(title="All In Capital intake desk", docs_url=None, redoc_url=None)
BATCH = ROOT / "runs" / "2026-11-19" / "batch.json"
CLOCK = DATA / "pipeline" / "clock.json"
PEOPLE = ["Kushal", "Aditya", "Riya"]
ORDER = ["RECOMMENDED", "DECIDED_GO", "EMAIL_DRAFTED", "EMAIL_APPROVED", "EMAIL_SENT", "FOLLOWED_UP",
         "RESCHEDULING", "NEEDS_HUMAN", "MEETING_BOOKED", "DECIDED_HOLD", "DECIDED_NO_GO", "DECLINED",
         "CLOSED_NO_REPLY", "CLOSED"]
BOARD = [("Define Rubrics", None), ("Collect Info", None), ("Score the Startup", None),
         ("Recommendation", {"RECOMMENDED"}), ("Final Decision", {"DECIDED_GO", "DECIDED_HOLD", "DECIDED_NO_GO"}),
         ("Draft Email", {"EMAIL_DRAFTED"}), ("HITL", {"EMAIL_APPROVED"}),
         ("Send / Booking Agent", {"EMAIL_SENT", "FOLLOWED_UP", "RESCHEDULING", "NEEDS_HUMAN"}),
         ("Meeting Booked", {"MEETING_BOOKED"}), ("Closed", {"DECLINED", "CLOSED_NO_REPLY", "CLOSED"})]

WEB_CSS = """
nav.top{display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center;font-size:14px}
nav.top a{text-decoration:none;font-weight:600}
nav.top .spacer{flex:1}
.board{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:8px}
.box{border:1px solid var(--line);border-radius:8px;padding:10px;background:var(--surface);display:grid;gap:2px}
.box b{font:700 22px/1 var(--mono)}
.box span{font-size:12px;color:var(--muted)}
.box.auto b{color:var(--muted);font-size:14px}
.panel{background:var(--surface);border:2px solid var(--accent);border-radius:12px;padding:18px clamp(14px,3vw,24px);display:grid;gap:12px}
form{display:grid;gap:8px;margin:0}
form.inline{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
label{font-size:13px;font-weight:600;display:grid;gap:4px}
input[type=text],input[type=password],input[type=email],input[type=number],select,textarea{font:inherit;padding:8px 10px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--ink);width:100%}
textarea{min-height:220px;font-family:var(--mono);font-size:13px}
button{font:600 14px var(--body);padding:8px 14px;border-radius:6px;border:1px solid var(--accent);background:var(--accent);color:var(--surface);cursor:pointer}
button.secondary{background:transparent;color:var(--accent)}
button.danger{border-color:var(--pass);background:transparent;color:var(--pass)}
button:focus-visible,input:focus-visible,textarea:focus-visible,select:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.msg{padding:10px 14px;border-radius:8px;background:var(--accent-soft);border:1px solid var(--accent)}
.msg.err{background:var(--pass-bg);border-color:var(--pass)}
.mail{border:1px solid var(--line);border-radius:8px;padding:12px;background:var(--bg);display:grid;gap:6px}
.mail pre{white-space:pre-wrap;margin:0;font:13px/1.5 var(--mono)}
.row2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:10px}
.timeline{font-size:13px;display:grid;gap:4px}
"""


# ------------------------------------------------------------------ helpers

def _secret() -> bytes:
    return (os.environ.get("SESSION_SECRET") or os.environ.get("APP_PASSCODE") or "dev").encode()


def _token() -> str:
    return hmac.new(_secret(), b"aic-desk", hashlib.sha256).hexdigest()


def authed(req: Request) -> bool:
    if not os.environ.get("APP_PASSCODE"):
        return True  # local development
    return hmac.compare_digest(req.cookies.get("aic") or "", _token())


def now() -> dt.datetime:
    off = (storage.read_json(CLOCK, {}) or {}).get("offset_days", 0)
    return flow.now_ist() + dt.timedelta(days=off)


def back(url: str, msg: str = "", err: bool = False) -> RedirectResponse:
    sep = "&" if "?" in url else "?"
    q = f"{sep}{'err' if err else 'msg'}={quote(msg)}" if msg else ""
    return RedirectResponse(url + q, status_code=303)


def items() -> dict:
    batch = load_json(BATCH)
    decisions = storage.read_json(DATA / "decisions.json", {}) or {}
    out = {}
    for it in batch["items"]:
        it["decision"] = decisions.get(it["dossier"]["slug"])
        out[it["dossier"]["slug"]] = it
    return out


def state() -> dict:
    return flow.load_state()


def page(title: str, body: str, req: Request) -> HTMLResponse:
    msg = req.query_params.get("msg")
    err = req.query_params.get("err")
    note = (f'<div class="msg">{e(msg)}</div>' if msg else "") + (f'<div class="msg err">{e(err)}</div>' if err else "")
    off = (storage.read_json(CLOCK, {}) or {}).get("offset_days", 0)
    clock = f" · demo clock +{off} days" if off else ""
    login = ('<form method="post" action="/logout" class="inline"><button class="secondary">Sign out</button></form>'
             if authed(req) and os.environ.get("APP_PASSCODE") else
             ("" if authed(req) else '<a href="/login">Sign in to act</a>'))
    nav = (f'<nav class="top"><a href="/">Pipeline</a><a href="/report">Review pack</a><a href="/writeup">Write-up</a>'
           f'<a href="/demo">Demo transcript</a><span class="spacer"></span>'
           f'<span class="muted mono">{e(now().strftime("%a %d %b %Y, %H:%M IST"))}{e(clock)}</span>{login}</nav>')
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap">
<style>{CSS}{WEB_CSS}</style></head><body><div class="wrap">{nav}{note}{body}</div></body></html>"""
    return HTMLResponse(html)


def need_auth(req: Request, slug: str = "") -> RedirectResponse | None:
    if authed(req):
        return None
    return back("/login" + (f"?next=/c/{slug}" if slug else ""), "Sign in with the desk passcode to take actions.", True)


# ------------------------------------------------------------------ pages

@app.get("/", response_class=HTMLResponse)
def home(req: Request):
    its, st = items(), state()["apps"]
    counts = {}
    for s in st.values():
        counts[s["stage"]] = counts.get(s["stage"], 0) + 1
    board = "".join(
        f'<div class="box{" auto" if stages is None else ""}"><span>{e(name)}</span>'
        + (f'<b>{len(its)}</b><span>done for all</span>' if stages is None else f'<b>{sum(counts.get(x, 0) for x in stages)}</b>')
        + "</div>" for name, stages in BOARD)

    def sort_key(slug):
        stage = st.get(slug, {}).get("stage")
        return (ORDER.index(stage) if stage in ORDER else 99, -its[slug]["verdict"]["revealed"]["score_10"])

    rows = []
    for slug in sorted(its, key=sort_key):
        it, a = its[slug], st.get(slug, {})
        v = it["verdict"]
        label, cls = REC[v["recommendation"]]
        stage = a.get("stage") or "–"
        nxt = NEXT.get(stage, "").split(":")[0]
        rows.append(
            f"<tr><td><a href='/c/{e(slug)}'><b>{e(it['dossier']['company'])}</b></a><div class='muted'>{e(it['dossier']['one_liner'])}</div></td>"
            f"<td><span class='pill {cls}'>{label}</span></td><td class='num'>{v['revealed']['score_10']}</td>"
            f"<td><b>{e(STAGE_LABEL.get(stage, stage))}</b><div class='muted'>{e(nxt)}</div></td></tr>")
    actions = ("" if not authed(req) else
               '<div class="row2"><form method="post" action="/agent" class="inline"><button>Run booking agent now</button>'
               '<span class="muted">It also runs every morning by itself.</span></form>'
               '<form method="post" action="/clock" class="inline"><label>Demo clock: days ahead '
               '<input type="number" name="offset_days" min="0" max="60" value="'
               f'{(storage.read_json(CLOCK, {}) or {}).get("offset_days", 0)}" style="width:6em"></label>'
               '<button class="secondary">Set</button></form></div>')
    body = f"""
<header><div class="eyebrow">All In Capital · intake desk · MESA T2 Case 03 prototype</div>
<h1>The pipeline, application by application</h1>
<p class="lede">Each application moves along the whiteboard: rubric, collect, score and recommend run automatically; the final decision and the draft email wait for a person; the booking agent handles replies.</p>
<p class="prov">Applicants and past memos are case-study material; this is not a document of All In Capital. Emails go to an outbox inside this app (no real mail is sent) and founder replies are simulated on each company's page.</p></header>
<section><h2>Where everyone is</h2><div class="board">{board}</div>{actions}</section>
<section><div class="scroll"><table><thead><tr><th>Company</th><th>Suggestion</th><th>Revealed</th><th>Stage · next</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table></div></section>
{_admin(req)}"""
    return page("All In Capital Intake Desk", body, req)


def _admin(req: Request) -> str:
    if not authed(req):
        return ""
    return ('<section><details><summary>Reset the demo</summary><form method="post" action="/reset" class="inline" style="margin-top:8px">'
            '<span class="muted">Puts every application back at Recommendation and clears decisions, emails, bookings, '
            'corrections added here and the demo clock.</span><button class="danger">Reset everything</button></form></details></section>')


def _mails(slug: str) -> str:
    out = []
    keys = [k for k in storage.list_keys(emailer.OUTBOX / slug) if k.endswith(".eml")]
    for k in keys:
        m = email.message_from_string(storage.read_text(k) or "", policy=email.policy.default)
        part = m.get_body(preferencelist=("plain",))
        att = [p.get_filename() for p in m.iter_attachments()]
        out.append(f'<div class="mail"><div class="muted mono">{e(k.rsplit("/", 1)[-1])} · to {e(m["To"] or "")} · {e(m["Date"] or "")}'
                   f'{" · attachment: " + e(", ".join(att)) if att else ""}</div><b>{e(m["Subject"] or "")}</b>'
                   f'<pre>{e(part.get_content() if part else "")}</pre></div>')
    return "".join(out) or '<p class="muted">No emails yet.</p>'


def _people(name: str = "by", default: str = "Kushal") -> str:
    return (f'<label>Who is acting<select name="{name}">'
            + "".join(f'<option{" selected" if p == default else ""}>{p}</option>' for p in PEOPLE) + "</select></label>")


def _actions(slug: str, a: dict, it: dict, req: Request) -> str:
    stage = a.get("stage")
    if not authed(req):
        return f'<p>Next step: <b>{e(NEXT.get(stage, "").split(":")[0])}</b>. <a href="/login?next=/c/{e(slug)}">Sign in</a> to act.</p>'
    rec = it["verdict"]["recommendation"]
    if stage in ("RECOMMENDED", "DECIDED_GO", "DECIDED_NO_GO", "DECIDED_HOLD") and stage != "EMAIL_SENT":
        expected = flow.EXPECTED[rec]
        decide = f"""<form method="post" action="/c/{e(slug)}/decide">
<h3>Final decision</h3>
<p class="muted">System suggests <b>{e(REC[rec][0])}</b>. If you decide differently, give a one-line reason: it is saved as a correction that later scoring uses on similar companies.</p>
<div class="row2">{_people()}<label>Decision<select name="decision">
{''.join(f'<option value="{d}"{" selected" if d == expected else ""}>{lbl}</option>' for d, lbl in (("go", "Go: take the call"), ("no_go", "No-go"), ("hold", "Hold")))}
</select></label></div>
<label>Reason (required if it overrides the suggestion)<input type="text" name="reason" placeholder="Written so it can be reused on similar companies"></label>
<div><button>Record decision</button></div></form>"""
    else:
        decide = ""
    found = flow._founder(slug)[1] or ""
    if stage == "DECIDED_GO":
        return decide + f"""<form method="post" action="/c/{e(slug)}/draft"><h3>Draft the invite</h3>
<label>Founder email<input type="email" name="to" value="{e(a.get('founder_email') or found)}" required placeholder="founder@company.com"></label>
<div><button>Draft email</button></div></form>"""
    if stage == "DECIDED_NO_GO":
        return decide + f"""<form method="post" action="/c/{e(slug)}/draft"><h3>Optional: tell the founder why</h3>
<input type="hidden" name="pass_note" value="1">
<label>Founder email<input type="email" name="to" value="{e(a.get('founder_email') or found)}" required></label>
<div><button class="secondary">Draft a pass note</button></div></form>"""
    if stage in ("RECOMMENDED", "DECIDED_HOLD"):
        return decide
    if stage == "EMAIL_DRAFTED":
        d = a["drafts"][-1]
        notes = "".join(f"<li>{e(n)}</li>" for n in d.get("style_notes", []))
        return f"""<form method="post" action="/c/{e(slug)}/review"><h3>Review the draft (human in the loop)</h3>
{('<p class="muted">Notes from earlier reviews:</p><ul>' + notes + '</ul>') if notes else ''}
<div class="row2">{_people(default="Riya")}<label>To<input type="text" value="{e(a.get('founder_email') or '')}" disabled></label></div>
<label>Subject<input type="text" name="subject" value="{e(d['subject'])}"></label>
<label>Body<textarea name="body">{e(d['body'])}</textarea></label>
<label>Note for future drafts (optional)<input type="text" name="note" placeholder="e.g. open warmer, name the company"></label>
<label style="display:flex;gap:8px;align-items:center;font-weight:500"><input type="checkbox" name="save_template" value="1"> Use my edited version as the template for future drafts</label>
<div class="inline" style="display:flex;gap:8px"><button name="action" value="approve">Approve</button><button name="action" value="reject" class="danger">Reject and redraft</button></div></form>"""
    if stage == "EMAIL_APPROVED":
        return f"""<form method="post" action="/c/{e(slug)}/send" class="inline"><h3 style="width:100%">Send</h3>
<button>Send email</button><span class="muted">Goes to this app's outbox; no real mail is sent from the demo.</span></form>"""
    if stage in flow.AWAITING_REPLY:
        offered = "".join(f"<li>{e(emailer.human_slot(x))}</li>" for x in a.get("offered_slots", []))
        return f"""<h3>Waiting for the founder</h3><p>Offered:</p><ul>{offered}</ul>
<form method="post" action="/c/{e(slug)}/reply"><label>Simulate the founder's reply (demo: no real inbox is connected)
<textarea name="text" style="min-height:90px" placeholder="e.g. Option 2 works for us / We're travelling next week, other times? / Not interested right now"></textarea></label>
<div class="inline" style="display:flex;gap:8px;flex-wrap:wrap"><button>Deliver reply and run the booking agent</button></div></form>
<p class="muted">No reply? The agent follows up after {flow.config()['follow_up_after_days']} days (move the demo clock on the Pipeline page, then run the agent).</p>"""
    if stage == "NEEDS_HUMAN":
        return f"""<form method="post" action="/c/{e(slug)}/resolve"><h3>The reply was unclear: what did the founder mean?</h3>
<p class="muted">{e((a.get('replies') or [{}])[-1].get('text', ''))}</p>
<div class="row2">{_people(default="Riya")}<label>Meaning<select name="intent"><option value="yes">Yes: book the first offered slot</option>
<option value="reschedule">Wants other times</option><option value="no">No</option></select></label></div><div><button>Resolve</button></div></form>"""
    if stage == "MEETING_BOOKED":
        b = a.get("booking", {})
        return f'<h3>Meeting booked</h3><p><b>{e(emailer.human_slot(b.get("slot", "")))}</b> with {e(", ".join(b.get("attendees", [])))}.</p>'
    return f"<h3>{e(STAGE_LABEL.get(stage, stage or ''))}</h3>"


@app.get("/c/{slug}", response_class=HTMLResponse)
def company(slug: str, req: Request):
    its = items()
    if slug not in its:
        return page("Not found", "<h1>No such application</h1>", req)
    it, a = its[slug], state()["apps"].get(slug, {})
    hist = "".join(f"<div><span class='mono'>{e(h['at'][:16].replace('T', ' '))}</span> · <b>{e(STAGE_LABEL.get(h['stage'], h['stage']))}</b>"
                   f" · {e(h['by'])} · <span class='muted'>{e(h['detail'])}</span></div>" for h in a.get("history", []))
    replies = "".join(f"<div class='mail'><div class='muted mono'>{e(r['at'])} · read as <b>{e(r['intent'])}</b> ({e(r['method'])}): {e(r['reason'])}</div><pre>{e(r['text'])}</pre></div>"
                      for r in a.get("replies", []))
    body = f"""
<div class="panel"><div class="eyebrow">{e(it['dossier']['company'])} · stage: {e(STAGE_LABEL.get(a.get('stage'), a.get('stage') or ''))}</div>
{_actions(slug, a, it, req)}</div>
<section><h2>Emails</h2>{_mails(slug)}{('<h3>Founder replies</h3>' + replies) if replies else ''}</section>
<section><h2>History</h2><div class="timeline">{hist or '<span class="muted">None yet.</span>'}</div></section>
{_company(it, load_thesis(), a)}"""
    return page(f"{it['dossier']['company']} · Intake Desk", body, req)


@app.get("/report", response_class=HTMLResponse)
def report(req: Request):
    batch = load_json(BATCH)
    decisions = storage.read_json(DATA / "decisions.json", {}) or {}
    for it in batch["items"]:
        it["decision"] = decisions.get(it["dossier"]["slug"])
    nav = '<nav class="top"><a href="/">← Pipeline</a></nav>'
    return HTMLResponse("<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>"
                        + render_html(batch, nav).replace("<title>", "<title>", 1) + "</html>")


@app.get("/writeup", response_class=HTMLResponse)
def writeup(req: Request):
    text = (ROOT / "docs" / "WRITEUP.md").read_text(encoding="utf-8")
    return page("Intake Desk Write-up", f'<div class="mail"><pre>{e(text)}</pre></div>', req)


@app.get("/demo", response_class=HTMLResponse)
def demo(req: Request):
    p = ROOT / "runs" / "demo" / "transcript.txt"
    text = p.read_text(encoding="utf-8") if p.exists() else "No demo transcript in this deployment."
    return page("Pipeline Demo Transcript", f'<div class="mail"><pre>{e(text)}</pre></div>', req)


# ------------------------------------------------------------------ actions

def _act(req: Request, slug: str, fn):
    if (r := need_auth(req, slug)):
        return r
    try:
        msg = fn()
        return back(f"/c/{slug}", msg)
    except flow.StageError as ex:
        return back(f"/c/{slug}", f"Not allowed: {ex}", True)


@app.post("/c/{slug}/decide")
def decide(slug: str, req: Request, decision: str = Form(...), by: str = Form(...), reason: str = Form("")):
    def run():
        d = flow.final_decision(slug, decision, by, reason, None, now())
        return f"Decision recorded: {decision}" + (f". Saved as correction {d['correction_id']}." if d.get("correction_id") else ".")
    return _act(req, slug, run)


@app.post("/c/{slug}/draft")
def draft(slug: str, req: Request, to: str = Form(""), pass_note: str = Form("")):
    return _act(req, slug, lambda: (flow.draft_email(slug, now(), pass_note=bool(pass_note), to=to.strip() or None),
                                    "Draft ready for review.")[1])


@app.post("/c/{slug}/review")
def review(slug: str, req: Request, by: str = Form(...), subject: str = Form(""), body: str = Form(""),
           note: str = Form(""), save_template: str = Form(""), action: str = Form("approve")):
    def run():
        a = state()["apps"][slug]
        d = a["drafts"][-1] if a.get("drafts") else {}
        subj = subject if subject and subject != d.get("subject") else None
        bod = body.replace("\r\n", "\n") if body and body.replace("\r\n", "\n") != d.get("body") else None
        r = flow.review_draft(slug, by, action == "approve", subj, bod, note, bool(save_template), now())
        return f"Draft {r['status']}" + (" and saved as the template." if r.get("feedback", {}).get("saved_as_template") else ".")
    return _act(req, slug, run)


@app.post("/c/{slug}/send")
def send(slug: str, req: Request):
    return _act(req, slug, lambda: f"Sent to {flow.send_email(slug, now())['to']} (outbox).")


@app.post("/c/{slug}/reply")
def reply(slug: str, req: Request, text: str = Form(...)):
    def run():
        prefix = emailer.INBOX / slug
        n = len(storage.list_keys(prefix)) + 1
        storage.write_text(prefix / f"{now().strftime('%Y%m%d%H%M%S')}_{n:02d}.txt", text)
        acts = flow.booking_agent(now(), [slug])
        if not acts:
            return "Reply stored; the agent had nothing to do."
        return f"Booking agent read the reply as '{acts[0]['reply']}' and moved the application to {STAGE_LABEL.get(acts[0]['stage'])}."
    return _act(req, slug, run)


@app.post("/c/{slug}/resolve")
def resolve(slug: str, req: Request, intent: str = Form(...), by: str = Form(...)):
    return _act(req, slug, lambda: f"Resolved as {intent}: {flow.resolve(slug, intent, by, None, now())['stage']}.")


@app.post("/agent")
def run_agent(req: Request):
    if (r := need_auth(req)):
        return r
    acts = flow.booking_agent(now())
    return back("/", f"Booking agent ran: {len(acts)} application(s) changed." if acts else "Booking agent ran: nothing to do.")


@app.get("/api/cron/agent")
def cron(req: Request):
    secret = os.environ.get("CRON_SECRET")
    if not secret or req.headers.get("authorization") != f"Bearer {secret}":
        return JSONResponse({"ok": False}, status_code=401)
    return {"ok": True, "actions": flow.booking_agent(now())}


@app.post("/clock")
def clock(req: Request, offset_days: int = Form(0)):
    if (r := need_auth(req)):
        return r
    storage.write_json(CLOCK, {"offset_days": max(0, min(60, offset_days))})
    return back("/", f"Demo clock set to {offset_days} days ahead.")


@app.post("/reset")
def reset(req: Request):
    if (r := need_auth(req)):
        return r
    s = storage.store()
    if s.name == "postgres":
        s.delete_prefix("")
        return back("/", "Reset: every application is back at Recommendation.")
    return back("/", "Reset only works on the deployed database; locally, use git to restore data/.", True)


@app.get("/login", response_class=HTMLResponse)
def login_form(req: Request):
    nxt = req.query_params.get("next", "/")
    body = f"""<section style="max-width:420px"><h1>Sign in to act</h1>
<p class="muted">Anyone with the link can read. Decisions, emails and bookings need the desk passcode.</p>
<form method="post" action="/login"><input type="hidden" name="next" value="{e(nxt)}">
<label>Passcode<input type="password" name="passcode" autocomplete="current-password" required></label><div><button>Sign in</button></div></form></section>"""
    return page("Sign In · Intake Desk", body, req)


@app.post("/login")
def login(req: Request, passcode: str = Form(...), next: str = Form("/")):
    target = next if next.startswith("/") and not next.startswith("//") else "/"
    if not hmac.compare_digest(passcode, os.environ.get("APP_PASSCODE", "")):
        return back("/login", "Wrong passcode.", True)
    r = back(target, "Signed in.")
    https = req.headers.get("x-forwarded-proto", req.url.scheme) == "https"
    r.set_cookie("aic", _token(), httponly=True, secure=https, samesite="lax", max_age=60 * 60 * 24 * 14)
    return r


@app.post("/logout")
def logout():
    r = back("/", "Signed out.")
    r.delete_cookie("aic")
    return r


@app.get("/healthz", response_class=PlainTextResponse)
def health():
    return f"ok · storage={storage.store().name}"
