# All In Capital intake triage: results and how far to trust it

**For:** Kushal Bhagia, Aditya Singh and Riya
**Batch:** 10 inbound applications
**Date:** 18 Nov 2026
**Review pack:** `runs/2026-11-18/report.html`

## The short version

**This week's suggestions.** All 10 applications were researched on the web, scored
against the thesis criterion by criterion, and given a suggestion. Nothing is decided;
every outcome waits for Kushal.

| | Company | Suggestion | Revealed / Stated | Why, in one line |
|---|---|---|---|---|
| 1 | **Pumpwise** | **Take the call**, with Aditya (deeptech) | 6.35 / 7.1 | 38 plant visits, then 11 pilots with 55% converting to paid. But revenue is 94% one-off hardware, and subscription income doesn't reconcile with the founders' own sensor ramp. |
| 2 | **GrainKind** | **Hold: portfolio overlap** (would be *take the call*) | 6.75 / 6.6 | Cohort repeat of 31%, 34% and 38% at 90 days, offered without being asked. But ~70% of new customers are bought, LTV:CAC is ~1.8x, and it sits on the same shelf as Taakat and MomsMade. |
| 3 | **Talkbook** | **Hold: portfolio overlap** (would be *screen first*) | 4.65 / 5.5 | Does the job **MeetRecord** (Fund I, now Outdoo) does: record sales calls, summarise them, fill the CRM. The application never mentions it, which is the Meeting 4 near-miss again. |
| 4 | **StockSathi** | **Hold: overlap** with SuperK (pre-fund); would be *suggest pass* | 4.45 / 5.5 | Did real field work (60 owner interviews), but the deck and form give different answers on who carries the credit risk. |
| 5 | **CareCorner** | **Screen first** | 5.75 / 5.45 | Founders name their own risks and offer clinic P&Ls. Capex-heavy, and the projections assume mature clinics earn 3.6x today's average. The fund has no precedent for this category. |
| 6 | **CAPilot** | **Screen first** | 4.7 / 6.05 | A practising CA built it, with 24 paying firms. The deck counts 7 trial firms as paying, calls MRR x 12 "ARR", and misses a direct competitor (GST Reply AI). |
| 7 | **Yatrika** | **Screen first** (score suggests pass; founder behaviour not visible) | 4.15 / 5.1 | A commission travel agency with a language-model front end. The deck says "thousands of travellers"; the form says ~1,300. |
| 8 | **Settlr** | **Suggest pass: mandate** | 4.55 / 4.65 | A INR 30 Cr Series A with four funds competing. The fund leads first rounds up to ~INR 6 Cr. Not a judgement on the company. |
| 9 | **RentRoute** | **Suggest pass: depends on a rule change** | 2.8 / 5.1 | Card rent payments were shut for CRED, PhonePe and Paytm by RBI's 2025 payment-aggregator rules. RentRoute runs through one payment aggregator, with no compliance account and no plan B. |
| 10 | **EarnWise** | **Suggest pass** | 2.25 / 3.65 | Six deck-vs-form contradictions: "Ex-Goldman, Ex-Google, IIM-A" against an internship, a vendor contract and a tier-2 MBA; team of 12 vs 5; 3 live clients vs 1. A co-founder's exit is left out of the deck. |

**Evidence behind those scores:**
- 470 of 470 claims cite a source.
- 298 of 298 quotes taken from decks and forms were found verbatim in the files.
- 63 of 68 web quotes were found again on the live page. The other five pages block
  scripts and need a click-through.
- 75 gaps are named, each with the question to ask.
- 0 of the 19 founders had any findable public footprint. Every application links
  `*.example` placeholders. That is reported as a gap and never treated as a negative.

**Can you trust it yet? No, by the bar written before any results were seen.**
- Re-scoring the fund's 12 past decisions blind, it agrees on **8 of 12**. The
  pre-agreed bar was 9.
- **Its misses are all cautious.** It never advanced any of the six companies the fund
  passed on.
- **It under-calls companies the fund backed for founder behaviour despite thin
  numbers:** Wint Wealth, SuperK, Jai Kisan and ePlane.
- **What to do now:** use it to rank, name gaps, write call questions and catch
  conflicts. Under rule v2 it may suggest a pass only on a gate, or when founder
  behaviour is actually visible. Run shadow mode against Riya's own reads before relying
  on it further.

## 1. Reconstructing the thesis

The fund publishes no scoring rubric, no ownership target and no exclusion list.
`data/fund/public_thesis.json` holds 229 verbatim quotes, each with its URL. Each quote
was checked by script against the saved page.

### What is public: the stated lens

These sources are the fund site and apply page, the Fund II launch coverage (Entrackr,
Business Standard, Inc42), Kushal's X posts and the Inc42 founder-market-fit interview.

| Criterion | Weight | What the fund says publicly |
|---|---|---|
| S1 Focus sector | 20 | Sector-agnostic, with special focus on consumer tech, deeptech, fintech and consumer brands. Fund II mix is about 50% consumer, 30% Indian AI and 20% deeptech. Vertical AI is preferred over thin wrappers. |
| S2 Stage and round the fund can lead | 20 | Paper-plan to early revenue. USD 200–600K first cheques. It leads or co-leads rounds up to about INR 6 Cr. |
| S3 Founder-market fit and earned secrets | 35 | What the founders know and can do; the key risk; earned secrets; love of the problem for 5–6 years. |
| S4 Non-obvious, ambitious | 25 | Non-consensus founders and ideas, a vision that inspires, global ambition. |

### What the fund actually rewards: the revealed lens

This lens is reconstructed from the 12 memos and 5 partner meetings. It drives the
suggestion.

| Criterion | Weight | Built from |
|---|---|---|
| R1 Founders own the defining risk | 25 | Jai Kisan vs CampusCredit; ePlane vs AeroDrop; Coinlane; HopBox |
| R2 Went to the customer first | 20 | Wint Wealth, SuperK, Jai Kisan, Unbox |
| R3 Earned traction on the sector's deciding metric (missing = drags) | 20 | Giva vs Petalry; Prepnest |
| R4 Credible path to market, scored apart from founder quality | 15 | Unbox vs AeroDrop; Meeting 3 |
| R5 Works on a pre-seed cheque | 10 | HopBox; ePlane's cheque sizing |
| R6 Travels beyond the founder | 10 | Prepnest; SuperK |

### Rules taken from the partner notes and enforced in code

- **A missing number drags the score.** A criterion with no evidence counts as 1/5 and
  lowers coverage (Kushal on Petalry, Meeting 1).
- **Credentials can't lift any criterion above 2/5** (Kushal on AeroDrop, Meeting 3).
- **Every application is checked against all 88 portfolio companies.** Both the code and
  the scorer do it, and false alarms are preferred (Meeting 4).
- **Calls are Tuesday or Thursday afternoons, 30 minutes.** Aditya joins only for
  deeptech (Meeting 5).
- **Nobody is auto-advanced or auto-rejected** (Meeting 5).

### Gates

Gates override the score:
- **G1 portfolio conflict:** hold.
- **G2 exists only if the rules change:** pass on category (Coinlane).
- **G3 sector-label stretch:** flag only (Jai Kisan).
- **G4 outside mandate:** pass on mandate. This one comes from the public stage and cheque
  statements.

### What isn't public, and what that costs

| Not found | What the system does instead | What it costs |
|---|---|---|
| Ownership target, valuation band | Can't check whether a round is priceable for the fund. It only uses the INR 6 Cr lead ceiling (G4). | A pre-seed raising at an unworkable valuation won't be flagged. |
| Exclusion list | Uses the G2 rule from the Coinlane memo instead. | Categories the partners dislike but never wrote down get scored on the merits. |
| Founder backgrounds for all 10 applicants | Each one is a named gap with the searches run. | R1/R6 rest on what the founders themselves stated; confidence is set to low or medium. |
| Partners' LinkedIn posts, podcast transcripts, Crunchbase/PitchBook | The lens uses the press and the fund's own site. | Recent shifts in tone may be missed. |

### Riya's drift question: which thesis should she score against?

The backtest gives a first answer. Read from what the fund actually says publicly, the
stated thesis separates past investments from passes almost as well as the revealed one:

| Lens | Separation (AUC), full memos | Separation (AUC), without founder notes |
|---|---|---|
| Revealed | 1.00 | 0.83 |
| Stated | 0.97 | 0.86 |

**The stated lens's one error is AeroDrop.** It scores AeroDrop 6.65 for credentials and
ambition, which is the mistake Kushal corrected in Riya's 7.5. So:
- **Aditya's view ("the thesis is stable") holds up better than the drift theory.** That
  is, if the stated thesis is read as the founder-market-fit wording the fund actually
  publishes, not just the sector list.
- **The real gap is narrower.** In practice the fund discounts credentials and
  ambition, and rewards unglamorous customer groundwork (Wint Wealth, SuperK, Jai Kisan).
  The public wording doesn't say either.
- **Both lenses are shown on every company.** The suggestion uses the revealed lens, and
  disagreements of 1.5+ points are printed. That follows Kushal's instruction: "tell me
  which one you used and why".

The caveats in section 3 apply: both lenses were tested on 12 decisions, and the revealed
lens was built from those same 12.

## 2. What it does for each of Kushal's asks

| Kushal asked for | Where it lives |
|---|---|
| "The whole pile, not one deck" | `python -m triage run` processes everything in `data/applications/` into one review pack. |
| "Criterion by criterion, with the source behind every claim" | Each score card cites dossier source ids. Deck/form quotes are verified against the files and web quotes are re-fetched (`triage/citations.py`). Every criterion in the report has its sources linked. |
| "What it couldn't find out" | `gaps` in each dossier: what was looked for, where, and the question to ask the founder. |
| "Whether we should take the call" | A deterministic routing rule in `triage/core.py`. The thresholds live in `thesis.json` and were set before any results. |
| "Go find it, not just read the deck" | The research step uses web search and fetch: 68 web sources across 10 companies. It found RBI's 2025 card-rent shutdown, the MeetRecord overlap, competitors the decks didn't name (GST Reply AI, Infinite Uptime, Convin, Thrillophilia, MakeMyTrip's Myra), and arithmetic errors in decks. |
| "A correction should count next time" | `python -m triage correct ...` stores a one-line reason with tags. The next similar applicant retrieves it, and the scorer must say where it was applied. Four corrections from the meeting notes are seeded. C004 (the lender rule) was applied to StockSathi, Settlr and EarnWise, and C002 (pedigree) to Pumpwise. A test proves a GrainKind correction reaches the next similar brand and not an unrelated fintech. |
| "Don't make me go back to email and calendars" | `approve <slug> call` then `book` holds a Tue/Thu afternoon slot, avoiding busy times, adds Aditya for deeptech, and writes the invite, the founder email with two alternates, and pass notes. `runs/2026-11-18/demo_outbox/` shows the output, clearly labelled as a demo, not a decision. A Google Calendar backend is included but untested here. |
| "I'll see every outcome first" | `needs_partner_review` is always true. Nothing is booked or sent without a recorded decision. |
| "Run it against our real decisions" | The backtest in section 3. |

## 3. Backtest: how often it disagrees with the fund, and who was wrong

**Method.**
- Each of the 12 memos was turned into an input with the decision and the "Why we…"
  paragraph removed.
- Fresh scorers, which could not see the answers, scored it against a thesis file with
  the precedent lists stripped out.
- There were two variants. **Full** has what it does, the partners' founder assessment,
  and the risks. **No-founder** has only what it does and the risks: roughly what a deck
  shows.

| | Full memos | No founder assessment |
|---|---|---|
| Agreement (take-call ⇔ invested) | **8/12** (95% CI 39–86%) | 6/12 |
| Passes the system would have advanced | **0 of 6** | 0 of 6 |
| Investments marked "suggest pass": pre-registered rule | 1 (ePlane) | 6 |
| Investments marked "suggest pass": rule v2 | **0** | **0** |
| Mean revealed score, invested vs passed | 5.68 vs 2.52 | 3.53 vs 2.62 |

### Where it disagreed, and who was wrong

All four disagreements were checked against the withheld reasoning
(`data/backtest/adjudication.json`). In each case the fund was right.

- **ePlane: the system was wrong, because of a gap in the thesis.**
  - The revealed lens expects traction and a path to market.
  - Pre-revenue deeptech can't show those, and the fund knowingly sized its cheque for a
    slow path.
  - The deciding evidence (the "what would make you quit?" milestone answer) was in the
    withheld paragraph.
- **Wint Wealth (5.9), SuperK (5.85), Jai Kisan (5.95): the system was wrong on
  calibration.**
  - It credited the same behaviour the memos did (R2 at 4.5–5) and was ranked correctly
    above every pass.
  - Each landed just under the 6.0 take-call bar.
  - The fund trades thin early numbers for proven customer-first behaviour more readily
    than that bar does.
- **Prepnest: an agreement, re-examined at Kushal's request.**
  - On its own evidence the pass holds up: no 30/90-day retention, the product was the
    teacher, and the founder was defensive.
  - A competitor's later success doesn't change that file.
  - Without the founder read, the system routes it to *screen first*, which is the right
    posture for a re-look.

### What changed because of the backtest

- **One rule, rule v2: a score-based pass now requires R1 to be evidenced with at least
  medium confidence.** Otherwise the application goes to *screen first*. This is the
  breach response written into the trust contract in advance.
- **The thresholds were not retuned.** Lowering the 6.0 bar to fit these 12 would be
  overfitting.
- **Both rule versions are reported.** In this week's batch, rule v2 moved Yatrika from
  *suggest pass* to *screen first*.

### Limits of this backtest

- **It is in-sample:** the revealed lens was reconstructed from these same 12 memos.
- **The founder assessments give the verdict away in places** (CampusCredit: "That
  answer decided it").
- **The gate rules name Coinlane and Jai Kisan as examples.**
- **The scorers may recognise the companies.** The six investments are real, well-known
  companies: all are in the partners' pre-fund portfolio.
- **The sample is small.** With n = 12, the interval is wide.

Treat this as a smoke test. The real test is shadow mode on new applications, and a
re-score of Ledgerly once Riya finds the notes.

## 4. The trust contract

The full table is in `data/fund/trust_contract.json` and at the end of the report. It was
written before the batch or the backtest results were seen. Its "now" column is filled
from this run.

**What to measure before relying on it:**
- **Shadow mode** for 6 weeks or 100 applications, whichever comes later.
- **Missed calls:** 0 in the first 20, and 5% or less overall.
- **Agreement with Riya:** 80% or more.
- **Fabricated facts:** 0. A single one stops the system.
- **Citations:** 95% or more supported, and 100% of deck/form quotes verified.
- **Conflict recall:** 100%.
- **Correction reuse:** 80% or more.
- **Backtest:** 9/12 or better, with no investment marked pass. **Currently failed: 8/12.**
- **Riya's time:** 10 minutes or less per application.

**Where it breaks:**
1. **Founder behaviour under pressure.** This is what decides All In Capital's deals, and
   it is visible only on calls. The no-founder backtest shows how much of the decision
   lives there.
2. **Founders with no public footprint.** That was every applicant this week.
3. **Thesis drift.** The revealed lens lags the fund's real behaviour.
4. **Categories the fund has never decided on,** such as healthcare delivery and travel.
5. **Deeptech technical judgement.** Aditya's second call is never delegated.
6. **A 12-decision backtest.**
7. **Founders learning the rubric.** "Written rules turn into checklists." The thesis
   file and prompts stay internal.

## 5. How this run was produced

**Code.** The pipeline (`triage/`) calls Claude through the Anthropic API for two steps:
- **Research:** Claude Opus 5.5 with the server-side web search and fetch tools.
- **Scoring:** structured output parsed into the `ScoreCard` schema.

Everything else is plain Python with tests: totals, missing values, gates, routing,
conflict check, corrections, citation audit, scheduling, backtest arithmetic, and the
report (18 tests).

**This batch.** There was no API key in this environment. Agents in a Claude Code
session ran the same two steps instead:
- They followed the same prompt files.
- They used the same input packets (`data/scores/_packets/`).
- They used live web search.
- They wrote the same schemas.
- Their output passed the same validators and audits.

Every output file says so in `produced_by`. With a key, `python -m triage run --refresh`
regenerates all of it through the API.
