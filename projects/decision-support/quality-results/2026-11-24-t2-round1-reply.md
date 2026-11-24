**Answer:** Use PostgreSQL, and record the ADR as proposed for now. Before 5 December, close one gap. None of the pages you sent says that PostgreSQL handles two writers at once, or how much work it is for three developers to run it.

You asked me to run straight through, so I did not stop. A database choice is hard to undo, so it got the full seven steps. Where I would have stopped, I list what I assumed.

## Step 1. Define

- **Decision:** Should Shiftboard use SQLite or PostgreSQL, given the Q3 2027 plan for a second app server?
- **Who decides:** you (tech lead) with your engineering manager. **Decision needed by:** 5 December 2026.
- **What good looks like in a year:** Shiftboard saves safely from two app servers, and the three of you spend little time running the database.
- **Limits:** three developers and no database administrator [12]. A second app server on a separate machine in Q3 2027, both servers writing to the same data [11]. Budget: not given.
- **What would change the answer:** (1) the second app server plan is dropped; (2) running PostgreSQL costs more time than the team can give.
- **Can it be undone?** Hard. Changing engines later means migrating live data.

*Assumed here (no stop):* you did not say which database Shiftboard uses today. I treat "do nothing" as keeping today's setup and deciding nearer Q3 2027.

## Step 2. Structure

**Options:** A. PostgreSQL now. B. SQLite now, then switch before the second app server. C. Do nothing: keep today's setup and decide nearer Q3 2027.

**What matters:**
1. Safe concurrent writes once two app servers run on separate machines (**must be met**)
2. Effort to run it with three developers and no DBA
3. Cost of switching later

**Sub-questions:**
- Q1. Can SQLite take writes safely from two app servers on separate machines?
- Q2. Can PostgreSQL?
- Q3. How much effort does each take for three developers with no DBA?
- Q4. What would a later switch cost, and is the Q3 2027 plan firm?

*What is missing?* Today's load on one server is covered under Q1, using your figure of 5 saves a second. Backups, upgrades and hosting cost are part of Q3. You did not list price as a criterion, so I left it out.

*Assumed here (no stop):* these three criteria are the full list, and only the first must be met.

## Step 3. Prioritise

- Q1 guess: no, not once the data sits across a network.
- Q2 guess: yes.
- Q3 guess: PostgreSQL takes more effort than SQLite.
- Q4 guess: a later switch costs more than starting with PostgreSQL. Only you can confirm whether the plan is firm.

**Deciding sub-questions:** Q1, Q2 and Q3. Q4 gets one line: none of your sources covers the cost of switching, and only you can confirm the plan.

## Step 4. Plan the evidence

- **Q1.** *Supports the guess:* SQLite's own pages say it allows one writer at a time, or that use over a network calls for a client/server engine. *Proves it wrong:* SQLite's own pages say several machines can safely write to one database.
- **Q2.** *Supports:* PostgreSQL's own documentation says many clients can write at the same time. *Proves it wrong:* the documentation limits concurrent writers or describes write conflicts.
- **Q3.** *Supports:* any source on the routine work each engine needs, such as backups and upgrades. *Proves it wrong:* a source showing that PostgreSQL needs little routine work from a small team.

## Step 5. Analyse

**Q1, SQLite.**
- SQLite allows only one writer at any instant [2].
- Its own page says that when many processes must write at the same instant and cannot take turns, you should use a client/server engine [3][4].
- When the data is separated from the application by a network, its network page says you generally want a client/server database [5].
- Under your Q3 2027 plan [11], at least one app server reaches the data over a network.
- Result: SQLite fails the must-meet criterion once there are two machines.
- Today, on one server at about 5 saves a second [9][10], the page says SQLite "works great" for most low to medium traffic websites [1]. The page does not define low or medium in saves a second, so whether Shiftboard counts as low traffic is not known.

I looked for the opposite: nothing in the SQLite text you pasted says that several machines can safely write to one database.

**Q2, PostgreSQL.**
- The page says reading never blocks writing [6].
- Result: **Partly.** The page covers readers against writers. It does not cover two writers at once, and it does not say that PostgreSQL is a client/server engine.
- So for PostgreSQL, the must-meet criterion is not yet checked. I had only one PostgreSQL paragraph, so I also could not look for evidence against it.

**Q3, effort to run.** No source covers either engine. Not known.

**Your teammate's claim** that "Postgres is always faster than SQLite" [7]: **No source.** None of the pages compares speed, so I left the claim out.

| | A. PostgreSQL now (recommended) | B. SQLite now, switch before Q3 2027 | C. Do nothing |
| --- | --- | --- | --- |
| Safe concurrent writes, two app servers (must meet) | ⚠ see sources [6] | No: one writer at any instant [2]; over a network, use client/server [5] | not known (today's database not given) |
| Effort to run with three developers, no DBA [12] | not known | not known | not known |
| Cost of switching later | not known | A switch is needed before Q3 2027 [5][11]; cost not known | not known |
| Can it be undone? | Hard: reversing means a data migration | Hard: a migration is built into the plan | Easy now; the choice is only put off |

No sums were needed. None of the sources gives figures to add up.

## Step 6. Synthesise

**Answer:** Use PostgreSQL now, on condition that two checks pass before 5 December.

**Reasons:**
1. SQLite allows one writer at any instant [2]. Its own page says a client/server engine is best when writers cannot take turns [3][4].
2. Your plan puts the data across a network from at least one app server [11]. For that case, SQLite's network page says you generally want a client/server database [5].
3. If you choose SQLite now, the Q3 2027 plan has to include a migration, carried out by three developers with no DBA [12]. The cost of that migration is not known; this reason rests on your plan, not on a sourced cost.

**The evidence against:**
- SQLite "works great" for most low to medium traffic websites [1], and today Shiftboard serves about 40 staff [8] at about 5 saves a second [9] on one server [10]. Until Q3 2027, SQLite may be enough.
- The PostgreSQL page you sent [6] covers readers against writers only. It does not yet show that PostgreSQL meets the must-meet criterion.
- The effort of running PostgreSQL with no DBA is not known. This is the cost the recommendation leaves open.

**Premortem:** see Risks and controls in the record below.

**Confidence:** medium. It would rise if PostgreSQL's own documentation said it handles writes from several clients at once, and if a short trial showed how many hours it takes your team to run.

## Step 7. Recommend

Suggested file: `docs/decisions/0001-use-postgresql-for-shiftboard.md`. If you already keep records, change the number to the next free one.

```markdown
# 0001. Use PostgreSQL for Shiftboard's database

- Status: proposed
- Date: 2026-11-24
- Deciders: tech lead and engineering manager (decision needed by 2026-12-05)
- Can it be undone: hard; reversing means migrating live data to another engine

## Context and problem
Shiftboard, our internal shift-scheduling web app, runs on one server [10]. About 40 staff
use it [8], with about 5 saves a second at the busiest time, our estimate from last month's
logs [9]. In Q3 2027 we plan a second app server on a separate machine behind a load
balancer, both writing to the same data [11]. We are three developers with no database
administrator [12]. SQLite allows one writer at any instant [2]. Its documentation says to
use a client/server engine when many processes must write at the same instant and cannot
take turns [3][4], and generally when the data is separated from the application by a
network [5]. PostgreSQL's documentation says reading never blocks writing [6]. A claim that
PostgreSQL is always faster than SQLite has no source and played no part in this decision [7].

## Decision drivers
- Safe concurrent writes once two app servers run on separate machines (must be met)
- Effort to run it with three developers and no DBA
- Cost of switching later

## Options considered
1. PostgreSQL now
2. SQLite now, then switch to a client/server engine before the second app server
3. Keep what we have and decide nearer Q3 2027 (today's database not recorded here)

## Decision
We will use PostgreSQL for Shiftboard. We will accept this record by 2026-12-05 if two
checks pass: PostgreSQL's own documentation confirms that it handles writes from several
clients at once, and a timeboxed trial shows that we can run it.

## Consequences
- Good: SQLite's own pages point setups with several writers, or data across a network, to a
  client/server engine [3][4][5], and our Q3 2027 plan is such a setup [11].
- Good: reading never blocks writing [6].
- Bad: the effort for three developers with no DBA to run PostgreSQL is not known [12].
- Bad: the must-meet driver is not yet confirmed in PostgreSQL's own words. Source [6]
  covers readers against writers only.
- Evidence against: SQLite "works great" for most low to medium traffic websites [1], and
  today's load is about 5 saves a second on one server [9][10]. If the Q3 2027 plan is
  dropped, SQLite may have been enough.

## Risks and controls
| Risk | Control | How we will know |
| --- | --- | --- |
| Running PostgreSQL takes more developer time than planned [12] | Before accepting, run a timeboxed trial of setup, backup, restore and upgrade on a test machine, and log the hours | The hours in the trial log; after that, the time spent on database work each month |
| The second app server is dropped or delayed, so the extra effort buys nothing [11] | Confirm the plan with the engineering manager before accepting; revisit this record if the plan changes | Roadmap review |
| Two people edit the same shift through different app servers, and one edit silently replaces the other | Test two app servers saving the same shift in staging before Q3 2027 | No lost edits in the staging test |
| Moving today's data into PostgreSQL loses or changes records | Rehearse the move on a copy; compare row counts and a sample of records | Counts and samples match before go-live |
| The unsourced "always faster" claim [7] sets the wrong expectations | Measure save times at the busiest hour before and after the move | The before and after save times |

## Confirmation
By 2026-12-05: finish the documentation check and the trial above. Then set the status to
accepted, or record why not. Before the second app server goes live in Q3 2027: run both app
servers in staging at the busiest rate seen so far, about 5 saves a second [9], and check
that no save fails or is lost. Look at this record again when the second app server goes
live, or if the Q3 2027 plan changes.

## Sources
| # | The exact words | Source and link | Checked | Result |
| --- | --- | --- | --- | --- |
| 1 | "SQLite works great as the database engine for most low to medium traffic websites (which is to say, most websites)." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 2026-11-24, pasted text | Checked. The page does not define "low to medium" in saves a second |
| 2 | "SQLite supports an unlimited number of simultaneous readers, but it will only allow one writer at any instant in time." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 2026-11-24, pasted text | Checked |
| 3 | "If many threads and/or processes need to write the database at the same instant (and they cannot queue up and take turns)" | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 2026-11-24, pasted text | Checked (first half of the sentence) |
| 4 | "it is best to select a database engine that supports that capability, which always means a client/server database engine." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 2026-11-24, pasted text | Checked (second half of the same sentence) |
| 5 | "Generally, if your data is separated from the application by a network, you want to use a client/server database." | SQLite Over a Network, Caveats and Considerations, https://sqlite.org/useovernet.html | 2026-11-24, pasted text | Checked |
| 6 | "in MVCC locks acquired for querying (reading) data do not conflict with locks acquired for writing data, and so reading never blocks writing and writing never blocks reading." | PostgreSQL 18 documentation, 13.1 Introduction, https://www.postgresql.org/docs/18/mvcc-intro.html | 2026-11-24, pasted text | Partly. Covers readers against writers, not two writers at once, and does not say PostgreSQL is client/server |
| 7 | "Postgres is always faster than SQLite." | A teammate, no link | n/a | No source |
| 8 | "about 40 staff use it" | Our figures (tech lead) | n/a | Our figures |
| 9 | "at the busiest time, about 5 saves a second (our estimate from last month's logs)" | Our figures (tech lead) | n/a | Our figures, estimated from logs |
| 10 | "Today it runs on one server." | Our figures (tech lead) | n/a | Our figures |
| 11 | "In the plan for Q3 2027, we add a second app server on a separate machine behind a load balancer, both writing to the same data." | Our figures (tech lead) | n/a | Our figures (a plan, not yet done) |
| 12 | "we are three developers, no database administrator" | Our figures (tech lead) | n/a | Our figures |
```

**Not known:** the effort to run PostgreSQL with your team, the cost of a later switch, and which database Shiftboard uses today. To close the first, read PostgreSQL's own documentation on concurrent writes from several clients, and time the trial described above.

**Before you commit:** I checked every quote against the text you pasted, not against the live pages. Open two of the links and find the quoted words with Ctrl+F (Cmd+F on a Mac). Fix or remove anything marked ⚠. This recommends; you and your engineering manager decide.
