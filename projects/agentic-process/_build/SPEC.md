# Agentic Process: specification, version 2

**Draft, 16 November 2026, rewritten the same evening to the simpler outline the owner approved.**
The source of truth for what Agentic Process is and when it is done. Decisions not yet confirmed
are marked **Owner to confirm**, with the default used until then.

## 1. Purpose

**Agentic Process builds useful tools for work people repeat.** Its nine-step method and its
builder skill are shared scaffolding for every project in this repository. Each project gives
someone a useful tool they can start quickly, with a short explainer that shows how to use it.

**The user's path:** open the explainer, give it your input, get a result.

**User value.** Save time or improve the quality of a specific result, against the usual way of
doing the job.

**North Star.** Someone opens a tool and gets a usable result with their own input. At Level 3,
connected systems supply the inputs and a person handles the exceptions.

## 2. One source of instructions per tool

Every custom tool has one `SKILL.md` in the open Agent Skills format. The same file is the Claude
skill, works in other tools that support the format, and can be pasted into any chatbot as the
fallback, so the repository is not tied to one provider. The README explains how to get a useful
result. The worked example shows what a good result looks like.

The portable part is the instructions. Connectors, permissions and scheduling still depend on
where a tool runs, and the README says so where it matters.

```
<tool-name>/
  README.md     the explainer
  SKILL.md      the tool
  example.md    one worked example, unedited, invented data
  template.md   optional: only if the output has a fixed shape
```

**Rules for SKILL.md**

- It works when pasted on its own, so everything essential is in it, including the output shape.
- Its `name` matches its folder name, so it also installs natively.
- It starts by asking for any missing context **in one reply**: a short list of what to give it,
  with an example line, then it waits. No stepper and no question-by-question interview.

**The README's parts:** what it does; the quick start (copy `SKILL.md` into a chat and add your
input, with the link offered as a shortcut, since some chatbots cannot open links); what to give
it; what you get, linking the example; what to check before acting; Level 2; Level 3 only if it
exists; and the check record.

## 3. Levels

A tool does not need all three. Level 1 is required.

| Level | What it is | It earns its place when |
| --- | --- | --- |
| 1 | Standalone in any chatbot: paste the file or share the link, add your context, get the result | Always required |
| 2 | Saved as a skill or project, started whenever needed | It removes repeated setup |
| 3 | Connected through MCP, endpoints or a trigger that supply inputs and take outputs. A person approves exceptions | It removes recurring work |

## 4. Reuse first

Do not rebuild what is already fully supported.

| What already exists | What we ship |
| --- | --- |
| An existing skill or plugin does the whole job | **Reuse-only:** one README with a link, the platform it needs, setup steps and a small example. No SKILL.md. If a wrapper depends on the plugin, the README says what a person can supply by hand for Level 1, and the tool is called portable once that path has been run |
| It does part of the job | A thin SKILL.md: the business rules and the missing steps |
| Nothing fits | A full SKILL.md |

Look at Anthropic's skills and plugins first, then the platform the person uses, then open
source. To write a skill in Claude, use the skill-creator skill; elsewhere, fill in the template.

## 5. What Agentic Process contains

Four things, and nothing else.

| Part | File | State |
| --- | --- | --- |
| The process, one page, with the nine steps as a compact checklist | [`PROCESS.md`](../base/PROCESS.md) | Written |
| The tool template | [`base/template/`](../base/template/) | Written |
| A thin builder skill | [`level-2-files/agentic-process/SKILL.md`](../level-2-files/agentic-process/SKILL.md) | Built [`learning-log`](../base/examples/learning-log/) (AC-3), then beat a direct build 93 to 73 in a blind pilot ([quality results](../quality-results/)) |
| One working example | [`base/examples/decision-support/`](../base/examples/decision-support/) | Passed the short check in Claude (AC-1) |

The explainer for Agentic Process itself is [`README.md`](../README.md).

## 6. The builder

**In:** the job (an idea, a spec or a transcript of someone doing it), who it is for, and one
input with what a good result looks like.

**Out:** a tool in the layout of section 2, the short check recorded, and a hand-back note: what
was built, the reuse decision, the check results, assumptions, and what a person decides next.

**When something is missing,** it asks once in one reply. If it cannot ask, it takes the plainest
reading, carries on and lists its assumptions. **Owner to confirm**; default: carry on.

## 7. Verification

The builder writes the usable result as five lines (U1 to U5: who uses it, what they give it,
what they need, what makes it usable, one exception), gives each a check, and runs the checks in
a separate session: an input missing something, the normal case, and the exception. Each result
is read twice: does it hold up, and would the recipient use it as it is. Details in
[`PROCESS.md`](../base/PROCESS.md). What the checks teach about the builder goes in
[`quality-results/`](../quality-results/).

## 8. Done when

| ID | Criterion |
| --- | --- |
| AC-1 | Decision support passes the three-input short check in Claude. **Met, 16 November 2026** |
| AC-2 | Decision support passes the same check in a second chatbot |
| AC-3 | The builder turns one plan (the learning system) into a tool in the section 2 layout, with the short check recorded and nothing extra. **Met, 16 November 2026**: the builder could not start a fresh session itself, so the check was run separately and passed |
| AC-4 | The owner runs one tool from its README with their own input and gets a usable result without editing the file |

## 9. Out of scope

Dropped from version 1, and since deleted (the git history keeps them): the chatbot
coach, courses and lessons, Autopilot, gates and check scripts inside each tool, the fresh-session
test harness, the separate workflow card and instruction file, and generated pages. A Level 3
connection is built only when a tool needs one.

## 10. Next, in order

AC-1 and AC-3 hold. [The check records](../quality-results/2026-11-16-decision-support-checks/).

1. Run AC-2: paste decision support's `SKILL.md` into ChatGPT or Gemini with the bakery input.
2. Owner: decide whether to make the brief read more like advice (fewer inline labels, plainer
   wording when the rule picks a check), the one weakness every blind grader named.
3. Done 16 November 2026: moved to `projects/agentic-process/`; `PROCESS.md` is the single process.

## 11. How it is scored

Out of 100. No item counts users.

| Item | Weight | What 100 looks like |
| --- | --- | --- |
| Useful result fast | 30 | From the README, a person pastes one file, adds their input and gets a usable result |
| One file, portable | 20 | Each tool's SKILL.md works pasted on its own and installed natively, in at least two chatbots |
| Reuse first | 15 | Each tool records what it reused, wrapped or built, with links and dates |
| Checked honestly | 20 | The short check is run and recorded for every tool; nothing claims more than was run |
| Small | 15 | Four parts in Agentic Process, three or four files per tool, nothing extra |

Version 1 scored 44 against the owner's spec.
Version 2 is not yet scored against this rubric.

## 12. Owner decisions, 16 November 2026

1. **One process.** [`PROCESS.md`](../base/PROCESS.md) is the single process, since the move to
   `projects/` on 16 November 2026. `workshop/plans/plans-template/BUILD-PROCESS.md` stays only as a short pointer
   if other pages still link to it.
2. **Level 3** stays unassigned until real use shows a recurring manual step worth automating.
3. **Artifact Studio** moves to one `SKILL.md` later; it stays in the backlog while this pattern
   is proven.
