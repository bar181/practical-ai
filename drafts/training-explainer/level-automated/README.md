# Level automated: training explainer with avatar

The working level, run by a skill, with an approval step before anything leaves.

**Status: outline.** The skill is written. It has not yet been run by a second agent.

## What this level adds

The `script-and-beat-sheet` skill produces the plan. An agent can then produce the whole piece with your avatar and stop at your approval. Avatar and voice services are outside tools: reviewed in the plan, none selected here.

## What it needs

- The `script-and-beat-sheet` skill installed
- An avatar and a voice of yourself, set up with your own material
- An account with the service you choose, and its costs understood
- A place where finished drafts wait for approval

## Install the skill

The skill is the folder [`skills/script-and-beat-sheet/`](../../../skills/script-and-beat-sheet/). In an assistant that supports
skills, add the folder. In any other assistant, paste its `SKILL.md` into the instructions of a
Project.

## What stays manual

| Step | Why |
| --- | --- |
| Approving every finished video | It carries your face and voice |
| Checking the teaching | Only someone who knows the subject can tell if it is right |
| Publishing | A person approves anything that goes out |
