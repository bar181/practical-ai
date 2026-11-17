# Quality results

What the checks have shown about Agentic Process, and the changes each result made to the
builder. The builder pilot's packages and raw review sit beside this page, unedited; earlier raw
logs are in `docs/reports/`. Runnable tools are in [`../base/examples/`](../base/examples/).

**The headline:** in one blind pilot, a tool built with Agentic Process scored 93/100. The
direct-build version scored 73/100 on the same brief. One build task, one unseen notice, one blind
reviewer.

The pilot packages are kept exactly as their builders handed them over, so their own status lines
still say "not yet run": the runs and the review below came afterwards.

## 1. Builder pilot: Document to action brief, 16 November 2026

**The task.** Two fresh Claude sessions got the same build brief: turn the
[document-to-action-brief plan](../../document-to-action-brief/_build/plan.md) into a tool an
owner can use with the chatbot they already have; Level 1 only; invented documents. Same repository
snapshot, same approved capabilities (read the repository, web search, write to one folder, no
installs, no questions). One followed the builder skill. The other built however it judged best,
with the Agentic Process files removed from its snapshot.

**Versions.** The builder skill, `PROCESS.md` and template as at commit `747c933`, before the move
to `projects/` (the move changed paths, not wording).

**The comparison.** Each package was then used by a fresh chat, following its own quick start, on
an unseen invented supplier notice whose **Effective Date is never given**. An answer key was
written before either package ran. A separate session reviewed both packages and results blind,
as X and Y.

| | Agentic Process | Direct |
| --- | --- | --- |
| Build time | 6 min 55 s | 7 min 50 s |
| Files in the package | 4 | 12 (including test scripts and a check sheet) |
| Key items found (of 9) | 9, all in the right place | 9, one in the wrong place |
| Quotes matching the notice word for word | 34 of 34 | 34 of 34 |
| Flagged the missing Effective Date | Yes, on the first screen, with who to ask | Yes, in the tables, with no next step |
| Corrections before the owner could act | 0 | 2 |
| Anything invented | No | No |
| Blind review score (out of 100) | **93** | **73** |
| The reviewer would hand to a busy owner | **This one** | |

[Both packages, both results, the notice, the answer key and the review](2026-11-16-builder-pilot/).

**What made the difference.** The reviewer traced both misses in the direct package to its
instructions: a polite "please" request was not counted as something to do, and there was no rule
to warn about missing dates. The builder's spec step made the other package name an exception
(U5: "the document leaves out what you need to act") and a recipient test (U4: "act without
rewriting"). Those produced a practice notice with no date and a warning block on the first screen.

**What did not work.** Neither builder could start a separate session, so neither ran its own
verification loop; the runs above were started from outside. One pilot, one notice and one
reviewer is a signal, not proof.

**The lesson that changed the builder.** When the builder cannot start a session, it now puts the
exact message for each case in the hand-back, so whoever started it can run them.

**Next:** repeat the comparison on a second job, then on a connected workflow, before calling the
verification loop proven.

## 2. Decision support and the first builder run, 16 November 2026

Decision support passed its three-input check in fresh Claude chats (AC-1). A plain chatbot on
the same question, graded blind three times: **86, 89 and 87 with the skill; 66, 61 and 67
without**, the same decision each time, and every grader preferred the plain answer's
readability. That finding is why the builder now has a recipient test. The builder also built a
second tool, the [learning log](../base/examples/learning-log/), whose check passed (AC-3).
[Raw reports](2026-11-16-decision-support-checks/).

**The lesson that changed the builder:** a result can hold up and still not be used. Check both.

## Methods borrowed into the builder, read 16 November 2026

Ideas rewritten in our own words; no text or code copied, nothing installed.

| Source | Version or date | Licence | What we took |
| --- | --- | --- | --- |
| Anthropic `build-agent` skill (small-business plugin) | Plugin 1.35.2 | Not stated in the package | Sort a job into fixed, varies and judgement; gate only what is consequential or where the owner hesitates; test on a known case before relying on it |
| [OpenAI cookbook: iterating development workflows with Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex) | 3 August 2026 | Not checked | A separate verification step that requires observed evidence, with external writes behind explicit approval |
| [GitHub Spec Kit, agentic SDD](https://github.github.com/spec-kit/reference/agentic-sdd.html) | Read 16 November 2026 | MIT | Every important requirement has a matching check before the work is called done |
| [Anthropic: Skills for enterprise](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise) | Read 16 November 2026 | Documentation | Read every file of an external skill, including scripts; look for network calls and tool use before trusting it |

## 3. A cold run of the starter guide, 16 November 2026

A fresh session read the README from the top and followed "Try it: build a tool" as a first-time
visitor, playing the coding agent too. It built the tool in about 3.5 minutes and found 1 blocking
and 15 minor points. The blocking one: run inside another agent, the builder could not start fresh
sessions, so the tool came back built but not ready, and the README had not said the tests could
fall to the person. Fixed: the README now says so up front, the build request names its catch, and
the builder says where test inputs, results and the hand-back go.
[Its friction notes and hand-back](2026-11-16-starter-run/).

## 4. The try-it-now prompt in a plain chatbot, 17 November 2026

A fresh Claude session, acting as a chatbot with no coding tools, got the "In the chatbot you
already use" prompt from the README with a meeting-notes job. In one reply it produced the
instruction file, a worked example and a 10-minute test, with no questions needed. It labelled the
example as written by hand, because a single chat cannot run a separate session; the test replaces
it with a real run. [The prompt, the reply and its notes](2026-11-17-chatbot-prompt/).
