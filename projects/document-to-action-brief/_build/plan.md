# Plan: Document to action brief

## Reassessed 17 November 2026: now project 3

The owner chose this as project 3, which answers gate 2: it is worth a project of its own. What
changed from the plan below, after a fresh check of what exists:

- **Level 1 is the business person.** Owners, managers and leaders who must act on a document they
  did not write. The classroom framing below is dropped.
- **The output fits the situation.** Six kinds of document (a contract before signing, a change of
  terms, a policy update, a tender, a report, a bill or official letter) each add one section, and
  the reader (me, my boss, my team) changes the top.
- **Try it is one paste.** The instructions and an invented notice in a single prompt, so a visitor
  sees a result before using their own document.
- **Level 2 saves it.** The same `SKILL.md` installs as a skill in Claude and in ChatGPT, which
  adopted the open Agent Skills format, plus a house rules file.
- **Level 3 is designed, not built:** scheduled watching of an inbox label or folder, an
  obligations register with owners, a review lane for anything unclear or costly, drafted
  reminders, and corrections fed to the learnings database. See `level-3-files/`.
- **What it is not:** contract risk review. Anthropic's open-source Legal plugin and contract tools
  such as Ironclad serve legal teams; Copilot in Word, NotebookLM and Acrobat summarise with
  citations. None gives a business person this fixed, checkable brief with the habit of checking.
- **The fictional company** (gate 3) is the invented Tallowmere Café, already used by the pilot.

The plan as written on 16 November 2026 follows, unchanged.


Written on 16 November 2026 by following [Agentic Process](../../../projects/agentic-process/),
steps 1 to 6, with the one-page plan from its template. Steps 2 to 4 were searched on the web on
that date. **The owner has not yet answered the gates;** each is marked open where it needs him.

**Think of it as:** a highlighter and a sticky note. The AI underlines what the document makes
you do, and you check every underline against the page before you act on it.

**North Star:** a business owner or employee turns a supplier notice or a business report into
the facts, obligations, dates and questions they need, and can point to the line each one came
from, in one sitting, with the chatbot they already use.

| Heading | Write here |
| --- | --- |
| The job | Turn one business document (a supplier notice, a contract change, a report) into a one-page brief: key facts, obligations, dates and open questions, each with the words it came from and where |
| The user | A business owner or employee who has to act on a document they did not write. In class: a learner with a fictional notice |
| What is out | Several documents at once. Legal advice. Deciding what to do: the brief lists, the person decides. Sending anything. Scanned images with no text layer |
| The wow | Every item carries a short quote and its place, and the learner finds each one on the page in seconds. The second wow: the check catches one item the AI got wrong, in the worked example, on purpose |
| What already exists | NotebookLM and Acrobat's AI Assistant both link each answer to the passage it came from; Claude's API has a citations feature for developers. None of them produces this brief's fixed shape or teaches the checking routine. See "Step 2" below |
| Build or buy | Build a prompt, a fictional notice and a worked example. Buy nothing. Do by hand: the check against the page, and the decision |
| Cost | Nothing new: any chatbot that accepts pasted text or an attached file. A free NotebookLM account is the optional upgrade for linked citations |
| The design | One paste-in prompt and the document. The brief comes back as four short lists with quotes. The learner checks each quote against the document, ticks or crosses it, and writes down the one action they will take |
| The folder layout | The showcase layout: `projects/document-to-action-brief/` made with the Agentic Process template, `base/` holds the prompt, the fictional notice, the worked example and the check sheet |
| The steps | 1. Paste the prompt. 2. Paste or attach the document. 3. Read the four lists. 4. Find each quote in the document and tick or cross it. 5. Write the one action, with its date |
| The front door | "Your supplier just changed the terms. What do you actually have to do, and by when?" and one prompt to try on the fictional notice in five minutes |
| The test | The fictional supplier notice (about one page, with three obligations, two dates, one buried penalty and one ambiguous line). A good result lists all three obligations and both dates with exact quotes, flags the penalty, and puts the ambiguous line under questions, not facts |
| Who reviewed it | Nobody yet. Step 7 is open |
| Gates | 1 pass. 2 pass on the author's reading, open for the owner. 3 pass. 4 pass. 5 pass. 6 pass. 7 open. 8 not started. 9 not started |
| Next three additions | 1. Artifact Studio's report layout for the brief, as a one-page page to share. 2. Two documents compared: what changed between the old and new terms. 3. Advanced: a skill that writes the dates to a calendar draft, after a person approves |

## Step 2: what already exists, checked 16 November 2026

| Option | Kind | What it covers | Cost | Limits | Source |
| --- | --- | --- | --- | --- | --- |
| NotebookLM | Built into a free Google product | Answers questions about uploaded documents. Each claim links to the passage it came from | Free tier; paid tiers not confirmed here | No fixed brief shape unless prompted. A Google account is needed | [Google's announcement of inline citations](https://thailand.googleblog.com/2024/06), [a description of how its citations work](https://www.simplilearn.com/what-is-notebooklm-article) |
| Acrobat AI Assistant | A paid add-on to a common PDF tool | Summaries and answers about a PDF, with numbered links that highlight the source text | Not confirmed | Mostly PDF and Office files. A paid plan is likely needed | [Adobe's learning page](https://experienceleague.adobe.com/en/docs/document-cloud-learn/acrobat-learning/get-started/ai/ai-assistant), [Adobe's summary generator page](https://www.adobe.com/acrobat/online/ai-summary-generator.html) |
| Claude API citations | A developer feature | Returns the exact passages that support each claim | Standard token prices; not confirmed for this use | Developers only. Not for a class | [Claude's documentation](https://platform.claude.com/docs/en/build-with-claude/citations) |
| Any chatbot with a good prompt | Built in | Can list facts and quote them if asked | What the learner already pays | Quotes are not checked by the tool: the learner must check them | Common practice |
| Established practice | Practice | Read with a highlighter, list what you must do and by when, ask about what is unclear | Free | Slow on long documents | Common practice |

**Lean for the Beginner level: wrap.** The citing tools exist. What is missing is the brief's
fixed shape, a fictional document built to test it, and the habit of checking each item. That
is a prompt, a document and a worked example, which works in NotebookLM, Acrobat or any chatbot.

## Steps 3 to 6, in one line each

- **3, outside help:** nothing to buy for the first version. Advanced options (a calendar
  connector) are listed under "Next" and not chosen.
- **4, cost:** nothing new. The free NotebookLM tier is optional.
- **5, simplest design:** one prompt, one document, one check sheet. The layout above is fixed.
- **6, plan and front door:** this page, and the front door line above.

## For the owner: the gates that need you

1. **Gate 2:** is a prompt plus a checking habit enough of a tool, given that NotebookLM already
   cites? The author's view is yes, because the lesson is the habit. If not, this becomes a guide
   to NotebookLM.
2. **Gate 7:** read this page, or give it to a new chat with the review prompt from step 7, and
   say back what it is for.
3. **The fictional company:** the priorities say to use one fictional company across all class
   exercises. Name it, or say "invent one".
