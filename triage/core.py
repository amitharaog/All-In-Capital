"""Paths, loading helpers and the deterministic verdict engine.

The LLM never produces a total or a recommendation. It scores criteria with
evidence; this module turns that into numbers and a routing suggestion using
rules a partner can read in data/fund/thesis.json.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .schemas import CriterionScore, LensResult, ResearchDossier, ScoreCard, Verdict

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
APPS = DATA / "applications"
RESEARCH = DATA / "research"
SCORES = DATA / "scores"
FUND = DATA / "fund"
PROMPTS = ROOT / "prompts"
RUNS = ROOT / "runs"


def load_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if hasattr(obj, "model_dump"):
        obj = obj.model_dump(mode="json")
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_thesis() -> dict:
    return load_json(FUND / "thesis.json")


def list_slugs() -> list[str]:
    return sorted(p.name for p in APPS.iterdir() if p.is_dir())


def load_dossier(slug: str) -> ResearchDossier:
    return ResearchDossier.model_validate(load_json(RESEARCH / f"{slug}.json"))


def load_scorecard(slug: str) -> ScoreCard:
    return ScoreCard.model_validate(load_json(SCORES / f"{slug}.json"))


# --------------------------------------------------------------------------
# Aggregation
# --------------------------------------------------------------------------

def aggregate_lens(lens_id: str, scores: list[CriterionScore], thesis: dict) -> LensResult:
    lens = thesis["lenses"][lens_id]
    by_id = {s.criterion_id: s for s in scores}
    missing_value = float(thesis["missing_value"])
    total_w = sum(c["weight"] for c in lens["criteria"])
    acc = 0.0
    covered = 0.0
    breakdown = []
    for c in lens["criteria"]:
        s = by_id.get(c["id"])
        if s is None or s.status == "not_evidenced" or s.score is None:
            value, status = missing_value, "not_evidenced"
        else:
            value, status = float(s.score), s.status
            covered += c["weight"] * (1.0 if s.status == "evidenced" else 0.5)
        acc += c["weight"] * value
        breakdown.append(
            {
                "id": c["id"],
                "name": c["name"],
                "weight": c["weight"],
                "score_5": round(value, 2),
                "status": status,
                "counted_as_missing": status == "not_evidenced",
            }
        )
    score_10 = round(acc / total_w * 2, 2)
    return LensResult(
        lens=lens_id, score_10=score_10, coverage=round(covered / total_w, 2), breakdown=breakdown
    )


def decide(dossier: ResearchDossier, card: ScoreCard, thesis: dict | None = None,
           conflict_hits: list[dict] | None = None) -> Verdict:
    thesis = thesis or load_thesis()
    revealed = aggregate_lens("revealed", card.criteria, thesis)
    stated = aggregate_lens("stated", card.criteria, thesis)
    routing = thesis["routing"]
    gates = {g.gate_id: g for g in card.gates}
    flags: list[str] = []

    conflict_hits = conflict_hits or []
    conflict = (gates.get("G1") and gates["G1"].triggered) or any(
        h["level"] in ("high", "medium") for h in conflict_hits
    )
    regulatory = bool(gates.get("G2") and gates["G2"].triggered)
    mandate = bool(gates.get("G4") and gates["G4"].triggered)
    if gates.get("G3") and gates["G3"].triggered:
        flags.append("G3 sector-label stretch: " + gates["G3"].detail)
    for h in conflict_hits:
        flags.append(f"Portfolio overlap ({h['level']}): {h['portfolio_company']} - {h['why']}")

    missing = [b["name"] for b in revealed.breakdown if b["counted_as_missing"]]
    if missing:
        flags.append("No evidence (scored as missing, drags score): " + ", ".join(missing))

    if conflict:
        rec = "HOLD_CONFLICT"
        headline = "Hold: possible overlap with a portfolio company. Kushal to speak to the portfolio founder first."
    elif regulatory:
        rec = "PASS"
        headline = "Suggest pass on category: the business depends on a favourable rule change (G2)."
    elif mandate:
        rec = "PASS"
        headline = "Suggest pass on mandate: the round or stage is outside what the fund leads (G4). Not a judgement on the company."
    elif revealed.score_10 >= routing["take_call"]["revealed_min"] and revealed.coverage >= routing["take_call"]["coverage_min"]:
        rec = "TAKE_CALL"
        headline = f"Take the call: {revealed.score_10}/10 on the fund's revealed thesis with {int(revealed.coverage*100)}% evidence coverage."
    elif revealed.score_10 >= routing["screen_first"]["revealed_min"]:
        rec = "SCREEN_FIRST"
        if revealed.coverage < routing["take_call"]["coverage_min"]:
            headline = f"Screen first: {revealed.score_10}/10 but only {int(revealed.coverage*100)}% of the thesis is evidenced - ask the founder for the missing numbers before a partner call."
        else:
            headline = f"Screen first: {revealed.score_10}/10 - borderline; Riya to run a short first screen."
    else:
        rec = "PASS"
        headline = f"Suggest pass: {revealed.score_10}/10 on the revealed thesis."
        r1 = next((c for c in card.criteria if c.criterion_id == "R1"), None)
        founder_seen = r1 is not None and r1.status == "evidenced" and r1.confidence in ("medium", "high")
        if routing.get("pass_requires_founder_evidence", False) and not founder_seen:
            rec = "SCREEN_FIRST"
            headline = (f"Low score ({revealed.score_10}/10) but founder behaviour is not observable from the application, "
                        "so it is not a pass yet: Riya to screen before anything is decided.")
            flags.append("Pass withheld: R1 not evidenced with confidence (rule v2, from the backtest).")

    lens_gap = round(revealed.score_10 - stated.score_10, 2)
    lens_note = None
    if abs(lens_gap) >= 1.5:
        higher = "revealed (what the fund does)" if lens_gap > 0 else "stated (what the fund says)"
        lens_note = (
            f"Lenses disagree by {abs(lens_gap)} points; it scores higher on the {higher} thesis. "
            "Recommendation uses the revealed lens."
        )

    attendees = routing["deeptech_attendees"] if dossier.sector == "deeptech" else routing["default_attendees"]
    if dossier.sector == "deeptech":
        flags.append("Deeptech: Aditya joins the call and runs the second call himself.")

    return Verdict(
        slug=dossier.slug,
        company=dossier.company,
        recommendation=rec,
        headline=headline,
        revealed=revealed,
        stated=stated,
        lens_disagreement=lens_note,
        flags=flags,
        call_attendees=list(attendees),
    )
