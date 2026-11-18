"""Data contracts for the triage pipeline.

Every LLM step must produce one of these shapes. The deterministic code
(aggregation, gates, routing, citation checks) only ever reads these models,
so a run made through the API and a run made by hand by an analyst are
interchangeable and auditable in the same way.
"""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

SourceKind = Literal["deck", "form", "web", "seed", "inference"]
Confidence = Literal["high", "medium", "low"]


class Source(BaseModel):
    """One place a claim can be traced to."""

    id: str = Field(description="Short id, e.g. D1 (deck), F1 (form), W3 (web)")
    kind: SourceKind
    title: str
    url: Optional[str] = None
    locator: Optional[str] = Field(
        default=None, description="Slide/section/question for deck & form sources"
    )
    retrieved_on: Optional[str] = None
    quote: Optional[str] = Field(
        default=None, description="Verbatim text from the source that supports the claim"
    )


class Claim(BaseModel):
    """A single factual statement about the applicant, tied to sources."""

    text: str
    source_ids: list[str]
    status: Literal["verified", "founder_stated", "contradicted", "unverifiable"] = (
        "founder_stated"
    )
    note: Optional[str] = None


class Gap(BaseModel):
    """Something the system looked for and could not establish."""

    what: str
    why_it_matters: str
    searched: list[str] = Field(default_factory=list, description="Where we looked")
    ask_founder: Optional[str] = Field(
        default=None, description="The question to put to the founder to close it"
    )
    blocks_criteria: list[str] = Field(default_factory=list)


class Founder(BaseModel):
    name: str
    role: Optional[str] = None
    background_claimed: Optional[str] = None
    background_verified: Optional[str] = None
    public_footprint: Literal["found", "partial", "not_found"] = "not_found"
    source_ids: list[str] = Field(default_factory=list)


class ResearchDossier(BaseModel):
    """Output of the research step: what the deck says plus what the web says."""

    company: str
    slug: str
    one_liner: str
    sector: Literal["fintech", "deeptech", "consumer_tech", "consumer_brand", "other"]
    sub_sector: str
    stage: str
    ask: Optional[str] = None
    business_model: str
    founders: list[Founder]
    claims: list[Claim]
    gaps: list[Gap]
    competitors_named: list[str] = Field(default_factory=list)
    competitors_found: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(
        default_factory=list, description="Product/category keywords used for conflict checks"
    )
    founder_contact: Optional[str] = None
    sources: list[Source]
    produced_by: str = "anthropic-api"
    research_notes: Optional[str] = None


class CriterionScore(BaseModel):
    criterion_id: str
    score: Optional[float] = Field(
        default=None, ge=0, le=5, description="0-5; null when there is no evidence at all"
    )
    status: Literal["evidenced", "partial", "not_evidenced"]
    rationale: str = Field(description="Why this score, in 1-3 sentences")
    evidence: list[Claim] = Field(default_factory=list)
    confidence: Confidence = "low"
    precedents_applied: list[str] = Field(
        default_factory=list, description="Correction ids that changed this score"
    )


class GateResult(BaseModel):
    gate_id: str
    triggered: bool
    detail: str
    source_ids: list[str] = Field(default_factory=list)


class ScoreCard(BaseModel):
    """Output of the scoring step (LLM judgement only — no totals, no verdict)."""

    slug: str
    lens_used_primary: Literal["revealed", "stated"] = "revealed"
    criteria: list[CriterionScore]
    gates: list[GateResult]
    case_for: list[str]
    case_against: list[str]
    call_questions: list[str] = Field(
        description="Questions for the first call, aimed at the gaps and the founder-behaviour criteria"
    )
    what_would_change_our_view: Optional[str] = None
    produced_by: str = "anthropic-api"


class LensResult(BaseModel):
    lens: str
    score_10: float
    coverage: float = Field(description="Share of criterion weight backed by evidence")
    breakdown: list[dict]


class Verdict(BaseModel):
    """Deterministic output computed in code from a ScoreCard + gates."""

    slug: str
    company: str
    recommendation: Literal["TAKE_CALL", "SCREEN_FIRST", "HOLD_CONFLICT", "PASS"]
    headline: str
    revealed: LensResult
    stated: LensResult
    lens_disagreement: Optional[str] = None
    flags: list[str]
    call_attendees: list[str]
    needs_partner_review: bool = True  # always true: nobody is auto-advanced or auto-rejected


class Correction(BaseModel):
    id: str
    date: str
    company: str
    criterion_id: Optional[str] = None
    old_score: Optional[float] = None
    new_score: Optional[float] = None
    by: str
    reason: str = Field(description="One line, written to be reusable on similar companies")
    applies_when: list[str] = Field(
        default_factory=list, description="Tags: sector, model, situation (e.g. 'missing_repeat_rate')"
    )
    origin: Literal["partner_notes", "review"] = "review"
