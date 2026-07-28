---
name: ltb-lit-review-claim-dev-sales-preview
description: >-
  Run a Lit Review™ + Claim Dev™ sales preview for Let There Be — point it at a prospect's product and category and it produces a substantive, unbranded preview deck (Claude Design brands + exports) previewing the science we'd uncover and the claims it unlocks. Use whenever a salesperson or BD person wants a pitch preview, a prospect teaser, a "what could we find / what could they claim for [brand]" deck, a pre-engagement sales asset, or a science-and-claims sample to help land a client — even if they just say "make a lit review preview for [brand]" or "build a claim preview to pitch [prospect]." Does a light Elicit pass (papers + trials, no systematic review), then does real claim development to surface spotlight studies and 4–6 ownable sample claims, and ends on a hook to engage. Output is an unbranded presentation draft for Claude Design. Do NOT use for a real signed engagement (use ltb-science-intelligence + ltb-lit-review-deck) or for Science Story clusters/narratives.
---

# LTB Lit Review™ + Claim Dev™ Sales Preview

## Writing voice — plain and factual

All copy in this deliverable follows one standard: plain, straightforward, and true to the work. We make complex science clear; the writing should do the same. This never overrides scientific accuracy or MLR/regulatory scoping — every claim still traces to a verified source.

- **Lead with the fact, not the flourish.** State what's true and what the brand does; let the evidence carry the weight. No hype, no hard sell.
- **Short, declarative sentences.** Explain it the way you would to a smart colleague who isn't a scientist. Cut any word that isn't doing work.
- **Specific over vague.** Name the ingredient, the finding, the number, the source. Specificity is what earns trust.
- **No salesmanship or showmanship.** Avoid superlatives and buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), teaser/hype phrasing, rhetorical-question hooks, wordplay, and puns. Never write to dazzle or to "sell."
- **Earned confidence, stated plainly.** Present results and experience without boasting; don't let adjectives do the persuading.
- **Headlines state the point; they don't perform.** No taglines written for effect.


You are building a **sales preview** that shows a prospect two things: the strong science we'd uncover for their brand, and the **new, ownable claims** that science supports. It's a preview, not the paid deliverable: light on research depth, honest about caveats, but genuinely sharp on claims. The claims are the centerpiece; present them as real, specific opportunities grounded in the science.

**Output: an unbranded, content-first presentation draft** — aim ~9–12 slides of copy + layout intent.

> **Output: an unbranded, content-first presentation.** Produce the full deck as slide-by-slide copy + clear layout intent — **no LTB branding, no styling, no file export.** We take this into **Claude Design**, which applies all branding and exports the final file. Don't spend compute making it look nice; spend it on correct, complete content and structure. Any brand/visual references below are **intent notes for Claude Design**, not things to render here.

## Inputs — take what the rep gives and run with it

A salesperson runs this, usually mid-conversation. They'll give you a little — often just a **product/brand and a category** ("Tylenol, pain" · "a new magnesium sleep gummy" · "Flonase, allergy"). Do **not** interrogate them. Take what they give and extrapolate the rest:

- **Active ingredient(s):** if not stated, identify them (Tylenol → acetaminophen, Advil → ibuprofen, Flonase → fluticasone; for a described product, infer from category + a quick search). If several are plausible, pick the most likely 1–2 and note the assumption.
- **Regulatory class:** infer it (OTC monograph drug / supplement / homeopathic / etc.) — enough to keep claims plausible and correctly caveated.
- **Territories / angles:** choose 2–3 promising directions to organize around (competitive vs. a rival, an underserved population, a high-value symptom), based on the science you find.
- **Competitor:** pick the obvious category rival to frame against if none is given.

Only ask a question if you truly can't proceed. Otherwise state your working assumptions in one line (a small scope note in the deck and back to the rep) and build.

## Phase 1 — Light research (organized by territory)
Use the connected Elicit tools — **`search_papers`** (run both `elicit` and `pubmed`, prioritize `typeTags` Meta-Analysis / Systematic Review / RCT, recent years) and **`search_trials`**. Do **NOT** run `create_systematic_review` — that depth belongs to the paid engagement.

Pull a strong set organized by your 2–3 territories — ~6–10 studies total worth spotlighting. For each: year, first author, PMID/DOI, one-line key finding, design, and evidence direction (Pivotal / Positive / Mixed / Note). Favor clear, ownable, recent, or landmark findings. Every study must be real and tool-sourced — never invent a study, statistic, or PMID.

## Phase 2 — Claim development (the centerpiece — do this properly)
Read `references/claim-development.md` and do **real claim development**, not a token list. Derive **4–6 sample claims** across the territories. For each claim: a tier (DTC-ready / DTC + HCP / HCP hero), a short name, the claim in quotes, an **"Ownable:"** rationale naming the specific study/authority, a whitespace/differentiation read, and a regulatory-risk sense scoped to the product class. Mix science-forward claims ("this ingredient does X") with positioning-forward ones (science advancing a market angle). Where evidence is early (e.g., preclinical), say so inline. Keep everything clearly **illustrative and directional — subject to MLR and legal review**.

## Phase 3 — Assemble the preview deck (unbranded draft)
Read `references/preview-structure.md` for the arc: cover → why it matters → territories → spotlight studies → how science becomes claims → **the claims (centerpiece)** → what the full engagement adds → the ask. Write every slide's copy and note its layout intent (e.g., "study table", "claim cards", "PMIDs should link to PubMed"). Use current website language. **Do not brand, style, or export** — hand the draft to Claude Design, which applies the brand system and produces the final file. `references/brand-system.md` is there only as intent for Design.

## Non-negotiable framing
- Every science/claims slide: footer **"Preview · no brand input · findings not validated."** Claims: **"Illustrative & directional — subject to MLR and legal review."**
- Make explicit what the preview did NOT do (no brand input, no systematic review, no MLR, no consumer testing) and that those live in the full engagement — the value gap that motivates the sale.
- Impress and open a door; don't hand over the full paid product for free.

## Guardrails
- Real, tool-sourced studies only — no fabricated papers, PMIDs, or numbers. A few strong verified studies beat many shaky ones.
- Claims are directional, caveated, and scoped to the plausible product class.
- State working assumptions briefly so the rep can correct them, but don't block — deliver a finished preview.
- On-brand, website language, no "gems" — claims (and, in the full engine, claim clusters) only.
- End on a clear, specific next step.
