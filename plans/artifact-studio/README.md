# Artifact studio

Ask for a web page or small tool and choose its style, from clean to cinematic to scrollytelling, with optional video and audio add-ons.

| Complexity | Research | Simple level | Draft |
| --- | --- | --- | --- |
| Beginner to intermediate | Partly: tool facts checked 2026-11-14 | [Drafted](../../drafts/artifact-studio/) | [`drafts/artifact-studio/`](../../drafts/artifact-studio/) |

**Think of it as:** A print shop with house rules. Any job comes out looking like the same studio made it, because the paper, the type and the margins were decided once.

## Overview

Pages built by an assistant tend to look generic because the assistant has to guess the look. This tool removes the guess: you fill in a design spec once, then name a style every time you ask.

## Who it is for

Anyone who asks an assistant for a page, a calculator, a dashboard or a landing page.

## Scope

- **In:** the simple level described below.
- **Out:** the working level and beyond, until the simple level is in use.
- **It works when:** to be written before anything is built.

## What might be involved at each level

The simple level is described in most detail, because it is built first. The later levels are
outlines and will change.

| Level | What it involves | Complexity |
| --- | --- | --- |
| Demo | A gallery page showing one request built in each style. | Beginner |
| Simple | Fill in a one-page design spec (colours, fonts, spacing, tone, three things you never want). Pick one of five style cards: clean, cinematic, scrollytelling, dashboard or editorial. Give the assistant the spec, the card and two sentences about what the page is for, then run a short pre-ship checklist. | Beginner |
| Working | A saved design system, review steps for accessibility and wording, and a hosting route. | Intermediate |
| Automated | One request produces the page, hosts it and attaches media add-ons such as a short video or an audio track. | Advanced |
| Commercial grade | Brand governance across a team, a component library, and review before anything is published. | Explained, not built here |

## Established best practices

_Partly done. The draft student guide lists the sources checked on 2026-11-14. A wider review of established practice is still to do._

## What it reuses

Design and front-end skills already available in chat assistants. Publishing a website covers the hosting.

Found so far in the reuse check, on 2026-11-14:

- Anthropic's skills repository includes a frontend design skill and a web artifacts builder skill for multi-component pages. [Source](https://github.com/anthropics/skills)
- OpenAI's skills catalogue for Codex includes a frontend skill, and both use the same open skill format. [Source](https://composio.dev/blog/top-design-skills), [format](https://developers.openai.com/codex/skills.md)
- Community skill packs already offer named visual styles such as editorial, bento and brutalism. Review these before writing more style cards. [Source](https://open-design.ai/plugins/codex-design/)

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

- Which styles beyond the first five are worth a card?
- Which paid add-ons are worth their cost per render?
