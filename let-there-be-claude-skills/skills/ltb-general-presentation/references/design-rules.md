# LTB deck design rules

The template already carries the Let There Be design system: Lexend, `#f0f0f0` backgrounds, the brand gradients, the mitosis shapes and the logos. These rules cover what the build step can still get wrong. Check every slide against them before publishing.

## Headlines
- **One line, always.** If a headline wraps, shorten the words, or step the size down within the template's scale. The one exception is "Science leads. / Creativity amplifies.", which is always split onto two lines.
- **The rule under a headline is a solid black line,** never a gradient.
- **Eyebrows stay grey,** never colored.

## Layout
- **No boxed tiles for everything.** Prefer two columns separated by a hairline, ruled rows, tables, or open grids. Use tiles only when three or four parallel items truly need them.
- **Center the shorter column.** When two columns hold different amounts of content, center the shorter one vertically against the longer. Columns of parallel items (four steps, three options) stay top-aligned.
- **Keys and legends live inside the graphic** they explain, not beside it.
- **Every slide and every text block has a job.** If a block only repeats the headline, cut it.

## Color and emphasis
- Emphasis comes from the **brand gradients**, used sparingly: one gradient element per slide at most. Never use flat accent colors for emphasis.
- Body text is black or the template's greys. It's never colored.

## Mitosis shapes and logos
- **Mitosis shapes sit in the margins.** They never overlap each other or sit near each other, and they never sit behind text.
- **The Let There Be logo** stays where the template puts it.
- **Accessory logos** (phase and service wordmarks such as Science Intelligence™, Science Story™, Science Studio™, Ad-to-Education Sequence™) go in the **bottom-left corner**, across from the Let There Be logo.

## Built to be edited
The team edits these decks and moves content around, so a layout that breaks when someone changes a line is a failure.
- Use the template's own flex and grid layouts. Don't hand-position text with absolute coordinates; that's only for decoration (mitosis shapes) and the footer row.
- Don't set fixed heights on text containers. Let them grow.
- Keep each text block as one element (one `<p>` per paragraph), not split across positioned pieces.
- Duplicate a template slide to repeat a layout. Don't rebuild it by hand.

## Content
- Never invent numbers, quotes, client results or dates. Mark gaps `[NEEDED: …]`.
- Use "videos," never "films," for LTB's mechanism and science video work.
- Client-facing decks leave out internal tool names, other clients' confidential details, and fee or retainer talk unless the deck is about pricing.
