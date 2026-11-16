# Level automated: publishing a website

The working level, run by a skill, with an approval step before anything leaves.

**Status: outline.** The skill is written. It has not yet been run by a second agent.

## What this level adds

The `publish-check` skill runs the check and recommends a route. The page lives in a repository connected to a host, so an approved change publishes itself and a proposed change gets a preview address.

## What it needs

- The `publish-check` skill installed
- A repository, with the main branch protected so a person must approve changes
- A host connected to that repository
- A decision on who may approve

## Install the skill

The skill is the folder [`workshop/skills/publish-check/`](../../../skills/publish-check/). In an assistant that supports
skills, add the folder. In any other assistant, paste its `SKILL.md` into the instructions of a
Project.

## What stays manual

| Step | Why |
| --- | --- |
| Approving a change | Approval is the publish button |
| Changing who can see the site | It is the decision that cannot be undone quietly |
| Connecting a domain and paying for anything | Accounts and money stay with a person |
