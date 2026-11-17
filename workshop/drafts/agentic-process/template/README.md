# [Tool name]

[What you give it and what you get back, in one or two sentences.]

**Status, [date].** [Who has run it, where, and on what. "Written" is not "run".]

## Try it: paste one file (5 minutes)

1. Open [`SKILL.md`](SKILL.md), press **Raw**, and copy all of it.
2. In any chatbot, start a new chat and paste it. On a new line, add your input: *[example]*.
3. If anything is missing, it replies once with what to give it.

**Shortcut:** if your chatbot can open links, send *"Follow the instructions at [the Raw link to
SKILL.md]. [Your input]"* instead of pasting.

<!-- Reuse-only tool: if an existing skill or plugin does the whole job, replace the steps above
     with: what it is and a link, the platform it needs, the setup steps, and a small example.
     If this tool wraps a plugin, add what a person can paste in by hand so Level 1 still works,
     and call it portable only once that path has been run. Then delete SKILL.md. -->

## What to give it

- [Input]
- [Input]

## What you get

[The result, in a sentence or two.] [See the worked example](example.md).

## Check before you act

[The facts or numbers to check, and against what. The decision that stays with you.]

## Save it (Level 2)

- **Claude:** add `SKILL.md` as a skill (in a folder named `tool-name`), or paste it into a
  Project's instructions.
- **ChatGPT** Project or **Gemini** Gem: paste it into the instructions.

<!-- Level 3, only if it removes recurring work: what connects (an MCP server, an endpoint, a
     trigger), what it supplies and receives, and what a person still approves. Otherwise say
     "There is no Level 3" and why in one line. -->

## How it was checked

Each line of the usable-result spec has one check, run in a separate session with only this README
and what it tells you to paste.

| ID | Spec line | Check | Result, who ran it, what they saw |
| --- | --- | --- | --- |
| U1 | [Who uses it] | [How it was checked] | |
| U2 | [What they give it] | An input missing something: asks for it in one reply, and waits | |
| U3 | [What they need to receive] | The normal case | |
| U4 | [What makes it usable] | [The recipient test: would they use or forward it as it is?] | |
| U5 | [One exception that matters] | [The exception case] | |
| | Works in other chatbots | The same file in a second chatbot | |
