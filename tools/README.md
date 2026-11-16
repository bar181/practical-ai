# Tools

Four small scripts that keep the repository honest. They need Python 3 and nothing else.

| Script | What it does | Run |
| --- | --- | --- |
| [`gates.py`](gates.py) | Runs every gate a project lists in its `gates.json` and ends with "All gates that ran passed" or "DO NOT SHIP" | `python3 tools/gates.py drafts/project-method` |
| [`check_links.py`](check_links.py) | Finds broken links in every Markdown file | `python3 tools/check_links.py .` |
| [`check_skills.py`](check_skills.py) | Checks every skill against the published authoring rules: name, description, length, references, test cases | `python3 tools/check_skills.py skills` |
| [`check_project.py`](check_project.py) | Checks that a project folder follows the layout: a landing page, agent instructions, a licence, a small `base/` and the optional level folders | `python3 tools/check_project.py projects/artifact-studio` |

**Think of a gate as** the check a pilot runs before take-off. It is short, it is the same every
time, and it does not depend on anyone remembering.

A gate is one command that must succeed. A project lists its gates in `gates.json`, each with a
line saying what it proves. How gates fit into building a tool is in
[`drafts/project-method/`](../drafts/project-method/).
