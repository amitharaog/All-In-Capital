"""DEMO: walk the whole whiteboard pipeline end to end on a sandbox copy.

Nothing here is a real partner decision or a real founder reply. The demo copies
data/ and prompts/ into a temporary folder (TRIAGE_ROOT), plays the partners
and three founders with a simulated clock, and writes a transcript plus every
email the system produced to runs/demo/. The real pipeline state is untouched.

  python scripts/demo_pipeline.py
"""
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "runs" / "demo"
log: list[str] = []


def main() -> None:
    box = Path(tempfile.mkdtemp(prefix="triage-demo-"))
    for d in ("data", "prompts"):
        shutil.copytree(REPO / d, box / d, ignore=shutil.ignore_patterns("pipeline", "_packets"))
    (box / "data" / "decisions.json").unlink(missing_ok=True)
    env = {**os.environ, "TRIAGE_ROOT": str(box), "ANTHROPIC_API_KEY": "", "ANTHROPIC_AUTH_TOKEN": ""}

    def cli(*args, now):
        log.append(f"\n$ python -m triage --now {now} {' '.join(args)}")
        r = subprocess.run([sys.executable, "-m", "triage", "--now", now, *args], cwd=REPO, env=env,
                           capture_output=True, text=True)
        log.append((r.stdout + r.stderr).rstrip())
        if r.returncode:
            raise SystemExit("\n".join(log))
        return r.stdout

    def state():
        return json.loads((box / "data" / "pipeline" / "state.json").read_text())

    def founder_replies(slug, text):
        d = box / "data" / "pipeline" / "inbox" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{len(list(d.glob('*'))) + 1:02d}.txt").write_text(text)
        log.append(f"\n[founder of {slug} replies] {text}")

    def say(text):
        log.append(f"\n## {text}")

    t = "2026-11-19T10:00:00+05:30"
    say("1-4. Define Rubrics, Collect Info, Score the Startup, Recommendation (whole pile)")
    cli("run", "--no-scrape", now=t)

    say("5. Final Decision (human). DEMO choices: Pumpwise go (agrees), GrainKind go (overrides the hold), "
        "CAPilot go (screen-first), Talkbook hold (agrees), Settlr no-go (agrees)")
    cli("decide", "pumpwise", "go", "--by", "Kushal (demo)", now=t)
    cli("decide", "grainkind", "go", "--by", "Kushal (demo)", "--reason",
        "Different shelf from Taakat and MomsMade; both portfolio founders told and fine with it", now=t)
    cli("decide", "capilot", "go", "--by", "Kushal (demo)", "--reason",
        "Vertical AI for CA firms built by a practising CA; worth a call despite the deck's overstatements", now=t)
    cli("decide", "talkbook", "hold", "--by", "Kushal (demo)", now=t)
    cli("decide", "settlr", "no_go", "--by", "Kushal (demo)", now=t)

    say("6-8. Draft Email -> HITL -> Send Email. Riya edits the first draft and saves it as the template (feedback loop 2)")
    cli("draft", "pumpwise", "--to", "karthik@pumpwise.example", now=t)
    draft = state()["apps"]["pumpwise"]["drafts"][-1]
    edited = draft["body"].replace("Thanks for applying to All In Capital.",
                                   "Thanks for applying to All In Capital. We enjoyed reading about Pumpwise.")
    edit_file = box / "edited.txt"
    edit_file.write_text(edited)
    cli("review", "pumpwise", "--by", "Riya (demo)", "--body-file", str(edit_file), "--note",
        "mention the company by name in the first line", "--save-template", now=t)
    cli("send", "pumpwise", now=t)
    for slug in ("grainkind", "capilot"):
        cli("draft", slug, "--to", f"founders@{slug}.example", now=t)  # starts from Riya's edited template
        cli("review", slug, "--by", "Riya (demo)", now=t)
        cli("send", slug, now=t)
    cli("draft", "settlr", "--pass-note", "--to", "rahul@settlr.example", now=t)
    cli("review", "settlr", "--by", "Riya (demo)", now=t)
    cli("send", "settlr", now=t)

    say("9. Meeting Booking Agent reads replies")
    s = state()["apps"]
    pw = dt.datetime.fromisoformat(s["pumpwise"]["offered_slots"][1])
    founder_replies("pumpwise", f"Hi Riya, {pw.strftime('%A')} {pw.strftime('%I:%M %p').lstrip('0').lower()} works for "
                                "both of us. Looking forward to it.\n\nOn Thu, Riya wrote:\n> Hi Karthik")
    founder_replies("grainkind", "Thanks! We're at a trade show all of next week. Could we do another time?")
    cli("agent", now="2026-11-19T14:00:00+05:30")
    founder_replies("grainkind", "Option 2 works.")
    cli("agent", now="2026-11-20T09:00:00+05:30")

    say("No reply from CAPilot: follow up after 3 days, twice, then close")
    for when in ("2026-11-22T10:00:00+05:30", "2026-11-25T10:30:00+05:30", "2026-11-28T11:00:00+05:30"):
        cli("agent", now=when)

    say("Final status")
    cli("status", now="2026-11-28T11:00:00+05:30")

    say("Feedback loop 1: each override is now a correction future scoring retrieves")
    log.extend(line for line in (box / "data" / "fund" / "corrections.jsonl").read_text().splitlines()
            if "decision_override" in line)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(box / "runs" / "outbox", OUT / "outbox")
    shutil.copy(box / "data" / "pipeline" / "state.json", OUT / "state.json")
    (OUT / "transcript.txt").write_text(
        "DEMO of the full pipeline on a sandbox copy. Partner decisions and founder replies are simulated.\n"
        + "\n".join(log) + "\n")
    shutil.rmtree(box)
    print("\n".join(log))
    print(f"\nwrote {OUT}/transcript.txt, state.json and outbox/")


if __name__ == "__main__":
    main()
