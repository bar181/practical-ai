# Rare Find

<h3 align="center">A five-minute daily quiz on your phone, where the right answer nobody else thought of scores the most.</h3>

<p align="center">Project 4, a side quest: not everything you do with AI has to be work.</p>

**Are you an AI agent?** Go to [AGENTS.md](AGENTS.md) for instructions you can follow now.

> **Status: built and machine-tested, not yet played by people.** 82 of 82 automated checks pass at
> phone and desktop width. Nobody has played it in the real Claude artifact runtime yet. See
> [Status](#status).

**Think of it as** a pub quiz where the obvious answer is worth the least. Anyone can say "Eagle".
The person who says "Shoebill" takes the round.

<p align="center"><a href="https://claude.ai/artifact/HyfbDjPjofvRttRYKgMCis"><b>Play today's game</b></a> &nbsp;·&nbsp; <a href="../../docs/reports/rare-find.html"><b>How this game was made</b></a></p>

<p align="center">
  <img src="_build/img/how-it-plays.svg" width="720" alt="Animation: the prompt Name a bird with a timer ring, then four answers in turn with their points: Eagle, the crowd pick, 25; Flamingo, 9th most popular, 38; Hummingbird, right but beyond the top ten, a Good find, 80; Shoebill, rare and right, a Gem, 100. A bar grows with the points. The rarer the right answer, the more it scores.">
</p>

<p align="center">
<img src="_build/img/home-phone.webp" width="230" alt="Rare Find home screen on a phone: today's game with its date, a practice round button and three scoring labels">
<img src="_build/img/result-phone.webp" width="230" alt="A result on a phone: Eagle is the crowd pick for 25 points, Madame Zara comments, and the top ten shows points rising from 25 to 40">
<img src="_build/img/scorecard-phone.webp" width="230" alt="The Scorecard tab on a phone: today's score on a bar chart of the estimated spread, the week, the streak and a friends group">
</p>
<p align="center"><sub><b>Home:</b> today's game, practice, friends &nbsp;·&nbsp; <b>A result:</b> points, a host's comment, the top ten &nbsp;·&nbsp; <b>Scorecard:</b> your place on the chart</sub></p>

## Get started

**Play now in Claude:** [the Rare Find artifact](https://claude.ai/artifact/HyfbDjPjofvRttRYKgMCis).
**In any browser, no account:** [bar181.github.io/practical-ai/rare-find](https://bar181.github.io/practical-ai/rare-find/),
published by GitHub Actions whenever the game changes.

1. Download [`base/game.html`](base/game.html) and open it in any browser, on a phone or a computer.
   It plays in full with 125 built-in prompts. Nothing to install, no account.
2. For the Claude features, run it as a Claude artifact: upload the file to Claude and ask Claude to
   publish it as an artifact and declare its capabilities (`sample`, `db`, `user`, `room`). The game
   finds what is there and turns on what it can. Only the author has tried this route so far.

## How it plays

1. **Today's game:** five prompts, the same for everyone on the same date, such as **"Name a bird"**.
   A new set every day: a calendar fixes each date's five prompts in advance, and the game reads the
   date, so nothing has to be uploaded each day. Or a **practice round** of 5, 10, or **party mode**
   (25 prompts, grouped by topic), up to 100 practice prompts a day with no repeats. The timer is 30
   seconds, or 15 or 45 if you change it in settings.
2. Type one answer. Spelling slips are forgiven, and the game shows what it counted.
3. See your points, a comment from an AI host, and the top ten. The rare **Gems** stay hidden so you
   can play again.
4. At the end, see your place on a chart from 0 to a perfect score (500 for five prompts), then
   **challenge a friend**.

| Your answer | Points |
| --- | --- |
| The most popular answer | 25 |
| 2nd to 10th most popular | Rising to 40 to 60 for 10th place. It is 60 when there are few possible answers (countries of Africa) and 40 when there are hundreds (dog breeds) |
| Right, but not in the top ten | 80 |
| A rare right answer: a **Gem** | 100 |
| Wrong, or out of time | 0 |

Popularity is the AI's estimate, not a survey, and the game says so.

**Not on our list?** Press **Check with Claude**. Claude checks the answer is real and right,
forgives small slips, and rates it: common scores 80, rare 100, wrong 0. "big hero 5" for an animated
film counts as Big Hero 6, worth 80. Think Claude got it wrong? **Check again**, once. Without Claude,
**We allow it** is the room's word: 80.

**The hosts.** Professor Pedant 🎓, Mo Mainstream 🍿, Madame Zara 🔮 and Unit 7 🤖 take turns
commenting on each answer and its points. They tease the answer, never you. Pick one, or turn them
off, in settings.

## Share and challenge a friend

Rare Find is a solo game. Sharing is one link. At the end, add your name and press **Copy
challenge**. It copies one line and a link to the public web copy, for example
`https://bar181.github.io/practical-ai/rare-find/#c-RF1d48b5-201-gtguu-Bradley`. The link carries
your exact prompts and your score: your friend plays the same game in any browser, with no account,
sees your result after each answer, and gets a link of their own to send back. Paste it on your
**Scorecard** and you both appear on that game's scoreboard. No server, no sign-in, no cost.

**Settings** sit behind the gear icon, closed until you open them. They also say who made the game. **✕ Back to start** is on every
screen.

## The three levels

| Level | What you get | Needs |
| --- | --- | --- |
| **Level 1:** play | Today's game, practice rounds, the hosts' written lines, an estimated chart of how you compare, a week of scores in this browser | Any browser |
| **Level 2:** Claude joins in | Claude checks answers that are not on the list, and the hosts write fresh lines, on the player's own Claude plan | The Claude artifact |
| **Level 3:** on the web | A public copy anyone can open, published by GitHub Actions on every change, and challenge links that open it with your prompts and score | GitHub Pages |

**Where do the questions come from?** A JSON bank, [`_build/packs.json`](_build/packs.json): 125
prompts, each with a ranked top ten, five Gems and 20 or more other right answers, drafted by Claude
and checked by a script. A JSON calendar, [`_build/calendar.json`](_build/calendar.json), fixes each
date's five prompts (17 November to 11 December 2026 so far). After it ends, the game deals from the
whole bank, so a day is never empty. Both are built into the page: nothing is downloaded each day.

**Does GitHub run any AI?** No. GitHub Actions only builds, tests and publishes the page; the web
copy has no AI and no database. The AI check and fresh host lines run only inside the Claude
artifact, on each player's own Claude plan.

## What is in this folder

| File | What it is |
| --- | --- |
| [`base/game.html`](base/game.html) | The game: one self-contained page. Generated; change `_build/` instead |
| [`base/try-it-prompt.txt`](base/try-it-prompt.txt) | For a chatbot that cannot open the file: a prompt to build a simpler version. A draft, not yet tested |
| [`base/examples/sample-pack.md`](base/examples/sample-pack.md) | Every prompt with its estimated answers and points. It lists the hidden Gems, so it is a spoiler |
| [`level-2-files/game-review/`](level-2-files/game-review/) | The review skill: a 100-point rubric for fun, usability and fairness, used at the end of every build loop |
| [`quality-results/`](quality-results/README.md) | The evidence: the review loops, the automated checks and what is not tested |
| [How this game was made](../../docs/reports/rare-find.html) | An explainer page in the practical instructor voice: the steps, the levels and the mistakes to avoid |
| [`_build/`](_build/NORTH-STAR.md) | The source, the packs, the build and test scripts, the North Star and the research plan |

## Questions

**Does it cost anything?** No. In a browser it uses nothing outside the page. In a Claude artifact,
the AI features run on each player's own Claude plan.

**Can the AI change my score unfairly?** Listed answers are scored by the word list alone. Claude
only rules on an answer that scored 0, and only when you ask. It may fix your spelling, but not swap
in a different answer. Text that reads like instructions is never sent to it.

**Can someone game the spelling forgiveness?** It is harder now. About 1,700 real English words,
including their -ing, -ed and -s forms, never count as a slip. A slip inside a short word makes a
different word. The reviewers keep trying to break it.

**Is the chart real?** No: it is an estimate, a model of typical play averaging about 154 of 500,
and it says so on screen. There is no shared scoreboard; friends compare by challenge link.

## Status

**17 November 2026.** Built by its author with Claude. It has been tested by an automated playtest
(82 of 82 checks) and by fresh reviewer agents. Loops 0 to 3 scored 37, 68, 80 and 84 out of 100 on
the earlier office-ladder version, loop 4 scored an interim build 80, and loop 5 scored this version
71. All five of loop 5's top problems are fixed and checked by the playtest, but not yet re-scored.
Every Claude feature was tested against a mock, not the real artifact runtime. Not yet tried: real players, a real
multi-device game, a screen reader, and ChatGPT. The answer lists are Claude's estimates. The tier
names, prompts, hosts and lists are this project's own. [The evidence](quality-results/README.md).

## About Bradley Ross

<img src="../agentic-process/_build/img/bradley-ross-avatar.webp" width="110" alt="Cartoon avatar of Bradley Ross with a small friendly robot">

Made by **Bradley Ross**, who builds and teaches practical AI. Part of [Practical AI](../../README.md).
[linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)
