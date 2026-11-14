# Plans template

Everything needed to add a plan to this repository, by hand or with a skill.

| File | What it is |
| --- | --- |
| [`PLAN-TEMPLATE.md`](PLAN-TEMPLATE.md) | The plan README, with a note on what goes in each section |
| [`skill/plan-writer/SKILL.md`](skill/plan-writer/SKILL.md) | A skill that researches a tool and writes its plan from the template |

## What a plan is

A plan is a starting point, not a specification. It says what the tool is, who it is for, what
might be involved at each level, and how hard each level is. It is detailed about the simple level
and deliberately light on everything after it.

## By hand

1. **Check the index.** Open [`../README.md`](../README.md). If the tool is already there, update its plan instead of adding a new one.
2. **Pick a slug.** Lowercase words joined by hyphens, for example `expense-form`.
3. **Copy the template** to `plans/<slug>/README.md`.
4. **Fill it in, top to bottom.** Use the section notes in the template. Keep to these rules:
   - Write the one-line promise from the user's side: what they get, not how it works.
   - Lead with an analogy from everyday life.
   - Describe the simple level fully. Give each later level one line.
   - Name what the tool reuses before describing anything new.
   - Put anything you do not know under Open questions. Never guess.
5. **Flag the complexity** using the scale below, for the tool overall and for each level.
6. **Update the indexes.** Add a row to [`../README.md`](../README.md) and to [`../../docs/TODO.md`](../../docs/TODO.md), and set the Plan flag in [`../../docs/PRIORITIES.md`](../../docs/PRIORITIES.md).
7. **Open a pull request.** Do not commit to the main branch.

## With the skill

Install [`skill/plan-writer/`](skill/plan-writer/) in an assistant that supports skills, open this
repository, and say:

> Write a plan for a tool that turns a folder of receipt photos into an expense form.

The skill checks the index, researches established practice, fills in the template, updates the
indexes, and shows you a summary before anything is committed.

Without skills, paste the text of `SKILL.md` into your assistant as instructions and attach
`PLAN-TEMPLATE.md`.

## Complexity scale

| Complexity | Means |
| --- | --- |
| Beginner | No code. A chat assistant and a few files. Usually under an hour to set up |
| Intermediate | Connecting accounts or tools, some setup and testing. A few hours |
| Advanced | Code, hosting, a database or scheduled automation. Needs someone technical |

When a tool spans levels, give the range, for example "Beginner to advanced".

## Rules for every plan

- **Reuse first.** If an existing product, connector or skill already does it, say so and plan around it.
- **Research before design.** The first step of every plan is finding established best practices, each with a source link and the date it was checked.
- **No names.** No real people, companies or client material. Examples are synthetic.
- **A person approves** anything that posts, sends, pays or publishes.
- **Plain words.** Someone with no technical background should be able to read the overview aloud.
