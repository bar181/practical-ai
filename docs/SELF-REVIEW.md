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
| 8. Inbox triage and daily summary | none | none | 64 | Evidence (30). Landscape review done in round 3 |
| 9. Weekly brief with research | none | none | 63 | Evidence (30). Landscape review done in round 3 |
| 10. Dashboard | none | none | 67 | Evidence (30). Landscape review added after the first draft |

Round 1 added skills, agent guides and the upper levels. Round 2 fixed the weakest fixable item it
found, the quality of three demos, by building a page for each with the artifact studio's own
skeleton and look. After round 2, the weakest item for every tool is evidence. By the rule at the
end of this file, building stops there until other people have used the tools.

## Artifact studio

"Before" is the single-page photo gallery. "After" is the studio with all levels, as it stood at the end of round 2. Round 3 below changes three of these scores.

| Item | Before | After | What changed |
| --- | --- | --- | --- |
| Teaching and promo value | 85 | 90 | Seven full voice pages and four recipe pages, each with "Behind this page" |
| Quality of the demo | 80 | 86 | Each voice has its own type, colour and behaviour |
| Easy for a non-coder | 70 | 76 | A tap-to-choose request mixer on the level 2 page, and the sentence under every example. Sentences still untested |
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

- Run the sentence test: `drafts/artifact-studio/base/sentence-test.md`.
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

The dashboard has since had its landscape review done, with dated sources, so its plan now says
"done". The inbox summary and the weekly brief had theirs done in round 3, below.

The dashboard demo is the only one of the three that works on a person's own data: it builds
tiles, a trend and a table from pasted rows, in the browser.

## Round 3: the first outside look at the studio

The repository owner opened the studio artifact on a phone. This is the first use by anyone other
than the author, and it found a failure the automated checks could not.

What was reported: the examples could not be found, the first screen showed dropdown menus with
no content under them, each voice was expected as its own tab, and one artifact per level was
expected.

What was wrong: the first tab was a sentence builder made of three dropdowns. Tabs were links
switched by a script, so one script problem in the viewer leaves every tab empty. Voices and
recipes sat one level down, behind index cards. All three levels shared one page.

What changed:

- Tabs are radio buttons styled as tabs. They switch with scripts turned off, and the first tab is
  showing on load. Each voice and each recipe has its own tab.
- Each tab's script is in its own script element. In the first version every tab's script
  shared one element, so a single fault would have left every tab without its set-up. That is
  the most likely cause of what the owner saw, and it is not proven. Breaking one tab's script
  on purpose now leaves the others working.
- The dropdowns are gone. The request mixer uses tap-to-choose buttons and starts with a complete
  request already written out.
- Four pages are built from one source: all examples, and one page per level.
- The keynote page opened on an empty black screen below the tabs. Its first screen is now short
  enough that the headline shows at once.

| Item | Round 2 | As the owner found it | Round 3 | Why |
| --- | --- | --- | --- | --- |
| Easy for a non-coder | 76 | 50 | 74 | The owner could not find the examples. Fixed, and the fix is not yet confirmed by the owner |
| Fits the level ladder | 88 | 88 | 90 | Each level has its own page |
| Evidence | 62 | 62 | 64 | One outside user, one failure found. Tabs tested with scripts off at three widths |

Overall for the studio: 77 at the end of round 2 by the author's own scoring, 73 as the owner found
it, 77 after the fix. The lesson is the rule at the end of this file: the author's score for "easy"
was 26 points higher than the first real user's experience.

The same test was then run on the nine other demo pages, with scripts turned off:

| Demo | At rest, with scripts off |
| --- | --- |
| Inbox summary, weekly brief, learning system, voice post drafter, publishing a website | Readable. The content is in the page |
| Estimator | Headings only. Every figure is worked out by script |
| Short video, training explainer | Text is readable. The player frame is empty |
| Dashboard | Sample rows show. Tiles and chart are empty |

What was done about it:

- All nine carry a one-line notice that shows only when scripts are off.
- The four that depended on script now have their starting state written into the HTML: the
  estimator's first quote, the dashboard's tiles and chart for the sample rows, and the first beat
  of each player. Each was kept only after a check that the live page, with scripts on, has the
  same text and the same number of elements as before.
- The estimator's business picker was appended on every start. It now clears itself first.
- With scripts off, the estimator's number boxes show empty, because their values are set by
  script. The quote beside them is correct for the starting job.

The rule that came out of this is the new "Complete at rest" section of the skill's build rules,
and one new line in the pre-ship checklist.

Still not checked: the pages inside the artifact viewer on a phone, by the author. The author
cannot see that viewer. Confirmation has to come from the owner.

## Round 3: landscape reviews for tools 8 and 9

Both tools had been started from notes, which broke the research-first rule. Each now has a
landscape review from dated sources, and each review changed the tool.

| Tool | What the review found | What changed |
| --- | --- | --- |
| Inbox triage and daily summary | Sorting by action is settled practice. Mail products are building the same page. Hidden instructions in mail are a documented risk with no complete fix. The official pages for one assistant disagree about plans | The skill and the project instructions now flag any request to change payment details. The review tells readers to check their own mail product first |
| Weekly brief | Every source says to open with the bottom line, including the ask and its date | The opening three lines must now state any decision needed and by when, or say that none is |

Evidence for each moves from 20 to 30: the research rule is now met, and nobody has used either
tool. By the plain average of the seven items, the inbox summary moves from 62 to 64 (446 of 700)
and the weekly brief from 62 to 63 (443 of 700). The round summary showed 60 for both, which was
below their own item scores. It now shows the plain averages.

The estimator had the same gap in a milder form: its tool facts were checked and it had no
landscape review. It has one now. The finding that changed the tool is that an estimate and a
quote can commit a business to different things. The skill now uses the business's own word,
heads every draft as a first draft that is not an offer, and asks how long prices hold. Its score
stays at 71: nothing about its evidence changed.

The last three tools without a review now have one, so all ten do.

| Tool | What the review found | What changed |
| --- | --- | --- |
| Voice post drafter | Assistants already build a style from writing samples. Guides say paired examples teach a voice fastest | The voice file has a "this is me, this is not me" section and asks for a reason beside each rule. The review says to try the built-in style first |
| Short video guide | The first two to three seconds decide, and many people watch muted. The sources' figures for how many disagree widely and are left out | The script skill and template gain a sound-off check on the opening |
| Training explainer | Published research supports teaching in learner-paced pieces. Watching time tops out near six minutes. A critique notes that watching is not learning | Lessons over six minutes are split. The guide asks for questions at the end as the check on learning |

None of these scores changes. Research was not what held them down. Evidence of use is.

The sources are trade and vendor guides plus security firms' reports, not studies. The training
explainer is the exception: its review rests on published research. Prices and
plan details were not checked, and the reviews say so.

## Round 4: a base, and levels that add to it

The owner reviewed the pages and asked whether the level folders were the right shape for a
repository that ships a usable product. They were not. Each level had its own page, and the
examples were divided between the levels by teaching order: recipes on one page, voices on
another. Someone who wanted "the thing" had to visit three places.

The artifact studio now trials a different shape.

| | Before | After |
| --- | --- | --- |
| Where the examples are | Split across four pages, by level | One studio page, and each example again as a file of its own, all in `base/` |
| What a level folder holds | A page, plus a copy of some of the examples | Only what that level adds |
| What decides the level | How much the person has learned | What the person must depend on: nothing, files, or connections |
| Level 1 | A page of recipes and parts | Two files: instructions for the assistant, instructions for the person |
| Level 2 | A page of voices, looks and templates | A preferences file, and the skill installed |
| Level 3 | A page of the skill's documents | A list of connection slots. Nothing built |

What this changes in the scores: nothing yet. The rubric item "fits the level ladder" measured
fit to the older folders, so it is not rescored here. The honest gain is that there is one place
to look and no copy of an example to keep in step. The honest cost is that level 3 is now visibly
empty, where the older "expert" page made it look finished.

The other nine tools still use the older folders. Converting them is a decision for the owner,
after this one has been looked at.

## Round 5: the studio becomes a library

The owner proposed eight additions and asked for each to be judged before it was built. All eight
were judged worth doing and were built in one sitting. The full account, with how to use each, is
[`reports/2026-11-15-artifact-studio-library.md`](reports/2026-11-15-artifact-studio-library.md).

| Addition | Value, out of 100 | State |
| --- | --- | --- |
| A templates folder with an index for people and one for agents | 92 | Built. Both indexes are generated |
| Options for each template, reachable from the index | 88 | Built |
| Recommending a combination from the requirements | 84 | Built. The page and the Python rules agree on all 120 requests |
| An MCP server and a front door for agents | 82 | Built. Tested with a client only |
| Decks and social formats | 80 | Built: four decks, five formats |
| Animated SVG, and GIF copies | 80 | Built: twelve and eleven |
| A way in for new ideas | 78 | Built. No real find has been through it |
| A list of outside skills, frameworks and services | 70 | Built, dated, prices left out |

Scored on a rubric that fits what the tool now is:

| Item | Score | Why |
| --- | --- | --- |
| One place for each thing, one source of truth | 88 | One catalogue feeds the index, the page and the server. Indexes, counts and starters are generated |
| Usable by an agent | 87 | A front door, a machine index, starters, nine tools. A scripted agent finished a file |
| Correct and checked | 85 | Automated checks pass. They missed three faults that the agent run found |
| Honest and current documents | 85 | Status lines say who has and has not tried each thing |
| Usable today by a person | 81 | Open, pick, copy, ask |
| Range and quality of templates | 81 | Four decks cover selling, inspiring, deciding and teaching. Social is one family of pictures in three styles |
| Evidence from real use | 40 | The owner has looked at the pages. One scripted run. Nothing else |

Overall 78, the plain average. This is a different rubric from rounds 1 to 3, so it is not
comparable with the 77 there. The earlier rubric measured a set of pages. This one measures a
library with delivery.

Three things in this round came from testing the work against itself and not from the proposal:

1. **A scripted agent.** A script used only the MCP server to pick a deck, fetch it and fill it. It
   failed three times: the tool returned markup without the script that makes it a deck; a comment
   that spelled out a tag was matched as a slide; and arrow keys did nothing until the deck was
   clicked. Each is fixed, and the script is kept as `level-3/mcp/example_agent.py`.
2. **Every request through the picker.** For a deck to report or to get a decision, the best answer
   scored 0 to 6 out of 15 and was given without comment. Two decks were added for those jobs, and
   every answer is now marked strong, fair or weak. Deck requests with a best answer under 10 fell
   from 20 to 11. The picker's agreement between the page and Python is a saved test.
3. **Starters.** A template that shows well is a poor thing to copy. Each deck and social picture
   also exists as a small complete file.
4. **The inbox read back.** Saved finds could be filed and never read. They are now step 3 of the
   agent's path and an MCP tool, so a person's taste shapes the choice.

Also added after the gap analysis: three styles for the social pictures, each checked for contrast,
with downloads that follow the chosen style.

Other faults found by the checks and fixed: a shared helper that made SVG elements where HTML ones
were needed, which left both decks blank and the picker dead until a screenshot caught it; SVG
styles that would have clashed when two files were pasted into one page; a slide photograph cut to
three quarters of its width; a PDF print that put each slide in the top third of a tall page; and a
deck control bar that ran off the side of a 320 pixel screen.

What this round did not change: evidence from people. It added a great deal of surface, and every
new part of it is untested by anyone else. The rule at the end of this file applies with more force
now.

## What only other people can do next

After round 3 the weakest item for every tool is still evidence, and the author cannot raise it
alone. In order of value:

1. **Open the four studio artifacts on a phone** and say whether every tab shows content. This
   confirms or refutes the round 3 fix. Five minutes.
2. **Run the sentence test.** The beginner sentence for each of the four recipes, in two
   assistants, with the sheet in `drafts/artifact-studio/base/sentence-test.md`. About an
   hour.
3. **Give the artifact-studio skill to a second agent** with one set of real notes, and compare
   what comes back against the pre-ship checklist.
4. **Watch one person do level 1 of any tool** without help, and write down where they stop.
5. **Put one real price list and rule page through the estimator.**
6. **Send the inbox assistant a message with a hidden instruction** and record whether it is
   reported or followed.

Until some of these are done, more building raises nothing but the author's own scores.

## How to run the next round

1. Pick the tool with the lowest overall score, or the one you need next.
2. Fix its weakest item first. Do not polish a strong item.
3. Score again and add a row to the round summary with the date.
4. When "evidence" is the weakest item, stop building and get someone to use the tool.
