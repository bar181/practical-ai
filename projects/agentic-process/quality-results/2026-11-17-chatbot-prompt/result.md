I had enough to build it, so I'm not holding you up with questions. I made two assumptions, listed at the end. Tell me if either is wrong and I'll adjust the file.

Below are three things: the instruction file to paste into a new chat, a worked example, and a short test.

## The usable result

- **U1, who uses it:** you, in ChatGPT, every Monday.
- **U2, what you give it:** that week's meeting notes, pasted in any format.
- **U3, what you get back:** a list of actions you can paste into an email, each with one owner and a due date.
- **U4, what makes it usable:** the problems come first, the email is ready to paste as plain text, and nothing is guessed.
- **U5, the mistake it must catch:** an action with no agreed owner, or with no date.

**Reuse check:** ChatGPT can already pull actions out of notes if you ask. What it won't do on its own is refuse to guess an owner or a date and flag the gap instead. Fixing that only takes clear instructions. So the right build is one short instruction file. You don't need any scripts, plug-ins or connections.

**Level:** start at Level 1 (paste the file each Monday). If pasting gets tedious, save it as a ChatGPT Project or custom GPT (Level 2). Connecting it to your email (Level 3) isn't worth it. You should read the list before it goes out anyway.

---

## 1. The instruction file

Copy everything in the box into a new ChatGPT chat, then paste your notes underneath. You can do both in one message.

```markdown
---
name: meeting-actions
description: Turns a team's meeting notes into an email-ready list of actions, each with one agreed owner and a due date, and flags any action with no agreed owner or no date so it can be settled before the list is sent.
---

# Meeting actions

You turn a team's meeting notes into a list of actions the user will email to the team.

## Step 1: check you have what you need

You need:
1. The meeting notes (pasted text, any format).
2. The meeting date, but only if the notes use relative dates ("Friday", "before next meeting",
   "end of month") and do not show the meeting date themselves.

If anything is missing, ask for all of it in one short message and wait. Do not start the list
until you have it. If nothing is missing, ask nothing and go straight to step 2.

## Step 2: find the actions

An action is a task someone will do after the meeting. Decisions, updates and discussion are not
actions unless they create a task. Write each action as a short phrase starting with a verb.

## Step 3: check each owner

An owner is agreed only when the notes show it:
- the person said they would do it ("I'll send it", "Sam will fix it"), or
- the person accepted it ("Priya: yes, I can do that"), or
- it is written as an assigned action ("Action: Lee", "Ana to send the budget").

An owner is NOT agreed when the notes say "someone", "we", "the team", "TBC", "maybe", "could",
"might", use a question mark, give two or more names with no lead, or do not tie a name to the task.

Never guess an owner.

## Step 4: check each date

A date is set when the notes give a day or a date ("by Thursday", "19 Nov", "before next
meeting", "end of month"). Work out the calendar date from the meeting date. Write it as weekday
and date, for example "Thu 19 Nov". If the notes used relative words, add them in brackets, for
example "Mon 30 Nov (end of month)".

These are NOT dates: "soon", "ASAP", "shortly", "next week", "when possible", "later", or nothing
at all.

Never invent a date.

## Step 5: write the result in this order

### Settle before you send

Show this first. For each action missing an agreed owner, a date, or both, write one line:
the action, what is missing, the words from the notes that show it, and the one question to ask
to settle it.

If there are none, write: "Every action has an agreed owner and a date."

### Email, ready to paste

Plain text only, no tables, so it pastes cleanly into any email.

Subject: Actions from [meeting name] on [meeting date]

Hi all,

Here are the actions from [meeting name] on [meeting date].

1. [Owner]: [action]. Due [date].
2. ...

Still needs an owner or a date:
- [action]. Needs [an owner / a date / an owner and a date].

(Leave out the "Still needs" part if nothing is missing.)

Thanks,
[leave the sign-off for the user to fill in]

### Count

One line: actions found, actions ready, actions to settle.

## Rules

- Use only what the notes say. Invent no owners, dates or tasks. If something is unclear, flag it.
  Do not quietly fix it.
- Keep people's names exactly as the notes write them.
- Do not send anything. The user reads the list, settles the flags and sends it.
- If the user replies with answers to the flagged questions, rewrite the email with those answers
  and move the settled actions into the main list.
```

---

## 2. Worked example

*Invented notes and names, made up to show the expected result. I wrote this result by hand to show the target. It is not the unedited output of a real run yet. Test case 2 below shows how to replace it with a real one.*

**Notes pasted in:**

```
Team meeting, Mon 16 Nov 2026. Present: Ana, Lee, Sam, Priya.
- Budget: Ana will send the Q1 budget to finance by Thursday.
- Website: Sam said he'd fix the broken contact form before next Monday's meeting.
- Rota: Lee will update the holiday rota.
- Printer: someone needs to chase the printer quote.
- Client visit: Priya to book the meeting room for the client visit, end of month. Priya: "I can do that."
- Newsletter: we should probably restart the newsletter. Lee maybe?
```

**Expected result:**

> **Settle before you send**
>
> 1. Update the holiday rota. Missing: a date. Notes say "Lee will update the holiday rota" with no day. Ask Lee: "When will the rota be updated?"
> 2. Chase the printer quote. Missing: an owner and a date. Notes say "someone needs to chase". Ask the team: "Who will chase the printer quote, and by when?"
> 3. Restart the newsletter. Missing: an agreed owner and a date. Notes say "Lee maybe?" Ask Lee: "Will you take the newsletter, and by when?"
>
> **Email, ready to paste**
>
> Subject: Actions from the team meeting on Mon 16 Nov 2026
>
> Hi all,
>
> Here are the actions from the team meeting on Mon 16 Nov 2026.
>
> 1. Ana: Send the Q1 budget to finance. Due Thu 19 Nov (by Thursday).
> 2. Sam: Fix the broken contact form on the website. Due Mon 23 Nov (before next Monday's meeting).
> 3. Priya: Book the meeting room for the client visit. Due Mon 30 Nov (end of month).
>
> Still needs an owner or a date:
> - Update the holiday rota (Lee). Needs a date.
> - Chase the printer quote. Needs an owner and a date.
> - Restart the newsletter. Needs an owner and a date.
>
> Thanks,
> [your name]
>
> **Count:** 6 actions found, 3 ready, 3 to settle.

---

## 3. Test (about 10 minutes)

Use a **brand-new chat** each time, and paste the instruction file first. Write down what you saw for each case.

**Case 1: something missing.** Paste the file, then only this:

```
Notes: Jo will renew the domain by Friday. Kim to order new chairs by end of month.
```

*Pass if:* it asks one short question for the meeting date (the notes say "Friday" with no date to count from), then stops and waits. *Fail if:* it guesses the date, or asks several separate questions.

**Case 2: the normal case.** Paste the file, then the example notes above.

*Pass if:* the result matches the example in substance. That means the same 3 ready and 3 flagged, the same dates, nothing added, and the flags come first. Then replace my hand-written example with its **unedited** output, so the example shows what the tool really does.

**Case 3: the mistake it must catch.** Paste the file, then:

```
Ops catch-up, Mon 9 Nov 2026. Present: Tom, Kim, Jo.
- Tom to send the March invoice by Friday.
- Action: Kim, server backup check.
- Jo might look into the van insurance.
- We agreed to review our prices soon.
```

*Pass if:* Tom's invoice is ready, due Fri 13 Nov. Three actions are flagged, each with a question to settle it:
- Kim's backup: no date.
- Jo's van insurance: owner not agreed ("might"), and no date.
- The price review: no owner, and "soon" isn't a date.

*Fail if:* it gives any of these an owner or a date the notes don't contain.

**For every case, read only the first screen and ask yourself:** would I paste this email to my team as it is? If you'd need to dig, rewrite or ask, it fails. Tell me what went wrong and I'll fix the file. Two rounds of fixes is usually enough.

**Status:** none of these checks have been run yet. I wrote the file and the example. Nobody has tested them in ChatGPT.

---

## What I assumed

1. **Notes are free text,** the kind someone types during the meeting. If yours follow a fixed format (a template, a Teams or Otter export), send me one sample with the names changed and I'll tune the file to it.
2. **A name written next to a task counts as agreed** ("Ana to send..."). If your team often writes names down for people who never said yes, tell me. I'll make the rule stricter, so a name only counts when the notes show the person accepting.
