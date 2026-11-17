# Hand-back: document-to-action-brief

Built in `/tmp/start/ap/out/document-to-action-brief/`: `README.md`, `SKILL.md`, `example.md`.

## Assumptions (read first)

1. **The checks have not been run.** The builder ran as a sub-agent with no way to start a separate
   session, so every check below says "not yet run" and `example.md` holds the input but no result.
   It is not ready until someone runs the three messages below in fresh chats.
2. **The catch (U5) was chosen by the builder.** The request gave no catch. I took the most
   costly hand mistake for this job: a deadline counted from a date the notice never gives
   (an undated letter, an unstated "Effective Date"), together with a mentioned enclosure that is
   not included.
3. "Supplier notice" also covers a landlord or service provider changing terms; the tool is
   written for a café owner but nothing in it is café-specific.
4. Deadlines counted in days are calendar days unless the notice says business days.
5. Silence that counts as agreement ("if we do not hear from you") is treated as an action.
6. All notices and names are invented.

## The usable result, each line with its check

| ID | Line | Check | Result | Who ran it |
| --- | --- | --- | --- | --- |
| U1 | A café owner, in the chatbot they already use; not a lawyer | Normal case in a plain chat with only `SKILL.md`; no unexplained legal terms | not yet run | nobody yet |
| U2 | One supplier notice: pasted text, a file or a photo | Message C (no notice): asks once, waits | not yet run | nobody yet |
| U3 | What they must do and by when, what changes, what is missing, each with the notice's words | Message A: 4 actions (return form by Mon 30 Nov 2026; reply in writing by Tue 15 Dec 2026 if they object; order by 11:00 am the day before from 4 Jan 2027; return crates by next delivery from 4 Jan 2027) and the price, payment-term and minimum-order changes, each quoted | not yet run | nobody yet |
| U4 | The first screen alone tells them the earliest deadline and first action | Read only the first screen of Message A's result as the owner; would they act on it as it is? | not yet run | nobody yet |
| U5 | A deadline counted from a date the notice never gives | Message B: "undated" flagged at the top, both deadlines "Cannot set", missing "overleaf" schedule flagged, no guessed date, says to ask Sam Reyes / orders@greenbank.example | not yet run | nobody yet |

## The messages to run, each in a new chat

Each message is: the whole of `SKILL.md`, copied as it is, then a blank line, then the quoted block
from `example.md`, without the leading `> `.

- **Message A (normal case, U1, U3, U4):** `SKILL.md` + the Harbourline Dairy block under "The
  message". Save the reply, unedited, below the first line in `example.md` in place of "Not yet
  run.", and fill in the date and chatbot.
- **Message B (the catch, U5):** `SKILL.md` + the Greenbank Produce block under "Practice notices".
- **Message C (missing input, U2):** `SKILL.md` + "My veg supplier sent a letter about new terms.
  What do I have to do and when?"
- **Second chatbot:** Message A in a different chatbot.

Record each result in the README's "How it was checked" table, with who ran it and what they saw.

## Implementation choice

A thin `SKILL.md` (row 2 of the table). The job is repeatable reading instructions plus local
rules. Date arithmetic is the one step that needs exact behaviour (row 3), but the owner works in
a plain chatbot where a script will not run, so the skill makes the chatbot show every sum
("9 Nov 2026 + 21 days = Mon 30 Nov 2026") and lists them for checking instead. If checks show
wrong dates, the next step is a formula the owner can paste into a spreadsheet, not a script.

## What already exists (checked 16 November 2026)

- **Anthropic: `small-business:contract-review`** (installed plugin skill in this session; listing
  read, not run). Reviews NDAs, MSAs and vendor contracts, flags non-standard terms and produces a
  DOCX redline. It answers "what am I signing", not "what must I do and by when"; no deadline
  table, no silence-means-agreement rule. Does not do the whole job.
- **Contract Obligation Extraction**, Happy-Technologies-LLC, from the `ThomasMoreAI/legal-skills-open`
  repository, listed at https://claudskills.com/skills/contract-obligation-extraction/ ; no version
  number, last updated 2026-06-06, Apache-2.0. Single `SKILL.md`; the registry page does not show
  its inputs, outputs or tool use, and I did not read the `SKILL.md` itself. Aimed at developers and
  contract work, not a café owner. Nothing copied from it.
- **Commercial obligation-tracking tools** (Sirion, Aavenir, Juro AI Extract and similar, found by
  web search): enterprise contract-lifecycle products, priced and set up for legal teams. Too heavy
  for a few notices a year.
- **`anthropic-skills:skill-creator`** was opened as the builder asks (step 3). Its evals
  workspace, baselines and viewer were not used, because the builder's rules say no extra files;
  only its writing advice (explain the why, a clear trigger description) was used.

## What a person decides next

1. Run Messages A, B and C in fresh chats and record the results; fix and rerun at most twice.
2. Whether the U5 catch I chose is the one that matters to the café owner.
3. Whether to publish the tool. Nothing has been merged, published or sent.
