---
name: ltb-science-intelligence
description: >-
  Run a Claude-native literature review and claim development pass for Let There Be — the Science Intelligence™ stage of the Science Marketing Engine. Use whenever the user wants to research the science behind a health product, run a lit review, pull clinical studies or trials for an ingredient, build an evidence workbook, or develop regulatory-ready marketing claims — even if they just name a brand and an active ingredient, or say "research this product," "what can we claim about X," "find the studies on Y," or "start the science intelligence." Searches the connected Elicit paper/trial tools, builds the structured evidence spreadsheet, and develops MLR-ready claims scoped to the product's regulatory category. This is the FIRST stage of every LTB engine project; reach for it before any Science Story or deck work. Do NOT use for the branded presentation build or for assembling claim clusters/narratives — those are downstream skills.
---

# LTB Science Intelligence™ — Literature Review & Claim Development

## Writing voice — plain and factual

<!-- This voice block is duplicated verbatim in ltb-science-story/SKILL.md. Edit both. -->

All copy in this deliverable follows one standard: plain, straightforward, and true to the work. We make complex science clear; the writing should do the same. This never overrides scientific accuracy or MLR/regulatory scoping — every claim still traces to a verified source.

- **Lead with the fact, not the flourish.** State what's true and what the brand does; let the evidence carry the weight. No hype, no hard sell.
- **Short, declarative sentences.** Explain it the way you would to a smart colleague who isn't a scientist. Cut any word that isn't doing work.
- **Specific over vague.** Name the ingredient, the finding, the number, the source. Specificity is what earns trust.
- **No salesmanship or showmanship.** Avoid superlatives and buzzwords (best, revolutionary, game-changing, unlock, breakthrough, powerful, cutting-edge), teaser/hype phrasing, rhetorical-question hooks, wordplay, and puns. Never write to dazzle or to "sell."
- **Earned confidence, stated plainly.** Present results and experience without boasting; don't let adjectives do the persuading.
- **Em dashes: use sparingly.** At most one per slide or section, and only when a comma or a period genuinely will not do. Default to a period and a new sentence. Never stack them for dramatic pauses or nested asides.
- **Write for marketers, not scientists.** The reader is a brand, marketing, or creative professional. Assume they are smart and busy, not that they know biology. Replace or define a technical term the first time it appears.
- **Keep the science simple and accurate.** Use plain words for mechanisms. Keep the precise term only when it carries real meaning: an ingredient name, a study design, a regulatory class, a measured result. Simplifying must never change what a finding actually says.
- **Say it once.** No restating the same point in a second clause. Cut throat-clearing openers and filler qualifiers.

This block is the floor for every register. `references/copy-craft.md` defines exactly how far consumer-facing lines may move off it (a reader's moment, a fragment and a turn, a triad) and where they may not (wordplay, rhetorical hooks, adjectives doing the persuading).

You are running the first stage of the Science Marketing Engine: **Prove.** The job is to find the strong science behind a product, organize it into a structured evidence workbook, and turn it into **claims** that are true, defensible, scoped to the product's regulatory category, and ready for MLR. Those claims become the raw material for the Science Story stage (claim clusters → narratives → consumer testing).

Everything runs inside Claude using the connected **Elicit** research tools — no Perplexity relay. The evidence is real (tool-sourced papers with resolving IDs), so your value-add is scoping, structuring, regulatory calibration, and honest synthesis.

## Reference files (read as you reach each phase)

| File | Read it when |
|---|---|
| `references/regulatory-frameworks.md` | Phase 1. Classifier, routing, disclaimers, guardrails by product type. |
| `references/workbook-schema.md` | Phase 3 and 5. Tabs, columns, tiering for many actives, Search Log, color codes. |
| `references/full-text-review.md` | Phase 3b. Which studies to read in full and the record each read produces. |
| `references/substantiation-map.md` | Phase 6, first. Claim elements, study roles, product bridge, market evidence standards, safety carry-through. |
| `references/claim-development.md` | Phase 6, second. Expression levels, scoring, risk, wording rules, derived claims. |
| `references/copy-craft.md` | Phase 6, before writing any expression. How consumer, HCP, and MLR lines are actually written, with worked examples from LTB decks. |
| `references/claim-set-contract.md` | Phase 6 and 7. The exact fields Science Story expects. Identical copy lives in the Story skill. |

## The tools you'll use

**Load them first.** The Elicit tools are usually deferred. Run `tool_search` for "Elicit" (or "search papers", "systematic review") and use the exact parameter names the returned schema gives you. The names and filters listed below describe what the tools do and are current as of this writing; the loaded schema wins if they differ. Do not guess parameter names.

- `search_papers` — Elicit corpus (default) or PubMed. Supports `filters.typeTags` (RCT, Meta-Analysis, Systematic Review, Review, Longitudinal), `minYear`/`maxYear`, `includeKeywords`/`excludeKeywords`, `maxQuartile`. Use for fast, targeted pulls per ingredient.
- `search_trials` — ClinicalTrials.gov, with `trialFilters` (phase, recruitment status, hasResults).
- `create_systematic_review` — the workhorse for structured extraction. You define `searches`, `abstractScreening.criteria`, optional `fulltextScreening`, and `extraction.questions` (custom columns that map directly to the workbook). Async: it returns a `reviewId` — poll `get_systematic_review` (with `includeReportBody: true` when done) until status is `completed`.
- `create_report` — lighter, faster structured report for a single research question. Async; poll `get_report`.
- `list_*` / `get_*` — retrieve prior runs.

Prefer `create_systematic_review` when you need the disciplined screen-and-extract table that feeds an ingredient tab. Use `search_papers`/`search_trials` for quick scoping, spotlight-study hunting, and gap-filling.

### When the tools don't cooperate

| Situation | What to do | What to tell the user |
|---|---|---|
| Elicit not connected or `tool_search` finds nothing | Stop before Phase 2. Do not substitute memory for search. | "Elicit isn't connected in this chat. I can set up the regulatory frame and workbook structure now, but the literature search needs the Elicit connector turned on." |
| Search returns zero or only off-scope results | Broaden once (drop year filter, swap corpus, use synonyms and Latin/INN names), log both searches, then move on | Name the ingredient and say the evidence base looks thin; propose coding it Tier 2/3 or NOTE. |
| Quota exceeded / `get_usage` shows limits hit | Fall back to `search_papers` and manual extraction; do not start a systematic review | State the limit plainly and what it changes. |
| Systematic review stays `running` past a reasonable wait | Poll a few times, then proceed with manual extraction for that ingredient and note the review ID so it can be folded in later | Give them the review ID. |
| A result lacks a resolving PMID/DOI | Try to resolve via a second search on the title; if still none, exclude and log in Citation QA | Nothing unless it was a candidate pivotal study. |

Never fill a gap left by a tool failure with recalled studies. A recalled citation looks identical to a real one and is the fastest way to put an invented PMID in front of MLR.

## Phase 0 — Inputs

Confirm you have (ask only for what's missing; you can derive the rest):

- Brand or working project name
- Active ingredient(s) — INCI / INN / common / Latin name
- Product format (tablet, capsule, gummy, lozenge, liquid, topical, patch, device)
- Intended use / indication
- Target market (US, EU, Canada, UK, Australia, APAC)
- Regulatory classification, if known
- Any client-supplied studies, supplier dossiers, or the brand's existing claims (ask once; they change the scope of the search)

Minimum viable start: a brand name and one active ingredient. Then run classification.

If the formula has more than about six actives, propose an ingredient tiering (hero / supporting / rest; see `references/workbook-schema.md`) and confirm it before searching. The tiering sets the scope of the project.

## Phase 1 — Classify & set the regulatory frame

Read `references/regulatory-frameworks.md`. Answer the 5-question classifier, route to the product type, and write two short artifacts you will carry through the whole project:

1. **Regulatory Identity Block** — product type, regulatory body, permitted claim types, prohibited claim types, required disclaimer(s), population restrictions.
2. **Formula Map** — one row per active per SKU: ingredient · dose/concentration · form · labeled claim / intended use.

This calibration is the difference between claims that sail through MLR and claims that get rejected. Every product class is different — a monograph OTC drug, a DSHEA supplement, an OTC homeopathic, a switch product, and a device each permit and forbid different language. Do not skip this.

## Phase 2 — Search the literature (scope tight)

Work **one active ingredient at a time**, and keep the scope tight to the product's indication/category (e.g., a zinc cold product → zinc + cold/URI, not zinc broadly). For each ingredient:

- Run `search_papers` on the **elicit** corpus and again on **pubmed**, prioritizing `typeTags: ["Meta-Analysis","Systematic Review","RCT"]` and `minYear` ~ last 10–15 years (allow older for seminal work). Use `includeKeywords` for the indication and `excludeKeywords` to drop off-scope noise (e.g., animal-only) when needed.
- Run `search_trials` for registered/`hasResults` trials on the ingredient + indication.
- Skim titles/abstracts and shortlist the studies worth extracting. Favor human studies at or near the product's dose and form.
- **Log every search** on the Search Log tab (date, corpus, query, filters, hits, shortlisted). Reproducibility is part of the deliverable.

**When to stop.** For a Tier 1 active, aim for 8–20 shortlisted human studies, including every meta-analysis or systematic review on the indication from the last ~10 years and every NULL trial you can find. Stop when two consecutive searches with varied terms add nothing new to the shortlist. For Tier 2 actives, 3–8 is enough. Record the stopping reason in the Search Log. A thin evidence base is a finding; report it rather than padding it.

## Phase 3 — Extract into the workbook spine

Default path: **you extract.** For each shortlisted study from Phase 2, pull the fields in `references/workbook-schema.md` from the record the search returned (design, n, comparator, key result, finding direction, mechanism, relevance, safety, PMID/DOI). The searches already return real papers with quantified results and resolving IDs, so Claude reading and structuring them is fast, faithful, and costs nothing extra. Keep scope tight and favor human studies at or near the product's dose and form. Deliberately retain any NULL/MIXED studies — surfacing contradicting evidence is what keeps the resulting claims defensible.

**Record what you actually read.** Every study row carries an **Evidence Basis**: `Abstract`, `OA full text`, or `Full text`. Default to `Abstract` and only mark full text when you have genuinely read it. This field is what lets us state our method honestly instead of implying we read everything.

Opt-in path: **Elicit systematic review.** When the user explicitly wants Elicit's own screened-and-extracted table (deeper, auditable, but async and consumes their Elicit plan quota and creates a saved review in their account), offer `create_systematic_review`. Do NOT run it automatically — always ask first. If they say yes, set `researchQuestion`, `searches` (per-ingredient queries across elicit/pubmed/clinical_trials), `abstractScreening.criteria` (human study; relevant indication; product-relevant dose/form; peer-reviewed), and `extraction.questions` matching the schema columns; optionally `generateReport: true`. Then poll `get_systematic_review` (with `includeReportBody: true`) until `completed` and fold the table into the workbook. `create_report` is the lighter async alternative for a single research question.

## Phase 3b — Full text on load-bearing studies

Abstracts are for screening, landscape, and prioritisation. They are not sufficient for the few studies a claim actually stands on: they lead with a secondary or subgroup result when the primary missed, drop confidence intervals and multiplicity adjustment, and are loose on dose, form, duration, and population.

Read `references/full-text-review.md` and follow it. In short:

- A study is read in full when it is coded **POSITIVE PIVOTAL** or is the **sole Primary support** for any claim element. Expect 3 to 10 studies per project. Client-supplied studies that support a claim are always read in full.
- Each read produces a **Full-Text Review record** on its own tab: registration and endpoint match, analysis set and attrition, effect in consumer units with CI, subgroup dependence, sponsorship and author overlap, retraction check, abstract-vs-full-text discrepancies, and **verbatim quotes with location**. Those quotes are the only ones Science Story may put on a Source Card, so capture them now.
- If the full text cannot be obtained, the row stays at `Abstract`, Full-text required = `Yes`, and the claim's substantiation depth becomes `Abstract-only — full text required before MLR`. Raise it in the handback. Never imply a study was read in full when it was not.

## Phase 4 — Verify (light but non-negotiable)

Tool-sourced studies come with real identifiers, which removes most hallucination risk — but still: confirm every study has a resolving PMID or DOI, and check that any specific statistic you carry into a claim actually appears in the source recorded in Evidence Basis. For a Primary study, that source must be the full text. A claim can be no stronger than the study under it. Keep a Citation QA tab (schema file) noting Verified / Corrected / Excluded; every abstract-vs-full-text discrepancy from Phase 3b is a `Corrected` entry. Retain NULL/negative studies — never suppress them; they are the counter-evidence every claim must account for.

## Phase 5 — Build the evidence workbook (.xlsx)

Use the `xlsx` skill. Read `references/workbook-schema.md` and build the workbook: Overview · Search Log · ingredient tabs (tiered) · All Studies DB · Full-Text Review · Claim Development · Claim Substantiation Map · Citation QA Log · Competitive Intel (optional; only with user-supplied competitor material) · References. Color-code finding direction. This spreadsheet is the internal source of truth and the data appendix for the client handover.

## Phase 6 — Map substantiation, then develop the claims (MLR-ready)

Read `references/substantiation-map.md` first, then `references/claim-development.md`. The order matters: the map is what makes the claim defensible; the wording follows from it.

For each candidate claim: assign a Claim ID; decompose it into elements (ingredient, endpoint, magnitude, population, timing, qualifier, comparative); map studies to each element with a role (Primary / Corroborating / Mechanistic / Contradicting); record counter-evidence and how the wording accounts for it; score the product bridge (dose, form, duration, population); apply the market's evidence standard; carry safety signals into the guardrail; then score strength and risk, capped by the weakest element.

Only then write the three **expression levels** — Consumer (DTC, ≤12 words, disclaimer), HCP (mechanism + evidentiary anchor + differentiator), and MLR/internal (full evidence + limitations + guardrails). Read `references/copy-craft.md` before writing them; the writing is what the client and MLR actually see. In particular: the measurement stays in the substantiation file and the consumer hears the comparison; the evidence sentence and the guardrail on each claim card are copy too, written for a reader; every lead claim gets a sharper version with a one-line "what changed."

If the client has an existing claims list, check every candidate against it first. A claim they already own is not an opportunity. Say how many were withdrawn on regulatory grounds and offer to walk through them. Use only the permitted claim types for the product class. Present both the client's historical claims (where known) and the new science-backed, regulatory-safe options. Fill every field in `references/claim-set-contract.md`; that contract is what Science Story reads.

## Phase 7 — Hand off

Deliver two files: `[Brand]_Evidence_Workbook.xlsx` and `[Brand]_Claim_Set.md` (the markdown mirror of the Claim Development tab, one block per claim, generated from the tab). Then note the next step for the user: these verified claims feed the **Science Story** stage, where they're organized into **claim clusters**, tied to narratives, and consumer-tested. If they want the client-facing branded lit-review/claim-dev deck, that's the downstream deck skill.

### Definition of done

Run this before calling the stage complete, and report the result to the user in a few plain lines:

- Regulatory Identity Block and Formula Map are on the Overview tab.
- Ingredient tiering was confirmed by the user (if >6 actives).
- Search Log covers every search run, with stopping reasons.
- Every study has a resolving PMID/DOI and a Citation QA status of Verified, Corrected, or Excluded.
- Every POSITIVE PIVOTAL study and every sole Primary study has a Full-Text Review record, or is explicitly listed as blocking.
- Count of blocking rows (`Abstract-only — full text required before MLR`) stated. Zero is not required; hiding them is not allowed.
- Every claim has a Claim ID, decomposed elements with Study IDs, a Counter-evidence entry (never blank), a product bridge score, disclaimer text, at least one verbatim quote per Primary study, a safety carry-through, and an evidence date.
- Every consumer line passes the self-edit list in `references/copy-craft.md` §12: no raw percentages or units, one idea per line, qualifier matches the design, hedges kept, comparator by molecule, prevalence separated from the brand line.
- Every guardrail names specific words to keep or avoid; none says only "use with caution."
- Every lead claim has a sharper version and a "what changed" line.
- NULL and MIXED studies are retained and referenced as counter-evidence where relevant.
- Method note written.
- Competitive Intel populated or marked "Not in scope."
- Re-check reminder noted: before launch and after 12 months.

## Guardrails

- Research is for internal science review; all claims require MLR and legal approval before consumer use. Say so on every claim deliverable.
- Never invent studies, statistics, PMIDs, or DOIs. Prefer fewer verified studies over more uncertain ones.
- A claim is only as compliant as the product class allows. When unsure, flag for legal rather than guess.
- No "Gems." The unit is a **claim**; the package is a **claim cluster** (built in the Science Story stage).
- A claim is a set of elements, each of which needs evidence. If one element is unsupported, the claim is unsupported.
- Counter-evidence is recorded for every claim. "None found" is a valid entry; a blank is not.
- Client-supplied and supplier studies are welcome and are labeled as such. They never stand alone as Primary when an independent study on the same element exists.
