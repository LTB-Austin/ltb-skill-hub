---
name: ltb-lit-review-deck
description: >-
  Build the client-facing Science Intelligence™ deck for Let There Be — the presentation that turns an
  evidence workbook into slides, covering both Lit Review™ (the evidence) and Claim Dev™ (the claims). Use
  whenever the user wants to build, refine, or restyle a Science Intelligence deck, a lit review deck, a claim
  development presentation, an evidence deck, a spotlight studies deck, or the client presentation for any
  brand — even if they just say make the science intelligence deck for a client, turn this workbook into
  slides, or build the claim dev presentation. Takes the evidence workbook and claim set from the Science
  Intelligence stage and produces the deck content — the headline finding, a claim board, one chapter per
  priority direction pairing each claim with the studies that hold it up, the guardrails, and the full evidence
  record at the back — unbranded, for Claude Design to style and export. Do
  NOT use for the raw literature research (that is ltb-science-intelligence) or for Science Story claim
  clusters and narratives.
---

# LTB Science Intelligence™ Deck Builder

## What this deliverable is called

The deck is the **Science Intelligence™ presentation** (or "Science Intelligence deck"). **Lit Review™** and **Claim Dev™** are the two parts *inside* it, and they appear as the two full-slide section dividers. Claim Dev™ is the spine of the deck and comes first; Lit Review™ is the record and comes after. Do not title the deck "Lit Review & Claim Dev" — that names the parts, not the product. The cover reads:

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

You are building the client-facing presentation for the **Science Intelligence™** stage — the deck that walks a client through the science you found and the claims it supports. It comes after the research is done: the evidence workbook exists, the claims are developed. Your job is to present that work so a brand team sees, within the first three minutes, what the science lets them say, sees every claim next to the evidence that holds it up, and leaves the meeting having picked the three directions Science Story will build on. This deck is presented live in a one-hour meeting. It is a conversation with a decision at the end, not a report read aloud.

> **Output: an unbranded, content-first presentation.** Produce the full deck as slide-by-slide copy + clear layout intent + speaker notes — **no LTB branding, no styling, no file export.** We take this into **Claude Design**, which applies all branding and exports the final file. Don't spend compute making it look nice; spend it on correct, complete content and structure. Any brand/visual references below are **intent notes for Claude Design**, not things to render here.

## Inputs

Confirm you have (ask for what's missing):
- The evidence workbook (`[Brand]_Evidence_Workbook.xlsx`) and the Claim Set (`[Brand]_Claim_Set.md` or the Claim Development tab) from the Science Intelligence stage. The Claim Set opens with **the Board**: the headline finding, the ranked priority directions with deck status, and the field counts. Slide 3, the claim board, the chapter order, and the footer counts come straight from it. The per-claim blocks are the source for every claim line, ID, pivotal study, consumer translation, honest line, guardrail, disclaimer, and sharper version. Its shape is in `references/claim-set-contract.md`.
- The client's current/approved claims and live claim language, if available (for the baseline and "already in market" slides).
- Brand/product name(s), the SKU line-up, and the regulatory class per SKU.
- Optional: audience or condition-burden data, if the project has it.
- Optional: the LTB brand archive (logos, cell/mitosis renders) for cover and spotlight imagery.

If the workbook doesn't exist yet, stop and point the user to the **ltb-science-intelligence** skill first — this deck presents that output, it does not generate science. If the Claim Set has no Board (an older workbook), say so and offer two paths: send it back to Science Intelligence for Phase 6b, or build a provisional Board here by applying the ranking rule in the contract, labeled `PROVISIONAL — rank not yet in Claim Set`, and write it back into the Claim Set so the files stay in sync. If claims are missing IDs, pivotal studies, consumer translations, honest lines, sharper versions, or word-level guardrails, say which and either send it back or mark those cards `Incomplete`; don't write the missing parts here as if they were verified.

## How to build

1. **Language & intent.** Use current site language (Science Intelligence™, Lit Review™, Claim Dev™, "Science leads, creativity amplifies," Prove/Persuade/Produce). `references/brand-system.md` is an **intent note for Claude Design** — do not render branding yourself.
2. **Load the structure.** Read `references/deck-structure.md` for the slide flow and the layout archetypes. The shape is: three-slide open with the headline finding, the claim board, one short chapter per priority direction (the claim, then its proof, side by side), the rest of the field and the guardrails, the evidence record, and a closing ask for the client's top three. Treat it as the default shape, not a fixed template — adapt to what the project actually has.
3. **Pull the content from the workbook.** Every study row, stat, and claim must trace to the workbook — never invent a study, a statistic, or a citation. The headline slide is the Board's headline finding; each chapter's spotlight is that claim's Pivotal study field; the "what the consumer hears" line is its Consumer translation; the honest line is its Honest line. Present these fields; do not rewrite them.
4. **Organise the main body by claim direction, not by active.** The directions and their order come from the Board in the Claim Set; do not re-rank them here. Give each a chapter. Every study in the main body appears next to the claim it supports. The per-active (or per-pillar) study tables still exist, in full, in the appendix and in the evidence record; that is where the client and MLR go for the complete list. When the ownable science is formulation, delivery, or mechanism rather than the actives themselves, the record is organised by pillar instead, and slide 15 says so.
5. **Assemble the unbranded draft.** Slide-by-slide copy + layout intent + a speaker note per slide. No styling or export.
6. **Keep it honest.** Show NULL/negative evidence and the guardrails openly — that candor is the LTB method's credibility, not a weakness. Where the evidence runs out, say so plainly. Where a client's existing approved claim does not survive the evidence, say that too, and show the trace.
7. **Scope claims to the regulatory class.** New/unapproved language carries a `WORKING LANGUAGE · PENDING MLR` badge and the required disclaimer for the product type. When a claim's risk is unclear, mark it for legal rather than presenting it as safe.
8. **Write the chapters to the craft.** Each lead claim direction gets the full anatomy in `references/deck-structure.md`: the lead claim with its consumer translation and sharper version on one slide, then the element-by-element substantiation table, the pivotal study, the supporting rows, the honest line, and the payoff line on the next. Every consumer line passes the `copy-craft.md` §12 self-edit before it goes on a slide. Tightening a line means keeping the same Claim ID and the same evidence; if tightening adds a promise or drops a hedge, it is a derived claim and is labeled `Derived / unscored`.
9. **Subtract what the client already owns.** Check every opportunity against the client's current claims list. A claim they already have approved is not an opportunity; say how many were removed for that reason and how many were withdrawn on regulatory grounds, and offer to walk through the withdrawn ones.
10. **Write the speaker notes as a talk track.** Each note carries its time budget and the two or three sentences to say. Chapter openers end with the question to ask the client. The closing "Your call" note tells the presenter how to run the room and land at least three named directions. The deck exists to get that pick; the notes are how it gets it.

## The shape

- **Open (three slides):** cover → what you're about to see (the four numbers, how the deck is ordered, the ask) → the headline finding and the claim it becomes.
- **Part I — the claim board (Claim Dev™):** every priority direction on one slide with its lead claim, evidence count, and status; then where the client stands today, then what the category says today (the Category Language Map from the scan).
- **Part II — the chapters:** one per priority direction, two slides each (the claim; the proof), a third when the material earns it. Claim and evidence are never separated.
- **Part III — the rest of the field:** the full claim library, where the evidence stops, and evidence statements kept apart from claims.
- **Part IV — the record (Lit Review™):** evidence at a glance, the matrix with direction numbers overlaid, the formula map, the synthesis. Brief live; the client keeps it.
- **Close:** the claim board again as a scorecard with the ask for three, what happens next, closing statement. Appendix holds the per-active tables, the full study list, and regulatory notes.

Audience or condition-burden data, when the project has it, goes on the `EVIDENCE, NOT CLAIM LANGUAGE` slide or inside the chapter it frames, with a scope note. It does not get its own opening section.

## Moves worth making when the material supports them

These land well with clients. Use them when the workbook genuinely supports them — don't manufacture them:

- **The multiplier.** If a defensible ratio or comparison exists, give it a comparison table and a card carrying the headline figure, with the arithmetic disclosed and flagged as directional framing pending MLR.
- **Translating the numbers.** Built into every chapter opener as the "what the consumer hears" line. Trials speak in NNT, hazard ratios, and effect sizes; consumers don't. The conversion follows `copy-craft.md` §3: percentages become fractions or comparisons, ratios show their arithmetic in the footnote, small-n and subgroup figures lose their percentage, some numbers are not used at all. Never bend what the number means. A standalone three-column table (`What was measured → What the consumer hears → Claim ID`) can sit in Part III when several directions share a numeric story.
- **Evidence statements, kept separate.** Findings too useful to leave in the workbook but not claims (burden data, category facts, the brand's own published methods) go on a slide labeled `EVIDENCE, NOT CLAIM LANGUAGE`: the finding, its source, no product benefit. Keeping them apart is what stops a category finding being read as a brand claim.
- **Where the evidence stops.** Required, in Part III. A card per line the evidence will not support. It is the credibility of the method. When the workbook contains a clear negative on a widely assumed benefit, consider giving it its own chapter labeled `WHAT NOT TO SAY, AND WHY`.

## Claim IDs

IDs come from the Claim Set and are displayed unchanged. This deck never assigns, renumbers, or re-prefixes an ID. Whether the project uses `CLM-nn` or territory-prefixed IDs (`PC1`, `LC-02`) was decided in Science Intelligence; the deck, the workbook, and the client's shortlist all use the same one. If a claim is cut in revision, it shows as `Retired` in the Claim Set rather than disappearing.

## Revision behavior

When the user gives feedback, edit surgically — restyle or reorder slides, swap spotlight studies, tighten claim language — without regenerating the whole deck or losing the workbook traceability. Keep every claim tied to its evidence and its ID.

## Definition of done

Before handing the draft over, check and report in a few plain lines:

- The headline finding is on slide 3, and the front matter is three slides.
- "What the category says today" is present, built from the Competitive Intel tab, or is a single honest line that the scan did not run. Every competitor quote carries source and date.
- The claim board appears twice: as the map in Part I and as the scorecard in the close, with the ask for three directions stated plainly.
- No study appears in the main body without the claim it supports; every Part II evidence slide ends with a payoff line carrying a Claim ID.
- Speaker notes are a talk track with time budgets, and each chapter opener ends with a question for the client.
- Every claim on every claim slide carries its Claim ID from the Claim Set, unchanged.
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
