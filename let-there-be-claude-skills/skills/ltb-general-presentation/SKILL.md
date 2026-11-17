---
name: ltb-general-presentation
description: "Build any Let There Be presentation that no other LTB skill covers, in the LTB Template — General Presentation. Use whenever someone at LTB wants a deck, slides, a presentation, a pitch, a recap, an internal briefing, a training deck, a capabilities or credentials deck, a conference talk or a meeting deck, even if they just say \"make a deck about [topic]\" or \"turn this into slides.\" It works out the story first, picks the template's layouts slide by slide, writes the copy in LTB's plain voice, and builds the finished deck in the same run. Do NOT use when a specific LTB skill fits: Project Overview, SOW, Sales Preview, Research Alignment Session, Science Intelligence deck (ltb-lit-review-deck), Science Story, Science 101, Activations, Success Story, Supplement Science Score or Script Feedback."
---

# LTB General Presentation

## How this skill finishes: the deck, in one run

**Every run of this skill ends with a finished presentation built in the LTB Template — General Presentation (https://claude.ai/artifact/CFZ5G3y4Su5DWCmFCXJh9y). Don't stop at an outline or a markdown file.**

1. Work out the story and write the content draft (`[topic]-deck.md`) in your working folder, filled into `references/output-template.md`. It's the working draft, not a deliverable, so don't save it to the outputs folder.
2. As soon as the draft is complete, build the deck by following `references/template-build.md`. Pick each slide's layout from `references/layout-library.md`. Do this in the same run. Don't ask whether to continue, and don't wait for the user to ask for slides.
3. Finish by giving the user the deck link.

Pause before building only if the topic or audience is too unclear to write a single headline, or the user asks for an outline only.

## When to use this skill, and when not to

This is LTB's **default for every presentation that isn't covered by another LTB skill or template**: internal decks, capability and credentials decks, conference talks, recaps, trainings, proposals that aren't SOWs, and anything else.

If the request matches one of these, use that skill instead:

| The request is for… | Use |
|---|---|
| A project kickoff or project overview | ltb-project-overview |
| A Statement of Work, scope or investment deck | ltb-sow |
| A prospect preview, pitch preview or Claims Lab | ltb-sales-preview |
| A research kickoff or alignment session | ltb-research-alignment-session |
| A Science Intelligence, lit review or claim dev deck | ltb-lit-review-deck |
| A Science Story or claim clusters | ltb-science-story |
| A Science 101 briefing for the creative team | ltb-science-101 |
| Activation examples | ltb-activations |
| A client case study or success story | ltb-success-story |
| A SuppCo or LLM visibility read | ltb-supplement-science-score |
| A walkthrough of script edits | ltb-script-feedback-presentation |

If the user names one of these decks but there's no material for it yet, say which skill it belongs to and what it needs. Don't fall back to this skill for it.

## Writing voice

- Plain and factual. Lead with the point, then the proof. Short, declarative sentences.
- Be specific: name the number, the client, the product, the date, the owner.
- No superlatives or buzzwords (best, revolutionary, unlock, breakthrough, game-changing, powerful), no rhetorical-question hooks, no puns.
- Write for smart, busy marketers, not scientists. Define a technical term the first time it appears.
- Use em dashes at most once per slide.
- Call LTB's mechanism and science video work "videos," never "films."
- Say it once. Every slide and every block of text has a job; cut anything that doesn't.

## Inputs

Work from what the user gives you: a topic, notes, a doc, a transcript, data or an old deck. Before writing, settle three things, inferring them from the material where you can and asking only if you can't:

- **Audience:** a client, a prospect, the LTB team, or a conference room.
- **The one thing they should leave with:** this becomes the spine of the deck.
- **Length:** default to 8–12 slides. A deck longer than 15 needs a reason.

Pull facts from the project space and connected drives before asking for them. Never invent a number, a quote, a client result or a date. If something is missing, mark it `[NEEDED: …]` on the slide and list it in your handback.

## How to build

1. **Write the spine.** One sentence on what the audience should leave believing. Then write the headline of every slide as a one-line statement. Read the headlines alone, top to bottom: they should tell the whole story. If they don't, fix the order before writing anything else.
2. **Pick a layout per slide** from `references/layout-library.md`. Choose by the shape of the content (one statement, a comparison, a sequence, a number, a quote), not by habit. Don't repeat the same layout three slides in a row.
3. **Write each slide** into `references/output-template.md`: eyebrow, headline, body fields and speaker notes. Keep inside the lengths in the layout library.
4. **Check the draft** against `references/design-rules.md` before building.
5. **Build the deck** following `references/template-build.md`. Use only the layouts you picked, and duplicate a layout under a new slide id when you need it twice.
6. **Hand back** the deck link, plus any `[NEEDED]` items and any slide where you used a layout other than the one planned.

## Reference files

| File | Read it when |
|---|---|
| `references/layout-library.md` | Planning slides. Every layout in the General Presentation template: what it's for, its fields and lengths, and when not to use it. |
| `references/design-rules.md` | Before building. LTB's deck rules: headlines, tiles, mitosis shapes, logos, columns, gradients, editability. |
| `references/output-template.md` | Writing the draft. The slide-by-slide skeleton. |
| `references/template-build.md` | Building the deck. Shared with every LTB deck skill. |

## Revisions

People edit these decks directly. Before any change, re-read the slide files you'll touch and keep their edits: changed headlines, deleted slides, reworded lines. Change only what was asked, and make the same change in the draft so the two stay in step.
