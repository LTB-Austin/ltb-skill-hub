# Output template — `[topic]-deck.md`

This is the working draft. Write it in your working folder, not the outputs folder. Fill it top to bottom, one block per slide, in deck order. A field value is the exact text that goes on the slide.

```markdown
# [Deck title]
Audience: [who] · Leave them with: [one sentence] · [n] slides · [Month Year]

## Spine (headlines only, in order)
1. [headline]
2. [headline]
…

---

## 01 · [layout id, e.g. cover]
- Eyebrow: [grey label, or none]
- Headline: [one line]
- [Fields for this layout, per layout-library.md]
- Image: [real file to upload, or none]
- Speaker notes: [2–4 sentences: what the presenter says, including reasoning the slide leaves out]

## 02 · [layout id]
…

---

## Open items
- [NEEDED: …] — slide [nn]
```

## Rules for the draft
- The spine comes first. If the headlines don't tell the story on their own, fix them before writing the bodies.
- Every slide names its layout id from `layout-library.md`. To use a layout twice, give the second one a suffix (`text-2`).
- Speaker notes carry the detail, so the slides stay clean.
