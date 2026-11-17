# Quality results

What the checks have shown about Agentic Process, and the changes each result made to the
builder. Raw outputs stay in `docs/reports/`, unedited; runnable tools stay in `../examples/`.

## 1. Builder pilot: Document to action brief, 16 November 2026

**The task.** Two fresh Claude sessions got the same build brief: turn the
[document-to-action-brief plan](../../../plans/document-to-action-brief/README.md) into a tool an
owner can use with the chatbot they already have; Level 1 only; invented documents. Same repository
snapshot, same approved capabilities (read the repository, web search, write to one folder, no
installs, no questions). One followed the builder skill. The other built however it judged best,
with the Agentic Process files removed from its snapshot.

**Versions.** The builder skill, `PROCESS.md` and template as committed with this file, on top of
`783c1f6`.

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

[Both packages, both results, the notice, the answer key and the review](../../../../docs/reports/2026-11-16-builder-pilot/).

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
second tool, the [learning log](../examples/learning-log/), whose check passed (AC-3).
[Raw reports](../../../../docs/reports/2026-11-16-decision-support-checks/).

**The lesson that changed the builder:** a result can hold up and still not be used. Check both.
