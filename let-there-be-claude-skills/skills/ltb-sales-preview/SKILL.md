---
name: ltb-sales-preview
description: >-
  Build a Science Intelligence preview deck for Let There Be - point it at a prospect's product and it runs a
  real Elicit pass, opens three evidence territories with four spotlight studies each, distills three key
  findings, writes three or four claims, and closes with an illustrative Science Story worked example, all
  inside the 15-screen LTB Sales Preview template. Use whenever someone wants a pitch preview, prospect
  teaser, claims preview, what-could-they-claim deck, pre-engagement sales asset, conference walkthrough or
  leave-behind (including the Claims Lab), even if they just say make a preview for a brand. Sources stay
  blurred. Output is one markdown file that drops field by field into the Claude Design template, plus a
  presenter sheet with full citations, product fit, risk and guardrails. Do NOT use for a signed engagement
  (ltb-science-intelligence, ltb-lit-review-deck) or for real Science Story clusters and narratives.
---

# LTB Sales Preview

## What this is

A **Science Intelligence preview** for a prospect. One product, a real pass through the public science, and a short deck that shows what the full engagement would find and what the brand could claim. It is presented live to a brand team, at a pitch meeting or a conference, and left behind as a PDF.

The deck is built in Claude Design from the fixed **15-screen LTB Sales Preview template** (the Banana Boat Mineral build is the reference). This skill does the research and writes every variable slot in that template, in the template's order, at the template's lengths, using the template's field names. The markdown it produces should go into Design without anyone rearranging, cutting or rewriting it.

The substantiation depth (fit to product, risk, guardrails, where the line sits) lives on the **presenter sheet**, so whoever presents can answer anything the room asks.

Read `references/deck-structure.md` first, then fill `references/output-template.md` screen by screen.

## Who is in the room

A prospect's brand team, and often their regulatory, medical or legal reviewers. Write so both are satisfied: claims a marketer wants to use, scoped tightly enough that a reviewer would take them to MLR.

- **Use the precise regulatory term** in speaker notes and on the presenter sheet (structure/function, monograph, Drug Facts, MLR, competent and reliable evidence). Explain biology the first time it appears.
- **Name the weakness before they find it.** In vitro only, small panel, self-report, dose above label, a population that doesn't match the buyer. It goes in the spotlight speaker note and the claim record.
- **Never let a claim outrun its category.** A supplement does not get a disease claim. A monograph OTC stays inside its monograph. If the brand already has a basis for something stronger, say so on the presenter sheet and rate it HIGH until MLR confirms it.
- **Claim lines stay consumer-facing.** The substantiation behind them is written for the reviewer.

## Writing voice — plain and factual

Plain, straightforward, true to the work. Never overrides scientific accuracy or regulatory scoping.

- Lead with the fact. Short, declarative sentences. Specific over vague: name the active, the finding, the number, the design.
- No salesmanship: no superlatives or buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), no rhetorical hooks, no wordplay. The prospect is judging whether we can write, not whether we can pitch.
- Headlines state the point.
- Em dashes: at most one per slide, only when a comma or period will not do. (The `That’s why` line and boilerplate are exempt.)
- Say it once.

`references/copy-craft.md` governs the claim lines (§1, §2, §3, §7, §11, §12), the worked example (§9), and the three versions in "Where the line sits" (§8, §10, §11).

## Reference files

| File | Read it when |
|---|---|
| `references/deck-structure.md` | First. Every screen and slot in the template, the boilerplate, lengths, emphasis, source masking. |
| `references/output-template.md` | When writing. The skeleton the file is filled into, including the fixed note to Claude Design. |
| `references/regulatory-scoping.md` | Before Phase 4. Claim types, qualifiers, product fit and risk by regulatory class. |
| `references/copy-craft.md` | Before writing claims and the worked example. Shared with ltb-science-intelligence, ltb-lit-review-deck and ltb-science-story; edit all four together. |
| `references/brand-system.md` | Only if Design asks for intent. The template already carries the look. |

> **Output:** one markdown file, `[brand]-sales-preview.md`, in `/mnt/user-data/outputs/`, following `output-template.md` exactly. Part 1 is the deck, with the fixed "For Claude Design" note at the top. Part 2 is the presenter sheet. No styling, no HTML, no export: the Design template carries the look, and decks ship as PDF. Present the file when done.

## Inputs

The presenter gives a product, and ideally a sentence of angle ("the site says 'blends in' but never says why that matters"). Infer the rest and state assumptions in one line back:

- **Actives and labeled dose or form.** From Drug Facts or Supplement Facts. The fit column on the presenter sheet depends on it.
- **Regulatory class and market.** US OTC monograph, US dietary supplement, UK P/GSL medicine, device, etc.
- **Brand owner.** For the cover's "prepared for" logo and the MLR line on screen 14.
- **The lineup.** The other SKUs in the range, their actives and what they claim.
- **Current claims.** Verbatim from the brand's public site or pack.

Do not interrogate. State assumptions and proceed.

## Phase 1 — Research

Use the connected Elicit tools: `search_papers` (prioritize meta-analysis, systematic review, RCT; recent and landmark) and `search_trials`. Load them with the tool search first and use the returned parameter names. Do not run `create_systematic_review`; that depth is the paid engagement.

If Elicit is not connected or returns nothing usable, stop and say so. A preview built from recalled studies is worse than no preview: the presenter will be asked for identifiers, and an invented PMID in front of a prospect is the one thing this skill can never produce.

Every study must be real and tool-sourced with a resolving PMID, DOI or NCT. Identifiers are blurred on the slide but must be correct; they go in full on the presenter sheet.

For each study, capture what a reviewer will ask: design, n, population, dose and form, comparator, primary endpoint, blinding, and whether it matches the product's labeled dose.

## Phase 2 — Product context

Pull four to six current claims, verbatim, each 58 characters or fewer (they sit in pills that cannot wrap). List the actives as Drug Facts or Supplement Facts names them.

Map the lineup: each SKU's actives and its job on the shelf. Find this SKU's job, the thing it does that the others don't. Sort the current claims into those that already have science behind them and those that don't, and find the open lane: what the evidence supports that nobody on the shelf is saying. None of this has its own slide. It goes in the screen 05 speaker note and the presenter sheet, and it decides the territories.

## Phase 3 — Territories and spotlights

Pick **exactly three territories**. Territories 01 and 02 sit behind claims the brand already makes. Territory 03 is the **new territory**, the open lane: it runs last so the deck builds toward it, and it carries the template's `New` pill and emphasis.

For each, choose **four studies**, ordered so they build the argument, with the number the claims will use last or named in the speaker note. Write each key finding as lead-in, mint result and optional purple context (see `deck-structure.md`). Use purple where a reviewer would raise something: a competing ingredient that performs too, a limit on who the result covers. One or two purple lines per screen, not four.

Write the limitation of each set into its speaker note. List one or two runner-up territories on the presenter sheet, with why they lost.

## Phase 4 — Key findings and claims

Write **three key-finding cards**, one per territory. These are evidence statements with no product name (copy-craft.md §6). Every number must appear in a spotlight row.

Then read `references/regulatory-scoping.md` and copy-craft.md §2, §3, §7, §11, §12, and write **four claims** (three if the evidence only carries three). Each plays a different role: the category gap, the population, the behavior, the formula.

- **Lead with the number or finding, then let the product arrive in its own sentence.** A category statistic never shares a sentence with the product name, so it can never read as a product result.
- The qualifier matches the design ("clinically shown" only on a human RCT for that endpoint at the product's dose and form). Never "proven."
- Comparators by molecule, not brand.
- Check grammar and punctuation line by line: matching curly quotes, plural agreement ("4 in 10 top sunscreens miss…"), the registered mark on the brand every time.

For every claim, record on the presenter sheet: claim type, role, the studies it rests on, **product fit** on dose, form, regimen and population (`Matches` / `Partial` / `Gap` with the reason), **risk** LOW / MEDIUM / HIGH per `regulatory-scoping.md`, the **guardrail**, and what would lower the risk.

**Honest risk beats clean risk.** Four LOW-risk claims reads as timid or unexamined. The presenter sheet shows the real mix.

## Phase 5 — Where the line sits (presenter sheet)

Choose the one claim with the most regulatory tension, where the evidence invites a stronger line than the category allows. Write it three ways (copy-craft.md §8, §10, §11): **Too far** and the one reason it fails; **Where it lands**, the screen 11 line; **Left on the table**, the timid version and what it gives up. Add the question to put to the room. This is Q&A material, not a slide.

## Phase 6 — Science Story worked example

Read copy-craft.md §9 first. Build the screen 12 story from the claims: a 2–5 word headline, a six-line narrative in the arc in `deck-structure.md`, three illustrative scores in the 70s, and a five-line heatmap. Label it `Illustrative — not [Brand] data` on the slide and in the speaker note. The story reuses claim language; it adds no new claims or numbers.

## Phase 7 — Fill the file

Fill `output-template.md` top to bottom. Leave the "For Claude Design" note in place. List boilerplate screens by label only. Check every field against the lengths in `deck-structure.md`, especially the no-wrap fields (cover title line 2, product heading, current-claim pills). Then complete the presenter sheet.

## Non-negotiables

- 15 screens in the template's order, labels and field names exactly as in `output-template.md`; boilerplate screens listed by label only.
- Three territories (the third is the new one), four studies per spotlight, three key-finding cards, three or four claims.
- Every study real and tool-sourced; identifiers on the slide for blurring and in full on the presenter sheet.
- Sources masked, substance legible.
- Every number on screens 10, 11 and 12 traces to a spotlight row.
- Product name never in the same sentence as a category statistic.
- The worked example is labeled illustrative on the slide and in the note. No scores anywhere else. No prices anywhere.
- Screen 05 speaker note states plainly: public science and public claims only, no brand documents, no conversations with the team.
- No markup inside fields beyond the five marks in `output-template.md`.

## Definition of done

Report back in a few plain lines:

- 15 screens, labels and field order matching the template; boilerplate untouched.
- Every study has a real, tool-sourced identifier; all appear on the presenter sheet.
- Every finding reads with its citation blurred.
- Every field inside its length; no-wrap fields fit.
- Each spotlight speaker note names a real limitation.
- Claims: three or four, number-first with the product in its own sentence, each passing the copy-craft.md §12 self-edit, with a full record and an honest risk mix.
- Worked example labeled illustrative; its claims match screen 11.
- If the prospect is a Studio-featured brand or a direct competitor of one (Centrum, Cheers, Qunol, A+D, Nexium, Lotrimin), say so.
- Assumptions stated in one line; presenter sheet complete.
