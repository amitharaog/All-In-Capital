"""Command line for the intake desk. One command per box on the whiteboard.

  Define Rubrics      python -m triage rubric
  Collect Info        python -m triage collect [slugs] [--no-scrape]     (deck + free sources + scrape)
  Score the Startup   python -m triage score [slugs]
  Recommendation      python -m triage recommend [slugs]
  (all four)          python -m triage run [slugs]                        + review pack in runs/<date>/
  Final Decision      python -m triage decide pumpwise go --by Kushal [--reason "..."]
  Draft Email         python -m triage draft pumpwise [--pass-note]
  HITL on the draft   python -m triage review pumpwise --by Riya [--body-file f.txt] [--note "..."] [--save-template] [--reject]
  Send Email          python -m triage send pumpwise
  Booking Agent       python -m triage agent                              (run on a schedule)
  Unclear reply       python -m triage resolve pumpwise yes|no|reschedule --by Riya [--slot ISO]
  Where is everyone   python -m triage status

  Also: correct, backtest, audit, ingest, report. Every stage command takes --now ISO to simulate the clock.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

from .core import APPS, RUNS, load_json


def _now(args):
    from .flow import IST, now_ist

    if getattr(args, "now", None):
        t = dt.datetime.fromisoformat(args.now)
        return t if t.tzinfo else t.replace(tzinfo=IST)
    return now_ist()


def _slugs(args):
    from .core import list_slugs

    return args.slugs or list_slugs()


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="triage")
    p.add_argument("--now", help="simulated current time (ISO, IST if no offset)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("rubric")
    for name in ("collect", "score", "recommend", "run"):
        sp = sub.add_parser(name)
        sp.add_argument("slugs", nargs="*")
        if name in ("collect", "run"):
            sp.add_argument("--no-scrape", action="store_true")
        if name == "run":
            sp.add_argument("--refresh", action="store_true", help="re-research and re-score (needs API key)")
    d = sub.add_parser("decide")
    d.add_argument("slug")
    d.add_argument("decision", choices=["go", "no_go", "hold"])
    d.add_argument("--by", required=True)
    d.add_argument("--reason", default="")
    d.add_argument("--tags", default="")
    dr = sub.add_parser("draft")
    dr.add_argument("slug")
    dr.add_argument("--pass-note", action="store_true")
    dr.add_argument("--to", help="founder email, if the application doesn't include one")
    rv = sub.add_parser("review")
    rv.add_argument("slug")
    rv.add_argument("--by", required=True)
    rv.add_argument("--reject", action="store_true")
    rv.add_argument("--subject")
    rv.add_argument("--body-file")
    rv.add_argument("--note", default="")
    rv.add_argument("--save-template", action="store_true")
    se = sub.add_parser("send")
    se.add_argument("slug")
    ag = sub.add_parser("agent")
    ag.add_argument("slugs", nargs="*")
    rs = sub.add_parser("resolve")
    rs.add_argument("slug")
    rs.add_argument("intent", choices=["yes", "no", "reschedule"])
    rs.add_argument("--by", required=True)
    rs.add_argument("--slot")
    sub.add_parser("status")
    sub.add_parser("report")
    c = sub.add_parser("correct")
    c.add_argument("slug")
    c.add_argument("criterion", help="criterion id, or '-' for a general correction")
    c.add_argument("score", help="new 0-5 score, or '-'")
    c.add_argument("--by", required=True)
    c.add_argument("--reason", required=True, help="one line, written so it can be reused on similar companies")
    c.add_argument("--tags", default="")
    sub.add_parser("backtest")
    sub.add_parser("audit")
    i = sub.add_parser("ingest")
    i.add_argument("pdf")
    i.add_argument("--slug", required=True)
    i.add_argument("--kind", choices=["deck", "form"], required=True)
    args = p.parse_args(argv)

    from . import flow

    now = _now(args)
    show = lambda x: print(json.dumps(x, indent=2, default=str))  # noqa: E731
    try:
        if args.cmd == "rubric":
            show(flow.define_rubrics(now))
        elif args.cmd == "collect":
            flow.define_rubrics(now)
            for s in _slugs(args):
                show(flow.collect_info(s, now, not args.no_scrape))
        elif args.cmd == "score":
            for s in _slugs(args):
                card = flow.score_startup(s, now)
                print(s, "scored:", len(card.criteria), "criteria")
        elif args.cmd == "recommend":
            for s in _slugs(args):
                r = flow.recommend(s, now)
                print(f"{r['recommendation']:<14} {r['revealed']:>5}  {s}")
        elif args.cmd == "run":
            from .pipeline import run_batch
            from .report import render

            if args.refresh:
                from .pipeline import ensure_card, ensure_dossier

                for s in _slugs(args):
                    ensure_card(ensure_dossier(s, True), True)
            for r in flow.run_automated(args.slugs or None, now, not args.no_scrape):
                print(f"{r.get('recommendation', r.get('skipped')):<14} {r.get('revealed', ''):>5}  {r['slug']}")
            print("review pack:", render(run_batch(args.slugs or None)))
        elif args.cmd == "decide":
            tags = [t.strip() for t in args.tags.split(",") if t.strip()]
            show(flow.final_decision(args.slug, args.decision, args.by, args.reason, tags, now))
        elif args.cmd == "draft":
            dft = flow.draft_email(args.slug, now, pass_note=args.pass_note, to=args.to)
            print(f"Draft v{dft['version']} ({dft['kind']}) for review:\n\nSubject: {dft['subject']}\n\n{dft['body']}")
            if dft["style_notes"]:
                print("Reviewer notes from earlier drafts:", *dft["style_notes"], sep="\n  - ")
        elif args.cmd == "review":
            body = Path(args.body_file).read_text() if args.body_file else None
            dft = flow.review_draft(args.slug, args.by, not args.reject, args.subject, body, args.note,
                                    args.save_template, now)
            print(f"{dft['status']}" + (" (saved as template)" if dft.get("feedback", {}).get("saved_as_template") else ""))
        elif args.cmd == "send":
            show(flow.send_email(args.slug, now))
        elif args.cmd == "agent":
            show(flow.booking_agent(now, args.slugs or None))
        elif args.cmd == "resolve":
            show(flow.resolve(args.slug, args.intent, args.by, args.slot, now))
        elif args.cmd == "status":
            for r in flow.status():
                last = r["last"] or {}
                print(f"{r['slug']:<11} {str(r['stage']):<17} {last.get('at', '')}  {last.get('detail', '')}")
        elif args.cmd == "report":
            from .report import render

            print(render(load_json(sorted(RUNS.glob("*/batch.json"))[-1])))
        elif args.cmd == "correct":
            from .pipeline import record_correction

            score = None if args.score == "-" else float(args.score)
            crit = None if args.criterion == "-" else args.criterion
            tags = [t.strip() for t in args.tags.split(",") if t.strip()]
            show(record_correction(args.slug, crit, score, args.reason, args.by, tags))
        elif args.cmd == "backtest":
            from .backtest import evaluate

            res = evaluate()
            for k, v in res["variants"].items():
                print(k, {x: v[x] for x in ("n", "agreement", "agreement_rate", "agreement_ci95", "stated_lens_rate",
                                            "missed_investments", "investments_marked_pass")})
        elif args.cmd == "audit":
            from .citations import audit
            from .core import list_slugs, load_dossier, load_scorecard

            for s in list_slugs():
                r = audit(load_dossier(s), load_scorecard(s))
                print(s, "PASS" if r["pass"] else "FAIL", r["claims_with_sources"], "/", r["claims"],
                      "doc quotes", r["doc_quotes"], *r["problems"][:3], sep="  ")
        elif args.cmd == "ingest":
            from .ingest import pdf_to_markdown

            out = APPS / args.slug / f"{args.kind}.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(pdf_to_markdown(args.pdf))
            print("wrote", out)
    except flow.StageError as e:
        raise SystemExit(f"Not allowed: {e}")


if __name__ == "__main__":
    main()
