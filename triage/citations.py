"""Citation audit: every claim must point at a source, and every quote taken
from the deck or form must actually appear in it.

This is the mechanical half of 'every claim traceable to its source'. Web
quotes are recorded with URL + retrieval date; `verify_web=True` re-fetches
the page and checks the quote is still there (best effort, needs network).
"""
from __future__ import annotations

import re
from difflib import SequenceMatcher

from .core import APPS
from .schemas import ResearchDossier, ScoreCard


def _norm(s: str) -> str:
    s = s.lower().replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[*_`#>|]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def quote_in(quote: str, text: str) -> bool:
    q, t = _norm(quote), _norm(text)
    if not q:
        return False
    if q in t:
        return True
    # tolerate small transcription differences (ellipses, punctuation)
    parts = [p.strip() for p in re.split(r"\.\.\.|…", q) if len(p.strip()) > 8]
    if parts and all(p in t for p in parts):
        return True
    window = len(q)
    best = 0.0
    for i in range(0, max(1, len(t) - window + 1), max(1, window // 4)):
        best = max(best, SequenceMatcher(None, q, t[i : i + window]).ratio())
        if best > 0.9:
            return True
    return False


def audit(dossier: ResearchDossier, card: ScoreCard | None = None, verify_web: bool = False) -> dict:
    app_dir = APPS / dossier.slug
    docs = {
        "deck": (app_dir / "deck.md").read_text(encoding="utf-8") if (app_dir / "deck.md").exists() else "",
        "form": (app_dir / "form.md").read_text(encoding="utf-8") if (app_dir / "form.md").exists() else "",
    }
    src = {s.id: s for s in dossier.sources}
    problems: list[str] = []
    quote_checks = {"checked": 0, "verified": 0}
    web_checks = {"checked": 0, "verified": 0, "skipped": 0}

    for s in dossier.sources:
        if s.kind in ("deck", "form") and s.quote:
            quote_checks["checked"] += 1
            if quote_in(s.quote, docs[s.kind]):
                quote_checks["verified"] += 1
            else:
                problems.append(f"{s.id}: quote not found in {s.kind}: '{s.quote[:80]}'")
        if s.kind == "web":
            if not s.url:
                problems.append(f"{s.id}: web source without URL")
            elif verify_web and s.quote:
                web_checks["checked"] += 1
                if _web_quote_ok(s.url, s.quote):
                    web_checks["verified"] += 1
                else:
                    problems.append(f"{s.id}: quote not found at {s.url} (page may have changed or blocks bots)")
            else:
                web_checks["skipped"] += 1

    claims = list(dossier.claims)
    if card:
        for cs in card.criteria:
            claims.extend(cs.evidence)
    unsourced = [c.text for c in claims if not c.source_ids]
    dangling = sorted({sid for c in claims for sid in c.source_ids if sid not in src})
    for u in unsourced:
        problems.append(f"claim without source: '{u[:80]}'")
    for d in dangling:
        problems.append(f"claim cites unknown source id {d}")

    return {
        "slug": dossier.slug,
        "claims": len(claims),
        "claims_with_sources": len(claims) - len(unsourced),
        "dangling_source_ids": dangling,
        "doc_quotes": quote_checks,
        "web_quotes": web_checks,
        "web_sources": sum(1 for s in dossier.sources if s.kind == "web"),
        "problems": problems,
        "pass": not unsourced and not dangling and quote_checks["checked"] == quote_checks["verified"],
    }


def _web_quote_ok(url: str, quote: str) -> bool:  # pragma: no cover - network
    try:
        import requests

        r = requests.get(url, timeout=15, headers={"User-Agent": "triage-citation-check/1.0"})
        text = re.sub(r"<[^>]+>", " ", r.text)
        return quote_in(quote, text)
    except Exception:
        return False
