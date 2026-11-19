# README review 3: Learnings database

Reviewer persona: a busy small-business owner who uses ChatGPT or Claude every day and does not code.
Read only `projects/learnings-database/README.md`.

## 1. What it does, and who it is for

It is a set of instructions I paste into my chatbot so that when something goes wrong I say "log that", it
writes the lesson as one spreadsheet row, and before similar work it hands me back the rules, for anyone
(solo or a small team) who keeps repeating the same avoidable mistakes.

## 2. From the first screen only: what I would do first, and how long

What I would do, in order:

1. Copy the grey box under "Get started (two minutes)", change the last line to a real mistake of mine
   (say, "the invoice reminder went to the old contact"), and paste it into ChatGPT or Claude.
2. Get the starter spreadsheet `learnings.xlsx`, save it somewhere private, and delete the twelve example rows.
3. Copy the line the chatbot gives me into the first empty row and use "Split text to columns".

How long: about 2 minutes for step 1. With steps 2 and 3 the first time, more like 8 to 10 minutes,
because I have to find and download the spreadsheet, delete the rows, and work out the split-columns menu.
"Two minutes" holds only for the paste.

Two problems I only found later:

- At line 79, under "Not yet tried", it says: "loading the instructions by the link (it works once this
  folder is on the main branch)". That reads as if the step I was told to do first **may not work today**.
  The first screen says nothing about this. If the link fails, the fallback (line 43) is to "press **Raw**",
  and I do not know what Raw is.
- Step 2 says "It gives you the starter spreadsheet". Does the chatbot make me a file, or do I click the
  link in the README? I would guess the README link, but it is not clear.

## 3. What would make me trust it, and what would make me hesitate

**Trust:**

- It is upfront: "Tested in Claude · Not yet used by a person" sits on the first screen, and the Status
  section repeats "No person has used it yet."
- "It asks before saving anything" and rules only count once I accept them. I stay in control.
- "Your log stays in your own file". Nothing goes to the people who made it.
- The privacy answer is honest that the chatbot company still sees what I attach, and tells me to keep
  client details out.
- It is free, and there is "A real, unedited first reply" I can look at before trying.
- The ship's log comparison makes the idea click at once.

**Hesitate:**

- The main start step (the link) is listed as not yet tried. That is the first thing I would do.
- Copying a row by hand and splitting columns every time is the kind of chore I would drop after a week.
- The weekly review only works if I remember it. Nothing says what reminds me.
- Nobody, not even one real person, has used it. I would be the guinea pig.
- ChatGPT, which I use most, is listed as "Not yet tried".

## 4. Confusing words, guessed jargon, claims that seem too strong

**Jargon I had to guess at:**

- "press **Raw**" (a GitHub button, I assume).
- "it works once this folder is on the main branch" (developer talk; I cannot tell if it works today).
- "L-9" in "this is a repeat of L-9" (I guess a row number, but the README never says rows get IDs).
- "merge or retire (stop using it)": retire is explained, merge is not.
- "For an agent with a folder, the idea file sets it up for you": I do not know what "an agent with a
  folder" or "idea file" means.
- "Claude plugin (`/log`, `/before-i-start`, `/weekly-review`)": slash commands mean nothing to me.
- "Supabase", "Supabase's own connector", "the database file on a real Postgres", "through SQL only".
- Status bullets read like test labels, not plain English: "a row that gives orders", "the link start",
  "a folder it can write to".
- "let it mark them sensitive": how? What happens to a sensitive row?

**Claims that seem too strong or untested:**

- "Get started (two minutes)": true for the paste, not for the whole first run.
- Level 3: "No code" next to "set up in the browser by pasting one file". Pasting a database file sounds
  like code to me, even if I do not write it.
- Level 3: "About fifteen minutes", while the Status says "a real Supabase project and its connector" is
  not yet tried. So fifteen minutes is a guess, but it is written as a fact.
- "Supabase's free plan is enough for a team's log": I have no way to check this, and no one has run it.
- "Stop making the same mistake twice": fine as a slogan, but it only works if I log and review regularly.

## 5. Would I try level 3 for my team? What would stop me?

Not yet. What would stop me:

- It is the least tested part: "a real Supabase project and its connector" has not been tried by anyone.
- I have never heard of Supabase. I would be creating a new account with a company I do not know and
  putting my team's mistakes in it. The README does not say who can see that database or how to give
  staff access.
- "Pasting one file" into a database setup screen is outside my comfort zone, whatever "No code" says.
- I would want to see level 1 work for me for a month first, then maybe level 2 as a Claude or ChatGPT
  project. Level 3 would need either a real person who has done it or a short video of the fifteen minutes.

## 6. Scores (1 to 100)

| Area | Score | Evidence |
| --- | --- | --- |
| Clear purpose | 88 | "Stop making the same mistake twice" plus the ship's log comparison and "One sentence in, one filed row out" tell me what it does in ten seconds. |
| Getting started | 60 | The copy box is clear, but the link step is "Not yet tried" (line 79, not on the first screen), the fallback says "press Raw", and step 3 is a manual split-columns chore. |
| Honesty about status | 88 | "Not yet used by a person" on the first screen and a clear "Not yet tried" list; loses points because "fifteen minutes", "No code" and "free plan is enough" are stated as facts for untested parts, and the link caveat is buried. |
| Trust and privacy | 76 | "Your log stays in your own file", "asks before saving anything", and an honest note that the chatbot company sees attachments; "let it mark them sensitive" is vague and level 3 access is not explained. |
| Plain language | 68 | The top 45 lines are plain; levels, status and level 3 slip into Raw, main branch, plugin, idea file, Postgres, SQL and connector. |
| Value for a business | 72 | Repeat mistakes cost real money and this is free, but the value depends on my discipline with hand copying and a weekly review I have to remember. |

**Overall: 75 / 100.** The idea is clear and the honesty is better than most tools I see. What holds it back is
the first step: the step I am told to do first is marked untested further down, and keeping the log takes
manual work every time.

## Top three fixes

1. **Make the first step work or say so on the first screen.** Either get the link working before
   anyone reads this, or put the "paste the instructions in" route first and the link second. Do not
   leave "it works once this folder is on the main branch" at line 79 under a "two minutes" promise.
   Explain "Raw" in plain words ("the button that shows plain text").
2. **Cut the spreadsheet chore.** Make the reply paste straight into separate columns (or say "click
   cell A in the first empty row and paste"), and say clearly where the spreadsheet comes from ("click
   this link to download it"), not "It gives you".
3. **Plain-language and claims pass on levels 2 and 3.** Explain Supabase in one phrase, drop
   Postgres, SQL, plugin slash commands, "idea file" and "agent with a folder" from the main page, and
   mark "About fifteen minutes", "No code" and "free plan is enough" as untested estimates until a real
   person has done it.
