# Sales preview — the deck

This file mirrors the **LTB Sales Preview template** in Claude Design (the Banana Boat Mineral Lotion SPF 50 build is the reference). The template has **15 screens**. Each screen lists its slots in the order they appear on the slide, with the template's own field names, so the brief drops into Design field by field.

Each screen is marked:

- **BOILERPLATE** — the template already holds this copy. Do not write it into the brief; list the screen by label only. It is reproduced here so you know what the deck says around your content.
- **SEMI** — fixed frame and labels, variable content inside.
- **VARIABLE** — written for this product.

**Structure is fixed at three territories.** Three territory cards, three spotlight screens, three key-finding cards. Do not build two or four.

**Screen labels.** Use the `data-screen-label` exactly as written below. The three spotlight labels take the territory name in lower case: `07 Spotlight: full protection, one mineral`.

**Footer.** Screens 05–14 carry `Preview · directional · findings not validated · sources masked until the full Lit Review™`. Screen 11 adds a second line. The template renders the footer and page number; do not write them into the brief except screen 11's second line.

**Speaker notes.** Every screen has one; the template stores them as `data-speaker-notes`. Three to five plain sentences, written as a talk track for a presenter walking a prospect's team through the deck live, often with regulatory or medical people in the room. Limitations of the evidence live in the spotlight speaker notes.

**Emphasis.** Exactly one gradient-tinted card on screens 06, 10 and 12, marked `(emphasized)` in the brief. Mint and purple highlights appear only in spotlight tables. Heatmap colors appear only on 12.

**Length.** Counts below come from the reference build. Staying inside them keeps the layout from breaking. Slots marked *one line* sit on a single line with no wrap.

---

## 01 Let There Be — BOILERPLATE

Title card. `Science leads. Creativity amplifies.`
Speaker note: Title card.

## 02 Science Marketing Engine — BOILERPLATE

What we do · Science Marketing Engine™ · "One operating model, three phases — from the evidence to content in market."
- Phase 01 · Prove — Science Intelligence™ — AI-powered Lit Review™ and Claim Dev™ uncover what your product's science genuinely supports. (Lit Review™ · Claim Dev™ · Science Index™)
- Phase 02 · Persuade — Science Story™ — Verified claims become clear, tested creative concepts that move consumers and HCPs. Persuadable Research™ · Consumer + HCP Testing
- Phase 03 · Produce — Science Studio™ — Content that converts — video, social and education, built to be recut and reused. (MOA Moment™ · Ad-to-Education Sequence™ · Science Carousel™)

Speaker note: One operating model, three phases. Proof with Science Intelligence, persuade with Science Story, produce with Science Studio. Everything in this preview sits inside phase one.

## 03 Cover — VARIABLE

- **eyebrow:** Science Intelligence™ logo | Preview *(fixed)*
- **title line 1:** Brand®, with the registered or trademark symbol as the brand uses it.
- **title line 2:** the product name as it reads on pack, e.g. `Mineral Lotion SPF 50`. Two lines total at 62px; keep line 2 under about 26 characters.
- **product image:** name the exact SKU and pack format so Design can source it. Design places it in the blob frame.
- **prepared for:** the brand owner company (e.g. Edgewell Personal Care). Design places its logo.
- **date:** `{{ deckDate }}` *(fixed token; Design fills it)*
- **speaker note:** Name the product, its regulatory class and its active(s). State the question the deck asks, the way a brand team would ask it ("what does this SKU do that the rest of the shelf doesn't?"). Say it was built from public science and public claims only, so every finding is directional.

There is no subtitle on this cover. The question lives in the speaker note.

## 04 Science Intelligence — BOILERPLATE

What we do · Science Intelligence™
- Lit Review™ — Directed searching and screening of the published science on your actives, graded by design, direction and fit to your product.
- Claim Dev™ — Claims written from that evidence and scoped to your regulatory class. Each one carries its proof, its risk and the words it may not use.
- Muted line: Science Intelligence™ is the first phase of the Science Marketing Engine™.

Speaker note: This is the part of our work we want to show you today. We read the science, and we write the claims from it, and we keep the two attached. Everything that follows is a short version of that on one product.

## 05 Product — SEMI

- **eyebrow:** Science Intelligence™ logo | Preview *(fixed)*
- **heading:** the full product name on one line: `Brand® Product Name` (e.g. `Banana Boat® Mineral Lotion SPF 50`). Under about 40 characters so it sits on one line at 44px.
- **product image:** same SKU as the cover.
- **current claims label:** CURRENT CLAIMS FROM LABEL AND SITE *(fixed)*
- **current claims:** four to six of the brand's claims, verbatim from pack or site, in curly quotes. Each is a pill that cannot wrap, so each must be **58 characters or fewer** including quotes. Keep the brand's own punctuation and asterisks. If a claim is longer, pick a shorter one; do not paraphrase a verbatim claim.
- **active ingredients label:** Active ingredients *(fixed)*
- **active ingredients:** one pill per active, as named on Drug Facts or Supplement Facts, no doses (`Zinc oxide`). Up to six pills. For a long formula, group the way the brand does (`Lutein + zeaxanthin`, `8 B vitamins`).
- **speaker note:** Say what was read (the public research on the actives, the retail listing including Drug Facts or Supplement Facts, the rest of the lineup) and what was not (no brand documents, no prior claim work, no conversations with the team). Walk the lineup: which actives each SKU runs and what each claims. Name which current claims already have science behind them. End on the lane this SKU can own.

The lineup analysis has no slide of its own. It lives in this speaker note and on the presenter sheet.

## 06 Territories — VARIABLE

- **eyebrow:** Science Intelligence™ logo | Lit Review™ logo *(fixed)*
- **heading:** The territories we explored. *(fixed; no subhead)*
- **three cards**, labeled `Territory 01`–`Territory 03`, in the order the spotlights run. Each has:
  - **name:** 3–5 words, no period. Fits in two lines at 28px. ("Full protection, one mineral")
  - **question:** the one question the territory asks, 6–12 words, ending in a question mark. ("Does blending in change how much sunscreen people put on?")
- Territory 03 is the new territory: it carries the `New` pill and is **(emphasized)**. Territories 01 and 02 sit behind claims the brand already makes and carry no tag.
- **speaker note:** One sentence per territory on why it matters: which is least exposed, which has the cleanest evidence, which is the open lane.

## 07–09 Spotlight — VARIABLE (one screen per territory)

- **label:** `07 Spotlight: [territory 1 name, lower case]`, then 08, 09.
- **eyebrow:** Science Intelligence™ logo | Lit Review™ logo | Spotlight studies · legend: mint `Supports the territory` · purple `Adds context` *(fixed)*
- **heading:** the territory name from screen 06, with a period.
- **subhead:** the territory question from screen 06, verbatim.
- **table, exactly four rows.** Columns `Yr` · `Study` · `Key finding` · `Design`:
  - **Yr:** publication year. *Blurred.*
  - **Study:** two lines, both *blurred*. Line 1 `Author et al.` (or `Author & Author`). Line 2 `Journal abbreviation · PMID nnnnnnnn`, adding ` · NCTnnnnnnnn` when a trial registration exists.
  - **Key finding**, up to three parts, 15–35 words in total:
    1. **lead-in (optional, plain):** the setup, 2–8 words, usually the population or n. "Of 65 top-rated sunscreens online,"
    2. **mint:** the result with its number, 6–16 words. "26 missed at least one dermatology basic: broad spectrum, SPF 30+, water resistant."
    3. **purple (optional):** one sentence a reviewer would raise: a competing ingredient that also performs, or a limit on who the result covers. One or two purple lines per screen, never four.
    A row may also end with a short plain sentence after the mint (Beleznay: "Fragrance and preservatives caused more.").
  - **Design:** 2–8 words: study type plus the first thing a reviewer checks. "Randomized; 5 mineral, 1 organic sunscreen." "In vitro, excised human epidermis." "Prospective multicenter photopatch study."
- Order rows to build the argument: mechanism or strongest design first, the number the claims will use last or clearly marked in the note.
- No evidence note on the slide. The limitation of the set goes in the speaker note.
- **speaker note:** Walk the rows in one sentence each (group two rows that make the same point). Say what the purple line adds. Name the limitation of the set. Say which row's number the claims will use.

## 10 Key findings — VARIABLE

- **eyebrow:** Science Intelligence™ logo | Lit Review™ logo *(fixed)*
- **heading:** Key findings from the literature. *(fixed)*
- **three cards**, one per territory, in territory order:
  - **headline:** 3–8 words, a finding you could say out loud. It may lead with the number ("40% of top sunscreens are missing a key feature"; "No allergic reactions").
  - **body:** one or two sentences, each its own line, 6–25 words each. The number a reader would repeat.
  - Card 3 (the new territory) is **(emphasized)**.
- These are **evidence statements, not claims** (copy-craft.md §6). No product name on this screen. Every number must appear in a spotlight row.
- **speaker note:** Three themes from the literature, one for each territory. These are findings, not claim language yet. The next slide turns them into claims.

## 11 The claims — VARIABLE

- **eyebrow:** Science Intelligence™ logo | Claim Dev™ logo *(fixed)*
- **heading:** `Four claims emerge.` (or `Three claims emerge.` if the evidence only carries three)
- **one card per claim**, `Claim 01`–`Claim 04`, none emphasized:
  - **claim line:** in curly quotes, one to three short sentences (copy-craft.md §1: ≤12 words a sentence). Lead with the number or finding, then let the product arrive in its **own** sentence, so a category statistic never reads as a product result. A short line can stand alone ("4 in 10 top sunscreens miss a basic."); the support sentence then names the product.
  - **support:** one or two sentences, 10–30 words, plain, readable with citations blurred. The evidence the line rests on.
- **footer line 2:** `Illustrative and directional. Subject to MLR and legal review.`
- **speaker note:** Say that each claim leads with the number and lets the product arrive in its own sentence. One sentence on the role each plays (the category gap, the population, the behavior, the formula). Say which claims own the open lane.

## 12 Science Story worked example — VARIABLE

A preview of the next phase. Everything on it is illustrative.

- **eyebrow:** Science Story™ logo | Worked example *(fixed)* · **tag:** `Illustrative — not [Brand] data`
- **headline:** 2–5 words, the story's promise. "Built to blend."
- **narrative:** six lines, each a sentence or two:
  1. The problem the shopper has.
  2. What the problem costs them.
  3. `That’s why [Brand® Product] …` — the product's answer.
  4. The proof line, reusing a claim from screen 11.
  5. A supporting line from the formula or another claim.
  6. Sign-off: `[Brand® Product]. [Headline]`
- **scores (emphasized):** label `Tested with 200–300 real consumers` *(fixed)*, then **Purchase intent**, **Uniqueness**, **Believability** as illustrative whole percentages in the 70s (reference: 74, 79, 77). Never presented as brand data.
- **heatmap:** label `Claims heatmap` *(fixed)*. The headline again, then five short lines (≤14 words each) condensed from the narrative, each tagged `Strongly liked`, `Liked` or `Disliked`. Pattern from the reference: the problem line `Disliked`; the cost and the product answer `Strongly liked`; proof and formula lines `Liked`.
- **speaker note:** This is what the next phase looks like. We take the claims you just saw and build them into one story: [headline, lower case]. Then we test it with 200 to 300 real consumers for purchase intent, uniqueness and believability, plus a line-by-line heatmap of what they liked and didn't. These numbers are illustrative, not [Brand] data.

The story reuses claim language. It adds no new claims and no new numbers.

## 13 Science Studio — BOILERPLATE

Science Studio™ · "From Science Story to screen."
Four films: Centrum® — Memory support, as you age. · Cheers — DHM at the GABAa receptor. · Qunol® — Absorption, by phospholipid micelle. · A+D® — A non-toxic, natural cleanser.
Four results: +158% purchase volume · Cheers · 685.2M TV impressions · Qunol® · +133% ROAS · Nexium 24HR® · +29% sales in two months · Lotrimin®

Speaker note: Then it gets made. The same citation sits under the claim, the narrative and the film. Four mechanism films from our studio — Centrum, Cheers, Qunol, A+D.

If the prospect is one of the four featured brands or a direct competitor of one, flag it in the handback so the team can decide whether to swap a film. Do not change the screen yourself.

## 14 What this preview did not do — SEMI

- **eyebrow:** Preview vs full engagement *(fixed)*
- **heading:** What the full engagement adds. *(fixed)*
- **left column, four blocks** (labels fixed, text product-specific):
  - **The full Lit Review™** — `Hundreds of papers screened and graded, building on the [n] here.` `[n]` is the number of studies on 07–09 (normally 12).
  - **Matching the research to your product** — 25–40 words naming the specific files the full run would check this formula against: the labeled dose or percentage, the product's own test data, the file behind any "dermatologist tested" or similar claim. End with `Each line of evidence connected directly to this formula.`
  - **MLR alignment** — `Claims written and documented to [Brand owner]’s regulatory, legal and medical standard, with the substantiation dossier behind each.`
  - **Competitive scan** — `What the category already claims, so every new claim is one a competitor doesn’t own, across [the relevant shelf] and your own.`
- **right column** *(BOILERPLATE)*: The full Science Intelligence™ engagement · Lit Review™: The complete evidence workbook: every study extracted, graded by design and direction, and matched to your label. · Claim Dev™: An MLR-ready claim set, every claim written three ways (consumer, HCP, MLR), each with its proof, risk and guardrail attached.
- **speaker note:** Everything you saw today is a sample. This is what the full version hands your team.

## 15 Let's talk — BOILERPLATE

Let's unlock your scientific potential. · Alex Gelbert · Founder & CEO · alex@lettherebe.com · Connect on LinkedIn ↗ · lettherebe.com

Speaker note: Close and take questions. Alex founded Let There Be and directs how the Science Intelligence and Science Story tools are applied for consumer health clients.

If someone else presents, swap the name and contact only when asked.

---

## Source masking

The prospect must see the science is real without being able to go read it. Blur **identifiers**, never substance. The template already blurs the `Yr` and `Study` cells. If anything else carries an author, year, journal or identifier, mark it `[BLUR]` and Design applies `filter: blur(4.5px); user-select: none` to that span only.

**Blurred:** publication years, author names, journal names, every PMID, DOI and NCT, and any author-year citation anywhere on a slide.

**Never blurred:** findings, n, designs, findings cards, claim lines, the story, and everything on boilerplate screens.

Because identifiers are blurred, every finding sentence must stand on its own. Never write "as Cole et al. showed."

The presenter sheet carries every identifier in full.

## Rules

- 15 screens, in this order, labels as written. Three territories, four studies per spotlight, three key-finding cards, three or four claims, one worked example.
- Boilerplate screens listed by label only, never rewritten.
- The worked example is labeled illustrative on the slide and in the note. No other screen carries scores.
- No prices anywhere.
