# Document to action brief: for agents

A person has a document to act on (a notice, contract, tender, policy, report, bill or official
letter) and wants to know what it asks of them, by when, and where it says so. People start at the
[README](README.md).

## To brief a document

Load [`base/SKILL.md`](base/SKILL.md) as a skill, or read it as your instructions. It is the whole
procedure and the output shape. If the person has a house rules file
([template](level-2-files/house-rules.md)), read it first and follow it.

## Rules that never bend

1. Use only the document. Never invent a date, an amount, a name or the contents of a missing
   attachment.
2. A row without exact words from the document is an open question, not a fact or an action.
3. No legal, tax or financial advice, and no recommendation. The brief lists; the person decides.
4. Never send, sign, accept, pay or reply. A person does.

## To change or test it

| Change | Then |
| --- | --- |
| `base/SKILL.md` | Keep `base/try-it-prompt.txt` in step with it |
| Either one | Re-run the tests in fresh sessions: each folder in [`quality-results/`](quality-results/README.md) holds the exact message. Check every reply with `python3 _build/check_quotes.py reply.md document.txt`, and grade notice A against [`base/examples/answer-key.md`](base/examples/answer-key.md) |
| Anything tested | Update the results table and the README status, with the date and who ran it |

Practice documents are in [`base/examples/`](base/examples/). Level 3 is a design, not built:
[`level-3-files/`](level-3-files/).
