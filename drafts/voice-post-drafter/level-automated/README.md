# Level automated: voice post drafter

The working level, run by a skill, with an approval step before anything leaves.

**Status: outline.** The skill is written. It has not yet been run by a second agent.

## What this level adds

The `voice-drafter` skill, plus a scheduled topic scout that finds subjects worth a post and queues a draft for each. Nothing is posted. You open the queue, pick, edit and publish.

## What it needs

- The `voice-drafter` skill installed
- Your voice file in a place the assistant can read
- A scheduled task, if you want the topic scout
- Sources for the scout to read: your own notes, a few sites you trust

## Install the skill

The skill is the folder [`skills/voice-drafter/`](../../../skills/voice-drafter/). In an assistant that supports
skills, add the folder. In any other assistant, paste its `SKILL.md` into the instructions of a
Project.

## What stays manual

| Step | Why |
| --- | --- |
| Choosing which draft to use | Only you know what you want to be known for |
| Editing | The draft is a start. Your edit is what makes it yours |
| Publishing | A person approves anything that goes out |
