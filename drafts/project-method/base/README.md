# Project method: the base

Everything the method is made of.

| File | What it is |
| --- | --- |
| [`METHOD.md`](METHOD.md) | The seven stages, what each produces and the gate that ends it |
| [`LESSONS.md`](LESSONS.md) | What went wrong on the first tool, and the rule each lesson became |
| [`scaffold/`](scaffold/) | The folder every new tool starts as. Words in double braces are filled in by the script |
| [`new_project.py`](new_project.py) | Copies the scaffold to `drafts/<slug>/` and fills in the name |

The gate runner and the three checks live in [`tools/`](../../../tools/), because every tool in the
repository uses them.
