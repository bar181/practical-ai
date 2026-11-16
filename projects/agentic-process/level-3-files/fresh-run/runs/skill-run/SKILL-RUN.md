# Skill run: agentic-process, new tool "Meeting actions"

Run on 16 November 2026 by a coding agent that had not seen this repository, in the throwaway
copy at `the repository copy`. Folder made: `projects/meeting-actions/`.

Read, in this order: `projects/agentic-process/AGENTS.md`, the skill
(`level-2-files/agentic-process/SKILL.md`), `base/PROCESS.md`, `base/plan-template.md`,
`level-2-files/new_project.py` and `level-2-files/template/`, then
`level-3-files/fresh-run/README.md` and `RULES.md`. After commands failed, to find out why:
`workshop/tools/gates.py`, `workshop/tools/check_project.py`, the head of
`workshop/tools/check_links.py`, `level-3-files/gates.json` and `.gitignore`. Not read: the root
`AGENTS.md`, `projects/README.md`, the scorecard, the examples in `agentic-process/base/examples/`.

## Headline

- Template script: FAILED as the skill writes it. Worked with the form in AGENTS.md.
- Layout check: PASSED on the first try.
- Link check: FAILED on the first try and still fails. 29 broken links, none in the new project.
- Gates: FAILED on the first try (no `gates.json`). PASS after I wrote `base/gates.json`.
- Under the skill's own rule ("Stop at the gate") this run should have stopped at step 2. The
  gates of steps 2, 4, 7 and 8 are not passed. I went on only because the task said to write
  "not checked" and go as far as possible. Everything from step 3 on is provisional.

## Steps, with the three lines the skill asks for

| # | Step | Gate | Result |
| --- | --- | --- | --- |
| 1 | Scope | The job fits in one sentence | PASS |
| 2 | Reuse check | Nothing existing does the whole job | NOT PASSED. Not checked: no search was run |
| 3 | Outside help | Build-or-buy is clear for the first version | PASS, on assumptions |
| 4 | Cost | The first version has a known cost | NOT PASSED. Prices and limits not checked |
| 5 | Simplest design | The layout check passes | PASS, first try |
| 6 | Plan and front door | The beginner version is fully described | PASS, judged by the author only. No command checks it |
| 7 | Review | The reviewer's summary matches the plan | NOT PASSED. Not run. Folder prepared |
| 8 | Build and test | The fresh session finished the job, friction log read | NOT PASSED. Built. Fresh-session test prepared, not run |
| 9 | Grow | The level below is in use | Not started |

**Step 1, Scope.**
Decided: one user, a team lead who ran the meeting. One job: turn one meeting transcript into a
short follow-up note with the actions, each with an owner and a date, and the questions nobody
answered. Out: recording, transcribing, minutes, sending, creating tasks, tracking across
meetings. The wow: the list of unanswered questions in the asker's words. The test: the transcript
in `base/examples/clean-transcript.md` and the result shown under it.
Assumed: the two lists are one job (one note), not two. "Short" means one line an item and no
summary, with no cap on the count.
Gate: PASS.

**Step 2, Reuse check.**
Decided: nothing. Not checked.
Assumed: something is left to build. From memory only, with no link and no date: meeting tools and
note-taking services already list action items, and at least one may list open questions. This
gate has a real chance of failing once someone looks.
Look up: (a) built in: Microsoft Teams recap and Copilot, Zoom AI Companion, Google Meet notes
with Gemini, Slack huddle notes, Webex. (b) free or free-plan tools: Otter, Fireflies, Fathom,
tl;dv, Granola, Read.ai, and open-source meeting summarisers. (c) common practice: what a plain
"list the action items and open questions" prompt gives in a chat assistant. For each: does it
give an owner and a date for every action, does it mark a missing one or guess, and does it list
questions nobody answered. Record the link and the date.
Gate: NOT PASSED (not checked).

**Step 3, Outside help.**
Decided: build one file of paste-in instructions. Buy nothing for the first version. No option
chosen.
Assumed: the paid options are the paid plans of the tools in step 2 and of the chat assistants.
Names from memory, not checked. Look up: the current paid plans and what each adds.
Gate: PASS, on assumptions.

**Step 4, Cost.**
Decided: three dependencies. A chat assistant that takes pasted text. A transcript from the
meeting tool the team already has. This folder (free, Apache 2.0).
Assumed: the team lead already has the first two, so there is no new spend.
Look up: the price and the message-length limit of the free plan of each assistant a team lead
is likely to use, and whether the meeting tool charges for transcripts.
Gate: NOT PASSED. The cost is "nothing" only on an assumption, and no limit is known.

**Step 5, Simplest design.**
Decided: any chat assistant. Files in `projects/meeting-actions/`. Manual: getting the
transcript, pasting, checking, filling gaps, sending. Layout fixed: `README.md`, `AGENTS.md`,
`LICENSE`, `base/` with `AI-INSTRUCTIONS.md`, `plan.md`, `gates.json` and `examples/`, and
`_build/runs/` for test runs. No `level-2-files/` or `level-3-files/`.
Assumed: slug `meeting-actions`, title "Meeting actions". `gates.json` belongs in `base/`. Test
runs belong in `_build/runs/`. Neither is said by the skill (Friction 3 and 8).
Gate: PASS. `meeting-actions: layout ok`, first try, and again after the files were filled.

**Step 6, Plan and front door.**
Decided: filled `base/plan.md`. README has the hook, "Try it in five minutes" with a sample
transcript, and two worked examples in `base/examples/`: a clean transcript and a rough one.
Assumed: "variant" means a kind of transcript, and there are two. The README's "picture" is a
text block. The worked examples are labelled as references written by hand by the authoring agent.
Gate: PASS by my own reading only.

**Step 7, Review.**
Decided: not run. Prepared `projects/meeting-actions/_build/runs/step-7-review/` with a copy of
the plan and a `prompt.txt`.
Assumed: the shape of that folder. The skill gives none.
Gate: NOT PASSED. Nobody has explained the plan back.

**Step 8, Build and test.**
Decided: built the beginner version: `base/AI-INSTRUCTIONS.md` (120 lines), the tool's
`AGENTS.md`, the two examples, `base/gates.json`. Prepared two run folders as
`fresh-run/README.md` describes. The fresh-session test was NOT RUN: I cannot start another agent.
Assumed: one run for each kind of transcript. "A copy of your tool's instructions" means
`AI-INSTRUCTIONS.md` alone.
Gate: NOT PASSED. No fresh session ran, so there is no friction log to hand back.

Run folders, each holding only what the instructions list:

```
projects/meeting-actions/_build/runs/round-1/clean-transcript/   AI-INSTRUCTIONS.md  prompt.txt
projects/meeting-actions/_build/runs/round-1/rough-transcript/   AI-INSTRUCTIONS.md  prompt.txt  transcript.txt
```

To run one: start a new session and give it
`projects/agentic-process/level-3-files/fresh-run/RULES.md` and the path of one run folder. Then
compare its result with the "What came back" block in the matching file in `base/examples/`.

## Every command, with its real result

1. Template script as the skill writes it (step 5), from the repository root. **FAILED.**

```
$ python3 new_project.py meeting-actions "Meeting actions"
python3: can't open file 'new_project.py': [Errno 2] No such file or directory
exit=2
```

Changed: nothing in the repository. Ran the form in AGENTS.md from `projects/agentic-process/`.

2. Template script, AGENTS.md form. **PASSED.**

```
$ cd projects/agentic-process && python3 level-2-files/new_project.py meeting-actions "Meeting actions"
Made projects/meeting-actions
Next: fill in base/plan.md, then write the README's first screen.
exit=0
```

3. Layout check, on the untouched template copy. **PASSED, first try.**

```
$ python3 workshop/tools/check_project.py projects/meeting-actions
meeting-actions: layout ok
exit=0
```

4. Link check. **FAILED, first try.**

```
$ python3 workshop/tools/check_links.py .
204 Markdown files, 29 broken links
  BROKEN README.md -> projects/artifact-studio/base/AI-INSTRUCTIONS.md
  BROKEN README.md -> projects/artifact-studio/base/examples/voice-explainer.html
  BROKEN README.md -> projects/artifact-studio/base/examples/
  BROKEN README.md -> projects/artifact-studio/base/AI-INSTRUCTIONS.md
  BROKEN README.md -> projects/artifact-studio/base/studio.html
  BROKEN README.md -> projects/artifact-studio/base/examples/
  BROKEN README.md -> projects/artifact-studio/base/AI-INSTRUCTIONS.md
  BROKEN README.md -> projects/artifact-studio/base/TEACH-IN-30-MINUTES.md
  BROKEN projects/artifact-studio/README.md -> base/examples/report.html
  BROKEN projects/artifact-studio/README.md -> base/studio.html
  BROKEN projects/artifact-studio/README.md -> base/TEACH-IN-30-MINUTES.md
  BROKEN projects/artifact-studio/README.md -> base/examples/
  BROKEN projects/artifact-studio/README.md -> base/examples/voice-visionary.html
  BROKEN projects/artifact-studio/README.md -> base/examples/voice-storyteller.html
  BROKEN projects/artifact-studio/README.md -> base/examples/voice-emotional.html
  BROKEN projects/artifact-studio/README.md -> base/examples/voice-explainer.html
  BROKEN projects/artifact-studio/README.md -> base/examples/voice-practical.html
  BROKEN projects/artifact-studio/README.md -> base/examples/voice-analyst.html
  BROKEN projects/artifact-studio/README.md -> base/examples/voice-brief.html
  BROKEN projects/artifact-studio/README.md -> base/examples/social-posts.html
  BROKEN projects/artifact-studio/README.md -> base/examples/photo-effects.html
  BROKEN projects/artifact-studio/README.md -> base/examples/report.html
  BROKEN projects/artifact-studio/AGENTS.md -> base/AI-INSTRUCTIONS.md
  BROKEN projects/artifact-studio/AGENTS.md -> base/examples/
  BROKEN projects/artifact-studio/AGENTS.md -> _build/examples/runs/
  BROKEN projects/artifact-studio/level-2-files/README.md -> ../base/studio.html
  BROKEN projects/agentic-process/level-3-files/fresh-run/README.md -> ../../../artifact-studio/_build/examples/runs/
  BROKEN projects/agentic-process/base/examples/monday-email.md -> ../../level-3-files/fresh-run/runs/round-2/monday-email/friction.md
  BROKEN projects/agentic-process/base/examples/supplier-notice.md -> ../../level-3-files/fresh-run/runs/round-2/supplier-notice/friction.md
exit=1
```

Changed: nothing. None of the 29 is in the new project, and the files they point at are not mine
to make. `projects/artifact-studio/` has no `base/` folder in this copy. I cannot tell whether
that is true of the real repository or only of this copy.

5. Gates, on the untouched template copy. **FAILED, first try.**

```
$ python3 workshop/tools/gates.py projects/meeting-actions
Traceback (most recent call last):
  File "workshop/tools/gates.py", line 24, in <module>
    gates = json.load(open(gates_file, encoding="utf-8"))
                      ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'projects/meeting-actions/gates.json'
exit=1
```

Changed: wrote `projects/meeting-actions/base/gates.json` with four gates of my own choosing:
layout, links (this project only), filled (no template placeholder left), examples (each worked
example shows both lists and the note). Nothing in `workshop/` or `agentic-process/` was changed.

6. After filling the project: layout check. **PASSED.**

```
$ python3 workshop/tools/check_project.py projects/meeting-actions
meeting-actions: layout ok
exit=0
```

7. After filling the project: gates. **PASSED.** Run twice, the second time after a one-line
README edit, with the same output.

```
$ python3 workshop/tools/gates.py projects/meeting-actions
pass    layout       0.0s  This project follows the repository's layout
pass    links        0.0s  No Markdown link in this project is broken
pass    filled       0.0s  No placeholder from the template is left in the project
pass    examples     0.0s  Each worked example shows a result with both lists and the note

All gates that ran passed.
exit=0
```

8. After filling the project: link check, whole repository. **FAILED**, same 29 links.

```
$ python3 workshop/tools/check_links.py .
209 Markdown files, 29 broken links
exit=1
```

No line of that output names `meeting-actions`.

Commands the skill does not name, run to understand the failures:

9. Link check on the new project alone. PASSED.

```
$ python3 workshop/tools/check_links.py projects/meeting-actions
9 Markdown files, 0 broken links
exit=0
```

10. Layout check on a scratch copy of the project with `gates.json` at its root. FAILED, as the
code suggested. The scratch copy was deleted.

```
ma: 4 problem(s)
  missing base/README.md
  missing level-1/README.md
  README.md has no '## Use it today'
  README.md has no '## How it is laid out'
exit=1
```

11. The "filled" gate's command against the untouched template, to see that it can fail. It
found the placeholders and failed (exit 1), as intended.

12. The parent project's gates, because AGENTS.md pairs `level-3-files/gates.json` with this
command. FAILED.

```
$ python3 workshop/tools/gates.py projects/agentic-process
pass    layout             0.0s  This project follows the layout it tells others to follow
pass    template           0.0s  A project made from the template passes the layout check
FAIL    first-showcase     0.0s  Artifact Studio, the first showcase, passes the layout check
          artifact-studio: 1 problem(s)
            missing base
FAIL    links              0.0s  No Markdown link in the repository is broken
            BROKEN projects/artifact-studio/AGENTS.md -> base/examples/
            BROKEN projects/artifact-studio/AGENTS.md -> _build/examples/runs/
            BROKEN projects/artifact-studio/level-2-files/README.md -> ../base/studio.html
            BROKEN projects/agentic-process/level-3-files/fresh-run/README.md -> ../../../artifact-studio/_build/examples/runs/
            BROKEN projects/agentic-process/base/examples/monday-email.md -> ../../level-3-files/fresh-run/runs/round-2/monday-email/friction.md
            BROKEN projects/agentic-process/base/examples/supplier-notice.md -> ../../level-3-files/fresh-run/runs/round-2/supplier-notice/friction.md
pass    skills             0.0s  This project's skill follows the authoring rules

DO NOT SHIP. Failed: first-showcase, links
exit=1
```

Side effects outside `the repository copy`, both mine to own up to: the "template" gate in command 12
runs `mktemp -d` and leaves a `trial-tool` folder in the system temp folder. And I wrote one
scratch file of link-check output to `(a scratch folder)` and deleted it straight away.

Also run: `python3` to confirm the weekdays of the dates in the worked example (16, 17, 19 and
25 November 2026 are Monday, Tuesday, Thursday and Wednesday), and `cmp` and `diff` to confirm
that the run folders hold exact copies of the instructions, the plan and the sample transcript.

## What I assumed

About the tool:

1. The two lists are one job. The person asked for both in one breath.
2. The team lead ran the meeting and already has a text transcript.
3. "Short" means one line an item and no summary. No cap on how many actions.
4. Any chat assistant. Nothing tied to one vendor. English only.
5. The assistant does not ask for a missing meeting date. It marks `[needs: meeting date]` and
   works out no calendar day.
6. A weekday means the next such day after the meeting. "The 25th" means the next 25th.
7. A task the meeting agreed on but nobody took is listed, with `[needs: owner]`.
8. A question someone promised to find out appears in both lists.
9. The note is plain text, not a table, so it pastes into email or chat.
10. A line about checking the organisation's rules before pasting a real transcript belongs in
    the README.
11. The people and meetings in the examples are made up.

About the process:

12. Slug `meeting-actions`, title "Meeting actions".
13. Going on past the gates of steps 2, 4 and 7 is allowed here, because the task said so. The
    skill says the opposite.
14. `gates.json` goes in `base/`. Test runs go in `_build/runs/`.
15. "Variant" means a kind of transcript. Two of them.
16. A text block can stand in for the README's picture.
17. A result I wrote by hand in the authoring session is a "reference".
18. No index needs the new project added. `projects/README.md` and the root README were not read
    or changed.
19. The end note the parent AGENTS.md asks for can live in this file.

## Friction

1. **BLOCKING (command failed).** SKILL.md line 29: "Make the folder from the template:
   `python3 new_project.py <slug> "<Title>"`". There is no path. The only working folder the skill
   names is at line 65, "From the repository root:", and from there the command fails with "can't
   open file". AGENTS.md line 21 gives a different command, "Run
   `python3 level-2-files/new_project.py <slug> "<Title>"`", which works only from
   `projects/agentic-process/`, and AGENTS.md does not say so. Three kinds of command, three
   working folders, one of them stated.

2. **BLOCKING (command failed).** SKILL.md line 69:
   "`python3 workshop/tools/gates.py projects/<slug>` runs the project's own gates". A project
   made from the template has no gates. The command ends in a Python traceback
   (`FileNotFoundError ... gates.json`). The skill never says to write a `gates.json`, what should
   be in it, or at which step. AGENTS.md line 23 makes it worse: "Checks to run after every step |
   `level-3-files/gates.json`, with `python3 workshop/tools/gates.py projects/<slug>`". That pairs
   the process's own gates file with the new project's slug. That file tests agentic-process, not
   the new tool. "After every step" also cannot be done for steps 1 to 4, when no folder exists.

3. **BLOCKING.** There is no place for `gates.json` that fits the layout rules. At the project
   root the layout check treats the project as "the earlier layout" and fails with four problems
   (command 10). In `level-3-files/` the check also demands `level-2-files/`, and SKILL.md lines
   42 and 43 say of both "Only if it holds something usable", and step 9's gate is "The level
   below is in use". In `base/` it uses one of the "six things at most" of "what a beginner
   needs", and a beginner does not need it. The skill's folder block does not list `gates.json`
   at all. I chose `base/`. An agent that copied the parent project would choose `level-3-files/`
   and add a `level-2-files/` to hold it up. Line 46 then makes either choice permanent: "Fix this
   layout at step 5. Do not change it later."

4. **BLOCKING (command failed).** SKILL.md line 67: "`python3 workshop/tools/check_links.py .`
   checks every Markdown link". It fails with 29 broken links before the new project exists and
   after it is finished, and none is in the new project. The skill does not say what to do when
   the check is red for reasons outside the project, and it gives no link check for one project.
   (`check_links.py projects/<slug>` works. I found that by reading the script.) Files that do not
   exist in this copy: everything under `projects/artifact-studio/base/`,
   `projects/artifact-studio/_build/examples/runs/`, and
   `projects/agentic-process/level-3-files/fresh-run/runs/round-2/`. This may be a fault of the
   copy and not of the repository. I cannot tell from inside it.

5. **MINOR.** `fresh-run/README.md` lines 38 and 39: "The logs are in
   `artifact-studio/_build/examples/runs/`", written there as a link to
   `../../../artifact-studio/_build/examples/runs/`. (Quoted here without the link syntax, so that
   this file does not add a broken link of its own.) That folder does not exist here. It is the only pointer to what a real friction log and run
   folder look like, so I had no example to copy.

6. **BLOCKING.** SKILL.md line 26: "Search for what already does it ... Record links and the
   date", with the gate "Nothing existing does the whole job." Nothing says what to do when the
   agent cannot search. Line 51 allows only two outcomes: "Stop at the gate. If a gate fails, fix
   the step. Do not carry on and come back." Yet AGENTS.md line 30 asks for an end note with a
   heading "Not checked", which implies a run can finish with things unchecked. One careful agent
   stops at step 2 and hands back a list of searches. Another goes on to step 8. I went on only
   because my task said to. The same gap applies to step 4 ("its price and limit"). Also "the
   whole job" is not defined: a meeting tool that lists action items but not open questions does
   half of this job, and the gate does not say whether half is enough to stop.

7. **BLOCKING.** SKILL.md line 31: "A person, or a fresh session that sees only the plan,
   explains it back", gate "The reviewer's summary matches the plan". There are no rules for that
   session, no prompt, no place for its summary, no test for "matches" and no word on who judges
   it. `fresh-run/` covers step 8 only. An agent with no person and no second session has two
   readings: review its own plan and pass, or fail the gate and stop. I failed the gate and made a
   review folder of my own design.

8. **BLOCKING.** `fresh-run/README.md` line 11: "Make a folder for the run." It does not say
   where. The skill's folder block has no place for test runs, and anything beside `base/` fails
   the layout check except `_build/`, which the skill never mentions (only the docstring of
   `check_project.py` does). The repository's own links show two conventions,
   `level-3-files/fresh-run/runs/round-2/...` and `_build/examples/runs/`, and both targets are
   missing. I chose `_build/runs/round-1/<kind>/`. Line 46 applies again: the choice has to be
   made at step 5, three steps before the reader meets the need for it.

9. **BLOCKING.** SKILL.md line 30: "one worked example for each variant". "Variant" is not
   defined in the skill, PROCESS.md, the plan template or the README template. The README template
   says "[Where the worked example is, so they can compare.]", one example. The same line's gate
   says "The beginner version is fully described", which suggests variants might be the levels.
   I read it as kinds of input and wrote two examples. Another agent writes one, or three. The
   number of fresh runs follows from this too (`fresh-run/README.md`: "one for each kind of
   request your tool should handle").

10. **MINOR.** SKILL.md line 30: "Fill `plan-template.md`." The template script makes
    `base/plan.md` and prints "Next: fill in base/plan.md". AGENTS.md line 20 says "The plan to
    fill in | `base/plan-template.md`", which is the master copy inside agentic-process. Read
    literally, the skill has the agent fill in the master. The script's own message settles it.

11. **MINOR.** SKILL.md line 19: "Find the project folder. If there is none, make one from the
    template (step 5)." Make it now, before step 1, or at step 5? Steps 1 to 4 have decisions to
    write down and nowhere to write them until the folder exists. I kept them in my head until
    step 5.

12. **MINOR.** SKILL.md line 16: "Read `PROCESS.md` in this project's `base/` folder". "This
    project" could be agentic-process or the new tool's folder. The new folder has no PROCESS.md.

13. **MINOR.** The skill says "The steps below are the same process" as PROCESS.md, but two gates
    differ. Step 5: skill "The layout check passes", PROCESS.md line 16 "Could a beginner draw
    it?". Step 4: skill "The first version has a known cost", PROCESS.md line 15 "Does the
    beginner version cost nothing, or a known amount?". The skill's step 5 gate also passes on an
    untouched template full of placeholders (command 3), so it can pass with no design decided.

14. **MINOR.** SKILL.md line 27: "List paid options for what is left. Do not choose", gate
    "Build-or-buy is clear for the first version". The step says not to choose and the gate asks
    for a choice. I read it as: decide build or buy, do not pick a supplier.

15. **MINOR.** SKILL.md line 52: "Hand-built is a reference. Made by a chat from a prompt is an
    example." A worked example that the authoring agent writes by hand in the same session is
    neither. Step 6 asks for the worked example before step 8 builds the tool, so at step 6 it
    cannot have been made by the tool. I called mine references and said who wrote them.

16. **MINOR.** SKILL.md line 54: "Numbers shown to a reader are checked by a script, or not
    shown." The section name the skill requires, "Try it in five minutes", and the template's
    "Next three additions" are numbers shown to a reader that no script checks. The skill does not
    say which script checks numbers, or how to add one.

17. **MINOR.** Template README: "[One picture or short animation of the result. Put it here,
    before any text.]" No word on what an agent that cannot draw should do, or where an image file
    may live. Beside `README.md` it fails the layout check. In `base/` it uses one of the six. I
    used a text block.

18. **MINOR.** Template README: "[The prompt, with sample input, ready to copy]". The template
    also makes `base/AI-INSTRUCTIONS.md`, "paste-in instructions". Two homes for the prompt, and
    nothing says which one is the source. I kept the instructions in one file and put only the
    sample message in the README, so step 1 of "Try it" is two pastes, not one.

19. **MINOR.** SKILL.md line 60: "Three lines: what was decided, what you assumed, and the gate
    with pass or fail. After step 8, also hand back the friction log". AGENTS.md line 30 adds "At
    the end: the plan on one page, the first version, and a note with four headings: Decided.
    Assumed. Not checked. Test this next." The skill does not mention that note. Neither says
    where it goes, and a file for it beside `base/` fails the layout check. The template's own
    AGENTS.md then asks for a different four headings (Chose, Assumed, Missing, Check before
    sharing). Those are for the tool, but two four-heading notes in one run are easy to mix up.

20. **MINOR.** AGENTS.md "Rules that never bend" 1: "One user and one job. A second job goes
    under 'Next'." The idea has two outputs. The step 1 gate, "The job fits in one sentence",
    passes for any pair of jobs joined by "and". Nothing tells one job from two. I kept both
    lists, since the person asked for both.

21. **MINOR.** `fresh-run/README.md` line 11: "a copy of your tool's instructions". One file
    (`AI-INSTRUCTIONS.md`) or the README and AGENTS.md as well? Line 14: "Give it `RULES.md` and
    the path of the run folder", while RULES.md rule 1 says "Read only the files named in your
    task", and a folder path names no files. RULES.md rule 5, "Use only facts from the person's
    message", read literally rules out the attached transcript. No file name is given for the
    result.

22. **MINOR.** SKILL.md step 8 gate: "Its friction log has been read and the recurring points
    fixed". `fresh-run/README.md` defines recurring as "The same point in three or more logs". The
    skill says "Run the fresh-session test", one test. With one or two runs nothing can recur.

23. **MINOR.** Template `base/plan.md`: "One page. If a section needs more than five lines, the
    scope is too big." Every section is a table cell. A cell has no lines to count, and the step 2
    cell must hold links and a date for each thing found.

24. **MINOR.** The skill never says whether a new project is listed anywhere. `projects/README.md`
    exists. I did not read it or change it.

## The end note the parent AGENTS.md asks for

**Decided.** One user, one job, the layout, the note's format and its rules, as in
`projects/meeting-actions/base/plan.md`.

**Assumed.** The 19 points above. The largest: that something is left to build after step 2.

**Not checked.** What already exists (step 2). Paid options (step 3). Every price and limit
(step 4). Whether the plan can be explained back (step 7). Whether a fresh session can follow the
instructions (step 8). Whether any real team lead wants this. Whether the worked examples are what
the instructions produce: I wrote both, so they agree by construction.

**Test this next.**

1. Do the step 2 look-up first. If a built-in feature does the whole job, stop and write a guide.
2. Run the step 7 review from `_build/runs/step-7-review/`.
3. Run both fresh-session tests from `_build/runs/round-1/` and read each `friction.md` before
   the result.
4. Have a person approve `projects/meeting-actions/` before it is merged.

Blocking: 8. Minor: 16.
