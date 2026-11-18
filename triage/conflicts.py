"""Portfolio conflict check (gate G1), run against the full portfolio list.

Partner notes, Meeting 4: the MeetRecord overlap was only caught because Riya
happened to remember the portfolio, and Kushal would rather get a flag on a
false alarm than miss a real conflict. So this check is deliberately
recall-biased and deterministic: it runs on every application regardless of
what the LLM concluded, and it explains every hit.
"""
from __future__ import annotations

import re

from .core import FUND, load_json
from .schemas import ResearchDossier

STOP = set(
    """a an and the of for to in on with by from at as is are be or our we you your their its it this that
    platform app apps company startup india indian based tech technology solution solutions service services
    using use users user customers customer businesses business small new first online digital smart ai
    across into via more less every all any who how what""".split()
)

# Category families: words that mean "the same job" even when no word is shared.
FAMILIES = {
    "meeting_notes": {"meeting", "meetings", "notes", "note", "notetaker", "transcript", "transcription",
                       "transcribe", "call", "calls", "summary", "summaries", "summarise", "summarize",
                       "recording", "recorder", "conversation", "conversations", "voice"},
    "lending": {"loan", "loans", "lending", "credit", "bnpl", "emi", "nbfc", "borrower", "borrowers", "financing"},
    "wealth": {"invest", "investing", "investment", "investments", "wealth", "bonds", "bond", "fixed",
               "income", "mutual", "funds", "stocks", "stock", "trading", "portfolio", "sip"},
    "payments": {"payments", "payment", "upi", "settlement", "settlements", "reconciliation", "invoice",
                 "invoicing", "receivables", "payables", "collections"},
    "accounting_tax": {"accounting", "bookkeeping", "tax", "gst", "ca", "audit", "compliance", "filing", "itr"},
    "retail_kirana": {"kirana", "grocery", "retail", "store", "stores", "shopkeeper", "shopkeepers", "inventory"},
    "logistics": {"logistics", "delivery", "warehouse", "sorting", "fulfilment", "fulfillment", "fleet", "trucking"},
    "mobility_aero": {"drone", "drones", "evtol", "aircraft", "aerial", "uav", "aviation"},
    "travel": {"travel", "trip", "trips", "tour", "tours", "booking", "itinerary", "hotel", "hotels"},
    "rental_housing": {"rent", "rental", "rentals", "tenant", "tenants", "landlord", "landlords", "housing", "pg", "flat"},
    "care_health": {"care", "caregiver", "caregivers", "elder", "elderly", "health", "healthcare", "clinic", "nursing", "patients"},
    "agri": {"farmer", "farmers", "agri", "agriculture", "crop", "crops", "irrigation", "dairy", "grain", "grains"},
    "food_brand": {"snack", "snacks", "food", "millet", "millets", "breakfast", "cereal", "beverage", "fmcg"},
    "beauty_jewellery": {"skincare", "beauty", "cosmetics", "jewellery", "jewelry", "silver", "gold"},
    "education": {"exam", "exams", "test", "prep", "learning", "edtech", "students", "tutor", "course", "courses"},
    "hr_payroll": {"payroll", "salary", "wages", "earned", "ewa", "employees", "workforce", "gig", "workers"},
    "creator_audio": {"podcast", "audio", "creator", "creators", "community"},
}


def _tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", (text or "").lower()) if t not in STOP and len(t) > 1}


def _families(tokens: set[str]) -> dict[str, set[str]]:
    out = {}
    for fam, words in FAMILIES.items():
        hit = tokens & words
        if len(hit) >= 2:
            out[fam] = hit
    return out


def load_portfolio() -> list[dict]:
    path = FUND / "portfolio.json"
    if not path.exists():
        return []
    data = load_json(path)
    return data["companies"] if isinstance(data, dict) else data


def check(dossier: ResearchDossier, portfolio: list[dict] | None = None) -> list[dict]:
    portfolio = portfolio if portfolio is not None else load_portfolio()
    app_text = " ".join(
        [dossier.one_liner, dossier.sub_sector, dossier.business_model, " ".join(dossier.keywords)]
    )
    app_tok = _tokens(app_text)
    app_fam = _families(app_tok)
    mentioned = " ".join([c.text for c in dossier.claims] + dossier.competitors_named + dossier.competitors_found).lower()

    hits = []
    for p in portfolio:
        names = [p["name"], *p.get("aliases", [])]
        p_text = " ".join([p.get("one_line", ""), p.get("sector", ""), " ".join(p.get("tags", []))])
        p_tok = _tokens(p_text)
        p_fam = _families(p_tok)
        shared_fam = sorted(set(app_fam) & set(p_fam))
        shared_words = sorted((app_tok & p_tok) - {"fintech", "deeptech", "consumer", "brand"})
        named = any(n.lower() in mentioned for n in names if len(n) > 3)

        level = None
        why = []
        if named:
            why.append(f"application or research names {p['name']}")
        if shared_fam:
            why.append("same job family: " + ", ".join(shared_fam))
        if named and shared_fam:
            level = "high"
        elif named or shared_fam:
            level = "medium"
        elif len(shared_words) >= 3:
            level = "low"
            why.append("shared vocabulary: " + ", ".join(shared_words[:6]))
        if level:
            if p.get("all_in_capital_fund_investment") is False:
                why.append("pre-fund partner investment (not Fund I/II)")
                if level == "high":
                    level = "medium"
            hits.append(
                {
                    "portfolio_company": p["name"],
                    "level": level,
                    "why": "; ".join(why),
                    "portfolio_one_line": p.get("one_line", ""),
                    "source_url": p.get("source_url"),
                }
            )
    order = {"high": 0, "medium": 1, "low": 2}
    return sorted(hits, key=lambda h: order[h["level"]])
