# Scoring rubric — what the metrics mean and how to read them

Every metric is computed per model, per prompt type, and overall, from N runs. Always print N next to the number. These are sample statistics about model behavior on a date, not a ranking of products.

## Core metrics (client and every competitor)

| Metric | Definition | How to read it |
|---|---|---|
| **Presence rate** | % of runs in which the brand is named at all | The recall question. Report per prompt type: a brand can be present in P4 (asked about directly) and absent in P1 (never recalled unprompted). P1 presence is the one that matters commercially. |
| **Share of recommendation** | Brand's mentions ÷ all product mentions across runs | Crowding. A brand with 20% presence but 5% share is being named alongside many others. |
| **First-mention rate** | % of runs where the brand is the first product named | Models lead with what they favor. |
| **Position profile** | Distribution of the brand's position when named (1, 2, 3, 4+) with mean | Pair with presence; "present but always last" is its own finding. |
| **Sentiment profile** | When named: Recommended / Acceptable / Caveated / Not recommended, as % of mentions | Code from words, quote them. "Fine but…" is Caveated. "Avoid" is Not recommended. |
| **Negative-mention rate** | % of runs naming the brand as something to avoid or as the loser of a comparison | Separate from sentiment because it includes runs where the brand is only mentioned to be dismissed. |

## Attribute metrics (the deliverable)

| Metric | Definition | How to read it |
|---|---|---|
| **Attribute frequency** | For each coded attribute (variable × polarity), % of runs citing it, by brand | The reasons. Sort by frequency. The top negative attributes for the client and the top positive attributes for the brands that beat it are the headline of the LLM read. |
| **Attribute-to-variable split** | Share of all cited attributes falling under Ingredient / Dose / Form / Testing-Transparency / Other | Tells you whether the models are reasoning on formulation (first four) or on something the formula can't fix (price, taste, brand trust, availability). |
| **Verbatim bank** | Up to five representative quotes per attribute per brand | Evidence for the report. Quotes are more persuasive than percentages. |

## Source metrics

| Metric | Definition | How to read it |
|---|---|---|
| **Domain frequency** | % of runs citing each domain, by model | Where the models are reading. Institutional (nih.gov, mayoclinic), editorial (healthline, verywell), retail (amazon, target, walmart), scoring platforms (supp.co, labdoor, consumerlab), brand-owned, video/social. |
| **Brand-associated sources** | Domains cited in runs that name the brand positively vs negatively | Where the client's negative story is coming from is actionable off-formula. |
| **Citation presence** | % of runs that show any citation at all, by model | Models that don't cite are reasoning from training; the source map can't help there and the limits say so. |

## Stability metrics

| Metric | Definition | How to read it |
|---|---|---|
| **Consistency index** | For each prompt × model: mean pairwise Jaccard overlap of the named-product sets across the N runs (0 = different products every time, 1 = identical every time) | Low index = the model isn't settled; don't over-read any single number from that prompt. Report it next to presence. |
| **Presence stability** | For each prompt × model: presence rate's binomial 95% interval given N | Shows how much to trust the rate. With N=10, 70% presence has an interval of roughly 35–93%. Say so. |
| **Version strata** | If the version changed mid-pass, all metrics reported pre/post | A version change is a finding; it also caps what can be claimed. |

## Convergence test (against the rubric pass)

For each attribute cited by the models, look up the matching ingredient / form / signal in the rubric-pass tiers:

| Models say | Rubric tiers say | Classification |
|---|---|---|
| Negative (e.g. "contains artificial dyes") | Drags | **Converges (negative)** — a change moves both |
| Positive (e.g. "methylated B vitamins") | Helps | **Converges (positive)** |
| Negative | Helps or Mixed | **Diverges** — name it |
| Positive | Drags or Mixed | **Diverges** — name it |
| Any | Not scored by the platform (taste, price, brand trust) | **Not testable** |

Summarize as counts and as a short table of the strongest convergences and the notable divergences. Divergence is a finding, not a problem to resolve.

## What not to compute

- A single composite "LLM score" for the client. It invites reading as a ranking and hides the attribute story. If the client asks for one number, give presence rate in P1 with its interval and N, and explain why that's the honest one.
- Trend claims from one pass. Compare to a prior pass or a vendor baseline only with dates and conditions side by side.
