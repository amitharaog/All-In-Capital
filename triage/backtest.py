"""Backtest against the fund's own 12 past decisions.

Kushal: 'Run it against those and tell me how often it disagrees with us.
When it does, tell me whether we were wrong or it was.'

Inputs are built from data/seed/deal_memos.md with the decision and the
'Why we invested/passed' paragraph held out. Two variants:

- full:        what it does + founder assessment + risks
- no_founder:  what it does + risks only (what a deck-only read sees; tests
               how much the system depends on founder behaviour that only
               a call reveals)

Leakage controls: the scorer gets the thesis with the `precedents` lists
removed and no stored corrections. Caveat that cannot be removed: the
revealed thesis was itself reconstructed from these 12 memos, so 'revealed'
agreement is in-sample (an upper bound). The 'stated' lens is not derived
from the memos and is the fair out-of-sample comparison.
"""
from __future__ import annotations

import math
import re

from .core import DATA, decide, dump_json, load_json, load_thesis
from .schemas import Claim, ResearchDossier, ScoreCard, Source

BT = DATA / "backtest"
SECTOR_MAP = {"deeptech": "deeptech", "consumer brand": "consumer_brand", "consumer tech": "consumer_tech",
              "fintech": "fintech", "web3": "other"}


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.lower().replace("the ", ""))


def parse_memos() -> list[dict]:
    text = (DATA / "seed" / "deal_memos.md").read_text(encoding="utf-8")
    memos = []
    for block in re.split(r"\n## Memo ", text)[1:]:
        head, _, body = block.partition("\n")
        n, name = head.split(": ", 1)
        meta = re.search(r"Sector: (.*?) \| Stage: (.*?) \| Source: (.*?) \| Decision: (\w+)", body)
        sec = {}
        for key, label in [("what", "What it does."), ("founder", "Founder assessment."),
                           ("risks", "Risks and open questions."), ("why", r"Why we (?:invested|passed).")]:
            m = re.search(r"\*\*" + label + r"\*\* (.*?)(?=\n\n\*\*|\Z)", body, re.S)
            sec[key] = m.group(1).strip() if m else ""
        sector_raw = meta.group(1)
        sector = next((v for k, v in SECTOR_MAP.items() if sector_raw.lower().startswith(k)), "other")
        memos.append({
            "n": int(n), "name": name.strip(), "slug": slugify(name), "sector_raw": sector_raw,
            "sector": sector, "stage": meta.group(2), "source": meta.group(3),
            "decision": meta.group(4), **sec,
        })
    return memos


def build_dossier(m: dict, variant: str) -> ResearchDossier:
    sources = [
        Source(id="M1", kind="seed", title=f"Memo {m['n']} header", locator="header",
               quote=f"Sector: {m['sector_raw']} | Stage: {m['stage']} | Source: {m['source']}"),
        Source(id="M2", kind="seed", title=f"Memo {m['n']} - What it does", locator="What it does", quote=m["what"][:300]),
        Source(id="M4", kind="seed", title=f"Memo {m['n']} - Risks", locator="Risks and open questions", quote=m["risks"][:300]),
    ]
    claims = [Claim(text=m["what"], source_ids=["M2"], status="founder_stated"),
              Claim(text="Risks recorded by the fund: " + m["risks"], source_ids=["M4"], status="verified")]
    if variant == "full":
        sources.append(Source(id="M3", kind="seed", title=f"Memo {m['n']} - Founder assessment",
                              locator="Founder assessment", quote=m["founder"][:300]))
        claims.append(Claim(text="Partner assessment of founders from the meeting: " + m["founder"],
                            source_ids=["M3"], status="verified"))
    return ResearchDossier(
        company=m["name"], slug=m["slug"], one_liner=m["what"].split(".")[0], sector=m["sector"],
        sub_sector=m["sector_raw"], stage=m["stage"], business_model=m["what"], founders=[],
        claims=claims, gaps=[], sources=sources, keywords=[],
        produced_by=f"backtest builder ({variant}; decision and 'why' paragraph withheld)",
    )


def blind_thesis() -> dict:
    t = load_thesis()
    for lens in t["lenses"].values():
        for c in lens["criteria"]:
            c.pop("precedents", None)
    return t


def build_inputs() -> None:
    for variant in ("full", "no_founder"):
        for m in parse_memos():
            dump_json(BT / "dossiers" / variant / f"{m['slug']}.json", build_dossier(m, variant))
    dump_json(BT / "thesis_blind.json", blind_thesis())
    dump_json(BT / "answer_key.json", [{k: m[k] for k in ("n", "name", "slug", "decision", "why")} for m in parse_memos()])


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(c - h, 2), round(c + h, 2))


def evaluate() -> dict:
    thesis = load_thesis()
    memos = parse_memos()
    out = {"variants": {}}
    for variant in ("full", "no_founder"):
        rows = []
        for m in memos:
            sp = BT / "scores" / variant / f"{m['slug']}.json"
            if not sp.exists():
                continue
            card = ScoreCard.model_validate(load_json(sp))
            dossier = ResearchDossier.model_validate(load_json(BT / "dossiers" / variant / f"{m['slug']}.json"))
            v = decide(dossier, card, thesis)
            system_yes = v.recommendation == "TAKE_CALL"
            fund_yes = m["decision"] == "INVESTED"
            stated_yes = v.stated.score_10 >= thesis["routing"]["take_call"]["revealed_min"]
            rows.append({
                "memo": m["n"], "company": m["name"], "fund": m["decision"], "system": v.recommendation,
                "revealed": v.revealed.score_10, "stated": v.stated.score_10, "coverage": v.revealed.coverage,
                "agree": system_yes == fund_yes, "stated_agree": stated_yes == fund_yes,
                "gates": [g.gate_id for g in card.gates if g.triggered],
                "weakest": sorted(v.revealed.breakdown, key=lambda b: b["score_5"])[0]["name"],
                "fund_reason": m["why"],
            })
        n = len(rows)
        k = sum(r["agree"] for r in rows)
        ks = sum(r["stated_agree"] for r in rows)
        inv = [r for r in rows if r["fund"] == "INVESTED"]
        pas = [r for r in rows if r["fund"] == "PASSED"]
        out["variants"][variant] = {
            "n": n,
            "agreement": k, "agreement_rate": round(k / n, 2) if n else None, "agreement_ci95": wilson(k, n),
            "stated_lens_agreement": ks, "stated_lens_rate": round(ks / n, 2) if n else None,
            "missed_investments": [r["company"] for r in inv if not r["agree"]],
            "would_have_advanced_passes": [r["company"] for r in pas if not r["agree"]],
            "mean_revealed_invested": round(sum(r["revealed"] for r in inv) / len(inv), 2) if inv else None,
            "mean_revealed_passed": round(sum(r["revealed"] for r in pas) / len(pas), 2) if pas else None,
            "mean_stated_invested": round(sum(r["stated"] for r in inv) / len(inv), 2) if inv else None,
            "mean_stated_passed": round(sum(r["stated"] for r in pas) / len(pas), 2) if pas else None,
            "rows": rows,
        }
    adj = BT / "adjudication.json"
    if adj.exists():
        out["adjudication"] = load_json(adj)
    dump_json(BT / "results.json", out)
    return out


if __name__ == "__main__":  # pragma: no cover
    build_inputs()
    print("built", len(parse_memos()), "memos x 2 variants")
