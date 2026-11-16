#!/usr/bin/env python3
"""Generate the practical-ai indexes and plan READMEs from plans_data.py.

Status flags are read from what is on disk. Usage: python scaffold2.py <repo_root>
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from plans_data import PLAN, TOOLS  # noqa: E402

CHECKED = "2026-11-14"
LEVELS = [
    ("level-demo", "Demo", "A finished example to look at. Nothing to set up."),
    ("level-simple", "Simple", "The smallest version you can run yourself, usually in a chatbot Project with a few files."),
    ("level-working", "Working", "The common size. What most people use day to day."),
    ("level-automated", "Automated", "The working version plus schedules and connections, so it runs without being asked."),
]
EXTRA = [
    ("student-projects", "Student projects", "Versions built by students, shared with permission and with private details removed."),
    ("commercial-grade", "Commercial grade", "An explanation of what a commercial build adds. Never contains a project. Usually an HTML explainer and a one-pager."),
]
NO_PLAN_NOTE = {"estimator": "No plan published. A candidate is in [`drafts/estimator/`](../drafts/estimator/)."}
STUB = "_Not started._"
SCALE = """| Complexity | Means |
| --- | --- |
| Beginner | No code. A chat assistant and a few files. Usually under an hour to set up |
| Intermediate | Connecting accounts or tools, some setup and testing. A few hours |
| Advanced | Code, hosting, a database or scheduled automation. Needs someone technical |
"""


def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def has_real_content(folder: Path) -> bool:
    if not folder.is_dir():
        return False
    files = [p for p in folder.rglob("*") if p.is_file()]
    if len(files) > 1:
        return True
    return bool(files) and STUB not in files[0].read_text(encoding="utf-8")


def build(root: Path) -> None:
    drafts = root / "drafts"
    draft_slugs = sorted(p.name for p in drafts.iterdir() if p.is_dir()) if drafts.is_dir() else []
    names = {t[0]: t[1] for t in TOOLS}

    def research(slug: str) -> str:
        if (drafts / slug / "landscape-review.md").is_file():
            return "Done: landscape review in the draft"
        if (drafts / slug / "landscape-notes.md").is_file():
            return "Partly: notes only, sources not checked"
        guide = drafts / slug / "STUDENT-GUIDE.md"
        if guide.is_file() and "## Sources" in guide.read_text(encoding="utf-8"):
            return f"Partly: tool facts checked {CHECKED}"
        return "Not started"

    def simple(slug: str) -> str:
        if has_real_content(root / "projects" / slug / "level-simple"):
            return "Published"
        if (drafts / slug / "level-simple").is_dir() or (drafts / slug / "level-1").is_dir():
            return f"[Drafted](../drafts/{slug}/)"
        return "Not started"

    # ---------------- root README
    w(root / "README.md", """# practical-ai

Suite of practical AI assisted workflows and automation tools. No fluff, just productivity.

Each tool here is something a person or a small team can set up and use, mostly without writing
code. Every tool is offered at several sizes, so you can start with a demo and stop at the level
that is enough.

## Layout

| Folder | What it holds |
| --- | --- |
| [`docs/`](docs/) | The priority list, with what is published for each tool, and the to-do project list |
| [`plans/`](plans/) | The plans index, one folder per planned tool, the build process and the plan template |
| [`skills/`](skills/) | Specialty skills identified along the way, such as the plan writer and the landscape review |
| [`drafts/`](drafts/) | Works in progress. First copies, not yet reviewed |
| [`projects/`](projects/) | Published projects, each with a student guide and one folder per level |

A tool moves in one direction: a line in the priority list, then a plan, then a draft, then a project.

## Levels

| Level | What it is |
| --- | --- |
""" + "".join(f"| `{s}` | {d} |\n" for s, _, d in LEVELS + EXTRA) + """
## Ground rules

- Reuse what already exists before building anything new.
- A person approves anything that posts, sends, pays or publishes.
- Examples use synthetic data. No real names, companies or client material.
- Every claim about a tool that changes often carries the date it was checked.

Licensed under Apache-2.0.
""")

    # ---------------- plans: per tool
    top = [t for t in TOOLS if t[3] == "top"]
    more = [t for t in TOOLS if t[3] == "more"]
    for slug, name, line, _ in TOOLS:
        if slug not in PLAN:
            continue
        p = PLAN[slug]
        overall, c_demo, c_simple, c_work, c_auto = p["complexity"]
        draft_cell = f"[`drafts/{slug}/`](../../drafts/{slug}/)" if slug in draft_slugs else "None yet"
        r = research(slug)
        s = simple(slug).replace("(../drafts/", "(../../drafts/")
        found = ("\nFound so far in the reuse check, on " + CHECKED + ":\n\n" + "".join(f"- {x}\n" for x in p["found"])) if p.get("found") else ""
        practices = (f"Done. See the [landscape review](../../drafts/{slug}/landscape-review.md) for what already exists, with dated sources"
                     + (f", and the [best practices](../../drafts/{slug}/BEST-PRACTICES.md) for how the tool is built and used." if (drafts / slug / "BEST-PRACTICES.md").is_file() else ".")
                     if r.startswith("Done") else
                     f"_Notes only. See the [landscape notes](../../drafts/{slug}/landscape-notes.md). Sources have not been checked. A proper review is the next step._" if "notes only" in r else
                     "_Research not started. This is the first step for this plan._" if r == "Not started" else
                     f"_Partly done. The draft student guide lists the sources checked on {CHECKED}. "
                     "A wider review of established practice is still to do._")
        w(root / "plans" / slug / "README.md", f"""# {name}

{line}

| Complexity | Research | Simple level | Draft |
| --- | --- | --- | --- |
| {overall} | {r} | {s} | {draft_cell} |

**Think of it as:** {p['analogy']}

## Overview

{p['overview']}

## Who it is for

{p['who']}

## Scope

- **In:** {p.get('scope_in','the simple level described below.')}
- **Out:** {p.get('scope_out','the working level and beyond, until the simple level is in use.')}
- **It works when:** {p.get('works_when','to be written before anything is built.')}

## What might be involved at each level

The simple level is described in most detail, because it is built first. The later levels are
outlines and will change.

| Level | What it involves | Complexity |
| --- | --- | --- |
| Demo | {p['demo']} | {c_demo} |
| Simple | {p['simple']} | {c_simple} |
| Working | {p['working']} | {c_work} |
| Automated | {p['automated']} | {c_auto} |
| Commercial grade | {p['commercial']} | Explained, not built here |

## Established best practices

{practices}

## What it reuses

{p['reuses']}
{found}
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

""" + "".join(f"- {q}\n" for q in p["questions"]))

    # ---------------- plans index
    rows = ""
    for n, (slug, name, line, _) in enumerate(top, 1):
        if slug in PLAN:
            rows += f"| {n} | [{name}]({slug}/) | {line} | {PLAN[slug]['complexity'][0]} | {research(slug)} | {simple(slug)} |\n"
        else:
            rows += f"| {n} | {name} | {line} | | | {NO_PLAN_NOTE.get(slug, 'No plan yet')} |\n"
    w(root / "plans" / "README.md", f"""# Plans index

One folder per planned tool. Each README gives an overview, what might be involved at each level,
and a complexity flag. A plan is a starting point: it is updated as research is done and replaced by
a draft and then a project as work proceeds.

To add or update a plan, use [`plans-template/`](plans-template/). It holds the nine-step build
process, the template and the instructions. The skills that do the work for you are in
[`../skills/`](../skills/).

## Complexity scale

{SCALE}
A tool can start at Beginner and reach Advanced at its automated level. The index shows the range.

## The {len(top)} priority tools

| # | Plan | In one line | Complexity | Research | Simple level |
| --- | --- | --- | --- | --- | --- |
{rows}
## Additional options, no plan yet

""" + "".join(f"- **{name}:** {line}\n" for _, name, line, _ in more) + """
Priority order and publishing status are in the [priority list](../docs/PRIORITIES.md). The work
queue is in the [to-do project list](../docs/TODO.md).
""")

    # ---------------- projects
    w(root / "projects" / "README.md", """# Projects

Published projects. Each project folder has the same shape, so once you have worked through one you
know your way around all of them.

```
projects/<tool>/
  README.md            what the project is
  STUDENT-GUIDE.md     step by step explainer
""" + "".join(f"  {s + '/':<20} {d}\n" for s, _, d in LEVELS + EXTRA) + """```

Start a new project by copying [`_template/`](_template/).

_No projects published yet. Candidates are in [`drafts/`](../drafts/)._

A level is published when its folder holds more than a placeholder. The count per tool is in the
[priority list](../docs/PRIORITIES.md).
""")

    # ---------------- drafts
    listing = "".join(f"| [`{s}/`]({s}/) | {names.get(s, s)} |\n" for s in draft_slugs)
    w(drafts / "README.md", """# Drafts

Works in progress. These are first copies: complete enough to read and react to, not yet reviewed
or tested by anyone else. Expect gaps, open questions and things that will change.

A draft that passes review moves to [`projects/`](../projects/).

""" + ("| Draft | Tool |\n| --- | --- |\n" + listing if listing else "_No drafts yet._\n"))

    # ---------------- docs: priorities
    def flags(slug: str):
        proj = root / "projects" / slug
        published = f"{sum(has_real_content(proj / s) for s, _, _ in LEVELS)} of {len(LEVELS)} levels" if proj.is_dir() else "0"
        d = drafts / slug
        if (proj / "STUDENT-GUIDE.md").is_file() and STUB not in (proj / "STUDENT-GUIDE.md").read_text(encoding="utf-8"):
            guide = "Published"
        elif (d / "STUDENT-GUIDE.md").is_file():
            guide = f"[Draft guide](../drafts/{slug}/STUDENT-GUIDE.md)"
        elif (d / "level-1" / "README.md").is_file():
            guide = f"[Draft guide](../drafts/{slug}/level-1/README.md)"
        else:
            guide = "No"
        plan = f"[Yes](../plans/{slug}/)" if slug in PLAN else "No"
        if has_real_content(proj / "commercial-grade"):
            commercial = "Published"
        elif (d / "commercial-grade").is_dir():
            commercial = "Draft"
        else:
            commercial = "No"
        return published, guide, plan, commercial

    def table(group, first):
        out = "| # | Tool | What it does | Published | Student guide | Plan | Commercial |\n| --- | --- | --- | --- | --- | --- | --- |\n"
        for n, (slug, name, line, _) in enumerate(group, first):
            out += f"| {n} | {name} | {line} | " + " | ".join(flags(slug)) + " |\n"
        return out

    built = [names[s] for s in [t[0] for t in TOOLS] if s in draft_slugs]
    demos = [names[t[0]] for t in TOOLS if any((drafts / t[0] / "level-demo").glob("*.html")) or any((drafts / t[0] / "base").glob("*.html"))]
    built_line = (f"**Built so far:** {len(built)} draft candidates in [`drafts/`](../drafts/): " + ", ".join(built) + "."
                  + (f" Working demo: {', '.join(demos)}." if demos else "")
                  + f" {len(PLAN)} plans in [`plans/`](../plans/). Nothing has been promoted to `projects/` yet.")

    w(root / "docs" / "PRIORITIES.md", f"""# Priorities

The tools this repository is working toward. Flags were read from the folders on {CHECKED}.

{built_line}

| Flag | Means |
| --- | --- |
| Published | How many levels of the tool are in `projects/` (demo, simple, working, automated) |
| Student guide | Whether a step by step explainer exists, and where |
| Plan | Whether a plan is published in `plans/` |
| Commercial | Whether a commercial-grade explainer exists |

## The {len(top)} priority tools

In priority order.

{table(top, 1)}
## {len(more)} additional options

Not scheduled. Any of these can move up.

{table(more, len(top) + 1)}
Order follows three tests: it is useful to the maintainer first, it can be taught without code, and
it reuses something that already exists.
""")

    # ---------------- docs: to-do project list
    todo_rows = ""
    for n, (slug, name, _, _) in enumerate(top, 1):
        r = research(slug)
        r_cell = "To do" if r == "Not started" else "Done" if r.startswith("Done") else "Notes only" if "notes only" in r else "Partly done"
        s_cell = "Drafted, needs review" if slug in draft_slugs and ((drafts / slug / "level-simple").is_dir() or (drafts / slug / "level-1").is_dir()) else "To do"
        plan_cell = f"[Plan](../plans/{slug}/)" if slug in PLAN else "No plan"
        todo_rows += f"| {n} | {name} | {r_cell} | {s_cell} | {plan_cell} |\n"
    n_drafted = todo_rows.count("Drafted, needs review")
    w(root / "docs" / "TODO.md", f"""# To-do project list

Every project starts with the same two steps, in this order:

1. **Research** established best practices. Record each with a source link and the date checked.
2. **Simple level:** write the level 1 solution and its overview.

The working level and beyond are not planned in detail until the simple level is in use.

Status read from the folders on {CHECKED}: {n_drafted} of {len(top)} simple levels drafted, 0 reviewed, 0 published.

| # | Project | 1. Research | 2. Simple level and overview | Plan |
| --- | --- | --- | --- | --- |
{todo_rows}
"Partly done" means the tool facts in the draft guide were checked against sources. A wider review
of established practice has not been done for any project yet.

## Across all projects

- [ ] Review the drafts in `drafts/` and promote the levels that are ready to `projects/`
- [ ] Have someone other than the author test each simple level
- [ ] Fill the open slots listed at the end of each draft student guide
- [ ] Draft a commercial-grade one-pager for each promoted project

## Waiting on a decision

- [ ] The avatar and voice tools to recommend in the video guides
- [ ] One hosting route confirmed end to end
- [ ] The scoring rubric for the daily builder, before it is scheduled
""")

    w(root / "docs" / "README.md", """# Docs

Priorities and to-do lists for this repository.

| File | Holds |
| --- | --- |
| [`PRIORITIES.md`](PRIORITIES.md) | Every tool in priority order, with a description and four flags |
| [`TODO.md`](TODO.md) | The to-do project list: research first, then the simple level |
| [`SELF-REVIEW.md`](SELF-REVIEW.md) | The score-and-fix loop: rubric, scores before and after, what was fixed and what is still open |
| [`practical-ai-explained.html`](practical-ai-explained.html) | A one-page explainer of the whole toolkit: the ten tools, how each is laid out and built, the artifact studio, and how to use it. Download and open in a browser |
""")


if __name__ == "__main__":
    build(Path(sys.argv[1]))
    print("scaffold written")
