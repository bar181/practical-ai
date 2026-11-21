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

## 21 November 2026: seven tones, one story

Seven fresh Claude agents each took one tone, the skill and one invented source
([`../base/examples/source-content.md`](../base/examples/source-content.md)) and wrote a cinematic
landing page and a social post. [The results](../base/examples/README.md).

- **Facts:** a script compared every number on every page and post with the source. None was added.
  Each folder's `notes.md` lists every fact used, and the lines that are the writer's own wording
  (for example a feeling line in the emotional tone, an analogy in the practical instructor's).
- **Length:** pages 241 to 403 words counted with headings, buttons and footer; posts 133 to 393
  words, each within its platform's range give or take a few words.
- **Pages:** each agent checked its page in Chrome at 390 and 1280 pixels wide, with scripts on and
  off and with reduced motion: no sideways scrolling, one `h1`, 44-pixel targets. The author
  captured all seven and confirmed the looks differ as the tones say.
- **Independent review:** a fresh agent read all fourteen pieces against the skill and the source.
  Tone fidelity scored 78 to 92 (visionary 92, storyteller 90, explainer 88, emotional 86, analyst
  80, executive brief 80, practical instructor 78). It found ten problems, all fixed the same day:
  two factual (a post that called the invented course "real", and a quote cut so it lost its
  meaning), plus "so what" lines that did not follow their findings, a missing "Draft
  recommendation" label, a board memo that invented its readers, and a page that drifted out of
  the first person.
- **Not checked:** whether a real reader finds each tone right, and these pages in other browsers.

## 21 November 2026: colour rebalanced to 60-30-10

At the owner's request every page was rebalanced to one dominant colour, one secondary and one bold
accent, with clean backgrounds on most. A new script, `workshop/tools/check_colour_balance.py`,
measures each role's share of the page with photos hidden. All seven pass at 1280 and 390 pixels:

| Tone | 60 / 30 / 10 at 1280 px | Accent |
| --- | --- | --- |
| Visionary | 67 / 26 / 2 | electric yellow on black |
| Storyteller | 67 / 23 / 3 | vermilion on warm off-white |
| Emotional | 62 / 30 / 6 | rose on warm paper |
| Explainer | 71 / 24 / 2 | marker yellow on white |
| Practical instructor | 66 / 26 / 2 | orange on off-white |
| Analyst | 64 / 27 / 3 | data blue on white |
| Executive brief | 69 / 23 / 3 | oxblood on paper |

The rest is lighter tints, borders and greys. Body text contrast is 8.7 to 1 or better on every
page; button labels are 5.7 to 1 or better.

## Still to test

1. ChatGPT and Gemini on the same three cases.
2. A brand tone file reused on two pieces.
3. The hand-off: Tone Studio's words built by Artifact Studio into a deck.
