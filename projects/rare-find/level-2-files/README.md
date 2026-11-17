# Level 2 files

| Folder | What it is |
| --- | --- |
| [`game-review/`](game-review/) | The review skill: plays a small browser game and scores it on a 100-point rubric for fun, usability and fairness. It is the builder's mini harness: every build loop of Rare Find ends with a fresh session running it |

The game's own Level 2 (scores saved to your Claude account, the Claude answer check, fresh lines
from the hosts) and Level 3 (the shared scoreboard, friends groups and live play) are inside
[`../base/game.html`](../base/game.html). They turn on by themselves when the game runs as a Claude
artifact with its capabilities declared.
