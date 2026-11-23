# WiseGeo: a one-page company site

The second Site Studio example: WiseGeo Inc., Bradley Ross's company. One short static page, no
build step, deployed on its own as a separate Vercel project for `wisegeo.com`. It is for people
who see the name on LinkedIn or an invoice: the legal name, Bradley as founder, what the company
does in three lines, and one link to Bradley's work at `https://bradley.academy/`.

Think of it as the brass plate by the door: it confirms who is inside and points you to the room
where the work is.

## What is here

| File | Holds |
| --- | --- |
| `index.html` | The page: the legal name, the founder, three lines on the work, "View Bradley's work at Bradley Academy" and LinkedIn |
| `styles.css` | The look: cool paper, deep ink, one teal for actions. Bricolage Grotesque and Inter Tight |
| `fonts/` | The two fonts, latin subsets from Fontsource (SIL Open Font License 1.1) |
| `img/` | The 1200 by 630 social preview |
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
- Keep it short. The work lives at Bradley Academy, behind one link; no portfolio here.
- The contact is "Message Bradley on LinkedIn", which opens `https://www.linkedin.com/in/bradaross/`.
  The founder's link in the structured data is `https://bradley.academy/`.
- Check at 390 and 1280 pixels: no sideways scrolling, 44 pixel tap targets.
- A person approves anything that is published or merged.

## Status

Built and checked by Claude on 22 November 2026 at 390 and 1280 pixels wide, served locally, and
simplified the same evening to a short company page at Bradley's direction. Not yet deployed on
Vercel, not yet on `wisegeo.com`.
