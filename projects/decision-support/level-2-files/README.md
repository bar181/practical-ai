# Level 2: save it, run it step by step, and check the links

For anyone who makes a decision like this every month, and for agentic engineers who want each step
as its own skill. Three additions to Level 1.

| You want | Do this once |
| --- | --- |
| **Every chat to know the process** | Add [`../base/SKILL.md`](../base/SKILL.md) as a skill in Claude, or paste it into a Project's instructions (ChatGPT Projects and Gemini Gems take the same text; not yet tried) |
| **One skill per step** | Add the seven folders in [`skills/`](skills/) as skills. Each holds one step, the rules, and only the parts of the process that step needs, so an agent can run, review or redo one step at a time |
| **Every quoted link checked by a program** | Run [`check_sources.py`](check_sources.py) on the finished brief. Python 3, nothing to install |

## Your standing preferences

Under the instructions, add a few lines, for example:

```
Who usually decides: the managing partner.
What we always weigh: two-year cost, disruption to clients, contract length.
Our rules that must be met: call recordings kept for 12 months.
Voice: executive, unless I say "for the team" or "ADR".
```

## The step skills

| Skill | Does |
| --- | --- |
| [`decision-step-1-define`](skills/decision-step-1-define/SKILL.md) | The question, who decides, by when, what would change the answer, whether it can be undone, and the depth and voice |
| [`decision-step-2-structure`](skills/decision-step-2-structure/SKILL.md) | The options, always with "do nothing", up to six criteria, the question broken into parts |
| [`decision-step-3-prioritise`](skills/decision-step-3-prioritise/SKILL.md) | A best guess per part, and the two or three parts that decide the answer |
| [`decision-step-4-plan-the-evidence`](skills/decision-step-4-plan-the-evidence/SKILL.md) | The evidence for and against each guess, named before anyone looks |
| [`decision-step-5-analyse`](skills/decision-step-5-analyse/SKILL.md) | The evidence with exact words, links and a result each, and the options table |
| [`decision-step-6-synthesise`](skills/decision-step-6-synthesise/SKILL.md) | The answer, three reasons, the evidence against, the premortem, the confidence |
| [`decision-step-7-recommend`](skills/decision-step-7-recommend/SKILL.md) | The executive brief or the decision record (ADR) |

They are generated from `base/SKILL.md` by `_build/build_step_skills.py`, so the one-file skill and
the step skills never drift apart. Change `base/SKILL.md`, then rebuild.

**For agent pipelines:** run steps 1 to 4 in one context, give step 5 to a researcher with web
access, then give the brief from step 7 and [`../base/rubric.md`](../base/rubric.md) to a separate
reviewer that has not seen the working, so the work is not grading itself.

## Check the links

```
python3 check_sources.py my-brief.md
```

It reads the Sources table, opens each link and looks for the quoted words on the page. Each row
comes back **OK**, **WORDS NOT FOUND**, **COULD NOT OPEN** or **NO LINK** (their own figures). It
exits with code 1 if a row the brief marks "Checked" is not OK, so you can put it in a checklist or
a pull request check for decision records.

Some sites block programs (Harvard Business Review does). Those come back COULD NOT OPEN: open them
in your own browser. The checker only reads pages; it never sends anything.

## Status

**24 November 2026.** The checker passes its tests on a local test server (six rows: found, found
with curly quotes, found in two parts, words missing, page missing, no link; and the exit-code
rule): `python3 _build/test_check_sources.py`. The step skills are generated and their frontmatter
parses. **Not yet tried:** the saved version in a Project, the step skills run one by one by an
agent, the checker on live websites (the build machine could not reach them), ChatGPT, Gemini, and
use by anyone else.
