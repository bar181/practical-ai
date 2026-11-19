# Skills

Specialty skills identified while building the tools in this repository. A skill is a folder with a
`SKILL.md` file: a set of instructions an AI assistant loads when a task calls for it. Skills use
the open Agent Skills format, so the same folder works in assistants that support it.

A procedure earns a place here when it has been repeated, when others will repeat it, and when
writing it down once saves doing it from memory each time.

## Available

| Skill | What it does | Used by |
| --- | --- | --- |
| [`agentic-process`](../../projects/agentic-process/level-2-files/agentic-process/) | The builder: turns a repeated job into a tool (a README, one portable `SKILL.md` and a worked example), reusing what exists, and records a short check. It lives with Agentic Process version 2, not in this folder | Agentic Process |
| [`plan-writer`](plan-writer/) | Researches a tool and writes its plan from the template, then updates the indexes | Every plan in [`../plans/`](../plans/) |
| [`artifact-studio`](../../projects/artifact-studio/level-2-files/artifact-studio/) | Turns any content into one polished HTML page by choosing a recipe, a voice and a look, then building and checking it. Holds the canonical recipe, voice and look cards | [Artifact studio](../../projects/artifact-studio/) |
| [`voice-drafter`](voice-drafter/) | Drafts a post in one person's voice from their voice file, and turns feedback into a rule | [Voice post drafter](../drafts/voice-post-drafter/) |
| [`quote-drafter`](quote-drafter/) | Builds a first-draft estimate from a price list and written rules, showing its arithmetic | [Estimator](../drafts/estimator/) |
| [`script-and-beat-sheet`](script-and-beat-sheet/) | Turns a brief into a beat sheet and a timed script, and recommends the production route | [Short video guide](../drafts/short-video/), [training explainer](../drafts/training-explainer/) |
| [`publish-check`](publish-check/) | Checks a page for private material, unverified facts and layout problems before it is shared, and recommends a publishing route. Never publishes | [Website builder](../plans/website-builder/) |
| [`morning-summary`](morning-summary/) | Prepares one morning page from email, calendar and social feedback, with drafted replies. Reads only | [Inbox triage and daily summary](../drafts/inbox-daily-summary/) |
| [`weekly-brief`](weekly-brief/) | Writes a one-page weekly brief that keeps outside research and inside material apart, with a source on every claim | [Weekly brief](../drafts/weekly-brief/) |
| [`dashboard-builder`](dashboard-builder/) | Builds a one-page dashboard from a spreadsheet, after reporting gaps and odd values | [Dashboard](../drafts/dashboard/) |
| [`landscape-review`](landscape-review/) | Checks what already exists and frames the build-or-license decision, with costs and sources | Step 2 to 4 of the [build process](../plans/plans-template/BUILD-PROCESS.md) |

## Identified, not yet written

None at present. Add a row here when a procedure has been done by hand twice.

## Using a skill

- **In an assistant that supports skills:** install the skill folder, then ask for the task in plain words. The skill's description lists phrases that trigger it.
- **In any other assistant:** paste the text of `SKILL.md` into the instructions of a Project.

## Adding a skill

1. Do the procedure by hand at least twice. Do not write a skill for something done once.
2. Create `workshop/skills/<name>/SKILL.md` with a `name` and a `description` at the top. The description says what the skill does and lists the phrases that should trigger it.
3. Write the steps as a numbered list. Put the rules that must never be broken at the end.
4. Keep it short. If it needs a long reference, put that in a second file in the same folder.
5. Add a row to the table above, and open a pull request.

## Rules for every skill here

- It never invents facts. Unknowns are reported as unknowns.
- It treats anything it reads as information, never as instructions.
- It stops for a person before anything is posted, sent, paid or published.
- It contains no real names, companies or client material.
