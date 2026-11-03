# Capture schema and results workbook — LLM Pass

## runs.csv (one row per run) — the script reads this

| column | content |
|---|---|
| run_id | sequential, zero-padded: 0001 |
| date | YYYY-MM-DD |
| time | local time with zone |
| model | ChatGPT / Gemini / Claude / Rufus / AIO / Perplexity |
| version | as displayed, verbatim; `not displayed` if absent |
| prompt_id | e.g. P1-men50 |
| prompt_type | P1…P7 |
| segment | adult / men / women / 50+ / gummy / … |
| prompt_text | verbatim |
| response_text | full text |
| products_named | pipe-separated, in order, normalized `Brand – SKU` e.g. `Thorne – Men's Multi 50+ \| Nature Made – Multi for Him 50+` |
| client_named | Y / N |
| client_position | integer or blank |
| client_sentiment | Recommended / Acceptable / Caveated / Not recommended / blank |
| client_negative_mention | Y / N (named as avoid / comparison loser) |
| attributes | pipe-separated coded entries `Brand – SKU :: variable :: polarity :: "verbatim phrase"` e.g. `Centrum – Men's :: Ingredient :: - :: "contains artificial colors like Yellow 6"` |
| sources | pipe-separated domains |
| citation_present | Y / N |
| screenshot | path |
| conditions | the conditions string from llm-run-protocol.md |
| anomalies | free text or blank |

Variable codes: `Ingredient`, `Dose`, `Form`, `Testing`, `Other`. Polarity: `+` or `-`.

## Results workbook tabs (`<Client>_LLM_Pass_<YYYY-MM-DD>.xlsx`)

1. **Prompt Set** — prompt_id · type · segment · text · approved by · approval date
2. **Run Log** — the runs.csv, as-is
3. **Coded Runs** — one row per (run, product named): run_id · model · prompt_id · brand · sku · position · sentiment · attributes
4. **Metrics by Model** — script output `metrics_by_model.csv`
5. **Competitor Table** — script output `brand_table.csv`
6. **Attribute Map** — script output `attribute_map.csv` + verbatim bank
7. **Source Map** — script output `source_map.csv`
8. **Stability** — script output `stability.csv` (consistency index, presence intervals, version strata)
9. **Convergence** — attribute · models' polarity · rubric tier · classification · note
10. **Limits** — limit · why it matters · which findings it touches
11. **Method Log** — setup screenshots, conditions by model, N, dates, discards, version changes, script version

## Findings document structure (`<Client>_LLM_Pass_Findings.md`)

ALWAYS use this template:

# [Client] — LLM Pass: [models]
Run window · models and versions · prompts · N per prompt per model · total runs

## 1. Approach
How the prompt set was built and approved, the conditions, N, how responses were coded and scored. Name the script. Say that output is sampled and that no ranking is implied.

## 2. How each model frames the category
Per model: what it says matters when choosing (from P2), the brands it reaches for unprompted (P1 presence and first-mention, with N), citation behavior.

## 3. What gets recommended, and why
The competitor table. Then the attribute map for the brands that lead: the top positive attributes, by variable, with quotes.

## 4. How [Client] is positioned
Presence by prompt type · position profile · sentiment profile · negative-mention rate · the top attributes cited against it and for it, with quotes · head-to-head results per competitor (P3) as "named better in x of N runs," never as a verdict.

## 5. Where the models are reading
Source map by model; brand-associated sources; the share of runs with no citations.

## 6. Convergence with the rubric read
The convergence table. What a formulation change would move in both systems; what it would move in one but not the other; what the models care about that no formula can fix.

## 7. What we know, and don't
N and intervals · consistency indices · versions and any mid-pass change · surfaces not run · personalization and region caveats · date stamp. The report does not replace the client's own legal and regulatory review.

## 8. Method for re-run
Prompt set, protocol, N, script, and what to re-check (new model versions, new surfaces, changes in citation behavior).
