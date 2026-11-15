# Self-review

A record of the score-and-fix loop run on the tools in this repository. Each round scores a tool
against the same rubric, names the weakest items, fixes what can be fixed, and scores again.

**Read this first.** Every score here was given by the author of the work, to the author's own
work. It is useful for finding the next thing to fix. It is not evidence that a tool works. Only
other people using it can show that.

## The rubric

Seven items, each scored from 1 to 100. The overall score is the plain average.

| Item | What a high score means |
| --- | --- |
| Easy for a non-coder | Someone with no technical background can use it from the guide alone |
| Reuse before build | It leans on what assistants, browsers and free tools already do |
| Fits the level ladder | Demo, simple, working, automated and commercial-grade all exist and connect |
| Business usefulness | It produces something a business needs, not only something impressive |
| Quality of the demo | The example is good enough to make someone want it |
| Teachable | A person can follow the guide, an agent can follow the skill |
| Evidence | Claims are checked, and someone other than the author has used it |

## Round summary, 15 November 2026

| Tool | Start | Round 1 | Round 2 | Weakest item now |
| --- | --- | --- | --- | --- |
| 1. Artifact studio | 61 | 77 | 77 | Reuse before build (58), evidence (62) |
| 2. Voice post drafter | 57 | 64 | 67 | Evidence (30) |
| 3. Short video guide | 55 | 62 | 66 | Evidence (45). The demo plays a script, not a video |
| 4. Estimator | 66 | 71 | 71 | Evidence (50) |
| 5. Training explainer | 51 | 58 | 61 | Evidence (30). The demo plays a plan, not a video |
| 6. Learning system | none | none | 69 | Evidence (35). New in round 2: demo, simple level, skill and outlines |
| 7. Publishing a website | none | none | 67 | Evidence (25). New in round 2. No route has been walked end to end |
| 8. Inbox triage and daily summary | none | none | 60 | Evidence (20). Research is notes only |
| 9. Weekly brief with research | none | none | 60 | Evidence (20). Research is notes only |
| 10. Dashboard | none | none | 64 | Evidence (25). Research is notes only |

Round 1 added skills, agent guides and the upper levels. Round 2 fixed the weakest fixable item it
found, the quality of three demos, by building a page for each with the artifact studio's own
skeleton and look. After round 2, the weakest item for every tool is evidence. By the rule at the
end of this file, building stops there until other people have used the tools.

## Artifact studio

"Before" is the single-page photo gallery. "After" is the six-tab studio with all levels.

| Item | Before | After | What changed |
| --- | --- | --- | --- |
| Teaching and promo value | 85 | 90 | Seven full voice pages and four recipe pages, each with "Behind this page" |
| Quality of the demo | 80 | 86 | Each voice has its own type, colour and behaviour |
| Easy for a non-coder | 70 | 76 | A sentence builder on the Start tab. Sentences still untested |
| Fits the level ladder | 60 | 88 | Every level folder written. The skill exists in a full and a single-file edition |
| Reuse before build | 45 | 58 | The skill loads a design skill when one is present. The demo itself still uses no libraries |
| Evidence | 45 | 62 | Three screen widths, an automated accessibility scan, link and arithmetic checks. No outside user |
| Business usefulness | 40 | 80 | A report, a proposal, an explainer and a landing page, each for a made-up business |

Found and fixed in this round:

- Dimmed text in two scrolling sections failed the contrast check. Raised, and the active step is
  now marked with a bar as well.
- Two button and badge colours failed contrast. Darkened.
- Tick marks in the comparison table had labels a screen reader would not announce. Fixed.
- Scrolling regions could not be reached by keyboard. Fixed.
- The comparison table overflowed a 320 pixel screen. Fixed.
- Text in three diagrams was too small on a phone. Redrawn.
- The chart tried to draw while its tab was hidden. Guarded.

Still open, and not fixable by the author alone:

- Run the sentence test: `drafts/artifact-studio/level-simple/sentence-test.md`.
- Have a second agent run the skill on fresh content.
- Watch one person do level 1 from the student guide.
- Check on a real phone, in Safari and in Firefox.
- Correct the practical instructor voice card.

## Tools 2 to 5

The same change was made to each: a skill, an agent guide, and outlines for the working,
automated and commercial-grade levels. The simple level and the examples were not changed.

| Item | Voice post drafter | Short video guide | Estimator | Training explainer |
| --- | --- | --- | --- | --- |
| Easy for a non-coder | 75 | 65 | 75 | 60 |
| Reuse before build | 60 | 80 | 55 | 75 |
| Fits the level ladder | 40 to 70 | 35 to 65 | 50 to 75 | 35 to 65 |
| Business usefulness | 80 | 70 | 85 | 65 |
| Quality of the demo | 60 | 35 | 80 | 40 |
| Teachable | 55 to 75 | 55 to 75 | 65 to 80 | 55 to 72 |
| Evidence | 30 | 45 | 50 | 30 |

A single number means the item did not change. "40 to 70" means before and after.

What would move each one most:

| Tool | Next fix |
| --- | --- |
| Voice post drafter | One real person builds a voice file and judges three drafts. That is the whole test |
| Short video guide | One finished video per route in the demo folder. A script is not a demo of a video |
| Estimator | Run each example through a fresh chat and compare totals with the worked examples |
| Training explainer | One finished video in one style, made from the beat sheet |

## Round 2: three demos

| Tool | Demo before | Demo after | What was built |
| --- | --- | --- | --- |
| Voice post drafter | 60 | 76 | A page that steps through one loop: voice file, point of view, draft with its voice traits marked, the flagged guess, and feedback becoming a rule |
| Short video guide | 35 | 60 | A page that plays a 20-second script beat by beat on a phone-shaped frame, with a word budget and a route chooser |
| Training explainer | 40 | 62 | A page that plays one beat sheet in two teaching styles |

Each page was checked at 320 and 390 pixels wide and with the automated accessibility scan: no
errors and no violations. The two video tools still have no finished video. That needs an outside
rendering service and the owner's own image and voice.

## Round 2: learning system, drafted from its plan

Built with the nine-step process: a short landscape review first (the known error database and
the lessons learned register are established practice, so their columns were reused), then the
simplest version that works.

| Item | Score | Why |
| --- | --- | --- |
| Easy for a non-coder | 72 | A spreadsheet and pasted instructions. Connecting the sheet differs by assistant and is unchecked |
| Reuse before build | 75 | Columns borrowed from established practice. Nothing built for the simple level |
| Fits the level ladder | 72 | Demo and simple level drafted. Working, automated and commercial levels outlined |
| Business usefulness | 78 | Starter entries for a business, for developers and for home |
| Quality of the demo | 72 | A searchable log with status, counts and a draft-entry form. It saves nothing |
| Teachable | 78 | Student guide, agent guide and the `learning-log` skill |
| Evidence | 35 | Checked in Chrome and by the automated scan. Never used on a real log |

## Round 2: publishing a website, drafted from its plan

| Item | Score | Why |
| --- | --- | --- |
| Easy for a non-coder | 68 | Three routes in plain words. The steps describe the routes and are not click-by-click |
| Reuse before build | 85 | Nothing is built. It uses the assistant's sharing and free static hosts |
| Fits the level ladder | 70 | Demo and simple level drafted. Upper levels outlined |
| Business usefulness | 80 | Every page made with the other tools needs this step |
| Quality of the demo | 65 | A route chooser and a pre-publish check. It publishes nothing |
| Teachable | 78 | Student guide, agent guide and the `publish-check` skill |
| Evidence | 25 | Host facts come from dated sources. No route was walked for this draft |

## Round 2: tools 8, 9 and 10, started from their plans

These three were taken only as far as the simple level, a sample page, a skill and outlines. They
break the repository's own rule that research comes first: each has landscape notes written from
general knowledge, clearly marked, and no checked sources. Their plans say "notes only". The
review is the next step for each, before anything else is built on them.

| Item | Inbox summary | Weekly brief | Dashboard |
| --- | --- | --- | --- |
| Easy for a non-coder | 65 | 68 | 72 |
| Reuse before build | 70 | 70 | 70 |
| Fits the level ladder | 65 | 65 | 65 |
| Business usefulness | 82 | 78 | 82 |
| Quality of the demo | 62 | 60 | 72 |
| Teachable | 72 | 72 | 72 |
| Evidence | 20 | 20 | 25 |

The dashboard demo is the only one of the three that works on a person's own data: it builds
tiles, a trend and a table from pasted rows, in the browser.

## How to run the next round

1. Pick the tool with the lowest overall score, or the one you need next.
2. Fix its weakest item first. Do not polish a strong item.
3. Score again and add a row to the round summary with the date.
4. When "evidence" is the weakest item, stop building and get someone to use the tool.
