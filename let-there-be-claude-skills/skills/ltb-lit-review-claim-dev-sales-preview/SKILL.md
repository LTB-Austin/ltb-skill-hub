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

This block is the floor for every word in the deck, including the claims and the worked-example story. `references/copy-craft.md` defines how far the consumer-facing lines may move off it (a fragment and a turn, the reader's moment, a triad, a callback close) and where they may not (wordplay, rhetorical hooks, adjectives doing the persuading). In a preview the temptation to sell is strongest and the copy has to resist it hardest: the prospect is judging whether we can write, not whether we can pitch.

## Reference files

| File | Read it when |
|---|---|
| `references/preview-structure.md` | First. The twelve screens, which are boilerplate, and the source-masking rule. |
| `references/copy-craft.md` | Before writing slide 06 (hero statement), slide 08 (three claims), or slide 09 (direction, headline, narrative). |
| `references/claim-development.md` | Phase 3. Scoring and risk, scoped to the preview. |
| `references/brand-system.md` | Intent notes for Claude Design only. |

> **Output: template-ready content, not a designed file.** Produce the twelve screens as copy plus a speaker note each. No styling, no export. **Claude Design** places it in the approved template. These decks ship as **PDF**.

## Inputs

The rep gives a product and category, plus **two or three sentences of angle**. The angle is the most valuable input: it tells you which finding to chase.

> "New entrant in a cluttered category. The incumbent is Flonase. See if the preview can find something that helps them differentiate."

Do not interrogate the rep. Infer the rest and state your assumptions in one line back to them:

- **Actives:** identify them from the product or lineup. Name them on slide 04.
- **Regulatory class:** infer it (OTC monograph, supplement, device, Rx) — it scopes the claims and appears in slide 08's subhead.
- **Competitor:** pick the obvious category rival if none is named.

## Phase 1 — Research

Use the connected Elicit tools: **`search_papers`** (both `elicit` and `pubmed`; prioritize Meta-Analysis, Systematic Review, RCT; favour recent and landmark) and **`search_trials`**. Load them first with `tool_search` and use the parameter names the returned schema gives; do not guess. Do **not** run `create_systematic_review`; that depth belongs to the paid engagement.

If Elicit is not connected or returns nothing usable, stop and say so. A preview built from recalled studies is worse than no preview: the rep will be asked for the identifiers, and an invented PMID in a sales deck is the one thing this skill can never produce.

Every study must be real and tool-sourced with a resolving PMID, DOI, or NCT. Never invent a study, a statistic, or an identifier. Identifiers are **blurred** in the deck, not omitted, so they must still be correct: the rep may be asked for them, and Design needs the real value to mask.

Look hardest for: a named mechanism (receptor, pathway, protein), a human trial with a comparator, a guideline position, and any trial the brand ran on its own formulation. That last one is often the strongest thing in the deck.

## Phase 2 — Pick the hero finding

Choose **one** finding to carry the deck, guided by the rep's angle. What makes a good one:

- **Specific and quantified**, or a named mechanism a rep can say out loud.
- **Serves the angle** the rep gave you.
- **Ownable**, not a category truism every competitor could claim.
- Graspable in one sentence without a biology lesson.

It must support the three-part structure of slide 06: a mechanism, a measured human result, and a second-order advantage.

**Writing the hero statement.** The two-part contrast line on slide 06 is the single sentence the rep will say most. It follows copy-craft.md §2: a fact and a turn, two short sentences, no adjectives, the mechanism named in plain words. "Menthol doesn't just cool the skin. It changes the signal." Not "A breakthrough in how menthol works." The number in point 02 is stated the way a marketer hears it (§3): a comparison or a simple fraction, with the measurement in the speaker note.

In your handback notes to the rep, not in the deck, list the **two or three runner-up findings** and why you chose this one. The rep may prefer a different angle and needs to swap it quickly.

## Phase 3 — Claims

Read `references/claim-development.md`, then `references/copy-craft.md` §2, §3, §7, and §11. Derive **exactly three** claims, all built on the hero finding. Each needs consumer-facing language, the evidence behind it with author-year citations, and a guardrail line naming the limit.

The three lines are written to the craft, because they are the prospect's first look at what our claims read like:

- Each is one or two short sentences, ≤12 words each; a fact and a turn where the rhythm allows.
- The measurement stays in the "Behind it" sentence; the claim carries the comparison. No percentages with decimals, no units, no p-values in the quoted line.
- The qualifier matches the design: "clinically shown" only on a human RCT for that endpoint; "helps support" for structure/function; never "proven."
- The product is named in at least one of the three, and never in the same sentence as a prevalence figure.
- The comparator, if any, is the molecule, not the brand.
- The three differ in what they say, not in how they say the same thing: typically one mechanism line, one measured-result line, one occasion or advantage line.
- The guardrail names words: "Keep to symptom relief. No nerve-disease implication." Not "use carefully."
- The "Behind it" sentence is written for a reader, in the same voice, one register more detailed. It must make sense with the citation blurred.

Scope every claim to the product's regulatory class. Keep them to language a brand could plausibly take to MLR. Run each line through the copy-craft.md §12 self-edit before it goes on the slide.

Preview claims are illustrative. They are not entered into a Claim Set and carry no Claim IDs; if the engagement signs, Science Intelligence re-derives them with full substantiation and assigns IDs then.

## Phase 4 — Fill the template

Because citations are blurred, **every finding sentence must stand on its own.** Do not write "as shown by Johar et al." — the reader cannot read that name. Write what was found, in what kind of study, against what comparator.


**Slide 09 is a real Science Story in miniature** and is written to copy-craft.md §9. The direction name is two to five words naming a point of view, not a benefit. The headline is the claim-shaped line the story hangs on. The narrative is three to five sentences (roughly 60–100 words) that still walk the five beats: the reader's moment, the reframe, the product by name doing one thing, the consequence, the callback. The claim cluster is the three claims from slide 08. Everything on it is labeled illustrative, and the scores stay empty.

Work through `references/preview-structure.md` screen by screen. For each: the `data-screen-label`, the copy, and a **speaker note** written for a rep who has not read the studies. The speaker notes matter as much as the slides; they are what makes the deck presentable cold.

## Non-negotiables

- **Twelve screens, in order, with the given labels.** No new slides unless the rep asks.
- **Reproduce the boilerplate** (01, 02, 10, 11, 12, and the frame of 04) rather than rewriting it.
- **Mask sources, not substance.** Years, author names, PMIDs and NCTs are blurred (`filter: blur(4.5px); user-select: none`). Findings, designs, signals, claims and guardrails stay legible. A reader should understand every finding and be unable to look up a single source. See Source masking in `references/preview-structure.md`.
- Slide 04 states plainly: public science only, no brand documents, no prior claim work, no conversations with the team.
- Slide 09 carries **Illustrative — not [Brand] data**, and its test scores stay empty (`--%`). Never invent test results.
- **No prices anywhere.** Testing is described, not quoted.

## Definition of done

Before handing back, check and report in a few plain lines:

- Twelve screens, in order, labels intact; boilerplate reproduced unchanged.
- Every study has a real, tool-sourced identifier, present and marked for blurring.
- Every finding sentence stands on its own with the citation unreadable.
- Hero statement is a two-part contrast in plain words; its number is stated as a comparison.
- Three claims, each passing the copy-craft.md §12 self-edit; each guardrail names words; the three say different things.
- Slide 09 direction name is a point of view in two to five words; narrative walks the five beats in 60–100 words and closes on a callback; scores empty; illustrative flag present.
- No prices, no superlatives, no "gem," no invented result anywhere.
- Handback note to the rep lists assumptions and the runner-up findings.

## Guardrails

- Real, tool-sourced studies only.
- One hero finding. Two territories. Three claims. One direction. Resist expanding any of them.
- State working assumptions in one line so the rep can correct them, but do not block on questions.
- Website language throughout. No "gems"; the unit is a claim.
