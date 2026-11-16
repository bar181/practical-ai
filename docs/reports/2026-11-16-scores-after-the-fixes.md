# Scores after the fixes: project one and project two

Written on 16 November 2026 by the assistant that built both, with no second reviewer. Read it as
the author marking their own work. The goal set for this round was every measure at 80 or above.
**That goal is not met, and this page says where and why.**

**Think of it as** a restaurant that has now served the same three dishes to strangers four
times and written down every complaint. The kitchen is better. Nobody has yet paid for a meal.

## Project one: Artifact Studio

**Overall: 78 out of 100**, up from 70 on 15 November.

| Measure | 15 Nov | Now | Evidence | At 80? |
| --- | --- | --- | --- | --- |
| The landing page | 86 | 86 | A hook, four callouts, one picture, "Try it in five minutes". Every link checked by script | Yes |
| The kitchen sink, `base/studio.html` | 90 | 91 | 46 tabs. Each checked in Chrome at three widths and in the WebKit engine Safari is built on | Yes |
| Worked examples, `base/examples/` | 66 | 84 | Ten pages, each the unedited result of a fresh session given the prompt shown on the page | Yes |
| The paste-in instructions | 60 | 78 | 22 fresh-session runs. Every run finished a page. Detail below | **No** |
| The one-link prompt | 55 | 72 | A fresh Claude session fetched the link and finished its page. Never tried in another assistant | **No** |
| The skill and the MCP server | 70 | 81 | A second agent ran the skill end to end. Another used only the server's tools and found a real fault, now fixed and tested | Yes |
| Honesty of the status lines | 92 | 92 | Each says who has and has not tried the thing | Yes |
| Accessibility and devices | 74 | 82 | Automated scan clean. Two browser engines. No real phone, Firefox or screen reader | Yes |
| How clean the repository is | 72 | 86 | Three folders at the root: `projects`, `docs`, `workshop`. Older drafts archived. 0 broken links in 258 Markdown files | Yes |
| Evidence of real use | 15 | 30 | The owner asked for one page and used it. Nobody else has | **No** |

### The instructions, round by round

The same three requests (a keynote deck, a one-page report, three social posts) were given to a
fresh session after each round of fixes. A blocking point is one where two careful readers
would have built visibly different pages.

| Round | Deck | Report | Social posts | Total blocking |
| --- | --- | --- | --- | --- |
| 2 | 3 | 6 | 4 | 13 |
| 3 | 3 | 3 | 3 | 9 |
| 4 | 2 | 3 | 1 | 6 |

Round 1 was the thirteen first runs, which did not count blocking points separately. The six
points from round 4 are fixed and have **not** been tested again. From round 3 the word
"blocking" was defined in the test rules; in round 2 each session used its own judgement, so the
drop from 13 to 9 is partly the stricter definition.

The score stays at 78 because the bar for 80 is a round with no blocking points, and no round
has reached it. Each round's list is new: the sessions do not repeat old points, they find
smaller ones. The logs are in
[`artifact-studio/_build/examples/runs/`](../../projects/artifact-studio/_build/examples/runs/).

### Three measures that cannot reach 80 from here

| Measure | What it needs | Who can do it |
| --- | --- | --- |
| The one-link prompt | The "Try it" prompt run in ChatGPT and in Gemini, and the result noted | The owner, in ten minutes |
| The instructions | One more round with no blocking points, or the same result in a second assistant | The assistant, in a later session |
| Real use | Three people who are not the author using it for real work | The owner's class |

## Project two: Agentic Process

**Overall: 67 out of 100.** Built in one sitting on 16 November by following its own nine steps.
Scored against its own sheet,
[`level-3-files/scorecard.md`](../../projects/agentic-process/level-3-files/scorecard.md).

| Measure | Score | Evidence | At 80? |
| --- | --- | --- | --- |
| The front door | 82 | A hook, one picture, a prompt to paste, a table by level. No stranger has read it | Yes |
| The beginner version | 82 | One file. Four fresh sessions each produced a plan, a first version and a note from it alone | Yes |
| Worked examples | 76 | Two unedited fresh-session results, Beginner and Advanced, and project one step by step. None for the Expert level | **No** |
| The instructions | 70 | Two rounds, two ideas. Blocking points: 9, then 7. Fixed after each round, not tested a third time | **No** |
| Other assistants | 20 | None tried | **No** |
| The advanced files | 72 | A second agent ran the skill and the template end to end. The layout check passed first time. Two commands failed as written (no path for the template script, no gates file in the template). Both are fixed and tested by the author, not re-run by a second agent | **No** |
| Honesty | 92 | Every status line says who has tried the thing. The one estimate is labelled | Yes |
| Devices and access | 82 | The explainer passes an accessibility scan at three widths in Chrome, works with scripts off and loads cleanly in WebKit | Yes |
| A clean folder | 88 | Passes the layout check. Six things in `base/`, three in each level folder | Yes |
| Real use | 10 | None. The explainer was made with project one, which counts for project one | **No** |

### What the coach's tests found

The first round found three faults the author had read past: the second gate ran backwards (yes
meant stop while every other gate's yes meant go on), the eighth gate asked for a test result
nobody had, and "decide when you cannot ask" collided with "never invent a fact". All three are
fixed. The results of the second round are kept as the worked examples, unedited, with their
friction logs beside them.

## Is the repository easy to use, by kind of user?

| User | Path | Works today? |
| --- | --- | --- |
| A beginner with a chatbot | Paste one prompt from the README | Yes in Claude. Unknown in others |
| A beginner who wants to browse | Download one HTML file and open it | Yes on a laptop. **On a phone it is awkward**: GitHub shows HTML files as code, so the page has to be downloaded first. Turning on GitHub Pages would give every page a link that opens |
| A teacher | Two lesson plans, 30 minutes each | Written. Neither has been taught |
| A builder with a coding agent | A skill and a template in `level-2-files/` | Tested by a second agent on both projects. On project two it found two commands that failed; they are fixed |
| A team running agents | An MCP server, gates, the fresh-run test | Tested by agents. Not tried in a desktop assistant |

## What to do next, in order

1. The owner runs the two "Try it" prompts in ChatGPT and Gemini. This is the cheapest way to
   move three scores.
2. Turn on GitHub Pages, so the explainer and the gallery open from a link on a phone.
3. Teach one of the lesson plans and correct its timings.
4. Build the next tool, the document-to-action brief, with Agentic Process from step 1, and time
   it. That is the first real use of project two.
