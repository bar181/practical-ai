# Friction with the guide

Blunt list. Each item quotes the line, says what was unclear and says what I did.

## 1. No recipe fits a decision brief, and the fallback fights the voice

> "If none fits, use the one-page report."

> "One-page report | Someone needs to know how a period went | Title, period, reader. Two-sentence summary. Three or four numbers with their change. One trend chart with a full-sentence heading. One breakdown table, weak row marked. What changed. What happens next."

> "Executive brief | Header: to, from, date, decision needed by. The decision. Numbered background. One options table including "do nothing". Recommendation. Risks with controls. Next steps."

This was the biggest problem. The executive brief voice is listed under two recipes (one-page report and proposal), and neither is a decision brief. The proposal is "A customer has to choose and say yes", which is wrong for an internal decision. The one-page report then forces a summary, three or four numbers, a trend chart and a breakdown table onto a page whose voice wants a memo with an options table and bans "More than one page". The result is seven voice sections plus seven recipe sections on one sheet. I had to drop to 9 point type in print to fit. The guide needs a decision brief recipe, or the executive brief voice needs to say which recipe sections it drops.

## 2. The tie-break rule does not settle the cases it creates

> "Where the recipe and the voice disagree, the voice sets the order, the counts and the headings. The recipe sets which sections the page must have."

- The voice says "One options table". The recipe says "One breakdown table, weak row marked". Is that one table or two? "The voice sets the counts" suggests one. "The recipe sets which sections the page must have" suggests two. I used one table and marked both the recommended row and the weak row in it. I am not confident that is what the guide wants.
- The voice sets the order, but the recipe's sections have no place in the voice's order. Where does the trend chart go in "Header, decision, background, options, recommendation, risks, next steps"? I put the summary under The decision, and the numbers and chart at the end of Background. That was a guess.
- "Two-sentence summary" and "The decision" overlap. So do "What happens next" and "Next steps", and "Title, period, reader" and the memo header. The guide never says a voice section can stand in for a recipe section. I merged them.

## 3. "No images" against "one trend chart"

> "A paper page, serif, one accent, no images, no motion."

> "One trend chart with a full-sentence heading."

Is a chart an image? The guide does not say. I drew the bars in HTML so no image file or drawing is involved, and kept the chart because the recipe requires it. A stricter reader would have cut it.

## 4. "More than one page" has no meaning on a screen

> "Avoid: More than one page"

> "Design at 390 pixels wide first."

A phone has no pages. At 390 pixels this brief is about 3,000 pixels tall, roughly three and a half screens. I read "one page" as one printed sheet, wrote a print layout, and checked it on A4 and US Letter. The guide should say what a page is: a printed sheet, a word count, or a number of screens.

## 5. The line-length rule and the one-page rule pull against each other

> "Read something through | One column, 60 to 75 characters wide"

Seven sections in a 60 to 75 character column do not fit one sheet at a comfortable size. I kept the measure for running text, let the table and chart run wider, and shrank the type. The guide gives no order of priority between a layout idea and a voice's "avoid" line.

## 6. Required header fields with no data

> "Header: to, from, date, decision needed by."

> "A gap is never filled with a guess. If the page would mislead without it, a number, a name, a date or a price the reader will act on, mark it on the page as `[needs: ...]`. Otherwise leave the page clean and list the gap under Missing."

The notes give no sender and no date. A missing sender does not exactly "mislead", so the rule says leave the page clean. But the voice requires the fields, so leaving them out breaks the voice. I marked both with `[needs: ...]`. The guide should say what to do when a section the voice requires has no content: mark it, or omit it.

## 7. The voice demands judgement the person did not supply, and the guide only talks about facts

> "The person's content is the material. You add structure and craft. You never add facts."

> "One options table including "do nothing". Recommendation. Risks with controls."

The notes contain no options list, no recommendation and no controls for three of the four limits. The voice requires all three. Is a recommendation a fact? Is a proposed control? Is deciding what "do nothing" means? The guide is silent. I wrote them, labelled my controls "proposed" on the page, and listed every one under Assumed. A stricter reading would leave the Recommendation section as `[needs: your recommendation]`, which would make the brief useless. The guide needs one sentence on whether the assistant may recommend.

## 8. "Infer what you can" against "never filled with a guess"

> "Infer what you can."

> "A gap is never filled with a guess."

Where is the line? I labelled the 22, 28 and 31 bars February, March and April. The notes say "then 22, 28 and 31" and that the trial ran February to April. That is an inference so safe it barely counts, and it is still not in the notes. Same question for "No tool cost" under do nothing. I inferred and listed both under Assumed.

## 9. Supplied content the voice has no place for

> "The person's content is the material."

The notes include a customer story ("Priya wrote to three companies..."). The executive brief voice has no slot for a story. The guide does not say whether every piece of supplied content must appear. I left it out and said so in the note.

## 10. Which request tier is this?

> "One sentence (beginner) | Choose voice and look yourself. Give the short note"
> "Names recipe, voice, look, parts (advanced) | Follow them exactly"
> ""Use the artifact-studio skill" (expert) | Every step, the check, and the note in full"

The request was "Read the design guide ... and follow it", plus a paragraph that describes a voice without naming it, plus notes. It is not one sentence, it names no recipe or look, and it does not say "use the artifact-studio skill". I treated it as the full version. The table has no row for the commonest case: a few sentences and a pile of notes.

## 11. "Preferences" catches things it does not mean

> "If there is a preferences file (a file named `preferences.md`, or a section headed Preferences in your instructions), read it before you choose anything. It sets the defaults for recipe, voice, look, layout and format."

A general assistant with a memory feature has a section called Preferences that holds writing habits and nothing about recipe, voice or look. Mine held "no em-dashes". Read literally, that section counts. I applied the one line that bears on a page and reported it. The guide should say what a preferences section must contain to count.

## 12. Loading a design skill has no stated rank

> "If a front-end design skill is available (for example `frontend-design`), load it as well."

One was available, so I loaded it. It tells the designer to avoid a cream page with serif type and hairline rules as an overused default, and to take visual risks. The voice's look is "A paper page, serif, one accent". The guide does not say which wins. I let the guide win wherever it gives a rule and used the skill only for the free choices (a cool paper tone and a blue accent, not cream and terracotta). The line also sits awkwardly with this test's rule to read only the named files. I judged that loading a skill is not reading a file on the machine, but the test's author may disagree.

## 13. Small things

- > "Seven named colour tokens at most, plus one data colour if the page has a chart."

  The comparison bar ("before the trial") needs a second, quieter treatment. The Analyst voice mentions "grey for comparison" but the build rules do not. I drew it as an outline in the secondary text colour.
- > "Totals add up and derived numbers show their working"

  Where? On a one-page brief I put the sum in brackets after the number. The guide does not say whether working belongs on the page or in the note.
- > "One accent, used only for what to act on."

  The Colour section also lists "a soft highlight" as one of the seven colours. It is not clear whether a tinted row behind the recommended option counts as a second use of accent. I used it.
- > "Three or four numbers with their change."

  The notes have four measures that changed. One of them (site visits) is the chart. The guide does not say whether the chart's measure counts as one of the numbers. I showed three numbers and the chart.
- > "Show the page as a rendered page if you can"

  Not possible when the deliverable is a file on disk. No friction with the guide, only with this test.

## A note on how I ran the test

My first command listed the `/tmp/runs` folder itself, so I saw the names of the other run folders. That breaks the rule against looking at other folders. I did not open or list the inside of any of them, and nothing from them was used.
