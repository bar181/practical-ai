# {{TITLE}}

[One sentence: what this tool does for whom.]

**Think of it as** [an everyday comparison that makes the idea obvious].

**North Star:** [one sentence that says what success is, for a person, in plain words].

## Use it today

| You want | Do this | Takes |
| --- | --- | --- |
| [The main thing] | [The shortest route to it] | [minutes] |

## How it is laid out

`base/` holds everything. A level holds only what it adds.

```
{{SLUG}}/
  README.md      the front door for people
  AGENTS.md      the front door for agents
  gates.json     the checks that must pass
  base/          everything you use
  level-1/       use it by hand
  docs/          the North Star page, the rubric and a progress note
```

| Level | You add | You depend on | State |
| --- | --- | --- | --- |
| Base | Nothing | [A browser] | Not started |
| [Level 1](level-1/) | Instructions | Any chat assistant | Not started |

## Is it working?

```
python3 ../../tools/gates.py .
```

## Status

Stage 1 of 9: Understand. See [`docs/north-star.md`](docs/north-star.md).

| Part | State |
| --- | --- |
| North Star page | Not yet approved |
| Real use | None |
