import datetime as dt

from triage import conflicts
from triage.backtest import parse_memos
from triage.citations import quote_in
from triage.core import aggregate_lens, decide, load_thesis
from triage.scheduling import IST, candidate_slots, free_slots
from triage.schemas import Claim, CriterionScore, GateResult, ResearchDossier, ScoreCard

THESIS = load_thesis()


def crit(cid, score, status="evidenced", confidence="medium"):
    return CriterionScore(criterion_id=cid, score=score, status=status, rationale="t", confidence=confidence)


def dossier(**kw):
    base = dict(company="X", slug="x", one_liner="x", sector="fintech", sub_sector="payments", stage="pre-seed",
                business_model="x", founders=[], claims=[], gaps=[], sources=[])
    base.update(kw)
    return ResearchDossier(**base)


def card(scores, gates=()):
    return ScoreCard(slug="x", criteria=scores, gates=list(gates), case_for=[], case_against=[], call_questions=[])


def all_revealed(v):
    return [crit(f"R{i}", v) for i in range(1, 7)] + [crit(f"S{i}", v) for i in range(1, 5)]


def test_perfect_scores_give_ten():
    assert aggregate_lens("revealed", all_revealed(5), THESIS).score_10 == 10.0


def test_missing_evidence_drags_score_and_coverage():
    scores = all_revealed(4)
    scores[2] = crit("R3", None, "not_evidenced")
    r = aggregate_lens("revealed", scores, THESIS)
    full = aggregate_lens("revealed", all_revealed(4), THESIS)
    assert r.score_10 < full.score_10
    assert r.coverage == 0.8
    assert any(b["counted_as_missing"] for b in r.breakdown)


def test_routing_take_call_and_pass():
    assert decide(dossier(), card(all_revealed(4))).recommendation == "TAKE_CALL"
    assert decide(dossier(), card(all_revealed(1.5))).recommendation == "PASS"


def test_low_coverage_cannot_take_call():
    scores = [crit("R1", 5), crit("R2", 5)] + [crit(f"R{i}", None, "not_evidenced") for i in range(3, 7)]
    v = decide(dossier(), card(scores))
    assert v.recommendation != "TAKE_CALL"


def test_conflict_gate_overrides_score():
    g = GateResult(gate_id="G1", triggered=True, detail="overlap")
    assert decide(dossier(), card(all_revealed(5), [g])).recommendation == "HOLD_CONFLICT"


def test_regulatory_gate_suggests_pass():
    g = GateResult(gate_id="G2", triggered=True, detail="needs rule change")
    assert decide(dossier(), card(all_revealed(5), [g])).recommendation == "PASS"


def test_deeptech_brings_aditya():
    v = decide(dossier(sector="deeptech"), card(all_revealed(4)))
    assert "Aditya" in v.call_attendees
    assert "Aditya" not in decide(dossier(), card(all_revealed(4))).call_attendees


def test_every_verdict_needs_partner_review():
    assert decide(dossier(), card(all_revealed(5))).needs_partner_review is True


def test_conflict_check_catches_meeting_notes_without_shared_name():
    d = dossier(one_liner="AI call summaries and CRM auto-fill for sales teams", sub_sector="sales productivity",
                business_model="SaaS seats", keywords=["call summary", "meeting notes", "CRM"])
    pf = [{"name": "MeetRecord", "one_line": "Conversation intelligence: records sales calls and meetings, generates notes and summaries"}]
    hits = conflicts.check(d, pf)
    assert hits and hits[0]["level"] == "medium"  # same job, not named: flag
    d.claims.append(Claim(text="Competitor MeetRecord also does this", source_ids=["W1"]))
    assert conflicts.check(d, pf)[0]["level"] == "high"  # named + same job: hold


def test_conflict_check_quiet_on_unrelated():
    d = dossier(one_liner="Millet breakfast cereal brand", sector="consumer_brand", sub_sector="food",
                business_model="D2C", keywords=["millet", "breakfast", "snack"])
    pf = [{"name": "MeetRecord", "one_line": "records sales calls and meetings, generates notes and summaries"}]
    assert conflicts.check(d, pf) == []


def test_quote_matching_is_strict_but_tolerant_of_formatting():
    doc = "**Traction:** 22 of our 38 retailers have   reordered at least twice."
    assert quote_in("22 of our 38 retailers have reordered at least twice", doc)
    assert not quote_in("40 of our 38 retailers reordered", doc)


def test_slots_are_tuesday_thursday_afternoons():
    slots = candidate_slots(dt.date(2026, 11, 18), cfg={"weekdays": [1, 3], "afternoon_window": ["14:00", "17:30"]})
    assert slots and all(s.weekday() in (1, 3) and 14 <= s.hour <= 17 for s in slots)


def test_busy_blocks_are_respected():
    cfg = {"weekdays": [3], "afternoon_window": ["14:00", "14:30"],
           "busy": [{"who": ["Kushal"], "start": "2026-11-19T14:00:00+05:30", "end": "2026-11-19T15:00:00+05:30"}]}
    free = free_slots(["Kushal"], dt.date(2026, 11, 18), set(), cfg)
    assert dt.datetime(2026, 11, 19, 14, 0, tzinfo=IST) not in free
    assert dt.datetime(2026, 11, 26, 14, 0, tzinfo=IST) in free


def test_memo_parsing_holds_out_decisions():
    memos = parse_memos()
    assert len(memos) == 12
    assert sum(m["decision"] == "INVESTED" for m in memos) == 6
    assert all(m["what"] and m["founder"] and m["risks"] and m["why"] for m in memos)


def test_no_pass_without_founder_evidence():
    scores = all_revealed(1.5)
    scores[0] = crit("R1", 1.5, "partial", "low")
    v = decide(dossier(), card(scores))
    assert v.recommendation == "SCREEN_FIRST"


def test_mandate_gate_suggests_pass_even_for_strong_company():
    g = GateResult(gate_id="G4", triggered=True, detail="Series A, INR 30 Cr")
    assert decide(dossier(), card(all_revealed(5), [g])).recommendation == "PASS"


def test_mandate_beats_conflict():
    gates = [GateResult(gate_id="G1", triggered=True, detail="overlap"),
             GateResult(gate_id="G4", triggered=True, detail="Series A")]
    v = decide(dossier(), card(all_revealed(5), gates))
    assert v.recommendation == "PASS" and any("overlap" in f for f in v.flags)


def test_correction_is_reused_on_a_similar_company(tmp_path, monkeypatch):
    from triage import corrections

    monkeypatch.setattr(corrections, "PATH", tmp_path / "c.jsonl")
    corrections.add("GrainKind", "Repeat above 30% with LTV/CAC under 2x: growth still partly bought; cap R3 at 3.5",
                    "Kushal", ["consumer_brand", "paid_growth"], "R3", 4.0, 3.5)
    from triage.schemas import Gap

    similar = dossier(company="Oatly-ish", sector="consumer_brand", sub_sector="packaged food",
                      claims=[Claim(text="60% of new customers from paid social ads", source_ids=["F1"])],
                      gaps=[Gap(what="No cohort repeat data", why_it_matters="deciding metric for a brand")])
    unrelated = dossier(company="LedgerCo", sector="fintech", sub_sector="accounting",
                        claims=[Claim(text="60% of new customers from paid social ads", source_ids=["F1"])])
    assert [p["correction"]["company"] for p in corrections.retrieve(similar)] == ["GrainKind"]
    assert corrections.retrieve(unrelated) == []
