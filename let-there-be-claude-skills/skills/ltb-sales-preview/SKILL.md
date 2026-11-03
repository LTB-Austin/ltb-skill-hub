---
name: ltb-sales-preview
description: Build a Science Intelligence preview deck for Let There Be. Point it at a prospect's product: it runs a real Elicit pass, picks the one direction the evidence supports best, and runs it the way a full engagement does. A hero claim, two supporting claims and the evidence share one slide with sources blurred, compliance logic follows on the next, and an illustrative Science Story worked example closes it. Use whenever someone wants a pitch preview, prospect teaser, claims preview, what-could-they-claim deck, pre-engagement sales asset, conference walkthrough or leave-behind (including the Claims Lab), even if they just say "make a preview for [brand]." It builds the finished 10-screen deck in the LTB Sales Preview template in the same run and adds a presenter sheet with citations, product fit, risk and runner-up directions. Do NOT use for a signed engagement (ltb-science-intelligence, ltb-lit-review-deck) or for real Science Story claim clusters.
---

# LTB Sales Preview

## How this skill finishes: the deck, in one run

**Every run of this skill ends with a finished presentation. Don't stop at the markdown.**

1. Do the work below and write `[brand]-sales-preview.md`. It's the working draft the deck is built from, not a deliverable in its own right.
2. As soon as the draft is complete, build the deck by following `references/template-build.md` and the two-template steps in "Building the deck" below. Do this in the same run. Don't ask whether to continue, and don't wait for the user to ask for slides.
3. Finish by giving the user the deck link and the presenter sheet. Never tell them to take the file into Claude Design, and never suggest they ask for a slide deck.

Pause before building the deck only if an input the deck needs is missing, or the user asks for content only.

## What this is

A **Science Intelligence™ preview** for a prospect. It takes one product and one real pass through the public science, and shows the prospect **how our process works** by running a single direction end to end: the claim, the other ways to say it, the evidence behind it, and the compliance logic that gets it through MLR. It's presented live to a brand team, at a pitch or a conference, and left behind as a PDF.

The preview is deliberately small. Instead of many claims, it gives one direction done properly. The runner-up directions go on the presenter sheet as "what the full engagement would run next."

Read `references/deck-structure.md` first, then fill `references/output-template.md` screen by screen.

## Who is in the room

A prospect's brand team, and often their regulatory, medical or legal reviewers. Write so both groups are satisfied: claims a marketer wants to use, scoped tightly enough that a reviewer would take them to MLR.

- **Use the precise regulatory term** in speaker notes, the compliance tiles and the presenter sheet (structure/function, monograph, Drug Facts, MLR, competent and reliable evidence). Explain biology the first time it appears.
- **Name the weakness before they find it.** In vitro only, a small panel, self-report, a dose above the label, a population that doesn't match the buyer. It goes in the honest-line tile and the speaker note.
- **Never let a claim outrun its category.** A supplement doesn't get a disease claim. A monograph OTC stays inside its monograph.
- **Claim lines stay consumer-facing.** The substantiation behind them is written for the reviewer.

## Writing voice — plain and factual

- Lead with the fact. Use short, declarative sentences. Be specific: name the active, the finding, the number, the design.
- No salesmanship: no superlatives or buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), no rhetorical hooks, no wordplay. The prospect is judging whether we can write, not whether we can pitch.
- Headlines state the point, on one line.
- Use em dashes at most once per slide, and only when a comma or period won't do.
- Say it once.

`references/copy-craft.md` governs the claim lines (§1, §2, §3, §7, §11, §12), the worked example (§9), and "Where the line sits" (§8, §10, §11).

## Reference files

| File | Read it when |
|---|---|
| `references/deck-structure.md` | First. The 10 screens: which template slide each comes from, its fields and lengths, and source masking. |
| `references/output-template.md` | When writing. The skeleton the file is filled into, plus the presenter sheet. |
| `references/regulatory-scoping.md` | Before writing claims. Claim types, qualifiers, product fit and risk by regulatory class. |
| `references/copy-craft.md` | Before writing claims and the worked example. Shared with ltb-science-intelligence, ltb-lit-review-deck and ltb-science-story; edit all four together. |
| `references/template-build.md` | When building the deck. |
| `references/brand-system.md` | Only if design intent is needed. The templates already carry the look. |

## Inputs

The presenter gives a product, and ideally a sentence of angle ("the site says 'blends in' but never says why that matters"). Infer the rest, state your assumptions in one line, and proceed:

- **Actives and labeled dose or form,** from Drug Facts or Supplement Facts. The fit tile depends on them.
- **Regulatory class and market:** US OTC monograph, US dietary supplement, cosmetic, UK P/GSL medicine, device, and so on.
- **Brand owner,** for the closing ask and the MLR language.
- **The lineup:** the other SKUs in the range, their actives and what they claim.
- **Current claims,** verbatim from the brand's public site or pack.

Don't interrogate the presenter.

## Phase 1 — Research

Use the connected Elicit tools: `search_papers` (prioritize meta-analyses, systematic reviews and RCTs, recent and landmark) and `search_trials`. Load them with the tool search first and use the parameter names they return. Don't run `create_systematic_review`. That depth is the paid engagement.

Search across **two or three candidate directions** so the choice in Phase 3 is real. Read **six to ten studies** in total.

If Elicit isn't connected or returns nothing usable, stop and say so. A preview built from recalled studies is worse than no preview. The presenter will be asked for identifiers, and an invented PMID in front of a prospect is the one thing this skill can never produce.

Every study must be real and tool-sourced, with a resolving PMID, DOI or NCT. Identifiers are blurred on the slide but must be correct, and they go in full on the presenter sheet. For each study, capture what a reviewer will ask: design, n, population, dose and form, comparator, primary endpoint, blinding, whether it matches the product's labeled dose, and whether you read the full text or only the abstract.

## Phase 2 — Product context

Pull the current claims verbatim and list the actives as Drug Facts or Supplement Facts names them. Map the lineup: each SKU's actives and its job on the shelf. Then find this SKU's job, and the open lane: what the evidence supports that nobody on the shelf is saying. None of this gets its own slide. It goes in the speaker notes and on the presenter sheet, and it decides the direction.

## Phase 3 — Pick the one direction

Choose the direction with the best combination of three things: the strength of its evidence (design, fit to the label), its value to this brand (a lane they can own, or a claim they already make that the science can deepen), and how clearly it demonstrates our process (a hero number, a real compliance question).

Give it a 2–6 word name of ≤ 40 characters, and a two- or three-letter ID prefix (e.g. `CG` for a carrageenan direction). Put the two runner-ups on the presenter sheet, with why each lost.

## Phase 4 — The claims

Read `references/regulatory-scoping.md` and copy-craft.md §2, §3, §7, §11, §12. Write:

- **One hero claim** of ≤ 110 characters (`[ID]1`), with who it speaks to.
- **Two supporting claims** of ≤ 90 characters each (`[ID]2`, `[ID]3`). Each one is another way to say the hero claim, in a different register: number-forward, short, the brand's own voice, names a competitor (only where the competitor's label supports it), or bolder · brand's call.

Then apply these to all three:

- Give each a **tier**: Core, Push or Stretch, using the definitions on screen 04.
- **Lead with the number or finding, then let the product arrive in its own sentence.** A category statistic never shares a sentence with the product name.
- Match the qualifier to the study design. "Clinically shown" goes only on a human RCT for that endpoint at the product's dose and form. Never use "proven."
- Name comparators by molecule. Name a brand only on a Push or Stretch line, and only when its label supports it.
- Check the curly quotes, plural agreement, and the registered mark on the brand every time.

Use an honest mix of tiers and risk. A preview where everything is Core and LOW reads as timid or unexamined.

## Phase 5 — Evidence and compliance

**Evidence (screen 05):**
- one hero number, from a study you read, with its meaning in one sentence;
- two study cards, each a finding, a design line, and a blurred journal and year.

**Compliance (screen 06):** six tiles in the order given in `deck-structure.md`:
1. where the number comes from
2. fit to this product
3. the honest line
4. what the study found versus the bigger words to avoid
5. the category line
6. what's still open before MLR

Then add the risk line for each claim ID, and the depth line.

## Phase 6 — Where the line sits (presenter sheet)

Choose the claim with the most regulatory tension and write it three ways (copy-craft.md §8, §10, §11):

- **Too far**, plus the one reason it fails;
- **Where it lands**, which is the line on screen 05;
- **Left on the table**, the timid version.

Add the question to put to the room. This is Q&A material, not a slide.

## Phase 7 — Science Story worked example

Read copy-craft.md §9. Build screen 07 from the three claims:

- a story name;
- two short story paragraphs;
- three cluster pills;
- three illustrative scores between 65 and 85;
- the "which words did the work" highlights.

Label it `Illustrative — not [Brand] data` on the slide and in the speaker note. The story reuses claim language and adds no new claims or numbers.

## Phase 8 — Fill the file

Fill `output-template.md` from top to bottom. List boilerplate screens by label only. Check every field against the lengths in `deck-structure.md`, especially the one-line fields: the cover title, the direction name and the headlines. Then complete the presenter sheet.

## Building the deck

Follow `references/template-build.md`, with these changes for this skill, which builds from **two** templates:

1. **Create the deck** with the title "[Brand] — Sales Preview".
2. **Read both templates' slides.** From the **LTB Template — Sales Preview (Science Marketing Engine)** (https://claude.ai/artifact/VEB4pUCzcLnEPc1EXy6Hjk), read `s01`, `s02`, `s03`, `s11`, `s12`, `s13` and `s14`. From the **LTB Template — Science Intelligence (Lit Review + Claim Dev)** (https://claude.ai/artifact/3eLTXv8dToy1DrofTGXhxk), read `s06`, `s08`, `s09`, `s10` and `s11`.
3. **Copy the assets from both templates** (`from_url` once per template, up to 10 asset ids per call). Then replace every `/_blob/` url in the slides with the new deck's urls. Both templates use the same Let There Be design system, so copy the tokens from the Sales Preview template.
4. **Build the 10 slides** in the order given in `deck-structure.md`. Screen 05 is a new slide assembled from SI `s08`, `s09` and `s10` elements, using the layout described there. Screens 04–06 also get the Sales Preview template's footer and page number.
5. Everything else follows the template-build rules. Never edit either template, nothing from a past client carries over, and headlines stay on one line.

If either template won't open for the person running the skill, stop and say which template isn't shared with them.

## Non-negotiables

- 10 screens in the order given in `deck-structure.md`.
- One direction, one hero claim, two supporting claims, two study cards, six compliance tiles, one worked example.
- Every study is real and tool-sourced. Identifiers are blurred on the slide and given in full on the presenter sheet.
- Sources are masked, but the substance stays legible.
- Every number on screens 05–07 traces to a study you read.
- The product name never shares a sentence with a category statistic.
- The worked example is labeled illustrative. No scores appear anywhere else, and no prices appear anywhere.
- The screen 03 speaker note says plainly: public science and public claims only, no brand documents, no conversations with the team.

## Definition of done

Report back in a few plain lines:

- The deck link, and the presenter sheet.
- The direction you chose, and the two runner-ups.
- The hero claim, with its tier and risk.
- Confirmation that every study has a real, tool-sourced identifier.
- Any field that didn't fit its layout, and what you did about it.
- Whether the prospect is a Studio-featured brand or a direct competitor of one (Centrum, Cheers, Qunol, A+D, Nexium, Lotrimin).
- Your assumptions, in one line.
