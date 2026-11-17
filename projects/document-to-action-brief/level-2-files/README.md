# Level 2: save it, and add your house rules

Level 1 is one prompt you paste each time. Level 2 saves the full instructions once, so every
document you attach gets the same brief, and adds a short file of your own house rules so the brief
fits your business. Worth it if documents like this reach you every week.

## 1. Save the instructions

Copy all of [`../base/SKILL.md`](../base/SKILL.md) (press **Raw** on GitHub).

| Where you work | Do this |
| --- | --- |
| Claude | Add it as a skill in a folder named `document-to-action-brief`, or paste it into a Project's instructions |
| ChatGPT | Add it as a skill: ChatGPT skills use the same open Agent Skills format. Or paste it into a Project's instructions |
| Gemini | Paste it into a Gem's instructions |
| A coding agent (Claude Code, Codex) | Put the folder in the agent's skills folder |

Then attach a document and say who you are in it. The skill works out the situation itself.

## 2. Add your house rules

Copy [`house-rules.md`](house-rules.md), fill it in, and add it to the same Project, Gem or skill
folder. It tells the brief who you are, which documents you get, who answers which kind of
question, and where actions should go. Five minutes, once.

## 3. Ask for a follow-up

At the end of each brief, ask for one of these in a sentence:

- `Write an email to my team with these actions and owners.`
- `List these dates so I can add them to my calendar.`
- `Turn this brief into a one-page report with Artifact Studio.` (see [Artifact Studio](../../artifact-studio/))

Nothing is sent or added for you. You copy what you want.

## Status

Level 2 is the same instructions as Level 1, saved. Saving it as a skill was tested in Claude,
where the skill ran on two documents (see [the evidence](../quality-results/README.md)). Not yet
tried in ChatGPT or Gemini. The house rules file has not been tested.
