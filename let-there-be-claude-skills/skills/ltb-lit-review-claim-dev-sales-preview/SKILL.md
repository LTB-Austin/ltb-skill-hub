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

# LTB Science Intelligence Preview (sales)

## What this is

A **sales preview**. A salesperson points it at a prospect's product, and it produces a short deck that does two jobs at once:

1. Shows a **real, specific** piece of science we found for their product, and the claims it supports.
2. **Frames that inside the whole Science Marketing Engine**, so the prospect sees where it goes next: Science Story, consumer testing, Science Studio.

It is a preview, not the paid deliverable. It should feel substantial and reputable while withholding the actual research.

**The single biggest rule: depth over breadth.** Earlier versions showed too much and landed as hypothetical wallpaper. One strong finding a rep can speak to beats ten they can't. Everything after the lit review table hangs off **one hero insight**.

## Writing voice — plain and factual

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

> **Output: an unbranded, content-first presentation.** Produce slide-by-slide copy plus layout intent. No LTB branding, no styling, no file export. **Claude Design** applies the brand system and exports. These decks are delivered as **PDF**, so Design can use gradient borders and richer treatments. Any brand or visual notes here are intent for Design only.

## Inputs — take what the rep gives and run

The rep usually gives a product and category, plus **two or three sentences of angle**. That angle is the most valuable input: it tells you which insight to chase.

> Example: "New entrant in a cluttered category. The incumbent is Flonase. See if the preview can find something that helps them differentiate."

Do not interrogate the rep. Infer the rest and state assumptions in one line:

- **Active ingredient(s):** identify them if unstated. If several are plausible, pick the most likely and note it.
- **Regulatory class:** infer it (OTC monograph drug, supplement, homeopathic) so claims stay plausible and correctly caveated.
- **Competitor:** pick the obvious category rival if none is named.
- **Product image:** the rep may supply one for the intro slide. If not, leave a labelled placeholder.

## Phase 1 — Research

Use the connected Elicit tools: **`search_papers`** (run both `elicit` and `pubmed`; prioritize Meta-Analysis, Systematic Review, and RCT; favour recent and landmark work) and **`search_trials`**. Do **not** run `create_systematic_review`. That depth belongs to the paid engagement.

Pull enough to fill a credible one-page table, about **8 to 10 studies**, all genuinely relevant to the product and its actives. Every study must be real and tool-sourced. Never invent a study, a statistic, or a PMID.

## Phase 2 — Pick the hero insight

From everything you found, choose **one** finding to build the rest of the deck on. You pick it, guided by the rep's angle.

What makes a good hero insight:

- It is **specific and quantified**. A number a rep can say out loud.
- It **serves the angle** the rep gave you (differentiation, an underserved population, a high-value symptom).
- It is **ownable**, not a category truism every competitor could claim.
- It is **recent or landmark**, from a design that holds up.
- A marketer can grasp it in one sentence without a biology lesson.

Then, in your handback notes to the rep (not in the deck), list the **two or three runner-up insights** you considered and why you chose this one. The rep may prefer a different angle and needs to be able to swap it quickly.

## Phase 3 — Claims

Read `references/claim-development.md`. Derive **one to three claims**, all built on the hero insight. Not four to six, and not spread across territories. Fewer, tighter, and connected is the point.

For each claim: consumer-facing language in quotes, the tier (DTC-ready / DTC + HCP / HCP hero), and a one-line note on why it is ownable. **Blur or omit the underlying evidence** in the deck. The claim language is the shop window; the substantiation is what they are buying.

Keep a short **category whitespace** read. It signals strategic thinking and prospects respond to it.

## Phase 4 — Deck structure

Read `references/preview-structure.md` for slide detail. The arc:

1. **Cover** — Let There Be. Product name.
2. **The Science Marketing Engine** — the three-phase frame the whole deck lives inside.
3. **Preview intro** — product name, product image, and the disclaimer plainly stated: no brand input, no brief, no guidance, no inputs from the client.
4. **Engine, Science Intelligence highlighted** — where we are now.
5. **The Lit Review** — one page, 8 to 10 studies, relevant to their product. **Sources delinked and blurred.** Lit Review mark on the slide. This slide exists to look like the real thing, not to be read.
6. **The finding** — the single hero insight, stated plainly with its number. Sources blurred. This is the slide the rep actually talks to.
7. **Claim Dev intro** — one slide: Claim Dev reads the literature and extracts what is substantiated, regulatory-friendly, and strategically useful.
8. **The claims** — one to three, built on the hero insight, consumer-facing language only. Evidence blurred. Include the whitespace read.
9. **Engine, Science Story highlighted.**
10. **Example Science Story** — a single slide: creative hook, short narrative, the relevant claims, and a line that we build several of these and test them with consumers on purchase intent, uniqueness, and believability, including highlight heat maps. One slide covers both the story and the testing.
11. **Engine, Science Studio highlighted.**
12. **Science Studio work** — boilerplate. Example stills from published LTB work. The rep should not have to supply screenshots.
13. **Closing** — unlock your science potential, plus contact details.

Slides 2, 4, 9, and 11 are the same engine graphic with a different phase highlighted. Design owns that treatment.

**Do not include** a general "your product and category context" slide. It was text-heavy and never got used.

## Non-negotiables

- **Blur or delink every source.** The rep is showing capability, not handing over the research.
- Every science or claims slide carries: **Preview · no brand input · findings not validated.**
- Claims carry: **Illustrative and directional. Subject to MLR and legal review.**
- Name what the preview did not do (no brand input, no systematic review, no MLR, no consumer testing) and that those live in the full engagement. That gap is the reason to buy.
- Do not quote a testing price. Say testing is available and what it measures; the rep quotes numbers live.

## Guardrails

- Real, tool-sourced studies only. No fabricated papers, PMIDs, or numbers.
- One hero insight. One to three claims. Resist adding more.
- State working assumptions in one line so the rep can correct them, but do not block on questions.
- Website language throughout. No "gems"; the unit is a claim.
- End on a clear, specific next step.
