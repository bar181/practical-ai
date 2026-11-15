# Level automated (expert): the skill does the job

The working level, run by a skill. You hand over any content and media. The skill chooses or
follows the recipe, voice and look, builds the page, checks it, and tells you what it assumed.

**Think of it as** a studio assistant who knows the house rules by heart, and still shows you the
proof before anything goes out.

## What you get

- The page, as one HTML file.
- A delivery note: what was chosen, what was assumed, what is missing, what to check.

## Install the skill

The skill is the folder [`skills/artifact-studio/`](../../../skills/artifact-studio/).

| Assistant | How |
| --- | --- |
| Claude, with skills turned on | Add the folder as a skill. It is then loaded when you ask for a page or say "use the artifact-studio skill" |
| An agent that reads skill folders, such as Claude Code or Codex | Copy the folder into the agent's skills directory |
| Any other assistant | Create a Project and paste [`SKILL-single-file.md`](../../../skills/artifact-studio/SKILL-single-file.md) into its instructions. It is the whole skill condensed into one file |

The skill uses the open Agent Skills format: a `SKILL.md` with a name and a description, plus
reference files it reads when needed.

## Run it

```
Use the artifact-studio skill.
Recipe: proposal. Voice: practical instructor. Look: my brand spec (attached).
Content: the attached estimate, site notes and three photos.
Invent no facts, mark every gap, and run the pre-ship check before you show me.
```

Leave out the recipe, voice or look and the skill chooses, then says what it chose.

## What stays manual

| Step | Why |
| --- | --- |
| Answering the gaps it lists | Only you know the missing facts |
| Checking numbers, names and quotes | The skill reports what to check. You check it |
| Deciding to publish, and where | A person approves anything that goes out |

## Going further

These are outlines. None is built here yet.

| Addition | What it involves | Belongs to |
| --- | --- | --- |
| Hosting the page | A shared artifact link first, then a hosting platform | Publishing a website |
| A schedule | The skill runs on new content each week, and waits for approval | Daily builder, weekly brief |
| Libraries for richer motion or charts | Named in `build-rules.md`. Each adds a network dependency | This tool, when a page needs it |
| Video, audio and avatar add-ons | Outside services. Reviewed in their own plans, not selected here | Short video guide, training explainer |

## Known limits

- The skill has not yet been run end to end by a second agent.
- Video handling is written down and has no worked example.
