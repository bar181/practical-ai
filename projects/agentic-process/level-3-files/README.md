# Expert: let agents build, and know whether it worked

For teams, and for agents that work unattended. Three things: gates a script can run, a test by
fresh sessions, and a score sheet.

**Think of it as** the inspection regime on a building site. Nobody takes the builder's word
that the wiring is safe.

| What | Where | What it does |
| --- | --- | --- |
| Gates | Your project's `_build/gates.json` | A list of commands, each proving one thing. An agent runs them after every stage and stops at the first failure |
| The fresh-run test | [`fresh-run/`](fresh-run/) | Hands the tool to a new AI session that knows nothing, and collects where it tripped |
| The score sheet | [`scorecard.md`](scorecard.md) | Ten measures, what 80 looks like for each, and rules for scoring your own work |

## Gates for your project

Every project made from [the template](../level-2-files/agentic-process/template/) starts with
three gates in `_build/gates.json`, and the scripts to run them in `_build/checks/`:

```
python3 my-tool/_build/checks/gates.py my-tool
```

```
pass    layout     0.0s  The folder follows the showcase layout
pass    links      0.0s  No Markdown link in this project is broken
pass    filled     0.0s  No blanks are left from the template. Fails until step 6 is done

All gates that ran passed.
```

Add a gate whenever a step produces something a command can check. A gate is a name, what it
proves, and one command that exits with an error when the thing is not true:

```json
{"name": "example", "proves": "The worked example still matches its input", "run": "python3 _build/check_example.py"}
```

Commands run from the project folder. Mark a slow gate with `"slow": true`; it runs only with
`--all`.

**A fuller gate file:** this project's own, [`gates.json`](gates.json), has six gates. The
[unattended run](../base/examples/unattended-run.md) shows an agent adding a gate of its own. One of
them makes a new project from the skill folder in an empty folder and runs that project's gates,
so a broken template is caught before anyone uses it.

## Run it unattended

1. Copy [the skill folder](../level-2-files/agentic-process/) into the agent's skills, and give
   it one approved idea in writing.
2. Tell it to run the gates after every step from step 5, and to stop if any gate fails. The
   script runs every gate, so one report shows everything that is wrong.
3. At step 8 it prepares the fresh-run folders. You, or an orchestrating agent, start a fresh
   session for each folder with [`fresh-run/RULES.md`](fresh-run/RULES.md).
4. The agent reads the friction logs, fixes the recurring points, runs the gates again and hands
   back: the plan, the first version, the gate output, the friction logs unedited, and a note.
5. A person reads the hand-back and decides. Nothing is merged, posted or sent before that.

[A worked unattended run](../base/examples/unattended-run.md) shows the whole hand-back from an
agent that had only the skill folder, in a repository it had never seen.

Add a schedule only after a run you started by hand has gone well.
