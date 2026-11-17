# Let There Be — Claude Skills

The Let There Be Science Marketing Engine, packaged as Claude skills. Every deck skill does its work, then builds the finished presentation in its LTB template in the same run.

## What's inside

Listed in the order a client meets them.

| Skill | What it does | Builds in |
|-------|--------------|-----------|
| `ltb-sales-preview` | Prospect preview. Reads the brand's claims against a top competitor's to find the white space, runs a real Elicit pass, then asks which of several hero claims to build out. Produces a 13-screen deck: current claims, the preview scan, key themes, one territory (hero claim, other ways to say it, the evidence with an honest line), and an illustrative Science Story. Includes a presenter sheet. | LTB Template — Sales Preview (Science Marketing Engine) |
| `ltb-sow` | Statement of Work deck in one of three shapes: a full engine program, a Science Studio™ program, or a single phase. Deliverables and prices come only from the pricing input, and the standard terms are verbatim. | LTB Template — Statement of Work |
| `ltb-project-overview` | Client project overview built around the three-phase engine. | LTB Template — Project Overview |
| `ltb-research-alignment-session` | Research kickoff deck, plus a decisions log for the room that becomes the brief for Science Intelligence. | LTB Template — Research Alignment Session |
| `ltb-science-intelligence` | Claude-native literature review and claim development (Elicit). Produces the evidence workbook and MLR-ready claims. The first stage of every engine project. | — (workbook) |
| `ltb-lit-review-deck` | The client Science Intelligence™ deck. Every direction runs Hero Claim → Supporting Claims → The Evidence → Compliance Logic. | LTB Template — Science Intelligence (Lit Review + Claim Dev) |
| `ltb-science-story` | Groups claims into claim clusters and writes the narratives, built so they can be consumer-tested. | LTB Template — Science Story & Claim Clusters |
| `ltb-science-101` | Internal briefing for the creative team once a Science Story is approved, including an MOA walkthrough written for animators. | LTB Template — Science 101 |
| `ltb-activations` | Shows the approved Science Story in the brand's real channels: video scripts, PDP and Amazon copy, influencer briefs, FAQs. Every efficacy line is tied to an approved claim. | LTB Template — Science Story Activations |
| `ltb-script-feedback-presentation` | Walks a client through script or copy edits line by line, so the script can go to production. | LTB Template — General Presentation |
| `ltb-success-story` | Seven-screen case study of a finished engagement, using project files and a short account-manager intake. | LTB Template — Client Success Story |
| `ltb-supplement-science-score` | Two-pass read of how a supplement category gets judged: SuppCo and similar scoring rubrics, plus how consumer AI assistants recommend the category, with a convergence test between the two. | LTB Template — Supplement Science Score |
| `ltb-general-presentation` | The default for any deck no other skill covers: internal decks, credentials, talks, recaps, trainings. | LTB Template — General Presentation |

## Conventions

- **No "gems."** The unit is a **claim**. The package is a **claim cluster**.
- **One claim format, start to finish.** The Sales Preview, the SOW and the Science Intelligence deck all present claims as hero claim → supporting claims → evidence. The Science Intelligence deck adds compliance logic and tiers every claim Core, Push or Stretch. The preview shows one territory with its sources blurred and has no compliance slide.
- **Decks build themselves.** A deck skill writes a content draft in Claude's working folder, then builds the deck in its template in the same run. The draft isn't saved to the outputs folder. The user gets the deck link, plus any real deliverables such as a presenter sheet, decisions log or workbook.
- **Templates are never edited.** Each build is a new deck copied from its template. Any client content still on a template is a placeholder and never carries over.
- **Brand images come from the design system.** Slides keep their design system image paths (`project/ds/lettherebedesignsystem_9f5f72/...`), so decks keep their images for everyone. Nothing is copied out of a template with `from_url`.
- **Templates must be shared with the team.** If someone can't open a template, the skill stops and tells them, rather than falling back to markdown.
- **Deck rules:**
  - Headlines stay on one line. The one exception is "Science leads. / Creativity amplifies.", which is always split onto two.
  - No boxed tiles for everything.
  - Mitosis shapes stay in the margins.
  - Accessory logos go bottom-left.
  - Layouts must survive the team's edits.
- **Voice:** plain, factual, specific. No hype. LTB's science video work is called "videos," never "films."

## Updating the plugin

- Update this README on every release, and ship it inside the plugin zip.
- Bump `version` in `.claude-plugin/plugin.json` on every release. Check for updates only shows a new version when this number changes.
- `references/template-build.md` is shared by every deck skill and must stay identical in all of them. When you change it, copy it to every skill.
- `references/copy-craft.md` is shared by `ltb-sales-preview`, `ltb-science-intelligence`, `ltb-lit-review-deck` and `ltb-science-story`. Edit all four together.
- When a template is replaced, update its link in the table in `template-build.md`, and in any skill that names the template directly.
- If a skill's `description` contains a colon followed by a space, wrap the description in double quotes, or the skill won't load.
