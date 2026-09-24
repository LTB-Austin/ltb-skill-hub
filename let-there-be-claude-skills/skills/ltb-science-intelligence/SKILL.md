---
name: ltb-science-intelligence
description: >-
  Run a Claude-native literature review and claim development pass for Let There Be — the Science Intelligence™ stage of the Science Marketing Engine. Use whenever the user wants to research the science behind a health product, run a lit review, pull clinical studies or trials for an ingredient, build an evidence workbook, or develop regulatory-ready marketing claims — even if they just name a brand and an active ingredient, or say "research this product," "what can we claim about X," "find the studies on Y," or "start the science intelligence." Searches the connected Elicit paper/trial tools, builds the structured evidence spreadsheet, and develops MLR-ready claims scoped to the product's regulatory category. This is the FIRST stage of every LTB engine project; reach for it before any Science Story or deck work. Do NOT use for the branded presentation build or for assembling claim clusters/narratives — those are downstream skills.
---

# LTB Science Intelligence™ — Literature Review & Claim Development

## Writing voice — plain and factual

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

You are running the first stage of the Science Marketing Engine: **Prove.** The job is to find the strong science behind a product, organize it into a structured evidence workbook, and turn it into **claims** that are true, defensible, scoped to the product's regulatory category, and ready for MLR. Those claims become the raw material for the Science Story stage (claim clusters → narratives → consumer testing).

Everything runs inside Claude using the connected **Elicit** research tools — no Perplexity relay. The evidence is real (tool-sourced papers with resolving IDs), so your value-add is scoping, structuring, regulatory calibration, and honest synthesis.

## The tools you'll use

- `search_papers` — Elicit corpus (default) or PubMed. Supports `filters.typeTags` (RCT, Meta-Analysis, Systematic Review, Review, Longitudinal), `minYear`/`maxYear`, `includeKeywords`/`excludeKeywords`, `maxQuartile`. Use for fast, targeted pulls per ingredient.
- `search_trials` — ClinicalTrials.gov, with `trialFilters` (phase, recruitment status, hasResults).
- `create_systematic_review` — the workhorse for structured extraction. You define `searches`, `abstractScreening.criteria`, optional `fulltextScreening`, and `extraction.questions` (custom columns that map directly to the workbook). Async: it returns a `reviewId` — poll `get_systematic_review` (with `includeReportBody: true` when done) until status is `completed`.
- `create_report` — lighter, faster structured report for a single research question. Async; poll `get_report`.
- `list_*` / `get_*` — retrieve prior runs.

Prefer `create_systematic_review` when you need the disciplined screen-and-extract table that feeds an ingredient tab. Use `search_papers`/`search_trials` for quick scoping, spotlight-study hunting, and gap-filling.

## Phase 0 — Inputs

Confirm you have (ask only for what's missing; you can derive the rest):

- Brand or working project name
- Active ingredient(s) — INCI / INN / common / Latin name
- Product format (tablet, capsule, gummy, lozenge, liquid, topical, patch, device)
- Intended use / indication
- Target market (US, EU, Canada, APAC)
- Regulatory classification, if known

Minimum viable start: a brand name and one active ingredient. Then run classification.

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

## Phase 3 — Extract into the workbook spine

Default path: **you extract.** For each shortlisted study from Phase 2, pull the fields in `references/workbook-schema.md` from the record the search returned (design, n, comparator, key result, finding direction, mechanism, relevance, safety, PMID/DOI). The searches already return real papers with quantified results and resolving IDs, so Claude reading and structuring them is fast, faithful, and costs nothing extra. Keep scope tight and favor human studies at or near the product's dose and form. Deliberately retain any NULL/MIXED studies — surfacing contradicting evidence is what keeps the resulting claims defensible.

**Record what you actually read.** Every study row carries an **Evidence Basis**: `Abstract`, `OA full text`, or `Full text`. Default to `Abstract` and only mark full text when you have genuinely read it. This field is what lets us state our method honestly instead of implying we read everything.

Opt-in path: **Elicit systematic review.** When the user explicitly wants Elicit's own screened-and-extracted table (deeper, auditable, but async and consumes their Elicit plan quota and creates a saved review in their account), offer `create_systematic_review`. Do NOT run it automatically — always ask first. If they say yes, set `researchQuestion`, `searches` (per-ingredient queries across elicit/pubmed/clinical_trials), `abstractScreening.criteria` (human study; relevant indication; product-relevant dose/form; peer-reviewed), and `extraction.questions` matching the schema columns; optionally `generateReport: true`. Then poll `get_systematic_review` (with `includeReportBody: true`) until `completed` and fold the table into the workbook. `create_report` is the lighter async alternative for a single research question.

## Phase 3b — Full text on load-bearing studies

Abstracts are appropriate for screening, landscape, and prioritisation. They are not sufficient for the few studies a claim actually stands on. Abstracts routinely lead with a secondary or subgroup result when the primary endpoint missed, omit confidence intervals and multiplicity adjustment, and are loose on dose, form, duration, and population.

**The rule.** A study must be read in full text before a claim can rest on it when either is true:

- it is coded **POSITIVE PIVOTAL**, or
- it is the **sole support** for a claim.

Everything else may stay abstract-based. In practice this is about 3 to 10 studies per project, not the whole set.

To retrieve full text, in this order:

1. Set `hasPdf: true` on `search_papers` when hunting candidates for pivotal status.
2. Check open access: PubMed Central, Europe PMC, and the publisher's own OA copy.
3. If the client has institutional or purchased access, ask them to supply the PDF.
4. If it is paywalled and unavailable, do not quietly fall back to the abstract. Mark the claim `ABSTRACT-ONLY - FULL TEXT REQUIRED BEFORE MLR` and raise it in the handback so someone can decide whether to buy the article.

When you do read full text, check the four things abstracts get wrong most often: whether the quoted result was the **primary** endpoint, the **actual effect size with confidence interval**, the **dose and form** against the product, and the **population**. If any of these contradicts the abstract, correct the row and log it in Citation QA.

Never state or imply that a study was read in full when it was not.

## Phase 4 — Verify (light but non-negotiable)

Tool-sourced studies come with real identifiers, which removes most hallucination risk — but still: confirm every study has a resolving PMID or DOI, and check that any specific statistic you carry into a claim actually appears in the source recorded in Evidence Basis. For a pivotal or sole-support study, that source must be the full text. A claim can be no stronger than the study under it. Keep a Citation QA tab (schema file) noting Verified / Corrected / Excluded. Retain NULL/negative studies — never suppress them; they are guardrails.

## Phase 5 — Build the evidence workbook (.xlsx)

Use the `xlsx` skill. Read `references/workbook-schema.md` and build the workbook: Overview · one tab per active ingredient · Claim Development · Competitive Intel · All Studies DB · Citation QA Log · References. Color-code finding direction. This spreadsheet is the internal source of truth and the data appendix for the client handover.

## Phase 6 — Develop the claims (MLR-ready)

Read `references/claim-development.md`. For each SKU, develop claims at three **expression levels** — Consumer (DTC, ≤12 words, disclaimer), HCP (mechanism + evidentiary anchor + differentiator), and MLR/internal (full evidence + limitations + guardrails). Every claim: traces to a verified study, carries an evidence-strength rating, a regulatory-risk rating, and a guardrail note. Use only the permitted claim types for the product class. Present both the client's historical claims (where known) and the new science-backed, regulatory-safe options.

## Phase 7 — Hand off

Deliver: the evidence workbook (.xlsx) + the claim development set. Then note the next step for the user: these verified claims feed the **Science Story** stage, where they're organized into **claim clusters**, tied to narratives, and consumer-tested. If they want the client-facing branded lit-review/claim-dev deck, that's the downstream deck skill.

## Guardrails

- Research is for internal science review; all claims require MLR and legal approval before consumer use. Say so on every claim deliverable.
- Never invent studies, statistics, PMIDs, or DOIs. Prefer fewer verified studies over more uncertain ones.
- A claim is only as compliant as the product class allows. When unsure, flag for legal rather than guess.
- No "Gems." The unit is a **claim**; the package is a **claim cluster** (built in the Science Story stage).
