"""gates.py PROJECT_FOLDER [--all]: run a project's gates and say plainly whether it may ship.

A gate is one command that must exit with code 0. A project lists its gates in gates.json:

    [{"name": "links", "proves": "No Markdown link is broken", "run": "python3 ../../tools/check_links.py ."},
     {"name": "pages", "proves": "...", "run": "...", "slow": true}]

Commands run from the project folder, in order. Gates marked slow run only with --all.
The run stops at nothing: every gate is run, so one report shows everything that is wrong.
Exit code 0 only if every gate that ran passed.
"""
import json, os, subprocess, sys, time

if len(sys.argv) < 2:
    sys.exit(__doc__)
project = os.path.abspath(sys.argv[1]); run_all = "--all" in sys.argv
gates = json.load(open(os.path.join(project, "gates.json"), encoding="utf-8"))
TAIL = 6                                                             # lines of a failed gate's output to show
results = []
for g in gates:
    if g.get("slow") and not run_all:
        results.append((g["name"], "skipped", 0, g["proves"], "")); continue
    t = time.time()
    p = subprocess.run(g["run"], shell=True, cwd=project, capture_output=True, text=True, timeout=g.get("timeout", 1800))
    out = (p.stdout + p.stderr).strip().splitlines()
    results.append((g["name"], "pass" if p.returncode == 0 else "FAIL", time.time() - t, g["proves"], "\n".join(out[-TAIL:]) if p.returncode else (out[-1] if out else "")))
width = max(len(r[0]) for r in results)
for name, state, secs, proves, detail in results:
    print(f"{state:8}{name:{width + 2}}{secs:6.1f}s  {proves}")
    if state == "FAIL":
        print("\n".join("          " + l for l in detail.splitlines()))
failed = [r[0] for r in results if r[1] == "FAIL"]; skipped = [r[0] for r in results if r[1] == "skipped"]
print("\n" + ("DO NOT SHIP. Failed: " + ", ".join(failed) if failed else "All gates that ran passed." + (f" Not run (use --all): {', '.join(skipped)}." if skipped else "")))
sys.exit(1 if failed else 0)
