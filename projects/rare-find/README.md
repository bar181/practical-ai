# Rare Find

<h3 align="center">A quick game with your AI and your co-workers, where the right answer nobody else thought of scores the most.</h3>

<p align="center">Project 4, a side quest: not everything you do with AI has to be work.</p>

**Are you an AI agent?** Go to [AGENTS.md](AGENTS.md) for instructions you can follow now.

> **Status: a plan, not built yet.** The rules, the scoring and a draft prompt are ready. Nobody has
> played it. See [Status](#status).

**Think of it as** a pub quiz where the obvious answer is worth the least. Anyone can say
"lightsaber". The person who says "the Kragle" takes the round.

## Why a game?

Working with AI as a digital co-worker includes the part where co-workers have fun together. Rare
Find is a five-minute break at the end of a meeting: your chatbot picks a category, works out what
most people would say, and builds the game in the chat. You play on a shared screen.

## How it plays

1. A prompt appears, such as **"Name a fictional weapon"**, with a 30-second timer.
2. Type one answer. Spelling slips are forgiven, and the game shows what it counted.
3. Score it, then see the board: the ten most popular answers and the rare ones.

| Your answer | Points |
| --- | --- |
| The most popular answer | 25 |
| Second or third most popular | 35 |
| Fourth to tenth | 50 |
| Correct, and not in the top ten | 75 |
| A rare one: a **Gem** | 100 |
| Wrong, or out of time | 0 |

Popularity is the AI's estimate, not a survey, and the game says so.

## Get started

**Not built yet.** The draft prompt is in [`base/try-it-prompt-draft.txt`](base/try-it-prompt-draft.txt):
one paste into the chatbot you use, with your own category or "surprise us". It has not been run;
the first test is the next step in [the plan](base/PLAN.md#first-step).

| Level | What it will be |
| --- | --- |
| **Level 1:** one prompt | Paste it, play the game page the chatbot builds in the chat |
| **Level 2:** play as a team | A Google Sheet of questions, players and scores, or a Claude game page that saves scores; rarity learned from your own players |
| **Level 3** | None planned yet |

## What is in this folder

| File | What it is |
| --- | --- |
| [`base/PLAN.md`](base/PLAN.md) | The plan: scope, rules, matching, levels, best practices with sources, copyright care, open questions |
| [`base/try-it-prompt-draft.txt`](base/try-it-prompt-draft.txt) | The Level 1 prompt, a draft, not yet run |
| [`base/examples/sample-pack.md`](base/examples/sample-pack.md) | Three prompts with estimated answers, to test with |
| [`base/images.md`](base/images.md) | Five images to make, each with a prompt under 25 words |

## Status

**17 November 2026.** A plan by its author with Claude. Nothing is built, and nobody has played it,
in any chatbot. The sample answers are Claude's estimates. The tier names, prompts and answer lists
are this project's own. [The evidence](quality-results/README.md).

## About Bradley Ross

<img src="../agentic-process/_build/img/bradley-ross-avatar.webp" width="110" alt="Cartoon avatar of Bradley Ross with a small friendly robot">

Made by **Bradley Ross**, who builds and teaches practical AI. Part of [Practical AI](../../README.md).
[linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)
