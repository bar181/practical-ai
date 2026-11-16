# Expert: let agents build, and know whether it worked

For teams, and for agents that work unattended. Three things: gates a script can run, a test by
fresh sessions, and a score sheet.

**Think of it as** the inspection regime on a building site. Nobody takes the builder's word
that the wiring is safe.

| What | Where | What it does |
| --- | --- | --- |
| Gates | [`gates.json`](gates.json) | A list of commands, each proving one thing. An agent runs them after every stage and stops at the first failure |
| The fresh-run test | [`fresh-run/`](fresh-run/) | Hands the tool to a new AI session that knows nothing, and collects where it tripped |
| The score sheet | [`scorecard.md`](scorecard.md) | Ten measures, what 80 looks like for each, and rules for scoring your own work |

## Run the gates

From the repository root:

```
python3 workshop/tools/gates.py projects/agentic-process
```

Each gate prints pass or fail and what it proves. Write your own in the same form: a name, what
it proves, and one command that exits with an error when the thing is not true.

## Run it unattended

1. Give the agent the [skill](../level-2-files/agentic-process/) and one approved idea.
2. Tell it to run the gates after every step and to stop at the first failure.
3. Tell it to run the fresh-run test at step 8 and to hand back the friction logs unedited.
4. It opens a change request and stops. A person reads the logs and decides.

Nothing here merges, posts or publishes. A schedule is not set up for you: add one only after a
run you triggered by hand has gone well.

The gates and the fresh-run test have been used on two projects, both by their author.
