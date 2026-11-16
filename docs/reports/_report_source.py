"""Writes 2026-11-16-agentic-process-report.html, a report on Agentic Process for its owner.

    python3 docs/reports/_report_source.py

Made by following Artifact Studio's instructions: one-page report recipe, analyst voice, the Practical AI
colours. Every number on the page is in the tables below, with where it came from.
"""
import html, pathlib
E = html.escape
HERE = pathlib.Path(__file__).resolve().parent

# The end-user rubric, scored by the author. "before" is the review written on 16 November 2026 in the morning.
RUBRIC = [  # measure, morning, now, evidence for now
 ("Purpose is clear in one screen", 84, 86, "Hook, the guide recommended at the top, the picture now present, the training linked"),
 ("A beginner gets value fast", 78, 78, "A short path for small jobs, a stop line and a ready-made second prompt if the link fails. Six coach runs; none in ChatGPT, none by a person"),
 ("Base content is worth its place", 82, 86, "Six items, each with a reader. One plan template. Examples made by the current or a recent coach"),
 ("Each step is easy to follow", 85, 86, "Purpose, a user story per level with a filter, what to expect, proof, the gate and a prompt"),
 ("The Advanced level works where builders work", 62, 80, "One folder that works in any repository. The fourth audit ran it in an empty repository, filled a project by hand and saw every check pass; its one blocking point, a copy command, is fixed"),
 ("The Expert level is usable as given", 66, 78, "Four starter gates, a full unattended run as a worked example, one rule for which test points to fix first"),
 ("The scaffolding is clean", 78, 84, "Test logs in _build/runs, every repeated page written by one build, a place named for code"),
 ("The files agree with each other", 70, 86, "The third audit found the steps, gates and plan headings word for word the same in all four places"),
 ("Honest about what is proven", 92, 88, "Every status line says who tried it. The audits caught two claims that had gone stale; both are dated now"),
 ("Evidence of real value", 25, 25, "AI sessions only. No person has used it, and no chatbot other than Claude has run it"),
]
# The independent newcomer audit: a fresh session reading the project as three people. Before = first audit, after = second.
AUDIT = [("Beginner, uses ChatGPT", 64, 60, 72, 72), ("Builder with a coding agent", 60, 70, 52, 76), ("Teacher with a class tomorrow", 52, 58, 70, 74)]
AUDIT_FOUND = [(4, 16, 23), (4, 12, 19), (1, 12, 16), (1, 7, 20)]   # blocking, confusing, minor, per audit
# GitHub, read through the GitHub API on 16 November 2026.
GITHUB = {"stars": 0, "forks": 0, "watchers": 0, "topics": 0, "releases": 0, "community_profile": 42,
          "description": "Suite of practical ai assisted workflows and automation tools - no fluff, just productivity",
          "homepage": "none", "pages": "off", "discussions": "off", "template": "no", "traffic": "not readable from this session"}
TESTS = [  # what ran on Agentic Process, all on 16 November 2026, all Claude sessions
 ("Coach runs by fresh sessions", 6), ("Skill runs by a second agent", 2), ("Fresh-session tests of a tool the skill built", 2), ("Newcomer audits", 4)]


def bars(rows):
    """rows: (name, value, value, ...). The last value is drawn in the data colour, the others in greys."""
    out = []
    for name, *vals in rows:
        cls = ['was', 'mid', 'now'][-len(vals):] if len(vals) <= 3 else ['was'] * (len(vals) - 2) + ['mid', 'now']
        spans = ''.join(f'<span class="bar {c}" style="--v:{v}%" title="{v}"><b>{v}</b></span>' for c, v in zip(cls, vals))
        out.append(f'<div class="pair" role="listitem"><span class="nm">{E(name)}</span>{spans}</div>')
    return '\n'.join(out)


def page():
    rub_before = round(sum(r[1] for r in RUBRIC) / len(RUBRIC)); rub_now = round(sum(r[2] for r in RUBRIC) / len(RUBRIC))
    au = [round(sum(a[i] for a in AUDIT) / 3) for i in (1, 2, 3, 4)]
    at80 = sum(1 for r in RUBRIC if r[2] >= 80)
    rub_rows = ''.join(f'<tr><th scope="row">{E(m)}</th><td>{a}</td><td><b>{b}</b></td><td>{E(ev)}</td></tr>' for m, a, b, ev in RUBRIC)
    below = [m for m, a, b, ev in RUBRIC if b < 80]
    gh = GITHUB
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agentic Process: where it stands</title>
<!-- Written by docs/reports/_report_source.py. Recipe: one-page report. Voice: analyst. Look: the Practical AI colours. -->
<style>
:root{{--bg:#f3f5f9;--panel:#fff;--line:#c9d1de;--muted:#48546a;--ink:#14202e;--accent:#0c2340;--hl:#ffd23f;--data:#2f6fb5;--was:#b8c2d1;
  --display:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--text:Georgia,"Iowan Old Style","Times New Roman",serif;color-scheme:light}}
*,*::before,*::after{{box-sizing:border-box}}html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--bg);color:var(--ink);font:400 1.08rem/1.55 var(--text)}}
h1,h2,h3{{font-family:var(--display);margin:0;line-height:1.1;letter-spacing:-.015em;text-wrap:balance}}p{{margin:0}}
a{{color:var(--accent)}}:focus-visible{{outline:3px solid var(--data);outline-offset:3px}}
.wrap{{max-width:900px;margin-inline:auto;padding-inline:20px}}
header{{background:var(--accent);color:#fff;padding:40px 0 34px}}
.meta{{font:700 .9rem/1.3 var(--display);color:var(--hl)}}
h1{{font-size:clamp(1.9rem,6.4vw,3rem);margin-top:12px;max-width:20em}}
.answer{{margin-top:16px;max-width:38em;font-size:1.18rem;color:#dfe6ef}}
.tiles{{display:grid;gap:12px;margin-top:26px}}@media(min-width:720px){{.tiles{{grid-template-columns:repeat(3,1fr)}}}}
.tile{{background:#17365f;border-radius:12px;padding:16px}}.tile b{{display:block;font:800 2.4rem/1 var(--display);color:#fff}}
.tile span{{display:block;margin-top:8px;font:400 .98rem/1.35 var(--display);color:#dfe6ef}}.tile i{{font-style:normal;color:var(--hl);font-weight:700}}
section{{padding-top:46px}}h2{{font-size:clamp(1.4rem,4.6vw,2rem);max-width:24em}}
.lab{{font:700 .86rem/1.2 var(--display);color:var(--data);margin-bottom:8px}}
section p+p,section h2+p{{margin-top:12px}}section p{{max-width:40em}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px;margin-top:18px}}
.lv{{display:grid;gap:12px;margin-top:16px}}@media(min-width:760px){{.lv{{grid-template-columns:repeat(3,1fr)}}}}
.lv div{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px;font:400 1rem/1.45 var(--display)}}.lv b{{display:block;font-size:1.08rem;margin-bottom:6px}}
figure{{margin:18px 0 0;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px 16px 14px}}
.key{{display:flex;flex-wrap:wrap;gap:16px;font:400 .92rem/1.2 var(--display);color:var(--muted);margin-bottom:12px}}.key span::before{{content:"";display:inline-block;width:14px;height:10px;border-radius:2px;margin-right:6px;background:var(--was)}}.key .k2::before{{background:var(--data)}}.key .k1::before{{background:#8d9ab0}}
.chart{{display:grid;gap:14px}}.pair{{display:grid;gap:3px;font:400 .95rem/1.25 var(--display)}}.pair .nm{{color:var(--ink)}}
.bar{{display:flex;align-items:center;justify-content:flex-end;width:var(--v);min-width:2.6em;height:20px;border-radius:0 4px 4px 0;background:var(--was)}}.bar.now{{background:var(--data)}}
.bar.mid{{background:#8d9ab0}}.bar b{{padding-right:6px;font:700 .82rem/1 var(--display);color:var(--ink)}}.bar.now b{{color:#fff}}
figcaption{{margin-top:12px;font:400 .86rem/1.4 var(--display);color:var(--muted)}}
.so{{margin-top:14px;padding:12px 14px;border-left:5px solid var(--data);background:var(--panel);border-radius:0 10px 10px 0;font:400 1rem/1.45 var(--display)}}
.tw{{overflow-x:auto;margin-top:14px}}table{{border-collapse:collapse;width:100%;min-width:560px;font:400 .94rem/1.4 var(--display)}}
th,td{{text-align:left;vertical-align:top;padding:9px 10px;border-bottom:1px solid var(--line)}}thead th{{font-size:.84rem;color:var(--muted)}}
tr.weak th,tr.weak td{{background:#fff7d6}}
details{{margin-top:12px}}summary{{cursor:pointer;min-height:44px;display:flex;align-items:center;font:700 1rem/1.3 var(--display)}}
ol.next{{padding-left:1.3em;font:400 1rem/1.5 var(--display);max-width:42em}}ol.next li+li{{margin-top:8px}}
.tag{{display:inline-block;padding:2px 7px;border-radius:4px;font:700 .78rem/1.3 var(--display);background:#e6ecf4;color:var(--accent)}}.tag.real{{background:#dff1e4;color:#1d5b33}}
footer{{margin-top:50px;background:var(--accent);color:#dfe6ef;padding:28px 0 36px;font:400 .92rem/1.5 var(--display)}}footer a{{color:var(--hl)}}
</style>
</head>
<body>
<header><div class="wrap">
  <p class="meta">Report for the owner of Practical AI · 16 November 2026 · Project two: Agentic Process</p>
  <h1>Agentic Process is ready to try and to teach; nobody but its author has used it yet.</h1>
  <p class="answer">Four independent audits and nine test runs found and fixed the faults a newcomer would hit at every level; every newcomer's score rose, and the last audit's fixes have not been audited again. GitHub shows none of this yet: no stars, no topics and no page that opens on a phone, and the links work only once the branch is merged.</p>
  <div class="tiles">
    <div class="tile"><b>{rub_before} → {rub_now}</b><span>The end-user rubric, out of 100, this morning and now. <i>{len(below)} of 10</i> measures still below 80.</span></div>
    <div class="tile"><b>{au[0]} → {au[3]}</b><span>An independent newcomer's average score, first audit to fourth (then {au[1]} and {au[2]} between), as a beginner, a builder and a teacher.</span></div>
    <div class="tile"><b>0</b><span>People outside the author who have used it. Every test so far was an AI session, in Claude.</span></div>
  </div>
</div></header>
<main class="wrap">

<section aria-labelledby="what"><p class="lab">What it is</p><h2 id="what">An order of work that stops an AI from building the wrong thing well.</h2>
  <p><b>Think of it as</b> a building site with an inspector. You agree the drawing before you pour concrete, and nobody moves to the next stage until the current one is signed off.</p>
  <p>Nine steps take an idea to a first version someone else can try: scope, reuse check, outside help, cost, simplest design, plan and front door, review, build and test, grow. Each step has a purpose, a user story for each level, what to expect, proof it is done, a prompt to paste, and a gate: a question you answer before you go on. Step 8 hands the work to a stranger, a fresh AI session that has only your instructions, and keeps a log of every place it had to guess.</p>
  <div class="lv">
    <div><b>Beginner</b>Pastes one prompt into any chatbot. A small job takes the short path (steps 1, 6 and 8 in full). Leaves with a one-page plan, a reusable prompt and a test.</div>
    <div><b>Advanced</b>Copies one skill folder into a coding agent. Any repository. The agent makes a project folder with its own checks, and stops at each gate.</div>
    <div><b>Expert</b>Agents work unattended: gates a script runs, fresh-session tests started by an orchestrator, a score sheet. A person reads the hand-back and decides.</div>
  </div>
  <p style="margin-top:14px">For teaching there is a 30-minute training: ten slides on Artifact Studio's workshop deck, a lesson timer, and a presenter window that keeps the notes off the projector.</p>
</section>

<section aria-labelledby="f1"><p class="lab">Finding 1</p><h2 id="f1">Over four audits every newcomer's score rose: the teacher's from {AUDIT[2][1]} to {AUDIT[2][4]}, the builder's from {AUDIT[1][1]} to {AUDIT[1][4]}, the beginner's from {AUDIT[0][1]} to {AUDIT[0][4]}.</h2>
  <figure>
    <div class="key"><span>First and second audits</span><span class="k1">Third</span><span class="k2">Fourth</span></div>
    <div class="chart" role="list" aria-label="Newcomer scores out of 100, four audits">
{bars([(n, a, b, c, d) for n, a, b, c, d in AUDIT])}
    </div>
    <figcaption>Unit: "would this be useful to me today", out of 100. Each audit was one fresh Claude session that read the whole project as three people and ran the builder's commands in an empty repository. The first two counted the links that do not work until the merge; the third and fourth were asked to score as if merged, so the first two are not like for like with the last two. Problems found (blocking, confusing, minor): {", then ".join(f"{x[0]}, {x[1]}, {x[2]}" for x in AUDIT_FOUND)}.</figcaption>
  </figure>
  <p class="so"><b>So what.</b> Each audit found new faults, some of them introduced by the previous round's fixes: a heading bug in the second, and in the third a check that a finished project could never pass. Both are fixed, and a gate now fills a new project and expects every check to pass, so that class of fault cannot return unnoticed. The fourth audit confirmed the builder's path recovered; its one blocking point, a copy command, is fixed and not audited again.</p>
</section>

<section aria-labelledby="f2"><p class="lab">Finding 2</p><h2 id="f2">{['None','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten'][at80]} of ten measures reach 80 or more; real use stays at {RUBRIC[-1][2]}.</h2>
  <figure>
    <div class="key"><span>This morning's review</span><span class="k2">Now</span></div>
    <div class="chart" role="list" aria-label="End-user rubric, out of 100, this morning and now">
{bars([(m, a, b) for m, a, b, ev in RUBRIC])}
    </div>
    <figcaption>Unit: score out of 100, scored by the author from the user's side, with evidence for each. Source: the review written this morning, and the tests run since. The table below gives the evidence.</figcaption>
  </figure>
  <details><summary>The rubric as a table, with the evidence</summary>
    <div class="tw" tabindex="0" role="region" aria-label="The rubric with evidence"><table><thead><tr><th scope="col">Measure</th><th scope="col">Morning</th><th scope="col">Now</th><th scope="col">Evidence now</th></tr></thead><tbody>{rub_rows}</tbody></table></div>
  </details>
  <p class="so"><b>So what.</b> The largest gain is that the files now agree: every page that repeats the steps is written from one source, and a gate fails if one drifts. The builder's path gained most in substance: one folder, any repository, and an independent session filled a project by hand and saw every check pass. The last measure cannot move from here: it needs people.</p>
</section>

<section aria-labelledby="f3"><p class="lab">Finding 3</p><h2 id="f3">On GitHub the repository shows none of the signals a visitor looks for, and the ones it could show are mostly vanity.</h2>
  <p>Read from the GitHub API on 16 November 2026. Traffic (views and clones) needs the owner's own access and could not be read here.</p>
  <div class="tw" tabindex="0" role="region" aria-label="GitHub measures"><table>
    <thead><tr><th scope="col">Measure</th><th scope="col">Now</th><th scope="col">Kind</th><th scope="col">What to do</th></tr></thead>
    <tbody>
      <tr><th scope="row">Stars</th><td>{gh["stars"]}</td><td><span class="tag">Vanity</span></td><td>Ask, do not chase. A star is one click and is sold in bulk; it shows interest, not use</td></tr>
      <tr><th scope="row">Forks and watchers</th><td>{gh["forks"]} and {gh["watchers"]}</td><td><span class="tag">Vanity</span></td><td>A fork with new commits is a real signal. An empty fork is not</td></tr>
      <tr class="weak"><th scope="row">Topics</th><td>{gh["topics"]}</td><td><span class="tag">Findability</span></td><td>Add up to 20, such as ai, ai-agents, agentic-ai, prompt-engineering, llm, chatgpt, claude, ai-education, small-business, workflow-automation</td></tr>
      <tr class="weak"><th scope="row">Description</th><td>"{E(gh["description"])}"</td><td><span class="tag">Findability</span></td><td>Name the two tools: "Free AI tools you can use today: Artifact Studio turns answers into pages and decks; Agentic Process takes an idea to a tested tool."</td></tr>
      <tr class="weak"><th scope="row">Website and Pages</th><td>{gh["homepage"]}, Pages {gh["pages"]}</td><td><span class="tag real">Real</span></td><td>Turn on GitHub Pages. Every HTML file then opens as a page, on a phone, without an outside service</td></tr>
      <tr class="weak"><th scope="row">Social preview</th><td>none</td><td><span class="tag">Findability</span></td><td>Upload a 1280 by 640 picture, such as the nine steps, so a shared link shows it</td></tr>
      <tr><th scope="row">Releases</th><td>{gh["releases"]}</td><td><span class="tag">Findability</span></td><td>After the merge, tag v0.1 with a short note of what works and what is untested</td></tr>
      <tr class="weak"><th scope="row">Community profile</th><td>{gh["community_profile"]}%</td><td><span class="tag">Findability</span></td><td>Has a README and a licence. Add CONTRIBUTING, a code of conduct and issue templates</td></tr>
      <tr><th scope="row">Issues from people who tried it</th><td>none yet</td><td><span class="tag real">Real</span></td><td>Add an issue template, "I tried it", asking what they made, which chatbot, and where they got stuck. This turns visits into the evidence the rubric lacks</td></tr>
      <tr><th scope="row">Discussions</th><td>{gh["discussions"]}</td><td><span class="tag real">Real</span></td><td>Turn on for learners after the first class, so questions are public and answered once</td></tr>
    </tbody></table></div>
  <p class="so"><b>So what.</b> Topics, a description, a social picture and Pages take the owner about 30 minutes and make the work findable. They do not prove value. The measure that matters, people who used it, needs a way to report back: the "I tried it" template.</p>
</section>

<section aria-labelledby="m"><p class="lab">How it was measured</p><h2 id="m">Every test was an AI session that had only the project's own files; the rubric is the author's.</h2>
  <div class="tw" tabindex="0" role="region" aria-label="What ran"><table><thead><tr><th scope="col">Test</th><th scope="col">Runs</th></tr></thead><tbody>{''.join(f'<tr><th scope="row">{E(n)}</th><td>{c}</td></tr>' for n, c in TESTS)}</tbody></table></div>
  <p style="margin-top:14px">Each run logged every place it had to guess, marked blocking or minor. The logs are kept unedited in <code>projects/agentic-process/level-3-files/test-runs/</code>. The pages were checked in Chrome at phone and laptop width with an automated accessibility scan, with scripts off, and the presenter window was driven from a second window.</p>
</section>

<section aria-labelledby="l"><p class="lab">What it does not show</p><h2 id="l">It does not show that a person can use it, or that it works outside Claude.</h2>
  <p>Every session was Claude. Nobody has run the coach in ChatGPT, Gemini or Copilot. No learner has been timed, so every time in the project is an estimate. The rubric is the author's own. The newcomer audits were independent sessions, but they are still AI reading files, not people deciding whether to come back.</p>
</section>

<section aria-labelledby="n"><p class="lab">Next steps</p><h2 id="n">Three things move the last measure, and only the owner can do them.</h2>
  <ol class="next">
    <li><b>Owner, before the merge:</b> run the "Try it" prompt in ChatGPT and Gemini, and note where each stops.</li>
    <li><b>Owner, after the merge:</b> turn on GitHub Pages, add topics, a description and the social picture (about 30 minutes).</li>
    <li><b>Owner, at the next class:</b> teach the 30-minute training once, time each part, and ask each learner to file "I tried it".</li>
    <li><b>Assistant, next session:</b> build Document to action brief with this process from step 1, and time each step.</li>
  </ol>
</section>
</main>
<footer><div class="wrap">
  <p>Made with Artifact Studio's instructions: one-page report, analyst voice, the Practical AI colours. Numbers come from the test logs and the GitHub API, read on 16 November 2026. The vanity and findability notes draw on GitHub's own documentation for topics and social previews, and on published research into purchased stars.</p>
  <p style="margin-top:10px"><b>Bradley Ross</b> is an agentic AI architect and developer for businesses of every size, from start-up to enterprise. <a href="https://www.linkedin.com/in/bradaross/">Connect on LinkedIn</a></p>
</div></footer>
</body>
</html>
'''


if __name__ == "__main__":
    out = HERE / "2026-11-16-agentic-process-report.html"
    out.write_text(page(), encoding="utf-8"); print(f"{out.name}: {out.stat().st_size // 1024} KB")
