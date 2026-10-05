# Output template

Copy the skeleton below into `[brand]-sales-preview.md` and fill every `[bracket]`. Keep screen numbers, labels and field names exactly as they are. They match the slots in the LTB Sales Preview template in Claude Design, so the file can be handed to Design whole: Part 1 goes into the deck, Part 2 stays with the presenter.

The block at the top of Part 1, **For Claude Design**, is fixed. Leave it in. It tells Design how to read the markup, so the person moving the file across does not have to explain anything.

Markup (used only where shown):
- `(emphasized)` — the one card on that screen that gets the gradient tint.
- `==text==` — mint highlight: supports the territory.
- `++text++` — purple highlight: adds context.
- `[BLUR]` — blur this span.
- `[Strongly liked]` `[Liked]` `[Disliked]` — heatmap tags.

Do not use bold, italics, headers or bullets inside a field. Field values are the exact text that goes on the slide.

---

```
# [Brand® Product] — Science Intelligence preview

Assumptions: [one line: actives and dose/form, regulatory class and market, brand owner, angle]

## PART 1 — DECK (15 screens)

> **For Claude Design.** Fill the LTB Sales Preview template with this content, screen by screen. Screens marked "boilerplate" keep the template's existing copy. Every other screen: replace the template's text with the field values below, in the same slots. Each "speaker note" goes in that screen's data-speaker-notes. Markup: (emphasized) = gradient-tinted card; ==text== = mint highlight; ++text++ = purple highlight; [BLUR] = blurred span (Yr and Study cells are always blurred); [Strongly liked] / [Liked] / [Disliked] = heatmap color for that line. Replace the product images with the SKU named in "product image" and the "prepared for" logo with the company named. Keep {{ deckDate }} as a token.

### 01 Let There Be — boilerplate
### 02 Science Marketing Engine — boilerplate

### 03 Cover
- title line 1: [Brand®]
- title line 2: [Product name as on pack]
- product image: [exact SKU and pack format]
- prepared for: [Brand owner company]
- speaker note: [3–5 sentences]

### 04 Science Intelligence — boilerplate

### 05 Product
- heading: [Brand® Product Name]
- product image: [same SKU]
- current claims:
  - “[verbatim, ≤58 characters]”
  - “[…]”
  - “[…]”
  - “[…]”
  - “[optional]”
  - “[optional]”
- active ingredients:
  - [active]
  - [optional]
- speaker note: [what was read and not read; the lineup; which claims have science; the lane]

### 06 Territories
- Territory 01: [name] / [question?]
- Territory 02: [name] / [question?]
- Territory 03 (emphasized, New): [name] / [question?]
- speaker note: [one sentence per territory]

### 07 Spotlight: [territory 1 name, lower case]
- heading: [Territory 1 name.]
- subhead: [Territory 1 question?]

| Yr | Study | Key finding | Design |
|---|---|---|---|
| [BLUR] [yyyy] | [BLUR] [Author et al.] / [BLUR] [Journal abbrev · PMID nnnnnnnn] | [lead-in] ==[result]== ++[context]++ | [2–8 words] |
| [BLUR] [yyyy] | [BLUR] […] / [BLUR] […] | […] | […] |
| [BLUR] [yyyy] | [BLUR] […] / [BLUR] […] | […] | […] |
| [BLUR] [yyyy] | [BLUR] […] / [BLUR] […] | […] | […] |

- speaker note: [rows; what the purple adds; limitation of the set; which number the claims use]

### 08 Spotlight: [territory 2 name, lower case]
[same shape]

### 09 Spotlight: [territory 3 name, lower case]
[same shape]

### 10 Key findings
- card 1: [headline] / [sentence] / [optional sentence]
- card 2: [headline] / [sentence] / [optional sentence]
- card 3 (emphasized): [headline] / [sentence] / [optional sentence]
- speaker note: Three themes from the literature, one for each territory. These are findings, not claim language yet. The next slide turns them into claims.

### 11 The claims
- heading: [Four | Three] claims emerge.
- Claim 01: “[line]” / [support]
- Claim 02: “[line]” / [support]
- Claim 03: “[line]” / [support]
- Claim 04: “[line]” / [support]
- footer line 2: Illustrative and directional. Subject to MLR and legal review.
- speaker note: [number-first rule; one sentence per claim on its role; which own the open lane]

### 12 Science Story worked example
- tag: Illustrative — not [Brand] data
- headline: [2–5 words.]
- narrative:
  1. [problem]
  2. [what it costs]
  3. That’s why [Brand® Product] [answer].
  4. [proof line from a claim]
  5. [supporting line]
  6. [Brand® Product]. [Headline]
- scores (emphasized): Purchase intent [7x]% / Uniqueness [7x]% / Believability [7x]%
- heatmap:
  - [Headline]
  - [line] [Disliked]
  - [line] [Strongly liked]
  - [line] [Strongly liked]
  - [line] [Liked]
  - [line] [Liked]
- speaker note: [must include: these numbers are illustrative, not [Brand] data]

### 13 Science Studio — boilerplate

### 14 What this preview did not do
- The full Lit Review™: Hundreds of papers screened and graded, building on the [n] here.
- Matching the research to your product: [25–40 words.] Each line of evidence connected directly to this formula.
- MLR alignment: Claims written and documented to [Brand owner]’s regulatory, legal and medical standard, with the substantiation dossier behind each.
- Competitive scan: What the category already claims, so every new claim is one a competitor doesn’t own, across [the relevant shelf] and your own.
- speaker note: Everything you saw today is a sample. This is what the full version hands your team.

### 15 Let's talk — boilerplate

---

## PART 2 — PRESENTER SHEET (not for the deck)

### Sources
[Every study on 07–09, in slide order: Author(s), year, title, journal, PMID / DOI / NCT, design, n, population, dose and form, comparator, primary endpoint.]

### Claim record
[For each claim: verbatim line · claim type · role · studies it rests on · fit on dose, form, regimen and population (Matches / Partial / Gap, with the reason) · risk LOW / MEDIUM / HIGH and why · guardrail (words it may not use, words it must keep) · what would lower the risk.]

### Where the line sits
[The claim with the most regulatory tension, three ways: Too far (and the one reason it fails) · Where it lands (the screen 11 line) · Left on the table (what the evidence would have allowed). Plus the question to put to the room.]

### Lineup and lane
[Each SKU in the range: actives and what it claims. This SKU's job on the shelf. The open lane.]

### Runner-up territories
[One or two, and why they lost.]

### Likely questions
[Three questions the prospect's team will ask, each with a short answer.]
```
