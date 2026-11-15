# Level automated: short video guide

The working level, run by a skill, with an approval step before anything leaves.

**Status: outline.** The skill is written. It has not yet been run by a second agent.

## What this level adds

The `script-and-beat-sheet` skill writes the beat sheet and script and checks the timing. An agent can then run a route end to end and stop at your approval. The rendering services are outside tools: they are reviewed in the plan and none is selected here.

## What it needs

- The `script-and-beat-sheet` skill installed
- An account with whichever rendering service you choose, and its costs understood
- Your own image and voice only, with your say-so recorded
- A place where finished drafts wait for approval

## Install the skill

The skill is the folder [`skills/script-and-beat-sheet/`](../../../skills/script-and-beat-sheet/). In an assistant that supports
skills, add the folder. In any other assistant, paste its `SKILL.md` into the instructions of a
Project.

## What stays manual

| Step | Why |
| --- | --- |
| Approving every finished video | Likeness and voice are yours. Nothing with your face goes out unseen |
| Choosing the service | A build-or-license decision with real costs |
| Posting | A person approves anything that goes out |
