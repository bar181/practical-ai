# Project method

How a tool in this repository gets built: nine stages, a gate after each, and a folder to copy so
every tool is laid out the same way.

**Think of it as** building a house. You agree the drawing before you pour concrete, you put up
the frame before you choose curtains, and an inspector signs off each stage before the next one
starts. The inspector here is a short script, and it never gets tired or polite.

**North Star:** a person, or an agent working alone, can take an idea to a tool that someone else
can use, without rebuilding it three times on the way.

**Where it came from:** the [artifact studio](../artifact-studio/) was rebuilt three times before
its shape was right. [`base/LESSONS.md`](base/LESSONS.md) lists each wrong turn and the rule that
would have prevented it. This method is those rules, in order, checked against how others
build with agents ([`base/SOURCES.md`](base/SOURCES.md)).

## Use it today

| You want | Do this | Takes |
| --- | --- | --- |
| To start a new tool | `python3 base/new_project.py my-tool "My tool"` makes `drafts/my-tool/` with the layout, both front doors and a first gate | 1 minute |
| To know what to do next on a tool | Read [`base/METHOD.md`](base/METHOD.md): find your stage, do its work, pass its gate | 5 minutes |
| To check a tool is laid out properly | `python3 ../../tools/check_project.py ../my-tool` | 5 seconds |
| To check a tool works | `python3 ../../tools/gates.py ../my-tool` | under a minute |
| An agent to build the tool | Give it the [`project-builder`](../../skills/project-builder/) skill and the idea. See [level 2](level-2/) | hours, mostly unattended |

## How it is laid out

`base/` holds everything. A level holds only what it adds.

```
project-method/
  README.md      you are here
  AGENTS.md      for an agent asked to start or continue a tool
  gates.json     the checks on this method itself
  base/
    METHOD.md      the nine stages and their gates
    SOURCES.md     what the method draws on, with links and dates
    LESSONS.md     what building the first tool taught, as a table
    scaffold/      the folder every new tool starts as
    new_project.py copies the scaffold and fills in the name
  level-1/       by hand: a person and an assistant, one stage at a sitting
  level-2/       agentic: a skill that runs the stages and the gates, and stops where a person must decide
```

| Level | You add | You depend on | State |
| --- | --- | --- | --- |
| Base | Nothing. Read and copy | Python 3 | Built |
| [Level 1](level-1/) | A prompt to paste at each stage | Any chat assistant | Written. Not yet used on a second tool |
| [Level 2](level-2/) | The `project-builder` skill and the gate runner | An agent that can run commands and load skills | Written. **Not yet run end to end** |

## The nine stages at a glance

```mermaid
flowchart LR
  A[1 Understand] --> B[2 Research] --> C[3 Scope] --> D[4 Plan] --> E[5 Prove]
  E --> F[6 Build] --> G[7 Verify] --> H[8 Score] --> I[9 Close]
```

| Stage | You produce | The gate |
| --- | --- | --- |
| 1. Understand | Who it is for, the one job, a North Star | The page reads true to the person who asked |
| 2. Research | What already exists, with dated sources | Every source dated. Build, use or build on top: decided |
| 3. Scope | In, out, the levels, and a "done when" line for each item | **A person approves the North Star page** |
| 4. Plan | The folder, both front doors, the gates and the rubric, before any content | The layout check passes |
| 5. Prove | One real request taken to one finished output | **A person says it is what they wanted** |
| 6. Build | One source file, generated copies, then breadth | The build and the link check pass |
| 7. Verify | Worked examples, a scripted agent, every request run | The example and agent gates pass |
| 8. Score | A self-review out of 100 on the rubric written at stage 4 | Every line scored, with evidence |
| 9. Close | Clean-up, lessons logged, status final, a short report | Every gate passes. **A person closes it** |

A person decides three times: after stage 3, after stage 5 and at stage 9.

## Status

Draft. Written by the author of the first tool, from that one experience.

| Part | State |
| --- | --- |
| The method and the lessons | Revised on 15 November 2026 from one build and from published practice. The artifact studio is the first tool closed through stage 9 |
| The scaffold and `new_project.py` | Built. A gate creates a project from it and checks the layout |
| The gate runner and the three checks | Built, and in daily use on the artifact studio |
| Level 2, the agentic run | Written. **No agent has yet taken a tool through all nine stages with it** |
| The nine older drafts | Still in the earlier layout. [`base/LESSONS.md`](base/LESSONS.md) says how they move over |

It moves to `projects/` when a second tool has been built with it from stage 1.
