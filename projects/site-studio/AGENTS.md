# Site Studio: instructions for agents

You are here to change the Bradley Academy website, or to help someone build a site like it. This
file is written for you. People start at the [README](README.md).

## What the site is

A React site (React Router, every page pre-rendered to HTML) published free by GitHub Pages. It
lives in [`base/examples/bradley-academy/`](base/examples/bradley-academy/). Its readers are business
people who never open GitHub, so every page is written for them, not for developers.

## Where things are

| You need | Go to |
| --- | --- |
| The words on every page | `app/content/`: `site.ts` (brand, home, About Bradley) and `tools.ts` (one entry per tool) |
| The try-it prompts and the pictures | Not stored here. `scripts/sync.mjs` copies them from each project's README and `_build/img/` before every build, so the site never drifts from the READMEs |
| The look | `app/styles/site.css`: colour and type tokens at the top. A night at the cinema: velvet, ivory, Harvard crimson and brass, Bodoni Moda titles |
| The motion | `app/lib/cinema.ts`: GSAP ScrollTrigger and Lenis, driven by `data-cine="..."` attributes on the pages. Off when the reader asks for reduced motion; every page reads fully without it |
| The large pictures | `app/content/images.ts`: one slot per picture. Today each shows a placeholder the owner already made. The Image brief page (`/image-brief`) lists what each final picture should show, its size and a prompt |
| The pages | `app/routes/`: home, one tool page, About Bradley, not found |
| How it is published | [`.github/workflows/pages.yml`](../../.github/workflows/pages.yml) and [`workshop/tools/build_site.py`](../../workshop/tools/build_site.py) |
| The plan, with a definition of done for each step | [`workshop/plans/site-studio/`](../../workshop/plans/site-studio/README.md) |

## Rules for this site

1. **Every fact comes from a README,** or for About Bradley, from Bradley himself. Change the README first, then `tools.ts`. Never invent a
   number, a quote, a customer or a result. A status says who has and has not tried the tool.
2. **The voice is Bradley's practical instructor voice:** the core idea in one sentence, an
   everyday analogy, then the detail. Short sentences. No em dashes. Sentence case headings.
3. **A tool page** has an About tab first (the core idea, what it is, why it helps, how it is
   designed to help, who it is for, three levels with a user story each, try it, what it does not
   do, status), then tabs of real examples.
4. **Pictures go in slots.** Never put a large picture straight into a page: add a slot to
   `images.ts`, so the Image brief stays the full list of what is still a placeholder.
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
