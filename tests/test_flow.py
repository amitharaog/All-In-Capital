"""End-to-end tests of the whiteboard pipeline, run through the real CLI on a
sandbox copy of the repo (TRIAGE_ROOT) with a simulated clock."""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from triage.replies import read_rules

REPO = Path(__file__).resolve().parent.parent
T0 = "2026-11-19T10:00:00+05:30"


@pytest.fixture()
def sandbox(tmp_path):
    for d in ("data", "prompts"):
        shutil.copytree(REPO / d, tmp_path / d, ignore=shutil.ignore_patterns("pipeline", "_packets"))
    for f in ("decisions.json",):
        (tmp_path / "data" / f).unlink(missing_ok=True)

    def cli(*args, now=T0, ok=True):
        env = {**os.environ, "TRIAGE_ROOT": str(tmp_path), "ANTHROPIC_API_KEY": "", "ANTHROPIC_AUTH_TOKEN": ""}
        r = subprocess.run([sys.executable, "-m", "triage", "--now", now, *args], cwd=REPO, env=env,
                           capture_output=True, text=True)
        if ok:
            assert r.returncode == 0, r.stderr + r.stdout
        return r

    def state():
        return json.loads((tmp_path / "data" / "pipeline" / "state.json").read_text())

    def reply(slug, text):
        d = tmp_path / "data" / "pipeline" / "inbox" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{len(list(d.glob('*'))) + 1:02d}.txt").write_text(text)

    cli("rubric")
    for s in ("pumpwise", "grainkind", "capilot", "settlr"):
        cli("collect", s, "--no-scrape")
        cli("score", s)
        cli("recommend", s)
    return type("S", (), {"cli": staticmethod(cli), "state": staticmethod(state), "reply": staticmethod(reply),
                          "root": tmp_path})


def test_cannot_skip_the_human_steps(sandbox):
    assert sandbox.cli("draft", "pumpwise", ok=False).returncode != 0          # no decision yet
    sandbox.cli("decide", "pumpwise", "go", "--by", "Kushal")
    sandbox.cli("draft", "pumpwise", "--to", "founder@example.invalid")
    assert sandbox.cli("send", "pumpwise", ok=False).returncode != 0           # draft not reviewed


def test_override_needs_a_reason_and_becomes_a_correction(sandbox):
    assert sandbox.cli("decide", "grainkind", "go", "--by", "Kushal", ok=False).returncode != 0
    sandbox.cli("decide", "grainkind", "go", "--by", "Kushal", "--reason",
                "Different shelf from Taakat and MomsMade; both portfolio founders told and fine with it")
    st = sandbox.state()["apps"]["grainkind"]
    assert st["decision"]["override"] and st["decision"]["correction_id"]
    lines = (sandbox.root / "data" / "fund" / "corrections.jsonl").read_text().splitlines()
    last = json.loads(lines[-1])
    assert "decision_override" in last["applies_when"] and "consumer_brand" in last["applies_when"]


def test_yes_reply_books_the_meeting_and_blocks_the_calendar(sandbox):
    s = sandbox
    s.cli("decide", "pumpwise", "go", "--by", "Kushal")
    s.cli("draft", "pumpwise", "--to", "founder@example.invalid")
    s.cli("review", "pumpwise", "--by", "Riya")
    s.cli("send", "pumpwise")
    offered = s.state()["apps"]["pumpwise"]["offered_slots"]
    assert len(offered) == 3
    s.reply("pumpwise", "Option 2 works for us, thanks!\n\nOn Thu, Riya wrote:\n> Hi Karthik")
    s.cli("agent", now="2026-11-19T12:00:00+05:30")
    app = s.state()["apps"]["pumpwise"]
    assert app["stage"] == "MEETING_BOOKED" and app["booking"]["slot"] == offered[1]
    assert "Aditya" in app["booking"]["attendees"]  # deeptech
    cal = json.loads((s.root / "data" / "fund" / "calendar.json").read_text())
    assert any(b["start"] == offered[1] for b in cal["busy"])
    emls = sorted((s.root / "runs" / "outbox" / "pumpwise").glob("*.eml"))
    assert [p.name.split("_", 1)[1] for p in emls] == ["invite.eml", "confirmation.eml"]
    assert "text/calendar" in emls[-1].read_text()


def test_no_reply_follows_up_then_closes(sandbox):
    s = sandbox
    s.cli("decide", "pumpwise", "go", "--by", "Kushal")
    s.cli("draft", "pumpwise", "--to", "founder@example.invalid")
    s.cli("review", "pumpwise", "--by", "Riya")
    s.cli("send", "pumpwise")
    s.cli("agent", now="2026-11-21T10:00:00+05:30")                 # 2 days: nothing yet
    assert s.state()["apps"]["pumpwise"]["stage"] == "EMAIL_SENT"
    s.cli("agent", now="2026-11-22T10:00:00+05:30")                 # 3 days: follow-up 1
    s.cli("agent", now="2026-11-25T11:00:00+05:30")                 # follow-up 2
    s.cli("agent", now="2026-11-28T12:00:00+05:30")                 # closed
    app = s.state()["apps"]["pumpwise"]
    assert app["follow_ups"] == 2 and app["stage"] == "CLOSED_NO_REPLY"
    assert [e["kind"] for e in app["emails"]] == ["invite", "followup", "followup"]


def test_draft_needs_a_founder_address(sandbox):
    sandbox.cli("decide", "pumpwise", "go", "--by", "Kushal")
    r = sandbox.cli("draft", "pumpwise", ok=False)
    assert r.returncode != 0 and "--to" in (r.stderr + r.stdout)


def test_reschedule_offers_new_slots_after_the_blocked_week_and_tells_riya(sandbox):
    s = sandbox
    s.cli("decide", "pumpwise", "go", "--by", "Kushal")
    s.cli("draft", "pumpwise", "--to", "founder@example.invalid")
    s.cli("review", "pumpwise", "--by", "Riya")
    s.cli("send", "pumpwise")
    first = set(s.state()["apps"]["pumpwise"]["offered_slots"])
    s.reply("pumpwise", "We're at a trade show all of next week, could we do another time?")
    s.cli("agent", now="2026-11-19T15:00:00+05:30")
    new = s.state()["apps"]["pumpwise"]["offered_slots"]
    assert new and not (set(new) & first)
    assert all(x >= "2026-11-30" for x in new)  # week of 23 Nov skipped
    assert list((s.root / "runs" / "outbox" / "_team").glob("*.eml"))


def test_reschedule_then_no(sandbox):
    s = sandbox
    s.cli("decide", "capilot", "go", "--by", "Kushal", "--reason", "Vertical AI for CA firms; founder lived the problem")
    s.cli("draft", "capilot", "--to", "founder@example.invalid")
    s.cli("review", "capilot", "--by", "Riya")
    s.cli("send", "capilot")
    first = s.state()["apps"]["capilot"]["offered_slots"]
    s.reply("capilot", "None of these work, I'm travelling. Can we do another time?")
    s.cli("agent", now="2026-11-19T15:00:00+05:30")
    app = s.state()["apps"]["capilot"]
    assert app["stage"] == "RESCHEDULING" and app["emails"][-1]["kind"] == "reschedule"
    s.reply("capilot", "Actually we've already closed our round, so not right now. Thanks!")
    s.cli("agent", now="2026-11-20T10:00:00+05:30")
    assert s.state()["apps"]["capilot"]["stage"] == "DECLINED"
    assert first  # slots were offered before the reschedule


def test_unclear_reply_goes_to_a_person(sandbox):
    s = sandbox
    s.cli("decide", "pumpwise", "go", "--by", "Kushal")
    s.cli("draft", "pumpwise", "--to", "founder@example.invalid")
    s.cli("review", "pumpwise", "--by", "Riya")
    s.cli("send", "pumpwise")
    s.reply("pumpwise", "Can you share who else from the fund will join and what we should prepare?")
    s.cli("agent", now="2026-11-19T12:00:00+05:30")
    assert s.state()["apps"]["pumpwise"]["stage"] == "NEEDS_HUMAN"
    s.cli("resolve", "pumpwise", "yes", "--by", "Riya", now="2026-11-19T13:00:00+05:30")
    assert s.state()["apps"]["pumpwise"]["stage"] == "MEETING_BOOKED"


def test_draft_edit_becomes_the_next_template(sandbox):
    s = sandbox
    s.cli("decide", "pumpwise", "go", "--by", "Kushal")
    s.cli("draft", "pumpwise", "--to", "founder@example.invalid")
    d = s.state()["apps"]["pumpwise"]["drafts"][-1]
    edited = d["body"].replace("Thanks for applying to All In Capital.", "Loved reading the Pumpwise deck.")
    f = s.root / "edited.txt"
    f.write_text(edited)
    s.cli("review", "pumpwise", "--by", "Kushal", "--body-file", str(f), "--note", "open warmer, name the company",
          "--save-template")
    s.cli("decide", "capilot", "go", "--by", "Kushal", "--reason", "vertical AI")
    s.cli("draft", "capilot", "--to", "founder@example.invalid")
    body = s.state()["apps"]["capilot"]["drafts"][-1]["body"]
    assert "Loved reading the CAPilot deck." in body and "Pumpwise" not in body
    assert s.state()["apps"]["capilot"]["drafts"][-1]["style_notes"] == ["open warmer, name the company"]


def test_two_founders_are_never_offered_the_same_slot(sandbox):
    s = sandbox
    for slug, reason in (("pumpwise", ""), ("capilot", "vertical AI")):
        s.cli("decide", slug, "go", "--by", "Kushal", *(["--reason", reason] if reason else []))
        s.cli("draft", slug, "--to", "founder@example.invalid")
    a = set(s.state()["apps"]["pumpwise"]["offered_slots"])
    b = set(s.state()["apps"]["capilot"]["offered_slots"])
    assert a and b and not (a & b)


def test_pass_note_branch(sandbox):
    s = sandbox
    s.cli("decide", "settlr", "no_go", "--by", "Kushal")
    s.cli("draft", "settlr", "--pass-note", "--to", "founder@example.invalid")
    s.cli("review", "settlr", "--by", "Riya")
    s.cli("send", "settlr")
    assert s.state()["apps"]["settlr"]["stage"] == "CLOSED"


# ------------------------------------------------------------- reply reader

OFFERED = ["2026-11-24T14:30:00+05:30", "2026-11-26T15:00:00+05:30", "2026-12-01T16:00:00+05:30"]


@pytest.mark.parametrize("text,intent,slot", [
    ("Thursday 3pm works for us", "yes", OFFERED[1]),
    ("Option 3 please", "yes", OFFERED[2]),
    ("Yes, happy to chat!", "yes", OFFERED[0]),
    ("Tuesday 2:30 is perfect", "yes", OFFERED[0]),
    ("Thanks, but we're not interested at this stage.", "no", None),
    ("None of those work, can we do next week?", "reschedule", None),
    ("What's the fund's typical cheque size?", "unclear", None),
])
def test_reply_reader(text, intent, slot):
    r = read_rules(text, OFFERED)
    assert r.intent == intent and r.slot == slot
