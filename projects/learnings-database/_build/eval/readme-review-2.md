# README review: Learnings database

Reviewer persona: a busy small-business owner who uses ChatGPT or Claude every day and does not code.
Only `projects/learnings-database/README.md` was read.

## 1. What it does and who it is for

It keeps a running list of lessons from things that went wrong or went well (one row each, written as "When ..., do ..."), and hands the right rules back before you start similar work. It is for anyone who repeats work and repeats mistakes. The README never names its reader outright, but the holiday-email example says "small business".

## 2. What I would do first, from the first screen (lines 1 to 40)

Copy the grey box, paste it into Claude or ChatGPT and send it. That takes 1 to 2 minutes, and I would get one lesson row back.

What the first screen does not tell me:
- It says "you get a starter file", but line 50 says to download `learnings.xlsx`. Which one do I keep?
- Keeping the row is a separate job: download the spreadsheet, delete twelve example rows, paste, then run "Text to Columns". That is another 5 to 10 minutes the first time and about 1 minute every time after.

Realistic total for the first lesson saved: about 10 minutes.

## 3. Trust and hesitation

**What makes me trust it**
- The banner says "Not yet used by a person". The Status section says "Built and tested by Claude only. No person has used it yet." That is rare honesty.
- "It asks before saving anything" and "nothing is used as a rule until you accept it".
- "Your log stays in your own file" and "Nothing is stored in this repository".
- It admits the chatbot company still sees what I attach: "the chatbot's company handles it like anything else you send there".
- It does not oversell the privacy step: "It is told to remove names ... check each row before you keep it."
- A real, unedited example reply is linked.

**What makes me hesitate**
- **The main start button may not work.** Status says the link loading is "Not yet tried ... it works only once this folder is on the main branch." The first thing the README asks me to do is the one thing it admits has not been tried. I cannot tell whether it works today.
- **ChatGPT is untested.** "Made for any chatbot" sits in the banner, but Status says ChatGPT is "Not yet tried". So is Google Sheets.
- **The instructions can change without me knowing.** "So you always get the latest version" also means they can change under me. The answer in Questions helps a little: "reviewed by a person", or paste a copy.
- **The pasting step looks fragile.** The lesson itself contains a comma ("When ..., do ..."). Will "split by comma" in Google Sheets break the row apart in the wrong places? The README does not say.
- **The time claim is untested.** "Five-minute weekly review" is promised, but no person has done one.

## 4. Confusing words, jargon and claims that seem too strong

**Jargon I had to guess at**
- "press **Raw**". I do not know GitHub, so I do not know what Raw is or where to find it.
- "main branch" (twice). Meaningless to me.
- "this is a repeat of L-9". I can guess L-9 is a row number, but nothing says so.
- "an agent's instructions". What agent?
- "accept, merge or retire". I can guess "merge", but "retire" a rule?
- "the kind of lesson". What kinds are there?
- "a row that gives orders" (in Status). Unclear.
- "MCP server", "Postgres", "Supabase", "pgvector", "embedding service", "`proposed`". These sit under "For a technical helper", which is fair, but "Searching by meaning is optional at level 3, with any embedding service" still leaks into plain reading.
- "Passes `claude plugin validate`". Means nothing to me.

**Claims that seem too strong**
- "**One line to log.**" Logging also takes a download, a paste and a Text to Columns step each time at level 1.
- "**No duplicates.**" This only works if I remember to attach the file every time. It is also the chatbot's judgment, not a guarantee.
- "**The rules come back when they matter.**" This sounds automatic. In fact I have to say "before I start ...".
- "**Made for any chatbot**". Only Claude has been tested.
- "Final run passed every target". "Final run" hints that earlier runs failed, and the targets are not stated on this page.
- "enough for a log of hundreds or thousands of rows". This is untested by a person, and pasting thousands of rows into a chat seems doubtful.

## 5. Scores (1 to 100)

| Area | Score | Evidence |
| --- | --- | --- |
| Clear purpose | 88 | "Stop making the same mistake twice" plus the ship's log analogy lands in two lines; the reader is never named. |
| Getting started | 62 | The copy box is quick, but Status says that link is "Not yet tried", the starter file appears in two places, and saving a row is a manual split step. |
| Honesty about status | 90 | "No person has used it yet" appears in both the banner and Status, with a clear "Not yet tried" list; docked for "Made for any chatbot" and the vague "passed every target". |
| Trust and privacy | 74 | Asks before saving, keeps the log in your own file, and admits the chatbot company sees attachments; docked because the privacy step is only "told to", and the instructions load from a link that can change. |
| Plain language | 76 | Short sentences, no em dashes, a good analogy; "Raw", "main branch", "L-9", "retire" and "agent's instructions" go unexplained in the part meant for me. |

**Overall: 76 / 100.** The plain average is 78. I took it down because getting started is the area that decides whether I try the tool at all.

## Top three fixes

1. **Make the first action certain to work.** Either confirm the link loads today (and update Status), or lead with the paste method until it does. Use one starter-file story: either "download this" or "the chatbot gives you one", not both.
2. **Be honest about the cost of saving a row, or cut it.** Change "One line to log" so the manual paste and split step is visible. Say how long it takes. Confirm that a lesson containing commas survives "Split text to columns" in Google Sheets.
3. **Do a plain-language pass on the first two screens.** Explain or remove "Raw", "main branch", "L-9", "agent's instructions" and "retire". Tone "Made for any chatbot" down to "Tested in Claude; should work in others". Say "when you ask" in "The rules come back when they matter".
