# Dashboard

Your key numbers on one page. Starts from a spreadsheet, then connects to your sales, accounting and customer systems.

| Complexity | Research | Simple level | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Partly: notes only, sources not checked | [Drafted](../../drafts/dashboard/) | [`drafts/dashboard/`](../../drafts/dashboard/) |

**Think of it as:** The instrument panel of a car. A few dials you can read at a glance, each wired to something real.

## Overview

Your key numbers on one page, each showing where it came from. It starts from a spreadsheet and later reads directly from your sales, accounting and customer systems.

## Who it is for

Anyone who currently opens four systems to answer "how are we doing?".

## Scope

- **In:** the simple level described below.
- **Out:** the working level and beyond, until the simple level is in use.
- **It works when:** to be written before anything is built.

## What might be involved at each level

The simple level is described in most detail, because it is built first. The later levels are
outlines and will change.

| Level | What it involves | Complexity |
| --- | --- | --- |
| Demo | A sample dashboard built from a synthetic spreadsheet. | Beginner |
| Simple | Put the numbers you care about in one spreadsheet such as Google Sheets: one tab of raw rows, one tab of the five to eight figures that matter. Ask your assistant to build a one-page dashboard from that sheet, with the source of each number shown. | Beginner |
| Working | Connect the systems the numbers come from: a sales system, accounting software such as QuickBooks, a customer system such as Salesforce. | Intermediate |
| Automated | Refreshes on a schedule and flags a number that crosses a limit you set. | Advanced |
| Commercial grade | Role-based views, data definitions agreed across the business, and an audit trail for every figure. | Explained, not built here |

## Established best practices

_Notes only. See the [landscape notes](../../drafts/dashboard/landscape-notes.md). Sources have not been checked. A proper review is the next step._

## What it reuses

Spreadsheet connectors, dashboard features in chat assistants, connectors for accounting and customer systems.

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

- Which five to eight numbers belong on the first page?
- Which systems have a connector and which need an export?
