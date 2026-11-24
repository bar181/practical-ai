**Answer:** Choose PostgreSQL now. Record it as *proposed*, not accepted. None of the pages you sent confirm that PostgreSQL handles two writers on separate machines, so confidence is low until you paste a PostgreSQL page that does.

You asked me to run straight through, so I did not stop. I list what I assumed at each stop. I cannot open web pages in this chat, so every source below is the text you pasted, not a page I opened.

## Step 1. Define

- **The decision:** Which database should Shiftboard use, SQLite or PostgreSQL, given the plan for a second app server in Q3 2027?
- **Who decides:** you (tech lead) with your engineering manager. **Decision needed by:** 5 December 2026.
- **What good looks like in a year:** both app servers save shifts safely to the same data, and three developers with no database administrator can run it.
- **Limits:** three developers, no database administrator [9]. The second app server is planned for Q3 2027 [8].
- **What would change the answer:** (1) the second app server plan is dropped, so all writes stay on one machine; (2) PostgreSQL's own documentation does not confirm safe writes from several machines, or running it proves too much work for three people.
- **Can it be undone?** Hard. Moving a live app's data from one database to another means a migration, and its cost is not known.

*Assumed at this stop:* "safe concurrent writes once there are two app servers" is the must-have. It applies from Q3 2027, not today.

## Step 2. Structure

**Options**
1. PostgreSQL now.
2. SQLite, and keep it after the second server arrives.
3. SQLite now, then switch to PostgreSQL before Q3 2027.
4. Keep what we have. You did not say which database Shiftboard uses today, so I cannot tell whether this is the same as option 1 or 2.

**What matters**
- Safe concurrent writes with two app servers on separate machines (**must be met**).
- Effort to run it with three developers and no database administrator.
- Cost of switching later.

**The question broken down**
- A. Can SQLite safely take writes from two app servers on separate machines?
- B. Can PostgreSQL safely take writes from two app servers at the same time?
- C. Can three developers with no database administrator run PostgreSQL?
- D. What does a switch cost, now or later?

What is missing? Speed. Your teammate's claim is about speed, but speed is not one of your criteria, so I checked the claim and did not score it. Whether the Q3 2027 plan is firm is covered under "what would change the answer".

*Assumed at this stop:* I added option 3 because it trades a switch later for less to run now.

## Step 3. Prioritise

- A. Guess: no, generally not. **Deciding.**
- B. Guess: yes. **Deciding.**
- C. Guess: yes, with effort that is not known. **Deciding.**
- D. Guess: switching later costs more than choosing now. One line only, because no source covers cost.

## Step 4. Plan the evidence

- **A.** For the guess: SQLite's own pages limit it to one writer, or point to client/server for data reached over a network. Against: SQLite's pages say it is fine at low traffic, or fine when writes can take turns.
- **B.** For the guess: PostgreSQL's own page says two clients can write at the same time safely. Against: a PostgreSQL page showing that concurrent writers block each other or fail in ways the app must handle.
- **C.** For the guess: a source on the routine work of running PostgreSQL that three developers can cover. Against: a source showing that work needs a specialist. You sent nothing on this, and I cannot search, so C stays open.

## Step 5. Analyse

| # | Result | What it means here |
| --- | --- | --- |
| 1 | Checked (pasted text) | SQLite "works great" for "most low to medium traffic websites". Your excerpt does not define low traffic. |
| 2 | Checked (pasted text) | SQLite allows one writer at any instant. |
| 3 | Checked (pasted text) | This holds only if writers "cannot queue up and take turns". |
| 4 | Checked (pasted text) | In the case in [3], the right engine "always means" client/server. The page does not name PostgreSQL. |
| 5 | Checked (pasted text) | "Generally", data across a network calls for client/server. This is a hedge, not a rule. |
| 6 | Checked (pasted text) | In PostgreSQL, reads and writes do not block each other. This says nothing about two writers. |
| 7 | Their figures | About 40 staff and about 5 saves a second at peak. This is your estimate from last month's logs. |
| 8 | Their figures | One server today. A second app server on a separate machine in Q3 2027, both writing to the same data. |
| 9 | Their figures | Three developers, no database administrator. |
| 10 | ⚠ No source | "Postgres is always faster than SQLite." This is your teammate's opinion. Nothing you sent supports it. |

From [8]: with two machines writing the same data, the data must sit across a network from at least one of them. That brings [5] into play.

The options table is under "Options considered" in the record below. There are no totals, so there are no sums.

**Not known**
- Whether PostgreSQL safely takes concurrent writes from several machines. This is the must-have, and no source covers it.
- The effort to run either database with your team.
- Which database Shiftboard uses today, and so the cost of any switch.
- Whether writes at 5 a second can "queue up and take turns" [3]. This depends on how long each save holds the lock, which is not known.

## Step 6. Synthesise

- **Answer:** PostgreSQL now, proposed until the must-have is confirmed.
- **Reasons and evidence against:** these are in the record below, stated once.
- **Premortem:** see "Risks and controls" below.
- **Confidence: low.** The must-have is not confirmed for PostgreSQL by any source you sent. To raise it, paste a page from PostgreSQL's own documentation that says what happens when two clients write at the same time.

## Step 7. Recommend

Suggested file: `docs/decisions/0001-use-postgresql-for-shiftboard.md`. Renumber it if you already keep records.

```markdown
# 0001. Use PostgreSQL for Shiftboard

- Question: Which database should Shiftboard use, SQLite or PostgreSQL, given a second app server in Q3 2027?
- Status: proposed
- Date: 24 November 2026
- Decision needed by: 5 December 2026
- Deciders: tech lead, engineering manager
- Can it be undone: hard; reversing means migrating live data, cost not known
- Decision in brief: we will use PostgreSQL, because (1) SQLite allows one writer at any instant [2], and client/server is "always" the answer only when writers cannot take turns [3][4], which at 5 saves a second [7] is not known; (2) with two machines, the data is across a network from one of them, and SQLite says that "generally" calls for client/server [5][8]; (3) choosing now avoids a second move before Q3 2027 [8]; this rests on your plan alone, and no source gives the cost. The case rests on SQLite's own pages. No PostgreSQL page confirms concurrent writes.
- What would change this: the Q3 2027 second server is dropped, so all writes stay on one machine [8]; or PostgreSQL's own documentation does not confirm safe concurrent writes, or running it is too much for three developers [9].

## Context and problem
Shiftboard is an internal shift-scheduling web app. It has about 40 staff and about 5 saves a second at peak, which is our estimate from last month's logs [7]. It runs on one server today. In Q3 2027 a second app server on a separate machine will write to the same data [8]. SQLite allows one writer at any instant [2]. SQLite's pages point to a client/server engine when writers cannot take turns [3][4], and "generally" when data is across a network [5]. PostgreSQL's documentation says reads and writes do not block each other [6]. We are three developers with no database administrator [9].

## Decision drivers
- Safe concurrent writes once there are two app servers (must be met)
- Effort to run it with three developers and no database administrator
- Cost of switching later

## Options considered
| Driver | PostgreSQL now (recommended) | SQLite, kept after Q3 2027 | SQLite now, switch before Q3 2027 | Keep what we have |
| --- | --- | --- | --- | --- |
| Safe concurrent writes, two app servers (must) | ⚠ not known; reads and writes do not block each other [6], two writers not covered | fails, generally: one writer at any instant [2], data across a network [5][8] | ⚠ not known after the switch, as for PostgreSQL | ⚠ not known; current database not given |
| Effort to run (3 developers, no DBA [9]) | not known | not known | not known | not known |
| Cost of switching later | no switch needed for the Q3 2027 plan [8]; cost of moving now not known | not known | one move before Q3 2027 [8]; cost not known | not known |
| Can it be undone? | hard; cost not known | hard; cost not known | hard; cost not known | hard; cost not known |

## Decision
We will use PostgreSQL for Shiftboard, subject to confirming safe concurrent writes from PostgreSQL's own documentation before 5 December 2026.

## Consequences
- Good: reads never block writes and writes never block reads [6]. No database move is needed when the second app server arrives [8].
- Bad: a database server to run with three developers and no administrator [9]. The effort is not known.
- Evidence against: (1) SQLite "works great" for "most low to medium traffic websites" [1], and Shiftboard may be low traffic [7], though the excerpt does not define it. (2) Client/server is needed only if writers "cannot queue up and take turns" [3]; at about 5 saves a second [7], they might be able to. (3) The network point is "generally", not always [5]. Your teammate's speed claim is not evidence either way [10].

## Risks and controls
| Risk | Control | How we will know | Owner |
| --- | --- | --- | --- |
| PostgreSQL does not handle two writers to the same rows the way the app expects | Paste PostgreSQL's own page on concurrent writes; test two app instances saving the same shift at once | Test shows no lost or failed saves | Tech lead |
| Running PostgreSQL costs three developers more time than planned | List backup, upgrade and monitoring tasks and estimate hours before deciding | Estimate fits the team's time | Tech lead |
| The Q3 2027 second server is dropped, so the extra running work buys nothing | Confirm the plan is funded and dated | Plan confirmed in writing | Engineering manager |
| Moving from today's database loses or corrupts data | Confirm today's database; rehearse the move on a copy | Row counts match after the rehearsal | Tech lead (proposed) |
| Peak writes are higher than the 5 a second estimate | Measure peak saves from logs over a busier period | Measured peak recorded | Developer (proposed) |

## Confirmation
Before deciding (dates proposed, working back from 5 December 2026):
1. Tech lead: confirm which database Shiftboard uses today, by 26 November 2026.
2. Tech lead: paste PostgreSQL's own page on concurrent writes and update this record, by 28 November 2026.
3. Tech lead: estimate the hours of running work, by 2 December 2026.
4. Engineering manager: confirm the Q3 2027 plan, by 3 December 2026.
5. Tech lead and engineering manager: accept or reject this record, by 5 December 2026.

After deciding: before the second server goes live in Q3 2027, the tech lead runs both app servers in a test environment at or above the measured peak write rate and checks for zero failed saves. We will look at this record again three months after the second server goes live (proposed).

## Sources
I could not open the links. Every source is text you pasted, copied 24 November 2026.

| # | The exact words | Source and link | Checked | Result |
| --- | --- | --- | --- | --- |
| 1 | "SQLite works great as the database engine for most low to medium traffic websites (which is to say, most websites)." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 24 Nov 2026 | Checked (pasted text) |
| 2 | "SQLite supports an unlimited number of simultaneous readers, but it will only allow one writer at any instant in time." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 24 Nov 2026 | Checked (pasted text) |
| 3 | "If many threads and/or processes need to write the database at the same instant (and they cannot queue up and take turns) then it is best to select..." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 24 Nov 2026 | Checked (pasted text) |
| 4 | "...it is best to select a database engine that supports that capability, which always means a client/server database engine." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 24 Nov 2026 | Checked (pasted text) |
| 5 | "Generally, if your data is separated from the application by a network, you want to use a client/server database." | SQLite Over a Network, Caveats and Considerations, https://sqlite.org/useovernet.html | 24 Nov 2026 | Checked (pasted text) |
| 6 | "...in MVCC locks acquired for querying (reading) data do not conflict with locks acquired for writing data, and so reading never blocks writing and writing never blocks reading." | PostgreSQL 18 documentation, 13.1 Introduction, https://www.postgresql.org/docs/18/mvcc-intro.html | 24 Nov 2026 | Checked (pasted text) |
| 7 | "about 40 staff use it; at the busiest time, about 5 saves a second (our estimate from last month's logs)" | Your message | 24 Nov 2026 | Their figures (estimate from logs) |
| 8 | "Today it runs on one server." ... "we add a second app server on a separate machine behind a load balancer, both writing to the same data." | Your message (Q3 2027 plan) | 24 Nov 2026 | Their figures (team plan) |
| 9 | "we are three developers, no database administrator" | Your message | 24 Nov 2026 | Their figures |
| 10 | "Postgres is always faster than SQLite." | A teammate, quoted in your message (opinion) | 24 Nov 2026 | ⚠ No source |
```

**Before you send:** Open two of the links above and find the quoted words with Ctrl+F (Cmd+F on a Mac). Fix or remove anything marked ⚠. This recommends; you decide.
