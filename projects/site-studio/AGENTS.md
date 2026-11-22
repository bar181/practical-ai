# Site Studio: instructions for agents

You are here to help someone publish a website, to change the Bradley Academy website, or to help
someone build a site like it. This file is written for you. People start at the [README](README.md).

## Publishing a website

The lesson has three levels. Use [`base/SKILL.md`](base/SKILL.md) as the guide: it picks the
smallest level that does the job.

| Level | Guide |
| --- | --- |
| 1. Share a chatbot artifact or canvas as a link | [`base/SKILL.md`](base/SKILL.md) |
| 2. GitHub Pages, your own domain, Vercel | [`level-2-files/README.md`](level-2-files/README.md), and [`base/BUILD-YOUR-OWN-SITE.md`](base/BUILD-YOUR-OWN-SITE.md) for a React site |
| 3. Cloudflare, Google Cloud (Firebase Hosting), Supabase database and login | [`level-3-files/README.md`](level-3-files/README.md) |

The person publishes, buys domains, changes DNS and creates accounts. You never do, and you never
handle a password or a secret key. Copy DNS values from the host's screen, never from memory.

## What the site is

A React site (React Router, every page pre-rendered to HTML) published free by GitHub Pages. It
lives in [`base/examples/bradley-academy/`](base/examples/bradley-academy/). Its readers are business
people who never open GitHub, so every page is written for them, not for developers.

## Where things are

| You need | Go to |
| --- | --- |
| The words on every page | `app/content/`: `brand.ts` (Bradley's home page and Research), `site.ts` (the brand, the Practical AI page, About Bradley) and `tools.ts` (one entry per tool) |
| The try-it prompts and the pictures | Not stored here. `scripts/sync.mjs` copies them from each project's README and `_build/img/` before every build, so the site never drifts from the READMEs |
| The look | `app/styles/site.css`: colour and type tokens at the top. A night at the cinema: velvet, ivory, Harvard crimson and brass, Bodoni Moda titles |
| The motion | `app/lib/cinema.ts`: GSAP ScrollTrigger and Lenis, driven by `data-cine="..."` attributes on the pages. Off when the reader asks for reduced motion; every page reads fully without it |
| The large pictures | `app/content/images.ts`: one slot per picture, each one of the owner's own photographs with its alt text. `scripts/make_webp.py` makes light WebP copies (1600 and 800 pixels wide) in `../../_build/photos-webp/`; the page serves those with `srcset` |
| AISP in its own notation | `app/content/aisp.ts`: verbatim excerpts of the AISP specification (`AI_GUIDE.md` in aisp-open-core) with a plain reading of key lines; `app/components/Aisp.tsx` draws them. Copy lines exactly and mark gaps with `;; …`. Only the open core is shown. After changing it, run `python3 scripts/make_aisp_fonts.py`, which regenerates the two small fonts in `app/fonts/` |
| Analytics and Search Console | Off unless set at build time: `SITE_GA_ID` (a Google Analytics 4 ID) shows a consent banner and loads analytics only after Yes; `SITE_GSC` adds the Search Console verification tag. The Privacy page (`/privacy`) says which is on |
| The pages | `app/routes/`: home (Bradley), research, practical-ai (the `/tools` page), one tool page, About Bradley, privacy, not found |
| How it is published | [`.github/workflows/pages.yml`](../../.github/workflows/pages.yml) and [`workshop/tools/build_site.py`](../../workshop/tools/build_site.py) |
| The plan, with a definition of done for each step | [`workshop/plans/site-studio/`](../../workshop/plans/site-studio/README.md) |

## Rules for this site

1. **Every fact comes from a README,** or for Bradley's own pages (home, Research, About), from Bradley himself. Those pages are a personal profile, not a services page: a vision and a few proof points with brief evidence. Early access to the research is by invitation, for Bradley's connections and partners only; everyone else connects on LinkedIn with a note. No offers of free help. No catalogue, no prices, and no statements about who has not used something. His title is Agentic Architect and Researcher; "agentic engineer" is also allowed. Bradley decided this on 22 November 2026 for a global audience, knowing both words are protected titles in Ontario. Research numbers come only from Bradley; a projection is labelled as one. Change the README first, then `tools.ts`. Never invent a
   number, a quote, a customer or a result. A status says who has and has not tried the tool.
2. **The voice is Bradley's practical instructor voice:** the core idea in one sentence, an
   everyday analogy, then the detail. Short sentences. No em dashes. Sentence case headings.
3. **A tool page** has an About tab first (the core idea, what it is, why it helps, how it is
   designed to help, who it is for, three levels with a user story each, try it, what it does not
   do, status), then tabs of real examples.
4. **Pictures go in slots.** Never put a large picture straight into a page: add a slot to
   `images.ts` with alt text that says what is shown, then run `python3 scripts/make_webp.py` for
   its light copies.
5. **Phone first.** Check every change at 390 pixels wide: no sideways scrolling, 44 pixel tap
   targets, readable with motion off. Pre-rendered pages must read fully before any script runs.
6. **Add a tool** by adding its slug to `app/content/slugs.ts`, its entry to `tools.ts`, and its
   README heading to `scripts/sync.mjs`. The page, the home card and the sitemap follow.
7. A person approves anything that is published or merged.

## Run it

```sh
cd base/examples/bradley-academy
npm install
npm run dev        # http://localhost:5173/practical-ai/
npm run build      # pre-renders every page into build/client/
npm run typecheck
```

Pages outside the app (the Artifact Studio master pages, Rare Find, the explainers) are added by
`build_site.py` in the workflow, so in `npm run dev` their links and embeds do not load.

**Custom domain:** set `SITE_BASE=/` and `SITE_URL=https://your-domain` for the build, and add the
domain in the repository's Pages settings.

## Plugins and skills

| For | Use |
| --- | --- |
| Design | `frontend-design`; `theme-factory` and `brand-guidelines` from `example-skills` |
| Modern CSS and HTML | `modern-web-guidance` |
| React | Vercel's `react-best-practices`, `composition-patterns` and `react-view-transitions`: `npx skills add vercel-labs/agent-skills` |
| Review | `web-design-guidelines` and `writing-guidelines` (Vercel), `design:accessibility-review`, `design:ux-copy` |
| Checking in a browser | `playwright`, `webapp-testing` |
| Library docs | `context7` |
