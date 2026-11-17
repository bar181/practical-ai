# First-visit friction log: Artifact Studio starter guide

Tester: a first-time visitor playing both the visitor and the chatbot.
Files made: `sample-report.html` (step 1 notes), `my-report.html` (own notes, step 3).
Phone-width checks were done with headless Chrome at 390 px (`shots/`), not a real phone.

**Totals: 0 BLOCKING, 12 MINOR.**

## Time per step

| Step | Agent clock | Estimated for a human visitor |
| --- | --- | --- |
| Read README top to the starter guide | about 5 s | 2 min |
| 1. Copy the sample, paste, link fails, find fallback, "chatbot" reads guide and builds page | about 70 s | 3 to 4 min (more if the link failure is noticed only after the reply) |
| 2. Compare with the capture and with `base/examples/report.html` | about 10 s | 2 min, plus confusion from point 1 below |
| 3. Own notes (five bullets, bakery, co-owner reader, navy) | about 70 s | 5 min |
| 4. Four-point check and fixes | about 15 s | 3 min, but "open it on your phone" has no how-to |

The "5 minutes" promise holds for steps 1 and 2 only if the chatbot can open the link.

## Friction points, in the order I hit them

1. **MINOR (biggest). The capture at the top is not the page it links to, and it contains claims the notes do not support.**
   The capture headline is "October was our best month this year" and its summary says "The main cause: quotes now go out in two days". The notes give only September and October and state no cause. The alt text and "The capture, in words" repeat "best month this year". Yet the text says the page was made "in one try, unedited" and "Open the page" leads to `base/examples/report.html`, whose headline is "October beat September: revenue up $12,700...". So either the capture is from another run or it is the hand-built library version. Either way the showcase image commits exactly the error step 4 tells you to catch ("Nothing is added that you did not write"). Step 2 then says "You should get a page like the one above", which points at the image, not the file.
   Fix: re-capture `base/examples/report.html` and rewrite the alt text and "in words" paragraph to match it.

2. **MINOR. The prompt in step 1 is hard-wrapped at about 40 characters mid-phrase** ("two / crews", "15 / November", "an HTML / page"). It pastes fine into a chatbot, but it looks broken and makes step 3 ("replace everything after `from these notes:`") easier to get wrong. Wrap by bullet, not by width.

3. **MINOR. The fallback for a chatbot that cannot open the link sits in step 2, after you have already pasted.** Here the WebFetch of the raw GitHub link failed (not reachable). A visitor learns this only from the chatbot's reply, then has to scroll on to step 2. Put the fallback in step 1.

4. **MINOR. The fallback itself made me guess.** It links to the GitHub blob page ("press the copy button at the top right") but never names the local path `base/AI-INSTRUCTIONS.md` for someone with a downloaded copy. It says paste it "before the notes" but not whether to keep or delete the "Read the design guide at <link>" line.

5. **MINOR. Guide vs reader request: where does the decision go?** The prompt says the reader "wants the answer first" (and the step 3 example says "She wants the decision first"). The guide says a decision gets its own section "placed directly before the next steps", that is, near the bottom, and is only named in the top answer. I had to choose. I named the decision in the headline and answer, kept its section where the guide says, and (in my report) added a "Go to the decision" link.

6. **MINOR. Guide conflict on note length.** For a beginner request the guide says "one line under each of the four headings", but the colour section says "List the contrast ratio of each text and background pair in your note" and the word-only colour rule says "give its hex code under Assumed". Those cannot fit in one line. I gave the ratios on one dense line.

7. **MINOR. The analyst voice forces `[needs: owner]` on every next step.** The notes never name owners, so a beginner's first page shows code-like yellow tags on both next-step cards. Correct by the rules, but the README never says these tags will appear or what they mean (see point 10).

8. **MINOR. Step 3 says "Keep the first line, the one with the design guide link".** The link is on line 2 of the block, and lines 4 and 5 ("Then show me a one-page report as an HTML page, from these notes:") must also be kept. It should say "Keep everything up to and including `from these notes:`". It also does not say that this drops the "tell me three ways I could tailor this" line.

9. **MINOR. Naming the reader.** I wrote "My co-owner Dev reads this on his phone...". The guide names a real person on the page only "if the notes say they agreed". Is the reader line part of "the notes"? I guessed no name on the page ("For: co-owner").

10. **MINOR. `[needs: ...]` markers are never explained in the README.** My notes gave sales and the oven repair without a currency, so the page shows `[needs: currency]` three times. That is the guide working as designed, but a visitor meets it unexplained. Step 4 should add: "Fill or accept every `[needs: ...]` tag."

11. **MINOR. "Open it on your phone" has no how-to.** Step 2 covers "it shows code, not a page", but nothing says how to get a chatbot artifact or an HTML file from a desktop chat onto a phone (share link, email the file, open the chat on the phone). I substituted a 390 px headless Chrome render.

12. **MINOR. The four-point check has no line for implied causes.** The commonest addition I found (and the one in the README's own capture) is causal language: "the main cause", "this bears on". Check 2 ("no new names, dates, quotes or claims") covers it only if the visitor reads "claims" broadly. Suggest: "Nothing says one thing caused another unless your notes say so."

## Did the result look like the capture?

Mostly yes in shape: green eyebrow, big headline, two-sentence summary, three tiles (revenue, jobs, quotes won) each with "up from", a September vs October bar chart with grey and green bars, what changed, and tagged next-step cards ("Decide by 15 November"). Differences: my headline says "October beat September on revenue, jobs and quotes won" (no "best month this year", which the notes do not support); the analyst voice gave each finding its own chart and "so what", plus a Method and limits section and `[needs: owner]` tags. It looks much more like `base/examples/report.html` than the capture, which is the point of friction 1.

## Did the four-point check catch anything?

Yes, on the sample report, check 2 (nothing added) caught three inferences the "chatbot" had written:
- "four more jobs than September, **with the same two crews**" (notes do not say the crew count was the same in September),
- "The crews shared **the other van**" (notes say only "Crews shared"),
- "**This bears on the van decision below**" (an editorial link the notes do not make).
All three were fixed in `sample-report.html`. Checks 1 and 3 found nothing: every number matched and derived numbers show their working (12,700 and 17.8%; 7,500 and 13.8%; 42 and 60%). On `my-report.html` nothing was added; the three `[needs: currency]` tags and the open question on the 6 cancellations are honest gaps. Check 4 could only be approximated (see point 11).

## Appendix: inputs and the chatbot's delivery notes

### My notes (step 3)

```
- Riverside Loaf: small bakery, one shop plus a Saturday farmers market stall
- Q3 sales 61,800 vs 54,300 in Q2
- market stall sales down, rained 5 of 13 Saturdays
- sourdough subscription: 112 members, was 70 at end of June. 6 cancelled
- oven repaired in Aug for 3,400. Repair again or replace? decide before 1 Dec

My co-owner Dev reads this on his phone before Monday's planning call.
He wants the decision first. Our colour is navy.
```

### Delivery note, sample report

- **Chose:** one-page report, analyst voice, quiet look built from "green" (#1d6b34 accent, #2f8a46 data); decision in the answer and as its own section before next steps.
- **Assumed:** green hue chosen by me; ratios: text 15.1:1 and secondary 6.5:1 on background, accent 6.0:1, tag text 13.5:1; currency is dollars as written; dates are November 2026.
- **Missing:** owners for both next steps (marked); costs or profit; any month before September; breakdown table left out (would repeat the tiles).
- **Check before sharing:** all figures against your notes, then look on your phone.
- **Three ways to tailor it:** put your own brand colour and logo text in the header; add your recurring numbers (for example margin) so the tiles stay the same each month; keep a "Decision needed" box at the top when your reader decides things.

### Delivery note, my report

- **Chose:** one-page report, analyst voice, navy look (#1f4e8c accent, #2b5fa8 data); decision named in the headline because the reader wants it first.
- **Assumed:** navy hex chosen by me; ratios: text 15.8:1, secondary 6.9:1, accent 7.6:1, data on panel 6.4:1; Q3 is 2026; reader not named on the page.
- **Missing:** currency (marked three times); stall sales figure; when the 6 cancellations happened; replacement oven price; no next steps beyond the decision, so that section is left out.
- **Check before sharing:** currency, the subscriber count, and the 1 December date.
