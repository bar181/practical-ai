# For agents working in this repository

Practical AI is a set of tools that save people time on work they already do. The tool is the
product. Each tool does one job: a README that explains it, one `SKILL.md` in the open Agent Skills
format that works pasted into any chatbot, and a worked example. Level 1 works in any chatbot;
Level 2 saves it as a skill or project; Level 3 connects it, only where that removes recurring
work. Reuse first: use an existing capability, wrap it, or build only the missing piece.

| You were asked to | Go to |
| --- | --- |
| Make a page, a slide deck or a social post | [`projects/artifact-studio/AGENTS.md`](projects/artifact-studio/AGENTS.md) |
| Turn a policy, contract or bill into an action list | [`projects/document-to-action-brief/AGENTS.md`](projects/document-to-action-brief/AGENTS.md) |
| Log a lesson, find the rules before work, or keep a learnings log | [`projects/learnings-database/AGENTS.md`](projects/learnings-database/AGENTS.md) |
| Play or change the Rare Find game | [`projects/rare-find/AGENTS.md`](projects/rare-find/AGENTS.md) |
| Build a new tool, or improve one | [`projects/agentic-process/AGENTS.md`](projects/agentic-process/AGENTS.md): the builder skill, the one-page process and the template |
| Understand what the repository holds | [`README.md`](README.md) |
| Decide what to build next | [`docs/README.md`](docs/README.md): the priority list. Every idea, in three groups: [`workshop/plans/README.md`](workshop/plans/README.md) |
| Write or update a plan | [`workshop/skills/plan-writer/`](workshop/skills/plan-writer/) |
| Check what already exists before building | [`workshop/skills/landscape-review/`](workshop/skills/landscape-review/) |

## Where things go

| Folder | Holds |
| --- | --- |
| `projects/<name>/` | A finished project: `README.md`, `AGENTS.md`, `CLAUDE.md`, `LICENSE`, `base/`, `quality-results/README.md` (its evidence), optional `level-2-files/`, `level-3-files/` and `_build/`. Its own images live in `_build/img/` so the folder works when copied alone |
| `assets/images/` | Images shared across the repository |
| `docs/` | `README.md` (the projects and the priority list) and `reports/` (one explainer page per project) |
| `workshop/` | Plans, earlier drafts, skills and checking scripts |

## Rules for this repository

- Invent no facts. Where content is missing, leave a visible gap and say so.
- Examples use invented data and say so. No real company or person is named.
- Every status line says who has and has not tried the thing. Keep that true when you change it.
- Generated files say so at the top. Change the source in `_build/`, rebuild, and say so.
- Before you finish, run `python3 workshop/tools/check_links.py .` and, for each project you
  touched, `python3 workshop/tools/check_project.py projects/<name>`. Both must pass.
- Write in plain English: short sentences, no em dashes, sentence case headings.
- Delete retired work rather than archiving it; the git history keeps it.
- A person approves anything that is sent, posted, paid, published or merged.
