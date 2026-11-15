# Plans template

> A plan starts as a **North Star page**: one to three pages on who the tool is for, what already exists and what is
> in scope. Its form is [`north-star.md`](../../drafts/project-method/base/scaffold/docs/north-star.md) in the project
> method's scaffold. The fuller plan template below is for a tool whose North Star has been approved.

Everything needed to add a plan to this repository, by hand or with a skill.

| File | What it is |
| --- | --- |
| [`BUILD-PROCESS.md`](BUILD-PROCESS.md) | The nine steps for building any new productivity tool. Read this first |
| [`PLAN-TEMPLATE.md`](PLAN-TEMPLATE.md) | The plan README, with a note on what goes in each section |
| [`../../skills/plan-writer/`](../../skills/plan-writer/) | A skill that researches a tool and writes its plan from the template |
| [`../../skills/landscape-review/`](../../skills/landscape-review/) | A skill that checks what already exists before anything is built |

## What a plan is

A plan is a starting point, not a specification. It says what the tool is, who it is for, what
might be involved at each level, and how hard each level is. It is detailed about level 1
and deliberately light on everything after it.

## By hand

1. **Check the index.** Open [`../README.md`](../README.md). If the tool is already there, update its plan instead of adding a new one.
2. **Pick a slug.** Lowercase words joined by hyphens, for example `expense-form`.
3. **Copy the template** to `plans/<slug>/README.md`.
4. **Work through the build process**, steps 1 to 6, filling the template as you go. Keep to these rules:
   - Write the one-line promise from the user's side: what they get, not how it works.
   - Lead with an analogy from everyday life.
   - Write the scope before anything else, including what is out.
   - Describe level 1 fully. Give each later level one line.
   - Name what the tool reuses before describing anything new.
   - Put anything you do not know under Open questions. Never guess.
5. **Flag the complexity** using the scale below, for the tool overall and for each level.
6. **Update the indexes.** Add a row to [`../README.md`](../README.md) and to [`../../docs/TODO.md`](../../docs/TODO.md), and set the Plan flag in [`../../docs/PRIORITIES.md`](../../docs/PRIORITIES.md).
7. **Open a pull request.** Do not commit to the main branch.

## With the skills

Install the two skills from [`../../skills/`](../../skills/) in an assistant that supports skills,
open this repository, and say:

> Write a plan for a tool that turns a folder of receipt photos into an expense form.

The plan writer checks the index, runs the landscape review, fills in the template, updates the
indexes, and shows you a summary before anything is committed.

Without skills, paste the text of each `SKILL.md` into your assistant as instructions and attach
`PLAN-TEMPLATE.md` and `BUILD-PROCESS.md`.

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
- **Review providers, do not select them,** until the level that needs one is being built.
- **No names.** No real people, companies or client material. Examples are synthetic.
- **A person approves** anything that posts, sends, pays or publishes.
- **Plain words.** Someone with no technical background should be able to read the overview aloud.
