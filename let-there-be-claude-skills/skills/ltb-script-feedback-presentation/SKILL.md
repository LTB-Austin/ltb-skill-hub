---
name: ltb-script-feedback-presentation
description: Build a client walkthrough deck for edits to a script or copy the client sent (or their feedback on ours): each change, why it changes, and the recommended line, aimed at getting to production. Use whenever someone says "walk them through the edits," "make a deck of the script changes," "we need to clear these before production," or shares a script .docx with highlighted compliance notes. Do NOT use to re-pitch a Science Story, propose a new creative direction, or present research.
---

# Script Feedback Presentation

A short Slides deck (about 8 to 10 screens) that walks a client through the changes we need on a script, VO, supers or other copy, line by line, so it can move into production. It is a working-session deck, not a strategy deck.

## When to use

- The client sends a script (or their revision of ours) and we have edits, compliance notes or claim concerns.
- The client gives feedback on our script and we need to show what we'll change, what we won't, and why.
- Someone says "walk them through the edits", "make a deck of the script changes" or "we need to clear these before production."

Do NOT use it to re-pitch a Science Story, propose a new creative direction, or present research. If the script is late in the process (several versions in, production waiting), the goal is to clear the edits, not to re-pivot.

## Inputs

1. **The script or copy doc.** Often a .docx with several versions stacked (for example a teammate's rewrite above, the client-preferred version with compliance edits below). Extract every version, plus highlights, comments and footnotes:
   - `python-docx`: read each run's `font.highlight_color` to find highlighted words.
   - `pandoc -t markdown`: footnotes come through as `[^n]`, highlights as `{.mark}`.
2. **Which version goes to production.** Ask if it isn't obvious. Don't assume the top version or the newest one.
3. **The notes on each highlight** (the footnotes or comments). These are the edits. Each note says what is wrong; it may or may not say what to change it to.
4. **Context, when it matters:** the approved Science Story and claim set, the product label, and any substantiation. Read from the project before writing "why it changes."

## Before writing, confirm

- Which version is the base, and whether another version already contains recommended wording for some edits. **If someone already wrote the fix, use their line. Don't write a new one.**
- For each edit, its type:
  - **Copy change:** the words change.
  - **Disclaimer only:** the copy stays exactly as written; add a symbol (*, †) and a super. Don't rewrite the VO.
  - **Already resolved:** an existing version handles it; show it as recommended.
- Whether the client wants anything flagged beyond the marked edits. Default to the marked edits. Put anything extra on a single "worth a look" slide, framed as quick checks, so it doesn't read as a rethink.

## Deck structure

1. **Cover:** "[Product] script edits." Subline: what it's for (for example "Four fixes to clear before production").
2. **The script as it stands:** the production base, verbatim, with each edit marked in place: the word or phrase in bold red (#e1483b) plus a circled number (① ② ③ ④). Footer: approximate runtime and "Numbered words are the edits, one per slide."
3. **One slide per edit,** two columns separated by a hairline, no cards:
   - Left: **As written** (the line, with the marked words in red), then **Why it changes** (the note, in plain language, one or two sentences).
   - Right: **Recommended** (the new line, large and bold), then a short second block: the new disclaimer, "Two changes" if a line carries more than one fix, or "Don't lose" for an asterisk or footnote that has to travel.
   - Headline: "Edit N: [verb] '[word].'" on one line.
4. **Open-question slide (only when needed):** when a recommended line is still true word by word but implies something the product can't back, add a slide after that edit. Left: what it implies, and what the ingredients or evidence actually show. Right: options as ruled rows (ship as written / an alternative line that removes the implication / substantiate it), with the trade-off of each. Center the options column vertically.
5. **The revised script:** the full script with all edits applied, changes in bold. Alternative lines go directly under the line they replace, in italics, labeled "Alt:". All footnotes go in the footer.
6. **Next steps:** ruled rows with an owner pill and timing, ending in production (agree the edits, clear open items, MLR or compliance review, record VO and build supers with footnotes).

Drop any slide that doesn't do a job. Eight to ten slides is typical.

## Copy rules

- Quote claims and lines in full. Never refer to them by claim code (F-01, X-01) on a slide or in a client message.
- Don't put people's names or version labels ("Lindsey's V5") on slides. Just say "Recommended."
- Keep the client's or teammate's wording wherever it already works. Change only what the note asks for.
- Every footnote symbol in the script has its footnote on the same slide, and the revised script carries all of them.
- Don't put negatives about the client's own ingredients in on-screen disclaimers (for example, say "Amino acids from salmon, the first ingredient," not what the other ingredient lacks).
- American English; dates as "November 2026" or "11/05/26."

## Common claim issues to check (pet and consumer health)

- **AAFCO "meat"** means flesh from slaughtered mammals. Use "real salmon" or "real fish" on fish products, everywhere "meat" appears.
- **"Complete protein"** can't be claimed when part of the protein is incomplete (for example, collagen from cod skin). It also sits close to AAFCO's "complete and balanced."
- **Amino acid comparisons.** Plant proteins like pea carry every essential amino acid, just less methionine. Collagen has no tryptophan. A line implying ours delivers more amino acids than competitors needs data; otherwise end it on source ("part of the protein isn't fish").
- **Serving claims** ("10g per serving") need the feeding-directions footnote; "up to" matches most approved wording.
- **Unsourced numbers** ("up to 80g of protein daily") need a source on file before VO records.

## Building the deck

Create it from the Slides type with the Let There Be design system, using the layouts of **LTB Template — General Presentation** (https://claude.ai/artifact/CFZ5G3y4Su5DWCmFCXJh9y). Read its cover, text, two-column, table, statement and next-steps slides, and copy its mitosis-cell and logo assets into the deck server-side.

- Headers stay on one line; shorten copy or step the size down.
- No tiles or boxed cards. Use two columns with a hairline, ruled rows or tables.
- Mitosis cells sit in corners with other cells around them. Never use a single blob on its own.
- Speaker notes carry the reasoning detail, so the slides stay clean.

## Revising live

The client and team will edit the deck and leave comments while you work. Before every change, re-read the slide files you'll touch, keep their edits (headline changes, deleted slides, reworded lines), and make only what was asked. Reply in each comment thread with what changed.
