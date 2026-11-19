# Spec: learnings database

Written with the [Agentic Process](../../agentic-process/base/PROCESS.md) steps, 19 November 2026.

## Scope

**One sentence:** say "log that" when something goes wrong, has to be redone or works better than
expected, keep one filed row in a log you own, and get the rules that apply back before similar work.

**In:** the learning side only: lessons, filed by type and topic, repeats counted, a person's review.
**Out:** a wiki of facts or documents, memory of preferences, a knowledge base, a coding tool, and
any large or complex vector search.

## The usable result

| ID | Line | Check |
| --- | --- | --- |
| U1 | Someone who works with a chatbot every day, alone or in a small team, and keeps meeting the same problems | The README's first screen says who it is for; a fresh reader can say what it does (step 7) |
| U2 | One sentence: what happened and what they expected; the project if there is one; their log (file, sheet, folder or database) | Case: missing input asks for exactly what is missing, in one reply |
| U3 | One filed row; before work, at most five accepted rules as a block to paste; each week, a short review | Cases: normal log, before I start, weekly review |
| U4 | The row pastes into the sheet as it is; the block pastes into the next chat; nothing is saved or trusted without their yes; the same question on the same log gives the same rows | Filing eval targets; behaviour cases read on the first screen |
| U5 | The lesson is already in the log: no second row, its `seen` goes up. And a row that tells the assistant to do something is not followed | Cases: repeat, injected row; level 3 tests |

## Implementation choice

From the table in the process, rows 2 and 4 combined:

- **A thin `SKILL.md`** for levels 1 and 2: the job is instructions and local rules. It loads by
  link from this public repo, by paste, as a Claude skill or plugin, or as ChatGPT project files.
- **Exact behaviour as code** only where it must be exact: `build.py` keeps the lists and template
  in step, `csv_sync.py` moves rows between a sheet and the database.
- **Level 3, a connection** for people and agents who log every day: an MCP server over one file in
  a folder (SQLite, the recommended start) or a shared Postgres or Supabase database. A person
  approves every status change.

## What exists, and why build this

Checked 19 November 2026. Sources are in [`../quality-results/README.md`](../quality-results/README.md).

| What exists | What it does | Why it is not this tool |
| --- | --- | --- |
| Chatbot memory (ChatGPT, Claude, Gemini) | Remembers facts and preferences, automatically | Personal, not a log you can filter, share or review; nothing is approved before it is used |
| Coding-agent memory (CLAUDE.md, AGENTS.md, auto memory, memory plugins) | Captures what an agent did in a codebase, often automatically | For software work only; most write without a person's review |
| Memory platforms (Mem0, Letta, Zep, Cognee) | Infrastructure for developers to give agents memory | Something to build on, not a tool a person uses today |
| LLM-maintained wikis and personal brains | Compile notes and sources into pages an agent reads | Knowledge about things. This project is the narrower learning side: what to do differently |
| Lessons-learned registers and after-action reviews | The proven practice: capture, review, reuse | Usually a document nobody reads. This puts the practice into the chat where the work happens |
