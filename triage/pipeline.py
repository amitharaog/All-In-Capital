"""Batch orchestration: a week of intake in, one partner review pack out."""
from __future__ import annotations

import datetime as dt
import os

from . import citations, conflicts, corrections
from .core import DATA, FUND, RESEARCH, RUNS, SCORES, decide, dump_json, list_slugs, load_json, load_thesis
from .schemas import ResearchDossier, ScoreCard

DECISIONS = DATA / "decisions.json"
OVERRIDES = FUND / "overrides.json"


def api_available() -> bool:
    return bool(os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"))


def ensure_dossier(slug: str, refresh: bool = False) -> ResearchDossier:
    path = RESEARCH / f"{slug}.json"
    if path.exists() and not refresh:
        return ResearchDossier.model_validate(load_json(path))
    if not api_available():
        raise SystemExit(f"No dossier for {slug} and no Anthropic credential to research it.")
    from . import llm

    d = llm.research(slug, dt.date.today().isoformat())
    dump_json(path, d)
    return d


def ensure_card(d: ResearchDossier, refresh: bool = False) -> ScoreCard:
    path = SCORES / f"{d.slug}.json"
    if path.exists() and not refresh:
        return ScoreCard.model_validate(load_json(path))
    if not api_available():
        raise SystemExit(f"No scorecard for {d.slug} and no Anthropic credential to score it.")
    from . import llm

    c = llm.score(d)
    dump_json(path, c)
    return c


def apply_overrides(card: ScoreCard) -> list[dict]:
    """Partner score corrections on *this* company take effect immediately."""
    if not OVERRIDES.exists():
        return []
    applied = []
    for crit_id, o in load_json(OVERRIDES).get(card.slug, {}).items():
        for cs in card.criteria:
            if cs.criterion_id == crit_id:
                applied.append({"criterion": crit_id, "from": cs.score, "to": o["score"], "by": o["by"],
                                "correction": o["correction_id"]})
                cs.score = o["score"]
                cs.status = "evidenced" if o["score"] is not None else "not_evidenced"
                cs.precedents_applied.append(o["correction_id"])
                cs.rationale += f" [Partner override {o['correction_id']}: {o['reason']}]"
    return applied


def run_batch(slugs: list[str] | None = None, refresh: bool = False) -> dict:
    thesis = load_thesis()
    slugs = slugs or list_slugs()
    decisions = load_json(DECISIONS) if DECISIONS.exists() else {}
    items = []
    for slug in slugs:
        d = ensure_dossier(slug, refresh)
        card = ensure_card(d, refresh)
        overrides = apply_overrides(card)
        hits = conflicts.check(d)
        verdict = decide(d, card, thesis, hits)
        items.append({
            "dossier": d.model_dump(mode="json"),
            "card": card.model_dump(mode="json"),
            "verdict": verdict.model_dump(mode="json"),
            "conflicts": hits,
            "precedents": corrections.retrieve(d),
            "overrides": overrides,
            "audit": citations.audit(d, card),
            "decision": decisions.get(slug),
        })
    order = {"HOLD_CONFLICT": 0, "TAKE_CALL": 1, "SCREEN_FIRST": 2, "PASS": 3}
    items.sort(key=lambda i: (order[i["verdict"]["recommendation"]], -i["verdict"]["revealed"]["score_10"]))
    batch = {
        "generated": dt.datetime.now().isoformat(timespec="seconds"),
        "thesis_version": thesis["version"],
        "items": items,
        "produced_by": sorted({i["dossier"]["produced_by"] for i in items} | {i["card"]["produced_by"] for i in items}),
    }
    run_dir = RUNS / dt.date.today().isoformat()
    dump_json(run_dir / "batch.json", batch)
    return batch


def record_decision(slug: str, decision: str, by: str, note: str = "") -> dict:
    decisions = load_json(DECISIONS) if DECISIONS.exists() else {}
    decisions[slug] = {"decision": decision, "by": by, "date": dt.date.today().isoformat(), "note": note}
    dump_json(DECISIONS, decisions)
    return decisions[slug]


def record_correction(slug: str, criterion_id: str | None, new_score: float | None, reason: str, by: str,
                      applies_when: list[str]) -> dict:
    d = ResearchDossier.model_validate(load_json(RESEARCH / f"{slug}.json"))
    card = ScoreCard.model_validate(load_json(SCORES / f"{slug}.json"))
    old = next((c.score for c in card.criteria if c.criterion_id == criterion_id), None)
    tags = sorted(set(applies_when) | (corrections.tags_for(d) if not applies_when else set()))
    c = corrections.add(d.company, reason, by, tags, criterion_id, old, new_score)
    if criterion_id:
        ov = load_json(OVERRIDES) if OVERRIDES.exists() else {}
        ov.setdefault(slug, {})[criterion_id] = {"score": new_score, "by": by, "reason": reason, "correction_id": c.id}
        dump_json(OVERRIDES, ov)
    return c.model_dump()
