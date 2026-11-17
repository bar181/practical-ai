# Decision support

Ask a business question and get a one-page brief: the facts with sources, the options compared by
a written rule, a SWOT, and a recommendation you check and share. You decide.

**Status, 16 November 2026.** The steps were tested by fresh Claude sessions on two invented
decisions, as instructions in an earlier format. This `SKILL.md` version has not been run yet, and
no other chatbot has tried it. Nobody has used it on a real decision.

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
- Your business, once: what you sell, where, your size, three goals, your limits, your comfort
  with risk, and who else has a say. It saves this as a profile so it never asks again.
- Any facts you already have, such as quotes or prices. Optional.

## What you get

The working (options, research, scores), then a brief of about 400 words: the decision, the
recommendation, why, a SWOT, risks, next steps, what would change it, assumptions and sources.
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

| Check | Result |
| --- | --- |
| Paste `SKILL.md` into a fresh chat and run the worked example | Not yet run |
| Run a different decision | Not yet run |
| Asks for missing context in one reply, applies the stated limits and goals, flags uncertainty | Not yet run |
| The same file in a second chatbot | Not yet run |

The earlier format had nine fresh-session runs on two decisions (a bakery's catering, a
landscaper's truck). In the last run of each, the recommendation followed the scores and the rule,
with one blocking point each, since fixed and not re-tested. [The logs](../../../../plans/archive/agentic-process/v1-project/level-3-files/test-runs/decision-support/).
