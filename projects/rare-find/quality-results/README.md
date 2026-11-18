# Quality results: Rare Find

**Built and machine-tested. As of 18 November 2026, users are testing it; their results are not in yet.**

## How it was tested

- **The automated playtest**, [`../_build/playtest.py`](../_build/playtest.py). It plays the built
  page in Chromium at 390 px (phone) and 1280 px, keyboard only, with reduced motion, with no Claude,
  and with a mock of Claude's answer check (`sample`). Last run, 18 November 2026, version 4.4: **123 of 123 checks
  passed**. They cover how an answer lands (on screen within 100 ms, ordinary effects 150 to 250
  ms, the Gem reveal inside 600 ms, Next usable during effects, a late verdict that changes only its
  own round), 60 spelling cases, the per-category points, hidden Gems, the daily calendar
  over 240 days, practice limits, Check again once per answer (never an approval without the AI's yes), Good finds
  scored by rarity, 7 prompts a day, the one result card, the
  hosts talking while the AI checks, an unreachable AI with Try again, the
  hosts, settings, the scorecard, challenge links, Back to start, the timer and phone width.
- **The review skill**, [`../level-2-files/game-review/SKILL.md`](../level-2-files/game-review/SKILL.md).
  At the end of each loop a fresh reviewer agent that had not seen the game played it and scored it
  out of 100.

## Scores by loop

| Loop | Version | Score | Verdict | Review |
| --- | --- | --- | --- | --- |
| 0 | The plan only | 37 | Not ready: nothing to play | [loop-0-baseline.md](loop-0-baseline.md) |
| 1 | 1, office ladder | 68 | Not ready, but close | [loop-1-review.md](loop-1-review.md) |
| 2 | 1 | 80 | Ready for friendly testers | [loop-2-review.md](loop-2-review.md) |
| 3 | 1 | 84 | Ready for friendly testers | [loop-3-review.md](loop-3-review.md) |
| 4 | Interim: rank points, Claude check | 80 | Ready for friendly testers | [loop-4-review.md](loop-4-review.md) |
| 5 | 2, daily game and scorecard | 71 | Ready for friendly testers, only just | [loop-5-review.md](loop-5-review.md) |
| 6 | 4, answer moments, blind against version 3 | 91 (version 3: 84) | Ready to share. Would replay the new one; remembered the old confetti Gem | [loop-6-review.md](loop-6-review.md) |
| 7 | 4, with the bigger Gem, blind, labels swapped | 86 (version 3: 82) | Ready to share, just. Would replay the new one; remembered its Gem | [loop-7-review.md](loop-7-review.md) |

**After loop 5**, at the owner's request: challenge codes, a prompts-per-game setting (5, 10 or party
mode) and an edit-access note. Then all five top problems from the loop 5 review were fixed: totals
that could disagree, a "Check again" that skipped Claude, real words that scored, codes trusted
blindly, and "saved" messages that were not true. The automated playtest checks every fix (80 of
80). No reviewer has re-scored the fixed build yet.

**Version 3, the simple version** (17 November 2026, after loop 5): a JSON bank of 125 prompts and a
JSON calendar, up to 100 practice prompts a day, one share link to the public web copy, and the
shared scoreboard, friends groups and live rooms removed at the owner's request. Checked by the
playtest (82 of 82); not re-scored by a reviewer. The 100 new prompts were drafted by Claude and
passed `check_packs.py`. Claude spot-checked a sample of them; no person has read every list yet.

**Version 4, answer moments** (18 November 2026): each kind of answer lands its own way, the Gem
has a signature reveal in place of confetti, Next works during effects and Claude's checks, and the
progress dots show each round's outcome, carried into the scorecard and a spoiler-free challenge
message. Two blind reviews by fresh agents, each playing this build and version 3 with the same
prompts, scored it higher both times (loops 6 and 7). Two small fixes after loop 7 are checked by
the playtest, not re-scored. Every test used a mock of Claude: **nobody has played version 4 in the
real Claude artifact runtime yet.**

**Version 4.1, no automatic approval, and play in any chatbot** (18 November 2026, the owner's
request): "We allow it" is removed. An answer not on the list scores only when the AI says it is
right; a second opinion is allowed once, and it can still say no. The hosts comment while the AI
checks. For ChatGPT and other chatbots, [`../base/SKILL.md`](../base/SKILL.md) has the chatbot
host the game in the chat from a daily answer file. In two test games, a session playing the
chatbot scored every answer correctly. It refused an answer written as an instruction, refused to
approve on demand, kept its verdict on a second opinion, and produced challenge links that the game
accepts. Its friction notes led to four rule fixes: the next prompt comes straight after each
result, a skip scores 0, the top ten fits on two lines, and the link is given once. One line added
after game 2 (when unsure between Gem and Good find, choose Good find) is not re-tested. The playtest
still passes 110 of 110.

**Later the same day: Check again, always reachable**, from tester feedback that the button was
missing. It is named **Check again**, it is offered after a Good find too (it can only go up), and a
"no" that lands after the player moved on can be checked again from the end screen, which updates
the saved score and the challenge link.

**Version 4.2, celebrations** (18 November 2026, the owner's feedback that celebrations were not
visible): every right answer now gets a celebration that grows with its points (five levels, from a
few sparks to the Gem shower), plus one for a strong final score; the top ten is in two columns;
the hidden-Gems note moved to settings. New playtest checks confirm the levels rise with the
points, the words show ("Deep cut!", "Good find!"), the Gem's celebration ends within 1.1 s, Next
is never blocked, and reduced motion shows none of it. 115 of 115 pass, with Claude mocked. Not
re-reviewed by a fresh reviewer.

**Version 4.3, a tidier result and fairer checks** (18 November 2026, the owner's feedback with a
screenshot): the result is one header (your answer and its points), the host's line, Check again
and Next; the "Sure it is right?" note and the extra answer row are gone; the timer ring hides
after an answer (it read as an eyeball); less bottom padding; the full width for the top ten on
desktop. The first AI check is also called Check again. An answer the AI accepts that is on no
list scores 60 (common) or 80 (uncommon), or 100 as a Gem, never a flat 80, and a second look can
only raise it. A place's own name counts without its title: "Helens" is Mount St. Helens (#2, 28
points) with no check needed. 118 of 118 checks pass, with Claude mocked.

**Check again, fixed for real Claude apps** (18 November 2026): the owner pressed Check again in the
real artifact and the AI check did not run. The likely cause: the check used `sample.json`, which
Claude's own guide says some Claude apps do not have, while the host lines, which did work, use the
plain text call. The check now uses the plain text call and reads the JSON from the reply itself;
the button stays on screen as "Checking..." while it runs; a failure names its reason. The mock now
has no `sample.json` at all, like those apps. 119 of 119 checks pass. **Confirmed by the owner in
the real Claude app** (private preview, 18 November 2026): Check again ran and accepted a Good find.

**Version 4.4, Good finds by rarity, one result card, seven prompts** (18 November 2026, the
owner's feedback). A Good find was a flat 80. Now every one of the 4,607 Good finds on the lists
carries a rarity from 1 to 9 (an AI's estimate, rated by five agents in batches and checked: every
answer present, whole numbers only), and scores from 10 above the prompt's 10th place up to 90. An
answer the AI checks gets a rarity from 1 to 10 on the same scale; 10 is a Gem. Check again is a
small button beside the 0 and runs once. The result is one card (tier, points, what counted, Check
again, Next question) that celebrates in proportion to the points; the AI's reasons no longer
repeat in it, so the host's bubble is the only comment. The daily game is 7 prompts, today
included. Then, at the owner's word that celebrations are the game play, they were made far bigger,
varied (eight styles drawn at random by level) and longer: 1.5 s at 25 points, 2.5 s at 80, 3 s over
80 and for a Gem, measured in the playtest. The estimated chart now mixes four kinds of player,
fitted to the owner's estimate: an average of about 275 of 700, about 1% of games at 600 or more.
123 of 123 checks pass, with Claude mocked. **Not yet
tried by a person.**

## Who has and has not tried it

| Who or what | Tried? |
| --- | --- |
| The author, with Claude, building it | Yes |
| The automated playtest, with a mock of Claude | Yes |
| Fresh reviewer agents, with a mock of Claude | Yes, eight loops, the last two blind against the version before |
| Version 4 in the real Claude artifact runtime | **Yes, by the owner**, in a private preview, up to the Check again fix. Version 4.4 **not yet** |
| The chat version (`base/SKILL.md`), with a session playing the chatbot | Yes, two games on 18 November 2026: every score and both challenge links were right. [Game 1](2026-11-18-chat-play-1/transcript.md) · [game 2](2026-11-18-chat-play-2/transcript.md) |
| The chat version in ChatGPT itself | **No.** The test sessions could not open web links, so they were given the day's file directly |
| Users, in the Claude artifact or the web copy | **In progress** since 18 November 2026. No results yet |
| A screen reader, ChatGPT | **No** |

The answer lists are Claude's estimates, not a survey. The research behind the rules is in
[`../_build/PLAN.md`](../_build/PLAN.md).
