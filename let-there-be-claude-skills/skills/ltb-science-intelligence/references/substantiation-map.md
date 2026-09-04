# Substantiation Map — connecting each claim to the evidence that holds it up

A citation says where a claim came from. A substantiation map says whether the claim is actually held up, element by element, against the product as sold, with the evidence that cuts against it in view. MLR reviewers work this way; building the map first means the claim they see has already survived the review they would run.

## Step 1 — Decompose the claim into elements

Most claims bundle several assertions. Each one needs its own evidence. Decompose before scoring.

Common elements:

| Element | Example | Evidence that supports it |
|---|---|---|
| Ingredient does X | zinc shortens colds | Primary study on the ingredient and endpoint |
| Endpoint | cold duration (not severity, not incidence) | the study measured this endpoint, ideally as primary |
| Magnitude | by about a third | effect size and CI from full text, in the same units |
| Population | in healthy adults | study population bridges to labeled population |
| Timing / condition | when started within 24 hours of symptoms | protocol detail from full text |
| Qualifier | "clinically shown," "clinically studied," "helps support" | "shown" needs ≥1 human RCT on that endpoint; "studied" needs a human study; structure/function verbs need mechanism plus human data |
| Comparative | "more than," "#1," "faster than" | head-to-head data or a defensible market-share source |
| Implied dose / form | (the product's) | the product bridge, below |

Write the elements out for every claim. A claim with an unsupported element is unsupported, however strong its best study.

## Step 2 — Map studies to elements with roles

Substantiation is many-to-many. Each claim ↔ study link carries a role:

| Role | Meaning |
|---|---|
| `Primary` | the element rests on this study. Must be full-text verified. |
| `Corroborating` | consistent with the element; adds weight and replication. May be abstract-based. |
| `Mechanistic` | explains why, not whether. Never sole support for an efficacy element. |
| `Contradicting` | NULL or MIXED finding on this element. Always recorded. |

Every claim needs at least one `Primary` per efficacy element. Every claim needs a Counter-evidence entry: the Contradicting studies (or `None found after search of [corpus] on [date]`) plus one line stating how the wording accounts for them. A claim that ignores a NULL trial in the same workbook is the single most common way a set fails MLR.

Independence: the replication criterion in claim-development.md counts research groups, not papers. Use the Author Overlap field from Full-Text Review. Two papers from one lab are one group.

## Step 3 — Score the product bridge

The study is not the product. Score how well the evidence transfers to the SKU as sold:

| Bridge element | `Match` | `Near` | `Gap` |
|---|---|---|---|
| Dose | within ±20% of study dose | same order, different amount | different order of magnitude, or unknown |
| Form | same salt / extract / standardization | related form with bioequivalence data | different form, no bridging data |
| Duration | product use pattern matches study duration | shorter but mechanism plausible | study duration not achievable in use |
| Population | labeled population matches study population | broader or adjacent | different (e.g. deficient-only study, replete consumers) |

A claim's evidence strength cannot exceed what its weakest bridge element allows. A `Gap` on dose or population caps the claim at `Moderate` and requires the gap to be stated in the MLR expression. Two `Gap`s → `Weak`, and the claim should usually be rewritten or dropped.

## Step 4 — Apply the market's evidence standard

Classification (regulatory-frameworks.md) sets what kind of claim is allowed. The evidence standard sets how much proof it needs. Judge substantiation depth against the right one:

| Market | Standard | Practical bar |
|---|---|---|
| US, FTC (all health products) | Competent and reliable scientific evidence; Health Products Compliance Guidance (Dec 2022) | Generally ≥1 well-controlled human RCT on the claimed endpoint, at product-relevant dose, considered with the totality of evidence including negative studies. "Clinically proven" and quantified efficacy claims need stronger support than qualitative structure/function. |
| US, FDA structure/function (DSHEA) | Substantiation on file; FDA guidance mirrors FTC | Same bar in practice; language restrictions come from regulatory-frameworks.md |
| EU / UK food supplements | Only authorized wording (EU Register; GB NHC Register) | Claim development is claim *matching*: find the authorized claim and conditions of use, then substantiate the product meets them (dose per daily portion). New claims are not permitted without authorization. |
| UK advertising | ASA / CAP Code section 15 (food) or 12 (medicines and health) | Authorized-wording rule plus general substantiation duty for any implied claim |
| Canada NHP | Licensed claim language | Match the NPN's licensed claims; evidence was assessed at licensing |
| Australia | TGA listed medicine, permissible indications list | Match the permissible indication; hold evidence per TGA evidence guidelines |

If the product is multi-market, build the map once and record permitted wording per market.

## Step 5 — Safety carry-through

Any adverse event, contraindication, or interaction recorded on a supporting study flows into the claim's Guardrail note. A claim that borrows a study's efficacy also inherits its safety context. Common cases: upper-limit warnings for minerals and fat-soluble vitamins, drug interactions for botanicals, population exclusions (pregnancy, children, specific conditions).

## Step 6 — Write the substantiation record

One record per claim, on the **Claim Substantiation Map** tab and mirrored in `[Brand]_Claim_Set.md`. Fields are defined in claim-set-contract.md. Downstream, Science Story renders Source Cards directly from this record: the verbatim quotes, the applicability note, and the study details come from here, not from a fresh read of the paper.

## Step 7 — Date-stamp and set the re-check

Record the evidence date on every claim. Evidence moves: a new meta-analysis, a retraction, a regulatory update. Note in the handback that claims should be re-checked before campaign launch and any time more than 12 months have passed since the evidence date. The Search Log tab makes the re-run reproducible.

## Worked example (compressed)

Claim CLM-03, consumer level: *"Clinically shown to shorten colds by about a third when started within 24 hours."*

Elements → evidence:

- Ingredient shortens colds → S-004 (Primary, RCT, full text), S-011 (Corroborating, meta), S-007 (Contradicting, NULL at lower dose)
- Endpoint = duration → S-004 primary endpoint, registered
- Magnitude ≈ one third → S-004: 7.0 → 4.7 days (33%), 95% CI [1.4, 3.2] days
- Timing = within 24 h → S-004 protocol
- Qualifier "clinically shown" → satisfied by S-004 as RCT on this endpoint
- Bridge: Dose `Match` · Form `Near` (acetate vs gluconate, bridging data in S-011) · Duration `Match` · Population `Match`
- Counter-evidence: S-007 null at 13 mg/day; product delivers 75 mg/day; wording specifies timing, and MLR expression notes dose dependence.
- Safety carry-through: nausea and dysgeusia at high dose (S-004 AE table) → guardrail: do not imply "no side effects."
- Substantiation depth: Full text verified. Strength: Strong. Risk: Medium (quantified efficacy claim; confirm class permits "clinically shown").
