# README review: Learnings database

Reviewer stance: a busy small-business owner who uses ChatGPT or Claude daily and does not code.
Only `projects/learnings-database/README.md` was read.

## 1. What it does and who it is for

It is a set of chatbot instructions that keeps a running list of "next time, do this" lessons from
my mistakes and wins, and hands the relevant ones back before I start similar work. It is for
anyone who uses a chatbot for their work and keeps repeating the same slip-ups.

## 2. First screen: what I would do first, and how long it takes

From the first 40 lines, I would copy the grey box (lines 31 to 38), paste it into Claude or
ChatGPT, and send it. I have no log yet, so I would expect a starter file back. Then I would swap
the holiday-email example for a real mistake of my own.

- Copy, paste, send: about 1 minute.
- Reading the reply and working out what to do with the starter file: 3 to 5 minutes. The first
  screen does not say where to save that file or how to "paste the line it gives you" into it.
- Logging my first real lesson: another 2 to 3 minutes.

That makes about 5 to 10 minutes. But line 91 says loading by the link is "Not yet tried" and
"works only once this folder is on the main branch". So the first thing I am told to do may simply
fail, and I would not find out why unless I read to the bottom.

## 3. Trust and hesitation

**What makes me trust it**

- The first screen says plainly "Not yet used by a person" and "Tested in Claude". Nobody is
  overselling it.
- "Nothing is saved without your yes" and the weekly review where I accept rules. I stay in
  control.
- It is free, and the data lives in my own file or sheet.
- The ship's log comparison makes the idea click right away.
- A "real, unedited reply" example is linked, so I can see the output before I try it.
- The "What it is not" section tells me it will not try to be my whole knowledge base.

**What makes me hesitate**

- The main start method (the link) is listed as untested, and so is ChatGPT, which I use.
- "Works in any chatbot" on line 9 does not match "Not yet tried: ... ChatGPT" on line 91.
- I am not sure what I physically do with "one line to paste under your log". If I paste a line of
  text into Excel, does it go into the right columns, or into one cell?
- "Names and contact details are removed" is done by the chatbot, so it can miss things. The README
  says it as a promise.
- Half the page (levels 2 and 3, the status table) is written for a technical person. That makes me
  wonder whether level 1 is really the main product or only a demo.
- A "five-minute weekly review" is a new habit I have to keep. No person has used it, so the five
  minutes is a guess.

## 4. Confusing parts, jargon and strong claims

**Jargon I had to guess at**

- "an agent's instructions" (line 20). What is an agent here?
- "press **Raw**" (line 40). Raw where? On GitHub? I do not know what that button is.
- "this is a repeat of L-9" (line 51). I guessed L-9 is a row number. It is not explained.
- "accept, merge or retire" (line 53). I can guess "merge" and "retire" but am not sure what they do
  to my file.
- "MCP server", "Postgres", "Supabase", "pgvector", "MCP client", "csv_sync.py" (lines 63 to 88).
  None of these mean anything to me.
- "Searching by meaning ... with any embedding service" (line 71). This is opaque.
- "Saved as `proposed`" (line 69). What does that mean for me?
- "main branch" (lines 91 and 101). This is a coding term.
- "Passes `claude plugin validate`" (line 89). It means nothing to me.
- "filed by the type of learning ... and the kind of lesson" (line 15). What is the difference
  between the two? And "coding" is in my list even though I do not code.
- "It belongs to the newsletter." (line 37). This sounds odd. I guessed it means a project name,
  but should I always say what my lesson "belongs to"?
- "the lists on their own tab" (line 67). Which lists?

**Claims that seem too strong**

- "**Works in any chatbot**" (line 9). Only Claude has been tested.
- "Names and contact details are removed; anything about a client, a person or money is marked
  sensitive and never pasted elsewhere" (lines 22 to 23). This is a chatbot following instructions,
  not a guarantee. "never" is too strong.
- "Nothing is stored in this repository or sent anywhere by these instructions" (line 98).
  Technically true, but my log still goes to the chatbot company when I attach it. A careful reader
  could feel misled.
- "you always get the latest version" (line 28), together with "Not yet tried: loading the
  instructions by the link" (line 91).
- "exact and enough for a log of hundreds or thousands of rows" (line 72). Was this tested at that
  size? The status table does not say.
- "Final run passed every target" (line 86). It does not say which targets, so it is hard to judge
  without clicking.
- "a five-minute weekly review" (line 22). No person has done one yet.

## 5. Scores (1 to 100)

| Area | Score | Evidence |
| --- | --- | --- |
| Clear purpose | 88 | "Stop making the same mistake twice" plus the ship's log comparison tells me the job in two lines. "coding" and "agent's instructions" blur who it is for a little. |
| Getting started | 60 | The copy-paste box is excellent, but the link it relies on is "Not yet tried", and nothing says where to keep the starter file or how to paste the returned line into a spreadsheet. |
| Honesty about status | 82 | "Not yet used by a person" is on the first screen, and the untested list is specific. The badge "Works in any chatbot" contradicts "Not yet tried: ... ChatGPT". |
| Trust and privacy | 68 | "Where is my data?" is answered clearly and saving needs my yes. But "never pasted elsewhere" and "Names ... are removed" overpromise, and the page does not say the chatbot provider sees the log. |
| Plain language | 66 | The top half is plain and friendly. From line 60 down it is MCP, Postgres, pgvector, embedding service, main branch and Raw, with no "for your technical helper" signpost. |

**Overall: 71 / 100.** The idea and the top of the page are strong, and the status is honest. The
first action may fail today, the step after the reply is missing, and the privacy wording promises
more than a chatbot can guarantee.

## Top three fixes

1. **Make the first action safe to try today.** Either confirm the link works before publishing, or
   lead with the paste-a-copy path and note on the first screen that the link starts working once
   the tool is published. Change the badge to "Made for any chatbot, tested in Claude".
2. **Add the missing level 1 step.** In two or three plain lines, say where to save the starter
   file, which app to open it in, and exactly how to add the returned line (for example, "paste
   the table row into the first empty row"). Also say what "attach your log" means in ChatGPT and
   Claude.
3. **Tone down the privacy claims and fence off the jargon.** Say "it is told to remove names and
   contact details; check the row before you save it", and add "your log is shared with your
   chatbot provider when you attach it". Move levels 2 and 3, the test table and every technical
   term under a heading such as "For a technical helper".
