# Student AI assistant

A course assistant that answers from the lesson material and names the lesson it used.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner to intermediate | Not started | Not started | None yet |

**Think of it as:** A teaching assistant who has read every lesson and always says which page the answer came from.

## Overview

A course assistant that answers student questions from the lesson material only, and names the lesson it used.

## Who it is for

Instructors, and students who get stuck at midnight.

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
| Base | A sample set of questions and answers over a synthetic three-lesson course. | Beginner |
| Level 1, Beginner: for students | A chatbot Project holding the course materials, with instructions to answer only from them, name the lesson, and say so when the material does not cover the question. | Beginner |
| Level 2, Advanced: skills and connectors | A skill with a Google Drive connector to the lesson folder, embedded in the training website, with a sheet of the questions the material could not answer. | Intermediate |
| Level 3, Expert: automation | Nudges for students who fall behind, and a weekly summary of common questions for the instructor. | Advanced |
| Commercial grade | Privacy controls for student data, integrity rules for graded work, and escalation to a person. | Explained, not built here |

## Established best practices

_Research not started. This is the first step for this plan._

## What it reuses

Projects in chat assistants. The training website for where it lives.

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

- What should it refuse to do for graded work?
- Who reads the unanswered questions?
