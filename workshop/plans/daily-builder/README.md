# Daily builder

A scheduled agent that researches and builds the next item on this list, then opens a pull request for review.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Intermediate to advanced | Not started | Running as a Claude scheduled task since 23 November 2026 | Two tools built and merged |

**Think of it as:** A night-shift apprentice who leaves finished work on the bench with a note, and never ships it without a signature.

## How it runs now

Since 23 November 2026 the daily builder is a Claude scheduled task. The prompt is in
[`scheduled-task-prompt.md`](scheduled-task-prompt.md); paste it into the task to change how it
works. Its first two drafts, [Rubric reviewer](../../../projects/rubric-reviewer/) and
[Weekly status update](../../../projects/weekly-status-update/), were built in `docs/`, reviewed by a
separate agent, and moved to `projects/` when Bradley merged them on 24 November 2026. From 24
November it builds each new tool straight into `projects/<slug>/`, with a visual README (an
animated how-it-works picture and a screenshot of the real result) and registration across the
repository and the site, all in one pull request that Bradley reviews and merges. No person has
reviewed its scoring of candidates yet.

## Overview

A scheduled agent that takes the next item on the priority list, researches what exists, builds a first version and asks for review.

## Who it is for

A maintainer who wants steady progress without doing every first draft by hand.

## Scope

- **In:** the Beginner level described below.
- **Out:** the Advanced level and beyond, until the Beginner level is in use.
- **It works when:** to be written before anything is built.

## What might be involved at each level

Level 1 is described in most detail, because it is built first. The later levels are
outlines and will change.

Level 1 is the Beginner level: a student can run it in any chat assistant with nothing installed. Levels 2 and 3 are the Advanced levels, with skills and connectors, for someone who works with agents every day.

| Level | What it involves | Complexity |
| --- | --- | --- |
| Base | One recorded run: the plan it wrote, what it built and the review it requested. | Beginner |
| Level 1, Beginner: for students | Run it by hand. Ask your assistant to take the top unfinished item, follow the plan template, write the plan and the Beginner level, and stop for your review. Do this for two items before scheduling anything. | Intermediate |
| Level 2, Advanced: skills and connectors | The `project-builder` skill with a fixed rubric, a second agent that scores the work, and a GitHub connection that opens a pull request for every run. | Advanced |
| Level 3, Expert: automation | Runs on a schedule with connections to the repository, file storage and a hosting route. | Advanced |
| Commercial grade | Budgets, run logs, alerts on failure and a human approval step that cannot be skipped. | Explained, not built here |

## Established best practices

_Research not started. This is the first step for this plan._

## What it reuses

Scheduled tasks in chat assistants, the plan template and its skill in this repository.

## Decisions to record during research

Follow the [build process](../plans-template/BUILD-PROCESS.md). Tick each as it is settled.

- [ ] **Reuse check:** what is built in, what is open source, and whether to stop here
- [ ] **Build or license:** the lean for each level, with outside providers reviewed but not selected
- [ ] **Dependencies and pricing:** what the Beginner level depends on and what it costs
- [ ] **Where it lives:** which assistant, where the files are kept, what stays manual

## First step

1. Research established best practices. Record each one with a source link and the date checked.
2. Write the Beginner level solution and its overview.

The Advanced level and beyond are planned only after the Beginner level is in use.

## Open questions

- What is the pass mark, and who scores?
- What must it never do without approval?
