You asked for no stops, so I ran all seven steps straight through. I note what I assumed at each point where I would normally stop. The record you can commit is at the end.

## Step 1. Define

- **The decision:** Which database should Shiftboard use, SQLite or PostgreSQL, given the plan to add a second app server in Q3 2027?
- **Who decides:** you (tech lead) with your engineering manager.
- **Decision needed by:** 5 December 2026.
- **What good looks like in a year:** two app servers both save shifts safely, and three developers can run the database without a database administrator.
- **Limits:** three developers and no database administrator [8]. The second app server arrives in Q3 2027 [7].
- **What would change the answer:** (1) whether the second app server on its own machine really goes ahead; (2) whether the PostgreSQL documentation confirms that two machines can write at the same time, and whether three developers can run it.
- **Can it be undone?** Hard. A database choice means moving the data and changing the app's database code to reverse it (my reasoning, not from a source).

*Assumed at this stop:* you did not say which database Shiftboard uses today, so I treat it as not known.

## Step 2. Structure

**Options:** A. PostgreSQL. B. SQLite. C. Do nothing: keep the current setup and decide closer to Q3 2027.

**What matters:**
1. Safe concurrent writes once there are two app servers. **Must be met.**
2. Effort to run it with three developers and no database administrator.
3. Cost of switching later.
4. Fit for today's load: one server, about 5 saves a second at the busiest time. I added this from your figures; it is not a must-have.

**Sub-questions:**
1. Can each option take writes from two app servers on separate machines safely?
2. Does each option handle today's load on one server?
3. How much effort does each option take to run with three developers?
4. If we choose SQLite now, will we have to switch at Q3 2027?

*What is missing?* Backups and recovery, and which database runs today. You sent no evidence on either, so I list them under "Not known" instead of scoring them.

*Assumed at this stop:* the four sub-questions above, and "do nothing" as defined above.

## Step 3. Prioritise

Best guesses, labelled as guesses:
1. Guess: SQLite is a poor fit for two machines writing; PostgreSQL fits. **Deciding.**
2. Guess: both handle today's load. Not deciding, because the must-have is about Q3 2027.
3. Guess: PostgreSQL takes more effort to run. **Deciding.**
4. Guess: yes, SQLite now likely means a switch later. Follows from 1.

## Step 4. Plan the evidence

- **Sub-question 1.** Support: SQLite's own pages point to a client/server database for many writers or data across a network, and PostgreSQL's pages confirm concurrent writes. Prove wrong: a SQLite page saying writes from separate machines are fine, or a PostgreSQL page silent on concurrent writes.
- **Sub-question 3.** Support: a source on PostgreSQL's operating tasks. Prove wrong: a source showing it needs little running for a small team.

## Step 5. Analyse

I could not open the links in this chat. I read the text you pasted, copied 24 November 2026.

| # | Fact | Result |
| --- | --- | --- |
| 1 | SQLite works for most low to medium traffic websites | Checked (pasted text). The page does not say whether 5 saves a second counts as low |
| 2 | SQLite allows one writer at any instant | Checked (pasted text) |
| 3 | Many writers at the same instant point to a client/server engine, **only when they cannot queue up and take turns** | Checked (pasted text). Whether your saves can take turns is not known |
| 4 | Data separated from the app by a network **generally** points to a client/server database | Checked (pasted text). A hedge, not a ban |
| 5 | Under MVCC, reading never blocks writing and writing never blocks reading | Checked (pasted text), from PostgreSQL's own documentation. It says nothing about two writers at once, or about writes from two machines |
| 6, 7, 8 | Your load, servers, plan and team | Their figures |
| 9 | "Postgres is always faster than SQLite" | ⚠ No source. A teammate's claim with no page. Not used. Speed is not one of your criteria |

What the pasted pages do not say: that PostgreSQL is a client/server database, or that it accepts writes from two machines at once. So the must-have is **not confirmed** for PostgreSQL. No source covers running effort for either database. No sums were needed.

## Step 6. Synthesise

- **Answer:** Choose PostgreSQL, on condition that its documentation confirms concurrent writes from separate machines and the running effort fits three developers.
- **Reasons:** (1) The second app server on a separate machine puts the data across a network from at least one app [7], and SQLite's own page says that generally calls for a client/server database [4]. (2) SQLite allows one writer at any instant [2]. Its own page points to a client/server engine when writers cannot take turns [3]; whether yours can is not known. (3) In PostgreSQL's MVCC model, reads and writes do not block each other [5]. This covers reads against writes only, not two writers.
- **Evidence against, strongest first:** SQLite's page says it works for most low to medium traffic websites [1], and today you run one server [7]. Nothing you sent says SQLite fails at 5 saves a second [6]. Sources [3] and [4] are hedged ("cannot queue up and take turns", "Generally"), not absolute. No source shows PostgreSQL's running effort is manageable with no database administrator [8].
- **Premortem:** see Risks and controls in the record.
- **Confidence: low.** The must-have is not confirmed for PostgreSQL from the pages you sent. To raise it, find and quote a PostgreSQL documentation passage confirming that several clients on separate machines can write at the same time.

## Step 7. The decision record

Suggested path: `docs/decisions/0001-use-postgresql-for-shiftboard.md`

```markdown
# 0001. Use PostgreSQL for Shiftboard

- Question: Which database should Shiftboard use, SQLite or PostgreSQL, given the plan to add a second app server in Q3 2027?
- Status: proposed
- Date: 2026-11-24
- Decision needed by: 2026-12-05
- Deciders: tech lead; engineering manager
- Can it be undone: hard. Reversing means moving the data and changing the app's database code; cost not known
- Decision in brief: we will use PostgreSQL, if its documentation confirms concurrent writes from separate machines, because the Q3 2027 plan puts the data across a network from one app server [7] and SQLite's page says that generally calls for a client/server database [4]; SQLite allows one writer at any instant [2]; and in PostgreSQL's MVCC, reads and writes do not block each other [5] (reads against writes only)
- What would change this: the Q3 2027 second server is dropped, or the PostgreSQL documentation does not confirm concurrent writes from two machines, or running it is beyond three developers

## Context and problem
Shiftboard is an internal shift-scheduling web app used by about 40 staff, with about 5 saves a second at the busiest time [6]. It runs on one server today. The Q3 2027 plan adds a second app server on a separate machine behind a load balancer, both writing to the same data [7]. We are three developers with no database administrator [8]. SQLite's own pages say it works for most low to medium traffic websites [1], allows one writer at any instant [2], and generally calls for a client/server database when data is across a network [4]. Which database Shiftboard uses today is not recorded here.

## Decision drivers
- Safe concurrent writes once there are two app servers (must be met)
- Effort to run with three developers and no database administrator
- Cost of switching later
- Fit for today's load (one server, about 5 saves a second)

## Options considered
| Driver | PostgreSQL | SQLite | Do nothing (decide nearer Q3 2027) |
| --- | --- | --- | --- |
| Safe writes, two servers (must) | ⚠ not known: reads and writes do not block each other [5]; two writers not covered | Generally not advised across a network [4]; one writer at any instant [2] | ⚠ not known (current database not given) |
| Effort to run | not known | not known | not known |
| Cost of switching later | not known | ⚠ see sources: [4] points to a switch if the Q3 2027 plan holds | not known |
| Today's load | not known | "most low to medium traffic websites" [1]; whether 5 saves/s counts is not known | not known |
| Can it be undone? | hard | hard | easy now; the decision returns before Q3 2027 |

## Decision
We will use PostgreSQL for Shiftboard, once a PostgreSQL documentation passage confirming concurrent writes from separate machines is added to the Sources. If no option is confirmed for the must-have by 5 December 2026, we keep the current setup and do not add the second app server until one is.

## Consequences
- Good: matches SQLite's own advice for data across a network [4]; reads and writes do not block each other [5].
- Bad: running effort with no database administrator is not known [8]; we take on a data move before Q3 2027.
- Evidence against: SQLite's page says it suits most low to medium traffic websites [1] and we run one server today [7]; [3] and [4] are hedged, not absolute.

## Risks and controls
| Risk | Control | How we will know | Owner |
| --- | --- | --- | --- |
| Running PostgreSQL takes more time than three developers have | List backup, upgrade and monitoring tasks and estimate hours before accepting | Estimate is over our capacity | Developer (proposed) |
| Data is lost or changed in the move | Trial the move on a copy and compare record counts | Counts differ | Developer (proposed) |
| The second server plan is dropped, so the switch was not needed | Confirm the Q3 2027 plan before accepting | Plan changes | Engineering manager |
| Two app servers still clash on the same shift | Test two app servers in staging at peak rate before Q3 2027 | Failed or lost saves in the test | Tech lead |
| Busy-time load is higher than our estimate [6] | Measure peak saves a second from logs | Peak above 5 saves a second | Developer (proposed) |

## Confirmation
Before Q3 2027, the tech lead runs two app servers in staging at 5 saves a second and above, and checks for failed or lost saves. We look at this record again one month after the second server goes live.

## Not known
- Whether PostgreSQL accepts writes from two machines at once: find and quote it in PostgreSQL's own documentation.
- The running effort for each database with no database administrator: list the tasks and estimate the hours.
- Which database Shiftboard uses today, and how backups and recovery work: check the current setup.
- Whether your saves can "queue up and take turns" [3]: look at last month's logs for clashes at peak.

## Next steps
1. Find and quote the PostgreSQL passage on concurrent writes from separate machines. Tech lead, 28 Nov 2026 (proposed).
2. Confirm the Q3 2027 second server plan and record the current database. Engineering manager, 28 Nov 2026 (proposed).
3. Estimate the running effort for PostgreSQL. Developer (proposed), 2 Dec 2026 (proposed).
4. Decide and set Status to accepted or rejected. Tech lead and engineering manager, 5 Dec 2026.
5. Trial the data move on a copy. Developer (proposed), 31 Mar 2027 (proposed).

## Sources
I could not open the links. Every Checked result below comes from the text you pasted, copied 24 November 2026.

| # | The exact words | Source and link | Checked | Result |
| --- | --- | --- | --- | --- |
| 1 | "SQLite works great as the database engine for most low to medium traffic websites (which is to say, most websites)." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 24 Nov 2026 | Checked (pasted text) |
| 2 | "SQLite supports an unlimited number of simultaneous readers, but it will only allow one writer at any instant in time." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 24 Nov 2026 | Checked (pasted text) |
| 3 | "...processes need to write the database at the same instant (and they cannot queue up and take turns) then it is best to select ... a client/server database engine." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 24 Nov 2026 | Checked (pasted text) |
| 4 | "Generally, if your data is separated from the application by a network, you want to use a client/server database." | SQLite Over a Network, Caveats and Considerations, https://sqlite.org/useovernet.html | 24 Nov 2026 | Checked (pasted text) |
| 5 | "...in MVCC locks acquired for querying (reading) data do not conflict with locks acquired for writing data, and so reading never blocks writing and writing never blocks reading." | PostgreSQL 18 documentation, 13.1 Introduction, https://www.postgresql.org/docs/18/mvcc-intro.html | 24 Nov 2026 | Checked (pasted text) |
| 6 | About 40 staff; about 5 saves a second at the busiest time | You, estimated from last month's logs | 24 Nov 2026 | Their figures |
| 7 | One server today; Q3 2027 plan: a second app server on a separate machine behind a load balancer, both writing to the same data | You | 24 Nov 2026 | Their figures |
| 8 | Three developers, no database administrator | You | 24 Nov 2026 | Their figures |
| 9 | "Postgres is always faster than SQLite." | A teammate, no page cited | 24 Nov 2026 | ⚠ No source |
```

**Before you send:** Open two of the links above and find the quoted words with Ctrl+F (Cmd+F on a Mac). Fix or remove anything marked ⚠. This recommends; you decide.
