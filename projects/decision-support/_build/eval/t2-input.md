Write this as an ADR for our repo. Run straight through.

Decision: SQLite or PostgreSQL for Shiftboard, our internal shift-scheduling web app. I am the tech lead and I decide with our engineering manager this sprint (by 5 December 2026).
Our figures: about 40 staff use it; at the busiest time, about 5 saves a second (our estimate from last month's logs). Today it runs on one server. In the plan for Q3 2027, we add a second app server on a separate machine behind a load balancer, both writing to the same data.
What matters: safe concurrent writes once there are two app servers; effort to run it (we are three developers, no database administrator); cost of switching later.

Pages I copied today (24 November 2026):

Page 1, https://www.sqlite.org/whentouse.html (Appropriate Uses For SQLite):
"SQLite works great as the database engine for most low to medium traffic websites (which is to say, most websites)."
"SQLite supports an unlimited number of simultaneous readers, but it will only allow one writer at any instant in time."
"If many threads and/or processes need to write the database at the same instant (and they cannot queue up and take turns) then it is best to select a database engine that supports that capability, which always means a client/server database engine."

Page 2, https://sqlite.org/useovernet.html (SQLite Over a Network, Caveats and Considerations):
"Generally, if your data is separated from the application by a network, you want to use a client/server database."

Page 3, https://www.postgresql.org/docs/18/mvcc-intro.html (PostgreSQL 18 documentation, 13.1 Introduction):
"The main advantage of using the MVCC model of concurrency control rather than locking is that in MVCC locks acquired for querying (reading) data do not conflict with locks acquired for writing data, and so reading never blocks writing and writing never blocks reading."

A teammate says: "Postgres is always faster than SQLite."
