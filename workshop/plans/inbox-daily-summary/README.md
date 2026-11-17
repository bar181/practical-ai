# Inbox triage and daily summary

One morning summary across your connected sources: email, calendar and social media feedback, with replies drafted.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner to intermediate | Done: landscape review in the draft | [Drafted](../../drafts/inbox-daily-summary/) | [`workshop/drafts/inbox-daily-summary/`](../../drafts/inbox-daily-summary/) |

**Think of it as:** A chief of staff who has read everything before you wake up and hands you one page: what needs you, what is drafted, what can wait.

## Overview

One morning summary across your connected sources: email, calendar and social media feedback. It ranks what needs you, drafts the replies, and lists the day's commitments.

## Who it is for

Anyone whose day starts in three different apps.

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
| Base | A sample summary built from a synthetic inbox, calendar and comment feed. | Beginner |
| Level 1, Beginner: for students | Connect your email and calendar to your assistant and ask for a morning summary in a fixed shape: needs you today, drafted and waiting, today's meetings, can wait. Paste in social media comments by hand. Nothing is sent without you. | Beginner |
| Level 2, Advanced: skills and connectors | The `morning-summary` skill with Gmail and Google Calendar connectors. It includes social media feedback, writes replies in your voice as drafts and files what is finished. | Intermediate |
| Level 3, Expert: automation | Runs every morning on a schedule and arrives on your phone. | Advanced |
| Commercial grade | Shared inboxes, delegation rules, and records of what was sent and by whom. | Explained, not built here |

## Established best practices

Done. See the [landscape review](../../drafts/inbox-daily-summary/landscape-review.md) for what already exists, with dated sources.

## What it reuses

Email and calendar connectors, and inbox skills already available in chat assistants.

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

- Which social platforms can be read directly and which need an export?
- What should never be drafted automatically?
