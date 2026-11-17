---
name: agentic-process
description: Turns a job someone repeats into a Practical AI tool, a README that explains it, one portable SKILL.md and a worked example, reusing an existing skill or plugin wherever one fits. Use when asked to build, package or turn an idea or spec into a tool.
---

# Agentic Process: the builder

You turn one repeated job into a tool someone can start in minutes. Follow the checklist in
`PROCESS.md` in the Agentic Process folder of the practical-ai repository. If you cannot open it,
these steps are enough.

## Start

You need: **the job** (an idea, a spec or a transcript of someone doing it), **who it is for**,
and **one real or invented input** with what a good result looks like. If any is missing, reply
once with only that list and an example line, then wait. If you cannot ask, take the plainest
reading, carry on, and list your assumptions at the top of the hand-back.

## Steps

1. **Scope.** Write the job in one sentence: who, what goes in, what comes out. One job only. If
   a plan asks for levels or files that `PROCESS.md` does not, follow `PROCESS.md` and list the
   difference in the hand-back. If the plan is not approved, build anyway and say so first.
2. **Reuse check.** Look for something that already does it: Anthropic's skills and plugins
   first, then the platform the person uses, then open source. Record links and dates.
   - **It does the whole job:** write only a README from `template/README.md` in its reuse-only
     form. Name the platform it needs, and say what a person can do by hand where it is missing.
     Stop there.
   - **It does part:** your SKILL.md holds only the business rules and the missing steps, and
     names what it builds on.
   - **Nothing fits:** write the whole SKILL.md.
3. **Write SKILL.md.** If the skill-creator skill is available, use it to draft the skill.
   Otherwise copy `template/SKILL.md`. Either way the file must work when pasted on its own:
   the Start section asks for missing context in one reply, and the output shape is in the file.
   Its `name` matches its folder name.
4. **Make the worked example.** Run the skill on the invented input in a fresh chat. Save the
   result unedited as `example.md`, from `template/example.md`. If you cannot start a fresh
   chat, save the input only, write "Result: not yet run" under it, and say so in the hand-back.
   Never write the result yourself.
5. **Write the README** from `template/README.md`: what it does, the quick start (paste the file,
   add your input; the link as a shortcut), what to give it, what you get, what to check, and
   Level 2. Add Level 3 only if a connection removes recurring work.
6. **Run the short check.** In fresh chats, paste the SKILL.md with: an input that is missing
   something, the example input, and a different input. Record the results in the README's check
   table. Never write "passed" for a
   check that was not run.

## Hand back

One short note: what you built and where; the reuse decision and what it rests on; the check
results; your assumptions; and what a person should decide next. Do not merge, publish or send
anything.

## Rules

- Invent no facts. Examples use invented data and say so.
- Nothing extra: no scripts, test harnesses or folders the tool does not need.
- A person approves anything that is sent, posted, paid, published or merged.
