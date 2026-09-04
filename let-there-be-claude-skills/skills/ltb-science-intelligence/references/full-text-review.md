# Full-Text Review — reading the studies a claim stands on

Abstracts are for screening. Full text is for substantiation. This file defines what a full-text read produces, so two readers of the same paper generate comparable records and so nothing needed downstream (quotes, provenance, endpoint hierarchy) has to be reconstructed later.

## Which studies get a full-text read

Read in full when either is true:

- the study is coded **POSITIVE PIVOTAL**, or
- it is the **sole Primary support** for any claim element.

Expect 3 to 10 studies per project. Everything else may stay abstract-based, and the row's Evidence Basis says so.

Client-supplied studies (the brand's own trials, branded-ingredient supplier dossiers) always get a full-text read if they support a claim. They carry the highest sponsorship-bias risk and MLR will read them first.

## Getting the full text

In order:

1. Set `hasPdf: true` (or the equivalent in the loaded Elicit schema) when hunting pivotal candidates.
2. Check open access: PubMed Central, Europe PMC, the publisher's own OA copy. In many environments Claude cannot fetch these directly; if you cannot retrieve the file, do not pretend you did.
3. Ask the user for the PDF if the client or LTB has access.
4. If it is unavailable, keep the row at `Abstract`, set Full-text required = `Yes`, and let the claim's substantiation depth become `Abstract-only — full text required before MLR`. Raise it in the handback so someone decides whether to buy the article.

Never state or imply a study was read in full when it was not.

## The Full-Text Review record

One record per study read, stored on the **Full-Text Review** tab. Fill every field; write `Not reported` rather than leaving blanks, because a blank is indistinguishable from "didn't look."

| Field | What to capture |
|---|---|
| Study ID | from All Studies DB |
| Source of PDF | PMC · Europe PMC · Publisher OA · Client-supplied · Purchased · URL |
| Date read | |
| Registration | Trial registry ID (NCT, ISRCTN, other) or `Not registered`. Does the reported primary endpoint match the registered one? `Yes` / `No` / `Cannot verify` |
| Design detail | randomization method, blinding (who), allocation concealment, comparator adequacy |
| Population | inclusion criteria, baseline status that matters for the ingredient (e.g. deficient vs replete; healthy vs diagnosed), age range, country |
| Intervention | dose, salt or form, delivery, frequency, duration, co-interventions |
| Analysis set | ITT · modified ITT · per-protocol. Randomized n vs analyzed n. Attrition % and whether it differed between arms |
| Primary endpoint | name, instrument, whether the instrument is validated, result with effect size and CI, p-value, multiplicity handling |
| Secondary / exploratory results used | each result you intend to carry into a claim, tagged `Secondary` or `Exploratory / post hoc` |
| Effect in consumer units | absolute and relative, with the denominator stated (e.g. "cold duration 7.0 → 4.7 days; 33% shorter"). This is what the claim will say, so compute it here and check it against the paper. |
| Subgroup dependence | does the headline result hold in the full sample or only a subgroup? |
| Safety | AEs, discontinuations, contraindications, interactions noted |
| Funding and COI | sponsor, author affiliations, declared conflicts. Flag `Industry-funded` or `Brand-funded` where applicable |
| Author overlap | shared authors with other supporting studies for the same claim (needed to judge independence) |
| Retraction / correction check | PubMed status and any published correction or expression of concern. `Clear` / `Correction` / `Retracted` |
| Abstract vs full text | anything the abstract said that the full text contradicts or qualifies. Log each item in Citation QA as `Corrected` |
| Verbatim quotes | one to three sentences quoted exactly, each with page or section. Prefer the results or conclusions section. These are the only quotes Story may put on a Source Card. |
| Reader verdict | one plain sentence: what this study can and cannot support |

## Meta-analyses and systematic reviews

Add these fields when the study is a pooled analysis:

| Field | What to capture |
|---|---|
| Included trials | count, and whether your pivotal RCT is among them (double counting if you cite both as independent support) |
| Dose range pooled | and whether the pooled effect holds at or near the product dose |
| Heterogeneity | I² and how the authors handled it |
| Risk-of-bias summary | tool used (RoB 2, Jadad, other) and the overall grade |
| Publication bias | funnel or Egger result if reported |
| Registered protocol | PROSPERO or equivalent |

A meta-analysis with high heterogeneity or a pooled dose range far from the product is `Corroborating`, not `Primary`, regardless of its p-value.

## What the read changes upstream

After the read, revisit the study row and every claim that cites it:

- If the quoted result was secondary or post hoc, the claim cannot say "clinically shown" for that element without saying so. Downgrade Finding Direction or reword.
- If the analysis set was per-protocol with material attrition, note it in the MLR expression and consider downgrading evidence strength.
- If population or dose does not bridge to the product, mark the bridge element `Gap` on the claim.
- If the study is industry-funded, it can still be Primary, but independence for the replication criterion requires at least one non-overlapping, non-sponsor study.
- If the study is retracted, exclude it and re-check every claim that leaned on it.
