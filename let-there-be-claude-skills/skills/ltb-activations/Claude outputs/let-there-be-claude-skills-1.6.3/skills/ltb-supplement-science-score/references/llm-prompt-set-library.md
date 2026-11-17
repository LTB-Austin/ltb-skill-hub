# Prompt-set library

Starter prompts by type. Adapt the category and segments to the project; keep the phrasing the way a consumer would actually type it. Build the matrix (type × segment), trim to 12–20, show the client, record approval before running.

Rules:
- Generic prompts (P1, P2, P5, P6) never name the client.
- Brand prompts (P3, P4, P7) name the client; P3 names one competitor at a time (rotate through the set across prompts, not across runs).
- Each prompt gets an id: `P<type>-<segment>` e.g. `P1-men50`, `P3-women-vs-ritual`.
- Keep the text identical on every run. Fix typos before approval, not after.

## P1 — Generic recommendation (brand recall)
- "What's the best multivitamin for men over 50?"
- "What's the best multivitamin for women?"
- "What multivitamin should I take? I'm a healthy adult."
- "Best gummy multivitamin for adults?"
- "Which multivitamin brands do doctors or dietitians actually recommend?"
- "Top 5 multivitamins I can buy at a drugstore"

## P2 — Choice criteria (what the model says matters)
- "How do I choose a good multivitamin?"
- "What should I look for on a multivitamin label?"
- "What ingredients should a multivitamin NOT have?"
- "Does the form of the vitamin matter, like methylfolate vs folic acid?"

## P3 — Head-to-head (one competitor per prompt)
- "[Client Men's SKU] vs Thorne men's multivitamin — which is better?"
- "[Client Women's SKU] vs Ritual Essential for Women — which should I take?"
- "[Client Silver SKU] vs Nature Made 50+ — which is better for someone over 50?"
- "[Client gummy] vs Olly gummy multivitamin?"

## P4 — Brand evaluation
- "Is [Client] a good multivitamin?"
- "Is [Client Silver] good for people over 50?"
- "What's in [Client Men's] and is it high quality?"

## P5 — Ingredient / quality probes (tests the four variables)
- "Which multivitamins don't have artificial dyes or titanium dioxide?"
- "Which multivitamins use the most absorbable forms of vitamins and minerals?"
- "Which multivitamins are third-party tested?"
- "Are cheap drugstore multivitamins as good as expensive ones?"
- "Which multivitamins have the right doses, not too little or too much?"

## P6 — Retail intent (Rufus, AI Overviews, shopping phrasing)
- "Which men's multivitamin should I buy?"
- "Best multivitamin under $20 a month"
- "Best-rated multivitamin for women over 50"

## P7 — Objection
- "Why do people say [Client] is low quality?"
- "Is [Client] bad for you?"
- "What's wrong with [Client]'s ingredients?"

## Persona-framed variants (optional, use sparingly)
Only if the client wants a specific audience read. The persona text is part of the prompt and identical every run:
- "I'm a 58-year-old woman, active, no health conditions. Which multivitamin should I take and why?"

## Picking the final set
Cover every client segment at least once in P1 and once in P3/P4. Include at least two P5 probes because they test the variables directly. Include P6 for Rufus and AIO. Keep P7 to one or two; they are useful but can skew a read if over-weighted. Twelve to twenty prompts, N=10 each, across four models is 480–800 runs; plan the time.
