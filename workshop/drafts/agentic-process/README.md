# Agentic Process

Turns a job you repeat into a tool someone can start in minutes: a README that explains it, one
`SKILL.md` that works pasted into any chatbot or installed as a skill, and a worked example.

**Status, 16 November 2026.** Version 2. Decision support passed its check in fresh Claude chats,
and the builder built a second tool, [learning log](examples/learning-log/), which passed its
check too. No other chatbot has tried either. Version 1 is in [the archive](../../plans/archive/agentic-process/).

## Try the example tool

[Decision support](examples/decision-support/): paste one file into a chatbot, type a business
decision, and get a one-page brief with sources and a recommendation.

## Build a tool

| If you are | Use |
| --- | --- |
| Building by hand, in any chatbot | Copy [the template](template/) and follow [the one-page process](PROCESS.md) |
| Working with an agent | Give it [the builder skill](builder/agentic-process/SKILL.md), the job, and one example input |

**In:** the job, who it is for, one input and what a good result looks like.
**Out:** a tool folder (README, SKILL.md, example) with its short check recorded.
**Check:** paste the SKILL.md into a fresh chat and run the example, then a different input.

## What is here

| File | What it is |
| --- | --- |
| [`SPEC.md`](SPEC.md) | What this is and when it is done |
| [`PROCESS.md`](PROCESS.md) | The process on one page |
| [`template/`](template/) | The tool template |
| [`builder/`](builder/agentic-process/) | The builder skill |
| [`examples/decision-support/`](examples/decision-support/) | The first tool |
| [`examples/learning-log/`](examples/learning-log/) | The second, built by the builder skill on its own |
