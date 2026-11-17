# Rubric reviewer: North Star

Stages 1 to 3 of the [project method](../../drafts/agentic-process/PROCESS.md). Written
15 November 2026. **Not yet approved.** Proposed by the assistant, not asked for by the owner.
Complexity: beginner.

**Think of it as** a marking scheme and a second marker. The scheme is written before the work is
handed in, and the marker has not watched it being made.

**North Star:** any piece of work can be scored out of 100 against a rubric written beforehand,
with one line of evidence for each score, by a reviewer with fresh eyes.

## Understand

| | |
| --- | --- |
| Who it is for | As someone who builds or commissions work from an assistant, I want it scored against a rubric I can read, so that "it looks good" is replaced by a number and a reason |
| The one job | Score a piece of work against a rubric, line by line, with evidence |
| The finished thing is | A product: a rubric format, a small library of rubrics, and a reviewing skill |

## Research: what already exists

| Source | Checked | What we take from it |
| --- | --- | --- |
| [Plannotator: planning with coding agents](https://docs.plannotator.ai/learn/planning/how-to-plan-with-ai-coding-agents) | 15 Nov 2026 | Keep coordination, execution and verification apart. Verify with fresh evidence and a fresh reviewer |
| [Ready Solutions: agentic development guide](https://readysolutions.ai/blog/2026-04-08-agentic-development-starter-guide/) | 15 Nov 2026 | Review the result in a new session against the original plan, and advance only when a deterministic check passes |
| This repository's own six rounds of self-review | 15 Nov 2026 | A rubric rewritten after the work cannot be compared between rounds. A line with no evidence was scored too high every time |

**Decision:** build. It is small, the owner already asks for every evaluation as a rubric out of
100, and the project method needs it at stage 8. Researched lightly: stage 2 proper is still to do.

## Scope

**In:** a rubric file format (line, what 90 looks like, weight); rubrics for a page, a deck, a
plan, a skill and a recommendation; scoring with evidence; a cap of 40 on any line with no
evidence; a comparison with the previous score.

**Out:** grading people; replacing gates (a gate is pass or fail, a rubric is how good).

**Where the data lives:** rubrics are public and live in the repository. Scores belong to the
project they score.

Level 1 is the Beginner level: a student can run it in any chat assistant with nothing installed. Levels 2 and 3 are the Advanced levels, with skills and connectors, for someone who works with agents every day.

| | Holds | Done when |
| --- | --- | --- |
| Base | The format, five rubrics, three invented pieces of work each scored twice to show a fair and an inflated review | A reader can tell the fair review from the inflated one |
| Level 1, Beginner | Paste the instructions, the rubric and the work into a fresh chat. Get scores, evidence and the three changes that would raise the score most | Two fresh chats score the same work within five points of each other |
| Level 2, Advanced | A skill that runs the review in a separate session and writes it beside the work | The project method's stage 8 is one command |

## Open questions

- How far apart do two reviewers land on the same work? That number decides whether this is useful.
- Should weights exist at all, or is a plain average more honest?

## Approved

Not yet.
