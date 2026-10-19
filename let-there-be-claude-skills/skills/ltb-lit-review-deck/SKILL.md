---
name: ltb-lit-review-deck
description: Build the client-facing Science Intelligence™ deck for Let There Be — the presentation that turns an evidence workbook into slides, covering both Lit Review™ (the evidence) and Claim Dev™ (the claims). Use whenever the user wants to build, refine, or restyle a Science Intelligence deck, a lit review deck, a claim development presentation, an evidence deck, a spotlight studies deck, or the client presentation for any brand — even if they just say make the science intelligence deck for a client, turn this workbook into slides, or build the claim dev presentation. Takes the evidence workbook and claim set and produces a territory-first deck as one markdown content brief plus CSV chart data, where each claim territory runs The Claim → The Evidence → Compliance Logic, unbranded, for Claude Design to style and export. Do NOT use for the raw literature research (that is ltb-science-intelligence) or for Science Story claim clusters and narratives.
---

# LTB Science Intelligence™ Deck Builder

## What this deliverable is called

The deck is the **Science Intelligence™ presentation**. **Lit Review™** and **Claim Dev™** are the two parts inside it; in the territory-first format they appear as the `LIT REVIEW™ | CLAIM DEV™` lockup on every territory slide and on the Results divider, not as separate halves of the deck. The cover reads:

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

You are building the client-facing presentation for the **Science Intelligence™** stage. The evidence workbook exists and the claims are developed. Your job is to present that work so a brand team can pick territories and take them into MLR.

> **Output: one markdown content brief + CSV files for every chart.** Write the deck slide by slide in a single `.md` file, with copy, layout intent and the data each visual needs. Put chart data in CSVs (one per chart or tile set) in a sibling `[brand]_si_deck_data/` folder and name the CSV on the slide that uses it. **No LTB branding, no styling, no file export.** Claude Design builds the deck from the markdown and CSVs. `references/brand-system.md` is intent for Design, not something to render.

## The format: territory-first (default)

Present claims first, then the evidence behind each one, then the case for MLR. Do **not** open with a literature walk-through. Every claim territory runs three slides:

1. **The Claim** (for the brand team): hero claim card, "Why this claim matters to [brand]", and **Other ways to say it**, 3–5 register variants, each tagged (SHORT, NUMBER-FORWARD, LABEL, REGULATOR'S WORDS, DIRECT, MORE POINTED · BRAND'S CALL, HCP).
2. **The Evidence** (for MLR and the brand): one hero data tile (big number + one-line meaning + study and evidence basis), one visual that shows how we got there, and an "On the label" or regulator-quote line. Add a method slide only when the number needs walking through (e.g., an original analysis).
3. **Compliance Logic** (for MLR): 4–6 tiles, each a short bold title + 1–2 sentences. Why the sources hold up, why the framing is safe, what the counter-evidence is, what's still open before MLR. End with risk and substantiation depth.

Read `references/deck-structure.md` for the full flow, and `references/evidence-visuals.md` to choose each territory's visual and format its CSV.

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
3. **Group claims into 4–6 territories.** A territory is one idea a brand could own. Lead with the strongest, best-substantiated one. A territory that only works for HCPs becomes a single "potential future HCP campaign" slide after the consumer territories.
4. **Choose each territory's evidence visual on purpose.** Match the visual to the shape of the evidence (comparison, share of a group, range, label-by-label, steps). Write its CSV. Never chart a number you can't trace.
5. **Show counter-evidence on the evidence slide** in a small outlined "honest line" card when a result runs the other way, and name it again in Compliance Logic. Candor is the method's credibility.
6. **Add "Your legacy claims, strengthened"** whenever the client's approved claims are known: legacy line → strengthened line → territory. Look for them in project files before asking.
7. **Close** with an owner-tagged "What happens next", an example Science Story slide (score dials as placeholders unless real data exists), any open calls for the client, and the appendix: source list CSV, label/regulator capture table, regulatory notes and required disclaimers.
8. **Scope every claim to the regulatory class.** Working language carries `WORKING LANGUAGE · PENDING MLR` (or the client's review body, e.g. PRC). A hero number resting on an abstract-only study is flagged as blocking in Compliance Logic.

`references/legacy-deck-structure.md` keeps the older Part I (Lit Review) / Part II (Claim Dev) flow. Use it only if the user asks for that format.

## Moves worth making when the material supports them

These land well with clients. Use them when the workbook genuinely supports them — don't manufacture them:

- **The multiplier.** If a defensible ratio or comparison exists, give it a comparison table and a card carrying the headline figure, with the arithmetic disclosed and flagged as directional framing pending MLR.
- **Translating the numbers.** A three-column table — `The clinical finding → What we could say → Claim ID`. Trials speak in NNT, hazard ratios, and effect sizes; consumers don't. Show the derivation, footnote it, and never bend what the number means.
- **Where the evidence stops.** A card or slide naming what the evidence will not support. Strongly recommended at the end of Part I — it is the credibility of the method.

## Claim ID convention

Give every claim a territory-prefixed ID so the deck, the workbook, and the client's shortlist stay cross-referenceable: `PC1`, `PC2` (period cramps), `DA1` (dual action), `HA1` (headache). Two to three letters for the territory, then a number. Keep IDs stable across revisions — if a claim is cut, retire its ID rather than reusing it.

## Revision behavior

When the user gives feedback, edit surgically — restyle or reorder slides, swap spotlight studies, tighten claim language — without regenerating the whole deck or losing the workbook traceability. Keep every claim tied to its evidence and its ID.

## Guardrails
- Never fabricate studies, statistics, or citations. If it's not in the workbook, it's not in the deck — flag the gap.
- All claims require MLR and legal approval before consumer use; say so on every claim slide and in the appendix disclaimers.
- No "gems" or "gem sets" language anywhere — the unit is a **claim**; clusters come later, in the Science Story stage.
