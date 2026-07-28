# Evidence Workbook Schema (.xlsx)

Build with the `xlsx` skill. Aim for 8–12 tabs. More than 6 actives → group mechanistically related ones.

## Tabs

| Tab | Sheet | Purpose |
|---|---|---|
| 1 | Overview | Classification · formula map · SKU index · regulatory summary · evidence legend · hyperlinks to tabs |
| 2–N | [Ingredient] | Mechanism · bioactives · studies table · synthesis · claim directions · guardrails |
| N+1 | Claim Development | Science-to-claim bridge by SKU · Consumer/HCP/MLR expressions · evidence strength · risk · guardrails · MLR status |
| N+2 | Competitive Intel | Competitor profiles · ingredient gaps · evidence quality |
| N+3 | All Studies DB | Flat, filterable, color-coded by finding direction |
| N+4 | Citation QA Log | Verification audit trail |
| N+5 | References | Numbered bibliography, live PubMed/DOI links |

## Ingredient tab — study table columns

Request these as the `extraction.questions` in `create_systematic_review` so the tool output maps 1:1 to the sheet:

| Col | Field | Extraction instruction |
|---|---|---|
| A | Study # | sequential |
| B | Year | 4-digit |
| C | Authors | first author et al. |
| D | Title | full title (link to PubMed/DOI) |
| E | Study Design | RCT / Meta / Systematic Review / Cohort / Open-label / In Vitro / Mechanistic |
| F | Sample size | n = ; population |
| G | Comparator | placebo / active / none |
| H | Key Result | effect size, p, CI, duration (quantified) |
| I | Finding Direction | POSITIVE PIVOTAL / POSITIVE / MIXED / NULL / NOTE |
| J | Mechanism | receptor/pathway/protein if relevant |
| K | Relevance to product | ties to labeled use, dose, or form |
| L | Safety signal | any AE/contraindication noted |
| M | PMID / DOI | resolving identifier |

Close each ingredient tab with: **Evidence Synthesis** (3–5 sentences), **Claim Direction** (bulleted), **⚠ Guardrails** (what must NOT be claimed).

## Finding-direction color codes

| Code | Meaning | When | Fill |
|---|---|---|---|
| POSITIVE PIVOTAL | Landmark/brand-direct trial, highest weight | Pivotal RCT at product dose/form | dark green |
| POSITIVE | Significant benefit on relevant endpoint | Clear p<0.05, well-designed | green |
| MIXED | Partial/inconsistent/formulation-dependent | Heterogeneous meta; subgroup-only | amber |
| NULL | No significant benefit | Retain as guardrail — never suppress | red |
| NOTE | Mechanistic/safety/chemistry/regulatory context | In vitro, animal, chemistry, guidance | grey |

## Citation QA Log columns

Study # · Authors · Year · Title (short) · PMID/DOI · Resolves (Y/N) · Key result verified (Y/N/Partial) · Status (Verified/Corrected/Excluded) · Notes.
Completion gate: every study Verified, Corrected, or Excluded before the workbook is "done."

## Competitive Intel fields

Competitor/Parent · Product Type · Target indication · Key actives (+doses) · Regulatory class & claim type · Labeled claims (verbatim) · Evidence quality (Strong RCT / Moderate review / Weak mechanistic / None) · Gap — brand advantage · Gap — competitor advantage · Differentiation opportunity.
