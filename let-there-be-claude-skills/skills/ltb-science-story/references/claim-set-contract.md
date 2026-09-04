# Claim Set Contract — the handoff between Science Intelligence and Science Story

<!-- Identical copies live in ltb-science-intelligence/references and ltb-science-story/references. Edit both. -->

Science Intelligence produces the Claim Set. Science Story consumes it. Every downstream skill (lit-review deck, consumer-test package, handover) reads the same object. Nothing about a claim is re-derived downstream; if a field is missing here, it is missing everywhere.

## Where it lives

Two synchronized forms of the same data:

1. **Claim Development tab** of the evidence workbook (`[Brand]_Evidence_Workbook.xlsx`). Source of truth.
2. **`[Brand]_Claim_Set.md`**, a markdown mirror with one block per claim, so the Story skill can read it without opening the spreadsheet.

The markdown mirror is generated from the tab, never edited independently.

## Identifiers

- **Claim ID**: `CLM-01`, `CLM-02`… assigned once in Science Intelligence and never reused or renumbered. A derived claim created downstream gets the next free number with a `D` suffix (`CLM-14D`).
- **Study ID**: `S-001`, `S-002`… from the All Studies DB. Claims reference studies by Study ID, never by "Smith 2019" alone.
- **Stimulus code** (Science Story, for testing): `H1…`, `N1…`, `C1…`. Each stimulus carries the Claim ID(s) it renders.

## Required fields per claim

| Field | Notes |
|---|---|
| Claim ID | see above |
| Status | `Verified` · `Derived / unscored` · `Flagged for legal` · `Retired` |
| SKU | one row per SKU if the claim applies to several with different disclaimers |
| Ingredient(s) | |
| Regulatory class | from the Regulatory Identity Block |
| Permitted claim type | e.g. structure/function, monograph use, authorized EU health claim |
| Expression level | Consumer · HCP · MLR/internal |
| Claim type | hero · supporting · differentiator · anchor |
| Register | Science-forward · Positioning-forward |
| Claim text | verbatim |
| Required disclaimer text | the exact text, per SKU and market. Story never looks this up elsewhere. |
| Claim elements | the decomposed parts (see substantiation-map.md), each with the Study IDs that support it |
| Supporting studies | Study IDs with role: `Primary` · `Corroborating` · `Mechanistic` |
| Counter-evidence | Study IDs with role `Contradicting`, plus one line on how the wording accommodates them. "None found" is a valid value; blank is not. |
| Product bridge | Dose · Form · Duration · Population, each `Match` / `Near` / `Gap` |
| Evidence strength | Strong · Moderate · Weak (claim-development.md) |
| Regulatory risk | Low · Medium · High |
| Substantiation depth | `Full text verified` · `Mixed` · `Abstract-only — full text required before MLR` |
| Verbatim quotes | at least one per Primary study, with Study ID and location (page or section). These feed Source Cards. |
| Safety carry-through | any AE or contraindication from the supporting set that must appear in a guardrail |
| Guardrail note | what must not be said alongside this claim |
| Candidate direction | loose grouping to speed clustering |
| Evidence date | date the supporting search was run |
| Sharper version | for lead claims: the pack / end-frame compression plus a one-line "what changed" (copy-craft.md §8) |
| Alternates held | other wordings written or supplied by the client, kept for MLR |
| Client status tag | IN-MARKET · SHORTLIST · NEW · APPROVED · PENDING, where the client uses these |
| MLR status | blank until MLR returns |

## Rules that follow from the contract

- Story renders claims by Claim ID. Every card, body slide, source card, and stimulus shows the ID. If a piece of copy in a Story deck cannot be traced to a Claim ID, it is not a claim; it is narrative and must be reviewed as narrative.
- Claim text and quotes carry through verbatim. Rewording the science means creating a derived claim.
- A derived claim (`CLM-nnD`) is legitimate only if it rests entirely on studies already in the workbook. It is labeled `Derived / unscored` until it has been run back through claim-development.md scoring, and it is never presented as MLR-ready before that.
- Disclaimer text travels with the claim, so it is identical in the workbook, the deck, and the test stimuli.
- Retired claims stay in the set with status `Retired` and a reason. IDs are never deleted.
