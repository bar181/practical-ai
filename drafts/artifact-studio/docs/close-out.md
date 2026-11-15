# Artifact studio: close-out

Stage 9 of the [project method](../../project-method/base/METHOD.md), 15 November 2026. The studio
is the first tool closed with it.

**Closed as a draft.** Built and checked by its author. Not yet used by anyone else for a real job,
so it stays in `drafts/` and does not move to `projects/`.

## The closing checklist

| Check | Result |
| --- | --- |
| Every gate passes | Yes. `python3 tools/gates.py drafts/artifact-studio --all`: ten gates, all pass, run on the day of closing |
| Nothing stale | Front doors, status table and counts were rewritten in the last round. Counts are written by the build |
| Nothing left over | The old level pages, the first gallery, the earlier project template and the plan generator are recorded in [`plans/archive/`](../../../plans/archive/) |
| Lessons kept | Thirteen rows in [`LESSONS.md`](../../project-method/base/LESSONS.md). They become the first import of the learnings database |
| The list is current | [`docs/PRIORITIES.md`](../../../docs/PRIORITIES.md) shows it as closed as a draft |
| Handed over | [`docs/reports/2026-11-15-practical-ai-project.md`](../../../docs/reports/2026-11-15-practical-ai-project.md) |

## The score at closing

From [`docs/SELF-REVIEW.md`](../../../docs/SELF-REVIEW.md), round 6. One caution: this rubric was
written after the work, three times, which is why the method now writes it at stage 4.

| Line | Score | Evidence |
| --- | --- | --- |
| One source of truth | 90 | `catalog.py` feeds the page, both indexes, the skill's sheets and the server. The `picker` gate proves they agree |
| Usable by an agent | 89 | `AGENTS.md`, `index.json`, eleven starters, ten tools. The `agent` gate finishes a deck through the server alone |
| Correct and checked | 88 | Ten gates behind one command |
| Honest, current documents | 87 | The `links` gate. Every status line says who has tried the thing |
| Usable today by a person | 84 | The "Use it today" table and six worked examples |
| Range and quality | 84 | 20 templates, 53 parts and design ideas, 9 looks |
| Evidence from real use | 40 | None. The owner has looked at the pages |
| Scaffolding a newcomer can follow | 80 | The `layout` gate |

Overall 80 on the first seven lines.

## What is handed on, still open

| Open item | Where it goes |
| --- | --- |
| Run the six worked examples in a fresh chat and record the scores | [`docs/TODO.md`](../../../docs/TODO.md) |
| Try the MCP server in a desktop assistant. Hosting is deferred | The owner |
| One other person uses it for a real job | The owner. This is what moves it to `projects/` |
| The fit scores are the author's judgement | Revisit after five real requests |
| `build.py` is dense | Rewrite only if someone else has to maintain it |
| Merge pull request 1 into `main` | The owner's decision |

## Reopening

Open it again only for one of three reasons: a real user found a fault, a new template is wanted,
or another tool needs something from it. Start at stage 1 of the method with one line saying why.
