# Site Studio: the evidence

**22 November 2026: in use.** Bradley reports that people other than the author now use this
project, from business owners to agentic developers. Their results are not recorded here yet. The
checks below were run by the author and by fresh Claude sessions; the dates on them still hold.

What was checked, by whom, and what was not.

The site is live on GitHub Pages since the pull requests were merged. The checks below were run by
Claude or by fresh Claude agents, on the dates shown.

## 22 November 2026: the publish-a-website lesson

What was checked, by Claude only:

- Every DNS value, menu name and key rule in the Level 1 to 3 guides was checked against the
  provider's own documentation on 22 November 2026. The sources are listed at the end of each guide.
- The new Site Studio tool page was built, pre-rendered and opened in headless Chrome at 390 and
  1280 pixels wide: no sideways scrolling, one heading, no console errors.

What was not checked: no person and no agent has followed the skill or the Level 2 and 3 guides, no
domain was connected, and nothing was deployed to Vercel, Cloudflare, Firebase or Supabase.

## 20 November 2026: the cinematic site, six review rounds

Two reviewer agents scored each round against one bar: would a client paying an agency at least
US$50,000 accept this as delivered? Neither reviewer edited any file. Each drove the live pages in a
real browser at 1440 by 900 and 390 by 844, and read screenshots taken at scroll stops.

| Round | Art direction (out of 100) | UX, content and accessibility (out of 100) | What changed before the round |
| --- | --- | --- | --- |
| 1 | 50 | 63 | The first cinematic build |
| 2 | 65 | 76 | Fixed a crash when leaving the home page; screen-reader text; tab bar under the header; hero contrast; copy then open a chatbot |
| 3 | 70 | 80 | One photo grade; one line of facts in place of a numbers band; the five-tool strip under the hero |
| 4 | 61 (a fresh reviewer) | 83 | No count-up on claims; the tool strip on the first screen at five sizes; a "Who it is for" scene |
| 5 | 70 | 85 | Fixed a black-out in the tool stack; the stack choreographs each title; its own pictures for each "Who it is for" scene |
| 6 | 73 | 86 | The side column after the story on phone; the letterbox on tool pages; "Try it" stays on a tool page; full-height stack scenes |

The art direction reviewer changed between rounds 3 and 4, and the fresh reviewer found the stack
black-out the first had missed, so its round 4 score fell before it rose again.

**Where it stands after round 6:**

- **UX (86):** a client would accept it at the US$50,000 bar once the placeholder photos are replaced (the owner has since confirmed the photos are final; see below).
- **Art direction (73):** it clears the bar for direction, type and motion, but the layout is still plain for an award site.

Its last suggestions were made after round 6 and have not been scored:

- a sticky "Try it in a minute" card beside the story on desktop tool pages;
- a picture-led scene behind the starter prompt;
- the cartoon first on the image brief (that page has since been removed);
- a shorter copy message for screen readers.

**What still holds it back:**

- **Photos.** The reviewers read the owner's photographs as placeholders because most do not show
  their tool. On 22 November 2026 the owner confirmed they are final, so the Image brief page was
  removed. Whether a picture that does not show its tool weakens a page is still the reviewers'
  open point.
- **The headline.** It is the owner's tagline from the root README. Reviewers asked for one that
  names an outcome. That decision belongs to the owner.

## The build-your-own guide

A fresh agent followed the first version of the guide for an invented bakery. The site built and
served at `/my-site/`, but the agent found six gaps:

- The steps were in the wrong order.
- Pictures were ignored by git.
- The address was set in three places.
- The prompt keys were unclear.
- The brand words were fixed in the code.
- New products had no icon.

All six are fixed. A second run of the revised guide built and served the bakery site from a fresh
clone with no Bradley Academy name or picture on any page. It found five smaller gaps, all fixed:

- the owner's pictures were still published;
- one step did not warn about expected errors;
- some template words were fixed in the code;
- `package.json` still carried the template's name;
- `README.md` still carried the template's text.

The publish to GitHub Pages itself has not been tried with the guide.

## 19 November 2026: first version

Built and checked by Claude:

- **Build:** `npm run build` pre-renders every page and `npm run typecheck` passes.
- **Assembled site:** built as the workflow does and served locally, every page returned 200.
- **Browser checks:** no sideways scrolling at 390 pixels and no script errors.

**Not yet checked:**

- the live deploy on GitHub Pages
- a real phone, Safari and Firefox
- a screen reader
- the owner's review of the voice and the look

## Build history, as recorded in the README

Moved here from the README on 24 November 2026, unchanged except for this heading. Lines that say
"not merged" or "not yet reviewed by Bradley" were true on the day they were written; the work was
merged later.

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

**WiseGeo, 22 November 2026:** a second example, Bradley's company site, as one static page for its
own Vercel project. Built and checked by Claude at 390 and 1280 pixels, served locally; not yet
deployed or reviewed by Bradley. Bradley Academy now links to it from home, About and the footer.

**Later, 22 November 2026:** after outside feedback that the site still did not read as a top
agentic engineer's, the home page leads with Bradley: a Harvard University graduate with twenty-five
years building software from MVP to global production, and a specialty in data prediction. Then the
systems he built (AISP, BAR Observatory) with determinism evidence from their repositories, the
notation, teaching at every level with Practical AI as his open-source teaching work, and his public
roles. WiseGeo became a short company page. Tested by Claude with `SITE_BASE=/` (direct loads of
`/research`, `/tools` and `/about`, assets and canonical URLs) and at 390 and 1280 pixels; not yet
reviewed by Bradley.

**22 November 2026, latest:** Site Studio became the publish-a-website lesson. A skill for any
chatbot (Level 1), GitHub Pages, your own domain and Vercel (Level 2), and Cloudflare, Google Cloud
and Supabase (Level 3), written from each provider's documentation with dated sources. No person and
no agent has followed the Level 1 to 3 guides yet.

**Users:** In use by people other than the author, from business owners to agentic developers (reported by Bradley, 22 November 2026); their results are not recorded here yet. The React guide was also followed twice by a fresh agent for an invented bakery.

**22 November 2026:** one new tool page, Research brief with checked sources. Built and type-checked,
and checked by an agent in headless Chrome at phone and desktop width: no sideways scrolling, no
console errors. The reviewers have not scored it.
The evidence is the rest of this page.
