# Evaluation of Agentic Process version 1, and why it restarts here

Written on 16 November 2026 for the owner, who asked whether it would be easier to start over.
**Answer: yes.** Version 1 holds good parts inside a structure that grew around teaching and
around its own testing. Fixing it in place means unwinding that structure file by file. Starting
over in this folder keeps the parts that proved their worth and drops the rest.

## Score against the owner's spec

The owner's spec of 16 November (now archived with version 1) is the measure. No item counts users.

| Item | Score | Why |
| --- | --- | --- |
| Clear purpose | 45 | The purpose moved from method, to teaching, to Autopilot, to chatbot tools in one day. The README, the coach, the course and the spec each said something different |
| Simple | 25 | 145 files and about 12,000 lines. A 1,300-line Python build wrote 12 files, three of them pages that were then parked. 101 files of test logs sat inside the project |
| A Base package someone can adopt | 65 | The four-file template and the decision-support example are sound |
| One process, one builder | 55 | The nine steps are solid, but they lived in a Python source, a generated process page, a chatbot coach, the skill, and a second nine-step page in the plan template |
| Reuse first | 40 | The reuse check was a step, not a habit. Anthropic's own `build-agent` skill does part of the job and was found only at the end |
| Proven | 65 | Real fresh-session tests: three coach rounds, two agent runs, nine runs of the decision tool on two decisions. All in Claude; no person |
| Level 3: connected and automated | 15 | No connected workflow. Autopilot was written and never run |
| **Overall** | **44** | Equal weights |

## What is carried over, and why

| Part | From version 1 | Here | Why it earned its place |
| --- | --- | --- | --- |
| The nine steps | `_build/steps.py` and `base/PROCESS.md` | [`PROCESS.md`](PROCESS.md), rewritten short | Stable since the fourth review; each step now names the decision it helps make |
| The builder skill, its project template and four checks | `level-2-files/agentic-process/` | [`builder/agentic-process/`](builder/agentic-process/), unchanged for now | Ran end to end once, unattended, in an empty repository |
| Autopilot | `level-2-files/AUTOPILOT.md` | [`builder/AUTOPILOT.md`](builder/AUTOPILOT.md), unchanged for now | The prompt and delivery targets are sound; never run |
| The fair-test rules | `level-3-files/fresh-run/RULES.md` | [`builder/TEST-RULES.md`](builder/TEST-RULES.md) | Every useful finding came from a session following these rules |
| The Base package template | `base/template/` | [`package-template/`](package-template/) | The shape the owner's spec asks for: explainer, runnable instructions, an example |
| The decision-support tool | `base/examples/decision-support/` | [`examples/decision-support/`](examples/decision-support/) | A complete tool, tested on two different decisions |
| What the tests taught | Logs and reports | [`LESSONS.md`](LESSONS.md), one page | The lessons, without the 101 files |

## What is left behind

All of it is kept, in [`workshop/plans/archive/agentic-process/v1-project/`](../../plans/archive/agentic-process/v1-project/):

- The build system (`build.py`, `pages.py`, `course_page.py`, `course.py`) and the files it wrote.
- The chatbot coach (`base/AI-INSTRUCTIONS.md`). The builder skill is plain Markdown and can be
  pasted into a chatbot, so one builder serves both. **Owner to confirm.**
- The guide, the North Star page and the course.
- The three older examples, made before the Base package existed.
- Level 3's gates file, score sheet and the full test logs.
