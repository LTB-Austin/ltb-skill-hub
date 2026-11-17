---
name: ltb-lit-review-deck
description: Build the client-facing Science Intelligence™ deck for Let There Be, the presentation that turns an evidence workbook into slides covering Lit Review™ (the evidence) and Claim Dev™ (the claims). Use whenever the user wants to build, refine or restyle a Science Intelligence deck, lit review deck, claim development presentation or evidence deck for any brand, even if they just say "make the science intelligence deck for [client]," "turn this workbook into slides" or "build the claim dev presentation." Every claim direction runs Hero Claim → Supporting Claims → The Evidence → Compliance Logic, the same format the Sales Preview and SOW show. It writes a markdown brief and CSV chart data first, then builds the finished deck in the LTB Science Intelligence template in the same run. Do NOT use for the raw literature research (ltb-science-intelligence) or for Science Story claim clusters and narratives.
---

# LTB Science Intelligence™ Deck Builder

## How this skill finishes: the deck, in one run

**Every run of this skill ends with a finished presentation built in the LTB Template — Science Intelligence (Lit Review + Claim Dev) (https://claude.ai/artifact/3eLTXv8dToy1DrofTGXhxk). Don't stop at the markdown.**

1. Do the work below and write the markdown content brief and its chart CSVs. That's the working draft the deck is built from. It isn't the deliverable on its own.
2. As soon as it's complete, build the deck in the template by following `references/template-build.md`. Do this in the same run. Don't ask whether to continue, and don't wait for the user to ask for slides.
3. Finish by giving the user the deck link. Never tell them to take the file into Claude Design, and never suggest they ask for a slide deck.

Wherever this skill mentions Claude Design, a design template, an "unbranded" or "content-first" output, or a markdown brief, it means the content draft that feeds this build step. Every rule about content still applies in full: what goes on each screen, exact wording, and gap markers.

Pause before building the deck only in three cases: the skill below requires an approval first, an input the deck needs is missing, or the user asks for content only.

## What this deliverable is called

The deck is the **Science Intelligence™ presentation**. **Lit Review™** and **Claim Dev™** are the two parts inside it; in the direction-first format they appear as the `LIT REVIEW™ | CLAIM DEV™` lockup on the Highlights (Results) slide, not as separate halves of the deck. The cover reads:

> [PRODUCT NAME]® Claims · **SCIENCE INTELLIGENCE™** PRESENTATION · PREPARED FOR [client] | [brand] | PREPARED BY LET THERE BE · [MONTH YEAR]

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

The voice rule governs **the deck's own copy** — headlines, body, synthesis lines. Candidate consumer claim language quoted inside a claim card is the *content being presented* and may be punchier; it still carries its guardrail.

You are building the client-facing presentation for the **Science Intelligence™** stage. The evidence workbook exists and the claims are developed. Your job is to present that work so a brand team can pick directions and take them into MLR.

> **Output: one markdown content brief + CSV files for every chart.** Write the deck slide by slide in a single `.md` file, with copy, layout intent and the data each visual needs. Put chart data in CSVs (one per chart or tile set) in a sibling `[brand]_si_deck_data/` folder and name the CSV on the slide that uses it. **No LTB branding or styling in the brief.** The deck is then built from the markdown and CSVs in the LTB template, in the same run (see the top of this skill). `references/brand-system.md` is design intent, not something to render.

## The format: direction-first (default)

Present claims first, then the evidence behind them, then the case for MLR. Do **not** open with a literature walk-through. Every claim direction runs **four parts**, in this order:

1. **Hero Claim** (for the brand team): the hero claim card, carrying its ID, its tier, who it speaks to, what it carries (Study / Survey / Label / Comparative), and its substantiation tag. Beside it goes "Why this matters to [Brand]" in 2–3 sentences.
2. **Supporting Claims** (for the brand team): 3–4 other ways to say the hero claim, in a 2×2 grid. Each card has a register tag (Number-forward, Short, [Brand] voice, Label, Regulator's words, HCP, Names a competitor (legal), Bolder voice · brand's call), a tier, an ID, the line, what it carries and its substantiation tag. A summary pill under the grid counts the related lines in the library.
3. **The Evidence** (for legal and the brand): one hero data tile (eyebrow = source type and date, a big number, a one-line meaning, a source tag) and "The science" cards (a finding, a design line, a source tag). Under them goes "The honest line": the counter-evidence, with its design and an `Abstract only` flag where true. When the number needs more than one slide, add `The Evidence 2`, `The Evidence 3` with short titles of their own (e.g. "30g vs 90g").
4. **Compliance Logic** (for legal): six tiles, each a bold title plus 1–2 sentences, covering why the sources hold up, the framing, what the claim must not say, the counter-evidence, and what's still open before MLR. It ends with a `Risk` line per claim ID and a `Depth` line.

**Tiers.** Every claim carries one tier, defined on the "How each direction runs" slide:
- **Core:** accurate and sourced, resting on an ingredient list or a label fact.
- **Push:** accurate and sourced, comparing the brand to a competitor or naming one.
- **Stretch:** accurate and sourced, pairing a brand or product with a health finding.

Separately, risk (LOW / MEDIUM / HIGH) goes on the Compliance Logic slide.

**One format, preview to SOW to delivery.** The Sales Preview shows one territory with its hero claim, other ways to say it, and the evidence with an honest line, sources blurred. It has no compliance slide; that reasoning stays in its speaker notes. The SOW shows this deck's four-part format so the client knows what's coming. This deck delivers every direction in full, compliance logic included, with real source tags. Keep the part names, tier names and order consistent, so the client recognizes the format from the first meeting.

Read `references/deck-structure.md` for the full flow, and `references/evidence-visuals.md` to choose each direction's evidence visual and format its CSV.

## Inputs

Confirm you have (ask for what's missing):
- The evidence workbook (.xlsx) from the Science Intelligence stage — studies, finding directions, mechanisms, per-active or per-pillar synthesis, claim development, guardrails.
- The client's current/approved claims and live claim language, if available (for the baseline and "already in market" slides).
- Brand/product name(s), the SKU line-up, and the regulatory class per SKU.
- Optional: audience or condition-burden data, if the project has it.
- Optional: the LTB brand archive (logos, cell/mitosis renders) for cover and spotlight imagery.

If the workbook doesn't exist yet, stop and point the user to the **ltb-science-intelligence** skill first — this deck presents that output, it does not generate science.

## How to build

1. **Load the structure** (`references/deck-structure.md`) and the visual guide (`references/evidence-visuals.md`).
2. **Pull everything from the workbook.** Every number, quote and claim traces to a workbook row or an official page read directly. Give every source a deck ID (S-001…) that matches the appendix CSV. Never invent a study, statistic or citation.
3. **Group claims into directions.** A direction is one idea a brand could own, with one hero claim and 3–4 supporting claims. Lead with the strongest, best-substantiated one. When the scope covers more than one product, group the directions into parts (Part A, Part B), one per product, with IDs A1, A2… B1, B2…. A direction that only works for HCPs or a future audience becomes a single "potential future audience" slide after the consumer directions.
4. **Choose each direction's evidence visual on purpose.** Match the visual to the shape of the evidence (comparison, share of a group, range, label-by-label, steps). Write its CSV. Never chart a number you can't trace.
5. **Show counter-evidence on the evidence slide** in "The honest line" strip whenever a result runs the other way, and name it again in Compliance Logic. Candor is the method's credibility.
6. **Add "Your legacy claims, strengthened"** whenever the client's approved claims are known: legacy line → strengthened line → direction. Look for them in project files before asking.
7. **Close** with the part libraries and the full library, any potential future audience, "What happens next" with owner tags, the closing slide, and "Where the evidence stops." Then the appendix: how to check any claim, the source list CSV, label capture, regulatory notes and required disclaimers, the claim index, and the label facts to confirm. See `references/deck-structure.md`.
8. **Scope every claim to the regulatory class.** Working language carries `WORKING LANGUAGE · PENDING MLR` (or the client's review body, e.g. PRC). A hero number resting on an abstract-only study is flagged as blocking in Compliance Logic.

`references/legacy-deck-structure.md` keeps the older Part I (Lit Review) / Part II (Claim Dev) flow. Use it only if the user asks for that format.

## Moves worth making when the material supports them

These land well with clients. Use them when the workbook genuinely supports them — don't manufacture them:

- **The multiplier.** If a defensible ratio or comparison exists, give it a comparison table and a card carrying the headline figure, with the arithmetic disclosed and flagged as directional framing pending MLR.
- **Translating the numbers.** A three-column table — `The clinical finding → What we could say → Claim ID`. Trials speak in NNT, hazard ratios, and effect sizes; consumers don't. Show the derivation, footnote it, and never bend what the number means.
- **Where the evidence stops.** A card or slide naming what the evidence will not support. Strongly recommended at the end of Part I — it is the credibility of the method.

## Claim ID convention

Give every claim a direction-prefixed ID so the deck, the workbook, and the client's shortlist stay cross-referenceable: `PC1`, `PC2` (period cramps), `DA1` (dual action), `HA1` (headache). Two to three letters for the direction, then a number. Keep IDs stable across revisions — if a claim is cut, retire its ID rather than reusing it.

## Revision behavior

When the user gives feedback, edit surgically — restyle or reorder slides, swap spotlight studies, tighten claim language — without regenerating the whole deck or losing the workbook traceability. Keep every claim tied to its evidence and its ID.

## Guardrails
- Never fabricate studies, statistics, or citations. If it's not in the workbook, it's not in the deck — flag the gap.
- All claims require MLR and legal approval before consumer use; say so on every claim slide and in the appendix disclaimers.
- No "gems" or "gem sets" language anywhere — the unit is a **claim**; clusters come later, in the Science Story stage.
