# How to build a new productivity tool

> These nine steps are how a **plan** is written. They are the detail behind stages 1 to 3 of the
> [project method](../../drafts/project-method/base/METHOD.md), which covers the whole build and the gates.

The steps every tool in this repository goes through, in order. Use it before writing a plan and
again before starting each new level.

**Think of it as:** building a deck. Decide what it is for. Check whether a kit already exists.
Price the lumber. Pick the spot. Draw it. Have someone check the drawing. Build the smallest
platform you can stand on. Extend it only once you are using it.

## The nine steps

| # | Step | What you write down | Stop or go |
| --- | --- | --- | --- |
| 1 | Scope | One user, one job, what is in, what is out, and how you will know it works | Go when the job fits in one sentence |
| 2 | Reuse check | What already exists: built in, open source, established practice | **Stop** if something existing does the whole job. Write a guide, not a tool |
| 3 | Provider review | Outside providers for anything you cannot do with step 2. Review, do not select | Go with a build-or-license view for each level |
| 4 | Dependencies and pricing | Every dependency for the level you are about to build, with its cost and its limits | Go when the simple level has a known cost, ideally zero |
| 5 | Architecture | The simplest set of tools: which assistant, where files live, what stays manual | Go when a beginner could draw it |
| 6 | Plan and steps | The plan, and the step by step process a person will follow | Go when the simple level is fully described |
| 7 | Review | Someone other than the author checks the plan against the scope | Go when the reviewer can explain it back |
| 8 | Build the simplest version and test | The simple level, tested on synthetic data and then by one real user | Go when it passes the check from step 1 |
| 9 | Build incrementally | One level at a time. What you learned. Any skill worth keeping | Move up only when the level below is in use |

## Each step in detail

### 1. Scope

- Name one user and the one job they are trying to get done.
- List what is in and what is out. The out list matters more.
- Write the acceptance check now: a specific input and what a good result looks like. If you cannot
  write it, the scope is not clear yet.
- Note what data the tool touches and what must have a person's approval (anything that posts,
  sends, pays or publishes).

### 2. Reuse check

Look in this order, cheapest first:

1. **Built in.** What chat assistants and coding agents already do: features, bundled skills,
   official skill and plugin catalogues, connectors. For example, before building a page designer,
   check whether the assistant you use already ships a design skill.
2. **Open source.** Repositories and community skills. Note the licence, the last update and who
   maintains it.
3. **Established practice.** How people who do this well actually do it. Three to six practices,
   each with a source link and the date checked.

Take inspiration freely. Record where each idea came from.

### 3. Provider review

Only for what steps 1 and 2 cannot cover, and mostly for levels above simple.

- **Review, do not select.** List the options with what each covers, how it charges, and its limits.
  Choosing comes later, when that level is actually being built.
- This is a build-or-license decision. Write down which way you lean for each level and why.
- Some dependencies cannot be avoided. Video generation is one. Say so plainly and move on.

| Lean | When |
| --- | --- |
| Reuse as is | Something built in or open source does the job |
| Wrap | Something existing does most of it and needs a thin layer of your own rules |
| Build | Nothing fits, the job is small, and you can maintain it |
| License | The capability is hard to build and a provider does it well |

### 4. Dependencies and pricing

Decide for the level you are about to build. Leave later levels as options.

| Record for each dependency | Why |
| --- | --- |
| What it is and what it is needed for | So it can be swapped |
| Cost: free, per month, or per use, and the free-tier limit | So the level has a known price |
| Who pays: the builder or each user | So nobody is surprised |
| What happens if it goes away or changes its price | So there is a way out |

The simple level should run on what a person already has. If it cannot, say what it costs before
anyone starts.

### 5. Architecture

- Pick the fewest moving parts that do the job.
- Decide where things live. A shared drive suits people who are not technical. A repository suits a
  record of every change.
- Decide what stays manual. A manual step that works beats an automated one that might not.
- Prefer one assistant and plain files over a custom application.

### 6. Plan and steps

- Fill in [`PLAN-TEMPLATE.md`](PLAN-TEMPLATE.md).
- Describe the simple level fully. Give each later level one line.
- Write the steps a person follows as a numbered list they could do with the plan closed.

### 7. Review

- A person other than the author, or a fresh agent that has not seen the work, reads the plan.
- They check it against the scope: does it do the one job, and nothing on the out list?
- They try to explain it back in two sentences. If they cannot, simplify.

### 8. Build the simplest version and test

- Build the simple level only.
- Test with synthetic data first, against the acceptance check from step 1.
- Then have one real user follow the steps without help. Watch where they stop.
- Fix the steps before you fix the tool.

### 9. Build incrementally

- Add one level at a time: demo, simple, working, automated.
- Move up only when the level below is being used.
- Each time you repeat a procedure, consider turning it into a skill and adding it to
  [`../../skills/`](../../skills/).
- Go back to step 3 when a new level needs a provider. That is when you select.

## Ways this usually goes wrong

1. Building before checking what exists.
2. Choosing a provider during research, then designing around it.
3. Designing the automated level before the simple level works.
4. Testing only by the person who built it.
5. Finding out what it costs after people depend on it.
6. No written check, so "it works" is an opinion.

## Sources

Checked 2026-11-14.

- [Building effective agents](https://www.anthropic.com/research/building-effective-agents): find the simplest solution and add complexity only when needed.
- [Agent Skills in Codex](https://developers.openai.com/codex/skills.md): skills as a shared format for reusable workflows, which is why the reuse check starts with what is built in.
