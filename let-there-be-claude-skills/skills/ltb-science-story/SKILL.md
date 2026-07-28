---
name: ltb-science-story
description: >-
  Build the Science Story™ deliverable for Let There Be — assemble verified claims into Claim Clusters, write the creative narratives, and produce the client-facing presentation, built so narratives/headlines/claims can be consumer-tested. Use whenever the user wants to build or refine a Science Story, assemble claim clusters, write story/claim narratives, create a claim-opportunities or science-story deck, turn client feedback and seed ideas into strategic directions, or prep stimuli for consumer testing — even if they just say "make the science story for [client]," "cluster these claims," or "build the claim clusters deck." Handles Stage 1 (Claim Cluster selection) and Stage 2 (Science Story with narratives, claim bodies, source cards, and a test plan). Replaces the retired gem-sets and polished-gems skills. Output is an unbranded content-first presentation for Claude Design (which brands and exports). Do NOT use for raw research (ltb-science-intelligence) or the evidence/claim-dev deck (ltb-lit-review-deck).
---

# LTB Science Story™ — Claim Clusters, Narratives & Testing

## Writing voice — plain and factual

All copy in this deliverable follows one standard: plain, straightforward, and true to the work. We make complex science clear; the writing should do the same. This never overrides scientific accuracy or MLR/regulatory scoping — every claim still traces to a verified source.

- **Lead with the fact, not the flourish.** State what's true and what the brand does; let the evidence carry the weight. No hype, no hard sell.
- **Short, declarative sentences.** Explain it the way you would to a smart colleague who isn't a scientist. Cut any word that isn't doing work.
- **Specific over vague.** Name the ingredient, the finding, the number, the source. Specificity is what earns trust.
- **No salesmanship or showmanship.** Avoid superlatives and buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), teaser/hype phrasing, rhetorical-question hooks, wordplay, and puns. Never write to dazzle or to "sell."
- **Earned confidence, stated plainly.** Present results and experience without boasting; don't let adjectives do the persuading.
- **Headlines state the point; they don't perform.** No taglines written for effect.


You are building the **Persuade** stage of the Science Marketing Engine. Verified claims come in from Science Intelligence; the client has reacted to the lit-review/claim-dev deck and given seed ideas and preferences. Your job is to turn that into **Claim Clusters** (strategic directions), write **narratives** that make the science clear, and package it so the strongest directions can be **tested with consumers** before one goes to production.

**Output: an unbranded, content-first presentation.** This skill replaces the retired "Gem Sets" and "Polished Gems" skills — the unit is a **claim**, the package is a **claim cluster**. Never use "gem" language.

> **Output: an unbranded, content-first presentation.** Produce the full deck as slide-by-slide copy + clear layout intent — **no LTB branding, no styling, no file export.** We take this into **Claude Design**, which applies all branding and exports the final file. Don't spend compute making it look nice; spend it on correct, complete content and structure. Any brand/visual references below are **intent notes for Claude Design**, not things to render here.

## Two stages — figure out which one you're in

- **Stage 1 — Claim Cluster Selection:** the client hasn't picked a direction yet. Build the selection deck: 2–4 meaningfully different clusters, each a strategic direction + narrative anchor + short narrative + 2–4 claims. The client picks one. → `references/stage1-clusters.md`
- **Stage 2 — Polished Science Story:** the client has chosen a direction (and given feedback). Build the polished deck: narrative(s) lead, then claim bodies + source cards + claim opportunities, plus a test plan. → `references/stage2-science-story.md`

If it's ambiguous, ask which stage. Most projects run Stage 1, get feedback, then Stage 2.

## Inputs

Confirm you have (ask for what's missing):
- The verified claim set + evidence workbook from Science Intelligence (the source of truth for every claim and citation).
- The client's feedback on the lit-review/claim-dev deck and their **seed ideas** (directions or claims they liked). This is what you cluster around.
- Brand/product name(s), SKU line-up, regulatory class per SKU, and the activation deliverables in scope (for the roadmap).
- Optional: the LTB brand archive (logos, cell/mitosis renders).

If there's no verified claim set yet, stop and point the user to **ltb-science-intelligence** (research) and **ltb-lit-review-deck** (the deck the client reacts to) first.

## How to build

1. **Language & intent** — use current site language. `references/brand-system.md` is an **intent note for Claude Design**, not something to render here.
2. **Load the right stage reference** — Stage 1 or Stage 2 above.
3. **Cluster around what the client liked.** Build clusters from the claims/directions the client reacted well to, plus the strongest verified claims. You may write new claims that *build on* liked ones — but only if the science supports them; every claim still traces to a verified source. Deliberately mix **science-forward** and **positioning-forward** claims and label the register.
4. **Write clear narratives.** The narrative is where the science becomes a story a consumer can follow. Plain, specific, product named naturally; never clinical, never hype.
5. **Build it test-ready** — `references/testing-readiness.md`. Structure headlines, narratives, and claims as discrete, comparable, neutrally-coded, compliance-clean stimuli, and include a Test Plan slide. The testing partner runs the field study; we hand them clean stimuli.
6. **Assemble the unbranded draft** — slide-by-slide copy + layout intent (cluster-claims cards, process, source cards). No styling or export; Claude Design brands and produces the final file.

## Rules
- Never invent a claim or a source. If it's not in the verified claim set / workbook, it doesn't exist — flag the gap.
- Claim body copy and citations carry through verbatim; "polish" means adding narratives, claim opportunities, and source cards — not rewording the science.
- All claims scoped to the regulatory class and carry the required disclaimer; unapproved language is labeled as such. Flag borderline claims for MLR rather than presenting them as safe.
- Show guardrails and any null/limiting evidence honestly — it is what makes the story defensible.
- LTBFavorite tags are selective (2–3 per deck), editorial judgment.
- Keep our creative judgment and the consumer's verdict separate: we propose directions; consumer testing decides.

## Revision behavior
Edit surgically on feedback — reorder clusters, swap claims, rewrite a narrative, restyle a slide — without losing traceability to the verified claim set. After each round, summarize what changed and whether it was global or slide-specific.
