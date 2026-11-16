# Expert: let agents build, and know whether it worked

For teams, and for agents that work unattended. Three things: gates a script can run, a test by
fresh sessions, and a score sheet.

**Think of it as** the inspection regime on a building site. Nobody takes the builder's word
that the wiring is safe.

| What | Where | What it does |
| --- | --- | --- |
| Gates | Your project's `_build/gates.json` | A list of commands, each proving one thing. An agent runs them after every step and stops if one fails |
| The fresh-run test | [`fresh-run/`](fresh-run/) | Hands the tool to a new AI session that knows nothing, and collects where it tripped |
| The score sheet | [`scorecard.md`](scorecard.md) | Ten measures, what 80 looks like for each, and rules for scoring your own work |
| The test logs | [`test-runs/`](test-runs/README.md) | Every fresh-session test of this project, unedited |

## Gates for your project

Every project made from [the template](../level-2-files/agentic-process/template/) starts with
four gates in `_build/gates.json`, and the scripts to run them in `_build/checks/`. On a
project whose blanks are all filled in, this is the real output:

```
python3 my-tool/_build/checks/gates.py my-tool
```

```
pass    layout     0.0s  The folder follows the showcase layout
pass    links      0.0s  No Markdown link in this project is broken
pass    filled     0.0s  The front page, the agent file and the plan have no blanks left. Fails until step 6
pass    built      0.0s  The beginner version has no blanks left. Fails until step 8

All gates that ran passed.
```

Add a gate whenever a step produces something a command can check. A gate is a name, what it
proves, and one command that exits with an error when the thing is not true:

```json
{"name": "example", "proves": "The worked example still matches its input", "run": "python3 _build/check_example.py"}
```

Commands run from the project folder. Mark a slow gate with `"slow": true`; it runs only with
`--all`.

**A fuller gate file:** this project's own, [`gates.json`](gates.json), has seven gates. Two of
them make a new project from the skill folder in an empty folder: one checks that its blanks are
caught, the other fills them in and expects every gate to pass, so a broken template is caught
before anyone uses it. The [unattended run](../base/examples/unattended-run.md) shows an agent
adding a gate of its own.

## Run it unattended

1. Copy [the skill folder](../level-2-files/agentic-process/) into the agent's skills, and give
   it one approved idea in writing.
2. Tell it to run the gates after every step from step 5, and to stop if one fails. The script
   runs every gate, so one report shows everything that is wrong. `filled` fails by design
   until step 6, and `built` until step 8: those are the only failures the agent expects.
3. At step 8 it prepares the fresh-run folders. You, or an orchestrating agent, start a fresh
   session for each folder with [`fresh-run/RULES.md`](fresh-run/RULES.md).
4. The agent reads the friction logs, fixes the recurring points, runs the gates again and hands
   back: the plan, the first version, the gate output, the friction logs unedited, and a note.
5. A person reads the hand-back and decides. Nothing is merged, posted or sent before that.

[A worked unattended run](../base/examples/unattended-run.md) shows the whole hand-back from an
agent that had only the skill folder, in a repository it had never seen.

Add a schedule only after a run you started by hand has gone well.
