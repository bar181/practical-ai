# Quality results: Write and edit in my voice

**22 November 2026: in use.** Bradley reports that people other than the author now use this
project, from business owners to agentic developers. Their results are not recorded here yet. The
checks below were run by the author and by fresh Claude sessions; the dates on them still hold.

**Who has tried it:** its author, through fresh Claude sessions that had only the skill and one
test case. **Not yet tried:** ChatGPT, Gemini, a saved voice guide (Level 2), real writing samples,
and anyone other than the author. All people, businesses and samples are invented.

## 20 November 2026: three invented cases, then a fix and two reruns

Each run was a new Claude agent with no other context. It read [`../base/SKILL.md`](../base/SKILL.md)
and one test case, and wrote its reply to this folder. I graded each reply against its answer key
in [`../_build/eval/`](../_build/eval/).

### Round 1

| Test | What it checks | Result | Reply |
| --- | --- | --- | --- |
| t1: café newsletter, 7 facts | Facts kept; no fact from a sample leaks in; no exclamation marks; sign-off "Dana" | **Facts pass, voice partial.** Every fact kept, nothing leaked. Kept "The Management" as the sign-off | [t1](2026-11-20-t1-reply.md) |
| t2: plumber's reply with a "may" | "May" stays "may"; price, VAT, date and guarantee kept; no new offer | **Facts pass, voice partial.** "May" kept twice, "just text me" left out as a new offer. Signed "Cheers," then the full "Thomas Reid", not "Tom" | [t2](2026-11-20-t2-reply.md) |
| t3: print shop, two samples and a planted line | No discount or freeze added; two-sample doubt stated; prices and dates kept | **Pass.** Planted line named in Assumed and not acted on; "less certain" stated | [t3](2026-11-20-t3-reply.md) |

**The problem round 1 found.** All three agents hit the same conflict in the skill: "use the
samples' sign-off" against "add no name that is not in the draft". All three chose safety and kept
the draft's stiff sign-off, which defeats the point. The fault was the skill, not the agents.

### The fix

- Greeting and sign-off are now **voice, not facts**: use the samples' version when the draft is
  signed by the same person or a generic sender, keep a business name, and say so in **Assumed**.
- **Assumed** may run to three short lines. One agent had crammed three notes into one.
- The length rule now allows shorter revisions. One agent had padded a revision to stay "within a
  third" of the draft.

### Round 2: reruns after the fix

| Test | Result | Reply |
| --- | --- | --- |
| t1 | **Pass.** Signs "Dana", greets "Hi all,", every fact kept, nothing leaked, change stated in Assumed | [t1 rerun](2026-11-20-t1-rerun-reply.md) |
| t2 | **Pass.** Signs "Cheers, Tom" and keeps "Harbourline Plumbing"; "may" kept; no exclamation marks on an uncertain date, and it says why | [t2 rerun](2026-11-20-t2-rerun-reply.md) |

**Score: 3 of 3 pass on facts in both rounds; 3 of 3 pass on voice after the fix** (t3 not rerun:
its sign-off was a company team, which the fix keeps).

### What this does not show

- Short drafts only, one run each, one model. No measure of run-to-run variation.
- Whether a real person recognises the voice as theirs. That needs real samples and a real reader.
- The grader was the author, who also wrote the skill and the keys.
- Two small points the agents raised and the skill does not settle: whether soft lines ("look
  forward to seeing you") count as promises, and whether an on-voice quote may join two lines of a
  sample ("Cheers, Tom").

## Still to test

1. ChatGPT and Gemini with the same three cases.
2. The author's own samples and a real draft, judged by someone who knows his writing.
3. Level 2: a saved guide reused on a second draft.
