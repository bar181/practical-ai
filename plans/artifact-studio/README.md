# Artifact studio

Pick a page type, a voice and a look from a menu of working examples, and get a page worth sharing built from your own content.

| Complexity | Research | Simple level | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Done: landscape review in the draft | [Drafted](../../drafts/artifact-studio/) | [`drafts/artifact-studio/`](../../drafts/artifact-studio/) |

**Think of it as:** Ordering at a counter. The recipe is the dish, the voice is how you like it, the look is the plate. You point at the menu and the assistant cooks.

## Overview

Pages built by an assistant tend to look and sound generic because the assistant has to guess three things: what kind of page this is, how it should speak and what it should look like. The studio removes the guesses. You choose a recipe (page type), a voice and a look from a menu of working examples, and the assistant builds the page from your own content.

## Who it is for

Anyone who asks an assistant for a report, a proposal, an explainer or a landing page. Also agents that build those pages, through the skill.

## Scope

- **In:** every level, from the demo to the skill. All are drafted. None has been reviewed by a second person.
- **Out:** hosting the page, and video, audio and avatar add-ons. Those belong to other tools on the list.
- **It works when:** a person with no design training gives an assistant their notes and one sentence from the studio, and gets a page they are willing to send on the first or second try.

## What might be involved at each level

The simple level is described in most detail, because it is built first. The later levels are
outlines and will change.

| Level | What it involves | Complexity |
| --- | --- | --- |
| Demo | One file with six tabs: a sentence builder, four recipes, seven voices, twelve page components and twelve photo components. Every example carries the sentence that asks for it. | Beginner |
| Simple | Copy one sentence from the studio, attach your notes, and paste both into a chat assistant. The assistant chooses the colours and type. Check every number against your notes. | Beginner |
| Working | Choose the recipe, the voice, the look and the parts yourself. Fill in a one-page design spec once and a five-line content brief per page, then run the pre-ship checklist. | Intermediate |
| Automated | Install the artifact-studio skill. Hand over any content and media. The skill chooses or follows the recipe, voice and look, builds one self-contained page, checks it, and reports what it assumed and what is missing. Hosting and media add-ons belong to other tools. | Advanced |
| Commercial grade | A design system with an owner, approved voices, facts traced to a source of record, an accessibility audit, a named reviewer and a release step with an audit trail. | Explained, not built here |

## Established best practices

Done. See the [landscape review](../../drafts/artifact-studio/landscape-review.md) for what already exists, with dated sources, and the [best practices](../../drafts/artifact-studio/BEST-PRACTICES.md) for how the tool is built and used.

## What it reuses

The assistant's own page-building and any front-end design skill it has. Browser features for scroll effects and cross-fades. Publishing a website covers the hosting.

Found so far in the reuse check, on 2026-11-14:

- Anthropic's skills repository includes a frontend design skill and a web artifacts builder skill for multi-component pages. [Source](https://github.com/anthropics/skills)
- OpenAI's skills catalogue for Codex includes a frontend skill, and both use the same open skill format. [Source](https://composio.dev/blog/top-design-skills), [format](https://developers.openai.com/codex/skills.md)
- Community skill packs already offer named visual styles such as editorial, bento and brutalism. [Source](https://open-design.ai/plugins/codex-design/)
- Scroll-driven animations and view transitions now work in current browsers without a library, and the standard animation, chart and component libraries are free. Details and licences are in the draft's landscape review.
- Nothing found lets a non-designer choose a page type, a voice and a look in plain words. That gap is what this tool fills.

## Decisions to record during research

Follow the [build process](../plans-template/BUILD-PROCESS.md). Tick each as it is settled.

- [ ] **Reuse check:** what is built in, what is open source, and whether to stop here
- [ ] **Build or license:** the lean for each level, with outside providers reviewed but not selected
- [ ] **Dependencies and pricing:** what the simple level depends on and what it costs
- [ ] **Where it lives:** which assistant, where the files are kept, what stays manual

## First step

1. Research established best practices. Record each one with a source link and the date checked.
2. Write the simple level solution and its overview.

The working level and beyond are planned only after the simple level is in use.

## Open questions

- Do the sentences reproduce the demo pages in fresh chats? The test sheet is in the draft and has not been run.
- Does the skill work for a second agent without help?
- Is the practical instructor voice card right? It is a guess.
- Which recipe should be added next: a dashboard, a case study or a one-page plan?
