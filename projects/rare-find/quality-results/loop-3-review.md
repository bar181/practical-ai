# Loop 3: playtest review, 17 November 2026

Scored with the [game-review skill](../level-2-files/game-review/SKILL.md) by a reviewer agent (Claude)
that had not played the game before. I played `base/game.html` in Chromium through Playwright, served
over http, at 1280 px and 390 px. I also played keyboard only, with reduced motion on, with no
`window.claude`, with every capability null, with `window.claude.use` throwing, and with it never
answering. **Every Claude feature (`sample`, `db`, `user`, `room`) ran against a fake `window.claude`
that I injected. It had delays: judge 1.5 to 8 s (and one that hangs), trash talk 1.5 to 1.8 s, new
prompt 5 to 6 s, saving 0.3 s. For the party, two pages relayed room messages to each other through a
`BroadcastChannel` with a 150 to 200 ms delay. None of it ran against the real Claude artifact
runtime.** My screenshots are in `/tmp/rf-review3/` and my scripts in `/tmp/rfr3s/`. I also read the
automated run in `/tmp/rf3/` (41 of 41 checks passed).

**Score: 84/100. Ready for friendly testers. One short loop from ready to share.** Most of the loop 2
fixes landed and work: the party now keeps a guest's typed answer and late judge verdicts, the end
screen shows the opponent's answers, the "Not on our list" tag is readable, Escape and a ✕ button ask
before leaving, and "We allow it" covers unlisted answers offline. What holds it back: the typo rule
has a loophole that lets real, different words score; a late judge verdict changes the total after
the end screen has shown a different one; quitting while an opponent thinks throws an error; and
offline trash talk repeats word for word.

| # | Item | Score | Evidence |
| --- | --- | --- | --- |
| 1 | First ten seconds | 15/15 | Cold open at 1280 and 390: "Rare Find", then "Name a right answer nobody else thinks of. **The rarer it is, the more it scores.**" and a big yellow "Play solo · 5 prompts · 30 seconds each" above the fold (`01-home-1280-fold.png`, `12-home-390-fold.png`). I knew what it was and what to press from two lines. The subtitle follows the timer ("5 prompts · 15 seconds each"), and with Claude present the third button now reads "Play together" |
| 2 | The core loop is fun | 12/15 | The ring counts down, turns red and pulses; the reveal lights my row, a Gem gets a full-width "GEM!" banner and confetti, and only three of five Gems show ("+ 2 more Gems still hidden. Find them next time.", `05-r2-gem-typo-1280.png`). There is still no bet. There are 10 built-in prompts, and games alternate between two fixed sets of five: game 1 and game 3 had the same five prompts, as did game 2 and game 4. With the full top 10 and three Gems on show, game 3 can be played from memory. Common right answers still score 0 offline unless the room presses "We allow it": "Scissors", "Clock", "Ruler", "Boss" (office); "A Bug's Life", "Pocahontas", "Finding Dory" (films); "Diamond sword", "Golden Gun" (weapons); "Blade", "Ghost Rider" (heroes); "Lyre", "Snare drum" (instruments); "Cheerios", "Scones", "Poached egg" (breakfast). With Claude, the fifth prompt was replaced by a fresh AI pack, which helps |
| 3 | Feedback and feel | 13/15 | The result appeared 14 to 31 ms after Enter. Points count up, tiers have distinct colours, and a Gem gets a flash, a banner and confetti. A judged answer locks Next for 2.3 s, and never more than 4.0 s even when the judge hangs (the loop 2 12 s lock is gone). A "no" now turns into a red "Miss" with "The judge says no." Problems: (a) a late verdict on the last prompt arrives after the end screen: it shows **100** and "Latecomer · Not on our list 0" while a toast says "The judge allowed "Latecomer" on prompt 5: +75" (`25-end-after-late-judge-1280.png`); (b) the AI trash talk (1.5 to 1.8 s in my mock) arrives after Next unlocks (0.6 s), so a player who presses Enter at once never sees it; (c) the Leave dialog does not pause the timer: with it open, the prompt ran out and scored "Miss" behind it |
| 4 | Fair scoring | 11/15 | Every total I checked matched the table: solo 210 (35+100+0+0+75), ladder 225 vs Penny 145, 500 vs 185, and the party host 250 and guest 400. The loop 2 false matches are fixed: "Siberia", "Catwoman", "Spanner", "Painter" and "Apples" are now a Miss. But 7-letter-plus words still accept real, different words, because a deleted letter plus an inserted letter costs 2, which is the 2-slip allowance, so any one changed letter passes. On screen: "Scramble" is `Counted as "Scrabble" · #3` (35), "Chatter" is `Counted as "Charger"` (Good find 75), "Doorman" is `Counted as "Doberman"` (75), "Boatman" is `Counted as "Batman" · #2` (35), and "Therein" is `Counted as "Theremin"` (**Gem 100**, `40-false-match-therein.png`). Against the hunspell English word list, 333 real words score on some pack. "Toy Story 9" counts as its series. The late verdict above leaves the shown total (100) and the saved best (100) different from the game's total (175). Offline, "We allow it" turns any text into a Good find 75 ("Snorkel" for a dog breed, `09-r5-allowed-1280.png`), in the ladder too, and the end recap shows it as a plain "Good find 75". When the judge cannot be reached, the answer stays "Not on our list 0" with no "We allow it" fallback (`24-judge-unreachable-1280.png`) |
| 5 | Usable by everyone | 9/10 | I played a whole ladder game keyboard only at 390 px with reduced motion: Tab, Tab, Enter starts it, focus goes to the answer box, then to Next, then to "Play again". No confetti, instant counts, no sideways scroll on normal answers, and the sticky Next sits at the bottom (`16-result-390-good.png`). Tier tags measure 6.2:1 to 11.5:1, and "Not on our list" is now light text with a dashed border. The judge's verdict is announced ("Good find, 75 points. Counted as Spam.", "Miss, 0 points."). Fails: a 60-letter answer with no spaces pushes the page to **608 px** wide on the result and **782 px** on the end screen at 390 (`14-result-390-longanswer.png`, `17-ladder-end-390.png`). "The judge could not be reached" is not announced. I had no real screen reader |
| 6 | Opponents feel alive | 9/10 | Four co-workers with their own think times (Penny 0.6 s, Gus 0.9 s, Marge 1.3 s, the Archivist 1.8 s), skill (Penny gave Crowd picks; the Archivist gave "Portal gun" and "Spirit: Stallion of the Cimarron", both Good finds) and voice. They think with dots, answer with "+50", and sometimes miss ("Poker", "Apples"), which feels human. The end screen now shows their answer per prompt ("🙋 Carrot 25"). The ladder moved to Gus and survived a reload, in the browser and in the mocked `db`, and the board showed "Player-654 500 pts". One point off: each opponent has one offline line for an unlisted answer, so five unlisted answers in a row gave the same line five times (see item 7) |
| 7 | Trash talk | 3/5 | Short and kind, and the switch works: with it off, no talk appeared and the AI was never asked (calls: `json`, `judge` only). With the mocked AI the line named the answer ("Mocked line about "Booster Gold"."), but the wording was mine, so funny and specific is untested. Offline the lines follow the tier, not the answer, and repeat word for word: Gus said "Not in the ledger. I'll flag it for audit." on all five prompts, Marge "Not on the list. I'd want that in writing." five times, the Archivist "Unfiled. Perhaps it belongs to a smaller archive." five times. And the AI line often lands after the player has moved on (item 3) |
| 8 | Robust | 7/10 | No console errors offline, with every capability null, with `use` throwing ("nope" is now caught), with `use` never answering (the game plays and offers "We allow it"), or through the whole mocked session. AI, party, fresh-prompt and board controls all hide when absent. Failures: **"pageerror: Cannot read properties of null (reading 'cur')"** when I pressed ✕ then Leave while Penny was still thinking; the Archivist thinks for 1.8 s, so a real player can hit this. In the party (beta, mocked), the guest who finishes first gets frozen standings: "You top the room! … 2. Player-677 150" stayed after the host finished on 250, so a host who overtook on the last prompt would be shown as losing. "Play again" after a party starts a solo game and leaves the room. The late verdict divergence (item 4) |
| 9 | Honest and safe | 5/5 | "Popularity is the AI's estimate, not a survey." is on the home page and under every reveal. AI packs are labelled "FOOD · MADE BY AI", and the fresh prompt "FRESH FROM CLAUDE". A note explains "Tomato counts here, even though a botanist calls it a fruit." No copied branding or character art, only answer names. Nothing hurtful in any line I saw |

## Fix first

1. **Close the typo loophole.** Where: `typoOK` and `osa`. In 7-letter-plus words, price a deleted
   letter next to an inserted letter as one changed letter, using the same `cost()` (vowel for vowel,
   or a neighbouring key). Then refuse a typo match when the typed word is itself a common English word
   ("Scramble", "Chatter", "Doorman", "Boatman", "Therein", "Commuter", "Strategy", "Bullfrog"). The
   333 words my hunt found are in `/tmp/rfr3s/dicthunt.json`; most can go straight into the packs'
   `wrong` lists. Raises item 4 (+2).
2. **Settle the judge before the end screen.** Where: `endGame` and `judge`. If a verdict is pending,
   show "Waiting for the judge..." on the end screen for up to its timeout, then draw the total, the
   recap and the saved best. Or redraw `#final`, the strip, the recap and `saveProgress()` when a late
   verdict lands. Raises item 4 (+1) and item 3 (+1).
3. **Guard against a quit game.** Where: the opponent `setTimeout`, `Promise.all(settle).then` and
   `trashTalk` in `showResult`. Use `if(!G||G.cur!==cur)` in all three. Raises item 8 (+1).
4. **Make party standings live.** Where: the `score` handler in `enterRoom` and `endGame`. Redraw the
   end banner and "Room standings" when a score arrives, and mark players still playing ("Player-677:
   still on prompt 5"). Let "Play again" after a party return to the room. Raises item 8 (+1).
5. **Write more offline lines, and let players see the AI line.** Where: `OPPS[].lines` and `LINES`.
   Give every opponent at least three lines per tier, unlisted included, and never repeat the last
   line. Hold Next for up to 1.5 s while an AI line is on its way, or keep a late line on screen when
   the next prompt opens. Raises item 7 (+1) and item 6 (+1).
6. **Offer "We allow it" when the judge fails.** Where: the `catch` in `judge`. Show `#judge-row` with
   "The judge could not be reached. Sure it is right?" and announce it. Raises item 4 (+0.5) and item 5
   (+0.5).
7. **Keep the honour button honest.** Where: `#b-allow` and `endGame`. Label allowed answers on the
   end recap ("Snorkel · allowed 75"). In the ladder, score an allowed answer as Solid 50 or let the
   opponent object, so typing anything and pressing "We allow it" cannot beat the office. Raises item 4
   (+0.5).
8. **Fill the obvious pack gaps.** Office: scissors, clock, ruler, marker, boss, coworker, garbage can,
   conference room, vending machine, fire extinguisher, elevator, window. Films: A Bug's Life,
   Pocahontas, Fantasia, Finding Dory, Monsters University, The Polar Express, The Super Mario Bros.
   Movie, Shrek the Third. Weapons: diamond sword, Golden Gun, trident, neuralyzer, Valyrian steel.
   Heroes: Blade, Ghost Rider, the Punisher, Spider-Woman, Gamora. Instruments: lyre, snare drum, tin
   whistle, pipe organ, congas, uke. Breakfast: Cheerios, corn flakes, scones, ham, poached egg, boiled
   egg, peameal bacon, cream of wheat. Dogs: Bichon, Rottie, Newfie, Chiwawa. Count a sequel only up
   to a real number ("Toy Story 9" should not score). Raises item 2 (+1) and item 4 (+0.5).
9. **Wrap long answers.** Where: `.reveal li span`, `.recap .a`, `.counted`. Add
   `overflow-wrap:anywhere`. Raises item 5 (+0.5).
10. **Small polish:** pause the timer while the Leave dialog is open; reshuffle the whole bag each
    time it empties so games do not alternate between the same two sets of five; add a few more
    built-in prompts. Raises item 3 (+0.5) and item 2 (+1).

## What I could not test

- **The real Claude runtime.** Every AI, saving and party result above comes from my fake
  `window.claude`. I could not confirm that `use("sample")`, `sample.json`, `db.doc().get()/set()`,
  `db.collection().orderBy().limit().get()`, `user.id()`, `user.profiles()` and
  `room.join/emit/on/presence/onPeers/leave` match the real API shapes, or how long the real model
  takes. The trash talk timing problem in item 3 depends on that.
- **Real AI wording.** My mock returned my own lines and a fixed pizza pack, so I could not judge
  whether trash talk is funny, whether AI packs are correct, or whether the judge is fair. I could not
  test whether a player can talk the judge into a Gem through the answer box.
- **A real multi-device party.** Two pages in one browser stood in for two phones, with one shared
  clock. Deadlines are still sent as clock times, so phones with clocks far apart would see different
  timers; I did not re-test that this loop.
- **A real screen reader.** I checked the live regions in the DOM only.
