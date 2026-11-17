# Decision support: a complete tool, built with Agentic Process

Ask a business question in your chatbot. It researches it, writes a SWOT and recommends what to
do, as a short brief you check and share. It knows your business because you describe it once.

This folder is the end-to-end example: the spec, the tool, a run by a fresh chat, and the test
that improved it. The business in it is invented. **Nobody has used this tool on a real decision
yet.**

| File | What it is | Step |
| --- | --- | --- |
| [`WORKFLOW.md`](WORKFLOW.md) | The spec: one card with the trigger, inputs, steps, output, what a person checks, and the acceptance test | Steps 1 to 6 |
| [`AI-INSTRUCTIONS.md`](AI-INSTRUCTIONS.md) | The tool: instructions you paste into a chatbot project | Step 8 |
| [`example.md`](example.md) | One run by a fresh chat, unedited: an invented bakery asks whether to start office catering | Step 8 |
| This page | How to set it up, how to use it, and how it was built and tested | |

## Set it up once (about 5 minutes)

**Simplest, in any chatbot:** keep [`AI-INSTRUCTIONS.md`](AI-INSTRUCTIONS.md) in a document or a
note. Each time, start a new chat and paste the instructions, then your input, in one message.

**Better, so you never paste the instructions again:** save them in a project. All three below
are free.

| Chatbot | Where | Paste the instructions into | Add as files |
| --- | --- | --- | --- |
| ChatGPT | Sidebar: **Projects**, then **New project** | The project's **Instructions** (in its settings) | [`example.md`](example.md) |
| Claude | Sidebar: **Projects**, then **New project** | **Set project instructions** | [`example.md`](example.md), under project knowledge |
| Gemini | gemini.google.com (not the phone app): **Gems**, then **New Gem** | **Instructions**, then **Save** | [`example.md`](example.md), as knowledge |

Then start every chat from inside the project or Gem. To get a file from this page onto your
computer, open it, press **Raw**, and save the page; a Word document or a Google Doc with the same
text works too.

The first time you ask a question, it asks six questions about your business and writes a
profile. Save that profile in the project as a file (or keep it in your note and paste it in with
your question). It will not ask again.

The tool needs web search to research. Without it, it says so and lists what to look up.

## Use it every time

Open the project and type the decision, for example: *Should we start a weekday catering service
for offices near our shops?* You get the research with sources, the options compared, a
recommendation, a SWOT and a brief. For a polished one-page layout, you can also use
[Artifact Studio](../../../../../projects/artifact-studio/), another tool in this collection that lays out
documents and pages; it is optional.

**Before you act, check:** every figure against its source, every line marked "assumed" or
"proposal", and that the recommendation fits your goals. You decide. Use real business figures
only if your workplace allows that chatbot for them.

**Is it worth keeping?** On your first three real decisions, note the minutes from question to a
brief you would share, and how many points you had to correct.

## How it was built

The short path of Agentic Process, because one person turns one question into one brief in a
chat. Built on 16 November 2026.

| Step | What happened | Gate |
| --- | --- | --- |
| 1. Scope | The request ("decisions on gut feel; I want research, a SWOT and a recommendation") became one job: one question in, one brief out | Pass: one sentence in the card |
| 2. Reuse check | Chatbots already research and write SWOTs when asked. What they lack is a fixed workflow, a saved business profile and a rule for recommending. So: wrap, do not build software | Pass: build the instructions only |
| 3 to 5 | Nothing to buy; costs nothing beyond the chatbot; the design is one instructions file in a chatbot project | Pass |
| 6. Plan | The workflow card: trigger, inputs, steps, output, checks, what to do when something is missing, and an acceptance test | Pass |
| 7. Review | Folded into the test, as the short path allows | |
| 8. Build and test | The instructions, then nine runs by fresh sessions on two different decisions | See below |
| 9. Grow | Left open until it is used on real decisions | Open |

## What the tests found, and what changed

Nine runs by fresh AI sessions, each with only the instructions and one message, on 16 November
2026, all in Claude. Two invented decisions: the bakery's catering question, and a landscaping
firm choosing between renting, buying used or leasing a truck.

| Run | Decision | Blocking, minor | What it found, and the fix |
| --- | --- | --- | --- |
| 1 | Bakery | 2, 13 | No rule for turning scores into a recommendation. Fix: a written decision rule |
| 2 | Bakery | 2, 11 | "The smallest step" could mean a few calls or a trial; a limit written as a fact had no pass-or-fail reading. Fix: limits become one-line tests, marked "assumed" when interpreted |
| 3 | Bakery | 1, 11 | The trial rule and the scoring rule could point at different options. Fix: the trial becomes a scored option |
| 4 | Bakery | 0, 10 | The fix held |
| 5 | **Truck: a new decision** | **5, 8** | The rules had been tuned to the bakery: "include a trial" assumed a new product people buy, and nothing set a time horizon. Fix: one general rule, with a "check first" step instead of a trial option |
| 6, 7 | Both, after that fix | 3, 7 and 2, 8 | What remained were real judgement calls: how to shape the smaller option, what "better" means, twelve months or four years. Fix: list every judgement call, the other reading, and whether it would change the answer |
| 8, 9 | Both, after that fix | 1, 11 and 1, 10 | Both recommendations followed the scores and the rule. The one blocking point in each (a tie with "do nothing"; a score resting on a fact not found) is fixed and **not re-tested** |

From run 8, a judgement call the instructions make the tool disclose counts as minor, not
blocking, because the person sees it and checks it. Earlier runs counted it as blocking.

**The lesson for the method:** a fix that works for one input can break on the next. Step 8 now
asks for one more run with a different input of the same kind.

The logs, unedited, are in [`level-3-files/test-runs/decision-support/`](../../../../plans/archive/agentic-process/v1-project/level-3-files/test-runs/decision-support/).
The two decisions' final runs: [bakery](../../../../plans/archive/agentic-process/v1-project/level-3-files/test-runs/decision-support/round-6/result.md)
(also [`example.md`](example.md)) and [truck](../../../../plans/archive/agentic-process/v1-project/level-3-files/test-runs/decision-support/new-decision-3/result.md).
