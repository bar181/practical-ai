# Agentic Process (version 2, draft)

**It builds useful tools for work people repeat.** Give it one real job, or a spec. It checks what
already exists, uses or wraps it where it can, builds only the missing piece, and hands back a tool
you can run with your own input: a short explainer, an instruction file or a link, and a worked
example, tested by a fresh AI session on two different inputs.

**Status: restarted on 16 November 2026.** Version 1 grew to 145 files around teaching and its own
tests; its good parts are carried over here. Nothing has run since the restart.
[Why it restarted](EVALUATION.md), and [the spec](SPEC.md).

## Try the example tool

A finished tool built with this process: **decision support**. Describe your business once, ask a
business question, and get research with sources, the options scored, a recommendation and a
short brief. [Open it](examples/decision-support/): the explainer, the instructions to paste, and
an unedited run on an invented bakery.

## Build a tool

| You have | Use | You get |
| --- | --- | --- |
| A job you repeat | Copy [the package template](package-template/) and fill it in with your chatbot | The explainer, instructions and example for your tool |
| A coding agent | [The builder skill](builder/agentic-process/), following [the process](PROCESS.md) | The same tool, built and tested by the agent, stopping only where you decide |
| A spec, and no time to guide each step | [Autopilot](builder/AUTOPILOT.md): one prompt for an agent or a scheduler | The tool and a hand-back note, or a draft pull request. Not yet run |

**What goes in:** one job, or a spec, and a few lines of guidance.
**What comes out:** a Base tool and a note: what was decided, what was assumed, what was not
checked, and what to test next.
**What you check:** the assumptions first, then the worked example against what you expected.

## In this folder

| File | What it is |
| --- | --- |
| [`SPEC.md`](SPEC.md) | What the project is for, and when version 2 is done |
| [`PROCESS.md`](PROCESS.md) | The nine steps, the short path, and what a finished tool contains |
| [`builder/`](builder/) | The builder skill, its project template and checks, Autopilot, and the fair-test rules |
| [`package-template/`](package-template/) | The Base package to copy |
| [`examples/decision-support/`](examples/decision-support/) | A complete tool, built and tested with the process |
| [`LESSONS.md`](LESSONS.md) | What version 1's tests taught, on one page |
| [`EVALUATION.md`](EVALUATION.md) | The score of version 1, and what was kept |
