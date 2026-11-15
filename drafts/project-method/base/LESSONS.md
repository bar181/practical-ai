# Lessons from the first tool

The artifact studio took four shapes before it was right. Each row is something that went wrong,
what it cost, and the rule in [`METHOD.md`](METHOD.md) that now prevents it.

| What happened | What it cost | The rule now |
| --- | --- | --- |
| A gallery of components was built before anyone agreed what the product was | The first version shown to the owner did not work for him: menus with nothing in them, and no examples in sight | Stages 1 to 3: an approved North Star page before any building |
| Each level was built as a full copy of the tool | Three near-identical pages to keep in step, then all three retired | "A level holds only what it adds" |
| The repository was framed as a course, with student guides, when the owner wanted products | Folders and documents that described the wrong thing | Stage 1, Understand, asks what the finished thing is: a product, a guide or a demo |
| The first real output was shown late, after much had been built on it | A rebuild around tabs and visible examples | Stage 5, Prove: one real example, approved, before breadth |
| The same rules were written in the page and again in the server | They would have drifted | Stage 6, Build: one source file, and a test that the copies agree |
| Counts and paths in documents went stale after every restructure | Each change needed a hunt through a dozen files | Generated counts, and a link check as a gate |
| Checks were run by hand from scratch scripts | Nobody else could rerun them, and some were forgotten | `gates.json` and one command |
| Only the author tested | Three faults that no page check could see: a tool that returned half of what an agent needed, a comment that broke a search, keys that needed a click first | Stage 7, Verify: worked examples and a scripted agent |
| The picker gave its best answer however poor | A deck recommended for a job it scored 0 for | Stage 7, Verify: run every request and look at the worst answers |
| The script that generated the plans lived outside the repository | Nobody else could regenerate them | Everything needed to rebuild is in the repository, or archived in it |
| Retired pages stayed where they were | A newcomer could not tell current from old | `plans/archive/`, with a line saying what replaced each thing |
| The first tool was called finished several times before anyone had cleaned up after it | Stale counts, a compiled file in the repository, a README that contradicted the folder beside it | Stage 9, Close: a clean-up checklist, and a person who says close |
| The rubric was written after the work, three times, each a little different | Scores from different rounds could not be compared | Stage 4, Plan: the rubric is written before the work. Stage 8 scores against it |

## What this means for the nine older drafts

They still use the earlier layout: `level-demo`, `level-simple`, `level-working`, `level-automated`
and a student guide. They are not being renamed in bulk, because a rename would make them look
converted while each level still held a full copy.

Each one moves over when it is next worked on, through the method from stage 1:

| Earlier folder | Becomes | Note |
| --- | --- | --- |
| `level-demo/` and the shared files | `base/` | The demo is the base's first example |
| `level-simple/` | `level-1/` | Keep only the instructions. The files it copied go to the base |
| `level-working/` | `level-2/` | Keep only what makes it repeatable |
| `level-automated/` | `level-3/` | Keep only the connections |
| `STUDENT-GUIDE.md` | `README.md`, under "Use it today" | A product has a front door, not a course |
| `AGENT-GUIDE.md` | `AGENTS.md` | Same content, standard name |
| `student-projects/` | Removed | Not part of a product |

`python3 tools/check_project.py drafts/<tool>` lists what is left to do for any one of them.
