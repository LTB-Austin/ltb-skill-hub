# Science Intelligence™ Presentation — Direction-First Structure (default)

The reference build is the Jocko Fuel Science Intelligence deck (Oct 2026), which is also the **LTB Template — Science Intelligence (Lit Review + Claim Dev)**. Its slide ids are given in brackets so the build step can match each screen to its template slide. The output is one markdown content brief plus CSVs, built into that template in the same run. Slides are 16:9 with one idea per slide, and tiles and cards sit on `#f0f0f0`. Headlines stay on one line.

## Flow

### Front matter

1. **Cover** [`s01-cover`]: "[Product]® Claims", the SCIENCE INTELLIGENCE™ PRESENTATION lockup, the prepared-for line, and the month and year.
2. **The Goal** [`s02-the-goal`]: on the left, the business goal as one large statement under the eyebrow THE GOAL. On the right, a card with three numbered rows (`01 THE GAP`, `02 THE OPENING`, `03 OUR BRIEF`), each 1–2 sentences.
3. **Where We Looked** [`s04-where-we-looked`]: three big-number tiles (for example studies or sources mapped, labels captured, official sources read in full), each with a 2–3 sentence explanation. Along the bottom, a "RISK AREAS WE EXPLORED" strip: 5–6 columns, each a bold label plus one line.
4. **The Highlights** [`s05-the-highlights`]: the `LIT REVIEW™ | CLAIM DEV™ | Results` lockup, then the list of directions by ID and name, grouped by part (one column per product when there are two).
5. **How each direction runs** [`s06-how-each-direction-runs`]: four cards:
   - `01 The claim`: For the brand team · The hero line · Why it matters to [Brand]
   - `02 Supporting claims`: For the brand team · Other ways to say the hero claim · Each linked to its dossier page
   - `03 The evidence`: For legal and the brand · Labels and studies · Each card linked to its source
   - `04 Compliance logic`: For legal · Why it holds · What it must not say · What's still open

   Then the "Tags open the dossier" example pills, and the Core / Push / Stretch risk legend with [Brand] filled in.

### Results, by part

When the scope covers more than one product:

- **Part divider** [`s07-part-a-divider`, `s26-part-b-divider`]: the part letter, the product name, and one sentence on what the part covers.

**Per direction** (repeat for every direction). Every slide carries the same header row:
- a black pill naming the part (Hero claim / Supporting claims / The evidence / Compliance logic);
- four progress dots, with the current part active;
- `Direction [ID]`;
- and at the right, the product's colored marker with the product name.

The heading is the direction name, identical on all four slides.

- **The Claim** [`s08-a1-the-claim`]:
  - Left, the gradient hero card:
    - eyebrow `The claim · [ID]` with its tier marker;
    - the hero claim in curly quotes, large;
    - `Speaks to`: who the line is for;
    - `Carries`: chips, from Study, Survey, Label, Comparative;
    - a `Substantiation: [ID] · Dossier p. [n]` pill.
  - Right, `Why this matters to [Brand]`: 2–3 sentences tying the claim to the brief.
- **Supporting Claims** [`s09-a1-supporting-claims`]:
  - 3–4 cards in a 2×2 grid. Each card has a register tag, a tier marker, the claim ID at the right, the line in curly quotes, a `Carries` row and a substantiation pill.
  - Under the grid, a summary pill, e.g. "14 carrageenan lines across 7 brands in the library · Workbook tab: [tab] (filter: [term])".
- **The Evidence** [`s10-a1-the-evidence`]:
  - Left, the gradient hero data tile: an eyebrow (source type and date), a big number, a one-line meaning, and a source pill.
  - Right, `The science`: 1–2 cards, each a finding, a design line (design · n · population · journal year), a source pill, and an optional regulator badge (e.g. `EFSA`).
  - Bottom, `The honest line`: the counter-evidence in 1–2 sentences, its design line, an `Abstract only` flag where true, and a source pill.
  - When the number needs walking through, add extra evidence slides titled `The Evidence 2 · [short title]` [e.g. `s22`, `s23`, `s33`–`s35`]. Use them for a comparison table, label-by-label facts, or the math behind a derived number.
- **(Optional) On the pack** [e.g. `s39-b3-on-the-pack`]: when the claim rests on what the client's own label or ingredient list says.
- **Compliance Logic** [`s11-a1-compliance-logic`]:
  - six tiles in a 3×2 grid, each a bold title of ≤ 30 characters plus 1–2 sentences;
  - then a `Risk` line, e.g. `CG1, CG2 medium · CG3 low · CG5 high`;
  - then a `Depth` line, e.g. `Label fact · Full text verified (science lines)`.

  Cover these:
  - it's on their label, or already approved;
  - the attribute first and the science second;
  - pairing a name with a health effect makes it HIGH;
  - say what the trial found;
  - what's unknown, such as dose;
  - expect the comeback.

**Part library** [`s25-the-shake-library`, `s43-the-powder-library`]: after each part's directions, give the count of claims in the library, a ranked list (for example, competitor ingredients the client's product doesn't have), "Also in the library" lines, and a "Where to find it" card naming the workbook tabs.

### Close

- **The full library** [`s44-the-full-library`]: totals across every part.
- **New audiences** [`s45-new-audiences`] *(optional)*: a potential future audience (HCPs, or a population the claims don't yet cover). Four numbered evidence cards, then a black bar headed "Why it's not a claim yet", with a candidate line marked for discussion only.
- **Your legacy claims, strengthened** *(optional, whenever the client's approved claims are known)*: rows of legacy line → strengthened line → direction pill. Use the closest table layout and tell the user which one you used.
- **What happens next** [`s47-what-happens-next`]: owner-tagged steps (CLIENT / LET THERE BE / CLIENT MLR): feedback → revise directions → MLR direction check → build claims → MLR claim review → (claims testing if planned) → Science Story™.
- **Closing** [`s48-closing`]: "Science leads. / Creativity amplifies." on two lines.
- **Where the evidence stops** [`s46-where-the-evidence-stops`]: what the evidence won't support. It's the credibility of the method.

### Appendix

- **Index** [`s49-appendix`].
- **How to check any claim** [`s50-how-to-check-any-claim`]: how to go from a claim's ID to its substantiation and its sources.
- **B. Sources** [`s51`–`s58`]: 10 per slide, as `# | STUDY ID (S-001) | CITATION` with PMID or DOI. Supply this as `Appendix_B_sources.csv`.
- **C. Label capture** [`s59`–`s63`]: `ID (L-001) | Product/source | Ingredient or fact used | Marketer | captured date`.
- **D. Regulatory notes** [`s64`] and **Disclaimers and footnotes** [`s65`]: the class identity and a class-safe flag per element, then the required disclaimers per SKU and per claim type, plus the working-language footer.
- **E. Claim index** [`s66`–`s69`]: every claim ID with its direction, tier, risk and substantiation page.
- **F. Label facts to confirm** [`s70`]: every label fact the claims rely on that the client should confirm before MLR.

## Copy rules for this format

- Hero claims and supporting claims may be punchier than deck copy. Everything else follows the plain voice.
- Every tile is self-contained: a title plus 1–2 sentences. No paragraphs on direction slides.
- Every number on a slide carries its source ID and evidence basis (full text, abstract, label or official page).
- Counter-evidence appears in "The honest line" on the evidence slide, and again in Compliance Logic.
- `Dossier p. [n]` pills appear only when a substantiation dossier exists. Otherwise the pill reads `Substantiation: [ID]` or `Source: S-0xx`.
- Part names, tier names and their order match the Sales Preview and SOW exactly.
