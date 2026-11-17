---
name: ltb-general-presentation
description: "Build any Let There Be presentation no other LTB skill covers, in the LTB Template — General Presentation, so every deck has the Let There Be look. Use whenever someone wants a deck, slides, a presentation, pitch, talk, workshop, training, internal update, meeting or discussion guide, or a one-off client deck, even if they just say \"make a few slides on X\" or \"turn this into a deck\" and never mention a template. Writes the content, then builds the finished deck from the template's layouts and brand images in the same run. Never design an LTB deck from scratch. Do NOT use when a specific LTB skill covers the deck: Project Overview, Science Intelligence, Science Story, Sales Preview, Research Alignment Session, Success Story, Supplement Science Score, SOW, Activations or Science 101."
---

# LTB General Presentation

## How this skill finishes: the deck, in one run

**Every run ends with a finished presentation built in the LTB Template — General Presentation (https://claude.ai/artifact/CFZ5G3y4Su5DWCmFCXJh9y). Don't stop at the outline, and never design the deck from scratch.**

1. Write the content first, into `[topic]-presentation.md` in `/mnt/user-data/outputs/`: one entry per screen with the layout it uses, its fields and its speaker notes.
2. As soon as it's complete, build the deck by following `references/template-build.md`, using the General Presentation template for every slide. Do it in the same run. Don't ask whether to continue.
3. Give the user the deck link in one line, plus the open items: placeholders still to fill and any images to add.

A deck built any other way — a fresh Slides deck styled with the design system, its own stylesheet, its own logo size or its own layouts — doesn't look like Let There Be. The template carries the look: type sizes, the header rule, the corner logo and the mitosis cells. This skill only supplies the words and picks the layouts.

Pause before building only if the user asks for content only, or if you have nothing to build from. With a thin brief, write the deck anyway with bracketed placeholders (`[Client]`, `[00%]`) and list them in the hand-over. Never invent a statistic, a quote, a client name or a result.

## The layouts

The template has 23 slides. Pick one per screen, use a layout as often as the content needs, and leave out the rest.

| Layout (slide id) | Use it for |
|---|---|
| `cover` | Title, subtitle, date. Always first. |
| `agenda` | Up to four numbered parts with one line each. |
| `divider` | The start of a section in a deck of more than about eight slides. |
| `statement` | One line the room should remember. |
| `text` | A headline and a short paragraph. |
| `bullets` | Three to five points, one idea each. |
| `two-column` | An explanation beside an image or a supporting block. |
| `split-image` | A short argument beside a photo that fills half the slide. |
| `three-cards` | Three parallel ideas of the same shape. |
| `grid-four` | Four parallel points. |
| `compare` | Two options side by side. |
| `process` | Steps in order, with who does what. |
| `timeline` | Dated milestones. |
| `stats` | Two to four numbers, each with what it measures and its source. |
| `big-stat` | One number that carries the slide. |
| `chart` | A simple bar chart with a takeaway. |
| `table` | Rows compared on the same criteria. |
| `quote` | A verbatim quote with name and role. |
| `image-full` | A full-bleed image with a caption. |
| `image-grid` | Three or four images with captions. |
| `team` | Who's in the room, LTB and client. |
| `next-steps` | Actions with owners and dates. |
| `closing` | Always last: **Science leads.** / **Creativity amplifies.** on two lines, exactly as the template has it. |

## Writing the screens

- **Every slide and every block earns its place.** One job per slide. Cut a slide or a line that doesn't move the story.
- **Headlines stay on one line.** Shorten the words; never let one wrap. The closing line is the only two-line headline.
- **Plain, declarative sentences.** Lead with the fact, the number or the decision. No hype.
- **Ration the cards.** Use `three-cards` and `grid-four` only when the points are truly parallel. Most content reads better as `bullets`, `two-column`, `process`, `stats` or `text`. A deck of boxes everywhere is not the Let There Be look.
- **Vary the rhythm.** Don't run the same layout more than three times in a row unless the content is a true series.
- **Speaker notes** say what the presenter says, in a few sentences, for every slide.

## Keep the look intact

These come with the template's slides. Keep them exactly as they are; template-build.md rule 2 covers the mechanics.

- The mitosis cells stay where the template puts them. Never add, move or resize one, and never let two overlap or sit near each other.
- The Let There Be logo stays in the bottom-right corner. A phase wordmark (Science Intelligence™, Science Story™, Science Studio™) goes in the bottom-left corner, across from it, never in the header.
- In a two-part layout (an explanation beside a list, panel, image or photo), the shorter column is centered vertically against the longer one. Columns of parallel items stay top-aligned so their labels line up.
- Nothing is placed off the slide. People edit these decks and move content around, and anything with a negative position gets pulled back onto the slide and breaks the layout.
- Brand images are design system paths (`project/ds/lettherebedesignsystem_9f5f72/assets/…`); copy them as template-build.md step 3 says. Photos and client images go in the empty image frames: upload the user's file if they gave you one, otherwise leave the frame empty and list it.

## When another skill fits

If the request turns out to be one a specific LTB skill covers (a SOW, a Project Overview, a sales preview, a Science Story, and so on), use that skill instead. This one is for everything else.
