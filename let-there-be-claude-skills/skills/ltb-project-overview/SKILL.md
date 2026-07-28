---
name: ltb-project-overview
description: "Build client project overview presentations for Let There Be Science Marketing. Use when creating, editing, or refining a project overview deck for any LTB client — even if someone just says 'make the overview for [client]' or 'put together the project overview.' Works inside a Claude project space: it pulls from the attached brief, brand book, science, and partner docs (or the project files), builds the full slide-by-slide deck on the current LTB brand and the three-phase engine (Proof / Persuasion / Production), then hands off to Claude Design to polish and export. Do NOT use for the Lit Review/Claim Dev deck, Science Story deck, or sales previews — those are separate skills."
---

# Skill: LTB Project Overview Deck Builder

## Writing voice — plain and factual

All copy in this deliverable follows one standard: plain, straightforward, and true to the work. We make complex science clear; the writing should do the same. This never overrides scientific accuracy or MLR/regulatory scoping — every claim still traces to a verified source.

- **Lead with the fact, not the flourish.** State what's true and what the brand does; let the evidence carry the weight. No hype, no hard sell.
- **Short, declarative sentences.** Explain it the way you would to a smart colleague who isn't a scientist. Cut any word that isn't doing work.
- **Specific over vague.** Name the ingredient, the finding, the number, the source. Specificity is what earns trust.
- **No salesmanship or showmanship.** Avoid superlatives and buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), teaser/hype phrasing, rhetorical-question hooks, wordplay, and puns. Never write to dazzle or to "sell."
- **Earned confidence, stated plainly.** Present results and experience without boasting; don't let adjectives do the persuading.
- **Headlines state the point; they don't perform.** No taglines written for effect.


You build the **client project overview** — the kickoff deck that shows a client (and any partner) the whole engagement: what we'll do, the brand and science we've absorbed, the challenge, and how the Science Marketing Engine™ solves it phase by phase.

## The workflow this skill lives in

1. You're running in a **Claude project space.** The brief, brand book, science, partner details, and any prior decks are attached to the message or already in the **project files** — use them. If a needed input isn't there, ask for it (don't invent it).
2. You produce the **complete deck, slide by slide** — every slide's eyebrow, title, copy, layout intent, and which brand assets/imagery it calls for — on the current LTB brand, following the structure below.
3. The draft then goes to **Claude Design to polish the visuals and export** the final file. So: **your job is correct, complete, on-brand content and layout direction; Claude Design does the final visual polish and file export.** Get the substance and structure exactly right; specify the visual intent clearly; don't fuss over pixel-level production here.

Build the draft as clean 16:9 slides (self-contained HTML is the friendliest handoff to Design, one `<section>` per slide) unless the project space indicates another format. Do not lock the deck to PPTX in this step — export happens in Design.

---

## PHASE 0 — Inputs

Confirm you have (from the attachment or project files; ask only for what's missing):

- [ ] Brand / product name (+ active ingredient, INN/common)
- [ ] Client + any partner (e.g., "Prepared for Glenmark · in partnership with PatientPoint")
- [ ] The objective / what success looks like
- [ ] Key deliverables in scope (Science Intelligence, Science Story, Science Studio pieces — MOA video, patient/HCP video, ad-to-education, influencer kit)
- [ ] Timeline start month + any pilot/launch target
- [ ] Brand materials (brand book, palette, packaging, logo) — for the Deep Dive
- [ ] The science (MOA, formulation, clinical) and any approved claims + guardrails
- [ ] Audience(s) — patient and/or HCP
- [ ] Reference project-overview deck (for structure/tone) if available

Never invent client-side facts (personas, taglines, claims, tone). Leave blank or mark "To be defined with [Client]" if not provided.

---

## PHASE 1 — Brand System (current 2026 rebrand)

- **Surface:** `#F0F0F0` on every slide. Never pure white for the slide background (cards may be white).
- **Ink:** `#0C0D10` for all titles and body. **Mute:** `#6B6B6E` for eyebrows, labels, captions.
- **Type:** **Lexend** throughout — 700 for titles, 300/400 for body, 600 for eyebrows/labels. No emojis. No corner chevrons.
- **Eyebrow → Title → Divider:** almost every content slide leads with a small uppercase, letter-spaced **eyebrow** in mute (e.g., `DEEP DIVE · ABOUT THE BRAND`, `SCIENCE INTELLIGENCE™ · 01`), then a large bold **title**, then a **3pt black divider** running ~3/4 width below the title.
- **Accent palette (use sparingly — never on body copy or titles):** Teal `#87CCCB` / deep teal `#5E9A93`, Mint `#9AD9CC`, Sky `#869FBC`, Purple `#9B83AA`, Coral `#F3755C`, Red `#EB6758` (genuine negatives only).
- **The mitosis gradient (signature accent):** `linear-gradient(110deg, #94CAB4 0%, #7FB6CC 18%, #7C82A1 38%, #8C6C8F 52%, #E1483B 70%, #EE6B4D 86%, #F2966A 100%)`. Reserve it for one accent per slide — a corner blob (bleeding off the edge), a card top-cap, a step number, a thin rule. Never behind or on top of type.
- Do **not** use the retired palette (teal `#008575` and its siblings) if you see it in an old deck.

---

## PHASE 2 — Logos & Imagery (specify intent; Design places finals)

Call out, per slide, which brand asset belongs there. Final files live in the Brand Archive / project files; Design positions them.

- **LTB wordmark:** top-left on the cover; bottom corner on content slides (corner matches the slide's content weight).
- **Client logo:** on the cover and section dividers (top-right). Not on every content slide unless asked.
- **Partner:** name the partner in the cover subline and the "Our Solution" slide when there is one.
- **Sub-brand marks — only on the slide about that thing:** Science Intelligence™, Science Story™, Science Studio™, MOA Moment™, Ad-to-Education Sequence™, Influencer Science Kit™. (There is no "Gems" mark — that language is retired; the unit is a **claim**, grouped into **claim clusters**.)
- **Mitosis gradient blobs:** as a large corner accent, varied corner per slide, never over text. Heavier on the cover, section dividers, and closing.

---

## PHASE 3 — Deck Structure (the current model)

The deck runs as **four numbered sections**, and Section 03 carries the **three-phase engine**. Section dividers read `SECTION 0N · OF 04`. Adapt to scope — drop a phase if it isn't sold (e.g., no Science Studio → no Production phase), and scale the Deep Dive to the material you have.

**SECTION 01 · Review project details**
1. **Cover** — LTB wordmark top-left; eyebrow `PROJECT OVERVIEW`; client logo + a one-line program descriptor ("A Patient & HCP Science Marketing Program"); 3pt divider; `PREPARED FOR [CLIENT] · IN PARTNERSHIP WITH [PARTNER] · [YEAR]`; ingredient line bottom-right; gradient blob top-right.
2. **Agenda** — "What we'll cover today" — the four sections as a numbered list with one-line descriptions.
3. **Section 01 divider.**
4. **Project Overview** — the objective in one clear headline + a short paragraph on strategy and focus.
5. **Key Deliverables** — a clean table: `Asset | Phase | Duration | Format | Placement`.
6. **Timeline** — kickoff → pilot/launch, month by month; note phases flex with feedback.

**SECTION 02 · Deep dive (the brand)** — "our grasp of the brand, so every team we hand off to starts from the same understanding."
7. **Section 02 divider.**
8. **About the Brand** — what the product is, in plain language.
9. **Brand at a glance / Brand Materials** — logo, packaging, palette (stand-ins if finals aren't in yet).
10. **Brand Identity** — connection, character, tone.
11. **Brand Idea & Platform** — the organizing idea (if the client has one).
12. **Main Competitors** — primary / secondary (Rx) / OTC alternatives.
13. **Target Audience** — patient audience and/or HCP audience.
14. **Useful Links** — brand book, sales aid, assets (as provided).

**SECTION 03 · The challenge & our solution**
15. **Section 03 divider.**
16. **The Challenge** — a plain headline statement of the core problem.
17. **The Four Forces** (or market dynamics) — the forces working against the brand.
18. **Objectives** — what success looks like, split by audience (For HCPs / For Patients).
19. **Our Solution** — "one science foundation, deployed everywhere" via the Science Marketing Engine™ (and the partner channel, if any).
20. **Our Operating Model** — "One engine. Three phases." Three cards: `01 · THE PROOF — Science Intelligence™`, `02 · THE PERSUASION — Science Story™`, `03 · THE PRODUCTION — Science Studio™`.
21. **Phase 01 · The Proof divider** — "What's true — and what we can say."
22. **Science Intelligence™ — the truth** — uncovering the science + "what we deliver" (lit review, evidence).
23. **Science Intelligence™ — the science & MOA** — the mechanism, made clear (split layout, visual right).
24. **Science Intelligence™ — claims** — "claims that hold up and move people," shepherded through MLR.
25. **Phase 02 · The Persuasion divider** — "Evidence, made to move."
26. **Science Story™ — the narrative(s)** — the story per audience ("Two audiences. Two stories. One source of truth.").
27. **Creative Direction** — the tone the story should carry ("confident and human, never clinical").
28. **Science Story™ — consumer testing (optional)** — "de-risk the creative before it becomes video."
29. **Phase 03 · The Production divider** — "Content that converts."
30. **Science Studio™ — [deliverable]** — one slide per production piece (e.g., patient video, HCP video, MOA Moment™).
31. **Why This Works** — the strategic payoff of the integrated approach.
32. **How We Work** — milestone model / unlimited revisions within a phase (boilerplate — Phase 5).
33. **Ownership** — copyright & working files (boilerplate — Phase 5).
34. **Getting Started** — the Lit Review™ kickoff.
35. **Lit Review™ Questions** — what we need to align on (evidence, guardrails, priorities).

**SECTION 04 · Questions & discussion**
36. **Section 04 divider.**
37. **Next Steps** — numbered action items.
38. **Closing** — "Thanks for trusting us with your science." + "Science leads. Creativity amplifies." Large gradient blob; LTB wordmark.

---

## PHASE 4 — Slide patterns

- **Section divider:** eyebrow `SECTION 0N · OF 04`; large section title lower-left; one-line description; client logo top-right; gradient blob one corner; no body.
- **Phase divider (Proof/Persuasion/Production):** eyebrow `PHASE 0N · THE [PROOF/PERSUASION/PRODUCTION]`; a short, plain line ("What's true — and what we can say."); gradient accent.
- **Content slide:** eyebrow → bold title → 3pt divider → content. Vary layout — full-width narrative with bold lead-ins, split (narrative left / visual or stat right), 2–4 card grid, or numbered list. Don't default to card grids; use them only for genuinely parallel content. Pick one card style for the deck and keep it consistent.
- **Table slide (deliverables):** white rounded container, subtle horizontal rules, bold gray headers, no heavy gridlines.
- **Operating-model / three-up:** three equal cards, each with a numbered eyebrow (`01 · THE PROOF`), the service name bold, one-line description.
- **Deliverable/phase slides:** the relevant sub-brand mark, a bold subheading, a 1–2 sentence description, and either accent-bulleted points or a split with a stat/visual (big bold accent stats like "+133% ROAS").

---

## PHASE 5 — Boilerplate (use consistently; adapt names only)

**How We Work (milestone model):**
> Unlike agencies that cap revisions, Let There Be uses a milestone model to deliver the strongest possible Science Stories and videos. We invite **unlimited feedback and revisions within each phase**, according to the timeline. Once a phase is approved or its duration expires, we move on; a client can extend a phase for more revisions, knowing it may shift delivery. Backtracking between approved phases may incur additional cost and time.

**Ownership (copyright):**
> [CLIENT] holds full copyright to all final ideas, designs, language, visuals and videos, to use in perpetuity — with minor voiceover exclusions: a VO artist's voice cannot be used to train AI or be reproduced, and videos cannot run on broadcast TV without upgrading VO licenses. On request, we **organize and provide the working files** for any/all assets, free of charge, so your team and partners can build on the work.

**Closing:** "Thanks for trusting us with your science." + "Science leads. Creativity amplifies."

---

## PHASE 6 — Content rules

- Every fact, claim, stat, and persona comes from the provided materials — never invented. Treat brief "examples" as examples, not brand facts.
- Approved claims always carry their required qualifiers.
- No process instructions or internal/feedback language on a client-facing slide.
- Unanswered brand questions (tone, platform, anti-brand) → leave blank or "To be defined with [Client]," never AI meta-commentary.
- Scale the deck to the sold scope: only include phases and deliverables actually in the engagement.

---

## PHASE 7 — Handoff to Claude Design

When the draft is complete: summarize the deck (section/phase structure, deliverables covered, anything left as "to be defined"), confirm every slide has its eyebrow/title/copy and a clear visual intent + named assets, and hand off to **Claude Design to polish the visuals and export**. Keep the copy final and correct — Design should be polishing look, not rewriting substance.
