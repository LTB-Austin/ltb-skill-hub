# Claim Set Contract — the handoff between Science Intelligence and Science Story

<!-- Identical copies live in ltb-science-intelligence, ltb-lit-review-deck, and ltb-science-story (each under references/). Edit all three. -->

Science Intelligence produces the Claim Set. Science Story consumes it. Every downstream skill (lit-review deck, consumer-test package, handover) reads the same object. Nothing about a claim is re-derived downstream; if a field is missing here, it is missing everywhere.

## Where it lives

Two synchronized forms of the same data:

1. **Claim Development tab** of the evidence workbook (`[Brand]_Evidence_Workbook.xlsx`). Source of truth.
2. **`[Brand]_Claim_Set.md`**, a markdown mirror with one block per claim, so the Story skill can read it without opening the spreadsheet.

The markdown mirror is generated from the tab, never edited independently.

## Identifiers

- **Claim ID**: assigned once in Science Intelligence and never reused or renumbered. Default scheme is `CLM-01`, `CLM-02`…. A project may instead use territory-prefixed IDs (`PC1`, `DA4`, `LC-02`) when the claims group naturally by territory and the client will reference them that way; the scheme is chosen in Science Intelligence and every downstream deck uses it unchanged. No skill other than Science Intelligence assigns an ID. A derived claim created downstream gets the next free number with a `D` suffix (`CLM-14D`, `PC7D`).
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
| Pivotal study | the one Study ID the claim leads with when it is presented. Must be a `Primary` study with a Full-Text Review record. |
| Consumer translation | the measured result converted to what the consumer hears (copy-craft.md §3), one line, with the derivation ("2.1 days vs 3.9 days, S-014" → "about two days shorter"). The number stays here; the comparison goes on the slide. |
| Honest line | one presentable sentence naming what this evidence does not show, or where the counter-evidence sits and how the wording accommodates it. Written for a slide, derived from Counter-evidence. Never blank. |
| Evidence level | `Product-level` (evidence at this product's dose/form) · `Class-level` (published for the ingredient class) · `Category-standard` (true of the whole category). From the workbook. |
| Market position | `Open` (no scanned competitor claims the endpoint) · `Contested` (one or two do; name them and cite the Competitive Intel rows) · `Commons` (category-standard claim) · `Not scanned`. From the competitive scan only, never from recall. |
| Voice collision | words or phrasing in the claim line that echo a scanned competitor's copy or tagline, with the competitor named; `None` if clean. |
| Client already says it | Y / N, from the client's approved claims list; `Unknown` if not supplied. |
| Deck status | `READY NOW` · `CLASS-LEVEL` · `NEEDS DETAIL`, derived by the rule in claim-development.md, never set by hand. |
| Priority rank | `1`–`6` for claims chosen as deck chapters; blank for the rest. Ranked science first (strength, depth, bridge, risk), then market position. Set once in Science Intelligence. |
| Alternates held | other wordings written or supplied by the client, kept for MLR |
| Client status tag | IN-MARKET · SHORTLIST · NEW · APPROVED · PENDING, where the client uses these |
| MLR status | blank until MLR returns |

## The Board — the header of the Claim Set

`[Brand]_Claim_Set.md` opens with a short header block before the per-claim blocks. The Claim Development tab carries the same content in its first rows (or on the Overview tab). The deck skill reads the Board directly and does not re-derive it; the Story skill reads the client's picks against it.

```
## Headline finding
Finding: [one plain sentence, with Study ID and design]
Becomes: "[lead claim]" · CLM-nn
Why ownable: [one line naming the scanned competitors that do not claim it, the evidence level, and that the client does not already say it. Market position `Not scanned` → this line says so.]

## Priority board
| Rank | Direction (2–4 words) | Lead claim | Claim ID | Pivotal study | Held up by (n studies) | Deck status |
|---|---|---|---|---|---|---|
| 1 | … | … | CLM-nn | S-nnn | 5 | READY NOW |
…

## Field counts
Claims in library: [n] · Removed, client already owns: [n] · Removed or reworded, category commons: [n] · Withdrawn on regulatory grounds: [n] · Flagged for legal: [n]

## Category language map
Scanned: [competitor list, capture date range] — or `Not scanned`
Commons: [endpoints / phrases two or more competitors claim]
White space: [endpoints our evidence supports that no competitor claims]
Category voice to avoid: [words, shapes, taglines]

## Client picks   ← blank until the Science Intelligence deck has been presented
Direction [rank] · CLM-nn · client note
…
```

The headline is the lead claim of rank 1. The Board has four to six rows. `Client picks` is the only part of the Claim Set that is written downstream: it is filled in after the deck meeting, by direction rank and Claim ID, and is what the Story skill clusters around.

## Rules that follow from the contract

- Story renders claims by Claim ID. Every card, body slide, source card, and stimulus shows the ID. If a piece of copy in a Story deck cannot be traced to a Claim ID, it is not a claim; it is narrative and must be reviewed as narrative.
- Claim text and quotes carry through verbatim. Rewording the science means creating a derived claim.
- A derived claim (`CLM-nnD`) is legitimate only if it rests entirely on studies already in the workbook. It is labeled `Derived / unscored` until it has been run back through claim-development.md scoring, and it is never presented as MLR-ready before that.
- Disclaimer text travels with the claim, so it is identical in the workbook, the deck, and the test stimuli.
- Retired claims stay in the set with status `Retired` and a reason. IDs are never deleted.
- Priority rank and Deck status are set in Science Intelligence from the substantiation record. The deck skill displays them; it does not reorder the Board or promote a claim. If the deck needs a different order, the change is made in the Claim Set and both files regenerate.
- A claim cannot hold Priority rank while its Substantiation depth is `Abstract-only — full text required before MLR`. Resolve the full text or rank a different claim.
