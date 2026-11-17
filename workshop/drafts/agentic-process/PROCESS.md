# The process: nine steps, a gate after each

The one process document for building a tool in this repository. The builder skill follows it.

**Think of it as** a site inspector on a small job: nothing moves to the next stage until the
current one is signed off.

## The short path, for most tools

One person turns one kind of input into one result in a chat. Do steps 1, 5 and 8 in full, step 2
in a few minutes, and the rest in a line each. Take all nine when the tool is used by more than
one person, reads or writes files other people use, or costs money.

## The nine steps

| # | Step | Why | The decision it helps you make | Gate: go on when |
| --- | --- | --- | --- | --- |
| 1 | Scope | A tool that does one job gets finished; one that does five gets rebuilt | Which one job, for whom, and what is out | You can say the job in one sentence, with one test input and what a good result looks like |
| 2 | Reuse check | The cheapest tool is the one you do not build | Use what exists, wrap it, or build only the missing piece | You know what exists, with links and dates. If something does the whole job, stop and write a short guide to it |
| 3 | Outside help | Building or buying should be a choice made on purpose | What, if anything, to buy or connect | You know what you would build and what you would buy |
| 4 | Cost | A tool people cannot afford to run is not finished | Whether it is worth running | It costs nothing, or an amount you accept |
| 5 | Simplest design | The fewest moving parts that do the job | Where it runs, where it is saved, what stays manual | Someone else could draw it |
| 6 | Plan | If the explainer cannot be written, the tool is not understood yet | The steps, the result, and what a person checks | The explainer's first lines and the workflow are written |
| 7 | Review | You cannot see your own gaps, because you know what you meant | Whether a stranger understands it | Someone other than the author explains it back |
| 8 | Build and test | A new session with only your instructions finds what you cannot | Ready to use, or what to fix first | A fresh session finished the job on two different inputs, and you have read what it tripped on |
| 9 | Grow | Small additions get reviewed; big ones get waved through | What to add next, from real use | The level below is in use |

## What a finished Base tool contains

| Part | What it is | Required |
| --- | --- | --- |
| Explainer | What it does, how to start, what goes in and comes out, what to check. It can be the README | Yes |
| Runnable entry point | One instruction file to paste or save, or a direct link to an existing tool | Yes |
| Worked example | One run, unedited, made by a fresh session, with invented data | Yes |
| Workflow card | Trigger, inputs, steps, output, what a person checks, what happens when something is missing | When it helps |

## Rules for every tool

- Invent no facts. Missing data is reported as missing, never as zero.
- Show judgement calls to the person; do not hide them in a rule.
- A person approves anything that is sent, posted, paid, published or merged.
- Tests use invented or anonymised data.
