# Learning system

A growing log of questions and the solutions that worked, so the same problem is never solved twice. Versions for developers, businesses and personal use.

| Complexity | Research | Simple level | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Not started | Not started | None yet |

**Think of it as:** A workshop notebook where every fix is written down once, with a note on whether it held. The next person with the same problem starts from the answer.

## Overview

A log of questions and the solutions that worked. Before solving, look it up. After solving, record it. A person confirms an entry before it counts as recommended. There are three versions: for developers, for businesses and for personal use.

## Who it is for

Developers who meet the same errors twice, teams that answer the same questions repeatedly, and individuals who want to keep what they figured out.

## What might be involved at each level

The simple level is described in most detail, because it is built first. The later levels are
outlines and will change.

| Level | What it involves | Complexity |
| --- | --- | --- |
| Demo | A sample sheet of synthetic entries for each of the three audiences. | Beginner |
| Simple | A spreadsheet such as Google Sheets with one row per entry: the question, the recommended solution, the context, whether it worked, and who confirmed it. Connect the sheet to your assistant with two instructions: look here before answering, and offer to add a row after a problem is solved. | Beginner |
| Working | Entries are confirmed, ranked by how often they held, and retired when they stop working. | Intermediate |
| Automated | A vector database, for example Supabase, so entries are found by meaning and not only by matching words, with entries captured from working sessions. | Advanced |
| Commercial grade | Access control by team, audit of who confirmed what, and measures of how often a stored answer was reused. | Explained, not built here |

## Established best practices

_Research not started. This is the first step for this plan._

## What it reuses

A spreadsheet connector for the simple level. A hosted database with vector search for the advanced level.

## First step

1. Research established best practices. Record each one with a source link and the date checked.
2. Write the simple level solution and its overview.

The working level and beyond are planned only after the simple level is in use.

## Open questions

- What are the right columns for each of the three audiences?
- When should an entry be retired?
