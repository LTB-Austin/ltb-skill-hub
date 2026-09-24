---
name: ltb-rsq-claims-lab-preview
description: >-
  Build a Claims Lab preview for Let There Be at CHPA's RSQ conference - a Science Intelligence-only preview
  deck walked through live with regulatory, scientific and quality professionals. Runs a real Elicit pass,
  opens two or three evidence territories, and turns them into claims shown beside their proof, product fit,
  risk and guardrail, plus one claim worked through to show where the line sits. Use whenever someone
  mentions RSQ, CHPA, the Claims Lab, a regulatory-audience preview, or a substantiation walkthrough - even
  if they just say make a Claims Lab for a brand. Sources stay blurred. Output is an unbranded deck draft
  for Claude Design plus a presenter sheet. Do NOT use for the standard engine sales preview
  (ltb-lit-review-claim-dev-sales-preview), a signed engagement, or Science Story or Studio work.
---

# LTB Claims Lab Preview (RSQ)

## What this is

A **Science Intelligence preview for a regulatory room.** LTB presents it live at CHPA's RSQ conference to regulatory affairs, scientific affairs and quality professionals. It is the sibling of `ltb-lit-review-claim-dev-sales-preview`, with two changes:

1. **Science Intelligence only.** No Science Story, no Science Studio, no worked example, no test scores. The deck ends at the claims and what the full Lit Review™ and Claim Dev™ would add.
2. **Substantiation is the point.** A marketing audience wants to see a good line. This audience wants to see that the line is earned. So every claim appears next to its proof, its fit to the actual product, its risk, and the words it may not use. One claim is walked to the edge on purpose, so the room can see where the line sits and argue about it.

The deck is presented, not read. Speaker notes are a talk track for the presenter, and two slides carry a question to put to the room.

Read `references/deck-structure.md` first and follow it screen by screen.

## Who is in the room, and what that changes

RSQ attendees review claims for a living. They know structure/function, monographs, Drug Facts, MLR, FTC substantiation and competent-and-reliable evidence better than most marketers. Write for that.

- **Use the precise regulatory term.** "Structure/function," "risk-reduction," "comparative," "monograph-permitted," "qualified." Do not explain these. Do explain biology the first time it appears; the room is regulatory, not always clinical.
- **Show the weakness before they find it.** Open-label design, dose above the labeled dose, a population that doesn't match, a mechanistic-only finding. Name it on the slide, in the footer or the risk column. A reviewer trusts a deck that flags its own gaps and distrusts one that hides them.
- **Never let a claim outrun its category.** A supplement does not get a disease claim on the claims slide. If the brand already has a qualified or legacy basis for something stronger, say what it is and rate it HIGH until MLR confirms it. That tension belongs on the "Where the line sits" slide, not buried in a clean-looking claim card.
- **Claim lines stay consumer-facing.** The claims are what a shopper would read. The substantiation around them is written for the reviewer.

## Writing voice — plain and factual

Same floor as every LTB preview. Plain, straightforward, true to the work. Never overrides scientific accuracy or regulatory scoping.

- Lead with the fact. Short, declarative sentences. Specific over vague: name the active, the finding, the number, the design.
- No salesmanship: no superlatives or buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), no rhetorical hooks, no wordplay. This room will read hype as a compliance problem.
- Headlines state the point. Two-part contrast headlines are house style.
- Em dashes: at most one per slide, only when a comma or period will not do.
- Say it once.

`references/copy-craft.md` governs the claim lines (§2, §3, §7, §11, §12) and the three versions on the "Where the line sits" slide (§8, §10, §11).

## Reference files

| File | Read it when |
|---|---|
| `references/deck-structure.md` | First. Every screen, which are boilerplate, source masking, the footer. |
| `references/regulatory-scoping.md` | Before Phase 3. Claim types, qualifiers and the risk rating by regulatory class. |
| `references/copy-craft.md` | Before writing the claims, the substantiation table and the line slide. Shared with the other LTB skills; do not edit here alone. |
| `references/brand-system.md` | Intent notes for Claude Design only. |

> **Output:** one markdown file, `[brand]-rsq-claims-lab.md`, in `/mnt/user-data/outputs/`. Part 1 is the deck, screen by screen, copy plus speaker note. Part 2 is the presenter sheet, clearly marked not for the deck. No styling, no export. Claude Design places it; decks ship as PDF.

## Inputs

The presenter gives a product, and ideally a sentence or two of angle ("the site leans on the B vitamins but never says why"). Infer the rest and state assumptions in one line back:

- **Actives and labeled dose/form.** From the pack or site. The dose matters more here than in the sales preview, because the fit column depends on it.
- **Regulatory class and market.** US OTC monograph, US dietary supplement, UK P/GSL medicine, device, etc. It sets the claim types and the middle pillar on the claims-method slide.
- **Current claims.** Pull them from the brand's public site or pack. These are slide 04.

Do not interrogate. State assumptions and proceed.

## Phase 1 — Research

Use the connected Elicit tools: `search_papers` (prioritize meta-analysis, systematic review, RCT; recent and landmark) and `search_trials`. Load them with `tool_search` first and use the returned parameter names. Do not run `create_systematic_review`; that depth is the paid engagement.

If Elicit is not connected or returns nothing usable, stop and say so. An invented PMID in front of a room of regulatory reviewers is the worst possible outcome of this skill.

Every study must be real and tool-sourced with a resolving PMID, DOI or NCT. Identifiers are blurred on the slide but must be correct: the presenter will be asked for them, and they go in full on the presenter sheet.

For each study, capture what a reviewer will ask: design, n, population, dose and form, comparator, primary endpoint, blinding, and whether it matches the product's labeled dose.

## Phase 2 — Territories

Pick **two territories** by default, three at most. A territory is a line of evidence that either sits behind an existing claim the brand makes without explaining, or opens something the brand doesn't say at all. Tag each `NEW TERRITORY` or `BEHIND AN EXISTING CLAIM`.

For each, choose **four studies** for its spotlight slide, ordered from the strongest design down or in the order that builds the argument. Include at least one study that complicates the picture if one exists (a null subgroup, an endpoint that did not separate). The Cialis confidence finding (p = 0.10) is the model: it makes the rest more believable.

In the presenter sheet, list one or two runner-up territories and why they lost.

## Phase 3 — Claims

Read `references/regulatory-scoping.md`, then copy-craft.md §2, §3, §7, §11, §12.

Write **three claims** by default, four at most. Each is built on the territories and each plays a different role (mechanism, measured result, population or occasion, comparative). For every claim, record internally:

- The claim line (consumer-facing, one or two sentences, ≤12 words each).
- Claim type (structure/function, comparative, monograph-permitted, risk-reduction, etc.).
- Evidence: design, n, population, and the study it rests on.
- **Product fit**: does the evidence match the labeled dose, form, population and regimen? `Matches` / `Partial` / `Gap`, with the reason in five words or fewer.
- Risk: LOW / MEDIUM / HIGH per `regulatory-scoping.md`.
- Guardrail: the specific words the line may not use, and any word it must keep.

Craft rules for the lines carry over unchanged from the sales preview: measurement stays out of the line; the qualifier matches the design ("clinically shown" only on a human RCT for that endpoint); never "proven"; comparator by molecule, not brand; product never in the same sentence as a prevalence figure.

**Honest risk beats clean risk.** If a claim is MEDIUM because the evidence is at 20 mg and the product is 10 mg, it is MEDIUM on the slide. A deck of three LOW-risk claims reads as either timid or unexamined to this room. The mix should reflect the evidence.

## Phase 4 — Where the line sits

Choose the one claim with the most regulatory tension: the one where the evidence invites a stronger line than the category allows. Write it three ways (copy-craft.md §8, §10, §11):

- **Too far** — the line the evidence tempts you toward, and the one reason it fails (disease claim for a supplement, dose mismatch, open-label support for a superiority line, a closed word).
- **Where it lands** — the defensible version. This is the claim as it appears on the claims slide.
- **Left on the table** — the timid version most brands ship, and what it gives up that the evidence would have supported.

This slide is the "lab." It is where the presenter stops and asks the room how they would rule.

## Phase 5 — Fill the deck

Work through `references/deck-structure.md` screen by screen: the `data-screen-label`, the copy, and a speaker note. Because citations are blurred, every finding sentence must stand on its own. Never write "as Huang et al. showed."

Then write the **presenter sheet** (Part 2): full citations with identifiers for every study on every slide; the internal claim record from Phase 3 for each claim; the runner-up territories; and three questions the room is likely to ask, with a short answer for each.

## Non-negotiables

- Screens in the order in `deck-structure.md`, labels intact, boilerplate reproduced unchanged.
- **No Science Story, no Science Studio, no test scores, no prices** anywhere in the deck.
- Every study real and tool-sourced; identifiers present on the slide for blurring and in full on the presenter sheet.
- Sources masked, substance legible (`filter: blur(4.5px); user-select: none` on identifiers only).
- Every spotlight slide ends with an evidence note naming the limitation.
- Every claim appears on the substantiation slide with its fit, risk and guardrail. No claim floats free of its proof.
- Slide 04 states plainly: public science and public claims only, no brand documents, no conversations with the team.

## Definition of done

Report back in a few plain lines:

- Screen count and labels match `deck-structure.md` for the number of territories used.
- Every study has a real, tool-sourced identifier; all appear on the presenter sheet.
- Every finding sentence reads with its citation blurred.
- Each spotlight slide has an evidence note naming a real limitation.
- Claims: three or four, each passing the copy-craft.md §12 self-edit, each with type, fit, risk and a guardrail that names words.
- The risk mix is honest; any dose, population or design mismatch shows in the fit column.
- "Where the line sits" has all three versions, each with its reason, and a question for the room.
- No Story, Studio, scores, prices, superlatives or invented results.
- Assumptions stated in one line; presenter sheet complete.
