---
name: ltb-lit-review-deck
description: >-
  Build the client-facing Science Intelligence™ deck for Let There Be — the presentation that turns an
  evidence workbook into slides, covering both Lit Review™ (the evidence) and Claim Dev™ (the claims). Use
  whenever the user wants to build, refine, or restyle a Science Intelligence deck, a lit review deck, a claim
  development presentation, an evidence deck, a spotlight studies deck, or the client presentation for any
  brand — even if they just say make the science intelligence deck for a client, turn this workbook into
  slides, or build the claim dev presentation. Takes the evidence workbook and claim set from the Science
  Intelligence stage and produces the deck content — evidence at a glance, per-active or per-pillar study
  tables, spotlights, guardrails and claim territories — unbranded, for Claude Design to style and export. Do
  NOT use for the raw literature research (that is ltb-science-intelligence) or for Science Story claim
  clusters and narratives.
---

# LTB Science Intelligence™ Deck Builder

## What this deliverable is called

The deck is the **Science Intelligence™ presentation** (or "Science Intelligence deck"). **Lit Review™** and **Claim Dev™** are the two parts *inside* it, and they appear as the two full-slide section dividers. Do not title the deck "Lit Review & Claim Dev" — that names the parts, not the product. The cover reads:

> [PRODUCT NAME] · **SCIENCE INTELLIGENCE™** PRESENTATION · PREPARED FOR [client] | [MONTH YEAR]

## Writing voice — plain and factual

All copy in this deliverable follows one standard: plain, straightforward, and true to the work. We make complex science clear; the writing should do the same. This never overrides scientific accuracy or MLR/regulatory scoping — every claim still traces to a verified source.

- **Lead with the fact, not the flourish.** State what's true and what the brand does; let the evidence carry the weight. No hype, no hard sell.
- **Short, declarative sentences.** Explain it the way you would to a smart colleague who isn't a scientist. Cut any word that isn't doing work.
- **Specific over vague.** Name the ingredient, the finding, the number, the source. Specificity is what earns trust.
- **No salesmanship or showmanship.** Avoid superlatives and buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), teaser/hype phrasing, rhetorical-question hooks, wordplay, and puns. Never write to dazzle or to "sell."
- **Earned confidence, stated plainly.** Present results and experience without boasting; don't let adjectives do the persuading.
- **Headlines state the point; they don't perform.** Two-clause contrast headlines are house style and are fine ("Allergies are treated like a nuisance. They behave like a chronic disease."). Taglines written for effect are not.
- **Em dashes: use sparingly.** At most one per slide or section, and only when a comma or a period genuinely will not do. Default to a period and a new sentence. Never stack them for dramatic pauses or nested asides.
- **Write for marketers, not scientists.** The reader is a brand, marketing, or creative professional. Assume they are smart and busy, not that they know biology. Replace or define a technical term the first time it appears.
- **Keep the science simple and accurate.** Use plain words for mechanisms. Keep the precise term only when it carries real meaning: an ingredient name, a study design, a regulatory class, a measured result. Simplifying must never change what a finding actually says.
- **Say it once.** No restating the same point in a second clause. Cut throat-clearing openers and filler qualifiers.

The voice rule governs **the deck's own copy** — headlines, body, synthesis lines — and it is the floor for the claim language too. Candidate consumer claim language inside a claim card follows `references/copy-craft.md`: a fragment and a turn, the measurement converted to a comparison, verbs not adjectives, one idea per line. That is as far off the floor as it goes. It still carries its guardrail.

## Reference files

| File | Read it when |
|---|---|
| `references/claim-set-contract.md` | First. Defines the Claim Set this deck presents and the ID scheme it must display unchanged. |
| `references/deck-structure.md` | Building the slide flow. |
| `references/copy-craft.md` | Before writing or tightening any claim line, evidence sentence, guardrail, or "what we could say" translation. |
| `references/brand-system.md` | Intent notes for Claude Design only. |

You are building the client-facing presentation for the **Science Intelligence™** stage — the deck that walks a client through the science you found and the claims it supports. It comes after the research is done: the evidence workbook exists, the claims are developed. Your job is to present that work as a clear, well-organized story that a brand team can take into MLR.

> **Output: an unbranded, content-first presentation.** Produce the full deck as slide-by-slide copy + clear layout intent + speaker notes — **no LTB branding, no styling, no file export.** We take this into **Claude Design**, which applies all branding and exports the final file. Don't spend compute making it look nice; spend it on correct, complete content and structure. Any brand/visual references below are **intent notes for Claude Design**, not things to render here.

## Inputs

Confirm you have (ask for what's missing):
- The evidence workbook (`[Brand]_Evidence_Workbook.xlsx`) and the Claim Set (`[Brand]_Claim_Set.md` or the Claim Development tab) from the Science Intelligence stage. The Claim Set is the source for every claim line, ID, evidence sentence, guardrail, disclaimer, and sharper version in Part II. Its shape is in `references/claim-set-contract.md`.
- The client's current/approved claims and live claim language, if available (for the baseline and "already in market" slides).
- Brand/product name(s), the SKU line-up, and the regulatory class per SKU.
- Optional: audience or condition-burden data, if the project has it.
- Optional: the LTB brand archive (logos, cell/mitosis renders) for cover and spotlight imagery.

If the workbook doesn't exist yet, stop and point the user to the **ltb-science-intelligence** skill first — this deck presents that output, it does not generate science. If the Claim Set exists but claims are missing IDs, sharper versions, or word-level guardrails, say which and either send it back or mark those cards `Incomplete`; don't write the missing parts here as if they were verified.

## How to build

1. **Language & intent.** Use current site language (Science Intelligence™, Lit Review™, Claim Dev™, "Science leads, creativity amplifies," Prove/Persuade/Produce). `references/brand-system.md` is an **intent note for Claude Design** — do not render branding yourself.
2. **Load the structure.** Read `references/deck-structure.md` for the slide flow and the layout archetypes (evidence-at-a-glance, per-active study table with the pivotal row highlighted, spotlight study, opportunity tables). Treat it as the default shape, not a fixed template — adapt to what the project actually has.
3. **Pull the content from the workbook.** Every study row, stat, and claim must trace to the workbook — never invent a study, a statistic, or a citation. Pick the most relevant, most ownable finding per active/pillar for its spotlight.
4. **Organise Part I by active, or by mechanism pillar if the product's science demands it.** Default is per-active. When the actives are category-standard and the ownable science is formulation, delivery, or mechanism architecture, organise by pillar instead — and say so on the "how to read this report" slide so the client understands the choice.
5. **Assemble the unbranded draft.** Slide-by-slide copy + layout intent + a speaker note per slide. No styling or export.
6. **Keep it honest.** Show NULL/negative evidence and the guardrails openly — that candor is the LTB method's credibility, not a weakness. Where the evidence runs out, say so plainly. Where a client's existing approved claim does not survive the evidence, say that too, and show the trace.
7. **Scope claims to the regulatory class.** New/unapproved language carries a `WORKING LANGUAGE · PENDING MLR` badge and the required disclaimer for the product type. When a claim's risk is unclear, mark it for legal rather than presenting it as safe.
8. **Write Part II to the craft.** Each lead claim direction gets the full anatomy in `references/deck-structure.md`: the lead claim, an element-by-element table showing what substantiates each part of the sentence, a sharper version, and a one-line "what changed." Every consumer line passes the `copy-craft.md` §12 self-edit before it goes on a slide. Tightening a line means keeping the same Claim ID and the same evidence; if tightening adds a promise or drops a hedge, it is a derived claim and is labeled `Derived / unscored`.
9. **Subtract what the client already owns.** Check every opportunity against the client's current claims list. A claim they already have approved is not an opportunity; say how many were removed for that reason and how many were withdrawn on regulatory grounds, and offer to walk through the withdrawn ones.

## The two parts

- **Part I — Lit Review™:** evidence at a glance → how to read this report → per-active/per-pillar study tables + spotlights → what the science will stand behind (including where it stops). Open on audience and condition burden when the project has that data — it frames the evidence well, but skip it rather than padding it. Any burden or audience data carries a scope note so nobody mistakes it for product substantiation.
- **Part II — Claim Dev™:** what the brand says today → current market claims → the opportunity field → guardrails → claim territories.

Close on the roadmap (including the testing decision), a Science Story™ preview, and the closing statement. If the record set is large, put it in a numbered appendix (A1, A2, …) with resolving links.

## Moves worth making when the material supports them

These land well with clients. Use them when the workbook genuinely supports them — don't manufacture them:

- **The multiplier.** If a defensible ratio or comparison exists, give it a comparison table and a card carrying the headline figure, with the arithmetic disclosed and flagged as directional framing pending MLR.
- **Translating the numbers.** A three-column table — `What was measured → What the consumer hears → Claim ID`. Trials speak in NNT, hazard ratios, and effect sizes; consumers don't. The conversion follows `copy-craft.md` §3: percentages become fractions or comparisons, ratios show their arithmetic in the footnote, small-n and subgroup figures lose their percentage, some numbers are not used at all. Never bend what the number means.
- **Evidence statements, kept separate.** Findings too useful to leave in the workbook but not claims (burden data, category facts, the brand's own published methods) go on a slide labeled `EVIDENCE, NOT CLAIM LANGUAGE`: the finding, its source, no product benefit. Keeping them apart is what stops a category finding being read as a brand claim.
- **Where the evidence stops.** A card or slide naming what the evidence will not support. Strongly recommended at the end of Part I — it is the credibility of the method.

## Claim IDs

IDs come from the Claim Set and are displayed unchanged. This deck never assigns, renumbers, or re-prefixes an ID. Whether the project uses `CLM-nn` or territory-prefixed IDs (`PC1`, `LC-02`) was decided in Science Intelligence; the deck, the workbook, and the client's shortlist all use the same one. If a claim is cut in revision, it shows as `Retired` in the Claim Set rather than disappearing.

## Revision behavior

When the user gives feedback, edit surgically — restyle or reorder slides, swap spotlight studies, tighten claim language — without regenerating the whole deck or losing the workbook traceability. Keep every claim tied to its evidence and its ID.

## Definition of done

Before handing the draft over, check and report in a few plain lines:

- Every claim on every Part II slide carries its Claim ID from the Claim Set, unchanged.
- Every lead claim direction has the full anatomy: lead claim, element-by-element substantiation table with a status per element, sharper version, "what changed."
- Every consumer line passes `copy-craft.md` §12: no raw percentages, units, or decimals; one idea per line; qualifier matches the design; hedges kept; comparator by molecule; prevalence never in the same sentence as the brand.
- Every guardrail names words to keep or avoid.
- Every number in a consumer line has its derivation in a footnote or the evidence sentence.
- Evidence statements sit on their own labeled slide, not among the claims.
- Opportunities already on the client's approved list have been removed and the count stated.
- NULL evidence and "where the evidence stops" are present.
- Working language badge and disclaimer on every claim slide; MLR line on the cover.

## Guardrails
- Never fabricate studies, statistics, or citations. If it's not in the workbook, it's not in the deck — flag the gap.
- All claims require MLR and legal approval before consumer use; say so on the cover and on every claim slide.
- No "gems" or "gem sets" language anywhere — the unit is a **claim**; clusters come later, in the Science Story stage.
