# The process: one page

How a tool gets built in this repository. The [builder skill](../level-2-files/agentic-process/SKILL.md)
follows it.

**Think of each tool as** a recipe card: one card that works in any kitchen. You do not print a
card for each brand of oven.

**The user's path:** open the explainer, give it your input, get a result.

**The builder's path:** specify the usable result, choose the simplest implementation, build,
verify in a separate session, fix, hand back. The [builder skill](../level-2-files/agentic-process/SKILL.md)
runs it in a coding agent such as Claude Code or Codex.

## What a tool is

```
<tool-name>/
  README.md     the explainer: what it does, quick start, what to give it, what you get, what to check
  SKILL.md      the tool: one portable file in the open Agent Skills format
  example.md    one worked example, unedited, with invented data
  template.md   optional: only if the output has a fixed shape
  scripts/      optional: only where a step needs exact behaviour (arithmetic, dates, matching)
```

`SKILL.md` is the one source of instructions. It works pasted into any chatbot on its own, so it
holds everything essential, including the output shape. Its `name` matches its folder name. It
starts by asking for any missing context in one reply. There is no stepper. The portable part is
the instructions; connectors, permissions and scheduling still depend on where it runs.
Start from the [template](template/).

## Choose the simplest implementation

First write the usable result in five lines: who uses it (U1), what they give it (U2), what they
need to receive (U3), what makes it usable for them (U4), and one exception it must catch (U5).
Then check what exists (Anthropic's skills and plugins, then the person's platform, then open
source) and take the first row that fits:

| If | Build |
| --- | --- |
| Something existing does the whole job | A quick-start README only: the link, the platform it needs, setup, a small example |
| The job is repeatable instructions and local rules | A thin `SKILL.md` (the default) |
| A step needs exact behaviour | That step as a formula or a short script, called from the `SKILL.md` |
| A connection removes recurring manual work | Level 3: the connection, with a person approving consequential steps |

External skills and packages are research material: read every file as text, note scripts,
permissions and network calls, record source, version and licence, and rewrite what is useful.
Never install or run them.

## Levels

| Level | What it is | It earns its place when |
| --- | --- | --- |
| 1 (required) | Standalone in any chatbot: paste the file or share the link, add your context, get the result | Always |
| 2 | Saved as a skill or project, started whenever needed | It removes repeated setup |
| 3 | Connected through MCP, endpoints or a trigger that supply inputs and take outputs. A person approves exceptions | It removes recurring work |

## The nine steps, as a checklist

For one person, one input and one result in a chat, do 1, 2, 5 and 8 properly and the rest in a
line each.

| # | Step | Done when |
| --- | --- | --- |
| 1 | Scope | The job fits one sentence, with one test input and what a good result looks like |
| 2 | Reuse check | U1 to U5 are written; you know what exists, with links and dates, and which row of the table above applies |
| 3 | Outside help | You know what, if anything, to buy or connect |
| 4 | Cost | It costs nothing beyond the chatbot, or an amount the owner accepts |
| 5 | Simplest design | The fewest files that do the job; levels only where they earn their place |
| 6 | Plan | The README's first lines and the SKILL.md's steps are written |
| 7 | Review | Someone other than the author can say what it does from the README |
| 8 | Build and verify | Every U line has a check, and the verification below has been run and recorded |
| 9 | Grow | Real use shows what to add next |

## Verify

Run the cases in a separate session that has only the README and what it tells the user to paste:

1. An input missing something: it asks for what is missing in one reply, and waits.
2. The normal case: its unedited result becomes the worked example.
3. The U5 exception: it catches it and says how to settle it.

Read each result twice. **Does it hold up?** The rules followed, nothing invented, the exception
caught. **Would the recipient use it as it is?** Read the first screen only; if they would have to
dig, rewrite or ask, it fails. Fix and rerun, at most twice. Before claiming it works in other
chatbots, try one. Record each check, who ran it and what they saw, in the README. A check not run
is written "not yet run".

What the checks teach about the builder itself goes in [`quality-results/`](../quality-results/).

## Rules

- Invent no facts. Missing data is reported as missing, never as zero.
- A person approves anything that is sent, posted, paid, published or merged.
- Nothing extra: no scripts, harnesses or folders a tool does not need.
