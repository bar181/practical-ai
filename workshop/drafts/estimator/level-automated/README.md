# Level automated: estimator

The working level, run by a skill, with an approval step before anything leaves.

**Status: outline.** The skill is written. It has not yet been run by a second agent.

## What this level adds

The `quote-drafter` skill, reading the price list and rules from where you keep them. A finished estimate can be passed to the `artifact-studio` skill to become a proposal page. Sending still waits for you.

## What it needs

- The `quote-drafter` skill installed
- The price list and rules in a file or sheet the assistant can read
- For a proposal page: the `artifact-studio` skill
- An approval step before anything reaches a customer

## Install the skill

The skill is the folder [`workshop/skills/quote-drafter/`](../../../skills/quote-drafter/). In an assistant that supports
skills, add the folder. In any other assistant, paste its `SKILL.md` into the instructions of a
Project.

## What stays manual

| Step | Why |
| --- | --- |
| Changing a price or a rule | Prices are the business. The skill never edits them |
| Resolving a conflict between rules | The skill stops and says which rules conflict |
| Sending the quote | A person approves anything that goes out |
