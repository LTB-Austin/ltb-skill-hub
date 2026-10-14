---
name: ltb-research-alignment-session
description: 'Build the Research Alignment Session deck for Let There Be - the meeting that kicks off Science Intelligence and Science Story on a signed project. Reads the client''s assets (brief, proposal, consumer research, sizing data, approved claims, labeling, brand book, clinical files) and writes a screen-by-screen content brief for Claude Design: the challenge, what we absorbed, how the engine runs, where we search and where we do not, three directions to pressure-test, the decisions we need, guardrails and the timeline. Also produces a decisions log for the room, which becomes the brief for Science Intelligence. Use whenever someone mentions a research alignment session, research kickoff, alignment deck or RAS, or says the client''s materials are in and it is time to build the session. Do NOT use for the Project Overview (ltb-project-overview), the SOW, a sales preview, or the lit review itself (ltb-science-intelligence).'
---

# LTB Research Alignment Session

## What this is

The Research Alignment Session is the first working meeting on a signed project. The client has sent their materials. We have read them. **We have not opened the literature yet**, and that is deliberate: before we search, we agree with the client on the evidence standard, the territories, the boundaries, and the decisions only they can make.

The deck does three jobs:

1. **Show we did the reading.** Their numbers, their language, their approved claims, played back accurately and organized better than they had them.
2. **Show how the work runs.** The evidence standard, how claims are built and rated, how Science Story turns claims into tested directions.
3. **Get decisions.** Proposed search priorities, proposed exclusions, three candidate directions, and a short list of questions that change the research depending on the answer.

It sits between `ltb-project-overview` (the kickoff brief) and `ltb-science-intelligence` (the lit review). The decisions log this skill produces is the brief that Science Intelligence starts from.

Reference builds: Tylenol (Kenvue, Adult Pain, Aug 2026), Habitrol (Dr. Reddy's, NRT, Oct 2026), Complete Commensal Probiotic (Designs for Health, Sept 2026).

## Reference files

| File | Read it when |
|---|---|
| `references/deck-structure.md` | First. Every screen, which are boilerplate, which are optional modules, and when to use each. |
| `references/writing-patterns.md` | Before writing the variable screens. How the challenge, priorities, exclusions, directions and questions are written, with examples from the reference builds. |
| `references/output-template.md` | When writing. The skeleton the brief and the decisions log are filled into. |

> **Output:** one markdown file, `[brand]-research-alignment-session.md`, in the outputs folder. Part 1 is the deck, screen by screen. Part 2 is the decisions log, a blank-ready capture sheet for the session. Content only: no styling, no layout instructions. Claude Design builds the deck from it.

## Writing voice

Plain, specific, and confident without selling. This is a working session with a client who has already bought.

- Lead with the fact. Short declarative sentences. Name the number, the population, the claim, the source.
- **Their words, their numbers.** Use the client's own names for things ("the Special Condition Consumer opportunity," "the Missing Biome platform") and their own data, with the source named. It shows we read it.
- **Proposals, not decisions.** Priorities, exclusions and directions are offered for the client to confirm or change. Say so on the screen.
- Explain the reasoning in one sentence. Every priority says why it ranks where it does. Every exclusion says why it is out.
- No superlatives, no hype, no wordplay. Headlines state the point.
- Em dashes: at most one per screen.
- American spelling throughout ("prioritizing," "randomized").

## Inputs

Work from the assets in the project or the conversation. Typical set:

- The client brief, RFP or our proposal and SOW (objective, scope, dates).
- Consumer research, segmentation, sizing, sales or shopper data.
- Approved claims, claims architecture, labeling or Drug Facts, previously rejected claims.
- Brand book, brand idea, positioning decks.
- Safety, clinical or scientific files (GRAS dossier, clinical protocols, science reviews, strain or ingredient files).
- Any notes from the kickoff call.

Also establish: brand and product, client company and team, **regulatory class** (US OTC monograph, OTC NDA, dietary supplement under DSHEA, device, UK/EU medicine), the **business moment** the work is pointed at (brand planning, a season, a launch, a go-live), the session date, and who will be in the room (brand only, or Medical, Legal and Regulatory too).

If something is missing, do not invent it. Mark it with `NEEDED FROM YOU` on the screen where it would go, and add it to the decisions log.

## Phase 1 — Read and inventory the assets

List every asset received with one line on what we understand it to be. Note what is missing or out of date. This drives the optional "What we have" screen and the `NEEDED FROM YOU` markers.

## Phase 2 — Extract the challenge and the numbers

- **The challenge.** What the business needs, in the client's terms, and what our job is inside it. Two or three short paragraphs.
- **Why evidence, not positioning.** Why this argument needs published evidence rather than brand language. Tie it to something the client said or wrote (their review standard, their plan, their claims situation).
- **The numbers.** Pull four headline figures from the client's materials for the stat screen, plus two "pattern underneath it" observations. Every figure carries its source in the source line. Never round or restate a figure in a way that changes it. Never add a figure from outside their materials to this screen.
- **The segments.** The population or user groups by scale, as a table, using their data.
- **Approved language.** Their current approved claims, verbatim. Then two places where evidence can add to them. If we do not have the approved claims, say `NEEDED FROM YOU` and still name the two places.

## Phase 3 — Propose the search

**Do not run Elicit or cite studies in this deck.** The literature has not been opened. Search priorities are lines of inquiry, written as questions or as "what the literature reports on…", and anything drawn from general domain knowledge is conditional ("If that holds up, …").

- **Where we search first.** Four to five priorities, plus an optional exploratory scan. Rank on population, opportunity value, and how much room the evidence could give beyond what the client already claims. Each priority has a name, its size or rationale line, and two or three sentences on the lines of inquiry.
- **Where we are not spending the time.** Four to six proposed exclusions, each with its reason. The strongest reason is usually that the territory invites a counter-argument against the product itself, or that the addressable number is much smaller than it looks.

## Phase 4 — Three directions to pressure-test

Write three candidate shapes for the argument (`Direction A`, `B`, `C`), each with a short name and a paragraph. They are "not conclusions," but candidate shapes so we know what to watch for as we search. Order them so the regulatory risk is visible: one bold and comparative, one built on a behavior or population insight, one that argues for the brand's own path rather than against a competitor. State the regulatory difficulty of each in plain words. If the client's own materials pull in two directions (a proposal promise versus a brand book idea), name the tension as **the question for today**.

## Phase 5 — The decisions

- **Questions we need answered today**, or **What we need to settle today**: five to seven, each one a decision that changes the research. Typical: comparator (class or named product), SKUs in scope (dose, form and duration change the literature), how far the argument can go, consumer or HCP or both, source threshold for MLR, who the reviewers are, and the outcome they want at the business moment.
- **Guardrails** (when relevant): restricted language and rejected claims, competitor-owned language, position on naming competitors, portfolio conflicts, off-limits populations, and where the product's own labeling limits the argument.

## Phase 6 — Timeline

Use the dates from the SOW or proposal. Lay out the standard stages (see `deck-structure.md`) and anchor the side note to the business moment: what the client has in hand, and by when. If the plan depends on a client-side date (reviewer availability over a holiday, shortlist turnaround), name it as the date to confirm today. If there are two realistic paths, show both (accelerated and standard) and say where the difference sits. Never invent dates; mark unknown ones `To be defined`.

## Phase 7 — Fill the brief and the decisions log

Fill `output-template.md`: the deck screen by screen, then the decisions log, with one row per question, guardrail, scope proposal and `NEEDED FROM YOU` item, ready to capture the client's answer in the room.

## Non-negotiables

- No studies, PMIDs, or literature findings stated as fact. The search has not started.
- Every number on the deck comes from the client's materials, with its source named.
- Approved claims quoted verbatim.
- Boilerplate screens reproduced as written in `deck-structure.md`.
- Every priority has a reason; every exclusion has a reason; every direction names its regulatory difficulty.
- Proposals are labeled as proposals.
- Gaps marked, never filled.

## Definition of done

Report back in a few plain lines:

- Screen count, and which optional modules were used and why.
- Assets read, and anything marked `NEEDED FROM YOU`.
- Every stat sourced to a client document.
- Priorities, exclusions and directions each carry their reasoning.
- Five to seven decisions, each one that changes the research.
- Timeline built from real dates, with the date to confirm named.
- Decisions log complete.
