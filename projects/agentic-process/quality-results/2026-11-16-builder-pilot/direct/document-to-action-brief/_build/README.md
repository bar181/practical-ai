# _build: the test

You do not need this folder to use the tool. It holds the test for the instructions and the worked
example. Standard library Python only.

| File | What it does |
| --- | --- |
| [`check_brief.py`](check_brief.py) | `python3 _build/check_brief.py BRIEF DOCUMENT [KEY]`. Checks that every quote in a brief appears word for word in the document, and, with a key, scores the brief against the acceptance test |
| [`test-key.json`](test-key.json) | The plan's acceptance test for the invented notice: three obligations, two dates, the $25 penalty flagged, the unclear standing-order line under questions, and the suggestion in para 7 not listed as a duty |
| [`run_tests.py`](run_tests.py) | `python3 _build/run_tests.py`. Runs three cases, each with the outcome it must have (below) |
| [`tests/weak-brief.md`](tests/weak-brief.md) | A hand-written weak brief, invented, with the mistakes a plain "summarise this" answer tends to make. It must fail |

## The three cases

| Case | Must |
| --- | --- |
| The worked example as published | Fail on exactly one quote, the planted O2, and on the O2 acceptance item only |
| The worked example with O2 replaced by the corrected line from its part 3 | Pass every quote and the whole acceptance test. The clean brief is made in memory, never stored, so there is one source |
| The weak brief | Fail |

## Testing a real chatbot run

Save the chatbot's brief as a Markdown file and run:

```
python3 _build/check_brief.py my-run.md base/supplier-notice.md _build/test-key.json
```

The quote check works on a brief for any document. The key works only for the invented notice.
This checker tests the instructions. It does not replace the person's own check against the page.
