# Rare Find: North Star and implementation plan

Version 3, 17 November 2026: the simple version. A solo daily game, a JSON question bank and calendar, and one share link. Version 2 below added a shared scoreboard, friends groups and live rooms; the owner cut them for simplicity, and the sections on them are marked as removed.

Version 2, 17 November 2026. It replaces version 1 (the office ladder), after the owner played it
and asked for a solo daily game with a scorecard. The research, sources and copyright care in
[`PLAN.md`](PLAN.md) still stand.

## North Star

**A five-minute daily trivia game on your phone, where the right answer nobody else thought of
scores the most, and you can see how you compare.** One answer per prompt before the timer runs out.
Then a comment from an AI host with a sense of humour, the top ten, and your place against everyone.

**It succeeds when** a new player starts without instructions, at least one reveal gets a reaction
("nobody said that?"), they check their place on the chart, and they come back tomorrow.

## What changed from version 1, and why

| Version 1 | Version 2 | Why (the owner's words, shortened) |
| --- | --- | --- |
| Office ladder of four AI co-workers | Solo play: today's game and practice rounds | "The office ladder doesn't make sense. Keep it as a solo game" |
| Ranks 4 to 10 all near 50, then 5 more per rank | #1 25, rising to 40 to 60 for 10th place by category | "More variation"; 10th of few possible answers is rarer than 10th of hundreds |
| Gems shown on the reveal | Gems hidden; only their count shows | "Remove the rare finds from the list, in case people want to play again" |
| New category, fresh last prompt | Removed | "I do not understand the last round or topic section" |
| Settings card on home | A gear icon with an accordion, closed | "Move settings as an icon with accordion, default closed" |
| A final score | A Scorecard tab and a chart of your place, 0 to 500 | "An end of day score that compares to others ... a bar chart with an estimated distribution" |
| Co-workers' trash talk | Four AI commentator personas | "Unique personas and some humour in the comments" |
| Claude judges unlisted answers on its own | "Check with Claude", then "Check again" | "Have 'We allow it' be the LLM check ... allow a check again" |

## The levels

| Level | What the player gets | Needs | Without it |
| --- | --- | --- | --- |
| **1. Play** | Today's game (same five prompts for everyone on a date), practice rounds, the timer, forgiving spelling, the top-ten reveal, the persona commentators' written lines, the estimated chart, a week of scores in this browser | A browser | Always works |
| **2. Claude joins in** | Claude checks answers that scored 0; the hosts write fresh lines; on the player's own Claude plan | The Claude artifact: `sample` only | "We allow it" is the room's word; written lines |
| **3. On the web** | A public copy published by GitHub Actions on every change; challenge links that open it with your prompts and score | GitHub Pages | The file still works anywhere |

## Scoring

| Answer | Points |
| --- | --- |
| #1 most popular | 25 |
| #2 to #10 | Rising evenly to the category's 10th-place value |
| 10th place | 40 to 60: 60 for a small answer space (countries of Africa), 40 for a large one (dog breeds, superheroes) |
| Right, not in the top ten | 80 |
| A Gem (rare, right) | 100 |
| Wrong or out of time | 0 |

A perfect game is 500. The home screen shows three labels only: Popular 25+, Rarer up to 80, Gem 100.

**Check with Claude.** An answer that scored 0 and has text can be checked. Claude is told the
prompt, the top ten and the answer, as data, and asked whether it is real and right, forgiving small
slips ("big hero 5" is Big Hero 6), and whether it is common (80) or rare (100). A listed answer gets
its listed points. Claude may fix spelling but not swap in a different answer. Text that reads like
instructions is never sent. A second look is allowed once. Claude unreachable or absent: "We allow
it", the room's word, 80. The game never waits more than 4 seconds; a late verdict still counts.

**The estimated chart.** Until 5 real players have scores for the day, the chart shows a model of
typical play (per prompt: about 30% miss, 33% top three, 21% ranks 4 to 10, 14% beyond the top ten,
2% Gems). That gives an average of about 154. It is labelled as an estimate everywhere.

## Challenge codes: the simple way to join

The owner's story: "I share the artifact, I send a link with the game and my score, others play the
same game in their own chatbot, and the scoreboard for that day includes them."

A code carries everything: `RF1` (format), one base-36 character per prompt (its place in the pack
list, which only ever grows at the end), the score, one letter per answer's result, and a name. For
example, `RF1a3k0p-245-cptgd-Sam`. The end screen shows one challenge link, the published artifact's
link plus `#c-<code>`, and "Copy challenge link" copies it with one line of invitation. A Claude
artifact passes a plain `#name` to the page, so the link opens straight into the challenge. The page
cannot learn its own claude.ai link, so the main game's link is built in; a copy published elsewhere
sets its own in settings. The friend plays exactly those
prompts and sends their own code back. Pasting it on the Scorecard adds them to that game's
scoreboard. Both players keep the board locally. No server, no account, and no AI are needed, so it
works in Claude, in a browser, or wherever the file opens. If the code is today's game and the
friend has not played yet, it counts as their daily game.

## Prompts per game

5 (default), 10, or party mode: all 25 prompts, grouped by topic, with "Topic 2 of 8" on each
prompt. Today's game is always 5, so daily scores compare. The chart and the perfect score scale with
the count (100 per prompt).

## The commentators

| Persona | Character |
| --- | --- |
| 🎓 Professor Pedant | A fussy trivia professor who grades every answer and adds footnotes |
| 🍿 Mo Mainstream | Loves whatever everyone loves; baffled by anything obscure |
| 🔮 Madame Zara | A dramatic fortune teller who foresaw every answer |
| 🤖 Unit 7 | A literal robot that reports odds and enjoys it too much |

They take turns, or the player picks one. Each comment names the answer and its points. They tease
the answer, never the player. The written line shows at once; with Claude, a fresh line replaces it.

## Feel

Version 4 (18 November 2026), on the owner's brief: a quick game people want to replay, with the
rhythm of a match-three game. Small rewards for ordinary answers, one memorable payoff for a Gem,
and the focus on the moment an answer lands.

| Answer | What happens |
| --- | --- |
| Popular, in the top ten | Its row lights up and says "Yours"; the score ticks with "+N" |
| Good find | It lands above the top ten with a purple entrance; a bigger score tick |
| Gem | A faceted gem drops in under the score, catches the light, sheds fragments, and +100 flies into the score. No confetti |
| Not on our list | Says so at once. "Check with Claude" (or "We allow it") sits beside Next. A changed verdict plays its reward once |
| Wrong, or out of time | A short shake, and Next pulses once |

Budgets: on screen within 100 ms, ordinary effects 150 to 250 ms, the Gem reveal inside 600 ms.
Next works after a 120 ms guard, during effects, host lines and Claude's checks. The host's
ready-made line shows at once; Claude's fresh line replaces it only while that prompt is on screen.
A late verdict changes its own round's points and dot, quietly, never the screen. The five dots show
each outcome by colour and shape, with the names in words for screen readers, and carry into the
scorecard and the spoiler-free challenge message. Reduced motion keeps every result and drops the
movement. Sound is for a second pass, if testers want it.

## Phone first

The base styles are for a 360 to 430 px phone: one column, 44 px or larger touch targets, a sticky
Next button, settings tucked away. One wide-screen rule set adds two columns at 760 px and up.

## Architecture

One HTML file, no outside files, fonts or libraries. Capabilities are found at run time with
`claude.use(name)`, and each feature lights up only when its capability resolves.

```
_build/packs.json ──┐ (25 packs, each with ranked, gems, good, wrong and its 10th-place value)
_build/game.src.html ┴─> build.py ─> base/game.html and base/examples/sample-pack.md
falsematch.py: real English words, with their suffixes, that must never count as a spelling slip
playtest.py:   plays the built game at 390 and 1280 px, offline and with a mock of Claude
add_packs.py:  the second set of nine packs
.github/workflows/rare-find-pages.yml: build, check the committed copy matches, playtest, publish to Pages (main only)
```

**Today's prompts.** Each cycle shuffles all 25 packs with a seed and deals five a day, so everyone
gets the same set on the same date and no day repeats the day before.

**Data (removed in version 3).** `board/<id>`: name the player chose, friends group code, and the last 30 days of daily
scores. Everyone with access reads it; each player writes only their own row. Settings and history
also stay in this browser.

**Live play (removed in version 3).** The host joins room `rf-<code>` and emits the full state (packs, prompt, deadline) on
each prompt; players emit their total. Messages can drop, so every message carries the full state.

## Questions: a JSON bank and a JSON calendar (version 3)

`_build/packs.json` holds 125 prompts. `_build/calendar.json` fixes each date's five prompts from
17 November to 11 December 2026; `make_calendar.py` appends days for new prompts and never changes a
day already in the calendar. After the calendar the game deals from the whole bank. Practice is up to
100 prompts a day with no repeats, never today's five. GitHub Actions runs no AI: it builds, tests
and publishes.

## Risks

| Risk | Handling |
| --- | --- |
| Answer lists are estimates and some will be argued | Labelled as estimates; Check with Claude |
| A player tries to talk the judge into points | Answers that read like instructions are not sent; the answer is sent as data; Claude may only fix spelling |
| 25 packs repeat after 5 days | Practice rounds help; more packs are the next content job |
| The estimated chart is wrong for real players | Labelled; replaced by real scores at 5 players |
