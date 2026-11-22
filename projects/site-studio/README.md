# Site Studio

<h3 align="center">Publish a website: from a shared page to your own domain, with your AI.</h3>

<p align="center">For anyone who has made a page with AI and wants it online.</p>

<p align="center"><b>Free to start</b> &nbsp;·&nbsp; <b>Three levels</b> &nbsp;·&nbsp; <b>Worked example: Bradley Academy</b></p>

**The core idea:** pick the smallest way online that does the job, then move up only when the site
needs more.

**Think of it as** hanging a painting. A pin board anyone can glance at (share a link from your
chatbot), a frame in your own hallway (your own address on GitHub Pages or Vercel), or a gallery with
a guard at the door (a platform with a database and sign-in).

- **Level 1 takes ten minutes.** Share the page your chatbot made as a link. No account to set up.
- **Level 2 is yours for good.** A free address that updates every time you save, then your own
  domain.
- **Level 3 when the site must remember.** Cloudflare or Google Cloud to host, Supabase for the
  database and login.

**The worked example is this repository's own site:** [Bradley Academy](https://bar181.github.io/practical-ai/),
Bradley Ross's personal site with every Practical AI tool, built in React and published by GitHub
Pages.

## Get started: try it now

Copy this into Claude, ChatGPT or Gemini and fill in the brackets. It picks the level and walks you
through each click.

```
Read https://github.com/bar181/practical-ai/blob/main/projects/site-studio/base/SKILL.md and follow it.
I made: [a page in Claude, ChatGPT or Gemini / an HTML file / a React site].
Who should see it: [anyone I send the link to / the public, under my own domain].
It must: [only show content / keep data or let people sign in].
```

Chatbot cannot open links? Open [`base/SKILL.md`](base/SKILL.md), press **Raw**, copy all of it into
a new chat, then answer its three questions.

| Level | For | What you do | Guide |
| --- | --- | --- | --- |
| **1. Share it** | Anyone with a page made in a chatbot | Share the Claude artifact, ChatGPT canvas or Gemini canvas as a link | [The skill](base/SKILL.md) |
| **2. Publish it** | Someone who wants a lasting address and their own domain | GitHub Pages step by step, your own domain, or Vercel as the easiest import | [Level 2](level-2-files/README.md), and [Build your own site](base/BUILD-YOUR-OWN-SITE.md) for a React site like this one |
| **3. Build on a platform** | A site that keeps data or lets people sign in | Cloudflare or Google Cloud (Firebase Hosting) to host, Supabase for the database and login | [Level 3](level-3-files/README.md) |

**Run the example on your computer:**

```sh
cd projects/site-studio/base/examples/bradley-academy
npm install
npm run dev
```

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
- the owner's own photographs, served as light WebP copies;
- a privacy page, and analytics only with consent (off until an ID is set);
- a guide to build your own.

Two reviewer agents scored six rounds against what a client paying an agency US$50,000 would accept:

- UX, content and accessibility rose from 63 to 86, which the reviewer says passes once the photos are replaced.
- Art direction rose from 50 to 73.

**21 November 2026:** four new tool pages (Web Sections, Tone Studio, Meeting notes to actions, and
Write and edit in my voice), so the site lists nine tools. Artifact Studio's page now presents it as
the design step, with the new cinematic effects. Checked by an agent in headless Chrome at phone and
desktop width; the reviewers have not scored these pages.

**22 November 2026: rebuilt as Bradley's own site.** The home page now presents Bradley Ross,
Agentic Architect and Researcher, for research labs and funded startups, with a new Research page. Practical AI moved to its own section at `/tools`, with a practical guide added. Built and
checked by Claude at phone and desktop width, with two rounds of independent agent review. Not yet
reviewed by Bradley, and not merged.

**22 November 2026, later:** office hours removed. The site is now a personal profile: research
milestones built on AISP, a one-line network note, and early access for research groups and partners
through LinkedIn. Built and checked by Claude at phone and desktop width; not rescored, not reviewed by
Bradley, and not merged.

**22 November 2026, evening:** after an outside reviewer read the site as decent rather than top
tier, the home and Research pages lead with the work (AISP and BAR Observatory), show only public
evidence with a link to each number's method and limits, and end with a "Check it yourself" path.
Unpublished results come off the site and are shared on request. Built and checked by Claude at
390 and 1280 pixels; not yet reviewed by Bradley or the outside reviewer.

**Later that evening:** AISP shown in its own notation, verbatim from the open-core specification:
the 512 symbols in eight categories, the foundation and glossary, then the binding proof, the Pocket
architecture, learning, search and the evidence block, each read line by line. The commercial grade
is named for research partners, not shown. Teaching sits beside research. Checked by Claude at 390
and 1280 pixels; not yet reviewed by Bradley.

**22 November 2026, latest:** Site Studio became the publish-a-website lesson. A skill for any
chatbot (Level 1), GitHub Pages, your own domain and Vercel (Level 2), and Cloudflare, Google Cloud
and Supabase (Level 3), written from each provider's documentation with dated sources. No person and
no agent has followed the Level 1 to 3 guides yet.

**Users:** In use by people other than the author, from business owners to agentic developers (reported by Bradley, 22 November 2026); their results are not recorded here yet. The React guide was also followed twice by a fresh agent for an invented bakery.

**22 November 2026:** one new tool page, Research brief with checked sources. Built and type-checked,
and checked by an agent in headless Chrome at phone and desktop width: no sideways scrolling, no
console errors. The reviewers have not scored it.
[The evidence](quality-results/README.md).

## About Bradley Ross

Created by **Bradley Ross**, who builds and teaches practical AI. Part of
[Practical AI](../../README.md). [linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)

**Are you an AI agent?** Read [AGENTS.md](AGENTS.md).

Licence: [Apache 2.0](LICENSE).
