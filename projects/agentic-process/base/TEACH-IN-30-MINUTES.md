<!-- Written by _build/build.py from _build/lesson.py. In the repository, change lesson.py and rebuild. A copy you keep can be edited by hand. -->
# Teach Agentic Process in 30 minutes

A lesson plan for one teacher and any number of learners. Nobody needs to code. Each learner
needs a chatbot they already use, and one job they repeat at work.

**By the end** each learner has a one-page plan for a small AI tool of their own, and knows the
one test that finds its faults.

**Present from** [`training.html`](training.html): the slides for this plan, with a lesson timer,
these notes, and a presenter window that keeps them off the projector. Open it from the link in the
project's README, or on GitHub open the file, choose **Download raw file**, and open it in a browser.

## Before the lesson

| Do this | Time |
| --- | --- |
| Open [`training.html`](training.html) on the screen you will present from. Press N to see your notes | 1 minute |
| Keep [the guide](explainer.html) open in a second tab, to show a step card if asked | 1 minute |
| Ask each learner to bring one job they do on their own every week that starts from a blank page | The day before |
| If several learners use a chatbot that cannot open links, put the coach's text in a shared document | 5 minutes |

## The lesson

| Minutes | You do | You say | Learners do |
| --- | --- | --- | --- |
| 0 to 3 | Show the first slide | "An AI will build whatever you ask. It will also build the wrong thing, quickly and with confidence. Today is about the order of work that stops that." | Listen |
| 3 to 7 | Show the inspector slide | "Think of a building site with an inspector. Nothing moves to the next stage until the current one is signed off. Our sign-off is a question called a gate." | Say one job they repeat, in one sentence, to the person beside them |
| 7 to 12 | Show the four stages, then the step card | "Nine steps in four stages. Every step has a purpose, a proof you are done, a prompt to paste, and a gate: the question you answer before you move on." | Write down which step they usually skip |
| 12 to 22 | Share the prompt. Walk the room | "Paste it in. Change the last line to your job. Say yes to the short path: it does steps 1, 6 and 8 in full and the rest in a line each, so it fits in ten minutes. Stop when it shows you the plan." | Run the coach on their own idea, on the short path, until it shows them the one-page plan |
| 22 to 26 | Share the review prompt | "You cannot see your own gaps, because you know what you meant. This is step 7: hand your plan to a stranger, a new chat that has never seen it. The short path folds this into the test at step 8. In class we do it now, because it is the habit that matters most." | Open a new chat, paste the review prompt and their plan so far, and read what it had to guess |
| 26 to 30 | Ask the three questions, then show the card | "What will you do first when you are back at your desk?" | Answer aloud. Write the next step on their plan |

## The prompts learners paste

**At minute 12, the coach:**

```
Read the build coach at https://raw.githubusercontent.com/bar181/practical-ai/main/projects/agentic-process/base/AI-INSTRUCTIONS.md and follow it. If you cannot open it, say so and stop: do not make up a coach of your own.

My idea: [one job you do on your own, in one sentence]
```

**If the chatbot cannot open the link:** open the coach on GitHub, press Raw, copy all of it, paste it into the chat, then:

```
Follow the build coach pasted above.

My idea: [one job you do on your own, in one sentence]
```

**At minute 22, the review in a new chat:**

```
You have never seen this project. Read the plan below. Explain it back in five sentences, then list every place where you had to guess, quoting the line. Do not improve the plan. Only report.

[paste your plan so far]
```

## The three check questions, at minute 26

1. **The reuse check finds a free tool that does the whole job. What now?** Stop, and write a short guide to that tool. The second gate exists to save you from building what already exists.
2. **Why fix the folder layout before anything is built?** Every file points at other files. Moving them later breaks those links, and you pay for the move each time the shape changes.
3. **A fresh session finishes the job and lists twelve problems. Did the test pass?** Yes. It finished, and the twelve problems are the next hour of work: first the ones in two or more logs, then the blocking ones.

## What to watch for

| You see | It means | Say |
| --- | --- | --- |
| A learner describing three jobs | The scope is too wide | "Which one would you miss most on Monday? That one. The others go under Next." |
| The coach found an existing tool | The process worked | "Good. You just saved a week. Write the guide to that tool." |
| A learner skipping the questions to get to the build | The usual habit | "The inspector does not let you choose curtains yet." |
| A chatbot that cannot open the link | Common | Show the next slide: paste the coach, then "Follow the build coach pasted above." |
| A learner whose job involves a team or shared files | The coach takes all nine steps, about an hour | "Pick a part you do on your own for today. The team version is your homework." |
| The coach offers the short path | A small job, in a chat | "Say yes. You will still do steps 1, 6 and 8 in full." |

## After the lesson

Homework: each learner runs the step 8 test in a new chat and sends you two things: the plan,
and what the new chat said was unclear. The second one tells you more than the first.

This plan has not yet been taught. The timings are estimates: change them after your first run.
