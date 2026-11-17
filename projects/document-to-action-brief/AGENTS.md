# Document to action brief: instructions for agents

You are here because a person has a document they must act on (a notice, a contract, a tender, a
policy, a report, a bill or an official letter) and wants to know what it asks of them, by when,
and where it says so. People start at the [README](README.md).

## The path

| You can | Do this |
| --- | --- |
| Load skills | Load [`base/SKILL.md`](base/SKILL.md) and follow it. It is the whole procedure |
| Not load skills | Read [`base/SKILL.md`](base/SKILL.md) as your instructions for this conversation |

If the person has a house rules file ([template](level-2-files/house-rules.md)), read it first.

## Output contract

One brief, in the order `SKILL.md` gives: the document line, **In short**, the situation section if
one applies, any **Warning**, then What you must do, Dates, Open questions and Key facts, each row
with exact words and where, then the check and the **Assumed** line.

## Rules that never bend

1. Use only the document. Never invent a date, an amount, a name or the contents of a missing
   attachment.
2. A row without exact words from the document is an open question, not a fact or an action.
3. No legal, tax or financial advice, and no recommendation. The brief lists; the person decides.
4. Never send, sign, accept, pay or reply. A person does.

## Where things are

| You need | Read |
| --- | --- |
| The procedure | [`base/SKILL.md`](base/SKILL.md) |
| The one-paste version for a chatbot | [`base/try-it-prompt.txt`](base/try-it-prompt.txt) |
| Practice documents and the answer key | [`base/examples/`](base/examples/) |
| Saving it, and house rules | [`level-2-files/`](level-2-files/) |
| The hands-off design (not built) | [`level-3-files/`](level-3-files/) |
| What has been tested | [`quality-results/README.md`](quality-results/README.md) |
