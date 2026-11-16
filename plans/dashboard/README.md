# Dashboard

Your key numbers on one page. Starts from a spreadsheet, then connects to your sales, accounting and customer systems.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Done: landscape review in the draft | [Drafted](../../drafts/dashboard/) | [`drafts/dashboard/`](../../drafts/dashboard/) |

**Think of it as:** The instrument panel of a car. A few dials you can read at a glance, each wired to something real.

## Overview

Your key numbers on one page, each showing where it came from. It starts from a spreadsheet and later reads directly from your sales, accounting and customer systems.

## Who it is for

Anyone who currently opens four systems to answer "how are we doing?".

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
| Base | A sample dashboard built from a synthetic spreadsheet. | Beginner |
| Level 1, Beginner: for students | Put the numbers you care about in one spreadsheet such as Google Sheets: one tab of raw rows, one tab of the five to eight figures that matter. Ask your assistant to build a one-page dashboard from that sheet, with the source of each number shown. | Beginner |
| Level 2, Advanced: skills and connectors | The `dashboard-builder` skill with a Google Sheets connector, then connectors to the systems the numbers come from: sales, accounting, customers. | Intermediate |
| Level 3, Expert: automation | Refreshes on a schedule and flags a number that crosses a limit you set. | Advanced |
| Commercial grade | Role-based views, data definitions agreed across the business, and an audit trail for every figure. | Explained, not built here |

## Established best practices

Done. See the [landscape review](../../drafts/dashboard/landscape-review.md) for what already exists, with dated sources.

## What it reuses

Spreadsheet connectors, dashboard features in chat assistants, connectors for accounting and customer systems.

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

- Which five to eight numbers belong on the first page?
- Which systems have a connector and which need an export?
