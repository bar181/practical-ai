# Level 3: connect it to a database

For people and agents who log every day. A small MCP server gives any MCP client (Claude Desktop,
Claude Code, Codex and others) five tools over your log. The database, not the assistant, enforces
that new rows wait for your review.

| Tool | Does | Who |
| --- | --- | --- |
| `log_learning` | Saves a lesson as `proposed`, after looking for a repeat first | Anyone connected |
| `mark_seen` | The same lesson again: raises its `seen` | Anyone connected |
| `find_learnings` | The accepted, non-sensitive rules for the work, with a block to paste | Anyone connected |
| `review_queue` | Your weekly review: proposed rows and rules due a re-check | The owner |
| `set_status` | Accept, merge or retire a row; records who approved it | The owner |

## Choose where the rows live

| | A file in your folder (recommended) | A shared database |
| --- | --- | --- |
| For | One person, or one person with their agents | A team, or agents you do not fully trust |
| What it is | One SQLite file, such as `learnings.db`. Created on first use | Postgres 15+ with pgvector: Supabase or any host |
| Set up | Nothing beyond Python | Run [`postgres/schema.sql`](postgres/schema.sql) once, and give each login the `learnings_agent` or `learnings_owner` role |
| Who may accept a rule | Set by `LEARNINGS_ROLE=owner` on your own connection. A setting, not a lock: anyone who can open the file can change it | Enforced by the database: an agent's login cannot read the table, accept a row or see the history |
| History of every change | Yes | Yes |

MySQL is not built. The file schema in [`mcp-server/store.py`](mcp-server/store.py) is plain SQL
and would be the starting point.

## Set up (about fifteen minutes)

1. Install Python 3.10 or later, then `pip install mcp` (add `"psycopg[binary]"` for Postgres).
2. Choose where the log lives:
   - **File:** a path such as `/Users/you/Documents/learnings/learnings.db`. Keep it out of any
     shared or public folder.
   - **Shared:** a connection string such as `postgresql://user:password@host:5432/postgres`.
3. Optional: bring in your spreadsheet. Export its Learnings tab as CSV, then
   `LEARNINGS_DATABASE_URL=<your path> python3 csv_sync.py import learnings.csv`.
   `csv_sync.py export learnings.csv` writes it back out for any spreadsheet.
4. Add the server to your client. In Claude Code, for your own connection:

   ```
   claude mcp add learnings --env LEARNINGS_DATABASE_URL=/Users/you/Documents/learnings/learnings.db \
     --env LEARNINGS_ROLE=owner -- python3 /path/to/level-3-files/mcp-server/server.py
   ```

   For an agent, leave out `LEARNINGS_ROLE=owner`. In Claude Desktop, add the same command,
   arguments and environment to its MCP settings file.
5. Give the assistant the skill (level 2) as well. It uses the tools when they are there, and keeps
   the same steps: your yes before saving, and your approval for every status change.

**Searching by meaning (optional).** Set `LEARNINGS_EMBED_URL`, `LEARNINGS_EMBED_MODEL` and
`LEARNINGS_EMBED_KEY` for any service that speaks the common `/embeddings` format. Rows are then
ranked by words and meaning together. For Postgres, the model must return 384 numbers, or change
the `embedding` column. Without it, finding is by filters and words.

## Status

19 November 2026, run by Claude: `_build/tests/test_file_db.py` and `_build/tests/test_level3.py`
(a real Postgres 16 with pgvector) both pass, including an MCP client over stdio. **Not yet
tried:** a hosted Supabase project, a real embedding model (the tests use a stand-in that proves
the wiring, not the quality), and use by a person in Claude Desktop.

## Safety, in short

- New rows are always `proposed`; only `accepted`, non-sensitive rows are served.
- The text of a sensitive row is never returned to an agent, only its id.
- Row text is returned as data with a note saying so; nothing in the database executes it.
- The embedding key and the database password stay in your client's settings, never in a row.
