# Site Studio

<h3 align="center">A real website for your work, made with your AI, hosted free.</h3>

<p align="center">For people whose customers will never open GitHub.</p>

<p align="center"><b>Free</b> &nbsp;·&nbsp; <b>React</b> &nbsp;·&nbsp; <b>Hosted free on GitHub Pages</b><br><b>Building</b> &nbsp;·&nbsp; <b>First site: Bradley Academy</b></p>

GitHub is a workshop. Builders are happy there, but most people never walk into a workshop. They
want a shop front: what each thing does, why it helps, and one button to try it. Site Studio builds
the shop front.

- **For people who never open GitHub.** A home page that says what you do, and one page per
  product that explains it in plain words, with real examples in tabs.
- **Made with your AI, from what you already wrote.** The words come from your READMEs, so the site
  and the code never disagree.
- **Free to host, yours to grow.** React, every page pre-rendered for search engines, published by
  GitHub Pages. Add your own domain later.

**The first site is its author's own:** [Bradley Academy](https://bar181.github.io/practical-ai/),
with every Practical AI tool. It goes live when this project is merged.

## Get started

**Today: see the site.** Open [bradley-academy](https://bar181.github.io/practical-ai/) once it is
live, or run it on your computer:

```sh
cd projects/site-studio/base/examples/bradley-academy
npm install
npm run dev
```

**Build your own:** [the step by step](base/BUILD-YOUR-OWN-SITE.md), from a new GitHub repository to a
live address on GitHub Pages, with a prompt that hands the whole job to a coding agent. Written
from how this site is built; not yet tried end to end by anyone.

| Level | For | What it will do |
| --- | --- | --- |
| **1. Make it in your chatbot** | An owner with notes and no developer | A one-page site, a multi-page site, or a showcase page with photo effects, from one prompt in Claude, ChatGPT or Gemini |
| **2. Make it your standard** | Someone who updates the site every month | Skills that keep every page in the same voice and look, with a check before anything goes out |
| **3. Your own React site on GitHub** | A builder with a coding agent | This site as a template: your content in one folder, a free address on GitHub Pages, your own domain when you are ready |

## How it is built

| Part | What it is |
| --- | --- |
| [`base/examples/bradley-academy/`](base/examples/bradley-academy/) | The site: React Router with every page pre-rendered, plain CSS, fonts installed with the site |
| `app/content/` in that folder | Every word on the site. Facts come from the project READMEs |
| `scripts/sync.mjs` in that folder | Copies the pictures and try-it prompts out of the READMEs before each build |
| [`.github/workflows/pages.yml`](../../.github/workflows/pages.yml) | Builds the site and publishes it with every other page in the repository |
| [The plan](../../workshop/plans/site-studio/README.md) | Users, levels, the stack decision, research and a definition of done for each step |

Built with Claude's `frontend-design` plugin, `modern-web-guidance`, Anthropic's example skills and
Vercel's open-source React skills. The list is in [AGENTS.md](AGENTS.md).

## Status

**20 November 2026: building.** The Bradley Academy site is cinematic, with:

- an About page that covers the research to instruction line;
- an Image brief page for the 24 placeholder pictures;
- a guide to build your own.

Two reviewer agents scored six rounds against what a client paying an agency US$50,000 would accept:

- UX, content and accessibility rose from 63 to 86, which the reviewer says passes once the photos are replaced.
- Art direction rose from 50 to 73.

**21 November 2026:** four new tool pages (Web Sections, Tone Studio, Meeting notes to actions, and
Write and edit in my voice), so the site lists nine tools. Artifact Studio's page now presents it as
the design step, with the new cinematic effects. Checked by an agent in headless Chrome at phone and
desktop width; the reviewers have not scored these pages.

**No person has used it, and it is not live until the owner merges it.** The guide was followed twice by
a fresh agent for an invented bakery; the publish step itself has not been tried.
[The evidence](quality-results/README.md).

## About Bradley Ross

Created by **Bradley Ross**, who builds and teaches practical AI. Part of
[Practical AI](../../README.md). [linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)

**Are you an AI agent?** Read [AGENTS.md](AGENTS.md).

Licence: [Apache 2.0](LICENSE).
