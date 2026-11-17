# Document to action brief

Paste a supplier notice, a change of terms or a report into the chatbot you already use, and get a
one-page brief: what you must do, the dates, what is unclear, and the key facts. Each line carries
the exact words it came from and where they are, so you can find it on the page and tick it before
you act. You decide what to do.

**Think of it as** a highlighter and a sticky note. The chatbot underlines what the document makes
you do; you check every underline against the page.

> *Your supplier just changed the terms. What do you actually have to do, and by when?*

**Status, 16 November 2026.** Built from the plan in `workshop/plans/document-to-action-brief/`
by following the Agentic Process builder skill. **Nobody has run it yet,** in any chatbot: the build session
could not start a separate chat, so every check below says "not yet run". The plan's gates 2 and 7
are still open with the owner. The two practice notices and the café are invented.

## Try it: paste one file (5 minutes)

1. Open [`SKILL.md`](SKILL.md), press **Raw**, and copy all of it.
2. In any chatbot, start a new chat and paste it. On a new line, type *"We are the customer,
   Tallowmere Café. Here is the notice from our supplier:"* and paste notice A from
   [`practice-notices.md`](practice-notices.md). For your own document, paste its text or attach
   the file instead.
3. If anything is missing, it replies once with what to give it.
4. Work down the brief with the notice open beside it. Use Find (Ctrl+F or Cmd+F) to search for
   each row's exact words, and write ✓ or ✗ in the last column.
5. Write your one action and its date.

**Shortcut:** if your chatbot can open links, send *"Follow the instructions at [the Raw link to
SKILL.md]. [Your document]"* instead of pasting.

**Your own documents:** paste real documents only into a chatbot your workplace allows for them.
A scan or a photo with no selectable text will not work: copy the text out first.

## What to give it

- **One document**, as text or an attached file the chatbot can read. One at a time.
- **Who you are in it**, such as "we are the customer". Optional: without it, it says what it
  assumed.
- **When you received it**, if the document counts days from that. Optional.

## What you get

- **In short:** how many things the document asks of you, the earliest date, and every penalty.
- A **warning** when something is missing: no date, an attachment not included, text cut off.
- Four tables: **what you must do, dates, open questions, key facts.** Every row has the exact
  words, where they are, and an empty column for your ✓ or ✗. Lines that could be read two ways go
  under open questions, never facts.
- **Check it against the page:** the three steps above, plus the document's first and last words
  so you can confirm the chatbot read all of it.

[The worked example](example.md) has the answer key for notice A, and one row with a mistake
planted on purpose to practise the check on. The unedited chatbot result is not yet run.

## Check before you act

- Every row: its exact words are in the document, at that place, and say what the row says. A row
  you cannot find gets a ✗ and is not acted on.
- The first and last words match your document. If not, the chatbot did not see all of it.
- Any date marked **worked out**: check it on a calendar. Any marked **cannot be worked out**:
  find the missing date before you plan around it.
- Every open question: ask the sender, or whoever can answer, before you rely on either reading.
- What to do stays with you, and so does whether a term is fair or binding. That is a question for
  a lawyer or an accountant, not this brief.

## Save it (Level 2)

Worth it if documents like this arrive every week.

- **Claude:** add `SKILL.md` as a skill (in a folder named `document-to-action-brief`), or paste
  it into a Project's instructions.
- **ChatGPT** Project or **Gemini** Gem: paste it into the instructions.

There is no Level 3: the owner asked for Level 1 first, with no connections. The plan's next
additions (comparing old and new terms, dates to a calendar draft after a person approves) wait
for real use.

**Already using a tool that links answers to the page?** NotebookLM and Acrobat's AI Assistant
both link answers to the passage they came from (see the plan's step 2). Pasting this file into
them as your question may give the same brief with clickable sources. Not yet tried.

## How it was checked

Each line of the usable-result spec has one check, to be run in a separate session with only this
README and what it tells you to paste.

| ID | Spec line | Check | Result, who ran it, what they saw |
| --- | --- | --- | --- |
| U1 | A business owner or employee who has to act on a document they did not write; in class, a learner with an invented notice | Someone other than the author reads this README and says, in one sentence, what the tool is for and what they paste | Not yet run |
| U2 | They give it one document as text, and optionally who they are in it | `SKILL.md` and *"Here's the notice from our supplier. What do I need to do?"* with no document: asks for the document in one reply, writes no brief, and waits | Not yet run |
| U3 | A one-page brief: what you must do, dates, open questions, key facts, each with exact words and where | Notice A: lists the three actions and both dates, flags the $35 penalty in the summary, puts the standard-plan line under open questions, and every quote is found with Find. Graded against [the answer key](example.md#the-answer-key). Its unedited result becomes the worked example | Not yet run |
| U4 | The recipient test: they can find every row on the page in seconds and act on the brief without rewriting it | Read the first screen only, as the owner would: is the earliest date and the penalty there? Then time the search for each row's words | Not yet run |
| U5 | The document leaves out what you need to act: no date, an attachment not included | Notice B: a warning at the top; "30 days after the date of this letter" marked cannot be worked out; no prices made up for the missing schedule; the schedule, the letter's date and clause 9 under open questions, each with who could answer; the "within 14 days of receiving" action kept as an "if" | Not yet run |
| | Works in other chatbots | The same file and notice A in a second chatbot | Not yet run |

The files were checked by the builder (not a fresh chat): every quote in the answer key was matched
by a script against notice A, and `SKILL.md`'s `name` matches this folder. Details are in the
build's hand-back note.
