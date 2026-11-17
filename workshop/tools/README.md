# Tools

Three small scripts that keep the repository honest. They need Python 3 and nothing else.

| Script | What it does | Run |
| --- | --- | --- |
| [`check_links.py`](check_links.py) | Finds broken links in every Markdown file | `python3 workshop/tools/check_links.py .` |
| [`check_skills.py`](check_skills.py) | Checks every skill against the published authoring rules: name, description, length, references, test cases | `python3 workshop/tools/check_skills.py skills` |
| [`check_project.py`](check_project.py) | Checks that a project folder follows the layout: a landing page, agent instructions, a licence, a small `base/` and the optional level folders | `python3 workshop/tools/check_project.py projects/artifact-studio` |

Run the first and the third before saying a project is ready.
