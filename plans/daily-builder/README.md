# Daily builder

A scheduled agent that researches and builds the next item on this list, then opens a pull request for review.

| Complexity | Research | Simple level | Draft |
| --- | --- | --- | --- |
| Intermediate to advanced | Not started | Not started | None yet |

**Think of it as:** A night-shift apprentice who leaves finished work on the bench with a note, and never ships it without a signature.

## Overview

A scheduled agent that takes the next item on the priority list, researches what exists, builds a first version and asks for review.

## Who it is for

A maintainer who wants steady progress without doing every first draft by hand.

## Scope

- **In:** the simple level described below.
- **Out:** the working level and beyond, until the simple level is in use.
- **It works when:** to be written before anything is built.

## What might be involved at each level

The simple level is described in most detail, because it is built first. The later levels are
outlines and will change.

| Level | What it involves | Complexity |
| --- | --- | --- |
| Demo | One recorded run: the plan it wrote, what it built and the review it requested. | Beginner |
| Simple | Run it by hand. Ask your assistant to take the top unfinished item, follow the plan template, write the plan and the simple level, and stop for your review. Do this for two items before scheduling anything. | Intermediate |
| Working | A fixed rubric, a second agent that scores the work, and a pull request for every run. | Advanced |
| Automated | Runs on a schedule with connections to the repository, file storage and a hosting route. | Advanced |
| Commercial grade | Budgets, run logs, alerts on failure and a human approval step that cannot be skipped. | Explained, not built here |

## Established best practices

_Research not started. This is the first step for this plan._

## What it reuses

Scheduled tasks in chat assistants, the plan template and its skill in this repository.

## Decisions to record during research

Follow the [build process](../plans-template/BUILD-PROCESS.md). Tick each as it is settled.

- [ ] **Reuse check:** what is built in, what is open source, and whether to stop here
- [ ] **Build or license:** the lean for each level, with outside providers reviewed but not selected
- [ ] **Dependencies and pricing:** what the simple level depends on and what it costs
- [ ] **Where it lives:** which assistant, where the files are kept, what stays manual

## First step

1. Research established best practices. Record each one with a source link and the date checked.
2. Write the simple level solution and its overview.

The working level and beyond are planned only after the simple level is in use.

## Open questions

- What is the pass mark, and who scores?
- What must it never do without approval?
