# Decision support

Ask a business question and get a one-page brief: the facts with sources, the options compared by
a written rule, a SWOT, and a recommendation you check and share. You decide.

**Status, 16 November 2026.** Passed the three-input check in fresh Claude chats (below). No
other chatbot has tried it, and nobody has used it on a real decision.

**What already exists:** any chatbot with web search will research a question and recommend
something when asked. What it lacks is a fixed rule for weighing the options against your goals
and limits, a date on every source, and labels on every estimate. This file adds those; it builds
no software.

## Try it: paste one file (5 minutes)

1. Open [`SKILL.md`](SKILL.md), press **Raw**, and copy all of it.
2. In any chatbot that can search the web, start a new chat and paste it. On a new line, type
   your decision: *My decision: should we start weekday catering for offices near our shops?*
3. The first time, it replies once with what it needs to know about your business. Answer, and it
   writes the brief.

**Shortcut:** if your chatbot can open links, send *"Follow the instructions at [the Raw link to
SKILL.md]. My decision: ..."* instead of pasting.

## What to give it

- Your decision, in one sentence.
- Your business: what you sell, where, your size, three goals, your limits, your comfort with
  risk, and who else has a say. It writes this up as a profile. Save the profile in your Project,
  or paste it into your next chat.
- Any facts you already have, such as quotes or prices. Optional.

## What you get

A short answer you can forward, then a brief of about 400 words, then the working (options,
research, scores), then what to check. The brief has: the decision, the recommendation, why, a SWOT, risks, next steps, what would change it,
assumptions and sources.
[See the worked example](example.md): an invented bakery deciding on office catering.

## Check before you act

Every figure against its source, every line marked **assumed**, **estimate** or **proposal**, and
whether the recommendation fits your goals. Use real business figures only if your workplace
allows that chatbot for them.

## Save it (Level 2)

So you never paste it again:

- **Claude:** add `SKILL.md` as a skill (keep it in a folder named `decision-support`), or paste
  it into a Project's instructions.
- **ChatGPT** Project or **Gemini** Gem: paste it into the instructions.

Save your business profile as a file in the same project.

There is no Level 3. A person starts every decision, so nothing needs connecting.

## The check

Run on 16 November 2026, each in a fresh Claude chat with web search, only `SKILL.md` and one
message, and no way to ask questions. [The logs](../../../../../docs/reports/2026-11-16-decision-support-checks/).

| Check | Result |
| --- | --- |
| The decision only, no business profile: asks for what is missing in one reply, and waits | **Pass, after one fix.** The first run asked again for the decision it had just been given. The Start section now repeats the decision back and asks only for what is missing; the rerun passed |
| The bakery example: a shareable brief that applies the limits and the scoring rule and keeps sourced facts, estimates and assumptions apart | **Pass.** Every figure dated or labelled, each limit tested pass or fail, the rule applied, judgement calls listed. Blind graders then found the useful part buried, so the reply now opens with a three-sentence answer to forward, then the brief, with the profile at the end. Two reruns passed; the last is the [worked example](example.md). Known rough edge: when a deciding fact is not found, the rule can say "do nothing leads" while recommending the trial as the check, which it discloses but which reads awkwardly |
| A different decision with a fact that cannot be found (a dog groomer weighing a mobile van) | **Pass.** It flagged local prices, insurance and staff capacity as not found, recommended a cheaper trial with a check first (an insurance broker call, and calling 20 older clients with a stated price), and named what would make the van the right call. Run before the two fixes above, neither of which changes this behaviour |
| The same file in a second chatbot | Not yet run |

**Before and after.** The same bakery question went to a fresh chat with no skill. Three separate
sessions graded it blind against each version of the skill, using a rubric written before any
output was read: **86, 89 and 87 with the skill; 66, 61 and 67 without.** Every grader found the
same decision both ways: test demand cheaply, then a small capped trial. The skill's answers
earned their points by dating every source, testing every limit and following a stated rule. But
every grader said a busy owner would rather receive the plain answer, which reads like advice.
The skill is more trustworthy, not yet more pleasant. See
[the grades](../../../../../docs/reports/2026-11-16-decision-support-checks/).
