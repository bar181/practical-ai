# Client project tracking and support site

A page each client can open to see where their project stands and get help. Starts as one HTML page, then adds sign-in, then a project plan with visuals.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Not started | Not started | None yet |

**Think of it as:** A parcel tracking page for a project. The client opens one link and sees where things stand, what happens next and who to ask.

## Overview

A page each client can open to follow their project and get support. It grows in three steps: a single page, then sign-in, then a project plan with visuals.

## Who it is for

Anyone delivering projects to clients who keep asking for a status update.

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
| Base | A sample status page for a synthetic project. | Beginner |
| Level 1, Beginner: for students | One HTML page per client: where the project stands, what was done this week, what happens next, open questions, and how to get help. Update it by asking your assistant to revise the page, then share the link. | Beginner |
| Level 2, Advanced: skills and connectors | A skill that rebuilds each client's page from a project sheet through a Google Sheets connector and publishes it. Sign-in so each client sees only their own page, using a hosted service such as Supabase. | Advanced |
| Level 3, Expert: automation | A project plan with a timeline view, kept in step with your task list, plus a support request form. | Advanced |
| Commercial grade | Many clients and roles, service targets, file sharing and a record of every update. | Explained, not built here |

## Established best practices

_Research not started. This is the first step for this plan._

## What it reuses

Artifact pages for the Beginner level, a hosted database with sign-in for the Advanced level, Site Studio for hosting.

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

- What must never appear on a client-facing page?
- Which sign-in method is simplest for clients?
