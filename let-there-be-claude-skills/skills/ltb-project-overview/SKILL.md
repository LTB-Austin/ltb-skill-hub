---
name: ltb-project-overview
description: >-
  Assemble the client Project Overview content brief for Let There Be — a single structured markdown
  document holding every piece of content a project overview needs, which Claude Design then expands
  into the branded presentation using its Project Overview template. Use whenever the user wants to
  build, refine, or update a project overview for any LTB client — even if they just say make the
  overview for a client or start the kickoff doc. Reads the brief, brand book, science, partner
  details, and prior decks from the project space and organises them into labelled sections: project
  details, deliverables, timeline, brand deep dive, audiences, the challenge, the three-phase engine,
  and next steps. Output is markdown only — never a PPTX, HTML, or styled deck. Unknowns are marked as
  open rather than filled in. Do NOT use for the Science Intelligence deck, the Science Story, the
  SOW, or the internal Science 101 briefing.

---

# Skill: LTB Project Overview — Content Brief Builder

## What you produce

**One markdown file. Nothing else.**

You are not building a presentation. You are assembling the **content** for a project overview — every fact, figure, table, and paragraph — into a clearly structured markdown document. **Claude Design** takes that markdown and expands it into the branded presentation using its Project Overview template.

This split exists for a reason: when this skill produced slides, Design had to reformat the whole deck anyway. So don't produce slides, layout intent, HTML, PPTX, or styling. No colors, no fonts, no blob placement, no "eyebrow / title / divider" instructions. Just correct, complete, well-labelled content.

**The contract with Claude Design:** the markdown is the single source of truth. Design expands and formats what's there — it does not invent, embellish, or fill gaps. That only works if you are explicit about what is known and what isn't, so mark every gap (see "Marking gaps" below) rather than writing around it.

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

Write the copy as the client will read it. Design should be formatting finished sentences, not drafting them.

---

## PHASE 0 — Inputs

You're running in a **Claude project space.** The brief, brand book, science, partner details, and prior decks are attached or already in the project files — use them. Ask only for what's missing; never invent.

- [ ] Brand / product name (+ active ingredient, INN/common)
- [ ] Client + any partner
- [ ] The objective / what success looks like
- [ ] Deliverables in scope (Science Intelligence, Science Story, Science Studio pieces)
- [ ] Timeline start month + any pilot/launch target
- [ ] Brand materials — brand book, palette, packaging, logo (as links/filenames, for Design to fetch)
- [ ] The science (MOA, formulation, clinical) and any approved claims + guardrails
- [ ] Audience(s) — patient, consumer, and/or HCP
- [ ] Competitors, if provided

---

## PHASE 1 — Marking gaps

Never fill a hole with plausible language. Use these markers verbatim so Design and the account lead can both see the state at a glance:

- `> **TO BE DEFINED WITH [CLIENT]**` — a client-side decision we don't have yet (tone, platform, personas).
- `> **NEEDED FROM CLIENT:** [what]` — an input we've asked for and are waiting on.
- `> **NOT IN SCOPE**` — deliberately excluded; keeps Design from adding it back.

If a whole section has no content, keep its heading and put the marker under it. A visible gap is useful; an invented sentence is a liability.

---

## PHASE 2 — Document structure

Produce exactly this shape. Keep the headings and their order — Design's template maps to them. Drop a section only if it's genuinely out of scope, and say so with the marker rather than deleting the heading.

Open with a metadata block, then the sections:

```
# [Product / Program Name] — Project Overview
**Client:** … | **Partner:** … | **Prepared by:** Let There Be | **Date:** [Month Year]
**Active ingredient:** … | **Audiences:** … | **Regulatory class:** …
**Program descriptor:** [one line, e.g. A Patient & HCP Science Marketing Program]
```

### 1. Project details
- **Objective** — one plain headline sentence, then a short paragraph on strategy and focus.
- **Deliverables** — a markdown table: `Asset | Phase | Duration | Format | Placement`. One row per deliverable actually sold.
- **Timeline** — a markdown table or list, month by month, kickoff → pilot/launch. Note that phases flex with feedback.

### 2. Brand deep dive
Everything we've absorbed, so every downstream team starts from the same understanding.
- **About the brand** — what the product is, in plain language.
- **Brand materials** — links/filenames for logo, packaging, palette, brand book. List them; don't describe styling.
- **Brand identity** — connection, character, tone.
- **Brand idea / platform** — the organizing idea, if the client has one.
- **Competitors** — primary / secondary (Rx) / OTC alternatives.
- **Target audiences** — a subsection per audience (patient/consumer, HCP).
- **Useful links** — brand book, sales aid, asset libraries.

### 3. The challenge and our solution
- **The challenge** — a plain statement of the core problem.
- **Market forces** — the dynamics working against the brand.
- **Objectives** — what success looks like, split by audience.
- **Our solution** — one science foundation, deployed everywhere, via the Science Marketing Engine™ (plus the partner channel, if any).
- **Operating model** — one engine, three phases: `01 · The Proof — Science Intelligence™`, `02 · The Persuasion — Science Story™`, `03 · The Production — Science Studio™`.

### 4. The engine, phase by phase
Only include phases that are sold. Under each, write the content — not slide directions.
- **Phase 01 · The Proof — Science Intelligence™** — the science and MOA in plain language; what the lit review covers; how claims get shepherded through MLR.
- **Phase 02 · The Persuasion — Science Story™** — the narrative per audience; creative direction and tone; consumer testing if in scope.
- **Phase 03 · The Production — Science Studio™** — one subsection per production piece (patient video, HCP video, MOA Moment™, etc.) with its specs and placement.

### 5. Why this works
The strategic payoff of the integrated approach, in a few plain sentences.

### 6. How we work
Use the boilerplate in Phase 3 verbatim (milestone model, ownership).

### 7. Getting started
- **Next steps** — numbered action items with owners where known.
- **Kickoff questions** — what we need to align on (evidence, guardrails, priorities).

### 8. Closing
"Thanks for trusting us with your science." + "Science leads. Creativity amplifies."

---

## PHASE 3 — Boilerplate (verbatim; adapt names only)

**How we work (milestone model):**
> Unlike agencies that cap revisions, Let There Be uses a milestone model to deliver the strongest possible Science Stories and videos. We invite **unlimited feedback and revisions within each phase**, according to the timeline. Once a phase is approved or its duration expires, we move on; a client can extend a phase for more revisions, knowing it may shift delivery. Backtracking between approved phases may incur additional cost and time.

**Ownership (copyright):**
> [CLIENT] holds full copyright to all final ideas, designs, language, visuals and videos, to use in perpetuity — with minor voiceover exclusions: a VO artist's voice cannot be used to train AI or be reproduced, and videos cannot run on broadcast TV without upgrading VO licenses. On request, we **organize and provide the working files** for any/all assets, free of charge, so your team and partners can build on the work.

---

## PHASE 4 — Markdown conventions

- `#` for the document title, `##` for numbered sections, `###` for subsections. Keep the numbering — Design maps to it.
- **Tables** for anything tabular (deliverables, timeline, competitors). Real markdown tables, not ASCII art.
- **Bold lead-ins** for labelled facts (`**Objective** — …`).
- Bullets for parallel items; short paragraphs for narrative. Don't nest more than two levels.
- Blockquotes only for boilerplate and gap markers.
- No HTML, no CSS, no color values, no font names, no slide numbers, no layout instructions. If you catch yourself writing "eyebrow" or "card grid," delete it.
- Plain-text asset references (filename or URL) so Design can fetch them.
- One file. If it's long, that's fine — long is easier to trim than thin is to fill.

---

## PHASE 5 — Content rules

- Every fact, claim, stat, and persona comes from the provided materials — never invented. Treat brief "examples" as examples, not brand facts.
- Approved claims always carry their required qualifiers.
- No internal process or feedback language — the client reads this content.
- Scale to the sold scope: only phases and deliverables actually in the engagement.
- Unanswered questions get a Phase 1 marker, never AI meta-commentary and never a plausible guess.

---

## PHASE 6 — Handoff

When the markdown is complete, save it as a `.md` file and summarize for the user: the sections included, the deliverables covered, and a list of every gap marker still open. Then tell them it's ready for **Claude Design's Project Overview template**, which expands the markdown into the branded presentation.

If the user asks you for slides, a PPTX, or an HTML deck, remind them that Design owns formatting now and that this skill's output is the markdown brief — then offer to make sure the content is complete instead.
