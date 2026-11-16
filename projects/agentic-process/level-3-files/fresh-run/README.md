# The fresh-run test

The author of a tool cannot see its faults, because the author knows what was meant. This test
hands the tool to a new AI session that knows nothing, and asks it to say where it tripped.

**Think of it as** asking a stranger to assemble your flat-pack furniture using only the leaflet.
Where they stop and frown is where the leaflet is wrong.

## How to run one

1. Make a folder for the run: `_build/runs/round-1/<what was asked>/` in your project. Put three things in it and nothing else: a copy of your tool's
   instructions, the message a user would send (`prompt.txt`), and any files that user would
   attach.
2. Start a new session: a new chat, or a sub-agent with no memory of the project. Give it
   [`RULES.md`](RULES.md) and the path of the run folder.
3. Let it finish. Do not help.
4. Read `friction.md` before you look at the result.

Run several at once, one for each kind of request your tool should handle. They do not need to
know about each other.

## How to read the results

| What you see | What it means | Do this |
| --- | --- | --- |
| The same point in two or more logs | The instructions are wrong | Fix it first |
| A blocking point in one log only | A different guess would change the result | Fix it next |
| A minor point in one log only | It may be that request, or that session | Note it. Fix it if it is cheap |
| The run did not finish | A real break, such as a missing file or a wrong path | Fix this first |
| The result is good and the log is long | The session guessed well. A weaker assistant will not | Fix the blocking points |

Then run it again on the fixed instructions, and compare the last line of each log.

## Evidence

This test was used on both tools in this repository. The logs, unedited, are in
[`test-runs/`](../test-runs/) for this project and in
[Artifact Studio's runs](../../../artifact-studio/_build/examples/runs/). On both, a fresh session
found faults the author had read past, and each round of fixes found new, smaller ones.

## Limits

- A fresh AI session is not a person. It reads everything and never gets bored. People do not.
- The sessions used here were all one assistant, Claude. A different assistant may trip elsewhere.
- It tests whether the instructions can be followed. It does not test whether the tool is wanted.
