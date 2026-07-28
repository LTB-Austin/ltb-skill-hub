# Layout Spec — measured from the Zegerid Art Styles & Scripts v1 deck

All coordinates in inches. Slide size: **10.0 × 5.625 (16:9)**. Background `#f0f0f0`. Always read this file before building slides.

## Global elements

| Element | Spec |
|---------|------|
| LTB wordmark | left-aligned logo png, x=0.13, y=5.19, w=1.33, h=0.31 — bottom-left of EVERY slide |
| Dividing line (content slides) | x=0.74, y=0.88, w=8.52, black, 2.25pt |
| Slide title (content slides) | textbox x=0.64, y=0.21, w=6.72, h=0.71 — Lexend Bold 30pt, black, left |
| Body textbox | x=0.74, y≈1.00–1.10, w=8.52 — Lexend ExtraLight (use "Lexend Light" if ExtraLight unavailable), black, left. Blank line between paragraphs |
| Mitosis blobs | 4.17×4.17 (corner deco) or 3.93×3.93, bleeding off-slide. Positions used: top-left (-1.5,-1.7), bottom-left (-1.9,3.4 / -2.3,-2.0 top), bottom-right (7.7,3.2 / 8.0,3.3), top-right (7.2,-2.3), (6.6,-2.2) |

## Slide recipes

### Title slide & Section dividers ("Art Styles", "Scripts")
Centered composition:
- Client logo: x=2.96, y=1.97, w=4.08 (height by aspect, ≈1.51)
- Line: x=2.88, y=3.64, w=4.25, 1.5pt black
- Title: textbox x=3.48, y=4.12, w=3.03 — Lexend Bold ~40.8pt, centered
- Mitosis: top-left (-1.53,-1.67, 4.17) and bottom-right (7.81,3.11, 3.93)
- LTB wordmark bottom-left

### Agenda ("What We'll Do Today")
- Title + line per global spec
- Body: x=0.74, y=1.51, w=8.52, h=2.81 — numbered items, 18pt; label runs Lexend Bold, descriptions Lexend ExtraLight, all black
- Mitosis: bottom-left (-1.91,3.36) and bottom-right (7.69,3.23), both 4.17

### Style divider ("Art Style #n - Name")
- Title: textbox x=0.24, y=2.11, w=8.64, h=1.21 — "Art Style #n " Lexend Bold 30pt + "- Name" Lexend ExtraLight 30pt, left
- Line: x=0.30, y=2.91, w=8.52, 2.25pt
- Mitosis: top-right bleeding (6.61,-2.15, 3.93)

### Brief / Style Details
- Title ("Brief" / "Style Details") + line per global spec
- Body: x=0.74, y=1.10, w=8.52, h up to ~4.1 — Lexend ExtraLight 13pt, 3–5 paragraphs
- Mitosis: Brief → bottom-right (8.01,3.32, 4.17); Style Details → top-right (7.17,-2.31, 4.17)

### Inspiration (placeholder grid)
No title, no dividing line. Style-name chip image/text top-center (x≈3.5, y=0.07, w=3.03, h=0.64) optional.
- Top row: 3 frames, y=0.80–0.93, h≈1.93–2.11; widths 2.0–3.4 varying, gutters ≈0.1–0.5; row spans x≈0.4 → 9.7
- Captions under top row: y=2.85–2.89, h=0.22 — Lexend ExtraLight 10pt, centered, width matching frame
- Bottom row: 2 frames, y=3.21–3.34, h≈1.62–1.93, centered-ish (e.g., x=1.98 and x=4.99, w≈2.9–3.0)
- Captions under bottom row: y≈4.92–5.08
- LTB wordmark bottom-left; no mitosis blob

### MOA Moment
- Line per global spec (no separate title textbox — the lead sentence acts as it)
- Text column: x=0.74, y=1.00, w=5.01, h≈4.2 — Lexend ExtraLight 11–13pt: "The key MOA moment happens in N parts:" then numbered paragraphs, then a closing craft sentence
- Client logo small top-left above line: x=0.43, y=-0.14, w=1.98, h=1.35 (optional)
- Right images/frames: two stacked, x≈6.3–6.6, w≈2.8–3.0, h≈1.5–1.7; first y≈1.1–1.4, second y≈3.1–3.4
- Captions beneath each: w=3.54, h=0.22, centered, 10pt
- Mitosis: top-left bleeding (-2.30,-2.03, 4.17) and bottom-right (7.74,3.60, 3.93)

### Summary
- Title "Summary" + line per global spec
- Three frames 4.00×2.25 with 0.75pt borders, staggered: #1 (1.00,1.01), #2 (5.00,1.01), #3 (3.00,3.25)
- Number badge at each frame's top-left corner: white circle 0.47×0.47 at (frame.x-0.04, frame.y-0.06), digit Lexend Bold 25pt black overlapping
- Mitosis: top-right (7.17,-2.31, 4.17)

### Script slides
- Title = script label + length ("Ad - 15 seconds") per global spec
- Body: x=0.74, y=1.10, w=8.52 — Lexend ExtraLight 12pt, verbatim script, blank lines between lines/beats; "Approx Ns" and asterisked alternates/disclaimers at the end
- Mitosis: one or two corners (e.g., bottom-right 8.01,3.32 or top-left + bottom-right)

### Next Steps
- Title 27pt + line per global spec
- Body: x=0.74, y=1.51, w=8.52 — 18pt; bold labels ("Update Art Style: ") + ExtraLight descriptions; sub-bullets ExtraLight
- Small mitosis bottom-left (0.12,4.46, 1.04) behind/above wordmark

## Placeholder frame style
For every image Austin will drop in later: a rectangle at the exact PIC geometry above, fill white (`#FFFFFF`), border 0.75pt `#BFBFBF`, containing centered placeholder text in Lexend ExtraLight 9pt gray `#999999` (e.g., "DROP IMAGE — heartburn visual"). Caption textbox below per spec. Frames must be plain shapes (easy to delete/replace in PowerPoint).
