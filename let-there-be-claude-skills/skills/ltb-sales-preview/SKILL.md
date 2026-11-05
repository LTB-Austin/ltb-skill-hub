---
name: ltb-sales-preview
description: Build a Science Intelligence preview deck for Let There Be. Point it at a prospect's product: it reads the brand's claims against a top competitor's to find the white space, runs a real Elicit pass, and develops several territories with their own hero claims. It then asks the person running it which hero claim to build out. The 13-screen deck covers the product, current claims versus the competitor, the preview scan, key themes, the hero claim, other ways to say it, the evidence (sources blurred, with an honest line) and an illustrative Science Story. Use whenever someone wants a pitch preview, prospect teaser, claims preview, what-could-they-claim deck, pre-engagement sales asset, conference walkthrough or leave-behind (including the Claims Lab), even if they just say "make a preview for [brand]." It builds the finished deck in the Sales Preview template in the same run, plus a presenter sheet. Do NOT use for a signed engagement (ltb-science-intelligence, ltb-lit-review-deck).
---

# LTB Sales Preview

## How this skill finishes: the deck, in one run

**Every run of this skill ends with a finished presentation built in the Sales Preview template (https://claude.ai/artifact/AtDJ3XjuJZhkDRPna9utYV, the One A Day® Teen Multi Gummy For Her build). Don't stop at the markdown.**

1. Do the work below, including the one question in Phase 4, and write `[brand]-sales-preview.md`. It's the working draft the deck is built from, not the deliverable.
2. As soon as the draft is complete, build the deck by following `references/template-build.md`. Use the template above for every screen. Don't wait for the user to ask for slides.
3. Finish by giving the user the deck link and the presenter sheet. Never tell them to take the file into Claude Design.

The Phase 4 territory choice is the only planned pause. Otherwise, pause only if an input the deck needs is missing.

## What this is

A **Science Intelligence™ preview** for a prospect. It shows a brand team, in 13 screens, what our process finds on their product:

- what they claim today against a top competitor;
- how we searched;
- what the science says;
- one territory built out the way a full engagement builds it: the hero claim, other ways to say it, and the evidence with an honest line;
- and how it becomes a Science Story.

It's presented live, at a pitch or a conference, and left behind as a PDF.

The research covers **several territories**, but the deck presents **one**. The person running the skill chooses which. The rest go on the presenter sheet as what the full engagement would run next.

**The template is the standard.** The One A Day® build sets the bar for which numbers we call out, how territories are named, how claims are shaped, and how the Science Story reads. `references/deck-structure.md` turns it into fields and lengths. Match it every time.

## Who is in the room

A prospect's brand team, and often their regulatory, medical or legal reviewers. Write so both groups are satisfied.

- **Use the precise regulatory term** in speaker notes and on the presenter sheet (structure/function, monograph, Drug Facts, MLR). Explain biology the first time it appears.
- **Name the weakness before they find it.** Every preview carries an honest line on the evidence screen. Speaker notes also name anything that has to stay out (disease language for the category) and compare the doses tested with the dose on the label.
- **Never let a claim outrun its category.** A supplement doesn't get a disease claim. A monograph OTC stays inside its monograph.

## Writing voice

- Plain and factual. Short, declarative sentences. Lead with the number, the finding, the design.
- No superlatives or buzzwords (best, revolutionary, unlock, breakthrough, powerful), no rhetorical hooks, no wordplay outside the brand-voice tagline. The prospect is judging whether we can write, not whether we can pitch.
- Headlines state the point, on one line.
- Use em dashes at most once per slide.
- Every page and every block of text has a job. Cut anything that doesn't.

`references/copy-craft.md` governs the claim lines (§1, §2, §3, §7, §11, §12) and "Where the line sits" (§8, §10, §11). For the Science Story layout, follow `deck-structure.md` screen 10, which replaces the older six-line format in copy-craft §9.

## Reference files

| File | Read it when |
|---|---|
| `references/deck-structure.md` | First. The 13 screens: their template slides, fields, lengths and speaker notes. |
| `references/competitor-scan.md` | Phase 2. How to pick the top competitor, capture both brands' claims, and find the white space. |
| `references/regulatory-scoping.md` | Before writing claims. Claim types, qualifiers, product fit and risk by regulatory class. |
| `references/copy-craft.md` | Before writing claims. Shared with ltb-science-intelligence, ltb-lit-review-deck and ltb-science-story; edit all four together. |
| `references/output-template.md` | When writing. The skeleton, plus the presenter sheet. |
| `references/template-build.md` | When building the deck. |
| `references/brand-system.md` | Only if design intent is needed. The template carries the look. |

## Inputs

The presenter gives a product, and ideally a sentence of angle. Infer the rest, state your assumptions in one line, and proceed:

- **Actives and labeled doses,** from Supplement Facts or Drug Facts.
- **Regulatory class and market.**
- **Brand owner.**
- **The line:** the other SKUs, for the closing ask.
- **A competitor,** only if the presenter names one. Otherwise you choose it in Phase 2.

## Phase 1 — Product

Pull the label: the audience, the format, the daily serving, every active with its dose, and the category. This fills screen 03. The doses matter later, when you compare them with the doses the studies used.

## Phase 2 — Current claims and the white space

Follow `references/competitor-scan.md`:

1. Capture the client's claims verbatim, with their sources and read dates.
2. Pick the one top competitor, and capture its claims the same way.
3. Sort the claims into three groups: what both claim, what one owns, and what neither says.

The "neither says" group is the open lane. It steers the territories.

## Phase 3 — Research and territories

Use the connected Elicit tools: `search_papers` (prioritize meta-analyses, systematic reviews and RCTs, recent and landmark) and `search_trials`. Load them with the tool search first and use the parameter names they return. Don't run `create_systematic_review`.

**Keep a scan log as you go.** Record every search run, every paper pulled and screened, every paper shortlisted (and why), and every study you end up using. Screen 05 shows these counts, and they must be real. If Elicit isn't connected or returns nothing usable, stop and say so. Never build a preview from recalled studies.

Every study must be real and tool-sourced, with a resolving PMID, DOI or NCT. For each one, capture: design, n, population, dose and form, comparator, primary endpoint, and whether you read the full text or only the abstract.

From the research, develop **three or four territories**. Each needs:

- a name of 2–4 words, in Title Case;
- a **draft hero claim**: the category number first, then the product's role in a second sentence;
- the best number behind it, with its study;
- its fit to the white space from Phase 2: open lane, deepens a shared claim, or echoes the competitor;
- its fit to the label: whether the product carries the active, and the label dose against the doses tested;
- its strongest counter-evidence;
- its risk: LOW, MEDIUM or HIGH.

Also draft the **four key themes** for screen 06 from the whole scan. They can run across territories.

## Phase 4 — Ask which hero claim to build

Show the person running the skill the shortlist and let them choose. Use the AskUserQuestion tool if it's available; otherwise ask in chat and wait for the answer.

- **Question:** "Which hero claim should I build out into the deck, with its other ways to say it, the evidence and the Science Story?"
- **One option per territory.** The label is the territory name. The description holds the draft hero claim, the best number and its study type, the white-space fit, the label fit, and the risk, kept short.
- **Recommend one.** Put your strongest first and add "(Recommended)" to its label: the best mix of evidence strength, open-lane fit and label fit.
- Let them choose another territory or edit the claim through the free-text answer. If they edit it, keep the substance traceable to its study.

If nobody is there to answer (a scheduled or unattended run), build the recommended territory and say so in the summary.

## Phase 5 — Build out the chosen territory

Read `references/regulatory-scoping.md` and copy-craft.md §2, §3, §7, §11, §12. Then write:

- **The hero claim** (screen 07) of ≤ 115 characters, plus who it speaks to, and why it matters to the brand (quoting their current claim where one exists).
- **Four other ways to say it** (screen 08), in this order: the product-fit line, the honest short version, the brand-voice tagline, the bolder line.
- **The evidence** (screen 09): one hero number, three study rows that build (the core trial, the population nuance, durability), and the honest line.

These rules apply to all of them:

- The category number never shares a sentence with the product name.
- Match the qualifier to the design. Never use "proven."
- Every factual line carries its substantiation. The brand-voice tagline carries none because it states no facts.

## Phase 6 — Science Story worked example

Build screen 10 from the chosen territory's claims:

- a story name of 2–4 words;
- four paragraphs: a setup, the science, the product, and the close;
- three illustrative dials between 65 and 85;
- the "Which words did the work" passage, with green, orange and red phrases, including at least one red word that real testing would catch.

Label it illustrative. Every factual sentence in the story must be one of the deck's claims. The setup paragraph is positioning copy and states no facts.

## Phase 7 — Fill the file and build

Fill `output-template.md` from top to bottom, including the presenter sheet: sources, the scan log, the competitor scan, the claim record, compliance logic, "Where the line sits," the other territories, and likely questions.

Check every field against the lengths in `deck-structure.md`, especially the one-line fields: the title, the territory name, the theme titles, the story title, and the closing line.

Then build the deck following `references/template-build.md`, mapping each screen to its template slide id. If the template won't open for the person running the skill, stop and tell them it isn't shared with them.

## Non-negotiables

- 13 screens in the order given in `deck-structure.md`, all built from the Sales Preview template.
- The person running the skill chooses the territory (Phase 4) unless the run is unattended.
- Competitor claims are verbatim and dated, from public sources only, and never called false or misleading.
- Every count on screen 05 comes from the scan log.
- Every study is real and tool-sourced. Identifiers are blurred on the slides and given in full on the presenter sheet.
- An honest line appears on screen 09, every time.
- The worked example is labeled illustrative. No scores appear anywhere else, and no prices appear anywhere.

## Definition of done

Report back in a few plain lines:

- The deck link, and the presenter sheet.
- The territory built, who chose it, and the other territories.
- The top competitor, and the open lane.
- The hero claim, with its risk.
- The scan counts.
- Confirmation that every study has a real, tool-sourced identifier.
- Any field that didn't fit its layout.
- Whether the prospect is a Studio-featured brand or a direct competitor of one (Centrum, Cheers, Qunol, A+D, Nexium, Lotrimin).
