# Level 2 files

| Folder | What it is |
| --- | --- |
| [`game-review/`](game-review/) | The review skill: plays a small browser game and scores it on a 100-point rubric for fun, usability and fairness. It is the builder's mini harness: every build loop of Rare Find ends with a fresh session running it |

The game's own Level 2 (Claude checks answers and the hosts write fresh lines, on the player's own
Claude plan) and Level 3 (the public web copy, published by GitHub Actions, and challenge links)
are inside [`../base/game.html`](../base/game.html) and `.github/workflows/rare-find-pages.yml`.
