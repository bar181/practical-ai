"""Tests for level-2-files/check_sources.py, with a local web server so no network is needed.

  python3 _build/test_check_sources.py   (from projects/decision-support)
Each case states what the checker must report. Exit code 1 on any failure.
"""
import functools, http.server, os, subprocess, sys, tempfile, threading

here = os.path.dirname(os.path.abspath(__file__))
pages = os.path.join(here, "test-pages")
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


handler = functools.partial(Quiet, directory=pages)
server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{server.server_port}"

brief = f"""# Test brief

| # | The exact words | Source and link | Checked | Result |
| --- | --- | --- | --- | --- |
| 1 | "it will only allow one writer at any instant in time." | Appropriate uses, {base}/sqlite-whentouse.html | 24 Nov 2026 | Checked |
| 2 | “SQLite works great as the database engine for most low to medium traffic websites” | {base}/sqlite-whentouse.html | 24 Nov 2026 | Checked |
| 3 | "SQLite supports an unlimited number ... one writer at any instant" | {base}/sqlite-whentouse.html | 24 Nov 2026 | Checked |
| 4 | "SQLite is always faster than PostgreSQL" | {base}/sqlite-whentouse.html | 24 Nov 2026 | Partly |
| 5 | "a page that is gone" | {base}/missing.html | 24 Nov 2026 | Could not open |
| 6 | "14 people need a phone line" | Our figures, from the person | 24 Nov 2026 | Their figures |
"""
expect = {"1": "OK", "2": "OK", "3": "OK", "4": "WORDS NOT FOUND", "5": "COULD NOT OPEN", "6": "NO LINK"}
script = os.path.join(here, "..", "level-2-files", "check_sources.py")
failures = []
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "brief.md")
    open(path, "w", encoding="utf-8").write(brief)
    run = subprocess.run([sys.executable, script, path, "--timeout", "5"], capture_output=True, text=True)
    out = run.stdout
    for num, status in expect.items():
        line = next((l for l in out.splitlines() if l.startswith(f"[{num}]")), "")
        if status not in line:
            failures.append(f"row {num}: expected {status}, got: {line or '(no line)'}")
    if run.returncode != 0:
        failures.append(f"exit code {run.returncode}: no Checked row fails, so it should be 0")
    # A Checked row that does not hold up must fail the run.
    open(path, "w", encoding="utf-8").write(brief.replace("| Partly |", "| Checked |"))
    if subprocess.run([sys.executable, script, path, "--timeout", "5"], capture_output=True).returncode != 1:
        failures.append("a Checked row with words not on the page did not give exit code 1")
server.shutdown()
print(out)
print("FAIL\n  " + "\n  ".join(failures) if failures else "PASS: 6 rows and the exit-code rule as expected")
sys.exit(1 if failures else 0)
