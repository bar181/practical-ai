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

1. Make a project in your chatbot: a Claude Project, a ChatGPT Project or a Gemini Gem. Or use a
   folder your chatbot can read, such as a Drive folder connected to it.
2. Paste [`AI-INSTRUCTIONS.md`](AI-INSTRUCTIONS.md) into the project's instructions.
3. Add [`example.md`](example.md) as a project file, so it sees what a good brief looks like.
4. Ask your first question. It asks six questions about your business once and writes a profile.
   Save that profile as a file in the project. It will not ask again.

The tool needs web search to research. Without it, it says so and lists what to look up.

## Use it every time

Open the project and type the decision, for example: *Should we start a weekday catering service
for offices near our shops?* You get the research with sources, the options compared, a
recommendation, a SWOT and a brief. If you want the brief laid out as a polished page and your
project has [Artifact Studio](../../../../artifact-studio/), ask for a polished version.

**Before you act, check:** every figure against its source, every line marked "assumed" or
"proposal", and that the recommendation fits your goals. You decide.

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
| 8. Build and test | The instructions, then two rounds by fresh sessions that had only the instructions and one message | See below |
| 9. Grow | Left open until it is used on real decisions | Open |

## What the test found, and what changed

A fresh chat with only the instructions and an invented bakery's question found **2 blocking
points and 13 minor ones** in round 1. The biggest:

| What the fresh chat hit | The change that fixed it |
| --- | --- |
| "Score each option ... Recommend one option." There was no rule for turning the scores into a recommendation, so a reader who weighted sales growth most could pick a different option from the same table | A decision rule: limits are pass or fail; of the rest, the option better on the most goals wins, goals in the profile's order; a tie goes to the smaller step |
| The fact that decides the question (how many nearby offices would order) cannot be found on the web, and nothing said whether to recommend anyway | If a deciding fact is "not found", recommend the smallest step that would find it out, and say so |
| The SWOT came before the comparison, so the "leading option" had to be picked before it was justified | Compare and recommend first; the SWOT is for the recommended option |

Round 2, with those fixes: **2 blocking, 11 minor**, both new and narrower. "The smallest step"
could mean a few calls instead of a trial, and a limit written as a fact ("the head baker already
works six days") had no pass-or-fail reading. The fixes: write each limit as a pass-or-fail test
and mark any reading "assumed"; score worse as minus one; let risk set the size of the step; when
a deciding fact is not found, recommend a capped trial with the cheap checks as its first steps.

Round 3: **1 blocking, 11 minor**. The trial rule and the scoring rule could point at different
options. The fix, not yet re-tested: any question about starting something new includes a capped
trial as one of its options. All three rounds recommended the same thing, a capped trial from one
shop, with different proposed numbers each time.

The full logs, unedited: [round 1](../../../level-3-files/test-runs/decision-support/round-1/friction.md)
[round 2](../../../level-3-files/test-runs/decision-support/round-2/friction.md) and
[round 3](../../../level-3-files/test-runs/decision-support/round-3/friction.md).
