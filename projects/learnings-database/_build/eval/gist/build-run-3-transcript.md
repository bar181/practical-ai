# Transcript: setting up the learnings log

What the agent said to the person, in order. Person's replies are quoted in each step. Date: 2026-11-19.

## Session 1

### Before step 1: create the log

> I'll set up a learnings log in this folder. First I'd like to make a folder called `learnings/`
> and a file in it, `learnings/learnings.csv`, with one header line and no rows yet. May I create
> them?

Person: "yes"

> Done. `learnings/learnings.csv` exists with the header line.

### Step 2: add the instructions

> I'm Claude, so the instructions file I read at the start of every session is `CLAUDE.md`. There
> is no `CLAUDE.md` in this folder yet. May I create it and add the "Learnings log" section, with
> its credit lines to Bradley Ross?

Person: "yes"

> Done. `CLAUDE.md` now holds the "Learnings log" section, unchanged. It ends with a "Projects" line
> that is still blank.

### Step 3: set the projects

> What are your current projects or jobs? Just the names.

Person: "the spring sale, the newsletter, and supplier onboarding"

> I'll write them lowercase with hyphens: `spring-sale`, `newsletter`, `supplier-onboarding`. I
> dropped "the". May I change `CLAUDE.md` to put them on the Projects line?

Person: "yes"

> Done. The Projects line now reads:
> `Projects (use these names in the project column): spring-sale, newsletter, supplier-onboarding`

### Step 4: log the first lesson together

> Now let's log one lesson so you can see how it works. Tell me about one thing that went wrong
> recently: what happened, and what you expected.

Person: "The newsletter went out with a broken link to the booking page because nobody clicked
the links before sending. I expected every link to work."

> That is a lesson. I searched the log: it is empty, so this is a new row. Here it is:
>
> | Column | Value |
> | --- | --- |
> | id | L-1 |
> | date | 2026-11-19 (you said "recently", so I used today) |
> | kind | error |
> | area | marketing |
> | project | newsletter |
> | lesson_type | check |
> | rule | When sending a newsletter, do click every link to check it opens the right page before it goes out. |
> | what_happened | The newsletter went out with a broken link to the booking page. |
> | expected | Every link to work. |
> | why | There was no step to click the links before sending. |
> | tags | newsletter;links;checking |
> | severity | (empty) |
> | status | proposed |
> | seen | 1 |
> | source | chat |
> | sensitive | no |
> | confidence | (empty) |
> | review_by | (empty) |
>
> Empty cells: severity, confidence and review_by. You did not say them, so I left them blank.
>
> Add it to the log?

Person: "yes"

> Added. `learnings/learnings.csv` now has row L-1, status proposed. No other line changed.
>
> A proposed row is not a rule yet. Shall I accept L-1 now, so it becomes a rule I follow? That
> changes its status from proposed to accepted.

Person: "yes, accept it, I'm Pat"

> Thanks, Pat. Changed: L-1 status proposed to accepted. Nothing else changed. The log now holds
> one rule. (The log has no column for who accepted a row, so your name is not recorded in it.)

### Step 5: show the habit

> What is the next real piece of work you're starting?

Person: "Write the newsletter for December."

> Before I start: I read the accepted rules whose project is `newsletter` or empty. One applies.
>
> Following: **L-1**. When sending a newsletter, do click every link to check it opens the right
> page before it goes out.
>
> So once the December newsletter is drafted, I will list every link in it and we will click each
> one before it goes out. I cannot click your live links myself, so I'll give you the list to check.
>
> To write it, I need the content: what is on offer in December, any dates, and the links you want
> in it (booking page, and anything else). I won't invent any of these; tell me and I'll draft it.

### Step 6: what happens next

> You're set up. From now on:
>
> - Say **"log that"** whenever something goes wrong, has to be redone, or works better than usual.
>   Tell me what happened and what you expected. I'll show you the row before saving it.
> - Say **"weekly review"** once a week. I'll list new lessons and suggest which to keep. It takes
>   about five minutes.
> - Say **"before I start"** with the work, and I'll tell you which rules I'm following.
> - The log is `learnings/learnings.csv`. Open it in any spreadsheet to read or edit it by hand.

## Session 2 (new session)

(Agent reread `CLAUDE.md` at the start.)

Person: "log that: the December newsletter had a dead link again, to the gift card page. I expected
all links to work."

> I searched the log. L-1 is the same lesson: same area (marketing), and its rule, "When sending a
> newsletter, do click every link to check it opens the right page before it goes out", would have
> prevented this.
>
> So I propose no new row, only this change:
>
> - L-1: seen 1 to 2.
>
> Add it to the log?

Person: "yes"

> Done. L-1 seen is now 2. No other line changed.
>
> Worth knowing: L-1 is already an accepted rule and it happened again. If it reaches 3, the weekly
> review will flag that the rule is not stopping it.

## Session 3 (new session)

(Agent reread `CLAUDE.md` at the start.)

Person: "log that: our supplier, Brightline Packaging, sent the wrong box size because Sam Okafor at
sam@brightline.example ordered from the old catalogue. I expected the new size."

> I searched the log. The only row, L-1, is about newsletter links in marketing. It would not have
> prevented this, so this is a new row. I replaced the person's name and email with [removed].
>
> | Column | Value |
> | --- | --- |
> | id | L-2 |
> | date | 2026-11-19 (no date given, so I used today) |
> | kind | error |
> | area | operations |
> | project | (empty) |
> | lesson_type | check |
> | rule | When placing a supplier order, do confirm the supplier is using the current catalogue and sizes before they ship. |
> | what_happened | Our supplier, Brightline Packaging, sent the wrong box size because [removed] at [removed] ordered from the old catalogue. |
> | expected | The new box size. |
> | why | Nothing in the ordering process checked which catalogue the order was taken from. |
> | tags | supplier;packaging;ordering;catalogue |
> | severity | (empty) |
> | status | proposed |
> | seen | 1 |
> | source | chat |
> | sensitive | yes (a supplier and a person were named) |
> | confidence | (empty) |
> | review_by | (empty) |
>
> Empty cells: project, severity, confidence and review_by. You didn't name a project, so I left it
> empty; that means the rule applies to all work. If it belongs to `supplier-onboarding`, tell me.
>
> Add it to the log?

Person: "yes"

> Added. `learnings/learnings.csv` now has row L-2, status proposed. No other line changed.

Person: "weekly review"

> **Proposed rows**
>
> - **L-2** (supplier order, current catalogue). Suggestion: **accept**. It is a clear check that
>   would have caught the wrong box size, and no other row covers it.
>
> **Accepted rows seen 3 or more times**
>
> - None. (L-1 is at 2: close. If the newsletter link problem happens once more, it is time to fix
>   the cause, not just repeat the rule.)
>
> I've changed nothing yet. Tell me what to do with L-2.

Person: "accept it"

> Changed: L-2 status proposed to accepted. Nothing else changed. The log now holds two rules.

## Session 4 (new session)

(Agent reread `CLAUDE.md` at the start.)

Person: "before I start: placing the spring order with our packaging supplier"

> Before I start: I read the accepted rules whose project is this work's project or empty. This
> order isn't the newsletter, so L-1 does not apply. One rule applies.
>
> Following: **L-2**. When placing a supplier order, do confirm the supplier is using the current
> catalogue and sizes before they ship.
>
> So when we place the spring order, I'll list each item with its size and ask you to get the
> supplier to confirm, in their reply, that they are working from the current catalogue. What
> items and quantities do you need?
