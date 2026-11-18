# Rare Find: instructions for agents

You are here because a person wants to play Rare Find, or to change it. People start at the
[README](README.md).

## If the person wants to play

| Where they are | Do this |
| --- | --- |
| Claude, with a shared Rare Find artifact link | Give them the link. The game runs in the artifact and uses their own Claude session for the answer check and the hosts' fresh lines |
| Claude, no link | Give them https://claude.ai/artifact/HyfbDjPjofvRttRYKgMCis, or point them to [`base/game.html`](base/game.html) to open in a browser |
| Any browser, no account | https://bar181.github.io/practical-ai/rare-find/ (published by `.github/workflows/rare-find-pages.yml` once Pages is on). The Claude features hide; challenges work |
| ChatGPT or another chatbot | The same file, opened in a browser. Or build a simpler version with [`base/try-it-prompt.txt`](base/try-it-prompt.txt), which is a draft and not yet tested |

## If the person wants to change it

Edit `_build/game.src.html` and `_build/packs.json`, never `base/game.html`. Each pack needs 10
ranked answers, 5 Gems, 20 or more other right answers, a few tempting wrong ones and `top`, its
10th-place points (40 to 60: higher when there are few possible answers). Then:

1. `python3 _build/build.py && python3 _build/falsematch.py && python3 _build/build.py` rebuilds the
   game and `base/examples/sample-pack.md`, and refreshes the list of real words that must not count
   as spelling slips. Run all three after any change to the packs.
2. `python3 _build/playtest.py /tmp/rf` must pass every check.
3. Review with [`level-2-files/game-review/SKILL.md`](level-2-files/game-review/SKILL.md) in a fresh session.

The design is in [`_build/NORTH-STAR.md`](_build/NORTH-STAR.md); the research is in
[`_build/PLAN.md`](_build/PLAN.md).

## Rules that never bend

1. Say that popularity is an AI estimate, not survey data.
2. Our own names, tiers, prompts and answer lists. Copy nothing from another game or answer site.
3. No quotes or lyrics, no pictures of characters or logos, and nothing on politics or religion.
4. Trash talk is about the answers only, never about the player as a person.
5. Scoring of listed answers never depends on the AI. Claude rules only on an answer that scored 0,
   and only when the player asks ("Check with Claude"). Its prompt treats the answer as data, it
   may fix spelling but not swap the answer, and text that reads like instructions is never sent.
6. Keep the Gems hidden in the game. Only `base/examples/sample-pack.md` lists them.
