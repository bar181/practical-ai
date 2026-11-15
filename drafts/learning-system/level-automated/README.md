# Level automated: learning system

The working level, run by a skill, with an approval step before anything leaves.

**Status: outline.** The skill is written. It has not yet been run by a second agent.

## What this level adds

The `learning-log` skill, and a database in place of the sheet so entries are found by meaning and not only by matching words. Entries can be drafted from working sessions as they end. A person still confirms.

## What it needs

- The `learning-log` skill installed
- A hosted database with search by meaning. Review the options and their prices first: none is selected here
- A way for the assistant to read the log, and to add Draft rows only
- A named person who confirms

## Install the skill

The skill is the folder [`skills/learning-log/`](../../../skills/learning-log/). In an assistant that supports
skills, add the folder. In any other assistant, paste its `SKILL.md` into the instructions of a
Project.

## What stays manual

| Step | Why |
| --- | --- |
| Confirming an entry | Only a person can say an answer is the recommended one |
| Retiring an entry | It changes what everyone is told |
| Deciding what must never be stored | Secrets and private details stay out |
