"""run_tests.py: test the checker and the worked example. Run from anywhere: python3 _build/run_tests.py

Three cases, each with the outcome it must have:
  1. The worked example as published, with its planted error: exactly one quote fails (O2), and the
     acceptance test fails on O2 only.
  2. The worked example with O2 replaced by the corrected line from part 3 of the same file: every
     quote matches and the acceptance test passes. One source: the clean brief is never stored.
  3. A weak brief (tests/weak-brief.md): fails, so the checker can tell a bad brief from a good one.
Exit code 1 if any case has the wrong outcome.
"""
import contextlib, io, os, re, sys, tempfile

sys.dont_write_bytecode = True                                       # leave no __pycache__ behind
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import check_brief  # noqa: E402

root = os.path.dirname(here)
notice = os.path.join(root, "base", "supplier-notice.md")
example = os.path.join(root, "base", "examples", "worked-example.md")
key = os.path.join(here, "test-key.json")


def run(brief_path):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = check_brief.main(["check_brief.py", brief_path, notice, key])
    return code, buf.getvalue()


text = open(example, encoding="utf-8").read()
fixed_row = re.search(r"<!-- corrected:start -->\s*(\|.*?)\s*<!-- corrected:end -->", text, re.S).group(1)
brief = re.search(r"<!-- brief:start -->(.*?)<!-- brief:end -->", text, re.S).group(1)
clean = re.sub(r"^\| O2 \|.*$", lambda m: fixed_row, brief, count=1, flags=re.M)
assert clean != brief, "could not find the O2 row to replace"

with tempfile.TemporaryDirectory() as tmp:
    clean_path = os.path.join(tmp, "clean-brief.md")
    open(clean_path, "w", encoding="utf-8").write(clean)
    cases = [
        ("worked example as published, with the planted error", example,
         lambda c, out: c == 1 and out.count("NOT IN DOCUMENT") == 1 and "the business day before" in out
         and out.count("FAIL") == 1 and "FAIL  O2" in out),
        ("worked example after the check fixed O2", clean_path, lambda c, out: c == 0),
        ("weak brief", os.path.join(here, "tests", "weak-brief.md"), lambda c, out: c == 1),
    ]
    bad = 0
    for name, path, expected in cases:
        code, out = run(path)
        ok = expected(code, out)
        bad += not ok
        print(f"{'ok  ' if ok else 'WRONG'} {name}")
        print("      " + out.strip().replace("\n", "\n      "))
print("ALL CASES AS EXPECTED" if not bad else f"{bad} case(s) wrong")
sys.exit(1 if bad else 0)
