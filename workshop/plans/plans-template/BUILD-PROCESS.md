# How to build a new tool

The method now lives in one place: the Agentic Process
[process page](../../../projects/agentic-process/base/PROCESS.md), with its nine steps as a checklist,
and its [builder skill](../../../projects/agentic-process/level-2-files/agentic-process/SKILL.md),
which runs it. Follow those. The longer guide that stood here was replaced on 16 November 2026.

## What the first build taught us

Artifact Studio was the first tool taken through to a showcase, in November 2026. These are the
things to do differently next time, each with the step it belongs to.

| Learning | What happened | Do this next time | Step |
| --- | --- | --- | --- |
| Name the one thing that makes people stop | Photo effects were the wow. They were built as one tab among many and promoted late | Decide the wow in the scope and build it first. Everything else is table stakes | 1 |
| Decide how you credit a style before you write | Three named people were removed from twelve files near the end | Describe the style. Do not name a person, a show or a brand | 1 |
| Fix the folder layout before you build | The layout changed four times. Each change meant moving files and rewriting links | Agree the layout in [`projects/README.md`](../../../projects/README.md) at this step and keep it | 5 |
| Write public links for the branch you will merge into | Every link named the working branch and had to be changed at the pull request | Point links at `main` from the first day | 5 |
| Plan the front door, not only the tool | The reviewer asked for one download and a worked example for every variant, with its prompt and sample input | Put these in the plan: a hook, one picture, "Try it in five minutes" first, one file to download, one worked example per variant | 6 |
| Test in a fresh chat before you polish | One run in a fresh session found six contradictions in the instructions that the author could not see | Run the beginner prompt in a fresh chat as soon as it exists, and fix what it finds before adding anything | 8 |
| Say what a result really is | Reference pages were built by hand. Calling them "examples" suggested a chat had made them | Label a hand-built page as a reference until a real run replaces it | 8 |
| Let the build check the numbers | Counts printed on pages drifted twice. The build caught both because it compares them with the library | Any number shown to a reader is checked by the build, or is not shown | 8 |
| One source, generated outputs | Edits to generated files were lost. A rebuild from a clean checkout must change nothing | Keep one source for each thing. Run the clean rebuild before every push | 8 |
| Record where every picture came from | Pictures arrived in batches. One carried a well-known character's emblem and was left out | Note the origin of each picture when it enters the repository. Refuse a picture with someone else's character or logo | 8 |
| One addition, one pull request | Post previews, a new voice and two layouts all rode in on the first pull request | Merge the first showcase. Then one pull request for each addition | 9 |
