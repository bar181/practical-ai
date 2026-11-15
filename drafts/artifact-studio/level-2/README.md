# Level 2: your preferences on file

Level 1, plus one file that holds how you like your pages, and the skill installed if your
assistant can load one.

**Think of it as** being a regular. The kitchen knows your usual, so you only say what is
different today.

## What this level adds to the base

| Addition | Where | What it changes |
| --- | --- | --- |
| A preferences file | [`preferences-template.md`](preferences-template.md), saved as `preferences.md` | Your default recipe, voice and look, your layout habits, your format rules, and the things you never want |
| The skill, installed | [`skills/artifact-studio/`](../../../skills/artifact-studio/) | The assistant loads the full instructions, the cards and the page skeleton by itself, instead of the condensed copy you pasted at level 1 |

Nothing else changes. The instructions from level 1 already tell the assistant to read a
preferences file first when one is there.

## What it depends on

| Addition | Needs |
| --- | --- |
| Preferences file | An assistant that keeps files between chats, such as a Project. Without one, attach the file to each request |
| Installed skill | An assistant or agent that loads skills. Without one, stay with the pasted instructions from level 1. The pages are the same; you lose only the longer reference cards |

Either addition works without the other.

## Set up once

1. Copy [`preferences-template.md`](preferences-template.md) and name the copy `preferences.md`.
2. Fill in the parts you care about. Leave the rest blank. A blank line means "the assistant
   chooses".
3. For colours and fonts, fill in [`base/templates/design-spec.md`](../base/templates/design-spec.md)
   and paste its table under "Brand" in your preferences file.
4. Put `preferences.md` where your assistant keeps files for you: the files of the same Project
   that holds the level 1 instructions.
5. If your assistant loads skills, install the skill.

   | Assistant | How |
   | --- | --- |
   | Claude, with skills turned on | Add the folder `skills/artifact-studio/` as a skill. It loads when you ask for a page or say "use the artifact-studio skill" |
   | An agent that reads skill folders, such as Claude Code or Codex | Copy the folder into the agent's skills directory |

   The skill uses the open Agent Skills format: a `SKILL.md` with a name and a description, plus
   reference files it reads when needed.

## Make a page

A short ask is now enough, because the file answers the rest.

```
Make a proposal from the attached estimate and site notes.
```

With the skill installed you can hand over more and say less:

```
Use the artifact-studio skill.
Content: the attached estimate, site notes and three photos.
Invent no facts, mark every gap, and run the pre-ship check before you show me.
```

Anything you say in the request beats the file. "Use the keynote voice for this one" changes
that page and leaves your file alone.

## Check it worked

The assistant returns a delivery note with each page. It must list which of your preferences it
applied. If the note does not mention them, it did not read the file: attach the file to the
request and ask again.

## What stays manual

| Step | Why |
| --- | --- |
| Answering the gaps it lists | Only you know the missing facts |
| Checking numbers, names and quotes | The assistant reports what to check. You check it |
| Deciding to publish, and where | A person approves anything that goes out |
| Updating the file when your taste changes | Change it when you catch yourself asking for the same fix twice |

## Status

The preferences file is new and has not been used on a real page yet. The skill has not yet been
run end to end by a second agent.
