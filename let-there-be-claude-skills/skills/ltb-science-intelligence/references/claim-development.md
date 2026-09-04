# Claim Development

A **claim** is a single, substantiated, defensible statement traced to verified studies. Each claim can be expressed at three audience levels. Use only the permitted claim types for the product class (regulatory-frameworks.md), substantiated to the market's evidence standard (substantiation-map.md), and recorded in the shape every downstream skill expects (claim-set-contract.md).

Every claim gets a **Claim ID** (`CLM-01`…) when it is first written. IDs are stable for the life of the project.

## Order of work

1. Decompose the candidate claim into elements (substantiation-map.md, Step 1).
2. Map studies to elements with roles; record counter-evidence.
3. Score the product bridge.
4. Score evidence strength and regulatory risk (tables below), capped by the bridge.
5. Write the three expressions so each says no more than the map supports.
6. Fill every field in claim-set-contract.md. A claim with a blank required field is not finished.

## Three expression levels

**Consumer (DTC)** — plain language, ≤12 words per claim.
- Hero claim: the single most defensible, consumer-resonant message.
- 2–4 supporting claims: each tied to one ingredient + one endpoint.
- Required disclaimer for the product type.

**HCP / science-literate**
- Mechanism statement (1–2 sentences).
- Evidentiary anchor: pivotal study, author + year + quantified result.
- Formulation differentiator: how this product's dose/form/delivery affects the science.

**MLR / internal (not for consumer use)**
- Full evidence summary (study names, sample sizes, effect sizes).
- Weight-of-evidence: study count, designs, direction consistency.
- Known limitations + explicit guardrails (what the evidence does NOT support).

## Two flavors of claim

- **Science-forward:** "This ingredient does X" — straightforward, mechanism/outcome. Highest defensibility, lower positioning lift.
- **Positioning-forward:** uses the science to advance a market angle. More marketing lift; watch regulatory risk. (The Science Story stage leans on these.)

Present both. Show the client's historical claims (where known) alongside the new science-backed, regulatory-safe options.

## Scoring & risk

| Criterion | Strong | Moderate | Weak |
|---|---|---|---|
| Study design | Pivotal RCT at product dose/form, primary endpoint | Systematic review / consistent meta, or RCT on a secondary endpoint | Mechanistic, in vitro, or post hoc only |
| Evidence direction | POSITIVE PIVOTAL (≥2 RCTs) | POSITIVE (1 RCT/consistent reviews) | MIXED or NOTE only |
| Counter-evidence | None, or explained by dose/population and reflected in wording | Some, partly accommodated | Unaddressed NULL on the same endpoint |
| Product bridge | All four elements `Match` | One `Near`, no `Gap` | Any `Gap` |
| Replication | 3+ independent groups (no author overlap) | 2 groups | Single lab/study |
| Sponsorship | Independent Primary study exists | Industry-funded Primary with independent Corroborating | Brand-funded only |

Rate the claim at the level of its weakest row. A `Gap` on dose or population caps strength at Moderate; two `Gap`s cap it at Weak.

| Risk | Definition | Action |
|---|---|---|
| LOW | ≥2 RCTs at dose; permitted language; disclaimer present; no unaddressed counter-evidence | Standard MLR |
| MEDIUM | 1 RCT/review; mechanism claim; boundary language; quantified efficacy ("by a third"); "clinically shown" | MLR + legal check |
| HIGH | No RCT; disease-adjacent; unsupported %; comparative or "#1"; result was secondary/post hoc but stated as shown | Do not use without MLR + legal clearance |

## Required fields per claim

Defined once in **claim-set-contract.md**. Do not maintain a second list here. The fields that most often get skipped, and must not be: Claim ID · Claim elements with Study IDs · Counter-evidence · Product bridge · Required disclaimer text · Verbatim quotes with location · Safety carry-through · Evidence date.

## Wording rules that follow from substantiation

The craft of the line itself (sentence shape, how a measurement becomes a comparison, product naming, the claim card, the sharper version) is in copy-craft.md. Read it before writing any expression. The rules below are the substantiation constraints the craft operates inside.

- **Qualifiers match the evidence.** "Clinically shown/demonstrated" requires a human RCT on that endpoint as `Primary`. "Clinically studied" requires a human study. "Helps support/maintain" requires mechanism plus human data. Never use "proven."
- **Numbers carry their denominator.** A relative change ("33% shorter") is stated with, or convertible to, the absolute change from the Full-Text Review record. Do not quote a percentage that only exists in a subgroup.
- **Timing and condition travel with the claim.** If the effect depended on when or how the product was taken, the consumer expression says so or the claim is not made.
- **Counter-evidence shapes the sentence.** If a NULL trial exists at a different dose, the wording either specifies the dose context or is softened. The MLR expression names the NULL study.
- **Safety context is not optional.** Guardrail notes carry any AE or contraindication from the supporting set.

## Derived claims

Downstream stages (Science Story) may propose new claims that build on verified ones. Those arrive as `CLM-nnD`, status `Derived / unscored`. Run them through this file in full: decompose, map, bridge, score. Only then do they become `Verified`. A derived claim that needs a study not already in the workbook is a research request, not a claim.

## Bridge to Science Story

Verified claims do not go to the client as a loose list. In the Science Story stage they are grouped into 2–4 strategic directions, assembled into **claim clusters** (2–4 mutually reinforcing claims each), tied to a **narrative**, and consumer-tested. Deliver claims already loosely grouped by candidate direction so clustering starts fast, and deliver them in the two forms the contract requires: the Claim Development tab and `[Brand]_Claim_Set.md`.
