# practical-ai

Practical AI tools a person or a small team can set up and use, mostly without writing code. No
fluff, just productivity.

**Think of it as** a workshop wall. Each tool has its outline painted on the board, so you can see
what is there, what is being made and what is still an idea.

## Start here

| You are | Open |
| --- | --- |
| Looking for something to use today | [`drafts/artifact-studio/`](drafts/artifact-studio/): pages, slide decks and social posts from your notes |
| An agent | [`AGENTS.md`](AGENTS.md) |
| Wondering what else is planned | [`docs/PRIORITIES.md`](docs/PRIORITIES.md) and [`plans/`](plans/) |
| Building a tool here | [`drafts/project-method/`](drafts/project-method/): seven stages, a gate after each |

## Layout

| Folder | What it holds |
| --- | --- |
| [`docs/`](docs/) | The priority list, the to-do list, the self-review and the reports |
| [`plans/`](plans/) | One folder for each planned tool, the plan template, and [`archive/`](plans/archive/) for what was replaced |
| [`drafts/`](drafts/) | Tools being built. Usable, not yet used by anyone but their author |
| [`projects/`](projects/) | Tools another person has used for a real job. Empty so far |
| [`skills/`](skills/) | Skills an assistant can load, one folder each |
| [`tools/`](tools/) | Four small scripts that check the repository: links, skills, layout, and a gate runner |

A tool moves one way: a line in the priority list, a plan, a draft, a project.

## How every tool is laid out

One rule: **`base/` holds everything. A level holds only what it adds.**

| | Holds | You depend on |
| --- | --- | --- |
| `base/` | The thing itself, its examples and its source | A browser |
| `level-1/` | Instructions: for the assistant and for you | Any chat assistant |
| `level-2/` | What makes it repeatable: a preferences file, a skill, gates | An assistant that keeps files |
| `level-3/` | Connections: an MCP server, a plugin, a schedule | Other systems |

Each tool also has two front doors, `README.md` for people and `AGENTS.md` for agents, and a
`gates.json` listing the checks it must pass.

The [artifact studio](drafts/artifact-studio/) and the [project method](drafts/project-method/)
follow this layout. Nine older drafts still use an earlier one and move over as each is next
worked on. [`plans/archive/`](plans/archive/) says what changed.

## Is it working?

```
python3 tools/gates.py drafts/artifact-studio
```

It ends with "All gates that ran passed" or "DO NOT SHIP" and the reason.

## Ground rules

- Reuse what already exists before building anything new.
- A person approves anything that posts, sends, pays or publishes.
- Examples use invented data and say so. No real names, companies or client material.
- Every claim about something that changes often carries the date it was checked.
- Every status line says who has and has not tried the thing. "Built" is not "used".

Licensed under Apache-2.0.
