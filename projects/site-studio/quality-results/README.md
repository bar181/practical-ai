# Site Studio: the evidence

What was checked, by whom, and what was not.

## 19 November 2026: first version of the Bradley Academy site

Built and checked by Claude in one session. **No person has used the site yet, and it is not live
until the owner merges it.**

| Check | Result |
| --- | --- |
| Build | `npm run build` pre-renders 7 pages (home, About Bradley, five tool pages) with no errors. `npm run typecheck` passes |
| Pages outside the app | The site was assembled as the workflow does it and served locally. Every page returned 200, including the embedded Artifact Studio master pages and Rare Find |
| Phone and desktop | Home, a tool page, About and an example tab at 390 and 1280 pixels wide: no sideways scrolling, no script errors |
| Tabs | A tap selects a tab and puts it in the address. Arrow keys move focus and Enter selects. With script off, every panel shows, one after another |
| Facts | Every fact on the tool pages was copied from that tool's README on 19 November 2026. The try-it prompts are copied from the READMEs at build time |

**Not yet checked:** the live deploy on GitHub Pages; a real phone; Safari and Firefox; a screen
reader; a reader review by a fresh agent briefed as a business owner (step 3 of the plan); the
owner's review of the voice and the look (step 4).
