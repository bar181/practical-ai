<p align="center"><img src="_build/img/icon.png" width="104" alt="Learnings database icon: a ruled page with a tick"></p>

<h1 align="center">Learnings database</h1>

<p align="center"><b>Stop making the same mistake twice.</b><br>
Tell your chatbot "log that" when something goes wrong. Get the rules back before you start
similar work.</p>

<p align="center"><b>Free</b> &nbsp;·&nbsp; <b>For Claude, ChatGPT and other chatbots</b> &nbsp;·&nbsp; <b>Your log stays in your own file</b><br><b>Tested in Claude</b> &nbsp;·&nbsp; <b>Not yet used by a person</b></p>

<p align="center"><img src="_build/img/how-it-works.svg" width="620" alt="How it works in three steps: say log that with what happened and what you expected; get one filed row with the lesson as an instruction, saved after your yes, or a repeat counted; before similar work, the rules you accepted come back. The AI files and finds. You accept the rules."></p>

**Think of it as** a ship's log: one line each time the crew hits a rock or finds a faster channel,
read by the next crew before they sail.

- **One sentence in, one filed row out.** Say what happened and what you expected. You get one row,
  filed by the kind of learning (marketing, sales, finance and seven more), with the lesson written
  as an instruction: "When ..., do ...".
- **Repeats are counted, not copied.** When your log is attached, it checks it first. A lesson
  already there gets its count raised, so you can see what keeps happening.
- **The rules come back when you ask.** Say "before I start the price update" and get the rules
  that apply.
- **You stay in charge.** It asks before saving anything, and a lesson becomes a rule only when you
  accept it at a five-minute weekly review.

## Get started (two minutes)

1. Copy this, change the last line to your own lesson, and paste it into Claude, ChatGPT or another
   chatbot that can open links. (If it says it cannot open the link, use the paste route below.)

   ```
   Read the instructions at this link and follow them for the rest of this chat:
   https://raw.githubusercontent.com/bar181/practical-ai/main/projects/learnings-database/base/SKILL.md

   log that: the email about our holiday opening hours went out with last year's dates. I expected this year's dates.
   ```

2. **First time?** It gives you the starter spreadsheet, [`learnings.xlsx`](base/template/learnings.xlsx).
   Save it somewhere private and delete its twelve invented example rows. **Next time,** attach it
   to the chat (the paperclip or **+** beside the message box), so it can spot repeats.
3. **Keep the row.** The easiest way: say "yes, give me the updated file" and save it over your old
   one. Or copy the line it gives you into the first empty row and use **Data > Split text to
   columns** (Google Sheets) or **Data > Text to Columns** (Excel).

**Chatbot can't open the link?** Open [`base/SKILL.md`](base/SKILL.md), press **Raw** (the button
that shows the plain text), copy all of it into a new chat, then add your "log that" line. A real, unedited first reply:
[`base/examples/logging-a-lesson.md`](base/examples/logging-a-lesson.md).

## What to say

| You say | You get |
| --- | --- |
| `log that: [what happened]. I expected [what you expected].` | One row, or "this is a repeat of L-9" with its count raised |
| `before I start [the work]` | At most five accepted rules that apply, ready to paste into the next chat |
| `weekly review` | The rows waiting for you, each with a suggestion: accept, merge or retire (stop using it) |

## When you use it every week

| Level | What it is | Set up |
| --- | --- | --- |
| 1. A link | The steps above: any chatbot, your spreadsheet | None |
| 2. Saved once | The instructions saved in a Claude or ChatGPT project, or installed as a [Claude plugin](level-2-files/README.md). Some assistants that work in a folder on your computer can also keep the log there for you | About five minutes |
| 3. A shared database | Your team's log in [Supabase](level-3-files/README.md), an online database service with a free plan. You set it up in your browser by pasting one file (no programming), then connect it to Claude or ChatGPT. The assistant saves rows itself, after your yes, and keeps a history of every change | About fifteen minutes (an estimate: not yet tried on a real account) |

## What it is not

It keeps one thing: what to do differently next time, approved by you. It is not a wiki or a
knowledge base, not memory of your preferences, and not a coding tool.

## Status

**19 November 2026. Built and tested by Claude only. No person has used it yet.** Each check ran
in a fresh Claude session given only the instructions ([details](quality-results/README.md)):

| Check | Result |
| --- | --- |
| Filing 40 invented messages | Area right 40 of 40, lesson type 36 of 40, every non-lesson declined |
| Eleven cases: a vague request, a repeat, names and money, not a lesson, before I start, the review, a row that gives orders, the link start, a folder it can write to | 11 of 11 |
| The idea file, followed by a fresh agent in an empty folder over four sessions | Set up and working |
| Level 3: an assistant using the database through SQL only, 8 chats; the database test | 8 of 8; 24 of 24 |

**Not yet tried:** loading the instructions by the link (it works once this folder is on the main
branch), ChatGPT, Google Sheets, a real Supabase project and its connector, and use by a real
person on a real log.

## Questions

**Where is my data?** In your own file or database. Nothing is stored in this repository. When you
attach the log to a chat, the chatbot's company handles it like anything else you send there, so
keep client details out, or let it mark them sensitive.

**What does it cost?** Nothing beyond your chatbot. For level 3, Supabase's free plan should be
enough for a team's log of a few thousand rows (an estimate, not yet tried).

**How is it different from my chatbot's memory?** Memory keeps facts about you, automatically. This
keeps rules for the work, counted so you can see what repeats, and used only after you accept them.

---

Created by [Bradley Ross](https://www.linkedin.com/in/bradaross/). Built with
[Agentic Process](../agentic-process/); the plan and research are in
[`workshop/plans/learning-system/`](../../workshop/plans/learning-system/README.md). Examples use
invented data. Licence: [Apache 2.0](LICENSE).
