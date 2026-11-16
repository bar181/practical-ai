# Artifact Studio: final review before the merge to main

Written on 15 November 2026 by the assistant that built it, with no second reviewer. Read it as
the author marking their own work.

**Think of it as** a house that photographs well and has passed its own inspection, and that
nobody has lived in yet.

**Overall: 70 out of 100.** The library is complete and checked. What holds the score down is
evidence: almost nothing has been tried by anyone but its author.

## Scores

| Item | Score | Why |
| --- | --- | --- |
| The landing page | 86 | A hook, four callouts, one picture, then "Try it in five minutes". Not yet seen rendered on GitHub by the author of this review |
| The kitchen sink, `base/studio.html` | 90 | One file, 46 tabs. Every tab checked at three widths in Chrome for script errors, sideways scroll and accessibility |
| Worked examples, `base/examples/` | 66 | Ten files, each with a prompt and sample input. Every finished page is a hand-built reference. None is the output of running its prompt |
| The paste-in instructions | 60 | Run once in a fresh Claude session: 6 of 6 on the skill's test. That run found six contradictions, listed below. They are not fixed |
| The one-link prompt | 55 | The link opens. Never tried from inside ChatGPT, Gemini or any chatbot other than Claude |
| The skill and the MCP server | 70 | Pass their own checks. No second agent has run the skill. The server has not been tried in a desktop assistant |
| Honesty of the status lines | 92 | Each says who has and has not tried the thing. Estimates are labelled |
| Accessibility and devices | 74 | Automated scan clean in Chrome. No real phone, Safari, Firefox or screen reader |
| How clean the repository is | 72 | The showcase is tidy. Nine older drafts and the project method still use an earlier layout |
| Evidence of real use | 15 | None. Nobody has presented a deck, sent a report or published a post made with it |

## Open before anyone relies on it

1. **Six contradictions in the paste-in instructions.** They concern: the number of colours
   (four to six in one place, seven in another); the counts of recipes and voices; the heading
   rules; the accent colour against the data colour; what the delivery note covers; and gap
   markers, where every gap is marked on the page with no split between a gap that blocks the
   page and one that does not.
2. **Run each worked example's prompt** in a fresh chat and either replace the reference with the
   real result or keep the label.
3. **Run the beginner prompt in ChatGPT and Gemini.**
4. **The pictures.** Settled on 15 November 2026: the owner confirmed he made every supplied
   picture with AI image tools. Two more, the lake and the sunset, are his photographs.
5. **Size.** `base/` is 9 MB: the kitchen sink is 2.9 MB and the examples carry their own fonts
   and pictures.
6. **Branch protection on `main`** could not be set by the assistant. The owner sets it by hand.

## What changed in the last session

One kitchen sink in place of two files. A worked example for each of seven voices, for post
previews and for photo effects. Post previews for six platforms. A personal story voice. Public
links pointed at `main`. Two named inspirations replaced with descriptions of a style.

The lessons for the next build are in
[the build process](../../plans/plans-template/BUILD-PROCESS.md#what-the-first-build-taught-us).
