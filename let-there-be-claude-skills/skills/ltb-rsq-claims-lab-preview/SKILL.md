---
name: ltb-rsq-claims-lab-preview
description: >-
  Build a Claims Lab preview for Let There Be at CHPA's RSQ conference - a Science Intelligence preview deck
  walked through live with regulatory, scientific and quality professionals, built to drop straight into the
  current 15-screen Claims Lab design template. Runs a real Elicit pass, maps the product against its lineup,
  opens three evidence territories with four spotlight studies each, turns them into three or four claims, and
  closes with an illustrative Science Story worked example. Use whenever someone mentions RSQ, CHPA, the Claims
  Lab, a regulatory-audience preview, or a substantiation walkthrough - even if they just say make a Claims Lab
  for a brand. Sources stay blurred. Output is a slot-by-slot content brief matching the Claude Design template,
  plus a presenter sheet carrying full citations, fit, risk and guardrails. Do NOT use for the standard engine
  sales preview (ltb-lit-review-claim-dev-sales-preview), a signed engagement, or a full Science Story.
---

# LTB Claims Lab Preview (RSQ)

## What this is

A **Science Intelligence preview for a regulatory room.** LTB presents it live at CHPA's RSQ conference to regulatory affairs, scientific affairs and quality professionals.

The deck is built in Claude Design from a fixed **15-screen template** (the Banana Boat Mineral build is the reference). This skill's job is to do the research and write every variable slot in that template, in the template's order, at the template's lengths, so the brief can be pasted into Design without rearranging or cutting.

The deck is presented, not read. Speaker notes are the talk track. The substantiation depth this audience expects (fit to product, risk, guardrails, where the line sits) lives on the **presenter sheet**, so the presenter can answer anything the room asks.

Read `references/deck-structure.md` first, then fill `references/output-template.md` screen by screen.

## Who is in the room, and what that changes

RSQ attendees review claims for a living. They know structure/function, monographs, Drug Facts, MLR, FTC substantiation and competent-and-reliable evidence better than most marketers. Write for that.

- **Use the precise regulatory term** in speaker notes and on the presenter sheet. Do not explain these. Do explain biology the first time it appears; the room is regulatory, not always clinical.
- **Name the weakness before they find it.** In vitro only, small panel, self-report, dose above label, a population that doesn't match the buyer. It goes in the spotlight speaker note and in the claim record. A reviewer trusts a presenter who flags the gaps and distrusts one who hides them.
- **Never let a claim outrun its category.** A supplement does not get a disease claim on the claims slide. A monograph OTC stays inside its monograph. If the brand already has a basis for something stronger, say so on the presenter sheet and rate it HIGH until MLR confirms it.
- **Claim lines stay consumer-facing.** The claims are what a shopper would read. The substantiation behind them is written for the reviewer.

## Writing voice — plain and factual

Plain, straightforward, true to the work. Never overrides scientific accuracy or regulatory scoping.

- Lead with the fact. Short, declarative sentences. Specific over vague: name the active, the finding, the number, the design.
- No salesmanship: no superlatives or buzzwords (best, revolutionary, game-changing, breakthrough, powerful, cutting-edge), no rhetorical hooks, no wordplay. This room reads hype as a compliance problem.
- Headlines state the point.
- Em dashes: at most one per slide, only when a comma or period will not do.
- Say it once.

`references/copy-craft.md` governs the claim lines (§1, §2, §3, §7, §11, §12), the worked example (§9), and the three versions in "Where the line sits" on the presenter sheet (§8, §10, §11).

## Reference files

| File | Read it when |
|---|---|
| `references/deck-structure.md` | First. Every screen and slot in the template, boilerplate copy, lengths, emphasis, source masking. |
| `references/output-template.md` | When writing. The skeleton the brief is filled into. |
| `references/regulatory-scoping.md` | Before Phase 4. Claim types, qualifiers, product fit and the risk rating by regulatory class. |
| `references/copy-craft.md` | Before writing claims and the worked example. Shared with the other LTB skills; do not edit here alone. |
| `references/brand-system.md` | Only if Design asks for intent. The template already carries the look. |

> **Output:** one markdown file, `[brand]-rsq-claims-lab.md`, in the outputs folder, following `output-template.md` exactly. Part 1 is the deck, slot by slot, with a speaker note per screen. Part 2 is the presenter sheet, clearly marked not for the deck. No styling, no export: the Design template carries the look, and decks ship as PDF.

## Inputs

The presenter gives a product, and ideally a sentence of angle ("the site says 'blends in' but never says why that matters"). Infer the rest and state assumptions in one line back:

- **Actives and labeled dose or form.** From the pack or Drug Facts. The fit column on the presenter sheet depends on it.
- **Regulatory class and market.** US OTC monograph, US dietary supplement, UK P/GSL medicine, device, etc.
- **Brand owner.** For the cover's "Prepared for" logo and the MLR line on screen 14.
- **The lineup.** The other SKUs in the brand's range, their actives and what they claim. Screen 06 is built on it.
- **Current claims.** Verbatim from the brand's public site or pack.

Do not interrogate. State assumptions and proceed.

## Phase 1 — Research

Use the connected Elicit tools: `search_papers` (prioritize meta-analysis, systematic review, RCT; recent and landmark) and `search_trials`. Load them with the tool search first and use the returned parameter names. Do not run `create_systematic_review`; that depth is the paid engagement.

If Elicit is not connected or returns nothing usable, stop and say so. An invented PMID in front of a room of regulatory reviewers is the worst possible outcome of this skill.

Every study must be real and tool-sourced with a resolving PMID, DOI or NCT. Identifiers are blurred on the slide but must be correct: the presenter will be asked for them, and they go in full on the presenter sheet.

For each study, capture what a reviewer will ask: design, n, population, dose and form, comparator, primary endpoint, blinding, and whether it matches the product's labeled dose.

## Phase 2 — Product context

Map the lineup: each SKU's actives and its job on the shelf. Then find this SKU's job, the thing it does that the others don't. That becomes the screen 06 subhead.

Sort the current claims into those that already have science behind them and those that don't, and find the open lane: what the evidence supports that nobody on the shelf is saying. Write the three opportunity cards, one per territory, with the open lane first and emphasized.

## Phase 3 — Territories and spotlights

Pick **exactly three territories**. A territory is a line of evidence that either sits behind a claim the brand already makes, or opens something the brand doesn't say at all. Tag each `Behind an existing claim` or `New territory`. At least one should be `New territory`; run it last, so the deck builds toward it.

For each, choose **four studies** for its spotlight, ordered so they build the argument, with the number the claims will use on the last row. For each row, write the key finding as lead-in, mint result and optional purple context (see `deck-structure.md`). Use purple where a reviewer would raise something: a competing ingredient that performs too, a limit on who the result covers. One or two purple lines per slide, not four.

Write the limitation of each set into its speaker note.

In the presenter sheet, list one or two runner-up territories and why they lost.

## Phase 4 — Key findings and claims

Write **three key-finding cards**, one per territory. These are evidence statements with no product name (copy-craft.md §6). Every number must appear in a spotlight row.

Then read `references/regulatory-scoping.md` and copy-craft.md §2, §3, §7, §11, §12, and write **four claims** (three if the evidence only carries three). Each plays a different role: the category gap, the population, the behavior, the formula.

On the slide, each claim is a line in quotes plus one support sentence. The craft rules:

- **Lead with the number or finding, then let the product arrive in its own sentence.** A category statistic never shares a sentence with the product name, so it can never read as a product result.
- The qualifier matches the design ("clinically shown" only on a human RCT for that endpoint at the product's dose and form). Never "proven."
- Comparators by molecule, not brand.
- Grammar and punctuation checked: matching curly quotes, plural agreement ("4 in 10 top sunscreens"), the registered mark on the brand.

For every claim, record on the presenter sheet (not the slide): claim type, role, the studies it rests on, **product fit** on dose, form, regimen and population (`Matches` / `Partial` / `Gap` with the reason), **risk** LOW / MEDIUM / HIGH per `regulatory-scoping.md`, the **guardrail** (words the line may not use and any it must keep), and what would lower the risk.

**Honest risk beats clean risk.** Four LOW-risk claims reads as timid or unexamined to this room. The presenter sheet should show the real mix.

## Phase 5 — Where the line sits (presenter sheet)

Choose the one claim with the most regulatory tension, where the evidence invites a stronger line than the category allows. Write it three ways (copy-craft.md §8, §10, §11): **Too far** and the one reason it fails; **Where it lands**, the screen 12 line; **Left on the table**, the timid version and what it gives up. Add the question to put to the room ("Would you clear the middle one? What would you change?"). This is the presenter's material for the Q&A, not a slide.

## Phase 6 — Science Story worked example

Read copy-craft.md §9 first. Build the screen 13 story from the claims: a 2–5 word headline, a six-line narrative in the arc in `deck-structure.md` (problem, cost, "That's why [product]", proof, support, sign-off), three illustrative scores in the 70s, and a five-line heatmap. Label it `Illustrative — not [Brand] data` on the slide and say so in the speaker note. The story reuses claim language; it adds no new claims.

## Phase 7 — Fill the brief

Fill `output-template.md` top to bottom. Boilerplate screens are listed by label only. Check every slot against the lengths in `deck-structure.md`, especially the *one line* slots (cover subtitle, current claims), which break the layout if they wrap.

Then complete the presenter sheet: full citations for every study, the claim record, where the line sits, runner-up territories, and three likely questions with short answers.

## Non-negotiables

- 15 screens in the template's order, labels intact, boilerplate reproduced exactly.
- Three territories, four studies per spotlight, three key-finding cards, three or four claims.
- Every study real and tool-sourced; identifiers on the slide for blurring and in full on the presenter sheet.
- Sources masked, substance legible.
- Every number on screens 11, 12 and 13 traces to a spotlight row.
- Product name never in the same sentence as a category statistic.
- The worked example is labeled illustrative on the slide and in the note. No scores anywhere else. No prices anywhere.
- Every claim has a complete record on the presenter sheet: type, fit, risk, guardrail.
- Screen 06 speaker note states plainly: public science and public claims only, no brand documents, no conversations with the team.

## Definition of done

Report back in a few plain lines:

- 15 screens, labels and slot order matching the template; boilerplate untouched.
- Every study has a real, tool-sourced identifier; all appear on the presenter sheet.
- Every finding reads with its citation blurred.
- Every slot inside its length; *one line* slots fit on one line.
- Each spotlight speaker note names a real limitation.
- Claims: three or four, number-first with the product in its own sentence, each passing the copy-craft.md §12 self-edit, with a full record on the presenter sheet and an honest risk mix.
- Worked example labeled illustrative; its claims match screen 12.
- No superlatives, prices or invented results.
- Assumptions stated in one line; presenter sheet complete.
