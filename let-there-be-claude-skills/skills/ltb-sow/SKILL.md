---
name: ltb-sow
description: Build the Statement of Work (SOW) deck for Let There Be. Use when creating or refining a SOW, proposal deck, scope or investment deck for any LTB client, even if the user just says "write the SOW for [client]" or "turn this pricing into a SOW." Reads the CRM or relationship notes and the pricing and services file. It picks the deck shape: a full Science Marketing Engine program (Science Intelligence™ → Science Story™ → Science Studio™), a Science Studio™ content program, or a single-phase scope. It writes every screen with speaker notes, using only the deliverables and prices in the pricing input and LTB's standard terms verbatim. It writes the content first, then builds the finished deck in the LTB Statement of Work template in the same run. Do NOT use for the Project Overview (ltb-project-overview), a sales preview (ltb-sales-preview) or a Success Story (ltb-success-story).
---

# LTB Statement of Work (SOW)

## How this skill finishes: the deck, in one run

**Every run of this skill ends with a finished presentation built in the LTB Template — Statement of Work (https://claude.ai/artifact/BU1JncBj1WwhzcCeNQumJr). Don't stop at the markdown.**

1. Do the work below and write `[brand]-sow.md`. That's the working draft the deck is built from. It isn't the deliverable on its own.
2. As soon as it's complete, build the deck in the template by following `references/template-build.md`. Do this in the same run. Don't ask whether to continue, and don't wait for the user to ask for slides.
3. Finish by giving the user the deck link. Never tell them to take the file into Claude Design, and never suggest they ask for a slide deck.

Wherever this skill mentions Claude Design, a design template, an "unbranded" or "content-first" output, or a markdown brief, it means the content draft that feeds this build step. Every rule about content still applies in full: what goes on each screen, exact wording, and gap markers.

Pause before building the deck only in three cases: the skill below requires an approval first, an input the deck needs is missing, or the user asks for content only.

The SOW is the deck a client signs against. It covers what the brand's problem is, what we will make, how we work, what it costs, and what happens next. The current reference builds are **iVIZIA® Micellar Eyelid Cleansing Wipes** (Théa, full engine program, September 2026) and the **Thorne Gut Health Education Series** (Science Studio™ program, September 2026). Match their tone, depth and screen order.

## Output

> The finished deck, built in the LTB Template — Statement of Work (see the top of this skill). First write `[brand]-sow.md` in `/mnt/user-data/outputs/`, filled into `references/output-template.md`. It holds every screen in order, each with an eyebrow, headline, body fields and **speaker notes**. Mark manual assets as placeholders. Don't add styling, HTML or an export. The LTB Template — Statement of Work carries the look (Lexend, `#F0F0F0`, cell imagery, sub-brand marks, LTB wordmark). The markdown carries the words.

## Writing voice

- Plain and factual. Lead with the fact and let the scope and the evidence carry the weight. No hype or hard sell.
- Use short declarative sentences, written for a smart marketer who isn't a scientist. Define a technical term the first time it appears, or replace it.
- Be specific: name the product, the asset length, the dimension, the audience, the number.
- Avoid superlatives and buzzwords (best, revolutionary, unlock, breakthrough, powerful), rhetorical questions, puns and taglines written for effect.
- **Headlines state the point on one line.** If one won't fit, shorten it.
- Use em dashes sparingly: at most one per screen.
- Say each thing once. Leave out throat-clearing and filler qualifiers.

## Inputs (Phase 0)

Confirm you have these. Ask only for what's missing.

- [ ] **CRM summary or relationship notes.** These drive The Challenge, The Bigger Picture and the speaker notes.
- [ ] **Pricing and services file.** This is the only source for deliverables, specs, prices, discount, contingency and payment terms.
- [ ] Client company and brand/product names, written exactly as the client writes them (®, ™, accents: Théa).
- [ ] The program name or label (e.g. "E-commerce program," "Gut Health Education Series").
- [ ] The SOW month, plus the kickoff month or date.
- [ ] Channel focus: Amazon or other retailers? This decides whether the retailer rejections term is included.
- [ ] Any preview work already shared (a sales preview or Claims Lab). If there is some, its territories can appear on the Lit Review screen.
- [ ] Open selections the client still owes (e.g. "Product A to be selected by Thorne").

## Pick the deck shape

Read the pricing input, then choose one shape. `references/deck-structure.md` has the full screen order for each.

| Shape | When | Reference build |
|---|---|---|
| **A. Engine program** | Scope runs through two or three engine phases, with at least one of Science Intelligence™ or Science Story™ | iVIZIA Wipes (18 screens) |
| **B. Studio program** | Scope is content production only: videos, ads, education assets, often across several programs or products | Thorne Gut Health (16 screens) |
| **C. Single-phase** | Science Intelligence™ only, or Science Story™ only | Shape A with the absent phases removed |

## Hard rules

1. **Deliverables come from the pricing input only.** Don't add, assume or carry over deliverables from past SOWs, even ones that seem to fit. `references/deliverable-library.md` supplies description language for what *is* in scope. It is not a menu.
2. **Never invent prices, specs, dates, discounts, contingency amounts or payment terms.** If the pricing input doesn't give one, write `[NEEDED: …]` and list it in your summary.
3. **Use the standard terms verbatim.** Copyright & Usage, Milestone Approach, Retailer Rejections, Working Together and the Closing line come from `references/boilerplate.md`. Don't paraphrase them. Fill only the slots each block marks, such as the milestone example and the client name.
4. **Mark timelines as tentative.** Every timeline says final dates are set at kickoff and depend on the client's review and MLR timing.
5. **Show open items openly.** When the client still has a choice to make (a product, a dimension, a direction), say so on the screen ("Product A: one Thorne product, to be selected by Thorne") and add it to Next Steps.
6. **Preview findings are labeled as preview.** If you show the preview's directions, add the line "Preview findings from [n] papers, no brand input. Directional until the full review and MLR."
7. **Apply client-facing restraint.** Don't name internal tools, other clients, internal strategy or anything from the CRM notes that isn't meant for the client. The CRM notes inform the framing. They aren't quoted.
8. **Placeholders, not assets.** Client logos, packshots, product photography and example visuals are inserted by hand. Leave a labeled slot such as `[Insert client logo]`, `[Insert packshot]` or `[Example carousel frames — insert manually]`.

## How to build

1. **Map the scope.** List every line item from the pricing input with its phase, specs and price. Every deliverable screen and every Investment line traces back to this list.
2. **Write The Challenge from the CRM notes.** Give the brand's real problem in its commercial terms: the gap in consumer understanding, plus what it costs the brand (conversion, ROAS, shelf, retail). End with one plain sentence stating the challenge.
3. **Add The Bigger Picture (Shape A, optional)** when the program is one lever in a larger client strategy, for example HCP effort plus e-commerce conversion leading to retail distribution. Use three numbered columns and a one-line close.
4. **Write the engine or program overview.** Shape A gets the three phases (The Proof / The Persuasion / The Production). Shape B gets "One program, [n] uses," with the audiences and uses.
5. **Write the deliverable screens** from `references/deliverable-library.md`, customized to this brand's mechanism, product and channel. Add specs from the pricing input. Whenever Science Intelligence™ is in scope, add screen 06b, **What each direction looks like**. It shows the same four-part format the client saw in the Sales Preview and will get in the Science Intelligence deck: hero claim, supporting claims, evidence and compliance logic (see "One format, preview to SOW to delivery" in `deliverable-library.md`).
6. **Explain how the assets work together** (Shape A, Above the Fold) or summarize the deliverables (Shape B: assets × files).
7. **Write the process screens.** Shape A gets the Timeline. Shape B gets the Visual Approach, MLR Checkpoints and Timeline.
8. **Add the standard terms** from `references/boilerplate.md`, in the form the shape uses.
9. **Build the Investment screen** from the pricing input only (see `deck-structure.md` for both layouts).
10. **Add Next Steps and the Closing screen.**
11. **Write speaker notes for every screen.** In two to five plain sentences, say what the presenter says, including the reasoning that's on the slide only in short form. The notes may give context the slide leaves out, but they never contradict it.

## Revisions

Update every affected screen after each change, not only the one named. After each round, summarize what changed, on which screen, and whether the change was global or local.

## Reference files

| File | Read when |
|---|---|
| `references/deck-structure.md` | First. Screen-by-screen order, fields and lengths for Shapes A, B and C. |
| `references/deliverable-library.md` | Writing deliverable screens. Standard description language and specs for every LTB deliverable. |
| `references/boilerplate.md` | Writing the terms, Working Together, Next Steps and Closing screens. Verbatim text. |
| `references/output-template.md` | Writing the file. The skeleton, including the note to Claude Design. |

## Building from two templates

When screen 06b is in the deck, build it from the **LTB Template — Science Intelligence (Lit Review + Claim Dev)** (https://claude.ai/artifact/3eLTXv8dToy1DrofTGXhxk), slide `s06-how-each-direction-runs`. Read that slide, copy its assets into the new deck (with `from_url` set to that template), and add the SOW template's footer and page number to it. Every other screen comes from the SOW template. Both templates use the same Let There Be design system. If the Science Intelligence template won't open for the person running the skill, say so and stop.
