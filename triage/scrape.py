"""Collect Info -> Scrape: fetch every link the founders put in the deck and form.

Deterministic, no LLM. Each URL is fetched once; a live page becomes a
source (id X1, X2, ...) with its title and opening text, a dead or placeholder
link becomes a named gap. Results are merged into the dossier idempotently
(previous X* sources and scrape gaps are replaced), so re-running is safe.
"""
from __future__ import annotations

import datetime as dt
import re

from .core import APPS, RESEARCH, dump_json, load_json
from .schemas import Claim, Gap, ResearchDossier, Source

URL_RE = re.compile(r"(?:https?://|www\.)[^\s)>\]|,\"'*]+|(?:linkedin\.com|github\.com|play\.google\.com|apps\.apple\.com)/[^\s)>\]|,\"'*]+", re.I)
SCRAPE_TAG = "[scrape]"


def find_urls(slug: str) -> list[dict]:
    found: dict[str, dict] = {}
    for kind in ("deck", "form"):
        path = APPS / slug / f"{kind}.md"
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("<!-- source:"):
                continue
            line = re.sub(r"((?:linkedin\.com/in|github\.com)/[\w-]*-)\s+([\w-]+)", r"\1\2", line)  # PDF line-break split
            for u in URL_RE.findall(line):
                u = u.rstrip(".;:")
                norm = u if u.startswith("http") else "https://" + u
                found.setdefault(norm, {"url": norm, "found_in": kind})
    return list(found.values())


def fetch(url: str) -> dict:
    out = {"url": url, "fetched_at": dt.datetime.now().isoformat(timespec="seconds")}
    try:
        import requests

        r = requests.get(url, timeout=12, headers={"User-Agent": "Mozilla/5.0 (triage-scraper)"}, allow_redirects=True)
        html = r.text
        title = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
        text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S | re.I)
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text)).strip()
        t = title.group(1).strip()[:200] if title else ""
        blocked = re.search(r"captcha|checking your browser|sign ?in|sign ?up|log ?in|just a moment|access denied|"
                            r"page not found|404", t, re.I)
        out.update(ok=r.ok and not blocked, status=r.status_code, final_url=r.url, title=t, snippet=text[:600])
        if blocked:
            out["error"] = f"blocked or not a real page (title: {t!r})"
    except Exception as e:
        out.update(ok=False, status=None, error=f"{type(e).__name__}: {str(e)[:160]}")
    return out


def placeholder(url: str) -> bool:
    return bool(re.search(r"\.example\b|-example\b|example\.com", url))


def scrape(slug: str) -> dict:
    results = []
    for u in find_urls(slug):
        res = fetch(u["url"])
        res["found_in"] = u["found_in"]
        res["placeholder"] = placeholder(u["url"])
        results.append(res)
    out = {"slug": slug, "scraped_on": dt.date.today().isoformat(), "results": results}
    dump_json(RESEARCH / "scrape" / f"{slug}.json", out)
    return out


def merge(slug: str, scraped: dict | None = None) -> ResearchDossier:
    scraped = scraped or load_json(RESEARCH / "scrape" / f"{slug}.json")
    d = ResearchDossier.model_validate(load_json(RESEARCH / f"{slug}.json"))
    d.sources = [s for s in d.sources if not s.id.startswith("X")]
    d.claims = [c for c in d.claims if not any(i.startswith("X") for i in c.source_ids)]
    d.gaps = [g for g in d.gaps if SCRAPE_TAG not in g.what]
    n = 0
    for r in scraped["results"]:
        if r.get("ok") and not r["placeholder"]:
            n += 1
            sid = f"X{n}"
            d.sources.append(Source(id=sid, kind="web", title=r.get("title") or r["url"], url=r.get("final_url") or r["url"],
                                    retrieved_on=r["fetched_at"][:10], quote=(r.get("snippet") or "")[:200] or None,
                                    locator=f"linked from {r['found_in']}"))
            d.claims.append(Claim(text=f"The {r['found_in']} links to a live page: {r.get('title') or r['url']}",
                                  source_ids=[sid], status="verified"))
        else:
            why = ("a placeholder address (*.example), so there is nothing to verify" if r["placeholder"]
                   else (r.get("error") or f"HTTP {r.get('status')}"))
            d.gaps.append(Gap(
                what=f"{SCRAPE_TAG} Link in the {r['found_in']} does not resolve: {r['url']}",
                why_it_matters="Links the founders give are the first place to verify the company and the team; a dead link means nothing here could be checked.",
                searched=[f"fetched {r['url']} on {r['fetched_at'][:10]}: {why}"],
                ask_founder=f"Can you share a working link for {r['url'].split('//')[-1].split('/')[0]}?",
            ))
    dump_json(RESEARCH / f"{slug}.json", d)
    return d
