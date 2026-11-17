# Autopilot progress

Autopilot is the Level 2 route where a coding agent takes a spec and guidance to a finished tool
without a person at each step. It is tracked here, apart from the method, because none of it has
run end to end yet. The definition is in [the spec](SPEC.md), sections 4 to 8.

| Part | State | Evidence |
| --- | --- | --- |
| The autopilot section of the skill | Written | `projects/agentic-process/level-2-files/agentic-process/SKILL.md` |
| The prompt, the delivery targets and what comes back | Written | `projects/agentic-process/level-2-files/AUTOPILOT.md` |
| Gate `spec-ready` | Not built | |
| Gate `tested` | Not built | |
| Gate `handback` | Not built | |
| AC-1: the learning-system spec to a draft pull request | Not run | |
| AC-6: a chatbot tool package from a spec | Not run by Autopilot. The decision-support tool was built with the method in a guided session and tested by fresh sessions | `projects/agentic-process/base/examples/decision-support/` |

**Next:** build the three gates (about 45 minutes), then run AC-1.
