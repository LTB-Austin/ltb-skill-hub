# Capturing live pages with Claude in Chrome

Activation screens are built on what the brand actually runs today. Capture it yourself rather than asking the client to send screenshots — it's faster and you get the whole page, in order.

## What to capture

For each SKU in scope:

- **Amazon PDP** — title, bullets, description, the full image carousel (every image, in order), A+ / "From the manufacturer" modules top to bottom, and the references block.
- **Amazon Brand Store** — the category page for this product line: hero, every band, the product grid, the footer.
- **DTC site PDP** — if the client sells direct.
- **Retailer pages** — only if the client flagged one.
- **Competitors** — capture only what you'll actually put on a context screen. One competitor's recent launch, a few frames of a social carousel. Label it "shown for reference."

## Don't screenshot product imagery — pull the source files

Product images and A+ modules on a retail page are flat image files on a CDN, usually 1500px or wider. Screenshotting them through a browser window gives you a downscaled copy with page furniture around it that someone then has to crop, and the result looks exactly as bad as it sounds in a deck. Extract the URLs instead and download the originals.

On an Amazon PDP, the carousel lives in a `colorImages` object inside a page script, each image with `hiRes` and `large` variants. A+ modules are `<img>` elements under `#aplus` / `#aplus_feature_div`. Run javascript_tool against the loaded page:

```js
// carousel, hi-res, in page order
const s=[...document.querySelectorAll('script')].map(x=>x.textContent).join('\n');
const m=s.match(/'colorImages':[\s\S]*?'colorToAsin'/);
let hi = m ? [...m[0].matchAll(/"hiRes":"(https:[^"]+)"/g)].map(x=>x[1]) : [];
if (!hi.length && m) hi = [...m[0].matchAll(/"large":"(https:[^"]+)"/g)].map(x=>x[1]);

// A+ modules — strip Amazon's crop/resize suffix to get the original
const ap=[...new Set([...document.querySelectorAll('#aplus img, #aplus_feature_div img, .aplus-module img')]
  .map(i=>i.getAttribute('data-src')||i.src).filter(u=>u&&u.startsWith('http')))]
  .map(u=>u.replace(/\.__CR[^.]*\.jpg/,'.jpg'))
  .filter(u=>!/__AC_SR/.test(u));   // __AC_SR = comparison-table thumbnails, not modules
```

Then hand the user a shell script of `curl` calls that downloads everything into a folder tree named by SKU and numbered in live page order (`ib-carousel-03.jpg`). Browser tools run on the user's machine, outside your container, so you cannot download these yourself or attach them — the script is the deliverable.

**Compare the file names across SKUs before writing anything.** Identical URLs on two listings mean the same asset is serving two products. That is a finding, and it's provable from a file hash rather than an opinion: if two products have different arguments and half the same images, the differentiation problem is literally in the asset list. The same check on A+ modules shows how much of a page is brand boilerplate versus product-specific.

Screenshots are still right for things that are genuinely page *layout* rather than imagery: a Brand Store hero, a nav bar, a module carousel, a page region you are annotating as a whole. Crop to the module, never the whole browser window.

## How to run it

1. Navigate to the page and let it fully load before the first screenshot.
2. Decline cookie and consent banners (choose the most privacy-preserving option) so they don't sit in the captures.
3. Expand anything collapsed — "See more" on the description, the full image carousel, A+ modules that lazy-load.
4. Screenshot **module by module, in page order**, not one giant capture. Each module becomes one annotated block in the deck.
5. For the image carousel, step through every image and capture each one separately. They get numbered 1–n in the deck and the numbering must match the live order.
6. Pull the page **text** too (get_page_text), not just pixels — you need the exact current title, bullets and description to write the CURRENT column verbatim.

## Naming and handoff

Save captures with names that survive the handoff to Claude Design:

```
<brand>-<sku>-pdp-image-03.png
<brand>-<sku>-aplus-module-02.png
<brand>-brandstore-hero.png
<competitor>-social-frame-01.png
```

Tell Claude Design which capture belongs on which screen. The deck references them by number; the files carry the same numbers.

## Annotating

Every captured module gets one of these verdicts, and never a blanket rewrite:

| Verdict | Use when |
|---|---|
| **KEEP** | In-market and still right. Say so — the client needs to see what you're not touching. |
| **KEEP · ADD ONE LINE** | The module works; the theme line goes above it. |
| **CHANGE COPY** | Body text moves to the new story; headline and structure stay. |
| **CHANGE HEADLINE** | The image is fine; the headline carries the new claim. |
| **CHANGE ONE ROW** | A single row or tile inside a multi-part module. Be specific about which. |
| **REPLACE** | The tile carries a claim we're retiring or a visual that breaks a guardrail. |
| **ADD · NEW** | New module or image. Say where it sits in the stack and what it shows. |
| **SUPPRESSED** | The module isn't rendering on the live page, though the copy exists in the feed. Not a copy verdict — a platform flag for the client's retail team. See the suppression note in `activation-types.md`. |

Each annotation gets: the verdict, one or two sentences of reason, and the claim ID(s). Where a visual currently implies something the claims don't support, say that explicitly — it's the most valuable thing on the screen.

## Boundaries

Read-only. Don't log in to the client's seller account, don't submit forms, don't change anything on a live page. If the user wants a change pushed, that's theirs to do.
