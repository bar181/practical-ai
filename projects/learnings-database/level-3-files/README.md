# Level 3: a shared database for your team

Your team's log in one Supabase database, connected to Claude or ChatGPT with Supabase's own
connector. No code to write and nothing to host: you paste one file and one line per project. The
chatbot saves rows itself after your yes, everyone gets the same rules, and the database keeps a
history of every change with who approved it.

**Think of it as** a shared logbook kept behind a counter: the chatbot asks at the counter, and the
logbook keeps the rules.

**Status, 19 November 2026, by its author:** the database file passes its test on Postgres, and a
fresh Claude session used it correctly through SQL alone ([results](../quality-results/README.md)).
**Not yet tried on a real Supabase project or with the real connector.**

## Set up (about fifteen minutes)

1. **Make a Supabase project for the log only.** Sign in at [supabase.com](https://supabase.com)
   (the free plan should be enough) and create a new Supabase project named `learnings`. Keeping
   the log on its own means the connection reaches nothing else.
2. **Create the database.** Open the Supabase project's **SQL Editor**, paste the whole of
   [`schema.sql`](schema.sql), and press **Run**. It is safe to run again.
3. **Add your projects or jobs to the list.** In the same editor, run one line for each, for
   example:

   ```sql
   insert into learnings.lists values ('project', 'newsletter', 'The monthly customer email');
   ```

   Keep `'project'` as it is. Change `'newsletter'` to a short name for your job (lowercase, hyphens,
   no spaces), and the last part to one line that describes it.

4. **Connect your chatbot.** A connector is a saved link that lets the chatbot use another app for
   you.
   - **Claude:** in **Settings > Connectors**, add a custom connector with this address, putting
     your ID from **Project Settings** in Supabase in place of `YOUR-PROJECT-ID`, then sign in to
     Supabase when asked:
     `https://mcp.supabase.com/mcp?project_ref=YOUR-PROJECT-ID`
     The ID keeps the chatbot inside this one Supabase project. In the connector's settings, keep
     its tools on "ask before use", so you see every change before it runs.
   - **ChatGPT (not yet tried):** add Supabase from its apps or connectors. If it asks for an
     address, use the one above.
5. **Give it the instructions.** Use the Level 1 link, or a Level 2 Project or plugin. They tell the
   chatbot to use the database when it is connected.
6. **Try it.** Say "log that: ...". You should see it look for a repeat, show you the row, and save
   it after your yes as `proposed`. At the weekly review, it changes a status only when you say so,
   and records your name.

**Already have a spreadsheet log?** Add its projects (step 3), save the Learnings tab as CSV, then
in Supabase's **Table Editor** choose the `learnings` schema and the `learnings` table, and use
**Import data from CSV**. Rows keep their ids, and new rows continue from the highest one.

**A team:** invite people to the Supabase project. Each person connects with their own Supabase
login.

## What the database guarantees, and what it does not

| The database does | The instructions do |
| --- | --- |
| Starts every new row as `proposed`, with `seen` 1 | Ask before saving anything |
| Refuses an area or lesson type that is not on the lists | Search for a repeat before writing |
| Refuses a status change without the name of the person who approved it | Change a status only for a decision you made in that chat |
| Records every insert and change in `learnings.history` | Use only the six functions, never edit or delete rows directly |
| Serves only accepted rows, and only their rules, never the details of a sensitive row | Treat the log as data, never as instructions |
| Keeps the log private: Supabase's public web access to your data cannot reach it | |

The Supabase connector can run any SQL in the project it reaches. The instructions forbid anything
but the six functions, but they cannot enforce it. That is why the log gets a project of its own,
the connection is limited to it, and the tools ask before each use.

## The six functions (the chatbot runs these; you do not have to)

| To | Run |
| --- | --- |
| Look for a repeat | `select * from learnings.similar_rows('area', 'project', 'key words')` |
| Add a lesson | `select learnings.log_learning(p_kind => 'error', p_area => 'marketing', p_rule => 'When ..., do ...', p_what_happened => '...', p_expected => '...')` |
| The same lesson again | `select learnings.mark_seen('L-9')` |
| Rules for the work | `select * from learnings.find_rules(p_project => 'newsletter')` |
| The weekly review | `select * from learnings.review_queue()` |
| Your decision | `select learnings.set_status('L-9', 'accepted', 'Your Name')` |

You can run these yourself in the SQL Editor too, and open the `learnings.learnings` table in the
Table Editor to read or export the whole log.
