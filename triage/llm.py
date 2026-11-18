"""Claude API calls for the two judgement steps: research and scoring.

Everything else in the pipeline is deterministic code. Requires an Anthropic
credential (ANTHROPIC_API_KEY or `ant auth login`).

- research(): Claude Opus 5.5 with the server-side web_search / web_fetch
  tools, streamed, with pause_turn handled. Output validated as ResearchDossier.
- score(): Claude Opus 5.5 structured output parsed straight into ScoreCard.
"""
from __future__ import annotations

import json
import re

from .core import APPS, FUND, PROMPTS, load_json, load_thesis
from .corrections import as_prompt_block, retrieve
from .schemas import ResearchDossier, ScoreCard

MODEL = "claude-opus-5-5"
WEB_TOOLS = [
    {"type": "web_search_20260209", "name": "web_search", "max_uses": 25},
    {"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": 15},
]


def _client():
    import anthropic

    return anthropic.Anthropic()


def _extract_json(text: str) -> dict:
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.S)
    raw = m.group(1) if m else text[text.find("{") : text.rfind("}") + 1]
    return json.loads(raw)


def research(slug: str, retrieved_on: str) -> ResearchDossier:
    client = _client()
    deck = (APPS / slug / "deck.md").read_text(encoding="utf-8")
    form = (APPS / slug / "form.md").read_text(encoding="utf-8")
    user = (
        f"Application slug: {slug}. Today's date for retrieved_on: {retrieved_on}.\n\n"
        f"<deck>\n{deck}\n</deck>\n\n<form>\n{form}\n</form>\n\n"
        "Return the ResearchDossier as a single JSON object in a ```json block. Schema:\n"
        + json.dumps(ResearchDossier.model_json_schema())
    )
    messages = [{"role": "user", "content": user}]
    for _ in range(6):  # resume paused server-tool turns
        with client.beta.messages.stream(
            model=MODEL,
            max_tokens=64000,
            system=(PROMPTS / "research.md").read_text(encoding="utf-8"),
            tools=WEB_TOOLS,
            output_config={"effort": "high"},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            messages=messages,
        ) as stream:
            resp = stream.get_final_message()
        if resp.stop_reason == "refusal":
            raise RuntimeError(f"research refused for {slug}: {resp.stop_details}")
        if resp.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": resp.content})
            continue
        break
    text = "".join(b.text for b in resp.content if b.type == "text")
    data = _extract_json(text)
    data["produced_by"] = f"anthropic-api ({MODEL})"
    return ResearchDossier.model_validate(data)


def score(dossier: ResearchDossier) -> ScoreCard:
    client = _client()
    portfolio = load_json(FUND / "portfolio.json") if (FUND / "portfolio.json").exists() else []
    precedents = retrieve(dossier)
    user = (
        "<thesis>\n" + json.dumps(load_thesis(), indent=1) + "\n</thesis>\n\n"
        "<portfolio>\n" + json.dumps(portfolio, indent=1) + "\n</portfolio>\n\n"
        "<partner_corrections>\n" + as_prompt_block(precedents) + "\n</partner_corrections>\n\n"
        "<dossier>\n" + dossier.model_dump_json(indent=1) + "\n</dossier>\n\n"
        "Score every criterion in both lenses (R1-R6, S1-S4) and evaluate gates G1-G3."
    )
    resp = client.messages.parse(
        model=MODEL,
        max_tokens=16000,
        system=(PROMPTS / "score.md").read_text(encoding="utf-8"),
        output_config={"effort": "high"},
        messages=[{"role": "user", "content": user}],
        output_format=ScoreCard,
    )
    if resp.stop_reason == "refusal":
        raise RuntimeError(f"scoring refused for {dossier.slug}: {resp.stop_details}")
    card = resp.parsed_output
    card.produced_by = f"anthropic-api ({MODEL})"
    return card
