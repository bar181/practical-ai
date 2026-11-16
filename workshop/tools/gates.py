"""gates.py PROJECT_FOLDER [--all]: run a project's gates and say plainly whether it may ship.

A gate is one command that must exit with code 0. A project lists its gates in gates.json:

    [{"name": "links", "proves": "No Markdown link is broken", "run": "python3 ../../tools/check_links.py ."},
     {"name": "pages", "proves": "...", "run": "...", "slow": true}]

Commands run from the folder that holds gates.json, in order. That is the project folder, or its base/ folder
when the project keeps everything there. A showcase may keep the file in level-3-files/ or in _build/; its
commands still run from the project folder. Gates marked slow run only with --all.
The run stops at nothing: every gate is run, so one report shows everything that is wrong.
Exit code 0 only if every gate that ran passed.
"""
import json, os, subprocess, sys, time

if len(sys.argv) < 2:
    sys.exit(__doc__)
project = os.path.abspath(sys.argv[1]); run_all = "--all" in sys.argv
if not os.path.exists(os.path.join(project, "gates.json")) and os.path.exists(os.path.join(project, "base", "gates.json")):
    project = os.path.join(project, "base")                          # a project that keeps everything in base/ keeps its gates there too
gates_file = os.path.join(project, "gates.json")
if not os.path.exists(gates_file) and os.path.exists(os.path.join(project, "level-3-files", "gates.json")):
    gates_file = os.path.join(project, "level-3-files", "gates.json")   # a showcase keeps its gates with its expert files. Commands still run from the project folder
if not os.path.exists(gates_file) and os.path.exists(os.path.join(project, "_build", "gates.json")):
    gates_file = os.path.join(project, "_build", "gates.json")          # a new showcase starts with its gates beside its build files
if not os.path.exists(gates_file):
    sys.exit(f"No gates.json in {project}, its _build/ or its level-3-files/. Write one: a list of checks, each with name, proves and run.")
gates = json.load(open(gates_file, encoding="utf-8"))
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
