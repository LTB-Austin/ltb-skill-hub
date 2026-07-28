---
name: ltb-art-styles-scripts
description: "Build Art Styles & Scripts presentation decks for Let There Be Science Marketing. Use whenever the user wants to create, edit, or refine an Art Styles deck, a scripts presentation, or an 'Art Styles & Scripts' deck for any LTB client — even if they just say 'make the art styles deck for [client]' or provide style notes plus a scripts doc. Builds the full deck with labeled placeholder frames where imagery will be dropped in manually. Inputs: style notes, scripts document. Output is an unbranded content-first presentation for Claude Design (which brands and exports)."
---

# Skill: LTB Art Styles & Scripts Deck Builder

> **OUTPUT: an unbranded, content-first presentation.** Produce the deck as slide-by-slide copy + layout intent (including labeled placeholder frames for imagery) — **no LTB branding, no styling, no export.** We take this into **Claude Design**, which applies branding and exports. The brand references below are **intent notes for Claude Design**.

This deck presents 2–4 candidate art styles for a client's video project (typically an MOA video), plus the draft scripts. The client picks a style direction and gives script feedback.

**Key concept — placeholder frames:** Austin drops the actual artwork into the deck himself afterward in PowerPoint. You build every slide complete with text, captions, branding, and clean empty frames exactly where each image belongs. Do not ask for an images zip.

**Formatting authority:** This deck type has its own layout system, different from the project-overview deck. `references/layout-spec.md` contains exact measured geometry (positions, sizes, fonts, pt sizes) from the reference Zegerid deck — **read it before building any slides and follow it closely.** Where this file and project-overview habits conflict, layout-spec.md wins.

---

## PHASE 0: Inputs Checklist

- [ ] **Client/brand name** and product basics (what it is, the MOA in plain terms)
- [ ] **Art style notes** — Austin's notes per style: name (or ask/propose), the visual idea, what imagery he plans to drop in. Rough bullets are fine; you turn them into prose.
- [ ] **Scripts document** — final or near-final script text with labels and lengths ("Ad – 15 seconds"). Placed verbatim — never rewritten unless asked.
- [ ] **Brand Archive zip** — LTB logos + mitosis 1–4 images
- [ ] MOA part count per style if Austin specifies; otherwise derive from his notes/scripts

If scripts or style notes are missing, ask before proceeding. Missing client logo → leave a labeled placeholder frame for it too.

### What you write (all in LTB voice, drafted from Austin's notes + scripts)

- **Frame captions**: 2–5 words under each placeholder ("Heartburn visual", "Isolated stomach", "Closeup biology", "Product showcase"). Derive from the notes — what imagery belongs in that spot. Keep any "(SKETCH)" markers Austin flags.
- **Brief**: 3–5 paragraph-sentences describing the style's visual world — what the viewer sees, how the science/product is rendered, why it suits this brand.
- **MOA Moment narration**: "The key MOA moment happens in N parts:" + numbered visual beats grounded in the actual mechanism, + one closing craft sentence. Never invent mechanism claims.
- **Style Details**: tone words first ("calm, confident, and precise"), then focus, palette, voiceover character, and why it works for the brand.
- **Placeholder labels** inside frames: "DROP IMAGE — [caption]" in small gray text.

---

## PHASE 1: Brand System

- Background `#f0f0f0` on every slide; font **Lexend** (Bold for titles/labels, ExtraLight for body — fall back to Lexend Light if ExtraLight is unavailable); all text black. **No emojis. No corner chevrons.**
- LTB wordmark (left-aligned logo) bottom-left of every slide.
- Mitosis blobs: large, bleeding off corners, never blocking text/frames; vary image (1–4) and corner per slide; omit on inspiration grids.
- Client logo: title slide, section dividers, and small top-left on MOA slides (per layout spec). Placeholder frame if no logo file provided.
- Accent palette (sparingly — summary badges, agenda numbers if desired): Teal `#87CCCB`, Mint `#9AD9CC`, Sky `#869FBC`, Purple `#9B83AA`, Yellow `#BEC0D8`, Coral `#F3755C`, Red `#EB6758`. Never for body copy or titles.

## PHASE 2: Deck Structure

(N = number of art styles, usually 3. Exact geometry for every slide type: `references/layout-spec.md`.)

1. **Title** — "Art Styles & Scripts", centered composition with client logo above a short line
2. **Agenda** — "What We'll Do Today": Review Art Styles (Brief, Inspiration, MOA Moment, Style Details) · Art Style Discussion (preferred style, strengths, weaknesses) · Scripts · Script Discussion · Next Steps
3. **Section Divider: "Art Styles"** — same centered composition as title
4. **Per style, 5 slides × N:**
   - Style divider — "Art Style #n " (bold) "- Name" (ExtraLight)
   - Brief
   - Inspiration — 3-over-2 placeholder grid with captions (count flexes with Austin's notes, 4–6 frames)
   - MOA Moment — numbered narration left, 2 stacked placeholder frames right with captions
   - Style Details
5. **Summary** — three staggered hero placeholder frames with numbered circle badges
6. **Section Divider: "Scripts"**
7. **One slide per script** — title "Label - length", script verbatim incl. "Approx Ns", alternates, and asterisked disclaimers
8. **Next Steps** — bold labels + ExtraLight descriptions; typically Update Art Style → Update Scripts → Storyboarding (with sub-steps like Skeleton Storyboard, Animatic)

No Questions slide in this deck type unless requested.

## PHASE 3: Content Rules

- Never invent claims; MOA narration and product statements trace to scripts/client materials, qualifiers intact.
- Scripts verbatim, line breaks preserved.
- No process notes or feedback language on client-facing slides.
- Briefs/Style Details describe the planned imagery from Austin's notes — specific but not fabricating details he didn't indicate.

## PHASE 4: Build & Revisions

- Build at 10×5.625"; verify no frame/caption overlaps and consistent wordmark placement before delivering.
- Placeholder frames must be plain, individually selectable shapes so Austin can delete one and drop an image in its place.
- After each revision round, summarize what changed, which slides, global vs. specific.
- If Austin later supplies some images, place them into their frames (preserve geometry, don't stretch) and leave remaining frames as placeholders.
