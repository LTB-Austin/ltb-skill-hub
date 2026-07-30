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

The voice rule governs **the deck's own copy** — headlines, body, synthesis lines. Candidate consumer claim language quoted inside a claim card is the *content being presented* and may be punchier; it still carries its guardrail.

You are building the client-facing presentation for the **Science Intelligence™** stage — the deck that walks a client through the science you found and the claims it supports. It comes after the research is done: the evidence workbook exists, the claims are developed. Your job is to present that work as a clear, well-organized story that a brand team can take into MLR.

> **Output: an unbranded, content-first presentation.** Produce the full deck as slide-by-slide copy + clear layout intent + speaker notes — **no LTB branding, no styling, no file export.** We take this into **Claude Design**, which applies all branding and exports the final file. Don't spend compute making it look nice; spend it on correct, complete content and structure. Any brand/visual references below are **intent notes for Claude Design**, not things to render here.

## Inputs

Confirm you have (ask for what's missing):
- The evidence workbook (.xlsx) from the Science Intelligence stage — studies, finding directions, mechanisms, per-active or per-pillar synthesis, claim development, guardrails.
- The client's current/approved claims and live claim language, if available (for the baseline and "already in market" slides).
- Brand/product name(s), the SKU line-up, and the regulatory class per SKU.
- Optional: audience or condition-burden data, if the project has it.
- Optional: the LTB brand archive (logos, cell/mitosis renders) for cover and spotlight imagery.

If the workbook doesn't exist yet, stop and point the user to the **ltb-science-intelligence** skill first — this deck presents that output, it does not generate science.

## How to build

1. **Language & intent.** Use current site language (Science Intelligence™, Lit Review™, Claim Dev™, "Science leads, creativity amplifies," Prove/Persuade/Produce). `references/brand-system.md` is an **intent note for Claude Design** — do not render branding yourself.
2. **Load the structure.** Read `references/deck-structure.md` for the slide flow and the layout archetypes (evidence-at-a-glance, per-active study table with the pivotal row highlighted, spotlight study, opportunity tables). Treat it as the default shape, not a fixed template — adapt to what the project actually has.
3. **Pull the content from the workbook.** Every study row, stat, and claim must trace to the workbook — never invent a study, a statistic, or a citation. Pick the most relevant, most ownable finding per active/pillar for its spotlight.
4. **Organise Part I by active, or by mechanism pillar if the product's science demands it.** Default is per-active. When the actives are category-standard and the ownable science is formulation, delivery, or mechanism architecture, organise by pillar instead — and say so on the "how to read this report" slide so the client understands the choice.
5. **Assemble the unbranded draft.** Slide-by-slide copy + layout intent + a speaker note per slide. No styling or export.
6. **Keep it honest.** Show NULL/negative evidence and the guardrails openly — that candor is the LTB method's credibility, not a weakness. Where the evidence runs out, say so plainly. Where a client's existing approved claim does not survive the evidence, say that too, and show the trace.
7. **Scope claims to the regulatory class.** New/unapproved language carries a `WORKING LANGUAGE · PENDING MLR` badge and the required disclaimer for the product type. When a claim's risk is unclear, mark it for legal rather than presenting it as safe.

## The two parts

- **Part I — Lit Review™:** evidence at a glance → how to read this report → per-active/per-pillar study tables + spotlights → what the science will stand behind (including where it stops). Open on audience and condition burden when the project has that data — it frames the evidence well, but skip it rather than padding it. Any burden or audience data carries a scope note so nobody mistakes it for product substantiation.
- **Part II — Claim Dev™:** what the brand says today → current market claims → the opportunity field → guardrails → claim territories.

Close on the roadmap (including the testing decision), a Science Story™ preview, and the closing statement. If the record set is large, put it in a numbered appendix (A1, A2, …) with resolving links.

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
- All claims require MLR and legal approval before consumer use; say so on the cover and on every claim slide.
- No "gems" or "gem sets" language anywhere — the unit is a **claim**; clusters come later, in the Science Story stage.
