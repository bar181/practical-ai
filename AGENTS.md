# For agents working in this repository

Practical AI is a set of tools that save people time on work they already do. The tool is the
product. Each tool does one job: a README that explains it, one `SKILL.md` in the open Agent Skills
format that works pasted into any chatbot, and a worked example. Level 1 works in any chatbot;
Level 2 saves it as a skill or project; Level 3 connects it, only where that removes recurring
work. Reuse first: use an existing capability, wrap it, or build only the missing piece.

| You were asked to | Go to |
| --- | --- |
| Make a page, a slide deck or a social post look designed: looks, effects, motion | [`projects/artifact-studio/AGENTS.md`](projects/artifact-studio/AGENTS.md) |
| Rewrite content in the tone and story order a reader needs: a pitch, a one-pager, a deck, a story | [`projects/tone-studio/AGENTS.md`](projects/tone-studio/AGENTS.md) |
| Lay out the sections of a website or page, or get a social post size | [`projects/web-sections/AGENTS.md`](projects/web-sections/AGENTS.md) |
| Publish a website (share a page, GitHub Pages, your own domain, Vercel, Cloudflare, Google Cloud, Supabase), change the Bradley Academy website, or build a site like it | [`projects/site-studio/AGENTS.md`](projects/site-studio/AGENTS.md) |
| Check a website and score it: speed, search and AI search, security, links, the message; a contact form or analytics to add | [`projects/website-audit/AGENTS.md`](projects/website-audit/AGENTS.md) |
| Turn a policy, contract or bill into an action list | [`projects/document-to-action-brief/AGENTS.md`](projects/document-to-action-brief/AGENTS.md) |
| Revise an email or post in someone's own voice, keeping every fact | [`projects/write-in-my-voice/AGENTS.md`](projects/write-in-my-voice/AGENTS.md) |
| Turn a meeting transcript or notes into decisions, actions and a follow-up | [`projects/meeting-notes-to-actions/AGENTS.md`](projects/meeting-notes-to-actions/AGENTS.md) |
| Turn a week of rough notes and last week's update into a short weekly status update | [`projects/weekly-status-update/AGENTS.md`](projects/weekly-status-update/AGENTS.md) |
| Compare options on one page with every claim checked against its source, or check a research report | [`projects/research-brief/AGENTS.md`](projects/research-brief/AGENTS.md) |
| Work a decision through to a one-page brief or a decision record (ADR), with every source checked | [`projects/decision-support/AGENTS.md`](projects/decision-support/AGENTS.md) |
| Score a piece of work out of 100 against a rubric, with evidence, or write the rubric first | [`projects/rubric-reviewer/AGENTS.md`](projects/rubric-reviewer/AGENTS.md) |
| Log a lesson, find the rules before work, or keep a learnings log | [`projects/learnings-database/AGENTS.md`](projects/learnings-database/AGENTS.md) |
| Answer questions about the tools or Bradley's work, or change the index for AI agents (`llms.txt`) | [`projects/practical-ai-guide/AGENTS.md`](projects/practical-ai-guide/AGENTS.md) |
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
- Never publish proprietary research: no architecture, learning processes, orchestration,
  optimisation, formulas, thresholds, settings or unpublished results, in pages, comments,
  generated files, `llms.txt`, commit messages or pull request descriptions. Publish only what is
  already public in Bradley's open repositories, with a link and its limits. For anything more,
  write: "Additional research capabilities and technical findings are available for discussion
  with qualified research partners." Never imply unpublished work was independently validated.
- Examples use invented data and say so. No real company or person is named.
- Every status line says who has and has not tried the thing. Keep that true when you change it.
- Generated files say so at the top. Change the source in `_build/`, rebuild, and say so.
- Before you finish, run `python3 workshop/tools/check_links.py .` and, for each project you
  touched, `python3 workshop/tools/check_project.py projects/<name>`. Both must pass. If you
  changed a README's title or promise, or added a project, run
  `python3 projects/practical-ai-guide/_build/build_index.py` to refresh `llms.txt`.
- Write in plain English: short sentences, no em dashes, sentence case headings.
- Delete retired work rather than archiving it; the git history keeps it.
- A person approves anything that is sent, posted, paid, published or merged.
