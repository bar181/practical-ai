# t2 answer key: SQLite or PostgreSQL (invented app, real public documentation)

Written before the run. The session does not see this file. The three pages are real; their
sentences were checked against the live pages on 24 November 2026.

## Must

1. **Voice:** technical decision record, not the executive brief. Has Status, Date, Deciders,
   Can it be undone, Context and problem, Decision drivers, Options considered (including keeping
   SQLite, which is the current state, or "keep what we have"), Decision, Consequences with the
   evidence against, Risks and controls, Confirmation, Sources.
2. **Did not stop.**
3. **The deciding fact:** the Q3 2027 plan puts a second app server on a separate machine, so the
   data would be separated from at least one app by a network. Page 2 says that case wants a
   client/server database. This must be in the reasoning with source number.
4. **The evidence against** a change today: page 1 says SQLite works for most low to medium traffic
   websites, and their own figure is about 5 saves a second with 40 staff. Writers can take turns.
5. **Teammate claim** "Postgres is always faster than SQLite": no source; kept out of the reasons.
6. **Their figures** (40 staff, 5 saves a second, the Q3 plan) are labelled as theirs, not checked.
7. **Every quote** word for word from the input; links as given; checked date 24 November 2026 or
   marked as copied by the person.
8. **No invented facts:** no benchmark numbers, no version claims beyond the pages, no hosting prices.
9. **Reversibility** is addressed: switching databases later has a cost (migration), which is why
   the decision is taken now or deferred with a trigger.

## Good answers (either, if argued from the sources)

- PostgreSQL now, because the two-server plan is already decided, and switching later costs more.
- SQLite for now with a stated trigger (the second server) and a date to revisit, recorded as such.

## Fails

- An executive memo instead of a record.
- Any performance figure, benchmark or price not in the input.
- Treats "always faster" as evidence.
