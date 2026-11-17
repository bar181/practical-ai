# Friction log: first-time visitor builds the starter tool

Run: README "Try it: build a tool" followed step by step, build request carried out by the same
agent, tool built in `/tmp/start/ap/out/document-to-action-brief/`, hand-back in
`/tmp/start/ap/out/HANDBACK.md`.

**Totals: 1 BLOCKING, 15 MINOR.**

**Time:** system clock 23:30:19 to 23:33:40 EST on 16 November 2026, about 3.5 minutes of agent time
from opening the README to this file. That is for the build only. The verify loop has not run:
three fresh-chat pastes, reading the results, and up to two fix-and-rerun rounds are still owed by
a person, so the README's "about 10 minutes" for a finished, checked tool was not achieved.

## Points, in the order I hit them

1. **MINOR. The opening promise does not hold for every agent.** The first paragraph says the
   builder "tests the package in a fresh session before you get it". Only the Status section at
   the very bottom admits that "a builder running inside another agent could not start sessions of
   its own". A visitor learns this after the build, not before.

2. **MINOR. The starter request has no "catch".** "Use it with your own job" says the request has
   four answers, the fourth being the catch, and "Is it ready?" requires "the catch was caught".
   The example request gives only three. The builder skill does not list the catch as required
   either (Start asks for job, user, input), so the builder silently picks its own U5. I had to
   choose it (undated letter / unstated anchor date, plus a missing enclosure) and list it as an
   assumption.

3. **MINOR. The link failed; the fallback works but changes where the tool lands.** WebFetch of the
   raw GitHub URL was refused (not on the session's allowlist). The fallback ("download this
   repository, open the agent in its folder") is clear, but it contradicts "open it in an empty
   folder": followed literally, `document-to-action-brief/` would be created at the root of the
   downloaded repository, mixed in with the project. The fallback does not say where the output
   should go.

4. **MINOR. "Copy `base/template/` from the Agentic Process project" and "`base/PROCESS.md` in the
   Agentic Process project" are not paths.** With the raw-link route, a visitor's agent has no copy
   of the project, so it cannot copy the template at all (it would have to fetch three more raw
   URLs it is never given). With the fallback route I had to work out that this meant
   `projects/agentic-process/base/template/`.

5. **MINOR. "(from `build-agent`)" points at nothing.** Step 1 says to sort fixed / varies /
   judgement "from `build-agent`", with no link or explanation. A visitor cannot tell whether it is
   a file, a skill or a person. (A `small-business:build-agent` skill happens to exist in this
   session, but the builder never says to read it.)

6. **MINOR. The reuse check has no stopping rule.** "Anthropic's skills and plugins first, then the
   platform the person uses, then open source. Record links and dates." There is no hint of how
   deep to go or what "does the whole job" means. I did two web searches, read one registry page,
   and noted the installed `small-business:contract-review` skill. I did not read the external
   `SKILL.md` itself, which step 3 says to do for anything external; it is unclear whether step 3
   applies to things you only considered or only to things you borrow from.

7. **MINOR. Rows 2 and 3 of the build table both fit, and "take the first that fits" leaves a gap.**
   Deadlines like "within 21 days of the date of this notice" are date arithmetic (row 3: a
   script), but the user is in "the chatbot they already use" where a script cannot run. I chose
   row 2 and made the skill show every sum. The table gives no guidance for exact-behaviour steps
   in a Level 1 tool.

8. **MINOR (slow). Step 3 sends you to the skill creator, which pulls the other way.** Opening
   `skill-creator` loads a long workflow: an `evals/` folder per case, baseline sub-agents, a
   workspace, a benchmark and an HTML viewer. That contradicts the builder's "Nothing extra" rule
   and step 4's "copy `base/template/`". I used only its writing advice. The builder should say
   which parts to use, or drop the pointer.

9. **MINOR. Step 4 "Write the inputs for two cases" does not say where.** The README's "What you
   get" says `example.md` holds "practice notices to try it on", but the template `example.md` has
   no slot for them and says "Nothing below the line is edited". I added a "Practice notices"
   section after the result.

10. **MINOR. Two cases or three?** The builder skill says two cases (normal and U5). `PROCESS.md`
    "Verify" and the template's U2 row require a third: an input missing something. The template
    also has a "Works in other chatbots" row that the builder skill never mentions. I wrote all
    four checks.

11. **BLOCKING. The separate-session test cannot happen from here, so the starter cannot reach a
    ready tool.** I am running as a sub-agent with no tool to start a new session or sub-agent. (A
    `claude` CLI exists on the machine, but starting it would mean launching a session on the
    host's credentials and writing transcripts outside the one folder I may write to, so I treated
    it as unavailable.) I followed the skill's fallback: every check "not yet run", and the exact
    messages in the hand-back. The fallback is honest, but it means none of the five "Is it ready?"
    items can pass without a person doing three more pastes. The guide does not tell the visitor
    up front that this is their job.

12. **MINOR. No instruction for `example.md` when nothing ran.** The skill says to save the normal
    result as `example.md` and never to write a result yourself, but not what `example.md` should
    contain meanwhile. I put the input message and "Not yet run." where the result goes.

13. **MINOR. "Hand back: one note": a chat message or a file?** Not said. The request says "Hand back
    what you built". I wrote `/tmp/start/ap/out/HANDBACK.md` beside the tool folder so the tool
    stays at three files.

14. **MINOR. "The exact message for each case" means repeating the whole `SKILL.md`.** The message
    the tester pastes is all of `SKILL.md` plus the notice. Copying it three times into the
    hand-back would be long and go stale after any fix; I described each message as "`SKILL.md` +
    this block" instead. The skill does not say which is wanted.

15. **MINOR. Check results are recorded in two places.** `PROCESS.md` says to record each check in
    the tool's README; the builder skill says to put them in the hand-back. I kept both, which a
    tester must now update in two files.

16. **MINOR. The README's time claim covers only the build.** "Build your first tool in about 10
    minutes" is true for writing the three files (about 3.5 minutes here), not for a tool that has
    passed its own "Is it ready?" checklist.

## "Is it ready?" on what I built

| Item | Answer |
| --- | --- |
| Every line of the spec has a check that ran | **No.** U1 to U5 each have a written check, listed in the README and the hand-back, but every result is "not yet run". |
| The checks ran in a separate session, and the hand-back says who ran them | **No.** "Not yet run"; who ran them: nobody yet. The three messages are in `HANDBACK.md`. |
| `example.md` is a real result, unedited | **No.** It holds the normal-case input and "Not yet run." No result was written in its place. |
| The catch was caught in its own test case | **No.** The catch has its own test case (Greenbank Produce, undated letter, missing schedule), but it has not been run. |
| Read only the first screen of a result: could they act on it as it is? | **Cannot answer.** There is no result to read. The output shape puts a one-line summary, "Missing or unclear" and the actions table first, but that is a design, not evidence. |

**Verdict: not ready.** The tool is built and its checks are written, but none has run. Next step:
paste Messages A, B and C from `HANDBACK.md` into fresh chats and record what they show.
