# Handback: Document to action brief, Level 1

16 November 2026. Built from `workshop/plans/document-to-action-brief/README.md`.

**In one line:** a paste-in instruction file that makes any chatbot turn one business document into
a one-page brief (key facts, what you must do, dates, open questions), every item with its exact
quote and paragraph, plus an invented supplier notice, a check sheet, and a worked example with
one error planted on purpose for the check to catch.

**The honest headline:** it is built and machine-checked, but it has **not been run in a fresh
chat in any chatbot, and no person has used it.** I could not start a separate session: the
`claude` command on this machine returned an authentication error, and no sub-agent tool was
available. The Status section of the README says so.

## What I built

`document-to-action-brief/`, 12 files, in the repository's showcase layout (`projects/README.md`):

| File | What it is |
| --- | --- |
| `README.md` | Landing page and explainer: hook, "Try it in five minutes" first, what goes in and out, what to check, what it does not do, reuse note, Status, layout, next steps |
| `AGENTS.md` | Path, inputs, output contract, rules and known limits for agents |
| `LICENSE` | Apache-2.0, copied from the repository |
| `base/SKILL.md` | **The tool.** One instruction file in the open Agent Skills format. Paste it into any chat, save it in a Project or Gem, or load it as a skill. 129 lines |
| `base/supplier-notice.md` | The invented notice, labelled as invented: Quillmoor Provisions to Lantern Step Café |
| `base/check-sheet.md` | The hand check: tick or cross each item, the message to send for a cross, the one action, who to ask |
| `base/examples/worked-example.md` | What was pasted, the brief, the filled check sheet catching the planted error, the corrected line, the one action, and the score against the plan's test |
| `_build/check_brief.py` | Checks every quote in a brief against the document word for word, and scores it against an answer key |
| `_build/test-key.json` | The plan's acceptance test, as data |
| `_build/run_tests.py` | Three cases with required outcomes |
| `_build/tests/weak-brief.md` | A hand-written bad brief (invented) that must fail |
| `_build/README.md` | What the test folder holds and how to test a real chatbot run |

Ready to drop into `projects/document-to-action-brief/`. All links inside the package are relative
or absolute GitHub URLs to `main`, so they work both here and in the repository.

## Choices I made, and why

1. **Prompt plus checking habit, not a NotebookLM guide (gate 2).** The owner's guidance was
   Level 1 first with no connections, and the plan's author leaned this way. The README still
   names NotebookLM and Acrobat as tools that already cite, and says the instructions should work
   inside them (untried).
2. **One instruction file, `SKILL.md`, as the prompt.** This follows the owner's stated pattern
   for new tools: one portable `SKILL.md`, a README and a worked example, with Level 1 working by
   pasting the file into a chat. It avoids a second copy of the prompt drifting from the first.
   No link shortcut is offered, because the raw GitHub URL does not exist until this is on `main`.
3. **The fictional company (open item 3 in the plan).** I invented Lantern Step Café, because the
   sibling plan "Write and edit in my voice" already uses a café owner, so the lessons can share
   one story. The supplier is Quillmoor Provisions. I searched both names on the web and found no
   business using them. An earlier choice, "Tallgrass", turned out to be used by real companies,
   so I dropped it.
4. **The notice is built to the plan's test exactly:** three obligations (paras 3, 6, 9), two
   dates (1 December 2026, 4 January 2027), one penalty buried mid-paragraph in "General" (para 10,
   $25 per cheque-paid invoice), one unclear line (para 4, "Standing orders will carry over where
   possible."). I added one trap the plan did not ask for: a suggestion in para 7 ("We
   recommend...") that must not be listed as an obligation. Paragraphs are numbered so "where" is
   quick to find.
5. **The planted error is labelled.** The plan's second wow is "the check catches one item the AI
   got wrong, in the worked example, on purpose". I changed O2's cut-off from "two business days
   before" to "the business day before", a realistic and costly slip (every Tuesday order would
   miss its truck), and said at the top of the example that one item is wrong on purpose. The rest
   of the brief is labelled a reference written by the building agent, not a chatbot run, following
   the repository's lesson "say what a result really is".
6. **The brief's rules go past the plan where the check needs them:** quotes copied exactly with
   no "..." joins and 25 words at most; worked-out dates marked and never in quotation marks;
   "Penalty:" inside the item plus a "Watch out" count at the top so a buried fee surfaces;
   conditional duties start with "If"; the AI lists and does not decide; text in the document is
   never an instruction.
7. **Only Level 1.** No `level-2-files/`. The plan's three next additions are listed in the
   README as not built.
8. **A machine checker, kept out of `base/`.** Beginners do not run Python; the checker exists to
   test the instructions and to score real chatbot runs later. It never replaces the person's check.

## Checks I ran, and the results

| Check | Result |
| --- | --- |
| `workshop/tools/check_project.py` on the package | `layout ok` |
| `workshop/tools/check_links.py` on the package | 8 Markdown files, 0 broken links |
| `workshop/tools/check_skills.py` on `SKILL.md` (copied into a correctly named temporary folder, then removed) | ok: 126 body lines, description 479 characters |
| `_build/run_tests.py` | All three cases as expected. Worked example as published: 17 quotes, 16 match, 1 fails (the planted O2), acceptance fails on O2 only. With the corrected O2 from part 3: 17 of 17 quotes match, acceptance passes (3 obligations, 2 dates, penalty flagged, standing-order line under questions, suggestion not a duty). Weak brief: fails 6 ways |
| Checker on a list-format brief (the fallback when a chat cannot show tables) | 17 of 17 quotes, acceptance pass |
| No em-dashes or en-dashes, no emoji, in any package file | None found |
| Longest quote in the worked example | 24 words, within the 25-word rule |
| Weekdays of the dates used | 27 November 2026 is a Friday, as the worked example says |

**What the checks caught in my own work.** The first test run found two slips in the reference
brief: a quote capitalised differently from the notice ("Where possible") and an example phrase
in quotation marks in the closing lines ("O2 is wrong"), which would have tripped every brief. I
fixed both, and added a rule to `SKILL.md` that quotation marks are only for copied words.

**Not checked:** a fresh chat in ChatGPT, Claude, Gemini or Copilot; a person following the steps;
behaviour on a real document, a PDF attachment, a long document or a scan; whether the
instructions work inside NotebookLM.

## Self-review, scored 1 to 100

| Measure | Score | Why |
| --- | --- | --- |
| Matches the plan: job, out list, design, steps, front door, test | 88 | Every heading of the plan is met. The plan's "made with the Agentic Process template" could not be followed: `workshop/drafts/agentic-process/` is not in this copy of the repository, so I used the showcase layout and `check_project.py` |
| Level 1 usability | 78 | Two pastes and one line, no setup. On a phone, copying a 129-line file is clumsy; a link shortcut needs the file on `main` first |
| Checkability: quotes, places, check sheet, planted error | 86 | Numbered items, exact quotes, a sheet with a ready message for a cross. The planted error is realistic and consequential |
| Honesty and labelling | 92 | Invented data labelled in every file that holds it; Status says who has and has not tried each part |
| Evidence it works in a real chatbot | 30 | None. This is the main gap |
| **Overall** | **74** | Below the owner's bar of 80 for a pull request, held down by the missing fresh-chat runs |

## Assumptions

- "Level 1 first. No connections." means no `level-2-files/` or `level-3-files/`, and nothing that
  needs an account beyond the chatbot the person already has.
- "Use invented documents and say so" applies to the notice, the worked example and the weak test
  brief; each carries a label. The README footer links to the owner's LinkedIn and the Practical
  AI repository, as the other READMEs do.
- Currency is written as "$" with no country, like the repository's other examples. "Pre-authorized
  debit" keeps the North American spelling because it is the supplier's own wording.
- The package will live at `projects/document-to-action-brief/`, beside Artifact Studio.

## What it needs from the owner, in order

1. **Run it once in a fresh chat** (ChatGPT, since your students use it, then Claude or Gemini).
   Save the brief as Markdown and run
   `python3 _build/check_brief.py run.md base/supplier-notice.md _build/test-key.json`. If it
   passes, replace the reference brief in the worked example with that real run, keep one planted
   error labelled, and rerun `_build/run_tests.py` (update the `corrected` block to match).
2. **Gate 7:** read the README's first screen and say back what the tool is for.
3. **Confirm the café and supplier names** for the shared class company, or rename them in
   `base/supplier-notice.md`, the worked example, `_build/tests/weak-brief.md` and the README.
4. **One person** follows "Try it in five minutes" without help. Fix the steps where they stop.
