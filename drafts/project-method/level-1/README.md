# Project method: level 1, by hand

You and a chat assistant, one stage at a sitting. Nothing to install but Python 3.

**You are done with a stage when** its gate passes. Not before, and not because it feels finished.

| Stage | Paste this to your assistant | Then |
| --- | --- | --- |
| 1. Purpose | "Interview me to fill in this purpose page. Ask one question at a time. Push back if my North Star is vague or if I name more than one job." Attach `docs/purpose.md` | Read the page the next morning. Approve it or change it |
| 2. Reuse check | "Before I build this, find what already exists: built into assistants, open source, and paid. Give each source with the date you checked it, then recommend build, use or build on top." | Write the decision into `docs/purpose.md` |
| 3. Skeleton | "From this purpose page, write the README and the AGENTS file for the folder I attached. Keep every heading that is already there. Then propose three to six gates that would prove this tool works." | Run `python3 ../../tools/check_project.py ../my-tool` |
| 4. One real example | "Take this one real request to one finished result, by the shortest route. No options." Attach real notes | Look at it. Is it what you wanted? If not, go back to stage 1 |
| 5. One source, then breadth | "List every fact that appears in more than one file here. Propose one source file for them and what should be generated from it." | Run the gates |
| 6. Play the user and the agent | "Write five requests a real person would type for this tool, with the notes they would attach. Then tell me which of them this tool would answer badly." | Make the examples. Fix the worst answer |
| 7. Ship honestly | "Score this tool out of 100 on a rubric of six lines. One line must be evidence from real use. Be blunt." | Give it to one other person for a real job |

## Start

```
python3 ../base/new_project.py my-tool "My tool"
```

Then open `drafts/my-tool/docs/purpose.md` and begin at stage 1.

## If it goes wrong

| What you see | What it means |
| --- | --- |
| You are rewriting the README again | The purpose changed. Go back to stage 1 and say so on the page |
| A gate fails and you want to skip it | The gate is doing its job. Fix the cause, or change the gate and write down why |
| Stage 4 gets "nearly" | Nearly is no. Ask what is missing before building more |
