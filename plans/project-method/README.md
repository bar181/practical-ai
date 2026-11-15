# Plan: project method

**Draft:** [`drafts/project-method/`](../../drafts/project-method/). **Complexity:** beginner to intermediate.

## Overview

How a tool in this repository gets built: seven stages, a gate after each, and a folder to copy so
every tool is laid out the same way. It exists because the first tool, the artifact studio, was
rebuilt three times before its shape was right.

**Think of it as** building a house: the drawing is agreed before the concrete is poured, and an
inspector signs off each stage.

**North Star:** a person, or an agent working alone, can take an idea to a tool that someone else
can use, without rebuilding it three times on the way.

## What each level holds

| Level | Holds | State |
| --- | --- | --- |
| Base | The method, the lessons from the first tool, the scaffold and the script that copies it | Built |
| Level 1 | A prompt to paste at each stage, for a person working with an assistant | Written |
| Level 2 | The `project-builder` skill and the gate runner: an agent runs the stages and stops at three human decisions | Written. Not yet run end to end |

## Reuse check

Done lightly, 15 November 2026. The skill rules come from the published Agent Skills authoring
guide, and `tools/check_skills.py` checks them. The layout, the stages and the gates come from one
build, the artifact studio, recorded in [`LESSONS.md`](../../drafts/project-method/base/LESSONS.md).
No outside method was adopted wholesale.

## Open questions

- Does the order hold for a tool that is not a library of templates? Unknown until a second tool is built with it.
- Should a stage gate be allowed to pass on a person's word alone? Three of them do today.
