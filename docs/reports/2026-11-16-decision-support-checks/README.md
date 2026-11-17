# Checks: decision support (AC-1) and the builder (AC-3), 16 November 2026

Every run was a fresh Claude session with web search, only the pasted `SKILL.md` and one message,
and no way to ask questions. Nothing below is edited. The rubric was written before any output
was read.

## AC-1: decision support

| Folder | Check | Skill version | Result |
| --- | --- | --- | --- |
| [`c1/`](c1/) | Decision only, no profile | As first written | Pass on behaviour, but it asked again for the decision it had been given |
| [`c1b/`](c1b/) | Same | Start section fixed | Pass |
| [`c2/`](c2/) | Full bakery input | As first written | Pass |
| [`c2b/`](c2b/) | Same | Brief first | Pass |
| [`c2c/`](c2c/) | Same | Short answer first, profile last (current) | Pass. Now the worked example |
| [`c3/`](c3/) | Dog groomer and a mobile van, with facts that cannot be found | As first written | Pass |
| [`base/`](base/) | Full bakery input, **no skill** | None | The baseline |

## Before and after, graded blind

Three separate grading sessions, each given the baseline and one skill version under the letters
A and B, the rubric, and the request. Each could spot-check three links per answer.

| Grade | Skill version | With the skill | Without | Which a busy owner would rather receive |
| --- | --- | --- | --- | --- |
| [1](BLIND-GRADE-1.md) (A = baseline) | As first written | 86 | 66 | Without |
| [2](BLIND-GRADE-2.md) (A = skill) | Brief first | 89 | 61 | Without |
| [3](BLIND-GRADE-3.md) (A = baseline) | Short answer first | 87 | 67 | Without |

**What it shows.** All three graders found the same decision both ways. The skill adds 20 to 28
points by dating every source, testing every limit, following a stated rule and labelling claims,
and its figures checked out more exactly (the baseline misattributed two). The plain chatbot reads
more easily, and every grader said a busy owner would rather receive it. Moving the useful part to
the top did not change that. The remaining causes, named by the graders: claim labels throughout
the brief, and the rule's "do nothing leads, so run the trial as the check" wording.

## AC-3: the builder

[`learning-log/`](learning-log/): the builder's hand-back and friction notes, the example it wrote
by hand (it could not start a fresh session, which it disclosed), and three fresh-chat checks of
the tool it built: [`l1/`](learning-log/l1/) missing context, [`l2/`](learning-log/l2/) the
example, [`l3/`](learning-log/l3/) a different log with a retired row and empty cells. All three
passed. The tool is in [`examples/learning-log/`](../../../workshop/drafts/agentic-process/examples/learning-log/).
