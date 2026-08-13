---
name: ltb-lit-review-claim-dev-sales-preview
description: >-
  Run a Science Intelligence preview for Let There Be - point it at a prospect product and category and it
  produces an unbranded preview deck that frames the whole Science Marketing Engine: a real Elicit pass, one
  hero finding, one to three claims built on it, and an example Science Story, ending in Science Studio work
  and a contact slide. Use whenever a salesperson or BD person wants a pitch preview, a prospect teaser, a
  what could we find or what could they claim deck, a pre-engagement sales asset, or a conference leave
  behind - even if they just say make a preview for a brand or build a claim preview to pitch a prospect.
  Sources stay blurred so the research is not given away. Output is an unbranded presentation draft for
  Claude Design. Do NOT use for a signed engagement (use ltb-science-intelligence and ltb-lit-review-deck)
  or for real Science Story clusters and narratives.
---

# LTB Science Marketing Engine Preview (sales)

## What this is

A **sales preview**. A rep points it at a prospect's product and it produces the content for a **fixed 12-slide deck** that does two jobs: it shows one real, specific piece of science we found, and it frames that inside the whole Science Marketing Engine so the prospect sees where it goes next.

**This skill fills a template. It does not design a deck.** There is an approved Claude Design template with twelve screens. Your output must drop into it without anyone deleting, merging, or inventing slides. If your material does not fit a slide, cut the material rather than adding a slide.

Read `references/preview-structure.md` and follow it exactly. Six of the twelve screens are boilerplate: reproduce them as written.

**Depth over breadth.** One hero finding, two secondary territories, three claims, one story direction. Those counts are fixed because the template's layouts are built for them.

## Writing voice — plain and factual

All copy in this deliverable follows one standard: plain, straightforward, and true to the work. We make complex science clear; the writing should do the same. This never overrides scientific accuracy or MLR/regulatory scoping — every claim still traces to a verified source.

- **Lead with the fact, not the flourish.** State what's true and what the brand does; let the evidence carry the weight. No hype, no hard sell.
- **Short, declarative sentences.** Explain it the way you would to a smart colleague who isn't a scientist. Cut any word that isn't doing work.
- **Specific over vague.** Name the ingredient, the finding, the number, the source. Specificity is what earns trust.
- **No salesmanship or showmanship.** Avoid superlatives and buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), teaser/hype phrasing, rhetorical-question hooks, wordplay, and puns. Never write to dazzle or to "sell."
- **Earned confidence, stated plainly.** Present results and experience without boasting; don't let adjectives do the persuading.
- **Headlines state the point; they don't perform.** Two-part contrast headlines are house style and are fine ("Menthol doesn't just cool the skin. It changes the signal."). Taglines written for effect are not.
- **Em dashes: use sparingly.** At most one per slide or section, and only when a comma or a period genuinely will not do. Default to a period and a new sentence. Never stack them for dramatic pauses or nested asides.
- **Write for marketers, not scientists.** The reader is a brand, marketing, or creative professional. Assume they are smart and busy, not that they know biology. Replace or define a technical term the first time it appears.
- **Keep the science simple and accurate.** Use plain words for mechanisms. Keep the precise term only when it carries real meaning: an ingredient name, a study design, a regulatory class, a measured result. Simplifying must never change what a finding actually says.
- **Say it once.** No restating the same point in a second clause. Cut throat-clearing openers and filler qualifiers.

> **Output: template-ready content, not a designed file.** Produce the twelve screens as copy plus a speaker note each. No styling, no export. **Claude Design** places it in the approved template. These decks ship as **PDF**.

## Inputs

The rep gives a product and category, plus **two or three sentences of angle**. The angle is the most valuable input: it tells you which finding to chase.

> "New entrant in a cluttered category. The incumbent is Flonase. See if the preview can find something that helps them differentiate."

Do not interrogate the rep. Infer the rest and state your assumptions in one line back to them:

- **Actives:** identify them from the product or lineup. Name them on slide 04.
- **Regulatory class:** infer it (OTC monograph, supplement, device, Rx) — it scopes the claims and appears in slide 08's subhead.
- **Competitor:** pick the obvious category rival if none is named.

## Phase 1 — Research

Use the connected Elicit tools: **`search_papers`** (both `elicit` and `pubmed`; prioritize Meta-Analysis, Systematic Review, RCT; favour recent and landmark) and **`search_trials`**. Do **not** run `create_systematic_review`; that depth belongs to the paid engagement.

Every study must be real and tool-sourced with a resolving PMID, DOI, or NCT. Never invent a study, a statistic, or an identifier. Identifiers are **blurred** in the deck, not omitted, so they must still be correct: the rep may be asked for them, and Design needs the real value to mask.

Look hardest for: a named mechanism (receptor, pathway, protein), a human trial with a comparator, a guideline position, and any trial the brand ran on its own formulation. That last one is often the strongest thing in the deck.

## Phase 2 — Pick the hero finding

Choose **one** finding to carry the deck, guided by the rep's angle. What makes a good one:

- **Specific and quantified**, or a named mechanism a rep can say out loud.
- **Serves the angle** the rep gave you.
- **Ownable**, not a category truism every competitor could claim.
- Graspable in one sentence without a biology lesson.

It must support the three-part structure of slide 06: a mechanism, a measured human result, and a second-order advantage.

In your handback notes to the rep, not in the deck, list the **two or three runner-up findings** and why you chose this one. The rep may prefer a different angle and needs to swap it quickly.

## Phase 3 — Claims

Read `references/claim-development.md`. Derive **exactly three** claims, all built on the hero finding. Each needs consumer-facing language, the evidence behind it with author-year citations, and a guardrail line naming the limit.

Scope every claim to the product's regulatory class. Keep them to language a brand could plausibly take to MLR.

## Phase 4 — Fill the template

Because citations are blurred, **every finding sentence must stand on its own.** Do not write "as shown by Johar et al." — the reader cannot read that name. Write what was found, in what kind of study, against what comparator.


Work through `references/preview-structure.md` screen by screen. For each: the `data-screen-label`, the copy, and a **speaker note** written for a rep who has not read the studies. The speaker notes matter as much as the slides; they are what makes the deck presentable cold.

## Non-negotiables

- **Twelve screens, in order, with the given labels.** No new slides unless the rep asks.
- **Reproduce the boilerplate** (01, 02, 10, 11, 12, and the frame of 04) rather than rewriting it.
- **Mask sources, not substance.** Years, author names, PMIDs and NCTs are blurred (`filter: blur(4.5px); user-select: none`). Findings, designs, signals, claims and guardrails stay legible. A reader should understand every finding and be unable to look up a single source. See Source masking in `references/preview-structure.md`.
- Slide 04 states plainly: public science only, no brand documents, no prior claim work, no conversations with the team.
- Slide 09 carries **Illustrative — not [Brand] data**, and its test scores stay empty (`--%`). Never invent test results.
- **No prices anywhere.** Testing is described, not quoted.

## Guardrails

- Real, tool-sourced studies only.
- One hero finding. Two territories. Three claims. One direction. Resist expanding any of them.
- State working assumptions in one line so the rep can correct them, but do not block on questions.
- Website language throughout. No "gems"; the unit is a claim.
