# Choosing the Evidence Visual (and its CSV)

Each territory's evidence slide gets one hero tile and one visual. Pick by the shape of the evidence. Write one CSV per chart or tile set in `[brand]_si_deck_data/`, named `T[n]_[what].csv`, and reference it on the slide.

| Evidence shape | Visual | CSV columns (minimum) | Example |
|---|---|---|---|
| Two groups compared on one outcome | Grouped bar chart | study, group, arm, value, timepoint, n, basis | Still using the product after quitting: 80% vs 9% |
| How a population splits | 100% stacked bar or waffle | category, percent, order | Dual users two years later: 55.2 / 25.7 / 7.0 / 12.1 |
| Label-by-label or class-by-class facts | Yes/No comparison table | row, product A, product B, product C, source | Warnings on NSAID vs Tylenol labels; FDA-approved vs authorized |
| A count built up step by step | Additive table ("added, not already counted") + 4-step method slide | label item, how measured, prevalence, added | NHANES 64.6% |
| A spread or inconsistency | Horizontal range chart (min–max bars, points for fixed values) | product, min, max, unit, market, source, basis | Nicotine per pouch vs labeled Habitrol strengths |
| Speed or time | Horizontal bars in minutes | product, low, high, source, funding | Time to peak nicotine |
| Several independent confirmations | 3 replication tiles (stat + one line + source) | study, finding, value, timepoint, basis | Three PATH analyses agreeing |
| A regulator or label said it | Quote card(s) with source and capture date | — | FDA "not safe, nor FDA approved" |

## Rules

- One hero number per evidence slide. It must be in a source read in full or an official page; if it rests on an abstract, say so in Compliance Logic and mark it blocking.
- Chart only traceable numbers. Every CSV row carries its source and evidence basis.
- Keep mixed units off one axis (e.g., per-piece oral doses vs 24-hour patch doses).
- Flag market and date differences in the CSV and on the chart (US vs EU sample; pre-2016 data).
- When counter-evidence exists, add it as its own small CSV or tile (e.g., `T2_efficacy_guardrail.csv`) so Design can place the "honest line" card.
- Derived numbers (sums, ratios) show their parts: "80.9% = 55.2% smoking only + 25.7% still dual."
