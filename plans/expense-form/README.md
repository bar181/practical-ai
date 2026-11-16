# Expense form creator

A folder of receipt photos becomes a categorised expense form.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Not started | Not started | None yet |

**Think of it as:** A bookkeeper's assistant who sorts the shoebox of receipts and fills in the form, then waits for you to check it.

## Overview

Receipt photos in, a categorised expense form out, in the categories your business already uses.

## Who it is for

Anyone who files expenses, and anyone who has to process them.

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
| Base | A sample form produced from synthetic receipts. | Beginner |
| Level 1, Beginner: for students | Put receipt photos in one folder. Give your assistant your form template and your category list. Ask it to read each receipt and fill in the form: date, supplier, amount, tax, category. Check every line against the photo. | Beginner |
| Level 2, Advanced: skills and connectors | A skill that reads a connected Google Drive folder of receipts and writes rows through a Google Sheets connector, with your accounting and tax codes in the category list. | Intermediate |
| Level 3, Expert: automation | An approval step, then posting to your accounting system. | Advanced |
| Commercial grade | Policy checks, duplicate detection, approval limits and an audit trail. | Explained, not built here |

## Established best practices

_Research not started. This is the first step for this plan._

## What it reuses

Image reading in chat assistants, spreadsheet skills, a file storage connector, accounting connectors.

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

- How are unreadable receipts handled?
- Which codes differ by country?
