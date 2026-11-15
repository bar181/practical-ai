# Artifact studio

Pick a page type, a voice and a look from a menu of working examples, and get a page worth sharing built from your own content.

| Complexity | Research | Simple level | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Done: landscape review in the draft | [Drafted](../../drafts/artifact-studio/) | [`drafts/artifact-studio/`](../../drafts/artifact-studio/) |

**Think of it as:** Ordering at a counter. The recipe is the dish, the voice is how you like it, the look is the plate. You point at the menu and the assistant cooks.

## Overview

Work built by an assistant tends to look and sound generic because the assistant has to guess three things: what kind of piece this is, how it should speak and what it should look like. The studio removes the guesses. It is a library of working templates for pages, slide decks and social posts, with rules that pick the best combination for a request, and a skill that builds it from your own content

## Who it is for

Anyone who asks an assistant for a report, a proposal, an explainer or a landing page. Also agents that build those pages, through the skill.

## Scope

- **In:** the base and levels 1 and 2. All are drafted. None has been reviewed by a second person. Level 3 is a list of connection slots, with nothing built.
- **Out:** hosting the page, and video, audio and avatar add-ons. Those belong to other tools on the list.
- **It works when:** a person with no design training gives an assistant their notes and one sentence from the studio, and gets a page they are willing to send on the first or second try.

## What might be involved at each level

The simple level is described in most detail, because it is built first. The later levels are
outlines and will change.

| Level | What it involves | Complexity |
| --- | --- | --- |
| Demo | A base that holds everything: a library of 20 templates (pages, voices, decks, social formats) and 36 parts, an index for people and one for agents, and one studio page that shows them all in tabs with a picker. Every template carries the sentence that asks for it. This tool trials the base-plus-levels layout | Beginner |
| Simple | Level 1, nothing to install. Paste the instructions for the assistant into a Project once. Then copy a sentence from any example, attach your notes, and check every number against them. | Beginner |
| Working | Level 2, your preferences on file. Fill in one preferences file: default recipe, voice and look, brand, layout and format rules. Install the skill if the assistant loads skills. A short ask then gives a page that looks and sounds like yours. | Intermediate |
| Automated | Level 3, connected. One connection is built: an MCP server that gives an assistant the library as tools, so it can choose a template, read its reference code and rules, and file a note about a design the person likes. Tested with a client only. Other slots are listed in the draft: content in, the page out to a web address, a plugin, and runs on a schedule | Advanced |
| Commercial grade | A design system with an owner, approved voices, facts traced to a source of record, an accessibility audit, a named reviewer and a release step with an audit trail. | Explained, not built here |

## Established best practices

Done. See the [landscape review](../../drafts/artifact-studio/landscape-review.md) for what already exists, with dated sources.

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
