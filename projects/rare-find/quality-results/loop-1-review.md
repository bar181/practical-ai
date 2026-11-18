# Loop 1: playtest review, 17 November 2026

Scored with the [game-review skill](../level-2-files/game-review/SKILL.md) by a reviewer agent (Claude) who had
not seen the game before. I played `base/game.html` in Chromium through Playwright, served over
http, at 1280 px and 390 px, with reduced motion on and off, keyboard only, with browser storage
blocked, and with no `window.claude`. **Every Claude feature (`sample`, `db`, `user`, `room`) was
tested against a fake `window.claude` that I injected, with added delays of 0.4 to 3.5 seconds. None
of it ran against the real Claude artifact runtime.** My screenshots are in `/tmp/rf-review1/`. I
also read the automated run in `/tmp/rf1/` (35 of 35 checks passed).

**Score: 68/100. Not ready to show, but close.** The solo game is clear, quick and pleasant. Three
timing bugs give wrong scores or wrong winners, and the matcher both misses common typos and
accepts some wrong answers. Fixing those two areas would likely take it past 80.

| # | Item | Score | Evidence |
| --- | --- | --- | --- |
| 1 | First ten seconds | 13/15 | Cold open: the title, "Name a right answer nobody else thinks of. **The rarer it is, the more it scores.**" and a big yellow "Play solo" button. I knew what to press at once. Lost points: after I picked 15s the button still says "5 prompts · 30 seconds each", and "Join my game" is the button you press to *host* a room |
| 2 | The core loop is fun | 10/15 | The ring timer turns amber at 10 s and red with a pulse at 5 s, and the reveal board highlights my row. But at the default 30 s the timer rarely bites, and there is no bet to make. The reveal shows only the top 10 and the Gems, so a Good find (75, the main reward for a rare answer) has no row to light up. The end screen shows `35 100 0 0 0` with no prompts or answers (those are hover-only titles) |
| 3 | Feedback and feel | 11/15 | The result appeared 48 ms after Enter. Points count up over about 300 ms. The tier colours are distinct, and a Gem gets confetti and a gold shimmer. Problems: the timer ring freezes on "30" after an answer and looks broken (`03-r1-result-1280.png`). The opponent's row in the reveal shrinks to 12 px grey centred text, because it reuses the ladder card's `.opp` style (`12-ladder-result-with-talk.png`, "5. Printer"). At 390 px the Next button sits at 1217 px in an 844 px screen, below the fold. A Gem looks the same size as any other result |
| 4 | Fair scoring | 7/15 | My solo round scored 35 + 100 + 0 + 0 + 0 = 135, which matches the table. But the home page says "Typos are forgiven" with no limit, and the game does not forgive "Gana", "Kael", "Leak", "Pees", "Brocolli", "Morroco" or "Carots". It does accept wrong answers: "Spider Woman" counted as "Spider-Man" (35) and "Sedan" counted as "Sudan" (Good find, 75). "Toy Story 2" counts as "Toy Story", but "Cars 2" is a Miss. Correct answers that are not listed ("Sweet potato", "Mushroom", "Swivel chair", "Batwoman") get a red **Miss 0** badge. The line "is not on our list" is honest, but the badge says the player was wrong. Two timing bugs give wrong totals: see the next two rows and fixes 1 and 2 |
| 5 | Usable by everyone | 7/10 | I played a whole game keyboard only. Tab reaches every control, focus moves to the answer box and then to Next, and the focus ring is clear. 390 px has no sideways scroll. Reduced motion is respected (no confetti, the points appear at once, no timer pulse). Fails: the locked ladder names (50% opacity) measure 4.16:1 and their roles 2.83:1. The whole result card, including about 15 rows of the reveal, is one `aria-live` region, so a screen reader would read a long list or nothing. I had no real screen reader to confirm |
| 6 | Opponents feel alive | 7/10 | There are four co-workers (Penny, Gus, Marge, The Archivist) with their own emoji, roles and skill levels, and the header shows a running score ("🙋 Penny: 50"). Each "thinks" with animated dots, then answers. The ladder saved, and survived a reload with the mocked `db`. But every opponent thinks for exactly 0.9 s, and without the AI all four use the same lines. A player who presses Enter twice never sees the opponent at all |
| 7 | Trash talk | 3/5 | Kind, short, and it has an off switch. Without the AI the line is chosen by tier, not by the answer ("Safe choice. Very safe."). It only appears in the ladder. With a 3.5 s mocked AI delay, the line about my prompt 1 answer ("Labrador Retriever") showed on prompt 2's result for about 1.5 s before being replaced (`20-trash-talk-about-previous-answer.png`) |
| 8 | Robust | 5/10 | Without `window.claude` there were no network requests and no errors. The AI box, party button and board all hide, and blocked storage degrades quietly ("saved in this browser when it allows it", with no false "Progress saved"). But in the ladder, a fast Enter, Enter threw `Cannot read properties of null (reading 'm')` twice, offline too. The party host's prompt 2 inherits prompt 1's deadline: after a 16 s reveal, prompt 2 opened already "Out of time" (`22-party-prompt2-instant-timeout.png`, mocked room). There is no way to quit a game in progress |
| 9 | Honest and safe | 5/5 | "Popularity is the AI's estimate, not a survey." is on the home page and under every reveal. AI-made prompts are labelled "made by AI". There is no copied branding or art, only answer names. Nothing I saw was hurtful |

## Fix first

1. **Stop late callbacks from landing on the wrong prompt or the end screen.** Where: `showResult`
   (the 900 ms opponent `setTimeout`), `trashTalk`, the `#b-judge` handler, and `endGame`. Evidence
   from three cases:
   - Offline ladder, Enter Enter: the end screen said "Penny wins, 85 to 25" while Penny's real
     total was 145. The same race can award an undeserved ladder win.
   - Asking the judge, then pressing Next: five Misses ended with a final score of 75, saved as
     "best" (`21-phantom-judge-points-end.png`). The screen said "The judge could not be reached.
     It stays a miss."
   - The two uncaught errors above.

   Add the opponent's points when the answer is submitted, not when they are shown. Tag each async
   call with the round and ignore stale ones. Keep Next disabled until the opponent has answered.
   Raises item 4 (+3), item 8 (+3) and item 6 (+1).
2. **Give each party prompt a fresh deadline.** In the `#b-next` host branch, `partyBroadcast` copies
   the old `G.endsAt`. Set `G.endsAt = Date.now() + S.timer*1000` first. Raises item 8 (+1).
3. **Make the typo rule match what the home page says, and stop the false matches.** Allow one edit
   from five letters up ("Gana" is the exception you choose). Try the singular before the typo
   check, so "Carots" works. Reject a typo match that changes a whole word or a number ("Spider
   Woman", "Toy Story 2"), and check the edited input is not just another real word ("Sedan"). Then
   write the rule on the home page: "Small typos are forgiven in words of five letters or more."
   Raises item 4 (+3).
4. **Stop calling unlisted answers a Miss.** Show a neutral grey "Not on our list · 0" badge, and when
   the AI is there, ask the judge automatically. Add the obvious gaps to the packs (sweet potato,
   mushroom, swivel chair, Batwoman, orange juice). Raises item 4 (+1) and item 2 (+1).
5. **Make the reveal pay off every rare answer.** Add a "Your answer" row when it is a Good find, so
   it lights up like the others. Give a Gem a full-width "GEM!" moment, not just the same badge. Put
   prompts and answers on the end screen, not only in hover titles. Raises item 2 (+2) and item 3 (+1).
6. **Rename the reveal's `.opp` class** (for example `.opp-pick`), so the opponent's row stops picking
   up the ladder card's 12 px grey centred style. Raises item 3 (+1).
7. **Phone layout of the result:** put Next above the reveal or make it sticky, and on narrow screens
   show the Gems before the popular list. Raises item 3 (+1) and item 5 (+1).
8. **Small polish on the timer and labels:** hide or dim the timer ring once an answer is in, and
   update "30 seconds each" when the timer setting changes. Raises item 1 (+1) and item 3 (+1).
9. **Give opponents their own voice offline:** lines per co-worker, and thinking time that varies with
   skill (Penny fast, The Archivist slow). Raises item 6 (+1) and item 7 (+1).
10. **Screen readers and contrast:** add a short live region ("Gem, 100 points. Penny said Desk,
    Crowd pick, 25") and take the reveal list out of `aria-live`. Raise the locked ladder cards above
    4.5:1. Raises item 5 (+1).

## What I could not test

- **The real Claude runtime.** Every AI, saving and party result above comes from my fake
  `window.claude`. I could not confirm:
  - that `window.claude.use("sample")`, `db.doc(...).get()/set()`, `db.collection(...).orderBy()`,
    `user.profiles()` and `room.join/emit/on/presence/onPeers` match the real API shapes;
  - real model delay and the quality of what it writes;
  - whether the new-category refusal works (the mock never refuses).
- **Real AI trash talk wording.** The mock returned placeholder text, so I could not judge whether
  the lines are funny, specific or kind.
- **A real multi-device party.** The mock room does not relay messages between players. I saw the
  guest view only by injecting a host message. Guests see no "waiting for the host" text after
  answering, and no one sees the room's standings at the end. I scored the beta lightly for this.
- **A real screen reader, a real phone with touch, and ChatGPT.** For ChatGPT I tested only that the
  game works with no `window.claude`.
