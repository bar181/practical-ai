**Answer first:** use PostgreSQL for Shiftboard and set it up before the second app server arrives in Q3 2027. Confidence is **low**. The text you sent shows that SQLite does not fit your Q3 2027 plan. It does not yet show that PostgreSQL meets your must-have of safe writes from two machines. One page of PostgreSQL's own documentation would settle that (see Not known).

You asked me to run straight through, so I did not stop for corrections. I note what I assumed at each stop below. This is a database choice, so it is hard to undo and I ran the full seven steps.

## Step 1. Define

- **The decision:** Should Shiftboard use SQLite or PostgreSQL, given the plan for two app servers in Q3 2027?
- **Who decides:** you (tech lead) with your engineering manager. **Decision needed by:** 5 December 2026.
- **What good looks like in a year:** Shiftboard runs on two app servers without lost or blocked saves, and three developers can run it without a database administrator.
- **Limits:** three developers, no database administrator. The Q3 2027 plan has two app servers on separate machines, both writing to the same data.
- **What would change the answer:** (1) the Q3 2027 plan changes to one app server, or (2) PostgreSQL turns out to need more running effort than three developers can give.
- **Can it be undone?** Hard. Changing the database later means moving the data, and that cost is not known.

*Assumed at this stop:* you did not say which database Shiftboard uses today. I treat "keep what we have" as its own option and mark its values "not known".

## Step 2. Structure

**Options**
1. PostgreSQL now.
2. SQLite now, then switch before Q3 2027.
3. Keep what we have and decide later (the current database was not given).

**What matters**
- Safe concurrent writes once there are two app servers (**must be met**).
- Effort to run it with three developers and no database administrator.
- Cost of switching later.

**The question broken down**
- A. Can SQLite take safe writes from two app servers on separate machines?
- B. Does PostgreSQL meet that must-have?
- C. What effort does each need from three developers with no database administrator?
- D. What does switching later cost?

*What is missing?* Speed. Your teammate raised it, but it is not one of your criteria and none of your pages mention it, so I left it out of the comparison. I also did not consider changing the Q3 2027 plan, because I took it as a limit.

*Assumed at this stop:* these three options and criteria are complete, and the two-server plan stands.

## Step 3. Prioritise

- A. Guess: no, not across a network.
- B. Guess: yes.
- C. Guess: PostgreSQL needs more running effort than SQLite, but how much is not known.
- D. Guess: cheaper to switch before the data grows (gets a line, not research).

**Deciding sub-questions:** A, B and C.

## Step 4. Plan the evidence

- **A.** *Supports the guess:* SQLite's own pages say writes are limited, or that networked data calls for a client/server database. *Proves it wrong:* SQLite's pages say it handles writers on separate machines safely.
- **B.** *Supports:* PostgreSQL's own documentation says many writers can work at once from separate clients. *Proves it wrong:* that documentation says writers block or conflict in a way that breaks safe saves.
- **C.** *Supports:* a source that describes the running tasks for each. *Proves it wrong:* a source showing PostgreSQL needs no more running work than SQLite. I found nothing either way in what you sent.

## Step 5. Analyse

| # | Fact | Result |
| --- | --- | --- |
| 1 | SQLite "works great" for most low to medium traffic websites | Checked. The page does not define low or medium traffic, so whether Shiftboard counts is not known |
| 2 | SQLite allows one writer at any instant | Checked |
| 3 | When processes write at the same instant and cannot take turns, SQLite's page points to a client/server engine | Checked. This applies only when writers "cannot queue up and take turns". At about 5 saves a second [8], whether yours can take turns is not known |
| 4 | When data is separated from the application by a network, you generally want a client/server database | Checked. It says "Generally". In Q3 2027 at least one app server is on a separate machine from the data [9] |
| 5 | In PostgreSQL, reading never blocks writing and writing never blocks reading | Checked. This covers readers against writers, not two writers against each other |
| 6 | "Postgres is always faster than SQLite" | ⚠ No source. A teammate's opinion, and none of the three pages mention speed |
| 7-10 | About 40 staff; about 5 saves a second at peak; one server today, two in Q3 2027; three developers, no database administrator | Their figures, from you |

**Option 2 against the must-have:** in Q3 2027 the data would sit across a network from at least one app server [9]. SQLite's own page says that case generally calls for a client/server database [4]. SQLite also takes one writer at a time [2]. So Option 2 needs a second switch before Q3 2027.

**Option 1 against the must-have:** [5] shows reads and writes do not block each other. It does not cover two writers on separate machines, so this is **not known** until you read more of PostgreSQL's documentation.

No sums were needed.

## Step 6. Synthesise

- **The answer:** PostgreSQL now.
- **Reasons:**
  1. The Q3 2027 plan puts the data across a network from at least one app server, which generally calls for a client/server database [4][9].
  2. SQLite allows one writer at any instant and points to a client/server engine when writers cannot take turns [2][3]. Whether your writers can take turns at about 5 saves a second [8] is not known.
  3. Choosing now avoids a planned second switch before Q3 2027 [4][9]. The cost of either switch is not known, and the pages you sent do not confirm that PostgreSQL meets the must-have ([5] covers reads against writes only).
- **The evidence against:**
  1. The must-have is not confirmed for PostgreSQL in your sources [5].
  2. SQLite "works great" for most low to medium traffic websites [1], and today you run on one server [9], so SQLite may serve well until Q3 2027.
  3. The running effort for three developers with no database administrator [10] is not known for either option.
- **Premortem:** see Risks and controls in the record below.
- **Confidence:** low, because the must-have is not confirmed for PostgreSQL. **What would raise it:** PostgreSQL's own documentation on concurrent writes (the rest of the chapter that page 3 belongs to), added as a source.

## Step 7. Recommend: the decision record

Suggested file: `docs/decisions/0001-use-postgresql-for-shiftboard.md`. Change the number if you already keep records.

```markdown
# 0001. Use PostgreSQL for Shiftboard

- Status: proposed
- Date: 2026-11-24
- Deciders: tech lead and engineering manager (names not given)
- Can it be undone: hard. Reversing means moving the data to another database; the cost is not known
- Decision in brief: we will use PostgreSQL before the second app server in Q3 2027, because
  (1) the planned setup puts data across a network, which generally calls for a client/server
  database [4][9]; (2) SQLite allows one writer at any instant [2][3]; (3) choosing now avoids a
  second switch before Q3 2027 [4][9] (switching cost not known; must-have not yet confirmed for
  PostgreSQL, see Sources [5])
- What would change this: the Q3 2027 plan drops the second app server, or PostgreSQL's running
  effort proves too much for three developers with no database administrator

## Context and problem
Shiftboard is an internal shift-scheduling web app used by about 40 staff [7]. At peak it takes
about 5 saves a second, a team estimate from last month's logs [8]. It runs on one server today.
The plan for Q3 2027 adds a second app server on a separate machine behind a load balancer, both
writing to the same data [9]. SQLite allows one writer at any instant [2], and its own pages
generally advise a client/server database when data is separated from the application by a network
[4]. The team is three developers with no database administrator [10].

## Decision drivers
- Safe concurrent writes once there are two app servers (must be met)
- Effort to run it with three developers and no database administrator [10]
- Cost of switching later

## Options considered
| Driver | PostgreSQL now (chosen) | SQLite now, switch before Q3 2027 | Keep what we have, decide later |
| --- | --- | --- | --- |
| Safe concurrent writes, two app servers (must) | not known: reads never block writes [5]; two writers on separate machines not covered | Against: one writer at any instant [2]; data across a network generally calls for client/server [4] | not known (current database not given) |
| Effort to run, 3 developers, no DBA | not known | not known | not known |
| Cost of switching later | not known (one switch, if not already on PostgreSQL) | not known (a second switch needed before Q3 2027 [4][9]) | not known |
| Can it be undone? | Hard: data move, cost not known | Hard: data move, cost not known | Hard once chosen; deferring past 5 Dec 2026 misses your decision date |

No totals in this table, so no working.

## Decision
We will use PostgreSQL for Shiftboard and run it in production before the second app server goes
live in Q3 2027. Status stays "proposed" until step 1 of Confirmation is done.

## Consequences
- Good: matches SQLite's own advice for data separated from the application by a network [4];
  reading never blocks writing in PostgreSQL [5].
- Bad: running effort for three developers with no database administrator [10] is not known; a
  data move from the current database (not given) is needed if it is not PostgreSQL.
- Evidence against: (1) the must-have is not confirmed for PostgreSQL in our sources; [5] covers
  reads against writes only. (2) SQLite "works great" for most low to medium traffic websites [1],
  and we run on one server today [9]. (3) Running effort is not known for either option.

## Risks and controls
| Risk | Control | How we will know | Owner |
| --- | --- | --- | --- |
| PostgreSQL does not handle two writers on separate machines as we assume | Read PostgreSQL's own documentation on concurrent writes and add it to Sources before accepting | A checked quote in Sources | Tech lead |
| Running PostgreSQL takes more time than three developers can give | List the running tasks (backups, upgrades, monitoring) with hours a month and an owner for each | List agreed with the engineering manager | Developer (proposed) |
| Two app servers overwrite each other's saves even on PostgreSQL | Test two app instances against one database at above 5 saves a second before Q3 2027 | Test shows no lost or failed saves | Developer (proposed) |
| Data is lost or changed in the move from the current database | Dry-run the move and compare row counts and sample records | Counts and samples match | Developer (proposed) |
| The peak of about 5 saves a second [8] is wrong | Measure peak saves over a longer period than one month | New figure recorded here | Tech lead |
| The Q3 2027 plan changes and the move was not needed | Confirm the two-server plan before accepting | Plan confirmed in writing | Engineering manager |

## Next steps
1. Read PostgreSQL's documentation on concurrent writes and add the quote to Sources. Tech lead, 27 Nov 2026 (proposed).
2. List PostgreSQL running tasks with hours and owners. Developer (proposed), 2 Dec 2026 (proposed).
3. Confirm the Q3 2027 two-server plan. Engineering manager, 2 Dec 2026 (proposed).
4. Decide and set Status to accepted or rejected. Tech lead and engineering manager, 5 Dec 2026.
5. Run the two-server write test. Developer (proposed), before the second server goes live in Q3 2027 (proposed).

## Confirmation
The tech lead checks that steps 1 to 3 are done before 5 Dec 2026. After the second app server
goes live, the tech lead reviews failed or lost saves and the team's running hours, and the team
looks at this record again one month later (date proposed: one month after go-live).

## Not known
- Whether PostgreSQL supports safe writes from two app servers on separate machines: not in the
  text you sent. Find out from PostgreSQL's own documentation.
- Running effort for each option with no database administrator: no source. Find out with step 2.
- Cost of switching later for any option: no source and no figures.
- Which database Shiftboard uses today: not given.
- Whether about 5 saves a second counts as writers that "can queue up and take turns" [3]: the
  page gives no threshold.
- None of the pasted pages contained instructions to AI assistants.

## Sources
I could not open the links in this chat. I read the text you pasted, which you copied on
24 November 2026.

| # | The exact words | Source and link | Checked | Result |
| --- | --- | --- | --- | --- |
| 1 | "SQLite works great as the database engine for most low to medium traffic websites (which is to say, most websites)." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 24 Nov 2026 (pasted text) | Checked |
| 2 | "SQLite supports an unlimited number of simultaneous readers, but it will only allow one writer at any instant in time." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 24 Nov 2026 (pasted text) | Checked |
| 3 | "processes need to write the database at the same instant (and they cannot queue up and take turns) ... which always means a client/server database engine." | Appropriate Uses For SQLite, https://www.sqlite.org/whentouse.html | 24 Nov 2026 (pasted text) | Checked (applies only when writers cannot take turns) |
| 4 | "Generally, if your data is separated from the application by a network, you want to use a client/server database." | SQLite Over a Network, Caveats and Considerations, https://sqlite.org/useovernet.html | 24 Nov 2026 (pasted text) | Checked |
| 5 | "in MVCC locks acquired for querying (reading) data do not conflict with locks acquired for writing data, and so reading never blocks writing and writing never blocks reading." | PostgreSQL 18 documentation, 13.1 Introduction, https://www.postgresql.org/docs/18/mvcc-intro.html | 24 Nov 2026 (pasted text) | Checked (reads against writes only) |
| 6 | "Postgres is always faster than SQLite." | A teammate, quoted by you; no link | not checked | ⚠ No source (opinion) |
| 7 | "about 40 staff use it" | You, in this chat | not checkable | Their figures |
| 8 | "at the busiest time, about 5 saves a second (our estimate from last month's logs)" | You, in this chat | not checkable | Their figures |
| 9 | "In the plan for Q3 2027, we add a second app server on a separate machine behind a load balancer, both writing to the same data." | You, in this chat | not checkable | Their figures |
| 10 | "we are three developers, no database administrator" | You, in this chat | not checkable | Their figures |
```

**Before you commit this:** open two of the links above and find the quoted words with Ctrl+F (Cmd+F on a Mac). Fix or remove anything marked ⚠. This recommends; you and your engineering manager decide.
