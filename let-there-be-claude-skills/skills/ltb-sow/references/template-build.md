# Building the deck in its LTB template

Read this once the skill's content file is complete. Each LTB template is a **Slides artifact**. Its slides are already designed, with bracketed placeholder fields (`[Product or program name]`), brand images and speaker notes. You build every client deck as a **new copy** of its template, then fill in the copy.

The content file stays the source of truth: the deck carries its words exactly as written. This step adds no copy, cuts no copy and doesn't rewrite any.

## The templates

| Deck | Template | Link |
|---|---|---|
| Project Overview | LTB Template — Project Overview | https://claude.ai/artifact/RxePUEHUnJNjtzUkSGwafb |
| Science Intelligence (Lit Review + Claim Dev) | LTB Template — Science Intelligence (Lit Review + Claim Dev) | https://claude.ai/artifact/3eLTXv8dToy1DrofTGXhxk |
| Science Story & Claim Clusters | LTB Template — Science Story & Claim Clusters | https://claude.ai/artifact/Qm7HgGxbT7os4Lz8jD2cqY |
| Sales Preview | Sales Preview template (One A Day® Teen Multi Gummy For Her build) | https://claude.ai/artifact/AtDJ3XjuJZhkDRPna9utYV |
| Research Alignment Session | LTB Template — Research Alignment Session | https://claude.ai/artifact/SqGzTEiEQWDJjRzDjFBHeV |
| Client Success Story | LTB Template — Client Success Story | https://claude.ai/artifact/Ax4uiPqesE1nUgsvo1P7pf |
| Supplement Science Score | LTB Template — Supplement Science Score | https://claude.ai/artifact/3UTxLhVcehMyFmSNbrKB64 |
| Statement of Work | LTB Template — Statement of Work | https://claude.ai/artifact/BU1JncBj1WwhzcCeNQumJr |
| Science Story Activations | LTB Template — Science Story Activations | https://claude.ai/artifact/9Ek9qbNGoTFun1g5cjK2W4 |
| Science 101 | LTB Template — Science 101 | https://claude.ai/artifact/TL7CM6pzzY87nXfkL8Rm4b |
| Anything else | LTB Template — General Presentation | https://claude.ai/artifact/CFZ5G3y4Su5DWCmFCXJh9y |

## Rules

1. **Never write to a template.** Never publish to a template's link. Every build goes to a new deck.
2. **Keep the design.** Keep each slide's markup, inline styles, image positions, cell imagery and logos as they are. Change only the text inside placeholder fields and the `<aside>` speaker notes.
3. **Use the content file's words exactly.** If a field in the content file is `[NEEDED: …]` or `[Insert …]`, leave that text visible on the slide so it's easy to spot.
4. **Keep headlines on one line.** If a headline doesn't fit its box, tell the user and offer a shorter version. Don't shrink or restyle it yourself.
5. **Nothing from a past client carries over.** Some templates hold a real past build instead of brackets (the Supplement Science Score template is the Centrum deck). Treat every word, number, chart value, product name and image of client content on those slides as a placeholder, and replace or remove it.
6. **Leave image slots alone unless you have the image.** An image slot with no `src` stays empty for manual insertion. If the user gave you the image file, upload it to the new deck and set its `src`.

## If the template won't open

Each template is a private artifact. The person running the skill can only copy it if the template has been shared with them. If reading the template fails, stop and tell them exactly that: "The [template name] template isn't shared with you. Ask Austin to share it, then run this again." Don't quietly fall back to a markdown file or to a deck you design yourself. Keep the content file in the outputs so the build can resume once access is granted.

## Steps

**1. Create the deck.** Start right away, without asking first. Publish with the Slides type (`type_url`: https://claude.ai/artifact/8jTsAFQMFDb2oA8MsPJ2eL), `title` "[Brand] — [Deck name]" (for example "iVIZIA Wipes — Statement of Work"), and `auto_open: "after_first_write"`, with no files. Use the reply's `url` for every call after this. That deck's type instructions come back with the reply, and they cover the file format and publishing. Follow them along with these steps.

**2. Read the template.** In one call, read the template's `project/deck.json` and every `project/slides/*.html` its `order` lists (the `read` action, the template link and `paths`). Then list the template's assets (`list`, `scope: "assets"`).

**3. Copy the brand images into the new deck.** Publish with `url` set to the new deck, `asset: true`, `from_url` set to the template link, and `asset_ids` set to the template's asset ids, up to 10 per call. Each reply gives a new url for every asset. In every slide you write, replace each `/_blob/<old id>` with its new url exactly as given.

**4. Map content to slides.** For each screen in the content file, pick the template slide built for it. The slide ids and the template's `sections` name them (`s02-the-challenge`, `s19-investment`).
- **Unused slides:** leave out template slides the content doesn't use, such as the Studio slides in a Science Intelligence-only SOW.
- **Repeated screens:** for one deliverable per screen or one storyline per program, copy the slide under a new id with a suffix (`s11-storyline-2`).
- **No matching slide:** pick the closest layout and tell the user which one you used.

**5. Write the index.** Write the new `project/deck.json`:
- `title`: the deck's name.
- `createdOnFiles`: `{"v":1,"at":"<now>"}`.
- `lists`: `"css"`.
- `cover`: the cover slide's id.
- `order`: the slides you used, in the content file's order.
- `sections`: the template's sections, updated to start at slides that exist.
- `faces`: copied from the template.
- `designSystems`: the template's Let There Be design system record. Confirm its address with the Artifact tool's `list` action, `type: "Design System"`.

In the same publish, copy the design tokens from the template: `"project/ds/<folder>/tokens.json": {"artifact": "<template link>", "path": "project/ds/<folder>/tokens.json"}`, where `<folder>` is the record's `namespace`.

**6. Fill the slides.** Write each slide file with the template's markup, the content file's text in place of the bracketed fields, the new asset urls, and the content file's speaker notes in the `<aside>`.
- Publish the index and the cover slide together first.
- Then publish three slides per call, in order.

**7. Hand it over.** Give the user the deck's link in one line, plus anything that didn't fit or that you placed in a different layout. Keep the content file (`.md`) in the outputs as the source.

Don't re-read, render or screenshot the deck to check it unless the user asks.

## Revisions

Change the client deck, never the template. For a wording change, update the content file first, then make the same change in the deck's slide. Both should stay in agreement.
