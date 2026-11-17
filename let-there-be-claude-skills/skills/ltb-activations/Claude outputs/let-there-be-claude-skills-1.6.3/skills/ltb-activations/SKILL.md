---
name: ltb-activations
description: Build the Activation Examples deliverable for Let There Be - the final engine stage, showing an approved Science Story working in the brand's real channels. Use whenever the user wants activations, activation examples, a video ad script, a 15s/30s/60s script, eComm or DTC or PDP or Amazon product page copy, Brand Store or A+ recommendations, an MOA description, an influencer brief, or FAQ/myth-busting copy - even if they just say "make the activations for [client]", "write the PDP copy", or "show them how the story shows up on Amazon." Captures the brand's live pages with Claude in Chrome, annotates them current-vs-proposed, and ties every efficacy line to an approved claim ID. Runs once per activation and once per SKU. Output is the finished deck, built in the LTB Science Story Activations template. Do NOT use for research (ltb-science-intelligence), the evidence deck (ltb-lit-review-deck), or writing the Science Story itself (ltb-science-story).
---

# LTB Activations — Science Story in Channel

## How this skill finishes: the deck, in one run

**Every run of this skill ends with a finished presentation built in the LTB Template — Science Story Activations (https://claude.ai/artifact/9Ek9qbNGoTFun1g5cjK2W4). Don't stop at the markdown.**

1. Do the work below and write the screen-by-screen content draft. That's the working draft the deck is built from. It isn't the deliverable on its own.
2. As soon as it's complete, build the deck in the template by following `references/template-build.md`. Do this in the same run. Don't ask whether to continue, and don't wait for the user to ask for slides.
3. Finish by giving the user the deck link. Never tell them to take the file into Claude Design, and never suggest they ask for a slide deck.

Wherever this skill mentions Claude Design, a design template, an "unbranded" or "content-first" output, or a markdown brief, it means the content draft that feeds this build step. Every rule about content still applies in full: what goes on each screen, exact wording, and gap markers.

Pause before building the deck only in three cases: the skill below requires an approval first, an input the deck needs is missing, or the user asks for content only.

## What this stage is

Activations are **examples of how the approved Science Story shows up in the brand's ecosystem**. They are chosen by the client at brief stage (usually 4–5 from a standard menu) and handed off at the end of the engagement.

Two rules govern everything below:

1. **Activations are illustrations, not live assets.** They are not MLR/LMR-reviewed deliverables. Say so on the section opener and in the MLR guidance screen.
2. **Every efficacy line is an approved claim, used verbatim.** Activations never create new claims. If a line isn't in the approved claim set, it is labeled PENDING MLR or it doesn't ship. See `references/claim-discipline.md`.

## Writing voice

Plain and factual, same standard as every LTB deliverable. Lead with the fact. Short declarative sentences. Name the number, not the adjective. No superlatives, no hype, no rhetorical-question hooks, no wordplay. Em dashes at most one per screen. Write for marketers, not scientists.

Consumer-facing copy inside an activation is a separate register: it should sound like the brand, not like a deck. But it still obeys the claim rules above.

## Inputs — confirm before building

- **The approved Science Story** (brand story plus any product stories) and the **approved claim set with IDs**, measured endpoints, and the qualifiers that travel with each claim.
- **Which activations are in scope.** From the client brief. If unclear, ask.
- **Which SKUs each activation runs for.** Most clients need the same activation repeated per product. Build the SKU × activation matrix before writing anything.
- **Consumer test results**, if the story was tested. Test scores decide which claim leads and which gets cut.
- **Access to the brand's live channels** — Amazon PDP, Brand Store, DTC site, social. Capture these yourself with Claude in Chrome rather than asking the client to send screenshots. See `references/capture-and-annotate.md`.

If there is no approved claim set, stop and point the user to **ltb-science-intelligence** and **ltb-science-story** first.

## How to build

1. **Build the matrix.** Activations in scope × SKUs in scope. Confirm it with the user before writing. This is usually more screens than people expect: four activations across three SKUs is not twelve decks, but it is twelve content blocks that need a shared spine.
2. **Capture what's live.** Claude in Chrome: PDP, Brand Store, A+ content, competitor pages if relevant. Screenshot everything that will become a graphic. → `references/capture-and-annotate.md`
3. **Check the competitive moment.** If a competitor launched on the same science recently, say so on a context screen and pivot the opening rather than landing on their beat. This happened on Qunol and it was the right call.
4. **Write each activation** to its own spec. → `references/activation-types.md`
5. **Annotate the live pages** module by module, top to bottom: KEEP / CHANGE COPY / CHANGE HEADLINE / REPLACE / ADD. Never a blanket rewrite — the client needs to see exactly what moves and what doesn't, with the claim ID on each change.
6. **Assemble the deck** in the proven order. → `references/deck-structure.md`
7. **Build the deck.** Write the slide-by-slide copy plus layout intent, then build it in the LTB template straight away (see the top of this skill).

## Repeating across SKUs

The brand story is shared; the product stories differ. For each activation:

- Write the **shared spine once** (the opening fact, the theme line, the structure).
- Write the **per-SKU body** from that SKU's own claim. A claim scoped to one SKU cannot travel to another — flag it on the screen when a line is product-specific.
- Where a SKU wasn't in the consumer test, say so and write the claim set from the approved claims it inherits.
- Keep the IDs consistent across every activation so the client can trace one claim through the whole set.

## Output

The finished deck, built in the LTB Template — Science Story Activations from a screen-by-screen draft of copy plus layout intent. Scripts go in two-column VISUAL / VO tables with a word count against target. Page copy goes in CURRENT vs PROPOSED pairs with a one-line **Why**. Every screen carries its claim IDs.

Close on a next-step screen: the client confirms and approves the direction, the claims cluster and the activations.

## Rules

- Never invent a claim, a number, or a source.
- Never write a visual that implies more than the claim says (no graphs showing levels rising, no before/after bodies, no symptom-disappearing imagery). Visual guardrails are claims too.
- Carry mandatory footnotes and disclaimers on every screen that carries a claim — DSHEA asterisk for supplements, dose disclosure where the claim rests on a multi-unit dose, drug-facts qualifiers for OTC.
- Keep in-market claims as they are, with their current footnotes. Don't improve copy the client has already cleared unless there's a reason, and say the reason.
- Flag anything you could not verify rather than smoothing it over.
