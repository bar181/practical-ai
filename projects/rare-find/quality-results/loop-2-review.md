# Loop 2: playtest review, 17 November 2026

Scored with the [game-review skill](../level-2-files/game-review/SKILL.md) by a reviewer agent (Claude)
who had not seen the game before. I played `base/game.html` in Chromium through Playwright, served
over http, at 1280 px and 390 px. I also played with reduced motion on, keyboard only, with browser
storage blocked, with every outside request blocked, and with no `window.claude`. **Every Claude
feature (`sample`, `db`, `user`, `room`) was tested against a fake `window.claude` that I injected,
with delays of 0.3 to 6 seconds plus a judge that hangs. For the party I relayed messages between two
browser tabs with a `BroadcastChannel`. None of it ran against the real Claude artifact runtime.** My
screenshots are in `/tmp/rf-review2/` and my scripts in `/tmp/rfr2s/`. I also read the automated run in
`/tmp/rf2/` (37 of 37 checks passed).

**Score: 80/100. Ready for friendly testers, not yet ready to share.** Most of the loop 1 problems are
fixed: no more phantom points, the opponent's points are fixed when you answer, Next waits for the
opponent, the phone layout has a sticky Next, and the end screen lists every answer. What holds it back
now is scoring fairness at the edges: typos that are wrongly accepted or wrongly refused, common right
answers that are not on the list, and a party mode that drops guests' answers.

| # | Item | Score | Evidence |
| --- | --- | --- | --- |
| 1 | First ten seconds | 14/15 | Cold open: "Rare Find", then "Name a right answer nobody else thinks of. **The rarer it is, the more it scores.**" and a big yellow "Play solo · 5 prompts · 30 seconds each" (`01-home-1280-fold.png`). I knew what it was and what to press at once. The subtitle now follows the timer ("5 prompts · 15 seconds each"). One point off: with Claude present, the button you press to *host* a room is still called "Join my game" |
| 2 | The core loop is fun | 11/15 | The timer ring turns red and counts "4" with a "5 seconds left" announcement (`50-timer-danger-1280.png`). The reveal lights up my row, a Good find gets its own "Your answer: Uganda 75" row, and a Gem gets a full-width "GEM!" banner (`05-r2-vegetable-1280.png`). But there is no bet to make. Prompts repeat fast: over three offline games in a row, "a superhero" and "a dog breed" came up in all three, and the reveal shows all five Gems, so by game 2 I could score 100 from memory. Common right answers score nothing offline ("Lilo and Stitch", "Toy Story 3", "Maracas", "Toilet": "Not on our list 0"), which deflates the payoff |
| 3 | Feedback and feel | 13/15 | The result appeared 8 to 21 ms after Enter. Points count up, the tier colours are distinct, and Gems get confetti and a flash. Problems: a wrong answer from the pack's wrong list reads **`Counted as "undefined"`** ("Joker" for a superhero, `06-r3-superhero-1280.png`). With the judge, Next stays locked while it thinks: 3 s normally, and **12 s** when the judge hangs ("is not on our list, and the judge could not be reached", `33-judge-timeout-1280.png`). After "The judge says no." the badge stays a grey "Not on our list" instead of turning into a Miss |
| 4 | Fair scoring | 9/15 | Every total I checked matched the table: solo 135, ladder 275 vs Penny 160, 250 vs 135, 500 vs 135, and an Enter-hammered game 325 vs 195 with the banner matching. The loop 1 timing bugs are gone in solo and ladder. But the typo rule still misfires. Wrong answers score: "Siberia" is `Counted as "Liberia"` (Good find 75), "Spanner" is `Counted as "Scanner"` (75), "Catwoman" is `Counted as "Batwoman"` (75), "Painter" and "Pointer" count as "Printer" (50), "Protector" as "Projector" (75) (`51-false-match-siberia.png`, `52-false-match-spanner.png`). And the home page says "Small typos are forgiven in answers of five letters or more", yet "Kenia", "Egipt", "Cerial" and "Lybia" get "Not on our list". It also says "Any right answer scores at least 25", which is not true offline for unlisted right answers. In the party (mocked), a guest whose judge was slower than the host's Next lost every verdict: 75 points instead of 375 |
| 5 | Usable by everyone | 8/10 | I played a whole ladder game keyboard only at 390 px with reduced motion: focus goes to the answer box, then to Next, then to "Play again". 390 px has no sideways scroll, Next is sticky at the bottom, and Gems come first (`24-ladder-result-390-after.png`). Reduced motion gave no confetti and instant counts. A short live region says "Gem, 100 points. Counted as Salsify." Fails: on the end screen the "Not on our list 0" tag and its strip tile measure **1.15:1**, dark text on a transparent tile, which makes them almost invisible (`10-end-solo-1280.png`, `27-ladder-end-390.png`). The judge's verdict is never announced: the live region still said "Not on our list, 0 points." after the badge became "Good find 75". I had no real screen reader to confirm |
| 6 | Opponents feel alive | 9/10 | Four co-workers with their own roles, emoji, think times (Penny about 0.6 s, the Archivist about 1.8 s), skill and offline lines ("Nice! Mine was way more obvious.", Gus: "Twenty-five. Low risk, low return."). Each thinks with dots, then answers with a "+50". The header keeps score ("🙋 Penny: 110"). The ladder moved to Gus and survived a reload, in the browser and in the mocked `db`. One point off: the end screen shows my answers but not theirs, so "Penny wins" has no story |
| 7 | Trash talk | 4/5 | Short, kind, and the switch works: with it off, no talk appeared and the AI was never called. A late line is dropped when you move on, so the loop 1 "talk about the previous answer" bug is gone. Without the AI the lines follow the tier, not the answer ("Huh, that wasn't on the list? Weird!"). Whether the AI lines are funny and specific is untested: my mock returned placeholder text |
| 8 | Robust | 7/10 | No console errors offline, with storage blocked, with every request blocked, or with my mocks. With no `window.claude`, or with every capability null or refused, the AI box, the fresh-prompt switch, the party button and the board all hide. With storage blocked the end note no longer claims "Progress saved". Problems: if `window.claude.use` throws instead of rejecting, an uncaught error "nope" lands in the console (the game still plays). There is still no way to quit a game in progress (no button, Escape does nothing). An AI-made category said "It comes first in your next game" and then came first in the game after that too, with answers I had already seen. The party (beta, mocked) has real faults: see fix 1 |
| 9 | Honest and safe | 5/5 | "Popularity is the AI's estimate, not a survey." is on the home page and under every reveal. AI prompts are labelled "FOOD · MADE BY AI" and "FRESH FROM CLAUDE", and the reveal adds "This prompt was written by Claude." No copied branding or art, only answer names. Nothing hurtful in any line I saw. (The false "at least 25" promise is scored under item 4) |

## Fix first

1. **Make the party fair to guests.** Where: the `r.on("rf")` state handler, `judge`, and the host's
   `#b-next` branch. Evidence from two tabs over a relayed room (mocked):
   - The host answered and pressed Next while the guest was typing. The guest's half-typed answer was
     wiped on every prompt, and their end screen listed one prompt out of five (`46-party-guest-end-holes.png`).
   - The guest's judge took 6 s, and the host moved on first. All four verdicts were thrown away
     (`if(G.cur!==cur) return`), so the guest scored 75 instead of 375.
   - Guests see no "waiting for the host" text after answering (`42-party-guest-after-answer.png`). No
     one sees the room's standings at the end, and the end note says "Try the Office ladder".

   Submit whatever the guest has typed when the host advances. Write late judge verdicts into
   `G.res[round]` and the total instead of dropping them. Show who has answered to the host. End with
   the room's standings. Raises item 4 (+1) and item 8 (+2).
2. **Tighten the typo rule and make the home page say what it does.** Where: `typoOK`. Refuse a typo
   match that changes the first letter ("Siberia", "Catwoman", "Painter") or turns one real word into
   another ("Spanner", "Protector", "Pointer"). Add those to the packs' `wrong` lists as well. Then
   either forgive one changed letter from five letters up ("Kenia", "Egipt", "Cerial", "Lybia"), or
   change the line to "Small slips (a missing, extra or swapped letter) are forgiven". Raises item 4 (+2).
3. **Stop unlisted right answers from feeling like a loss offline.** Add the obvious gaps to the packs:
   Lilo and Stitch, Sleeping Beauty, Peter Pan, The Jungle Book, Big Hero 6, Wreck-It Ralph, Minions;
   maracas, castanets, timpani, bugle, gong; toilet, cubicle, mug, water fountain; Goldendoodle,
   Cavapoo; Boggle, Mastermind, Trouble; cinnamon roll, frittata, quiche, avocado on toast. Count a
   numbered sequel ("Toy Story 3", "Frozen 2") as its series. Offline, offer a "We allow it" button that
   scores a labelled Good find when the room agrees. Change "Any right answer scores at least 25" to
   "Any answer on our list scores at least 25". Raises item 4 (+1) and item 2 (+1).
4. **Stop repeats.** Where: `newGame`. Deal prompts from a shuffled bag across the session, so none
   repeats until all ten are used. Remove an AI-made category from `S.custom` once it has been played.
   Consider showing three of the five Gems, so the reveal does not hand out next game's answers.
   Raises item 2 (+1) and item 8 (+1).
5. **Fix `Counted as "undefined"`.** Where: `countedText`, the `how:"wrong"` case. Say
   `"Joker" is not a superhero` (or "Not a right answer"). Check the singular against the wrong list
   too, so "Apples" and "Jokers" are a Miss like "Apple" and "Joker", not "Not on our list". Raises
   item 3 (+1).
6. **Make the end-screen "Not on our list" tag readable.** Where: `.recap .t` and `.strip span` set
   `color: var(--ink)`, which overrides `.t-unlisted`. Give unlisted text `var(--text)` there. Raises
   item 5 (+1).
7. **Announce and settle the judge's verdict.** Call `announce()` after the judge rules. Turn a "no"
   into a red Miss badge. Raises item 5 (+0.5) and item 3 (+0.5).
8. **Do not lock Next for 12 seconds.** Unlock Next after about 4 s of judging and apply a late verdict
   to its own round (the same change as fix 1). Raises item 3 (+1).
9. **Let players quit.** Add a small "Quit" or "Home" link on the play screen, and make Escape ask
   "Leave this game?". Raises item 8 (+1).
10. **Small robustness and polish:** wrap `window.claude.use(n)` in `Promise.resolve().then(...)` so a
    synchronous throw is caught; when the AI refuses a topic say so ("That topic is off limits. Try
    another.") instead of "That did not work. Try a simpler topic"; show the opponent's answer per
    prompt on the end screen; rename the hosting button "Play together". Raises item 8 (+0.5), item 6
    (+1) and item 1 (+1).

## What I could not test

- **The real Claude runtime.** Every AI, saving and party result above comes from my fake
  `window.claude`. I could not confirm that `use("sample")`, `sample.json`, `db.doc().get()/set()`,
  `db.collection().orderBy().limit().get()`, `user.id()`, `user.profiles()` and
  `room.join/emit/on/presence/onPeers/leave` match the real API shapes, or how long the real model takes.
- **Real AI wording.** My mock returned placeholder lines and always said yes or always said no, so I
  could not judge whether trash talk is funny and specific, whether AI-made packs are correct, or
  whether the judge is fair. I could not test whether a player can talk the judge into a Gem by typing
  instructions into the answer box (the answer is pasted into the judge's prompt; 60 characters max).
- **A real multi-device party.** Two tabs in one browser stood in for two phones. I simulated a guest
  clock 20 s slow and 25 s fast: the guest timer started at 50 s and at 5 s
  (`45-party-guest-skew-20.png`, `45-party-guest-skew+25.png`), because deadlines are sent as clock
  times. Real phones are usually closer than that, so I did not score it.
- **A real screen reader.** I checked the live regions in the DOM only.
