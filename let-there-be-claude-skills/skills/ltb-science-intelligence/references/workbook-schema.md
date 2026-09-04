# Evidence Workbook Schema (.xlsx)

Build with the `xlsx` skill. Aim for 10–14 tabs. Filename: `[Brand]_Evidence_Workbook.xlsx`.

**Many actives.** A formula with more than 6 actives (a multivitamin, a complex botanical blend) does not get a full tab per ingredient. Tier them:

- **Tier 1 — hero actives:** the ingredients the brand markets on, or that any candidate claim depends on. Full tab each.
- **Tier 2 — supporting actives:** grouped by mechanism or benefit area on shared tabs, studies table only, no full synthesis.
- **Tier 3 — the rest:** one summary tab at NOTE depth (role in formula, dose vs RDA/UL, any safety flag). Promote an ingredient to Tier 1 the moment a claim needs it.

Confirm the tiering with the user before searching; it sets the scope of the whole project.

## Tabs

| Tab | Sheet | Purpose |
|---|---|---|
| 1 | Overview | Classification · Regulatory Identity Block · formula map · SKU index · ingredient tiering · evidence legend · method note · hyperlinks to tabs |
| 2 | Search Log | Every search run, so the evidence base is reproducible (columns below) |
| 3–N | [Ingredient] | Mechanism · bioactives · studies table · synthesis · claim directions · guardrails |
| N+1 | All Studies DB | Flat, filterable, color-coded by finding direction. Assigns Study IDs `S-001`… |
| N+2 | Full-Text Review | One record per study read in full (fields in full-text-review.md) |
| N+3 | Claim Development | One row per claim with Claim ID `CLM-nn`; all fields in claim-set-contract.md |
| N+4 | Claim Substantiation Map | Claim ↔ study links with roles; claim elements; product bridge; counter-evidence (substantiation-map.md) |
| N+5 | Citation QA Log | Verification audit trail |
| N+6 | Competitive Intel | *Optional.* Only when the user supplies competitor label copy or asks for it explicitly; Elicit does not return competitor label claims. Mark "Not in scope" on the Overview if omitted. |
| N+7 | References | Numbered bibliography, live PubMed/DOI links |

## Search Log columns

Date · Corpus (elicit / pubmed / clinical_trials) · Query string · Filters (type tags, years, keywords, quartile) · Hits returned · Shortlisted · Notes (why stopped, what was excluded and why).

Log every search you run, including ones that returned nothing useful. The log is what lets MLR, a colleague, or a future re-check reproduce the evidence base.

## Ingredient tab — study table columns

Request these as the `extraction.questions` in `create_systematic_review` so the tool output maps 1:1 to the sheet:

| Col | Field | Extraction instruction |
|---|---|---|
| A | Study ID | `S-nnn`, assigned in All Studies DB, stable for the project |
| B | Year | 4-digit |
| C | Authors | first author et al. |
| D | Title | full title (link to PubMed/DOI) |
| E | Study Design | RCT / Meta / Systematic Review / Cohort / Open-label / In Vitro / Mechanistic |
| F | Sample size | n = ; population |
| G | Comparator | placebo / active / none |
| H | Key Result | effect size, p, CI, duration (quantified) |
| I | Finding Direction | POSITIVE PIVOTAL / POSITIVE / MIXED / NULL / NOTE |
| I2 | Endpoint hierarchy | `Primary` / `Secondary` / `Exploratory` for the result quoted in Key Result. Default `Unknown` until full text is read. |
| J | Mechanism | receptor/pathway/protein if relevant |
| K | Relevance to product | ties to labeled use, dose, or form |
| L | Safety signal | any AE/contraindication noted |
| M | PMID / DOI | resolving identifier |
| N | Evidence Basis | `Abstract` / `OA full text` / `Full text` — what this row was actually read from. Default `Abstract`. |
| O | Full-text required? | `Yes` if POSITIVE PIVOTAL or sole Primary support for a claim element, else `No`. If `Yes` and Evidence Basis is `Abstract`, the row is blocking. |
| P | Sponsorship | `Independent` / `Industry-funded` / `Brand-funded` / `Unknown` |
| Q | Source | `Search` / `Client-supplied` / `Supplier dossier` |

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

Study ID · Authors · Year · Title (short) · PMID/DOI · Resolves (Y/N) · Key result verified (Y/N/Partial) · Status (Verified/Corrected/Excluded) · Notes.
Completion gate: every study Verified, Corrected, or Excluded before the workbook is "done." Abstract-vs-full-text discrepancies found during Full-Text Review are logged here as `Corrected` with the specific field that changed.

## Competitive Intel fields

Competitor/Parent · Product Type · Target indication · Key actives (+doses) · Regulatory class & claim type · Labeled claims (verbatim) · Evidence quality (Strong RCT / Moderate review / Weak mechanistic / None) · Gap — brand advantage · Gap — competitor advantage · Differentiation opportunity.

---

## Substantiation depth (Claim Development tab)

Every claim carries a **Substantiation Depth** value stating what its supporting evidence was actually read from:

| Value | Meaning |
|---|---|
| `Full text verified` | Every study the claim rests on has been read in full. Cleared to go to MLR. |
| `Mixed` | Every `Primary` study is full-text verified; some `Corroborating` studies are abstract-based. Acceptable for MLR with the method note. |
| `Abstract-only — full text required before MLR` | The claim rests on a study read only at abstract level. **Blocking.** Resolve before the claim leaves Claim Dev. |

A claim cannot be presented as MLR-ready while any blocking row remains.

## Method note (for the deliverable)

The Lit Review deck and the client handover each carry one plain line stating the method, for example:

> Screened at abstract level across [N] studies. The [n] studies supporting the recommended claims were verified against full text.

State it plainly. It is a credibility asset, and it is the difference between an accelerated review and an unverified one.

## Client-supplied evidence

When the brand or an ingredient supplier provides studies (their own trials, supplier dossiers, white papers):

- Enter them in All Studies DB with Source = `Client-supplied` or `Supplier dossier` and Sponsorship set honestly.
- Unpublished or non-peer-reviewed material is coded NOTE unless it is a registered trial with results; it can inform, not substantiate.
- Any client-supplied study that supports a claim gets a Full-Text Review record regardless of Finding Direction.
- Never let a client-supplied study be the only `Primary` for an element if an independent study on the same element exists in the workbook; list both.
