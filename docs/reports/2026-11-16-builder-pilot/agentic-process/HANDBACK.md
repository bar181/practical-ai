# Hand-back: Document to action brief

Built 16 November 2026 by following the Agentic Process builder skill
(`workshop/drafts/agentic-process/builder/agentic-process/SKILL.md`) on the plan in
`workshop/plans/document-to-action-brief/README.md`. Package: `document-to-action-brief/`, four
files.

## Read first

1. **The plan is not approved.** Its gates 2 and 7 are open with the owner. Built anyway, as the
   builder skill says.
2. **No fresh-session check has been run.** The build environment had no sub-agent tool, and the
   `claude` command line returned an authentication error when started as a separate session. As
   the builder skill requires, every behaviour check says **not yet run**, and `example.md` holds
   the message and an answer key but **no chatbot result**. I did not write one myself and present
   it as a result.
3. **The fictional company was invented, not chosen by the owner:** Tallowmere Café (customer) and
   Kestrel Fold Wholesale Ltd (supplier). A web search on 16 November 2026 found no business by
   either name. The plans for meeting notes and write-in-my-voice expect the same company, and
   the voice plan expects a café, so a café was chosen. Rename freely: the names appear in
   `practice-notices.md`, `example.md`, `SKILL.md` (one example line) and `README.md`.

## What was built

| File | What it is |
| --- | --- |
| `README.md` | The explainer: front door line, 5-minute try-it, what to give, what you get, what to check, Level 2, the check table |
| `SKILL.md` | The tool. Paste it into any chatbot with one document; returns the brief. Asks once if the document is missing or unreadable |
| `example.md` | The worked example's message, the answer key for notice A (every quote matched against the notice), one row with a mistake planted on purpose to practise the check, and an empty, labelled slot for the unedited result |
| `practice-notices.md` | Two invented notices. A: the normal case (one page, three obligations, two action dates, one buried penalty, one ambiguous line). B: the exception (no date, a missing price schedule, a clause in another agreement) |

The brief has four tables, in the order the reader uses them: what you must do, dates, open
questions, key facts. Each row has the exact words, where they are, and an empty ✓ or ✗ column.
Above them: a two-sentence summary that must name every penalty, and a warning when something is
missing. Below them: the check steps, the document's first and last words (to catch a paste that
was cut off), and a blank line for the person's one action.

## The usable result, U1 to U5

| ID | Line | Check | Result, who ran it |
| --- | --- | --- | --- |
| U1 | A business owner or employee who has to act on a document they did not write; in class, a learner with an invented notice | Someone other than the author reads the README and says what it is for and what to paste | Not yet run |
| U2 | They give one document as text (pasted or a readable file), optionally who they are in it and when they received it | `SKILL.md` plus "Here's the notice from our supplier. What do I need to do?" with no document: asks once, writes no brief, waits | Not yet run |
| U3 | A one-page brief: obligations, dates, open questions, key facts, each with exact words and where | Notice A, graded against the answer key in `example.md`: three actions, both dates, the $35 penalty in the summary, the standard-plan line under questions, every quote found with Find | Not yet run |
| U4 | Recipient test: they can find every row on the page in seconds and act without rewriting | First screen only: earliest date and penalty visible? Then time the search for each quote | Not yet run |
| U5 | The document leaves out what you need to act: no date, a missing attachment | Notice B: warning at the top, "30 days after the date of this letter" marked cannot be worked out, no prices made up, the missing pieces under open questions with who could answer | Not yet run |
| | Works in a second chatbot | Same file and notice A in ChatGPT or Gemini | Not yet run |

**Checks the builder did run, on the files (not on the tool's behaviour):**

| Check | Result |
| --- | --- |
| Every answer-key quote is in notice A, character for character (Python string match) | Pass: all 9 key quotes found. The 10th quoted phrase, the "fails if" wrong reading, is correctly absent |
| The planted-mistake quote is not in notice A | Pass: absent |
| Notice A has exactly two action dates plus the letter date; notice B has no date | Pass: 20 November 2026, 1 December 2026, letter dated 3 November 2026; notice B has none |
| Notice A is about a page | 320 words. Notice B: 116 words |
| `workshop/tools/check_skills.py` on the output folder | Pass: name matches folder, description 521 characters, body 127 lines, no problems |
| `workshop/tools/check_links.py` on the package | Pass: 4 Markdown files, 0 broken links (anchors are not checked by the script; I checked the two by eye) |
| `workshop/tools/check_project.py` on the package | **Fails, expected:** it tests the `projects/` showcase layout (AGENTS.md, LICENSE, `base/`, a North Star line). The package follows the Agentic Process tool layout instead; see "Differences from the plan" |
| No em dashes or en dashes in any file | Pass: 0 in all four |

**To run the real checks** (about 20 minutes, any Claude chat with nothing else loaded): one new chat
per case, each with all of `SKILL.md` pasted, then (1) the U2 message, (2) notice A with its
suggested message, (3) notice B with its suggested message. Paste case 2's reply unedited into
`example.md` below the line, grade it against the answer key, and fill in the README's check
table with the date, the chatbot and what was seen. Then case 2 again in a second chatbot.

## Choices, and why

- **Implementation: a thin `SKILL.md`** (row 2 of the builder's table). The job is repeatable
  instructions and fixed rules; nothing existing does the whole job, and the owner asked for
  Level 1 with no connections.
- **No script.** The one step needing exact behaviour is matching each quote to the page. The
  person does it with Find (Ctrl+F or Cmd+F), which is exact and already on every machine, and the
  plan says the check is done by hand. Date arithmetic is limited to "worked out" dates the
  person is told to check on a calendar; a date that counts from something not in the document is
  marked "cannot be worked out".
- **The brief is the check sheet.** The plan lists a separate check sheet; instead every table has
  an empty ✓ or ✗ column, which keeps the file count down and keeps the check next to the claim.
- **Exact quotes or it is a question.** Any item without word-for-word text moves to open
  questions. This is what makes the checking routine work in any chatbot, since only NotebookLM,
  Acrobat and the Claude API check citations for you.
- **First and last words.** Added to catch the commonest silent failure with pasted text: a
  truncated paste. Not in the plan.
- **Penalties get their own row** placed right after the action they apply to, and must appear in
  the summary, because the plan's test hides one mid-paragraph.
- **The planted mistake** in `example.md` meets the plan's second "wow" (the check catches an item
  the AI got wrong, on purpose) without editing or faking a chatbot result. It is labelled as
  written by the builder.
- **U5 chosen as an incomplete document** (undated, attachment missing) rather than a scanned
  image: both are caught in the Start section, but the incomplete document is the one that
  produces a confident wrong date if the tool fails.

## Differences from the plan

| The plan says | Built | Why |
| --- | --- | --- |
| Showcase layout: `projects/document-to-action-brief/` with `base/` | Agentic Process tool layout: README, SKILL.md, example.md, plus `practice-notices.md` | The builder skill says to copy `template/` and follow its table when a plan asks for more. Moving it into `projects/` later needs AGENTS.md, LICENSE, `base/` and a North Star line (what `check_project.py` reports) |
| Prompt, notice, worked example, check sheet | Check sheet folded into the brief's ✓ or ✗ column | Fewer files, same routine |
| No extra file named | `practice-notices.md`, a fourth file | The front door needs a notice the learner can copy without seeing the answer, and the U5 case needs its own input |
| Worked example is the unedited result | Answer key plus planted mistake; result slot empty | No separate session was available |

## External sources reviewed (16 November 2026)

Nothing was installed or run. No external skill text was copied.

| Source | What I took from it |
| --- | --- |
| Anthropic's legal plugin skill `review-contract`, in `anthropics/knowledge-work-plugins`, as described at [skills.sh](https://skills.sh/anthropics/knowledge-work-plugins/review-contract). Version and licence not stated on that page | Reviews a contract against an organisation's negotiation playbook: deviations, redlines, business impact. A different job (negotiation, not acting on a notice) and needs a playbook. Not reused |
| Anthropic's `small-business` plugin skill `contract-review`, from its description in this environment | Lightweight NDA, MSA and vendor contract review with a redline DOCX. Again risk review, and a plugin, so not Level 1 in any chatbot. Not reused |
| [Google's help page "Use chat in NotebookLM"](https://support.google.com/notebooklm/answer/16179559?hl=en) | Confirms answers carry citations you can open in context. The fetched page now describes "Gemini Notebook", so the product name may have changed; worth rechecking before class. Kept as an optional, untested upgrade in the README |
| The plan's own step 2 (NotebookLM, Acrobat AI Assistant, Claude API citations) | Not re-verified beyond the NotebookLM page above |
| Anthropic's `skill-creator` skill (loaded in this session) | Borrowed: a description that names the phrases people use ("what do I have to do", "what are the deadlines"), and explaining the reason behind each rule rather than shouting it. Its fallback of running tests yourself was not used, because the builder skill forbids self-written results |

## Assumptions

- "Level 1 first. No connections" means: no Level 3 and no calendar step; Level 2 (save as a skill
  or Project) stays as the README's usual short section because it needs no connection.
- Currency is written as plain "$" with no country, and no law is referred to, so the notices
  work in Canada or elsewhere.
- The tool lives in a folder whose final place in the repository is not decided, so the README
  names the plan by path instead of linking to it.
- `.example` email addresses are used so no invented address can reach a real inbox.

## What a person decides next

1. Answer the plan's gates 2 and 7, and keep or rename the invented company.
2. Run the three cases and the second-chatbot check above, and put the case 2 result into
   `example.md`.
3. Choose where the package lives: `workshop/drafts/agentic-process/examples/`, or `projects/`
   (which needs the showcase files listed above).

## Possibly worth remembering

From this build, not from memory: the `claude` command line could not authenticate as a child
session in this environment, so builder runs here cannot do their own fresh-session checks.
