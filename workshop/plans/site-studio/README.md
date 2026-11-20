# Site Studio: the full plan

One-line promise: a real website for your work, made with your AI, hosted free on GitHub Pages,
that people who never open GitHub can read, use and share.

| Complexity | Research | Status |
| --- | --- | --- |
| Beginner (level 1) to advanced (level 3) | Done, 19 November 2026 (sources below) | **Building.** Project 6. The first version of the Bradley Academy site is in [`projects/site-studio/`](../../../projects/site-studio/). Replaces the Website builder plan and the Publishing a website plan |

**Think of it as** a shop front for a workshop. The workshop (GitHub) is where the tools are made,
and builders are happy there. Most customers never walk into a workshop. They want a clean shop
front: what each tool does, why it helps, and one button to try it. Site Studio builds the shop
front, and shows you how to build your own.

**North Star:** a business owner who has never opened GitHub lands on the site, understands in
one screen what the tools do for them, and tries one within a minute. Builders still get the
GitHub READMEs, unchanged.

**Dogfood:** the first site is Bradley's own: **Bradley Academy**, with the Practical AI tools,
built in React and published by GitHub Actions to GitHub Pages. The source code stays at
[bar181/practical-ai](https://github.com/bar181/practical-ai). Once it works, the project adds the
step by step for anyone to build their own.

---

## The usable result (U1 to U5)

| | |
| --- | --- |
| **U1, who uses the site** | A business owner, manager or student who uses a chatbot and has never opened GitHub. Second: Bradley's course students and clients, sent a link |
| **U2, what they come with** | A link from a post, a course or a person, and one question: what is this, and will it help me? |
| **U3, what they get** | A home page that says what the tools do and the core benefits. One page per tool: what it is, why it helps, how it is designed to help, who it is for, the three levels with a user story each, and tabs of real examples. A copy button for each try-it prompt |
| **U4, what makes it usable** | Readable on a phone. Every page answers "what is it and what do I do first" on its first screen. Nothing is invented: every fact comes from the tool's README. Each status says who has and has not tried it |
| **U5, the exception it must catch** | A visitor who only wants to try it: the try-it prompt and its copy button are one tap away on every tool page. A visitor who wants the code: one link to GitHub on every page |

**Who uses the project (the builder):** someone who wants the same kind of site for their own
work. Bradley first, then his students and clients.

## Site map

| Page | Its one job | Main action |
| --- | --- | --- |
| **Home** | Say simply what the tools do and the core benefits | See the tools, or copy the starter prompt |
| **One page per tool** (5 today) | Explain the tool so a busy person can decide | Copy the try-it prompt |
| **About Bradley** | Who made this and why to trust it | Connect on LinkedIn |

**A tool page** has tabs. The first tab, **About**, is the landing page in Bradley's practical
instructor voice: the analogy, what it is (product description), why it helps (value), how it is
designed to help, who it is for (core user), the three levels with a user story and what each level
does, the try-it prompt, and the honest status. **The other tabs are examples:** the live pages,
pictures and worked examples each tool already has.

## Stack decision

**React Router 7 in framework mode, with every page pre-rendered at build time.**

- It is React, so features can be added later (search, a playground, sign-in pages).
- Each page is still a real HTML page when it is published, which search engines and link
  previews need. React Router says pre-rendering with `ssr:false` is for deploying to a static file
  server ([React Router docs](https://reactrouter.com/how-to/pre-rendering), checked 19 November 2026).
- GitHub Pages hosts it free. Vite's guide covers it: set `base`, then deploy with a GitHub Actions
  workflow ([Vite docs](https://vite.dev/guide/static-deploy), checked 19 November 2026).
- **Custom domain later:** the base path is one setting (`SITE_BASE`). For your own domain on GitHub
  Pages, set it to `/` ([Vite docs](https://main.vitejs.dev/guide/static-deploy), checked 19 November 2026).

**The alternative considered:** Astro with React islands. Astro ships less script and is the common
pick for content sites ([Lucky Media, 2026](https://www.luckymedia.dev/insights/astro)). It was not
chosen because the owner asked for React so that features can be added, and pre-rendering gives the
same plain HTML for every page.

## Plugins and skills used

Installed for this build on 19 November 2026, all from Anthropic's marketplaces or open source:

| For | Plugin or skill | From |
| --- | --- | --- |
| Distinctive design | `frontend-design` | Anthropic, claude-plugins-official |
| Modern CSS and HTML | `modern-web-guidance` | claude-plugins-official |
| Themes, brand and web-artifact patterns, browser testing | `example-skills` (`theme-factory`, `brand-guidelines`, `web-artifacts-builder`, `webapp-testing`) | Anthropic, anthropics/skills |
| Current library docs (React Router, Vite) | `context7` | claude-plugins-official |
| Checking pages in a real browser | `playwright` | claude-plugins-official |
| TypeScript checking | `typescript-lsp` | claude-plugins-official |
| React patterns, interface review, writing review | `react-best-practices`, `composition-patterns`, `react-view-transitions`, `web-design-guidelines`, `writing-guidelines` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), MIT |
| Content and copy | `marketing` (content-creation, brand-review), `design` (ux-copy, accessibility-review) | Already enabled |
| The voice and the look | Artifact Studio's practical instructor voice | This repository |

`.claude/settings.json` in the repository lists the marketplaces and plugins, so anyone who opens
the repository in Claude Code is offered the same set.

## What each level holds

| Level | Core user | User story | What it does |
| --- | --- | --- | --- |
| **1. Make it in your chatbot** | A business owner with notes and no developer | As an owner, I want a site that says what I do, so that customers understand me without a call | A guide and one prompt for Claude, ChatGPT or Gemini: a one-page site, a multi-page site, or a showcase page with Artifact Studio's photo effects. Shared with the chatbot's own button |
| **2. Make it your standard** | Someone who will update the site every month | As a builder, I want every page made the same way, so that the site stays consistent as it grows | The skills: Artifact Studio for the look and voice, a site checklist, and `publish-check` before anything goes out. Saved once as a skill or a Project |
| **3. Your own React site on GitHub** | A builder with a coding agent, and the owner of this repository | As a builder, I want my own React site on free hosting with my content in one folder, so that I can add features and never pay for hosting | This site as a template: content files, the build, and the GitHub Pages workflow, with the step by step from a new repository to a live address, and a custom domain as the last step |

## Build steps, with a definition of done for each

| Step | What is built | Done when |
| --- | --- | --- |
| 1 | The React site with Home, five tool pages and About Bradley, content from the READMEs | Builds with no errors. Every page is pre-rendered HTML. Every fact is found in a README. Opens at 390 pixels with no sideways scrolling |
| 2 | Publishing: the Pages workflow builds the React site at the root and keeps every existing page path (`/artifact-studio/`, `/rare-find/`, `/reports/`) | Built in CI on a pull request. After the owner merges, the site is live at bar181.github.io/practical-ai |
| 3 | Review loop: a fresh reader agent briefed as a business owner, plus `web-design-guidelines` and an accessibility review | The reader scores 80 or more out of 100 and can say what to do first. No contrast or keyboard failures |
| 4 | The owner reviews the voice and the look | The owner approves, or lists changes that are then made |
| 5 | Level 3 guide: build your own React site on GitHub, step by step, from this template | A fresh agent follows the guide from an empty repository to a live site |
| 6 | Levels 1 and 2 guides and examples | Each example made by a fresh session, kept unedited with its prompt |
| 7 | README landing page, explainer, quality results, indexes | `check_links.py` and `check_project.py` pass. The status line says who has and has not tried it |

## Decisions to record

- [x] **Name:** Site Studio, the partner to Artifact Studio. The first site is branded Bradley Academy; source code under bar181. (19 November 2026)
- [x] **Where the site lives:** `projects/site-studio/base/examples/bradley-academy/`, published at the root of the repository's Pages site.
- [x] **Stack:** React Router 7, pre-rendered, plain CSS with design tokens, fonts installed with the site rather than loaded from a font service.
- [x] **Hosting:** GitHub Pages through GitHub Actions. Custom domain left open.
- [ ] **Owner review of voice and look** (step 4).
- [ ] **Custom domain:** later, owner's choice.

## Established best practices

1. **Unique title and description on every page.** [Google Search Central](https://developers.google.com/search/docs/guides/get-started), checked 19 November 2026.
2. **A sitemap.** [Google Search Central](https://developers.google.com/search/docs/guides/get-started), checked 19 November 2026.
3. **Pre-render content pages** so they are complete HTML without running script. [React Router docs](https://reactrouter.com/how-to/pre-rendering), checked 19 November 2026.
4. **Publish from a workflow, with the base path set for a project site.** [Vite docs](https://vite.dev/guide/static-deploy), checked 19 November 2026.
5. **Phone first, readable with motion off, real buttons and visible focus.** Artifact Studio's build rules, reused.

## Chatbot hosting today (for the Level 1 guide)

- **Claude** publishes an artifact to a public link ([Claude docs](https://code.claude.com/docs/en/artifacts), checked 19 November 2026).
- **ChatGPT Sites** builds and hosts a site and can use a domain you own. Public beta since 9 July 2026, paid plans only ([OpenAI help](https://help.openai.com/en/articles/20001339), checked 19 November 2026).
- **Gemini Canvas** makes pages and shares them by link ([Google help](https://support.google.com/gemini/answer/16047321?hl=en), checked 19 November 2026).
- **Netlify Drop** publishes a dropped folder with no account; an unclaimed site is deleted ([Netlify docs](https://docs.netlify.com/start/get-started-with-drop/), checked 19 November 2026).

So Level 1 must not compete with hosting. It adds the brief, the design and the site checks.

## What it replaces

The Website builder plan (never merged) and the Publishing a website plan and draft. Its research on
chatbot hosting is kept above.
