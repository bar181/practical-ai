# Rare Find: for agents

People start at the [README](README.md). The design is in [`_build/NORTH-STAR.md`](_build/NORTH-STAR.md).

## To play

- In Claude: https://claude.ai/artifact/HyfbDjPjofvRttRYKgMCis. Answer checks run on the player's own plan.
- In any browser, no account: https://bar181.github.io/practical-ai/rare-find/. No AI; challenge links work.
- Offline: open [`base/game.html`](base/game.html).

## To change it

Edit `_build/`, never `base/game.html` (generated).

| Change | Then run, from `_build/` |
| --- | --- |
| The game (`game.src.html`) | `python3 build.py` |
| Add prompts | Append to the end of `packs.json` (challenge codes use positions). `python3 check_packs.py packs.json`, `python3 make_calendar.py`, then `python3 build.py && python3 falsematch.py && python3 build.py` |
| The game's look | `python3 make_store_images.py` (README screens) and `python3 explainer/build_explainer.py` |

Each pack: 10 ranked answers, 5 Gems, 20 or more other right answers, a few tempting wrong ones,
and `top`, the 10th-place points (40 to 60, higher when few answers exist).

Before you finish: `python3 playtest.py /tmp/rf` passes every check, and the README status and
check count are still true. For a bigger change, review with
[`level-2-files/game-review/SKILL.md`](level-2-files/game-review/SKILL.md) in a fresh session.

## Rules

1. Popularity is an AI estimate, not a survey. Say so.
2. Our own names, prompts and answer lists. Copy nothing from another game or answer site.
3. No quotes, lyrics, characters, logos, politics or religion.
4. Hosts tease the answer, never the player.
5. Listed answers never depend on the AI. Claude rules only on a 0, only when asked, may fix
   spelling but not swap the answer, and never sees text that reads like an instruction.
6. Gems stay hidden in the game. Only `base/examples/sample-pack.md` lists them.
7. GitHub runs no AI and no database. Keep it free to host.
