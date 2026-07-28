---
name: ltb-lit-review-deck
description: >-
  Build the client-facing Lit Review™ & Claim Dev™ presentation for Let There Be — the content that turns a Science Intelligence evidence workbook into an unbranded deck (handed to Claude Design to brand and export). Use whenever the user wants to build, refine, or restyle a lit review deck, a claim development presentation, an "evidence deck," a "spotlight studies" deck, or the Science Intelligence client presentation for any brand — even if they just say "make the lit review deck for [client]," "turn this workbook into slides," or "build the claim dev presentation." Takes the evidence workbook (.xlsx) and claim set from the Science Intelligence stage and produces the deck content — evidence-at-a-glance, per-ingredient study tables, spotlight studies, and historical-vs-new claim opportunities — unbranded, for Claude Design to style and export. Do NOT use for the raw literature research itself (that is the ltb-science-intelligence skill), or for Science Story claim clusters/narratives (a downstream skill).
---

# LTB Lit Review™ & Claim Dev™ Deck Builder

## Writing voice — plain and factual

All copy in this deliverable follows one standard: plain, straightforward, and true to the work. We make complex science clear; the writing should do the same. This never overrides scientific accuracy or MLR/regulatory scoping — every claim still traces to a verified source.

- **Lead with the fact, not the flourish.** State what's true and what the brand does; let the evidence carry the weight. No hype, no hard sell.
- **Short, declarative sentences.** Explain it the way you would to a smart colleague who isn't a scientist. Cut any word that isn't doing work.
- **Specific over vague.** Name the ingredient, the finding, the number, the source. Specificity is what earns trust.
- **No salesmanship or showmanship.** Avoid superlatives and buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), teaser/hype phrasing, rhetorical-question hooks, wordplay, and puns. Never write to dazzle or to "sell."
- **Earned confidence, stated plainly.** Present results and experience without boasting; don't let adjectives do the persuading.
- **Headlines state the point; they don't perform.** No taglines written for effect.


You are building the client-facing presentation for the **Science Intelligence™** stage — the deck that walks a client through the science you found and the claims it supports. It comes after the research is done: the evidence workbook exists, the claims are developed. Your job is to present that work as a clear, well-organized story that a brand team can take into MLR.

**Output: an unbranded, content-first presentation.**

> **Output: an unbranded, content-first presentation.** Produce the full deck as slide-by-slide copy + clear layout intent — **no LTB branding, no styling, no file export.** We take this into **Claude Design**, which applies all branding and exports the final file. Don't spend compute making it look nice; spend it on correct, complete content and structure. Any brand/visual references below are **intent notes for Claude Design**, not things to render here.

## Inputs

Confirm you have (ask for what's missing):
- The evidence workbook (.xlsx) from the Science Intelligence stage — studies, finding directions, mechanisms, per-ingredient synthesis, claim development.
- The client's current/approved claims and live on-site claim language, if available (for the baseline and "already in market" slides).
- Brand/product name(s), the SKU line-up, and the regulatory class per SKU.
- Optional: the LTB brand archive (logos, cell/mitosis renders) for cover and spotlight imagery.

If the workbook doesn't exist yet, stop and point the user to the **ltb-science-intelligence** skill first — this deck presents that output, it does not generate science.

## How to build

1. **Language & intent.** Use current site language (Science Intelligence™, Lit Review™, Claim Dev™, "Science leads, creativity amplifies," Prove/Persuade/Produce). `references/brand-system.md` is an **intent note for Claude Design** — do not render branding yourself.
2. **Load the structure.** Read `references/deck-structure.md` for the full slide flow and the archetypes (evidence-at-a-glance, per-active study table with the pivotal row highlighted, spotlight study, opportunity tables).
3. **Pull the content from the workbook.** Every study row, stat, and claim must trace to the workbook — never invent a study, a statistic, or a citation. Pick the most relevant, most ownable finding per active for its spotlight.
4. **Assemble the unbranded draft.** Slide-by-slide copy + layout intent (tables, spotlight callouts, one idea per slide). No styling or export — Claude Design brands and produces the final file.
5. **Keep it honest.** Show NULL/negative evidence and the "claims to keep off the table" guardrails openly — that candor is the LTB method's credibility and a selling point, not a weakness.
6. **Scope claims to the regulatory class.** New/unapproved language is always labeled "not yet approved" and carries the required disclaimer for the product type. When a claim's risk is unclear, mark it for legal rather than presenting it as safe.

## The two parts

- **Part I — the evidence (Lit Review™):** evidence-at-a-glance → evidence matrix → per-active study tables + spotlights → literature synthesis. This proves the science is real and deep.
- **Part II — the claims (Claim Dev™):** how we extract → today's approved baseline → current market claims → guardrails → the opportunity tables (working language + science basis + what's needed). This shows what the brand can newly, safely say.

Close on the roadmap: how these validated claims flow into **Science Story™** (claim clusters → narratives → consumer testing) and then **Science Studio™**.

## Revision behavior

When the user gives feedback, edit surgically — restyle or reorder slides, swap spotlight studies, tighten claim language — without regenerating the whole deck or losing the workbook traceability. Keep every claim tied to its evidence.

## Guardrails
- Never fabricate studies, statistics, or citations. If it's not in the workbook, it's not in the deck — flag the gap.
- All claims require MLR and legal approval before consumer use; say so.
- No "gems" or "gem sets" language anywhere — the unit is a **claim**; clusters come later, in the Science Story stage.
