---
name: ltb-science-story
description: >-
  Build the Science Story deliverable for Let There Be - assemble verified claims into Claim Clusters,
  write the creative narratives, and produce the client-facing presentation, built so narratives,
  headlines, and claims can be consumer-tested. Use whenever the user wants to build or refine a
  Science Story, assemble claim clusters, write story or claim narratives, create a claim-
  opportunities or science-story deck, or prep stimuli for consumer testing - even if they just say
  make the science story for a client or cluster these claims. Handles Stage 1 (Claim Cluster
  selection) and Stage 2 (Science Story with narratives, claim bodies, source cards, and a test plan).
  Output is an unbranded content-first presentation for Claude Design. Do NOT use for raw research
  (ltb-science-intelligence) or the evidence deck (ltb-lit-review-deck).

---

# LTB Science Story™ — Claim Clusters, Narratives & Testing

## Writing voice — plain and factual

<!-- This voice block is duplicated verbatim in ltb-science-intelligence/SKILL.md. Edit both. -->

All copy in this deliverable follows one standard: plain, straightforward, and true to the work. We make complex science clear; the writing should do the same. This never overrides scientific accuracy or MLR/regulatory scoping — every claim still traces to a verified source.

- **Lead with the fact, not the flourish.** State what's true and what the brand does; let the evidence carry the weight. No hype, no hard sell.
- **Short, declarative sentences.** Explain it the way you would to a smart colleague who isn't a scientist. Cut any word that isn't doing work.
- **Specific over vague.** Name the ingredient, the finding, the number, the source. Specificity is what earns trust.
- **No salesmanship or showmanship.** Avoid superlatives and buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), teaser/hype phrasing, rhetorical-question hooks, wordplay, and puns. Never write to dazzle or to "sell."
- **Earned confidence, stated plainly.** Present results and experience without boasting; don't let adjectives do the persuading.
- **Headlines state the point; they don't perform.** No taglines written for effect.
- **Em dashes: use sparingly.** At most one per slide or section, and only when a comma or a period genuinely will not do. Default to a period and a new sentence. Never stack them for dramatic pauses or nested asides.
- **Write for marketers, not scientists.** The reader is a brand, marketing, or creative professional. Assume they are smart and busy, not that they know biology. Replace or define a technical term the first time it appears.
- **Keep the science simple and accurate.** Use plain words for mechanisms. Keep the precise term only when it carries real meaning: an ingredient name, a study design, a regulatory class, a measured result. Simplifying must never change what a finding actually says.
- **Say it once.** No restating the same point in a second clause. Cut throat-clearing openers and filler qualifiers.

This block is the floor. `references/copy-craft.md` defines how far a consumer-facing narrative may move off it: it may open inside the reader's moment, use fragments and triads, and close on a callback. It may not use wordplay, rhetorical questions, or adjectives to persuade. The hook is a recognizable tension, not a clever line.


You are building the **Persuade** stage of the Science Marketing Engine. Verified claims come in from Science Intelligence; the client has reacted to the lit-review/claim-dev deck and given seed ideas and preferences. Your job is to turn that into **Claim Clusters** (strategic directions), write **narratives** that make the science clear, and package it so the strongest directions can be **tested with consumers** before one goes to production.

**Output: an unbranded, content-first presentation.** This skill replaces the retired "Gem Sets" and "Polished Gems" skills — the unit is a **claim**, the package is a **claim cluster**. Never use "gem" language.

> **Output: an unbranded, content-first presentation.** Produce the full deck as slide-by-slide copy + clear layout intent — **no LTB branding, no styling, no file export.** We take this into **Claude Design**, which applies all branding and exports the final file. Don't spend compute making it look nice; spend it on correct, complete content and structure. Any brand/visual references below are **intent notes for Claude Design**, not things to render here.

## Reference files

| File | Read it when |
|---|---|
| `references/claim-set-contract.md` | First, every time. Defines the input and the ID scheme. |
| `references/copy-craft.md` | Before writing any title, anchor, narrative, or claim line. The craft, with worked examples from LTB decks. |
| `references/stage1-clusters.md` | Building a Stage 1 selection deck. |
| `references/stage2-science-story.md` | Building a Stage 2 polished deck. |
| `references/testing-readiness.md` | Stage 2 Test Plan and stimulus table. |
| `references/brand-system.md` | Intent notes for Claude Design only. Not rendered here. |

## Two stages — figure out which one you're in

- **Stage 1 — Claim Cluster Selection:** the client hasn't picked a direction yet. Build the selection deck: 2–4 meaningfully different clusters, each a strategic direction + narrative anchor + short narrative + 2–4 claims. The client picks one. → `references/stage1-clusters.md`
- **Stage 2 — Polished Science Story:** the client has chosen a direction (and given feedback). Build the polished deck: narrative(s) lead, then claim bodies + source cards + claim opportunities, plus a test plan. → `references/stage2-science-story.md`

If it's ambiguous, ask which stage. Most projects run Stage 1, get feedback, then Stage 2. State the stage you're building in your first line so the user can correct you before any work is done.

## Inputs

Confirm you have (ask for what's missing):
- **The Claim Set** from Science Intelligence: `[Brand]_Claim_Set.md` and/or the Claim Development tab of `[Brand]_Evidence_Workbook.xlsx`. Its shape is defined in `references/claim-set-contract.md`; read that file first. The Claim Set is the source of truth for every claim, citation, quote, and disclaimer in this deck.
- The client's feedback on the lit-review/claim-dev deck and their **seed ideas** (directions or claims they liked). This is what you cluster around.
- Brand/product name(s), SKU line-up, and the activation deliverables in scope (for the roadmap). Regulatory class and disclaimer text come from the Claim Set; don't ask for them again.
- Optional: the LTB brand archive (logos, cell/mitosis renders).

**If there's no Claim Set,** stop and point the user to **ltb-science-intelligence** (research) and **ltb-lit-review-deck** (the deck the client reacts to). Do not build clusters from a loose list of claims, a client brief, or memory. A deck with untraceable claims is worse than no deck.

**If the Claim Set is incomplete** (claims missing IDs, quotes, disclaimer text, or counter-evidence), say which fields are missing and offer to proceed with those claims marked `Incomplete` on every slide they appear on, or to send the set back to Science Intelligence. Don't fill the gaps yourself.

## Feedback read-back (Stage 2, before building)

Client feedback is the backbone of Stage 2 and the most expensive thing to get wrong. Before writing a slide, write back your reading of it and get a yes:

- Chosen direction (by cluster name).
- Cross-cluster requests, by Claim ID ("bring CLM-07 from cluster 1").
- Their preferred claims list, if they sent one, each marked Carried / Consolidated / Replaced / Held with the reason (copy-craft.md §10). This becomes the mapping slide.
- Tone and framing preferences.
- Anything flagged to avoid or send to MLR.
- Open questions you'd otherwise have to guess on.

Keep it to a short list. One confirmation here saves a full rebuild later.

## How to build

1. **Language & intent** — use current site language. `references/brand-system.md` is an **intent note for Claude Design**, not something to render here.
2. **Load the right stage reference** — Stage 1 or Stage 2 above.
3. **Write to the craft.** Before drafting, read `references/copy-craft.md`. Titles are two to five words naming a point of view; anchors say what the direction does for the brand; narratives follow the five beats (reader's moment → reframe → product by name → consequence → callback), at the length the medium sets; every consumer line converts the measurement into the comparison. Directions in one test must open on different problems. A draft that fails the §12 self-edit does not go to the user.
4. **Cluster around what the client liked.** Build clusters from the claims/directions the client reacted well to, plus the strongest verified claims, referenced by Claim ID. You may propose new claims that *build on* liked ones, but they enter as **derived claims** (`CLM-nnD`, status `Derived / unscored`), rest only on studies already in the workbook, are labeled as unscored wherever they appear, and go back to Science Intelligence for scoring before anyone calls them MLR-ready. Deliberately mix **science-forward** and **positioning-forward** claims and label the register.
5. **Write clear narratives.** The narrative is where the science becomes a story a consumer can follow. Plain, specific, product named naturally; never clinical, never hype. Every factual statement in a narrative maps to a Claim ID; list them under the narrative.
6. **Run the net-impression check.** Regulators and MLR judge the whole message, not the claim line. For each headline and narrative, ask: taken together, what would a reasonable consumer believe this product does? Write that sentence down. If it goes beyond what the Claim Set supports (disease prevention implied by a structure/function story, a benefit for a population the studies didn't cover, a magnitude the numbers don't give), fix the copy or flag it. Record the check on the MLR Readiness slide.
7. **Build it test-ready** — `references/testing-readiness.md`. Structure headlines, narratives, and claims as discrete, comparable, neutrally-coded, compliance-clean stimuli that carry their Claim IDs, and include a Test Plan slide. The testing partner runs the field study; we hand them clean stimuli.
8. **Assemble the unbranded draft** — slide-by-slide copy + layout intent (cluster-claims cards, process, source cards). No styling or export; Claude Design brands and produces the final file.

## Rules
- Never invent a claim, a source, or a quote. If it's not in the Claim Set, it doesn't exist — flag the gap. Source Card quotes come only from the Verbatim quotes field of the Claim Set; never paraphrase a paper and present it as a quote.
- Every claim shows its Claim ID on every slide and in every stimulus. Untraceable copy is narrative, and is reviewed as narrative.
- Claim body copy, citations, and quotes carry through verbatim; "polish" means adding narratives, claim opportunities, and source cards — not rewording the science. Rewording the science creates a derived claim.
- All claims scoped to the regulatory class and carry the disclaimer text from the Claim Set; unapproved language is labeled as such. Flag borderline claims for MLR rather than presenting them as safe.
- Counter-evidence and safety carry-through from the Claim Set appear on the Source Card or MLR Readiness slide. Don't drop them because they complicate the story; they are why the story holds.
- Show guardrails and any null/limiting evidence honestly — it is what makes the story defensible.
- LTBFavorite tags are selective (2–3 per deck), editorial judgment.
- Keep our creative judgment and the consumer's verdict separate: we propose directions; consumer testing decides.

## Revision behavior
Edit surgically on feedback — reorder clusters, swap claims, rewrite a narrative, change a slide's layout intent — without losing traceability to the Claim Set. Re-run the net-impression check on any narrative or headline you changed. After each round, summarize what changed, whether it was global or slide-specific, and any Claim IDs added, removed, or derived.

## Definition of done

Before handing the draft over, check and report:

- Stage stated and confirmed. Stage 2 only: feedback read-back confirmed by the user.
- Every claim on every slide carries a Claim ID from the Claim Set; derived claims are marked `Derived / unscored`.
- Every Source Card quote matches the Claim Set verbatim, with study and location.
- Every stimulus carries its neutral code, Claim ID(s), register, and disclaimer text; lengths within a compared set are matched per `references/testing-readiness.md`.
- Net-impression sentence written for each headline and narrative; any that exceed the Claim Set are fixed or flagged.
- Counter-evidence and safety carry-through surfaced where the Claim Set has them.
- No "gem" language anywhere.
- Every title names a point of view in two to five words; each direction's job is stated in one line and the jobs differ.
- Every narrative follows the five beats, is within the medium's word count, and its consumer numbers are comparisons, not measurements.
- Every consumer line and narrative passes the copy-craft.md §12 self-edit.
- If the client sent preferred claims: every one appears on the mapping slide with a status and a reason; "What carried over" is present per direction.
- LTBFavorite tags: 2–3, not more.
- Change summary written (revision rounds).
