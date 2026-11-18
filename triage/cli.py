"""Command line for the intake desk.

  python -m triage run                      # research + score + verdicts for every application, writes runs/<date>/
  python -m triage report                   # render runs/<date>/report.html from the latest batch
  python -m triage approve talkbook hold --by Kushal --note "speak to MeetRecord founder"
  python -m triage approve pumpwise call --by Kushal
  python -m triage correct grainkind R3 4.0 --by Kushal --reason "..." --tags consumer_brand,d2c
  python -m triage book                     # hold slots + invites + founder emails for approved calls; pass notes
  python -m triage backtest                 # agreement with the fund's 12 past decisions
  python -m triage audit                    # citation audit for every dossier
  python -m triage ingest deck.pdf --slug newco --kind deck
"""
from __future__ import annotations

import argparse
import datetime as dt
import json

from .core import APPS, RUNS, load_json


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="triage")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("slugs", nargs="*")
    r.add_argument("--refresh", action="store_true", help="re-research and re-score (needs API key)")
    sub.add_parser("report")
    a = sub.add_parser("approve")
    a.add_argument("slug")
    a.add_argument("decision", choices=["call", "pass", "hold", "screen"])
    a.add_argument("--by", required=True)
    a.add_argument("--note", default="")
    c = sub.add_parser("correct")
    c.add_argument("slug")
    c.add_argument("criterion", help="criterion id, or '-' for a general correction")
    c.add_argument("score", help="new 0-5 score, or '-'")
    c.add_argument("--by", required=True)
    c.add_argument("--reason", required=True, help="one line, written so it can be reused on similar companies")
    c.add_argument("--tags", default="", help="comma-separated applies-when tags")
    sub.add_parser("book")
    sub.add_parser("backtest")
    sub.add_parser("audit")
    i = sub.add_parser("ingest")
    i.add_argument("pdf")
    i.add_argument("--slug", required=True)
    i.add_argument("--kind", choices=["deck", "form"], required=True)
    args = p.parse_args(argv)

    if args.cmd == "run":
        from .pipeline import run_batch
        from .report import render

        batch = run_batch(args.slugs or None, args.refresh)
        path = render(batch)
        for it in batch["items"]:
            v = it["verdict"]
            print(f"{v['recommendation']:<14} {v['revealed']['score_10']:>5}  {v['company']:<12} {v['headline']}")
        print("report:", path)
    elif args.cmd == "report":
        from .report import render

        latest = sorted(RUNS.glob("*/batch.json"))[-1]
        print(render(load_json(latest)))
    elif args.cmd == "approve":
        from .pipeline import record_decision

        print(json.dumps(record_decision(args.slug, args.decision, args.by, args.note), indent=2))
    elif args.cmd == "correct":
        from .pipeline import record_correction

        score = None if args.score == "-" else float(args.score)
        crit = None if args.criterion == "-" else args.criterion
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]
        print(json.dumps(record_correction(args.slug, crit, score, args.reason, args.by, tags), indent=2))
    elif args.cmd == "book":
        from .booking import book_approved

        print(json.dumps(book_approved(), indent=2))
    elif args.cmd == "backtest":
        from .backtest import evaluate

        res = evaluate()
        for k, v in res["variants"].items():
            print(k, {x: v[x] for x in ("n", "agreement", "agreement_rate", "agreement_ci95", "stated_lens_rate",
                                        "missed_investments", "would_have_advanced_passes")})
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


if __name__ == "__main__":
    main()
