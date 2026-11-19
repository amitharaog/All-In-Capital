"""Render a batch into a single self-contained HTML review pack for partners."""
from __future__ import annotations

import datetime as dt
from html import escape as e
from pathlib import Path

from .core import DATA, FUND, RUNS, load_json, load_thesis

REC = {
    "HOLD_CONFLICT": ("Hold: conflict", "hold"),
    "TAKE_CALL": ("Take the call", "call"),
    "SCREEN_FIRST": ("Screen first", "screen"),
    "PASS": ("Suggest pass", "pass"),
}

CSS = """
/* Layout: an investment-committee review pack. Summary strip -> queue table -> one dossier per company -> backtest -> trust contract. */
:root{
  --bg:#f5f7f6; --surface:#ffffff; --ink:#14201c; --muted:#5b6b65; --line:#d9e1dd; --accent:#0d6b57; --accent-soft:#e3f1ec;
  --call:#1f7a4d; --call-bg:#e2f3e9; --screen:#9a6400; --screen-bg:#fbf0d9; --hold:#6b3fa0; --hold-bg:#efe7f8;
  --pass:#8a3b32; --pass-bg:#f8e6e3; --miss:#b4442f;
  --display:"Bricolage Grotesque","Inter",system-ui,sans-serif; --body:"Inter",system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0f1513; --surface:#161f1c; --ink:#e3ebe7; --muted:#97a8a1; --line:#2a3833; --accent:#5cc7a8; --accent-soft:#183029;
  --call:#6fd29d; --call-bg:#173022; --screen:#e8b552; --screen-bg:#33270f; --hold:#c3a2ec; --hold-bg:#2a2038;
  --pass:#ef9a8c; --pass-bg:#3a1f1b; --miss:#f08c74; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0f1513; --surface:#161f1c; --ink:#e3ebe7; --muted:#97a8a1; --line:#2a3833; --accent:#5cc7a8; --accent-soft:#183029;
  --call:#6fd29d; --call-bg:#173022; --screen:#e8b552; --screen-bg:#33270f; --hold:#c3a2ec; --hold-bg:#2a2038;
  --pass:#ef9a8c; --pass-bg:#3a1f1b; --miss:#f08c74; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:15px/1.55 var(--body);margin:0}
.wrap{max-width:1120px;margin:0 auto;padding-block:28px 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:36px}
h1,h2,h3{font-family:var(--display);text-wrap:balance;margin:0;letter-spacing:-.01em}
h1{font-size:clamp(26px,4vw,36px);font-weight:700}
h2{font-size:22px;font-weight:650}
h3{font-size:17px;font-weight:650}
p{margin:0;max-width:72ch}
a{color:var(--accent)}
a:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.eyebrow{font:600 11px/1 var(--body);letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
.muted{color:var(--muted)}
.mono,td.num{font-family:var(--mono);font-variant-numeric:tabular-nums}
header{display:grid;gap:10px}
.wrap > *, .company > *, section > *{min-width:0}
li{overflow-wrap:anywhere}
.prov{font-size:13px;color:var(--muted);border-left:3px solid var(--line);padding-left:12px}
.strip{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.tile{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px 16px;display:grid;gap:4px}
.tile b{font:700 26px/1.1 var(--display)}
.pill{display:inline-block;font:600 12px/1 var(--body);padding:5px 9px;border-radius:999px;white-space:nowrap}
.pill.call{color:var(--call);background:var(--call-bg)} .pill.screen{color:var(--screen);background:var(--screen-bg)}
.pill.hold{color:var(--hold);background:var(--hold-bg)} .pill.pass{color:var(--pass);background:var(--pass-bg)}
.scroll{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{font:600 11px/1.2 var(--body);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:var(--bg)}
tr:last-child td{border-bottom:0}
.bar{height:6px;border-radius:3px;background:var(--line);min-width:70px;position:relative;overflow:hidden}
.bar i{position:absolute;inset:0 auto 0 0;background:var(--accent);border-radius:3px}
.company{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:22px clamp(16px,3vw,28px);display:grid;gap:18px;scroll-margin-top:16px}
.company-head{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:baseline;justify-content:space-between}
.company-head > div{min-width:0}
.scores{display:flex;gap:18px;flex-wrap:wrap}
.score{display:grid;gap:2px}
.score b{font:700 22px/1 var(--mono)}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:18px}
.grid2 > div{min-width:0;display:grid;gap:8px;align-content:start}
ul{margin:0;padding-left:18px;display:grid;gap:5px}
.flag{border-left:3px solid var(--screen);padding:6px 10px;background:var(--screen-bg);border-radius:0 6px 6px 0;font-size:14px}
.flag.hold{border-color:var(--hold);background:var(--hold-bg)}
.missing{color:var(--miss);font-weight:600}
.src{font:500 11px/1 var(--mono);color:var(--accent);background:var(--accent-soft);padding:2px 5px;border-radius:4px;margin-left:3px;text-decoration:none;white-space:nowrap}
details{border-top:1px solid var(--line);padding-top:10px}
summary{cursor:pointer;font-weight:600;color:var(--muted)}
.srclist{font-size:13px;display:grid;gap:6px;margin-top:8px}
.srclist div{overflow-wrap:anywhere}
.contradicted{color:var(--pass);font-weight:600}
.dots{display:inline-flex;gap:3px;vertical-align:middle}
.dots span{width:9px;height:9px;border-radius:2px;background:var(--line)}
.dots span.on{background:var(--accent)}
.dots span.half{background:linear-gradient(90deg,var(--accent) 50%,var(--line) 50%)}
section{display:grid;gap:14px}
.lede{font-size:16px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""


def _dots(score) -> str:
    if score is None:
        return '<span class="missing">missing</span>'
    cells = []
    for i in range(1, 6):
        cls = "on" if score >= i else ("half" if score >= i - 0.5 else "")
        cells.append(f'<span class="{cls}"></span>')
    return f'<span class="dots" aria-label="{score} of 5">{"".join(cells)}</span> <span class="mono">{score:g}</span>'


def _srcs(ids, slug) -> str:
    return "".join(f'<a class="src" href="#{e(slug)}-{e(i)}">{e(i)}</a>' for i in ids)


NEXT = {
    "RECOMMENDED": "Waiting for Kushal: python -m triage decide {slug} go|no_go|hold --by Kushal",
    "DECIDED_GO": "Draft the invite: python -m triage draft {slug}",
    "DECIDED_NO_GO": "Closed. Optional pass note: python -m triage draft {slug} --pass-note",
    "DECIDED_HOLD": "On hold until Kushal speaks to the portfolio founder",
    "EMAIL_DRAFTED": "Riya reviews the draft: python -m triage review {slug} --by Riya",
    "EMAIL_APPROVED": "Send: python -m triage send {slug}",
    "EMAIL_SENT": "Booking agent is waiting for the founder's reply",
    "FOLLOWED_UP": "Booking agent sent a follow-up and is waiting",
    "RESCHEDULING": "Booking agent offered new times and is waiting",
    "NEEDS_HUMAN": "Reply was unclear: python -m triage resolve {slug} yes|no|reschedule --by Riya",
    "MEETING_BOOKED": "Meeting booked",
    "DECLINED": "Founder declined",
    "CLOSED_NO_REPLY": "Closed: no reply after follow-ups",
    "CLOSED": "Closed",
}
STAGE_LABEL = {k: k.replace("_", " ").capitalize() for k in NEXT}


def _pipeline_state() -> dict:
    p = DATA / "pipeline" / "state.json"
    return load_json(p)["apps"] if p.exists() else {}


def _pipeline_line(slug: str, app: dict | None) -> str:
    if not app or not app.get("stage"):
        return ""
    stage = app["stage"]
    nxt = NEXT.get(stage, "").format(slug=slug)
    steps = " → ".join(f"{e(h['stage'].replace('_', ' ').lower())}" for h in app["history"][-6:])
    booking = app.get("booking")
    extra = f" · booked {e(booking['slot'][:16].replace('T', ' '))}" if booking else ""
    return (f'<p class="prov"><b>Pipeline:</b> {e(STAGE_LABEL.get(stage, stage))}{extra}. Next: <span class="mono">{e(nxt)}</span>'
            f'<br><span class="muted">History: {steps}</span></p>')


def _company(item: dict, thesis: dict, app: dict | None = None) -> str:
    d, card, v = item["dossier"], item["card"], item["verdict"]
    slug = d["slug"]
    label, cls = REC[v["recommendation"]]
    crit_by = {c["criterion_id"]: c for c in card["criteria"]}
    rows = []
    for lens_id in ("revealed", "stated"):
        for c in thesis["lenses"][lens_id]["criteria"]:
            cs = crit_by.get(c["id"], {})
            ev = "".join(
                f"<li>{e(x['text'])}{_srcs(x['source_ids'], slug)}"
                + (' <span class="contradicted">contradicted</span>' if x.get("status") == "contradicted" else "")
                + "</li>"
                for x in cs.get("evidence", [])
            )
            prec = "".join(f'<span class="src">{e(p)}</span>' for p in cs.get("precedents_applied", []))
            rows.append(
                f"<tr><td class='mono'>{c['id']}</td><td><b>{e(c['name'])}</b><div class='muted'>weight {c['weight']}</div></td>"
                f"<td>{_dots(cs.get('score'))}<div class='muted'>{e(cs.get('confidence', ''))} confidence</div></td>"
                f"<td>{e(cs.get('rationale', 'not scored'))} {prec}{'<ul>'+ev+'</ul>' if ev else ''}</td></tr>"
            )
    flags = "".join(f'<div class="flag">{e(f)}</div>' for f in v["flags"] if not f.startswith("Portfolio overlap"))
    conf = "".join(
        f'<div class="flag hold"><b>Portfolio overlap ({e(h["level"])}): {e(h["portfolio_company"])}</b> — {e(h["why"])}. '
        f'{e(h.get("portfolio_one_line", ""))}'
        + (f' <a href="{e(h["source_url"])}" target="_blank" rel="noopener">source</a>' if h.get("source_url") else "")
        + "</div>"
        for h in item["conflicts"]
    )
    gates = "".join(
        f"<li><b>{e(g['gate_id'])}</b> {'triggered' if g['triggered'] else 'clear'}: {e(g['detail'])}{_srcs(g.get('source_ids', []), slug)}</li>"
        for g in card["gates"]
    )
    gaps = "".join(
        f"<li><b>{e(g['what'])}</b> — {e(g['why_it_matters'])}"
        + (f"<div class='muted'>Searched: {e('; '.join(g['searched']))}</div>" if g.get("searched") else "")
        + (f"<div>Ask: <i>{e(g['ask_founder'])}</i></div>" if g.get("ask_founder") else "")
        + "</li>"
        for g in d["gaps"]
    )
    contradictions = [c for c in d["claims"] if c["status"] == "contradicted"]
    contra = "".join(f"<li>{e(c['text'])}{_srcs(c['source_ids'], slug)}" + (f"<div class='muted'>{e(c['note'])}</div>" if c.get('note') else "") + "</li>" for c in contradictions)
    founders = "".join(
        f"<li><b>{e(f['name'])}</b>{', ' + e(f['role']) if f.get('role') else ''}: "
        f"{e(f.get('background_claimed') or '')} <span class='muted'>— public footprint: {e(f['public_footprint'].replace('_', ' '))}"
        f"{'; ' + e(f['background_verified']) if f.get('background_verified') else ''}</span>{_srcs(f.get('source_ids', []), slug)}</li>"
        for f in d["founders"]
    )
    sources = "".join(
        f'<div id="{e(slug)}-{e(s["id"])}"><span class="src">{e(s["id"])}</span> {e(s["kind"])} · {e(s["title"])}'
        + (f' · {e(s["locator"])}' if s.get("locator") else "")
        + (f' · <a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["url"])}</a>' if s.get("url") else "")
        + (f' · retrieved {e(s["retrieved_on"])}' if s.get("retrieved_on") else "")
        + (f'<div class="muted">“{e(s["quote"])}”</div>' if s.get("quote") else "")
        + "</div>"
        for s in d["sources"]
    )
    a = item["audit"]
    audit = (
        f"{a['claims_with_sources']}/{a['claims']} claims sourced · deck/form quotes verified "
        f"{a['doc_quotes']['verified']}/{a['doc_quotes']['checked']} · {a['web_sources']} web sources"
        + ("" if a["pass"] else f" · <span class='missing'>{len(a['problems'])} audit problems</span>")
    )
    decision = item.get("decision")
    dec_html = (
        f"<span class='pill {'call' if decision['decision']=='call' else 'hold' if decision['decision']=='hold' else 'pass' if decision['decision']=='pass' else 'screen'}'>"
        f"Partner decision: {e(decision['decision'])} · {e(decision['by'])}</span>"
        if decision else "<span class='muted'>Awaiting Kushal's decision</span>"
    )
    precedents = "".join(
        f"<li><span class='src'>{e(p['correction']['id'])}</span> {e(p['correction']['reason'])} <span class='muted'>(matched on {e(', '.join(p['matched_on']))})</span></li>"
        for p in item["precedents"]
    )
    return f"""
<article class="company" id="{e(slug)}">
  <div class="company-head">
    <div><div class="eyebrow">{e(d['sector'].replace('_', ' '))} · {e(d['sub_sector'])} · {e(d['stage'])}{' · ask ' + e(d['ask']) if d.get('ask') else ''}</div>
      <h2>{e(d['company'])}</h2><p class="muted">{e(d['one_liner'])}</p></div>
    <div style="display:grid;gap:8px;justify-items:start"><span class="pill {cls}">{label}</span>{dec_html}</div>
  </div>
  <p class="lede">{e(v['headline'])}</p>
  {_pipeline_line(slug, app)}
  <div class="scores">
    <div class="score"><span class="eyebrow">Revealed thesis</span><b>{v['revealed']['score_10']}</b><span class="muted">/10 · {int(v['revealed']['coverage']*100)}% evidenced</span></div>
    <div class="score"><span class="eyebrow">Stated thesis</span><b>{v['stated']['score_10']}</b><span class="muted">/10 · {int(v['stated']['coverage']*100)}% evidenced</span></div>
    <div class="score"><span class="eyebrow">Call with</span><b style="font-size:16px">{e(', '.join(v['call_attendees']))}</b></div>
  </div>
  {('<p class="muted">' + e(v['lens_disagreement']) + '</p>') if v.get('lens_disagreement') else ''}
  {conf}{flags}
  <div class="grid2">
    <div><h3>Case for</h3><ul>{''.join('<li>'+e(x)+'</li>' for x in card['case_for'])}</ul></div>
    <div><h3>Case against</h3><ul>{''.join('<li>'+e(x)+'</li>' for x in card['case_against'])}</ul></div>
  </div>
  <div class="scroll"><table><thead><tr><th>#</th><th>Criterion</th><th>Score</th><th>Why, with sources</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
  <div class="grid2">
    <div><h3>What it couldn't find out</h3><ul>{gaps or '<li>No gaps recorded.</li>'}</ul></div>
    <div><h3>Questions for the call</h3><ul>{''.join('<li>'+e(q)+'</li>' for q in card['call_questions'])}</ul>
      {('<h3>Deck vs form contradictions</h3><ul>' + contra + '</ul>') if contra else ''}</div>
  </div>
  <div class="grid2">
    <div><h3>Founders</h3><ul>{founders}</ul></div>
    <div><h3>Gates</h3><ul>{gates}</ul>
      <h3>Partner corrections consulted</h3><ul>{precedents or '<li>None matched.</li>'}</ul></div>
  </div>
  {('<p><b>If we pass, what would change our view:</b> ' + e(card['what_would_change_our_view']) + '</p>') if card.get('what_would_change_our_view') else ''}
  <details><summary>Sources ({len(d['sources'])}) · {audit}</summary><div class="srclist">{sources}</div></details>
</article>"""


def _backtest() -> str:
    path = DATA / "backtest" / "results.json"
    if not path.exists():
        return ""
    res = load_json(path)
    full = res["variants"].get("full")
    nof = res["variants"].get("no_founder")
    if not full or not full["n"]:
        return ""
    adj = {a["company"]: a for a in res.get("adjudication", {}).get("cases", [])} if res.get("adjudication") else {}
    rows = []
    nof_rows = {r["company"]: r for r in (nof or {}).get("rows", [])}
    for r in full["rows"]:
        nr = nof_rows.get(r["company"])
        a = adj.get(r["company"])
        label, cls = REC[r["system"]]
        rows.append(
            f"<tr><td class='num'>{r['memo']}</td><td><b>{e(r['company'])}</b></td><td>{e(r['fund'].title())}</td>"
            f"<td><span class='pill {cls}'>{label}</span></td><td class='num'>{r['revealed']}</td><td class='num'>{r['stated']}</td>"
            f"<td class='num'>{nr['revealed'] if nr else '–'}</td>"
            f"<td>{'agrees' if r['agree'] else '<span class=missing>disagrees</span>'}</td>"
            f"<td>{e(a['verdict']) + ': ' + e(a['reasoning']) if a else ''}</td></tr>"
        )
    summary = res.get("adjudication", {}).get("summary", "")
    def pct(x):
        return f"{int(round(x*100))}%" if x is not None else "–"
    nof_line = (
        f"Without the partners' founder assessment (deck-level information only) agreement drops to "
        f"<b>{nof['agreement']}/{nof['n']}</b> ({pct(nof['agreement_rate'])}). That gap is how much of the fund's decision lives in the call, and it is where this system stops being reliable."
        if nof and nof["n"] else ""
    )
    return f"""
<section id="backtest">
  <div class="eyebrow">Backtest · the fund's 12 past decisions</div>
  <h2>How often it disagrees with us</h2>
  <p>Each memo was re-scored with the decision and the “Why we…” paragraph withheld. The system “agrees” when it says
  <i>Take the call</i> on a company the fund invested in, or anything else on a company it passed on.</p>
  <div class="strip">
    <div class="tile"><span class="eyebrow">Agreement, revealed lens</span><b>{full['agreement']}/{full['n']}</b><span class="muted">{pct(full['agreement_rate'])} · 95% CI {full['agreement_ci95'][0]}–{full['agreement_ci95'][1]} · in-sample</span></div>
    <div class="tile"><span class="eyebrow">Agreement, stated lens</span><b>{full['stated_lens_agreement']}/{full['n']}</b><span class="muted">{pct(full['stated_lens_rate'])} · public wording only</span></div>
    <div class="tile"><span class="eyebrow">Missed investments</span><b>{len(full['missed_investments'])}</b><span class="muted">{e(', '.join(full['missed_investments']) or 'none')}</span></div>
    <div class="tile"><span class="eyebrow">Passes it would advance</span><b>{len(full['would_have_advanced_passes'])}</b><span class="muted">{e(', '.join(full['would_have_advanced_passes']) or 'none')}</span></div>
  </div>
  <p>{nof_line}</p>
  <p>Mean revealed score: invested <b class="mono">{full['mean_revealed_invested']}</b> vs passed <b class="mono">{full['mean_revealed_passed']}</b>.
  Mean stated score: invested <b class="mono">{full['mean_stated_invested']}</b> vs passed <b class="mono">{full['mean_stated_passed']}</b>.</p>
  {('<p>' + e(summary) + '</p>') if summary else ''}
  <div class="scroll"><table><thead><tr><th>Memo</th><th>Company</th><th>Fund</th><th>System</th><th>Revealed</th><th>Stated</th><th>No-founder</th><th>Result</th><th>Who was wrong</th></tr></thead>
  <tbody>{''.join(rows)}</tbody></table></div>
</section>"""


def _trust() -> str:
    path = FUND / "trust_contract.json"
    if not path.exists():
        return ""
    t = load_json(path)
    rows = "".join(
        f"<tr><td><b>{e(m['metric'])}</b><div class='muted'>{e(m['how'])}</div></td><td class='num'>{e(m['threshold'])}</td>"
        f"<td class='num'>{e(m.get('current', '–'))}</td><td>{e(m['if_breached'])}</td></tr>"
        for m in t["metrics"]
    )
    breaks = "".join(f"<li><b>{e(b['where'])}</b> — {e(b['why'])} <span class='muted'>Mitigation: {e(b['mitigation'])}</span></li>" for b in t["where_it_breaks"])
    return f"""
<section id="trust">
  <div class="eyebrow">Trust contract · agreed before it touches a real decision</div>
  <h2>How far to trust it, and where it breaks</h2>
  <p>{e(t['summary'])}</p>
  {('<p class="flag hold"><b>Status:</b> ' + e(t['status']) + '</p>') if t.get('status') else ''}
  <div class="scroll"><table><thead><tr><th>What we measure</th><th>Threshold</th><th>Now</th><th>If breached</th></tr></thead><tbody>{rows}</tbody></table></div>
  <h3>Where it breaks</h3><ul>{breaks}</ul>
</section>"""


def render(batch: dict, out: Path | None = None) -> Path:
    thesis = load_thesis()
    items = batch["items"]
    counts = {k: sum(1 for i in items if i["verdict"]["recommendation"] == k) for k in REC}
    gaps = sum(len(i["dossier"]["gaps"]) for i in items)
    claims = sum(i["audit"]["claims"] for i in items)
    sourced = sum(i["audit"]["claims_with_sources"] for i in items)
    qv = sum(i["audit"]["doc_quotes"]["verified"] for i in items)
    qc = sum(i["audit"]["doc_quotes"]["checked"] for i in items)
    web = sum(i["audit"]["web_sources"] for i in items)
    wc_path = DATA / "research" / "_web_quote_check.json"
    wc = load_json(wc_path) if wc_path.exists() else None
    web_line = (f"{wc['summary']['verified'] + wc['summary']['wording_only']}/{wc['summary']['total']} web quotes re-found on the live page; "
                f"{wc['summary']['unverifiable']} blocked or JS-rendered (check by hand)") if wc else f"{web} web sources"
    pstate = _pipeline_state()
    queue = "".join(
        f"<tr><td><a href='#{e(i['dossier']['slug'])}'><b>{e(i['dossier']['company'])}</b></a><div class='muted'>{e(i['dossier']['one_liner'])}</div></td>"
        f"<td><span class='pill {REC[i['verdict']['recommendation']][1]}'>{REC[i['verdict']['recommendation']][0]}</span></td>"
        f"<td class='num'>{i['verdict']['revealed']['score_10']}</td><td class='num'>{i['verdict']['stated']['score_10']}</td>"
        f"<td><div class='bar'><i style='width:{int(i['verdict']['revealed']['coverage']*100)}%'></i></div><span class='muted mono'>{int(i['verdict']['revealed']['coverage']*100)}%</span></td>"
        f"<td class='num'>{len(i['dossier']['gaps'])}</td><td>{e(i['dossier']['sector'].replace('_',' '))}</td>"
        f"<td>{e(STAGE_LABEL.get((pstate.get(i['dossier']['slug']) or {}).get('stage') or '', '–'))}</td></tr>"
        for i in items
    )
    provenance = "; ".join(batch.get("produced_by", []))
    html = f"""<title>All In Capital Intake Desk</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header>
  <div class="eyebrow">All In Capital · intake week · thesis {e(batch['thesis_version'])} · generated {e(batch['generated'][:16].replace('T', ' '))}</div>
  <h1>{len(items)} applications, scored against the fund's thesis</h1>
  <p class="lede">Every score names the thesis criterion it is scored against and the source behind each claim. Gaps are listed, not filled in.
  Nothing here is decided: every outcome waits for Kushal.</p>
  <p class="prov"><b>MESA T2 Case 03 prototype.</b> Applicants and past memos are case-study material; this is not a document of All In Capital.</p>
  <p class="prov">Scores use the <b>revealed</b> thesis (what the fund's past decisions reward) for the recommendation and show the <b>stated</b> thesis (public wording) beside it.
  Provenance: {e(provenance)}.</p>
</header>
<div class="strip">
  <div class="tile"><span class="eyebrow">Take the call</span><b>{counts['TAKE_CALL']}</b><span class="muted">Slot held once approved</span></div>
  <div class="tile"><span class="eyebrow">Screen first</span><b>{counts['SCREEN_FIRST']}</b><span class="muted">Missing numbers to request</span></div>
  <div class="tile"><span class="eyebrow">Hold: conflict</span><b>{counts['HOLD_CONFLICT']}</b><span class="muted">Portfolio overlap</span></div>
  <div class="tile"><span class="eyebrow">Suggest pass</span><b>{counts['PASS']}</b><span class="muted">With what would change our view</span></div>
  <div class="tile"><span class="eyebrow">Claims sourced</span><b>{sourced}/{claims}</b><span class="muted">{qv}/{qc} deck/form quotes verified · {web_line}</span></div>
  <div class="tile"><span class="eyebrow">Gaps named</span><b>{gaps}</b><span class="muted">Each with the question to ask</span></div>
</div>
<section>
  <h2>Review queue</h2>
  <div class="scroll"><table><thead><tr><th>Company</th><th>Suggestion</th><th>Revealed</th><th>Stated</th><th>Evidence</th><th>Gaps</th><th>Sector</th><th>Stage</th></tr></thead><tbody>{queue}</tbody></table></div>
</section>
{''.join(_company(i, thesis, pstate.get(i['dossier']['slug'])) for i in items)}
{_backtest()}
{_trust()}
</div>
"""
    out = out or RUNS / dt.date.today().isoformat() / "report.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out
