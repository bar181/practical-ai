# Web Sections: instructions for agents

You are here because a person wants a website or page started: the sections, their order and a
first responsive build. People start at the [README](README.md).

## The path

| You can | Do this |
| --- | --- |
| Load skills | Load [`base/SKILL.md`](base/SKILL.md) and follow it |
| Open files | Copy sections from [`base/template/sections.html`](base/template/sections.html). Each is wrapped in `SECTION:` comments with a "use when" line |
| Neither | Read [`base/SKILL.md`](base/SKILL.md) as plain instructions. It can build the sections from its own rules |

## What you return

One self-contained HTML page and a note: page type, sections, placeholders, check, next. The exact
layout is in the skill.

## Rules that never bend

1. The person's content is the only source of facts. Placeholders are visible, never guesses.
2. No invented reviews, ratings, prices, logos or awards. A quote section appears only with real words.
3. The library's photos stay in the library. A missing photo is a dashed placeholder box.
4. Structure only: hand words to [Tone Studio](../tone-studio/AGENTS.md) and design to
   [Artifact Studio](../artifact-studio/AGENTS.md).
5. You never publish. A person checks and decides.

## Where things are

| You need | Go to |
| --- | --- |
| The skill | [`base/SKILL.md`](base/SKILL.md) |
| The section library | [`base/template/sections.html`](base/template/sections.html) |
| Photos for the library | [`base/template/img/`](base/template/img/) |
| Social post sizes | [`base/template/social/`](base/template/social/) |
| A worked example | [`base/examples/cafe-home.html`](base/examples/cafe-home.html) |
| A saved section set (Level 2) | [`level-2-files/`](level-2-files/) |
| The tests and evidence | [`_build/eval/`](_build/eval/), [`quality-results/`](quality-results/README.md) |
| The plan | [`workshop/plans/web-sections/`](../../workshop/plans/web-sections/README.md) |
