# Document to action brief: what does this notice make you do, and by when?

<h3 align="center">Your supplier just changed the terms. What do you actually have to do, and by when?</h3>

**Document to action brief turns one business document into a one-page list of key facts, what
you must do, the dates and the open questions.** Every item carries the exact words it came from
and where they are, so you can find each one on the page in seconds before you act. It works in
the chatbot you already use: ChatGPT, Claude, Gemini, Microsoft Copilot or any other that accepts
pasted text or an attached file. Free. Nothing to install. No connections.

**Think of it as** a highlighter and a sticky note. The AI underlines what the document makes you
do. You check every underline against the page before you act on it.

**North Star:** a business owner or employee turns a supplier notice or a business report into the
facts, obligations, dates and questions they need, and can point to the line each one came from,
in one sitting, with the chatbot they already use.

## Try it in five minutes

The notice is invented, so there is nothing to prepare and nothing private to paste.

1. **Paste the instructions.** Open [`base/SKILL.md`](base/SKILL.md), copy all of it, and paste it
   into a new chat. The chatbot asks for your document.
2. **Paste the document.** Open [`base/supplier-notice.md`](base/supplier-notice.md), an invented
   notice from a food supplier to a café. Copy it from "QUILLMOOR PROVISIONS" down, paste it, and
   add one line: `I own the café. Make the brief.`
3. **Read the "Watch out" line first.** It counts the penalties, the things you must do, the dates
   and the open questions.
4. **Check every item.** Use the [check sheet](base/check-sheet.md). For each item, find its quote
   at the place it gives. Tick it or cross it. If you cross one, tell the chat its number.
5. **Write your one action, with its date.** The brief lists. You decide.

Then open the [worked example](base/examples/worked-example.md). It shows a finished brief for
the same notice, the check filled in, and **one item that is wrong on purpose**, so you can see what
the check catches. Try to find it before you read the answer.

### Use it on your own document

Same steps, with your own document in step 2: a supplier notice, a change to a contract or a
policy, a lease renewal letter, a report you have to act on. One document per chat.

- **Check what you may paste.** If the document is confidential, use only a chatbot your business
  has approved for it, or remove names and account numbers first.
- **A long file?** Attach it instead of pasting. It must have real text in it: a photo or a scan
  may be misread, and the instructions tell the chatbot to say so.
- **The brief is wrong somewhere?** That is what the check is for. Tell the chat the item number
  and what the page says.

### Keep it for next time

Paste [`base/SKILL.md`](base/SKILL.md) once into the instructions of a Project (Claude, ChatGPT), a
Gem (Gemini) or a custom assistant. After that, start a chat in it and paste the document. If your
assistant loads skills, put `SKILL.md` in a folder named `document-to-action-brief` and add that
folder as a skill. Nothing is connected either way.

### If you are an AI agent

Follow [`AGENTS.md`](AGENTS.md).

## What goes in, what comes out

| Goes in | Comes out |
| --- | --- |
| One document as pasted text or a file with real text | A title line and a "Watch out" count |
| Optional: who you are in it ("I am the customer") | **Key facts**, six at most, suggestions marked "not required" |
| | **What you must do**, every obligation, with its deadline and any **Penalty** inside it |
| | **Dates**, every deadline and every date something starts or changes |
| | **Open questions**, every unclear line that affects what you must do, with why it is unclear |
| | Each item numbered (F1, O1, D1, Q1), with its exact quote and where it is |

A line from the worked example:

| # | You must | By | Quote | Where |
| --- | --- | --- | --- | --- |
| O1 | Confirm your delivery window, 7 to 9 a.m. or 9 to 11 a.m., in the customer portal | 1 December 2026 | "You must confirm your preferred delivery window (7 to 9 a.m. or 9 to 11 a.m.) in the customer portal by 1 December 2026." | para 3 |

## What to check

The AI drafts. You check every item against the page before you act. That is the tool.

| Check | Why |
| --- | --- |
| The quote is at the place given, in the same words and numbers | A chatbot can paraphrase inside quotation marks, or change one number. The worked example shows a cut-off moved by a day |
| The item says what the quote says | A true quote can still be summarised wrongly |
| Nothing is missing | Skim once more for "must", "fee", "charge" and every date. Penalties hide in the "General" paragraph |
| Unclear lines are questions, not facts | "Where possible" is not a promise. Ask the sender |

Then write the one action you will take first, and its date, and who you will ask about each open
question. You ask them; the chatbot sends nothing.

## What it does not do

- Several documents at once, or comparing an old version with a new one. One document per brief.
- Legal, tax or financial advice. It reads one document, not the agreement behind it.
- Decide for you. It lists; you choose the action.
- Send, sign, reply or put anything in a calendar.
- Read scanned images reliably. It asks for a text version instead.

## Why not just use a tool that already cites?

Some tools already link each answer to its passage. As recorded in the plan for this tool
(`workshop/plans/document-to-action-brief/`) on 16 November 2026: NotebookLM links each claim to the passage it came from, on a free tier with a
Google account; Acrobat's AI Assistant does the same for PDFs on a paid plan; Claude's API has a
citations feature for developers. None of them gives this brief's fixed shape, flags penalties
and unclear lines on purpose, or builds the habit of checking. The instructions here should work
inside those tools too, as the prompt; that has **not been tried**.

## Status

**Built on 16 November 2026 by an AI agent, from the plan. Nobody has used it yet.**

| Part | State |
| --- | --- |
| The instructions, [`SKILL.md`](base/SKILL.md) | Written and checked against the plan's test by the agent that wrote them. **Not yet run** in a fresh chat in ChatGPT, Claude, Gemini or any other assistant. **No person** has used them |
| The invented notice | Built to the plan's test: three obligations, two dates, one buried penalty, one unclear line, plus one suggestion that is not an obligation |
| The worked example | A reference brief written by the building agent following `SKILL.md`, with one error planted by hand and labelled. Not a recorded chatbot run |
| The test | [`_build/run_tests.py`](_build/run_tests.py) checks every quote in the worked example against the notice word for word and scores it against the plan's test. It passes all three cases. It tests the reference, not a live chatbot |
| The check sheet | Written. **Not yet tried** by a person |

Until someone runs it, the worked example is what a good brief should look like, not proof that
your chatbot will produce one. Try it and tell us what you find.

## How it is laid out

`base/` is all you need.

```
document-to-action-brief/
  README.md                this page
  AGENTS.md                instructions for AI agents
  LICENSE                  Apache-2.0
  base/
    SKILL.md               the instructions: paste into any chat, save in a Project, or load as a skill
    supplier-notice.md     the invented notice to practise on
    check-sheet.md         the check you do by hand, and your one action
    examples/
      worked-example.md    a finished brief, the check filled in, and one planted error
  _build/                  the test: a quote checker, the answer key and a weak brief. You do not need it
```

## What comes next

Not built. Each waits until this level is in use.

1. The brief as a one-page report to share, with [Artifact Studio](https://github.com/bar181/practical-ai/tree/main/projects/artifact-studio).
2. Two documents compared: what changed between the old and the new terms.
3. Advanced: a skill that writes the dates to a calendar draft, after a person approves.

Part of [Practical AI](https://github.com/bar181/practical-ai), a free set of tools for the jobs you
repeat. **More information, training or feedback:** [linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)

Free to use, change and share under Apache-2.0. Every company, person and figure in the notice and
the example is invented. The times on this page are estimates, not measurements.
