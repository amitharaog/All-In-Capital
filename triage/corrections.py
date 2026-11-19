"""Correction memory: a partner's correction should count next time, not just once.

Each correction is one line of reasoning plus tags describing when it applies
(sector, business model, situation). Before scoring, the closest precedents
are retrieved and handed to the scorer, which must say which ones it applied.
Retrieval is deliberately simple and inspectable (tag overlap), so Kushal can
see exactly why a precedent was pulled.
"""
from __future__ import annotations

import datetime as dt
import json
import re

from . import storage
from .core import FUND
from .schemas import Correction, ResearchDossier

PATH = FUND / "corrections.jsonl"

# Situation tags inferred from the dossier's gaps/claims, so precedents about
# a *kind of gap* (e.g. missing repeat rate) find new companies with that gap.
SITUATIONS = {
    "missing_repeat_rate": r"repeat|cohort|retention",
    "credentials_heavy": r"phd|iit|iim|ex-|former|alumn",
    "regulatory_dependency": r"regulat|licen|rbi|sebi|dgca|approval|permission",
    "lending_risk": r"default|npa|credit risk|underwrit|collection",
    "paid_growth": r"paid (social|ads|acquisition|marketing|channels?)|performance marketing|cac (is )?rising",
    "founder_dependent": r"influencer|following|audience|personal brand|creator",
    "capital_intensive": r"density|dark store|fleet|capex|inventory|working capital",
}
SECTORS = {"fintech", "deeptech", "consumer_tech", "consumer_brand", "other"}
STOP = {"and", "for", "the", "with", "from", "led", "based", "end", "front"}


def load() -> list[Correction]:
    text = storage.read_text(PATH) or ""
    return [Correction.model_validate_json(line) for line in text.splitlines() if line.strip()]


def add(company: str, reason: str, by: str, applies_when: list[str], criterion_id: str | None = None,
        old_score: float | None = None, new_score: float | None = None) -> Correction:
    existing = load()
    c = Correction(
        id=f"C{len(existing) + 1:03d}",
        date=dt.date.today().isoformat(),
        company=company,
        criterion_id=criterion_id,
        old_score=old_score,
        new_score=new_score,
        by=by,
        reason=reason,
        applies_when=sorted({t.lower() for t in applies_when}),
    )
    storage.append_text(PATH, c.model_dump_json() + "\n")
    return c


def tags_for(dossier: ResearchDossier, conflict_hits: list[dict] | None = None) -> set[str]:
    words = {w for w in re.findall(r"[a-z0-9_]+", dossier.sub_sector.lower()) if len(w) > 2 and w not in STOP}
    tags = {dossier.sector, *words}
    if conflict_hits is None:
        from .conflicts import check

        conflict_hits = check(dossier)
    if any(h["level"] in ("high", "medium") for h in conflict_hits):
        tags.add("portfolio_overlap")
    blob = " ".join([g.what + " " + g.why_it_matters for g in dossier.gaps]).lower()
    blob_all = blob + " " + " ".join(c.text for c in dossier.claims).lower()
    for tag, pattern in SITUATIONS.items():  # situation tags from the evidence
        target = blob if tag == "missing_repeat_rate" else blob_all
        if re.search(pattern, target):
            tags.add(tag)
    return tags


def retrieve(dossier: ResearchDossier, k: int = 5) -> list[dict]:
    """A correction applies when (a) its sector tags include this company's
    sector, or it has none, and (b) at least one non-sector tag matches.
    Portfolio-overlap corrections apply across sectors."""
    tags = tags_for(dossier)
    scored = []
    for c in load():
        ctags = set(c.applies_when)
        sector_tags = ctags & SECTORS
        overlap = tags & ctags
        situational = overlap - SECTORS
        cross_sector = "portfolio_overlap" in situational
        if not situational:
            continue
        if sector_tags and dossier.sector not in sector_tags and not cross_sector:
            continue
        scored.append((len(overlap), c, sorted(overlap)))
    scored.sort(key=lambda x: -x[0])
    return [{"correction": c.model_dump(), "matched_on": m} for _, c, m in scored[:k]]


def as_prompt_block(precedents: list[dict]) -> str:
    if not precedents:
        return "No stored partner corrections match this applicant."
    lines = []
    for p in precedents:
        c = p["correction"]
        crit = f" [{c['criterion_id']}]" if c.get("criterion_id") else ""
        lines.append(f"- {c['id']}{crit} ({c['company']}, by {c['by']}): {c['reason']}  (matched on: {', '.join(p['matched_on'])})")
    return "\n".join(lines)


if __name__ == "__main__":  # pragma: no cover
    print(json.dumps([c.model_dump() for c in load()], indent=2))
