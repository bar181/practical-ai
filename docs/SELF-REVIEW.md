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

| Tool | Before | After | Weakest item now |
| --- | --- | --- | --- |
| 1. Artifact studio | 61 | 77 | Reuse before build (58), evidence (62) |
| 2. Voice post drafter | 57 | 64 | Evidence (30) |
| 3. Short video guide | 55 | 62 | Quality of the demo (35) |
| 4. Estimator | 66 | 71 | Evidence (50) |
| 5. Training explainer | 51 | 58 | Evidence (30) |

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

## How to run the next round

1. Pick the tool with the lowest overall score, or the one you need next.
2. Fix its weakest item first. Do not polish a strong item.
3. Score again and add a row to the round summary with the date.
4. When "evidence" is the weakest item, stop building and get someone to use the tool.
