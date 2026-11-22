# WiseGeo: a one-page company site

The second Site Studio example: WiseGeo Inc., Bradley Ross's company. One static page, no build
step, deployed on its own as a separate Vercel project for `wisegeo.com`. It sells hands-on
agentic software for startups and links back to Bradley Academy for the research, the teaching and
the demos that support the offer.

Think of it as the shop front to Bradley Academy's lecture hall: one says what Bradley will build
for you, the other shows what he researches and teaches.

## What is here

| File | Holds |
| --- | --- |
| `index.html` | The page: the offer, three services, selected work, who builds it, and the LinkedIn call to action |
| `styles.css` | The look: cool paper, deep ink, one teal for actions. Bricolage Grotesque and Inter Tight |
| `fonts/` | The two fonts, latin subsets from Fontsource (SIL Open Font License 1.1) |
| `img/` | Bradley's photo (from `assets/images/`) and the 1200 by 630 social preview |
| `vercel.json` | Clean URLs, security headers, long caching for fonts, and a rule that skips a deploy when nothing in this folder changed |
| `404.html`, `robots.txt`, `sitemap.xml`, `favicon.svg` | The usual small files |

Paths start with `/`, so the page works only at the root of a domain or a Vercel preview, not in a
sub-folder. To preview it on your own computer: `python3 -m http.server 8770` in this folder, then
open `http://localhost:8770/`.

## Deploy on Vercel

The person who owns the Vercel account does these steps. Copy any DNS values from Vercel's screen,
never from a guide.

1. In Vercel, **Add New Project** and import `bar181/practical-ai`.
2. **Root Directory:** `projects/site-studio/base/examples/wisegeo`.
3. **Framework Preset:** Other. Leave the build command and install command empty. **Output
   Directory:** `.` (this folder).
4. Deploy. Every pull request that changes this folder then gets its own preview address.
5. **Settings, Domains:** add `wisegeo.com` and `www.wisegeo.com`, then set the DNS records Vercel
   shows at the domain's registrar. Vercel issues the HTTPS certificate once DNS resolves.

Bradley Academy links here through its `SITE_WISEGEO_URL` build setting (default
`https://wisegeo.com`), so the links work as soon as the domain does.

## Rules for this page

- Every fact comes from Bradley. No invented clients, numbers, quotes or testimonials.
- Selected work is public work only, labelled: live website, open-source tool, demo or research.
  Client projects appear only with the client's written approval.
- The main call to action is "Message Bradley on LinkedIn" and opens
  `https://www.linkedin.com/in/bradaross/`.
- Check at 390 and 1280 pixels: no sideways scrolling, 44 pixel tap targets.
- A person approves anything that is published or merged.

## Status

Built and checked by Claude on 22 November 2026 at 390 and 1280 pixels wide, served locally. Not
yet deployed on Vercel, not yet on `wisegeo.com`, and not yet reviewed by Bradley.
