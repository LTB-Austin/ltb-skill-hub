---
name: ltb-science-101
description: >-
  Build the Science 101 presentation for Let There Be - the internal team briefing after a Science
  Story is approved, bringing the creative team up to speed before production. Use whenever the user
  wants a Science 101, a science briefing for the creative team, a project and science rundown, or an
  animator-facing MOA walkthrough - even if they just say make the science 101 for a client, brief the
  team on this project, or walk the animators through the science. Covers project details and
  deliverables, a plain-language MOA walkthrough written so animators can visualize it, what Science
  Intelligence uncovered, the client claim-cluster priorities, the Science Story options presented,
  and the one they approved. Output is an unbranded presentation for Claude Design. Do NOT use for
  client-facing decks - ltb-project-overview, ltb-lit-review-deck, and ltb-science-story are separate
  skills.

---

# Skill: LTB Science 101 — Internal Team Briefing

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

This deck is **internal**, so the voice is even plainer than a client deck: teaching, not pitching. It should read like a smart colleague explaining the project out loud.

---

## What a Science 101 is

The Science 101 happens **after the Science Story is approved by the client and before production begins.** It is an internal meeting where the science/strategy lead walks the delivery team through the whole project: what we're making, the science behind the product, and the path that got us to the approved story.

**Who's in the room:** the science/strategy lead presenting, the account manager, and the creative team — script writer, illustrators, 2D/3D animators, and interns.

**Why it exists:** the creative team is about to visualize a mechanism they didn't research. They need the science in plain language, the reasoning behind the approved direction, and enough context to make good visual decisions without re-litigating settled ones.

**What success looks like:** an animator can read the MOA section and start sketching. A writer can see which claims are approved and which are off-limits. Everyone understands why *this* story won and what came before it.

> **OUTPUT: an unbranded, content-first presentation.** Produce the full deck as slide-by-slide copy + layout intent — **no LTB branding, no styling, no file export.** It goes to **Claude Design**, which applies branding and exports. Spend compute on correct, complete, well-sequenced content — not on making it look nice. Brand/visual notes below are **intent notes for Claude Design**.

Build as clean 16:9 slides (self-contained HTML, one `<section>` per slide) unless the project space indicates otherwise.

---

## PHASE 0 — Inputs

Pull from the attachment or project files; ask only for what's missing. **Never invent science, claims, or client decisions.**

- [ ] Brand / product name + active ingredient(s) and dose
- [ ] Client name, and the meeting date
- [ ] Deliverables in scope (MOA Moment™, Ad-to-Education Sequence™, education videos, influencer kit, etc.) with specs and counts
- [ ] Timeline / production milestones
- [ ] Team on the project and who owns what
- [ ] **The evidence workbook** from Science Intelligence™ (the source of truth for every study and stat)
- [ ] **The approved claim set** + the client's claim-cluster priorities
- [ ] **The Science Story deck** — all options presented, which the client selected, and their feedback
- [ ] MOA detail: how the product works, how it interacts with the body, what the body does with it (PK/PD if available), and the product format
- [ ] Regulatory class + any claim guardrails (what we cannot say)
- [ ] Audience(s) for the content — consumer, patient, HCP

If the Science Story isn't approved yet, stop and say so — a Science 101 briefs an approved direction. Point the user to **ltb-science-story** first.

---

## PHASE 1 — Brand system (intent notes for Design)

- **Surface:** `#F0F0F0`. **Ink:** `#0C0D10` for titles/body. **Mute:** `#6B6B6E` for eyebrows and captions.
- **Type:** **Lexend** — 700 titles, 300/400 body, 600 eyebrows. No emojis. No corner chevrons.
- **Eyebrow → Title → 3pt black divider (~3/4 width) → content** on nearly every slide.
- **Accents (sparing, never on body copy):** Teal `#87CCCB` / deep teal `#5E9A93`, Mint `#9AD9CC`, Sky `#869FBC`, Purple `#9B83AA`. Reserve Coral/Red for genuine negatives only.
- **Mitosis gradient** (`linear-gradient(110deg, #94CAB4 0%, #7FB6CC 18%, #7C82A1 38%, #8C6C8F 52%, #D84B40 70%, #E66E52 86%, #EC986F 100%)`) — one accent per slide max, as a corner blob or thin rule. Never behind or on type.
- **Sub-brand marks only on the slide about that thing:** Science Intelligence™, Science Story™, Science Studio™, MOA Moment™.
- Because this is internal, favor clean and legible over decorative. Diagrams beat card grids here.

---

## PHASE 2 — Deck structure

Five sections, in this order. The sequence is deliberate: **what we're making → the science → how we got here → what's approved → what happens next.** The science comes before the strategy so the team understands the product before they see the claims built on it.

### SECTION 01 · The project

1. **Cover** — eyebrow `SCIENCE 101`; product/brand name; one-line program descriptor; `[CLIENT] · [MONTH YEAR]`; gradient blob.
2. **Why we're here** — 3–4 lines on the purpose: the Science Story is approved, production is starting, and this session gives the team the science and the context behind it. Name who's in the room and what each person should walk away with.
3. **Agenda** — the five sections as a numbered list with one-line descriptions.
4. **The project at a glance** — client, product, audience(s), regulatory class, and the objective in one plain sentence. Compact table or two-column layout.
5. **What we're making** — one row or card per deliverable: name, format/specs, length/dimensions, audience, and where it runs. Pull verbatim from scope; do not add deliverables.
6. **Timeline & who owns what** — production milestones mapped to dates, plus team roles. Flag the dates that constrain creative.

### SECTION 02 · The science

This is the heart of the deck. Full guidance in `references/moa-walkthrough.md` — follow it.

7. **The product** — what it is, active ingredient(s) and dose, format, and how a person actually uses it. Plain language.
8. **The problem in the body** — what's happening physiologically *without* the product. Establishes the baseline the product acts on; usually the opening beat of any MOA animation.
9. **How it works — the MOA walkthrough** — the mechanism as **numbered sequential beats** (typically 4–7). Each beat: what happens, where in the body, and what it looks like. Written so an animator can visualize it without a biology background. One beat per slide if the mechanism is complex.
10. **What the body does with it** — absorption, distribution, timing, duration, clearance, in plain terms. Include real numbers (onset, peak, half-life) where the evidence supports them.
11. **Scale & setting** — the physical scale of each beat (molecular / cellular / tissue / whole-body) and where the "camera" sits. This directly informs animation staging.
12. **What the science does *not* say** — the honest limits: steps that are inferred rather than demonstrated, extrapolations, and anything the team must not visualize as established fact. Protects us in MLR.

### SECTION 03 · What Science Intelligence™ uncovered

13. **How we researched it** — one plain slide: scope of the literature review, what was searched, how much came back.
14. **What we found** — the strongest evidence, organized by theme or active. Per finding: the plain-language takeaway, the study behind it, and evidence strength (Pivotal / Positive / Mixed / Note). Every line traces to the workbook — never invent a study or stat.
15. **Spotlight studies** — the 2–3 studies doing the most work for this brand. Design, population, result, and why it matters to the story.
16. **Claim territories that opened up** — the areas the evidence let us claim in, and which were closed off. Plain, not salesy.

### SECTION 04 · The path to the approved story

17. **The client's priorities** — which claim clusters the client cared about most, and their stated reasoning. Attribute it to them; don't editorialize.
18. **The claim clusters** — each cluster: name, strategic idea, and the claims inside it. Mark which are approved for use.
19. **Science Story options we presented** — each option with its headline, its angle, and a one-line note on what it emphasized. Show the real set so the team sees the range considered.
20. **What they chose, and why** — the selected direction, the client's reasoning, and any feedback or edits that came with it. If they rejected a direction for a specific reason, say so — it prevents the team from reintroducing it.

### SECTION 05 · What we're producing

21. **The approved Science Story** — the final headline and narrative in full, as approved. This is the source text creative works from.
22. **Approved claims & guardrails** — a clean two-column list: claims we can use (with required disclaimers) beside language we cannot use. The most-referenced slide in the deck; make it unambiguous.
23. **What this means for creative** — the practical translation: which beats matter most visually, tone, must-includes, known constraints.
24. **Next steps** — immediate actions with owners and dates (typically: art styles → scripts → storyboards/animatic).
25. **Questions** — a plain closing slide.

Adapt to scope: if a mechanism is simple, collapse the MOA beats onto fewer slides; if there was only one Science Story option, say that plainly instead of inventing a range.

---

## PHASE 3 — Optional: the NotebookLM video companion

The lead sometimes produces a short video walkthrough of the science alongside the deck. If asked, also output a **narration script**: 2–4 minutes, plain spoken language, following the Section 02 beats in order, with a visual cue in brackets for each beat. Same accuracy guardrails apply. This supplements the deck, never replaces the MOA slides.

---

## PHASE 4 — Content rules

- **Everything traces to a source.** Science from the workbook; claims from the approved claim set; client decisions from the Science Story feedback. If it isn't in the inputs, ask — don't fill the gap.
- **Never invent a study, statistic, citation, or client rationale.**
- **Approved claims are verbatim.** Do not reword an approved claim; MLR approved specific language.
- **Separate fact from inference.** If a mechanism step is inferred, label it. The team will otherwise animate it as settled fact.
- **Write for the animator.** Where a beat has a visual consequence, say what it looks like — not just what it does.
- **Keep the client's voice attributed.** Their priorities and reasoning are theirs; don't blend them into ours.
- **Internal deck, internal candor.** Include what didn't work and what we can't say. That's the point of the meeting.
- **No emojis. No process instructions on slides.**

---

## PHASE 5 — Output requirements

- **Format:** unbranded, content-first slide-by-slide draft → Claude Design brands and exports.
- Every slide: eyebrow, title, body copy, layout intent, and any asset it calls for.
- Include a short **speaker note** under each science slide — the one or two sentences the presenter says out loud. This deck is presented live, so the talk track matters.
- After each revision round, summarize what changed and on which slides.
