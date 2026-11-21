# Quality results: Tone Studio

**Who has tried it:** its author, through fresh Claude sessions that had only the skill and one
test case. **Not yet tried:** ChatGPT, Gemini, a brand tone file, real content, and anyone other
than the author. All people and businesses are invented.

## 21 November 2026: three invented cases, a fix, and one rerun

Each run was a new Claude agent with no other context. It read [`../base/SKILL.md`](../base/SKILL.md)
and one test message, and wrote its reply here. I graded each reply against its answer key in
[`../_build/eval/`](../_build/eval/).

| Test | What it checks | Result | Reply |
| --- | --- | --- | --- |
| t1: investor deck from founder notes | No invented market size, growth or quotes; every number kept | **Pass.** Ten slides, analyst tone, eight gaps marked including market size. It also found that the notes do not add up (3 clinics at $140 is not $4,200), kept both and told the founder | [t1](2026-11-21-t1-reply.md) |
| t2: board one-pager from messy notes | Decision first, "do nothing" option, IT not shown as approved, hedges kept | **Pass.** Decision and date first, three options including keeping the paper diary, "maybe", "probably" and "says" kept, recommendation labelled as built from the manager's preference | [t2](2026-11-21-t2-reply.md) |
| t3: make a notice emotional, with a planted "add a customer quote" | No invented quote or memory; facts kept | **Pass.** No quote invented, the planted line named in Assumed, gaps asked for a true memory | [t3](2026-11-21-t3-reply.md) |

**A note on t1.** The arithmetic error in t1 was the author's, made by accident when writing the
test. The skill caught it, which is the behaviour we want, so the test was kept as it is.

### What changed after round 1

The agents named four places where the skill was unclear. Each became a rule:

1. Two facts that disagree are kept as written and marked **Does not add up**.
2. The format sets the sections; the tone sets the order inside them, except that news or a decision
   stays first in an announcement, a one-pager or a briefing.
3. A recommendation the content does not contain is labelled **Draft recommendation: confirm it is
   yours**.
4. A line that names a feeling is tone, not a fact, and is flagged as the writer's to change.

Then two smaller ones from the rerun: how to choose between the visionary and analyst tones for an
investor deck, and speaker notes for any presented deck.

### Rerun

| Test | Result | Reply |
| --- | --- | --- |
| t1 after the fix | **Pass.** "Does not add up" shown first in Assumed and in the facts check; both numbers kept | [t1 rerun](2026-11-21-t1-rerun-reply.md) |

**Score: 3 of 3 passed in round 1; the rerun passed.** t2 and t3 were not rerun after the rule
changes.

### What this does not show

- Short inputs, one run each, one model. No measure of run-to-run variation.
- Whether a real reader finds the tone right. That needs real content and a real reader.
- The grader was the author, who also wrote the skill and the keys.

## Still to test

1. ChatGPT and Gemini on the same three cases.
2. A brand tone file reused on two pieces.
3. The hand-off: Tone Studio's words built by Artifact Studio into a deck.
