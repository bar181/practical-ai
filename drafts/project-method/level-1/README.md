# Project method: level 1, by hand

You and a chat assistant, one stage at a sitting. Nothing to install but Python 3.

**You are done with a stage when** its gate passes. Not before, and not because it feels finished.

| Stage | Paste this to your assistant | Then |
| --- | --- | --- |
| 1. Understand | "Interview me to fill in the top of this North Star page. Ask one question at a time, five at most. Push back if my North Star is vague or if I name more than one job." Attach `docs/north-star.md` | Read it the next morning. Is it true? |
| 2. Research | "Before I build this, find what already exists: built into assistants, open source, and paid. Give each source with a link and the date you checked it. Name the three to six strongest influences and the one thing to take from each. Then recommend build, use or build on top." | Write them into the page |
| 3. Scope | "Finish the page: what is in, three things that are out, what the base holds and what level 1 adds, and a 'done when' line for each item that anyone could check." | **Approve the page, or change it** |
| 4. Plan | "From this North Star page, write the README and the AGENTS file for the folder I attached. Keep every heading that is there. Turn each 'done when' line into a gate. Then write a rubric of six to eight lines, one of them evidence from real use." | Run `python3 ../../tools/check_project.py ../my-tool` |
| 5. Prove | "Take this one real request to one finished result, by the shortest route. No options." Attach real notes | **Is it what you wanted? If not, go back to stage 1** |
| 6. Build | "List every fact that appears in more than one file here. Propose one source file for them and what should be generated from it." | Run the gates after each piece |
| 7. Verify | "Write five requests a real person would type for this tool, with the notes they would attach. Then tell me which of them this tool would answer badly." | Make the examples. Fix the worst answer |
| 8. Score | "Score this tool out of 100 on the rubric in docs/rubric.md. One sentence of evidence for each line. A line with no evidence gets 40 or less. Be blunt." | Read it. Disagree where you can |
| 9. Close | "Go through the closing checklist in the method. Tell me what is stale, what is left over and what lessons to keep." | **Say close.** Then give it to one other person |

## Start

```
python3 ../base/new_project.py my-tool "My tool"
```

Then open `drafts/my-tool/docs/north-star.md` and begin at stage 1.

## If it goes wrong

| What you see | What it means |
| --- | --- |
| You are rewriting the README again | The purpose changed. Go back to stage 1 and say so on the North Star page |
| A gate fails and you want to skip it | The gate is doing its job. Fix the cause, or change the gate and write down why |
| Stage 5 gets "nearly" | Nearly is no. Ask what is missing before building more |
