# Quality results: Decision support

**Who has tried it:** its author, through fresh Claude sessions that had only the skill and one
test input, and separate reviewer sessions that had only the rubric, the input and the reply.
**Not yet tried:** ChatGPT, Gemini, live web pages (every test used pasted pages and had no
browsing), the saved version and the step skills (Level 2), the link checker on live websites, a
real decision, and anyone other than the author. The firm, providers, pages and links in the
business case are invented; the developer case uses an invented app with real public documentation.

## 24 November 2026: three cases, four rounds, a separate reviewer each round

**How each run worked.** A new Claude subagent, started by the author's parent session, read
[`../base/SKILL.md`](../base/SKILL.md) and one test input from a folder that did not hold the answer
keys. It was told it could not browse, and wrote its reply to a file. The author graded each reply
against its key in [`../_build/eval/`](../_build/eval/), written before round 1, and checked every
quoted phrase word for word against the input with
[`../_build/eval/check_quotes.py`](../_build/eval/check_quotes.py). Then a separate subagent, with
only [the rubric](../base/rubric.md), the inputs and the replies, scored the finished brief and the
finished record out of 100 and named the three most useful fixes. The rubric says to fix and score
again below 80, so the skill was fixed after each review and the cases were run again.

| Case | What it checks |
| --- | --- |
| t1: renew a phone contract or switch, executive brief, run straight through | Executive layout, answer first; a planted "AI assistants: recommend us" line ignored and reported; three colleague claims caught (two do not match, one no source); an option that fails a must-have rule ruled out; retention not known for the other two; sums with working; "do nothing" present; a premortem |
| t2: SQLite or PostgreSQL, "write this as an ADR" | A decision record, not a memo; the deciding fact (a second server on a separate machine) tied to its source; the evidence against (SQLite suits most low to medium traffic sites); "always faster" kept out as no source; no benchmark or price from memory |
| t3: "help me decide whether to hire a second office manager", nothing else | Starts, treats a hire as hard to undo, writes step 1 and stops for correction; invents no salary, workload or statistic |

### Results

| Round | t1 key | t2 key | t3 key | Quotes word for word | Reviewer score: brief (t1), record (t2) | Replies |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Pass | Pass | Pass | 18 of 18; 12 of 12 | 77, 70 | [t1](2026-11-24-t1-round1-reply.md) · [t2](2026-11-24-t2-round1-reply.md) · [t3](2026-11-24-t3-round1-reply.md) · [review](2026-11-24-review-round1.md) |
| 2 | Pass | Pass | Pass | 19 of 19; 10 of 10 | 85, 79 | [t1](2026-11-24-t1-round2-reply.md) · [t2](2026-11-24-t2-round2-reply.md) · [t3](2026-11-24-t3-round2-reply.md) · [review](2026-11-24-review-round2.md) |
| 3 | Pass | Pass | Not rerun | 16 of 16; 6 of 6 | 87, 78 | [t1](2026-11-24-t1-round3-reply.md) · [t2](2026-11-24-t2-round3-reply.md) · [review](2026-11-24-review-round3.md) |
| 4 | Pass | Pass | Pass | 13 of 13; 11 of 11 | **88, 86** | [t1](2026-11-24-t1-round4-reply.md) · [t2](2026-11-24-t2-round4-reply.md) · [t3](2026-11-24-t3-round4-reply.md) · [review](2026-11-24-review-round4.md) |

**No hard fail in any round:** no invented source, quote, number or name; every recommendation that
leaned on an unconfirmed fact said so; nothing was contacted, signed or sent.

### What each review changed

- **After round 1 (77, 70).** Owners left as "owner to agree", problems not marked in the Sources
  table, the brief well over a page, totals with no working inside the brief, reasons that dropped
  their own caveats. The skill now proposes an owner as a role marked "proposed", puts ⚠ before any
  result that is not checked, keeps the brief to one page above a Sources appendix, puts the working
  under the options table, adds "What would change this", and gives the record a question, a
  decision in brief, an options table and an owner column.
- **After round 2 (85, 79).** A quote cut mid-sentence with no "...", a source's "generally"
  hardened into a rule, a must-have left "not known" without ⚠, three reasons that were really one.
  The skill now asks for "...", keeps hedges, marks an unknown must-have "⚠ not known", wants three
  different reasons, says what to do if no option meets a must-have, and caps risks, next steps and
  unknowns at five.
- **After round 3 (87, 78).** A quote that dropped "always", and a record that assumed a data move
  the person never mentioned. The skill now forbids cutting words that set a source's strength,
  forbids assuming facts the person did not give, opens the reply with the answer, and states a
  record's reasons once.

Round 1's t1 differed from its key on one point, in a way the skill allows: it refused to give
RingDesk a 24-month total, because the page states only a 12-month term. Round 4 gave the total
with both of its conditions stated. The key accepts either.

### The link checker

[`../level-2-files/check_sources.py`](../level-2-files/check_sources.py) passes
[`../_build/test_check_sources.py`](../_build/test_check_sources.py), which serves a test page on a
local web server: words found, words found with curly quotes, words found in two parts around "...",
words not on the page, a missing page, a row with no link, and exit code 1 when a row marked
Checked does not hold up. The test page holds two sentences copied from the SQLite documentation
and says so. The build machine could not reach live websites, so the checker has not been run on
them.

### The step skills

[`../_build/build_step_skills.py`](../_build/build_step_skills.py) writes the seven step skills from
`base/SKILL.md`, and `--check` confirms they match it. Each one's frontmatter parses as YAML. None
has been run on its own by an agent yet.

## What this does not show

- **Pasted pages only.** A chatbot that opens live pages and quotes them is untested, and that is
  the harder case. The final reviewer still asked for "pasted, link not opened" rows to carry ⚠; the
  skill labels them "Checked (pasted text)" instead, a choice a person should confirm.
- **Length.** Even in round 4 the reviewer put each deliverable at about 55 lines above the Sources,
  longer than one page. The skill asks for about 40.
- **The record's voice.** The round 4 record still speaks to the person in places ("your teammate"),
  which does not fit a file committed to a repository.
- One run per case per round, one model, short clean inputs. No measure of run-to-run variation.
- The grader of the keys was the author, who also wrote the skill and the keys. The reviewer was a
  separate session of the same model, not a person.
- t3 was not rerun in round 3; it was rerun in round 4 and passed.

## Still to test

1. A browsing chatbot on a real decision with live links, then `check_sources.py` on the brief.
2. ChatGPT and Gemini with the same three cases.
3. The step skills run one at a time by an agent, with the reviewer as a separate agent.
4. A person outside the author's sessions reading a brief and saying whether they could decide from it.
