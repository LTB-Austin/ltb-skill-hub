# Integrated report structure: Supplement Science Score

Use this template when both passes have run. Write it as `<Client>_Supplement_Science_Score.md`. It is built from the two pass findings documents (`rubric-report-structure.md` and the findings template at the end of `llm-capture-schema.md`), and it doesn't replace them. Those stay in the hand-off as appendices.

Write in a plain voice. Every number cites its workbook and tab. Label statements as Published, Observed or Inferred wherever the source document does.

ALWAYS use this template:

# [Client] — Supplement Science Score
Rubric capture window · population size · score range · platform methodology version/date
LLM run window · models and versions · prompts · N per prompt per model · total runs

## 1. Approach
Write one paragraph per pass and then one on convergence. Cover:
- What was read and how the population was built.
- How the prompt set was built and approved, plus N.
- The two scripts.
- The four shared variables.

State that the rubric read is an explanation, not a score, and that LLM output is sampled, not ranked.

## 2. The rubric read
How the platform scores the category: published criteria, observed patterns, and what isn't disclosed. Include the rebuilt scoring model table and what separates the top decile from the bottom quartile on the four variables. Pull this from Rubric Pass findings §2–4.

## 3. The LLM read
Cover how each model frames the category, what gets recommended and why (the attribute map), and how the client is positioned. Include presence, position, sentiment and head-to-head results, written as "named better in x of N runs." Add where the models are reading (the source map). Pull this from LLM Pass findings §2–5.

## 4. Where the two systems agree, and where they don't
Include the convergence table:
- Formulation changes that would move both systems (converges).
- Changes that would move one system but not the other (diverges), each named.
- What the models care about that no formula can fix (not testable). These are off-formula levers such as sources, retail content and brand trust.

## 5. Why [Client] scores and shows up as it does
Per SKU: the platform score and percentile, the penalties mapped to score components, and **what already holds up**. Then the same SKU's LLM presence and the attributes cited against it and for it. Close with the portfolio view: recurring penalties, SKU-specific ones, and components the brand already wins.

## 6. Guardrail implications
Write guardrails as constraint statements, ordered by portfolio reach. Converging guardrails come first, because they're supported by both systems. Each guardrail gets: the constraint · variable · SKUs affected · rubric evidence · LLM evidence · statement type · caveat. State plainly that acting on these may improve outcomes but promises none.

## 7. What we know, and don't
Cover both passes:
- Undisclosed weighting, gated fields, population gaps and confounds.
- N, intervals, consistency indices, version changes, surfaces not run, and personalization or region caveats.
- Capture and run dates.

State that the report doesn't replace the client's own legal and regulatory review.

## 8. Method for re-run
Give the steps for both passes in order: capture protocol, tiering script and flags, prompt set (approved version), run protocol, N, scoring script and flags, and the convergence step. Note what to re-check in twelve months: methodology page changes, score-scale changes, new sub-scores, new model versions or surfaces, and changes in citation behavior.
