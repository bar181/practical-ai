# The fresh-run test

The author of a tool cannot see its faults, because the author knows what was meant. This test
hands the tool to a new AI session that knows nothing, and asks it to say where it tripped.

**Think of it as** asking a stranger to assemble your flat-pack furniture using only the leaflet.
Where they stop and frown is where the leaflet is wrong.

## How to run one

1. Make a folder for the run, outside the project or in its `_build/runs/round-1/`. Put three things in it and nothing else: a copy of your tool's
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
| The same point in three or more logs | The instructions are wrong | Fix the instructions |
| A point in one log only | It may be that request, or that session | Note it. Fix it if it is cheap |
| The run did not finish | A real break, such as a missing file or a wrong path | Fix this first |
| The result is good and the log is long | The session guessed well. A weaker assistant will not | Fix the blocking points |

Then run it again on the fixed instructions, and compare the last line of each log.

## What it found on project one

On 16 November 2026, thirteen fresh sessions ran in parallel against Artifact Studio. Each took
between 5 and 11 minutes. Every one finished. Together they logged about 230 points of friction.
One found that the server broke when its folder was copied by itself. The author's own review,
over two days, had found two faults. The logs are in
[`artifact-studio/_build/examples/runs/`](../../../artifact-studio/_build/examples/runs/).

## What it found on this project

The build coach was tested the same way on 16 November 2026: two invented people, a beginner
and a builder, two rounds each. All four runs handed over a plan, a first version and a note.
The first round found that the second gate ran backwards (yes meant stop), that the eighth gate
asked for a test result nobody had, and that "decide" collided with "never invent". The logs and
the unedited results are in [`runs/`](runs/).

| Round | Beginner idea | Builder idea |
| --- | --- | --- |
| 1 | 4 blocking, 11 minor | 5 blocking, 12 minor |
| 2, after fixes | 4 blocking, 11 minor | 3 blocking, 9 minor |

The round 2 points were fixed and not tested again. The count did not fall much because each
round finds new, smaller points: the round 2 list does not repeat the round 1 list.

## Limits

- A fresh AI session is not a person. It reads everything and never gets bored. People do not.
- The sessions used here were all one assistant, Claude. A different assistant may trip elsewhere.
- It tests whether the instructions can be followed. It does not test whether the tool is wanted.
