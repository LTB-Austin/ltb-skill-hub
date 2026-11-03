---
name: ltb-success-story
description: Build the client Success Story deck for Let There Be. It is a seven-screen case study of a finished engagement covering the challenge, what Science Intelligence™ found, the Science Story™, what Science Studio™ made, and the impact, with client quotes. Use whenever someone wants a success story, case study, client win, project recap or results deck for a completed LTB project, even if they just say "make the success story for [client]" or "write up the Lamisil project." It pulls the approved claims, story and deliverables from the project files, and gets the client-side facts from the account manager through a short intake: the brief, dates, what's live, quotes, feedback ratings and photos. It never invents results or quotes. It writes the content first, then builds the finished deck in the LTB Client Success Story template in the same run. Do NOT use for a SOW (ltb-sow), a sales preview (ltb-sales-preview) or a Project Overview (ltb-project-overview).
---

# LTB Success Story

## How this skill finishes: the deck, in one run

**Every run of this skill ends with a finished presentation built in the LTB Template — Client Success Story (https://claude.ai/artifact/Ax4uiPqesE1nUgsvo1P7pf). Don't stop at the markdown.**

1. Do the work below and write `[brand]-success-story.md`. That's the working draft the deck is built from. It isn't the deliverable on its own.
2. As soon as it's complete, build the deck in the template by following `references/template-build.md`. Do this in the same run. Don't ask whether to continue, and don't wait for the user to ask for slides.
3. Finish by giving the user the deck link, and the open items for the account manager. Never tell them to take the file into Claude Design, and never suggest they ask for a slide deck.

Wherever this skill mentions Claude Design, a design template, an "unbranded" or "content-first" output, or a markdown brief, it means the content draft that feeds this build step. Every rule about content still applies in full: what goes on each screen, exact wording, and gap markers.

Pause before building the deck only in three cases: the skill below requires an approval first, an input the deck needs is missing, or the user asks for content only.

A Success Story shows a finished engagement end to end, in seven screens, as proof that the Science Marketing Engine™ works. The reference build is **Lamisil (Karo Healthcare), October 2026**, LTB's first Success Story.

The reader is a prospective client's brand or marketing lead, so it has to read clearly and fast. Every fact in it is real, approved and traceable.

## Output

> The finished deck, built in the LTB Template — Client Success Story (see the top of this skill). First write `[brand]-success-story.md` in `/mnt/user-data/outputs/`, filled into `references/output-template.md`. It holds seven screens in fixed order, each with its fields and **speaker notes**, followed by a source log and an open-items list. Don't add styling or HTML. The **LTB Template — Client Success Story** carries the look. Photos, packshots and logos are placeholders that get filled by hand.

## Writing voice

- Plain and factual. Lead with the fact: the claim, the number, the date, the result.
- Use short declarative sentences. Define a term the first time it appears, or replace it.
- No hype or superlatives, and no self-congratulation. Let the client's words do the praising, quoted exactly.
- **Headlines state the point on one line.** If one doesn't fit, shorten it.
- Use em dashes sparingly: at most one per screen.

## Where the content comes from

The skill draws on two sources. Keep them separate, and log which one each fact came from.

**1. Project files (gather these yourself).** Search the project space and connected drives before asking anyone.

- **The approved claim set**, with claim IDs, territories and the approver (e.g. Karo MLR). This feeds screen 03.
- **The Science Intelligence™ deck or workbook**, for the territory names and the central insight.
- **The approved Science Story™**: the story line, its beats and the key comparison numbers with their source study. This feeds screen 04.
- **The SOW**, for what was in scope and how each Studio deliverable was described.
- **The Science Studio™ deliverables**: final films or assets, lengths, placements, and approval dates. This feeds screen 05.
- **The Project Overview or kickoff deck**, for the brief, the product and the problem. This feeds screen 02.

**2. The account manager (ask for these).** Send the intake in `references/am-intake.md` as one message, and pre-fill anything the files already answer so the AM only confirms it. The intake covers:

- What the client asked for, in their terms.
- Engagement dates: start and end, shoot location and date, approval dates.
- Where the work is live now, and who is rolling it out (agencies, retail partners).
- Results data the client has shared and approved for use. Use none if none was shared.
- Client quotes, verbatim, with name, title and company, and **confirmation that they're cleared for use**.
- Client feedback survey ratings, if a survey was run.
- Photos (shoot, set, closing call), the hero packshot, and the client's parent-company logo.

If the AM hasn't answered yet, build the deck with `[NEEDED FROM AM: …]` markers and list them at the end. Don't fill the gaps yourself.

## Hard rules

1. **Claims are verbatim from the approved set.** Copy them exactly, including qualifiers. Never paraphrase, combine or improve a claim. If you can't find the approved wording, mark the slot `[NEEDED: approved wording for …]`.
2. **Every number traces to a source.** Each claim count, comparison figure, date and rating goes in the source log with its file or AM answer. A chart always carries its study line (e.g. "Terbinafine 1 week vs clotrimazole 4 weeks, randomized double-blind trial (BMJ 1993).").
3. **No invented results.** Impact means what's live and where, plus any results the client has shared and cleared. Never estimate sales lift, ROAS, conversion or reach. If there is no results data, the Impact screen leads with what's live.
4. **Quotes are verbatim and cleared.** Use exact words, with name and title. Leave out a quote the AM hasn't cleared for use. A recording transcript is a source, but clearance is still needed.
5. **Show only the engine phases that ran.** If the engagement skipped a phase, leave its mark off the title and its row off the challenge card. Replace its screen as described in `references/deck-structure.md`.
6. **Apply client-facing restraint.** Leave out fees, internal tools, internal process names, other clients and any internal feedback. Name partners only if the AM confirms they can be named.
7. **Include ratings only if a survey exists.** If there's no survey, set `showRatings: false`. Never infer ratings from tone.

## How to build

1. **Gather from the project files.** Fill every slot you can, and log the source of each one.
2. **Send the AM intake** with the gaps you found and your pre-filled answers to confirm.
3. **Find the through-line.** In one sentence, state what LTB did for this brand for the first time or differently. It becomes the title subline, for example "Lamisil's first mode-of-action story for US consumers, from claims to campaigns."
4. **Write the seven screens** to `references/deck-structure.md`, in order and at the stated lengths.
5. **Pick the lead claims.** Take one per territory, up to six, and highlight the one with the clearest number. Order them so they build to it.
6. **Choose the comparison numbers** for screen 04. Use up to two head-to-head figures from one source study, with the brand against the comparator.
7. **Write speaker notes** for every screen in two to four plain sentences. They can give context the slide leaves out, such as dates, locations, who approved what, and what the client said on the closing call.
8. **Check the file.** Every claim must match the approved set word for word. Every number must be in the source log. Every quote must be cleared. Headlines must be one line. Confirm there are no fees or internal names.

## Reference files

| File | Read when |
|---|---|
| `references/deck-structure.md` | First. The seven screens, their fields, lengths and fallbacks. |
| `references/am-intake.md` | Before asking the account manager anything. The message to send. |
| `references/output-template.md` | Writing the file. The skeleton, the note to Claude Design and the source log. |
