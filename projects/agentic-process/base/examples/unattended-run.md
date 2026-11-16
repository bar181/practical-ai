# Worked example: an agent working unattended

**Level:** Advanced and Expert. **Made on** 16 November 2026 by a coding agent that had only the
[skill folder](../../level-2-files/agentic-process/), copied into an empty repository it had never
seen. A team lead's one-paragraph idea was its only instruction. Nobody answered its questions,
because nobody was there.

**The idea it was given**

> Build the first version of a tool for our shop. A customer sends a long, often upset email;
> the tool turns it into a short, calm reply draft for the shop owner to edit and send. One user:
> the shop owner, who is not technical and uses ChatGPT. Take it as far as you can without me.
> Do not send anything to anyone.

**What happened, in order**

1. The agent ran steps 1 to 6, searched the web in steps 2 to 4 with dated sources, made the
   project folder from the template, and added a third gate of its own.
2. It left step 7 open, because nobody was there to review the plan, and said so.
3. At step 8 it prepared two test folders and stopped. An orchestrating session started two fresh
   sessions, one for each folder. Each finished and logged 3 blocking points.
4. The agent read both logs, fixed the instructions, ran its gates again, and handed back.

**What it made:** [the project folder](../../_build/runs/unattended/calm-reply/), as the agent
left it. **The test logs:** in that folder's `_build/runs/round-1/`.

Below the line is the agent's hand-back. Only the machine paths were shortened. Nobody has yet
used the tool it made, and the second round of tests was not run.

---

## Handback: Calm Reply, first version (unattended run, 2026-11-16)

Tool folder: `calm-reply/`. Process followed: `.claude/skills/agentic-process/SKILL.md`.
Nothing was sent to anyone. Nothing was committed (the new folder is untracked in git).
Web searches were made in steps 2 to 4 only; every source is listed with its link and the date
checked (2026-11-16) in `calm-reply/base/plan.md`, section "Reuse check".

Where the process stands: steps 1 to 6 done; step 7 gate OPEN (no reviewer available); step 8
done for round 1 (two fresh sessions run by the orchestrator, logs read, instructions fixed),
gate PASS as its check is worded, round 2 not run; step 9 not started.

## Before you start

- Decided: no plan or project folder existed, so start at step 1 and make the folder at step 5.
  The skill says to offer the short path (steps 1, 6, 8); nobody could answer the offer, so all
  nine steps were used.
- Assumed: the lead's brief (steps 2 to 4 searching, step 8 test) means the full nine steps.
- Gate: none at this point.

## Step by step

### Step 1: Scope
- Decided: user = the shop owner (not technical, uses ChatGPT). Job, one sentence: "Turn one long,
  upset customer email into a short, calm reply draft that the shop owner edits and sends." Out:
  sending, inbox or shop-system connections, order lookups, refund or policy decisions, saved
  history, other staff, replies over 120 words. Wow: a "WHAT THEY WANT" line plus visible
  `[needs: ...]` blanks so nothing is promised. Test: the email in `base/examples/example-1-email-only.md`.
- Assumed: the shop is a small online shop (repo README: "Small tools for an online shop"); what it
  sells is unknown, so examples use made-up shops and products.
- Gate "Can you say the job in one sentence?": PASS (the plan's job line is one sentence).

### Step 2: Reuse check
- Decided: searched built in (ChatGPT Free, Projects, Go/Plus, Gemini in Gmail, Shopify Inbox),
  open source (useful-ai-prompts "Escalation Handler", MIT; awesome-chatgpt-prompts, CC0),
  practice (HEARD method), providers (Gorgias, Help Scout). Nothing does the whole job for this user
  at no cost with the shop's rules, so continue; what is left is one paste-in instruction file.
- Assumed: a bare ChatGPT chat does not keep "short, no promises, blanks" from one email to the
  next without instructions (not tested). Zendesk and Outlook Copilot marked "Not checked".
- Gate "After what already exists, is there still something to build?": PASS, with a caveat: the
  thing built is close to "a guide to ChatGPT" (see friction 3).

### Step 3: Outside help
- Decided: listed paid options evenly (ChatGPT Go US$8/month US, Plus US$20/month; Gorgias from
  US$10/month, AI Agent add-on from US$250/month; Help Scout paid plans US$25 and US$45 per
  user/month, AI Drafts US$50 per 100 conversations on legacy plans; Google AI plan prices not
  confirmed; Shopify Inbox AI cost not confirmed). Build the instruction file; buy nothing for v1.
- Assumed: "do not choose" means do not pick a provider; saying "buy nothing for v1" answers the gate.
- Gate "Do you know what you would build and what you would buy?": PASS (answer written in the plan).

### Step 4: Cost
- Decided: one dependency, ChatGPT Free at US$0, limit quoted from OpenAI: "unlimited everyday
  text chats, subject to abuse-prevention safeguards".
- Assumed: US$0 needs no one's acceptance.
- Gate "Does the first version cost nothing, or an amount you accept?": PASS (costs nothing).

### Step 5: Simplest design
- Decided: ChatGPT, any plan; one file `base/AI-INSTRUCTIONS.md` pasted at the start of a chat
  (or into a Project's instructions where available: not confirmed); everything else manual.
  Folder made with `new_project.py calm-reply "Calm Reply"` from the repo root.
- Assumed: the repo root is the right `<where>` (no `projects/` folder exists).
- Gate "Could a beginner draw it?": PASS. Check `python3 _build/checks/gates.py .` passed (output below).

### Step 6: Plan and front door
- Decided: filled `base/plan.md`, README (text picture, hook, "Try it in five minutes" first,
  status), AGENTS.md, and two worked examples, one per kind of request the beginner version
  handles: (1) the email only, (2) the email plus `What I know:` lines. Added a third gate,
  `examples`, with `_build/checks/check_examples.py` (shape of each example, reply body 120 words
  or fewer, no exclamation mark), because the README shows the number 120.
- Assumed: the worked examples, written by me by hand from the instructions, are "references",
  not "examples" in the skill's sense; they are labelled that way.
- Gate "Is the beginner version fully described?": PASS (plan filled; all three gates pass).

### Step 7: Review
- Decided: no person and no fresh session were available to me, so no review was done. Plan's
  "Who reviewed it" says so.
- Assumed: the lead's instruction to reach step 8 outranks "Stop at the gate"; I carried on with
  this gate open (see friction 17).
- Gate "Can someone else explain it back to you?": OPEN.

### Step 8: Build and test
- Decided: the beginner version is `base/AI-INSTRUCTIONS.md`. Two run folders were prepared in
  `_build/runs/round-1/` (a copy of the instructions and `prompt.txt` each). The orchestrator ran
  one fresh session per folder with my instruction. I read both `friction.md` files before their
  `result.md`, then fixed in `base/AI-INSTRUCTIONS.md` every point that appeared in both logs
  and each blocking point that showed a real gap (details in "Test results, round 1"). I also
  removed one line from worked example 1 that broke the new "asks" rule, and updated the status
  rows in README and plan. Run folders not edited. Round 2 not run, as instructed.
- Assumed: "a copy of the instructions" meant `base/AI-INSTRUCTIONS.md`. A fix counts as done
  when it is written, though no session has tried the fixed text yet.
- Gate "Did a fresh session finish the job, and have you read what it tripped on?": PASS as the
  check is worded (both sessions finished; both logs read; recurring points fixed). Not yet shown
  that the fixes work: that needs round 2. Gates after the fixes: all three pass (output below).

### Step 9: Grow
- Not started: the level below has not been used by anyone. Gate: OPEN.

## The fresh-session test (round 1 was run by the orchestrator)

Run folders:
- `calm-reply/_build/runs/round-1/email-only-broken-teapot/`
- `calm-reply/_build/runs/round-1/email-with-facts-wrong-size/`

Instruction to give a fresh session (one session per folder, replace `<RUN FOLDER>`):

> You have no memory of this project. Use only the folder `<RUN FOLDER>`. Read `AI-INSTRUCTIONS.md`
> and follow it exactly, treating the text of `prompt.txt` as the message the shop owner sent you.
> Do not ask anyone anything: wherever you would ask, decide, and say so in your note. Write three
> files into the same folder: `result.md` (your answer, exactly as the instructions say to hand it
> over), `note.md` (a short hand-over note: what you did and where you would have asked), and
> `friction.md` (every place you had to guess, quoted from the instructions, numbered, and marked
> BLOCKING if a different guess would change the result or MINOR otherwise). Do not read or change
> anything outside that folder. Do not send anything to anyone.

Round 1 has been run with this instruction. For round 2, make `_build/runs/round-2/` the same
way with the current `base/AI-INSTRUCTIONS.md` (the copies in round-1 are the old text and must
stay as they are).

## Test results, round 1

Both sessions finished and wrote `result.md`, `note.md` and `friction.md`. Both logs ended
"Blocking: 3." Read `friction.md` first in each folder, then the result. Neither result broke a
rule of the instructions as they stood: no invented facts, no unmade promise, reply bodies of
117 (A) and 109 (B) words as the sessions counted them, the four-part note present. Session B's
note reports a process slip: it briefly wrote `/tmp/body.txt` outside its folder, then deleted
it. That is a breach of the test instruction, not of the tool.

A = `email-only-broken-teapot`, B = `email-with-facts-wrong-size`.

**Blocking points, both logs, and what changed in `base/AI-INSTRUCTIONS.md`**

| Log, # | The point (short) | Also in the other log? | What I changed |
| --- | --- | --- | --- |
| A1 | Does a small cut count as "an injury"? | No | Fixed as a real gap: "any injury (however small, a cut counts)". |
| A2 | Is the 28th (a family visit) a "deadline"? | Yes, B9 (minor) | Fixed: a date by which the customer expects the shop to answer or act goes in "Check before sharing"; a date by which they need the item is part of the ask and is handled in the reply. |
| A3 | Should the reply accept the shop's fault for the packing? | Yes, B4 (minor, apology scope) | Fixed: admit fault plainly only when `What I know:` says it was the shop's mistake; otherwise neither admit nor deny. In a serious case never admit fault; leave it to the owner. |
| B1 | Is "I don't want to queue at the post office" an ask or venting? | Yes, A6 (minor, implied asks) | Fixed: defined an ask (something the customer asks the shop to do or answer); conditions belong to their ask; complaints, venting and rhetorical questions are acknowledged in the opening and get no blank. |
| B2 | Is repeating the owner's restock date a "date promise"? | No | Fixed as a real gap: a promise is what the shop commits to do; facts the owner gave, dates included, may be repeated as facts with the owner's limits. |
| B3 | Offer an option that does not meet the customer's condition, or steer? | No | Fixed as a real gap: offer all the owner's options in the owner's order without steering, and say plainly beside an option if it does not meet the ask. |

**Minor points in both logs, also fixed**

| Logs | The point | What I changed |
| --- | --- | --- |
| A4, B7 | Do blanks and list numbers count toward 120 words? | Count every word between the greeting line and "Kind regards,", blanks and list numbers included (matches `check_examples.py`). |
| A5, B5 | Exact greeting form | "Hello <first name>," or "Hello,". |
| A9, B10 | Layout of the "Missing" lines | "Missing:" then each blank exactly as in the draft, one per line; or "Missing: Nothing". |

**Single-log minor points changed anyway, because the fix was one line:** A8 (next step when
nothing is decided: "I will reply by [needs: day]."), B6 (shop name under the owner's name).
**Not changed:** A7 (order number as a personal detail), A10 (non-risky points in "Check before
sharing"), A11 (labelled lines instead of prose), B8 (whether the code fence is part of the shape).
These are worth watching in round 2.

**Knock-on change:** worked example 1 gave a blank to "Is anyone actually running this
business?", which the new rule calls rhetorical. I removed that line and its "Missing" entry
(reply body now 93 words, checked by the `examples` gate).

## Every command, with its output

Reading only (outputs were the file contents, not repeated here):
`ls -la the repository .claude/skills/agentic-process/ && cat .../SKILL.md`;
`cat README.md && git log --oneline | head && git status && cat .../new_project.py && find .../template -type f | sort`
(git: `a65f030 start`, "nothing to commit, working tree clean");
`for f in $(find . -type f | sort); do cat "$f"; done` in the template folder.

1. The skill's step 5 command, then its check in both forms (from `the repository`):

```
$ python3 .claude/skills/agentic-process/new_project.py calm-reply "Calm Reply"
Made calm-reply
Check it now:  python3 calm-reply/_build/checks/gates.py calm-reply
Next: fill in base/plan.md, then write the README's first screen.
exit=0
$ python3 calm-reply/_build/checks/gates.py calm-reply
pass    layout     0.0s  The folder follows the showcase layout
pass    links      0.0s  No Markdown link in this project is broken

All gates that ran passed.
exit=0
$ cd calm-reply && python3 _build/checks/gates.py .
pass    layout     0.0s  The folder follows the showcase layout
pass    links      0.0s  No Markdown link in this project is broken

All gates that ran passed.
exit=0
```

2. Added the `examples` gate and ran its check. First run failed because my two example files
   lacked a closing code fence (my error, not the skill's):

```
$ python3 _build/checks/check_examples.py .
2 worked examples, 2 problems
  PROBLEM example-1-email-only.md: no answer block with 'REPLY DRAFT:'
  PROBLEM example-2-email-with-facts.md: no answer block with 'REPLY DRAFT:'
exit=1
$ python3 -c "...re.findall(...)..."; grep -n '```' base/examples/example-1-email-only.md | cat -A
1
['Subject: VERY disappointed - order #4471']
12:```$
35:```$
39:```$
$ for f in base/examples/*.md; do printf '```\n' >> "$f"; done; tail -3 base/examples/*.md; python3 _build/checks/check_examples.py .
tail: option used in invalid context -- 3
example-1-email-only.md: reply body 106 words (limit 120)
example-2-email-with-facts.md: reply body 103 words (limit 120)
2 worked examples, 0 problems
exit=0
```

3. Proof the new gate can fail (a copy with an exclamation mark, in a temporary folder, then deleted):

```
$ python3 calm-reply/_build/checks/check_examples.py .neg; rm -rf .neg
x.md: reply body 106 words (limit 120)
1 worked examples, 1 problems
  PROBLEM x.md: reply has an exclamation mark
exit=1
```

4. Prepared the run folders and checked the copies and the README sample:

```
$ mkdir -p $A $B && cp base/AI-INSTRUCTIONS.md $A/ && cp base/AI-INSTRUCTIONS.md $B/ && (write prompt.txt in each) && find $R -type f | sort
_build/runs/round-1/email-only-broken-teapot/AI-INSTRUCTIONS.md
_build/runs/round-1/email-only-broken-teapot/prompt.txt
_build/runs/round-1/email-with-facts-wrong-size/AI-INSTRUCTIONS.md
_build/runs/round-1/email-with-facts-wrong-size/prompt.txt
copies identical
README sample == example 1 email: True
```

5. Gate output after the step 5 to 8 build (before round 1 was run):

```
$ cd calm-reply && python3 _build/checks/gates.py .
pass    layout       0.0s  The folder follows the showcase layout
pass    links        0.0s  No Markdown link in this project is broken
pass    examples     0.0s  Each worked example has the promised shape and a reply body of 120 words or fewer

All gates that ran passed.
exit=0
$ cd the repository && python3 calm-reply/_build/checks/gates.py calm-reply --all
(same three pass lines)
All gates that ran passed.
exit=0
$ git -C the repository status --short
?? calm-reply/
```

6. After round 1: read the logs and results, confirmed the run copies of the instructions had not
   changed, applied the fixes, and reran the gates.

```
$ cd calm-reply/_build/runs/round-1 && find . -type f | sort
./email-only-broken-teapot/AI-INSTRUCTIONS.md
./email-only-broken-teapot/friction.md
./email-only-broken-teapot/note.md
./email-only-broken-teapot/prompt.txt
./email-only-broken-teapot/result.md
./email-with-facts-wrong-size/AI-INSTRUCTIONS.md
./email-with-facts-wrong-size/friction.md
./email-with-facts-wrong-size/note.md
./email-with-facts-wrong-size/prompt.txt
./email-with-facts-wrong-size/result.md
(then cat of both friction.md, then of both result.md and note.md: contents not repeated here)
$ diff ../../../base/AI-INSTRUCTIONS.md email-only-broken-teapot/AI-INSTRUCTIONS.md && echo same-A; diff ... && echo same-B
same-A
same-B
$ (python edit of base/AI-INSTRUCTIONS.md); diff <backup> base/AI-INSTRUCTIONS.md; wc -l base/AI-INSTRUCTIONS.md
(diff: 6 changed hunks, as in "Test results, round 1")
79 base/AI-INSTRUCTIONS.md
$ (python edit removing two lines from example 1); rm <backup>; grep -n needs base/examples/example-1-email-only.md
(4 blanks in the reply, 4 matching "Missing" lines)
```

7. New gate output (the gate output to hand back), run after every fix, including the README and
   plan status rows:

```
$ cd calm-reply && python3 _build/checks/gates.py .
pass    layout       0.0s  The folder follows the showcase layout
pass    links        0.0s  No Markdown link in this project is broken
pass    examples     0.0s  Each worked example has the promised shape and a reply body of 120 words or fewer

All gates that ran passed.
exit=0
$ cd the repository && python3 calm-reply/_build/checks/gates.py calm-reply --all
pass    layout       0.0s  The folder follows the showcase layout
pass    links        0.0s  No Markdown link in this project is broken
pass    examples     0.0s  Each worked example has the promised shape and a reply body of 120 words or fewer

All gates that ran passed.
exit=0
$ python3 calm-reply/_build/checks/check_examples.py calm-reply
example-1-email-only.md: reply body 93 words (limit 120)
example-2-email-with-facts.md: reply body 103 words (limit 120)
2 worked examples, 0 problems
exit=0
$ git status --short
?? HANDBACK.md
?? calm-reply/
```

Other file writes (README.md, AGENTS.md, base/plan.md, base/AI-INSTRUCTIONS.md, the two examples)
were made with the editor, not commands.

## What is handed back

- The plan: `calm-reply/base/plan.md`
- The first version: `calm-reply/base/AI-INSTRUCTIONS.md` (plus README, AGENTS.md, two references in `base/examples/`)
- The gate output: above, item 7 (all three gates pass)
- The friction logs, unedited, in their run folders:
  `calm-reply/_build/runs/round-1/email-only-broken-teapot/friction.md` and
  `calm-reply/_build/runs/round-1/email-with-facts-wrong-size/friction.md`

## Note

**Decided.** Full nine steps. Build one paste-in instruction file for ChatGPT, buy nothing, cost
US$0. Two kinds of request: email only, and email plus `What I know:`. Replies of 120 words or
fewer, a "WHAT THEY WANT" line, `[needs: ...]` blanks, a four-part note. A third gate checks the
worked examples. Proceeded past the open step 7 gate, as the lead asked. After round 1: defined
an "ask", a "promise", a "deadline", when to admit fault, how to offer options, how to count
words, the greeting and the "Missing" layout; made any injury count as serious; trimmed worked
example 1 to match.

**Assumed.** The shop is a small online shop selling physical goods. The owner pastes emails by
hand. ChatGPT Free is enough. The worked examples count as references. "A copy of the
instructions" in the test means `base/AI-INSTRUCTIONS.md`. The two fresh sessions stand in for
ChatGPT well enough to find gaps in the instructions (they were AI agent sessions, not ChatGPT).

**Not checked.** Whether the fixed instructions remove the round 1 blocking points: no round 2.
Whether real ChatGPT (any plan) follows them. Whether Projects are on the Free plan today
(OpenAI's page could not be read; source is a 2025 article). ChatGPT pricing page (could not be
read). Zendesk and Outlook Copilot. Whether the shop is on Shopify or uses Gmail. Prices of
Google AI plans and of Shopify Inbox AI. The step 7 review.

**Test this next.** Round 2: two new fresh sessions on `_build/runs/round-2/` with the current
instructions, ideally the same two prompts plus one new one, and see whether any blocking point
returns. Watch the unchanged minor points (order number, labelled lines, the code fence). Then
paste the instructions and the README sample into real ChatGPT Free and compare with example 1.
Then give it to the shop owner with one real email and watch, without helping.

## Friction with the skill

Quotes are from `SKILL.md` unless another file is named.

1. BLOCKING. "Small job? ... offer the short path: steps 1, 6 and 8 in full ... Use all nine if
   they say no, or if the tool needs files, other people or anything paid." Nobody can answer the
   offer unattended, and the tests are unclear (is the customer "other people"? is an email a
   "file"? is a ChatGPT plan "paid"?). This job fits the short-path description; another agent
   could take it and produce a much thinner plan.
2. MINOR. Step 1 "the wow" is not defined in SKILL.md; only `base/plan.md` defines it, and adds
   "Build it first", which clashes with building at step 8.
3. BLOCKING. Step 2: "If not, stop and write a guide to that thing." When the thing built is a
   paste-in prompt for an assistant the user already has, "build" and "write a guide to ChatGPT"
   are nearly the same; one agent would stop here, another would carry on.
4. BLOCKING. Step 2: "Record one row per option" does not say where. `base/plan.md` says "One
   page. If a section needs more than five lines, the scope is too big", yet eleven sourced rows
   do not fit one cell. I added a table under the plan; another agent would put it elsewhere or
   cut it.
5. MINOR. Step 2 row fields ("cost, limits, what happens if it goes away") do not fit
   "Established practice" rows.
6. BLOCKING. Step 3: "List paid options for what is left. Do not choose" against the gate "Do
   you know what you would build and what you would buy?" Answering the gate requires a choice.
7. MINOR. Steps 3, 4 and 6 checks say "Your answer, written in the plan", but `base/plan.md` has
   no heading for build-or-buy or for "fully described".
8. MINOR. Step 4 gate: "an amount you accept". The "you" who accepts is unclear when the agent
   works alone.
9. MINOR. Step 5 check "`python3 _build/checks/gates.py .` passes in the new folder" passes on
   the untouched template, so it cannot answer "Could a beginner draw it?".
10. MINOR. "Without `<where>` it uses `projects/` if there is one, otherwise the current folder."
    The current folder, not the repository root: the result depends on where the agent stands.
11. MINOR. "Every project uses this layout. Fix it now and do not change it later" against
    `base/plan.md`: "The folder layout | Decide it now".
12. MINOR. "base/ what a beginner needs: six things at most, plus examples/" against
    `check_project.py`, which counts `examples/` inside the six (`len(inside) > 6`). Did not bite here.
13. BLOCKING. "README.md hook, one picture" and the README template "[One picture or short
    animation of the result. Put it here, before any text.]" The layout has no place for an image
    file (`check_project.py` rejects extra top-level files; base/ is capped). I used a text
    diagram; another agent would add an image somewhere else.
14. BLOCKING. Step 6: "one for each kind of request the beginner version handles". "Kind of
    request" is not defined. I chose two (email only; email plus `What I know:`); another agent
    could make one, or one per complaint type.
15. BLOCKING. "Say what a result is. Hand-built is a reference. Made by a chat from a prompt is an
    example." Worked examples written by the building agent fit neither label, and the folder the
    layout requires is called `examples/` while its contents are references.
16. MINOR. "Before you start: 2. ... If there is none, you make one at step 5", while steps 1 to 4
    must be "written in the plan", and the plan file only exists once the folder is made.
17. BLOCKING. Step 7 needs "A person, or a fresh session"; unlike step 8 it says nothing about
    what to do when neither is available, and "Stop at the gate ... Do not carry on and come
    back" then forbids reaching step 8. I carried on with the gate open because the lead asked.
18. MINOR. Step 7: "a fresh session that sees only the plan": `base/plan.md` alone, or the plan
    with README and instructions?
19. BLOCKING. Fresh-session test: "put in it only: a copy of the instructions". Which
    instructions: `base/AI-INSTRUCTIONS.md`, `AGENTS.md`, or the test instructions? I used
    `base/AI-INSTRUCTIONS.md`.
20. MINOR. "`_build/runs/round-1/<what was asked>/`": no naming rule for the folder.
21. MINOR. "write the result, a hand-over note and `friction.md`" and "decide where it would
    ask": no file names for the result and the note, and no format for recording where it would ask.
22. MINOR. "a note with four headings: Decided. Assumed. Not checked. Test this next." against the
    template `AGENTS.md`: "Chose. Assumed. Missing. Check before sharing." Two different
    four-heading notes in one process.
23. MINOR. "Numbers shown to a reader are checked by a script, or not shown" against step 4
    "Every dependency ... with its price". Prices from the web cannot be script-checked.
24. MINOR. `check_project.py` mentions "everything in projects/" and "drafts/project-method and
    its scaffold"; `gates.py` shows `python3 ../../tools/check_links.py`; the step table says
    "written by _build/build.py from _build/steps.py". None of these exist here, against "This
    folder is all you need, in any repository".
25. MINOR. "What you hand back ... the first version": a path or its full text is not said.
26. MINOR. Short path: "steps 1, 6 and 8 in full, the others in one line each", but step 5 makes
    the folder that steps 6 and 8 need.

Blocking: 9. Minor: 17.
