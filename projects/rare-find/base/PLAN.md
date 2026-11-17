# Rare Find

One-line promise: a quick game you play with your AI and your co-workers, where the right answer
nobody else thought of scores the most.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner to intermediate | Done, 17 November 2026 | Drafted (the prompt in [`try-it-prompt-draft.txt`](try-it-prompt-draft.txt), not yet run) | This folder |

**Think of it as:** a pub quiz where the obvious answer is worth the least. Anyone can say
"lightsaber". The person who says "the Kragle" gets the round.

**Project 4, and a side quest.** The other projects are about work. This one is a reminder that
working with AI as a digital co-worker includes the fun part of having co-workers: a five-minute
game at the end of a meeting, made by the AI you already use.

## Overview

The chatbot picks a category (or you give it one), works out the ten most popular answers and a
handful of rare correct ones, and builds a small game page right in the chat. You get 30 seconds
per prompt to type one answer. A correct answer scores 25; the rarer it is, the more it scores, up
to 100. Spelling mistakes are forgiven. At the end of each prompt the board shows what was popular
and what was rare, which is half the fun.

## Who it is for

A team or a family who wants a light, shared break, led by whoever has a chatbot open.

## Scope

- **In (Level 1):** one copy-paste prompt. The chatbot researches one to five category prompts and
  builds one HTML game page with the answers inside it: a 30-second timer, one answer per prompt,
  forgiving spelling, five scoring tiers, a reveal board after each prompt, and a final score.
- **Out:** accounts, saved scores, leaderboards and many players at once (Level 2); a daily game
  for everyone (not planned); real survey data (the popularity is the AI's estimate, and the game
  says so); prompts on politics, religion or anything a co-worker could find hurtful.
- **It works when:** a fresh chat given the prompt and the category "Name a fictional weapon"
  builds a page that runs in the chat. "Lightsaber" scores 25, "light sabre" also scores 25 with a
  "counted as Lightsaber" note, "ray gun" scores 35 or 50, "the Kragle" scores 100, "spoon" scores 0,
  the timer stops input at 0, and the reveal board shows the top ten and the rare answers.

## How the game plays

1. **The prompt appears** with a 30-second ring timer (15, 30 or 45 seconds, chosen at the start).
2. **Type one answer** and press Enter. One try per prompt: the fun is the bet on a rare answer.
3. **The score lands,** with the tier name and, if the spelling was fixed, what it was counted as.
4. **The reveal board** shows the ten most popular answers, the rare answers, and where yours sat.
5. **After the last prompt,** the total out of 100 per prompt, and a "play again" button.

### Scoring

| Tier | What it means | Points |
| --- | --- | --- |
| **Crowd pick** | The most popular answer | 25 |
| **Popular** | Second or third most popular | 35 |
| **Solid** | Fourth to tenth most popular | 50 |
| **Good find** | Correct, and not in the top ten | 75 |
| **Gem** | On the list of rare correct answers | 100 |
| **Miss** | Wrong, or out of time | 0 |

Every correct answer earns at least 25; rarity adds up to 75 more. The tier names are this game's
own. They do not borrow another game's names.

### What counts as correct

- **Normalise first:** ignore case, accents, punctuation, spaces and hyphens, and a leading "the",
  "a" or "an". "The light-saber" and "lightsaber" are the same answer.
- **Aliases:** each answer carries its other names ("Thor's hammer" for Mjolnir).
- **Typos:** answers of four letters or fewer must match exactly. Five to eight letters allow one
  slip; nine or more allow two. Numbers must match exactly. The page always says what it counted.
- **Not on the list:** the page cannot judge an answer it does not hold, so each prompt carries a
  long list of accepted answers (the top ten, the gems, and about 30 more good finds). An answer not
  on it scores 0 with a "Not on our list: ask your chatbot" button that copies the answer, so the
  player can appeal in the chat. In Claude, where a game page can call Claude itself, it can ask
  instead (Level 1 option, not required).

### Where the answers come from

The chatbot builds each prompt's answer list before the game starts, using web search where it has
it and its own knowledge where it does not. **Popularity is the AI's estimate, not a survey,** and
the page says so on the reveal board. Level 2 replaces the estimate with what your own players
actually answer.

## What might be involved at each level

| Level | What it involves | Complexity |
| --- | --- | --- |
| Base | The plan, the draft prompt, a sample pack of three prompts and the image list, in this folder | |
| Level 1, Beginner: the simplest version that works | Paste one prompt into the chatbot you use, with a category or "surprise us". The chatbot researches the answers and builds the game page in the chat (a Claude artifact, a ChatGPT or Gemini canvas, or an HTML file to open). Play it on a shared screen. Check the reveal board and appeal any answer you think was wrong | Beginner |
| Level 2, Advanced: repeatable | A Google Sheet with three tabs (questions with their ranked and rare answers, players, scores) linked through the Google Drive connector, or a Claude game page with shared storage; several players, saved scores, and rarity updated from your team's own answers | Intermediate |
| Level 3, Expert: connected and automated | None planned. A weekly game posted to a team channel on a schedule is the obvious next step if Level 2 gets regular use | Advanced |
| Explainer | The README: what it is, the rules, the scoring table, one prompt to try, and the sample pack | Part of every delivery |
| Commercial grade | Real answer data from many players, moderation of player answers, and hosting | Explained, not built here |

## Established best practices

Checked 17 November 2026.

1. **Reward the correct answer few people give, and score a wrong answer at zero.** That trade-off
   is what makes the game tense and fair. Sources: [Pointless, Wikipedia](https://en.wikipedia.org/wiki/Pointless);
   [a Krillion guide](https://aiidelist.com/blog/krillion-game-guide-how-to-play-rare-answers).
2. **A short, fixed timer per prompt.** It keeps the pace up and stops searching. Krillion uses
   seven prompts of 25 seconds each. Source: [a Krillion guide](https://aiidelist.com/blog/krillion-game-guide-how-to-play-rare-answers).
3. **Accept aliases and small typos, and show what was accepted.** Players forgive a strict quiz
   less than a lenient one. Source: [an answer site's note that Krillion accepts unpublished aliases and autocorrects small typos](https://www.thewordfinder.com/misc-solvers/krillion-answers/).
4. **Normalise text before fuzzy matching, use edit distance for short answers, and match very
   short answers and numbers exactly.** Most "typos" disappear after normalising; edit distance
   handles the rest without accepting a different word. Sources:
   [normalise first](https://codemia.io/knowledge-hub/path/comparing_strings_with_tolerance);
   [Levenshtein for short quiz answers](https://tfoucher5.github.io/guess-rater/recipes/quiz-answers.html);
   [exact match for short answers and numbers](https://triviamaker.com/?p=87520).
5. **Borrow the mechanics, never the expression.** Copyright does not protect a game's idea or
   method of play, but the text of its rules, its art and its branding are protected or trademarked.
   Source: [U.S. Copyright Office factsheet FL-108](https://webarchive.library.unt.edu/web/20170124184513/https://www.copyright.gov/fls/fl108.pdf).
6. **Expect a game page to forget scores unless it has storage.** A chat game resets on reload; a
   Claude artifact can keep data with persistent storage on paid plans, and can call Claude while it
   runs. Sources: [Claude Help Center on artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts);
   [a guide noting scores reset without storage](https://fast.io/resources/claude-artifacts-guide/).

## Keeping it clear of copyright and trademark

- **Our own name, tier names, look, prompts and answer lists.** Nothing is copied from Krillion,
  Pointless or any answer site: no tier names, no daily prompts, no answer sheets.
- **Pop culture as answers, not as pictures.** Naming a film's weapon is a fact; showing it is not
  ours to do. No character, logo, film still or game art appears in the game or the images.
- **No quotes or lyrics** as prompts or answers.
- **Every image is made for this project** from the prompts in [`images.md`](images.md), which
  name no character, brand or artist. Its origin is recorded when it enters the repository.

## What it reuses

- **The chatbot's own game pages:** Claude artifacts, and ChatGPT and Gemini canvases, already
  build and run small HTML games in the chat. Nothing to install.
- **The chatbot's web search** to rank answers, where it has it.
- **Artifact Studio** for the look of the game page, if the person wants it styled.
- **Level 2:** the Google Drive connector and Google Sheets, or Claude's artifact storage, for
  scores. Reviewed, not selected.

**Stop-rule check:** Krillion is a free daily rare-answer game in the browser. It does not let you
pick the topic, run in your chatbot, or play your own team's trivia, so a tool here is worth it.

## Decisions to record during research

- [x] **Reuse check:** built-in chat game pages and web search cover the engine. Krillion covers a
  public daily game, not a team game on your topic. Build Level 1 as a prompt.
- [x] **Build or license:** Level 1: build a prompt, a sample pack and the matching rules. Level 2:
  options reviewed (Google Sheet with the Drive connector; Claude artifact storage), not selected.
- [x] **Dependencies and pricing:** Level 1 needs any chatbot that can show an HTML page, or a
  browser to open the file. No cost beyond the chatbot.
- [ ] **Where it lives:** Level 2's choice between a Google Sheet and artifact storage waits for
  Level 1 to be played.

## First step

1. Run the draft prompt in a fresh chat with the sample category "Name a fictional weapon", and
   check it against "It works when" above.
2. Fix what that run finds, then run it in a second chatbot.
3. Make the images on the list, then write the README's showcase.

Level 2 is planned in detail only after Level 1 has been played by a team.

## Open questions

- Does a ChatGPT or Gemini canvas run the timer and input as well as a Claude artifact? Not tested.
- Can the Google Drive connector write scores to a Sheet, or only read it? The sources disagree.
  Check before Level 2.
- Should players see the answer list size (for example "48 accepted answers")? It helps fairness
  and hurts suspense. Decide after play.
- One answer per prompt, or up to three with the best one counting? One is the default; test both.
