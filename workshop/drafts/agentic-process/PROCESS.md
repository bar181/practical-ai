# The process: one page

How a tool gets built in this repository. The [builder skill](builder/agentic-process/SKILL.md)
follows it.

**Think of each tool as** a recipe card: one card that works in any kitchen. You do not print a
card for each brand of oven.

**The user's path:** open the explainer, give it your input, get a result.

## What a tool is

```
<tool-name>/
  README.md     the explainer: what it does, quick start, what to give it, what you get, what to check
  SKILL.md      the tool: one portable file in the open Agent Skills format
  example.md    one worked example, unedited, with invented data
  template.md   optional: only if the output has a fixed shape
```

`SKILL.md` is the one source of instructions. It works pasted into any chatbot on its own, so it
holds everything essential, including the output shape. Its `name` matches its folder name. It
starts by asking for any missing context in one reply. There is no stepper. The portable part is
the instructions; connectors, permissions and scheduling still depend on where it runs.
Start from the [template](template/).

## Reuse first

| What already exists | What we ship |
| --- | --- |
| Something does the whole job | A README only: what it is and a link, the platform it needs, setup steps, a small example. If it depends on a plugin, say what a person can paste in by hand for Level 1, and call it portable once that path has been run |
| Something does part of it | A thin SKILL.md: the business rules and the missing steps |
| Nothing fits | A full SKILL.md |

Look at Anthropic's skills and plugins first, then the platform the person uses, then open
source. In Claude, draft the SKILL.md with the skill-creator skill; elsewhere, fill in the template.

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
| 2 | Reuse check | You know what exists, with links and dates, and which row of the reuse table applies |
| 3 | Outside help | You know what, if anything, to buy or connect |
| 4 | Cost | It costs nothing beyond the chatbot, or an amount the owner accepts |
| 5 | Simplest design | The fewest files that do the job; levels only where they earn their place |
| 6 | Plan | The README's first lines and the SKILL.md's steps are written |
| 7 | Review | Someone other than the author can say what it does from the README |
| 8 | Build and check | The short check below has been run and recorded |
| 9 | Grow | Real use shows what to add next |

## The short check

1. Paste `SKILL.md` into a fresh chat and run the worked example's input.
2. Run a different input of the same kind.
3. Confirm it asks for missing context in one reply, follows the stated rules, and flags what it
   is unsure of.
4. Try the same file in a second chatbot before saying it works across chatbots.

Record the results in the README. A check not run is written "not yet run".

## Rules

- Invent no facts. Missing data is reported as missing, never as zero.
- A person approves anything that is sent, posted, paid, published or merged.
- Nothing extra: no scripts, harnesses or folders a tool does not need.
