# Level 2, Advanced: it knows your brand

[Level 1](../README.md#try-it-in-five-minutes), plus one file that holds how you like your work, and the skill installed if your
assistant can load one. After that a short ask comes back in your style.

**Think of it as** being a regular. The kitchen knows your usual, so you only say what is
different today.

## What is in this folder

| File | What it is | What it changes |
| --- | --- | --- |
| [`preferences.md`](preferences.md) | A fill-in template | Your default template, voice and look, your brand colours, your layout habits, and the things you never want |
| [`artifact-studio/`](artifact-studio/) | The skill, with its reference cards and starter files | The assistant loads the full instructions by itself, in place of the condensed copy you pasted at level 1 |

Either works without the other. The preferences file needs an assistant that keeps files between
chats, such as a Project. The skill needs an assistant or agent that loads skills.

## Set up once

1. Download [`preferences.md`](preferences.md).
2. Fill in the parts you care about. Leave the rest blank. A blank line means "the assistant
   chooses".
3. For colours and fonts, open the Design spec tab of [`base/studio.html`](../base/studio.html),
   copy the form, fill it in and paste it under "Brand" in your preferences file.
4. Put `preferences.md` where your assistant keeps files for you: the files of the same Project
   that holds the level 1 instructions.
5. If your assistant loads skills, install the skill.

   | Assistant | How |
   | --- | --- |
   | Claude, with skills turned on | Add the folder [`artifact-studio/`](artifact-studio/) as a skill. It loads when you ask for a page or say "use the artifact-studio skill" |
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
