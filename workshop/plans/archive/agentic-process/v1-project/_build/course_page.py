"""Writes base/course.html for build.py: how to use Agentic Process, as a visual guide and short course.

The nine steps are a scrollyteller: a diagram stays at the top and walks with you, step by step. Content comes from
course.py and steps.py. Look: the Practical AI colours, the same as the guide and the North Star page.
"""
import pathlib
from steps import STEPS, coach_prompt, TOTAL_MINUTES
from pages import E, md, BASE_CSS, creator, diagram, NORTH_STAR
from course import COURSE, WHY, PATHS, LADDER, GATES, FIRST, CHECKS, NOTES, G, FORM

HERE = pathlib.Path(__file__).resolve().parent
STAGE = {1: "Decide", 2: "Decide", 3: "Decide", 4: "Decide", 5: "Design", 6: "Design", 7: "Design", 8: "Build and test", 9: "Grow"}
SPLIT = {'Reuse check': ('Reuse', 'check'), 'Outside help': ('Outside', 'help'), 'Simplest design': ('Simplest', 'design'),
         'Plan and front door': ('Plan and', 'front door'), 'Build and test': ('Build and', 'test')}
X0, DX = 70, 95


def track_svg():
    """The scrolling diagram: nine steps, a gate after each, a marker that walks to the step you are reading, and a time bar."""
    out = ['<svg viewBox="0 0 900 250" class="track" role="img" aria-labelledby="trk-t" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif">',
           '<title id="trk-t">The nine steps in four stages, with a gate after each. The marker shows the step you are reading.</title>',
           '<rect width="900" height="250" rx="18" fill="#0c2340"/>']
    for name, a, b in [('Decide', 1, 4), ('Design', 5, 7), ('Test', 8, 8), ('Grow', 9, 9)]:
        xa, xb = X0 + (a - 1) * DX - 34, X0 + (b - 1) * DX + 34
        out.append(f'<rect x="{xa}" y="20" width="{xb - xa}" height="30" rx="15" fill="#17365f"/><text x="{(xa + xb) / 2}" y="41" fill="#ffd23f" font-size="16" font-weight="700" text-anchor="middle">{name}</text>')
    out.append(f'<path class="rail" d="M{X0},112 H{X0 + 8 * DX + 36}" stroke="#2f5a8f" stroke-width="4"/>')
    for st in STEPS:
        i, cx = st['n'] - 1, X0 + (st['n'] - 1) * DX
        l1, l2 = SPLIT.get(st['name'], (st['name'], ''))
        out.append(f'<g class="nd" data-n="{st["n"]}"><circle cx="{cx}" cy="112" r="24"/><text x="{cx}" y="119" font-size="20" font-weight="800" text-anchor="middle">{st["n"]}</text>'
                   f'<text class="lbl" x="{cx}" y="166" font-size="15" text-anchor="middle">{E(l1)}</text>' + (f'<text class="lbl" x="{cx}" y="184" font-size="15" text-anchor="middle">{E(l2)}</text>' if l2 else '') + '</g>')
        out.append(f'<rect class="gt" data-n="{st["n"]}" x="{cx + 36 - 7}" y="105" width="14" height="14" transform="rotate(45 {cx + 36} 112)"/>')
    out.append(f'<g class="mk"><circle cx="{X0}" cy="72" r="9" fill="#fff"/><path d="M{X0 - 6},82 L{X0},92 L{X0 + 6},82 Z" fill="#fff"/></g>')
    out.append('<rect x="70" y="212" width="760" height="10" rx="5" fill="#17365f"/><rect class="tb" x="70" y="212" width="0" height="10" rx="5" fill="#ffd23f"/>')
    out.append('<text class="tt" x="70" y="204" font-size="15" fill="#d5e2f5">Time, steps 1 to 8: about 60 minutes in all (an estimate)</text></svg>')
    return ''.join(out)


def bars(title, rows, top, unit, note):
    """A small single-series bar chart, labelled directly; each bar has a tooltip."""
    w, h, pad, bw = 420, 230, 46, 56
    gap = (w - 2 * pad - len(rows) * bw) / max(1, len(rows) - 1)
    out = [f'<svg viewBox="0 0 {w} {h}" class="chart" role="img" aria-label="{E(title)}: ' + E(', '.join(f"{a} {v:g}" for a, v in rows)) + '" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif">',
           f'<line x1="{pad - 10}" y1="{h - 40}" x2="{w - pad + 10}" y2="{h - 40}" stroke="#c9d1de" stroke-width="1"/>']
    for i, (lab, v) in enumerate(rows):
        x, bh = pad + i * (bw + gap), (h - 80) * v / top
        y = h - 40 - bh
        out.append(f'<g class="bar"><title>{E(lab)}: {v:g} {E(unit)}</title><path d="M{x},{h - 40} V{y + 4} q0,-4 4,-4 h{bw - 8} q4,0 4,4 V{h - 40} Z" fill="#17365f"/>'
                   f'<text x="{x + bw / 2}" y="{y - 8}" text-anchor="middle" font-size="17" font-weight="700" fill="#14202e">{v:g}</text>'
                   f'<text x="{x + bw / 2}" y="{h - 18}" text-anchor="middle" font-size="14" fill="#48546a">{E(lab)}</text></g>')
    out.append('</svg>')
    return f'<figure class="fig"><figcaption><b>{E(title)}</b></figcaption>{"".join(out)}<p class="small">{E(note)}</p></figure>'


def check(n):
    qs = []
    for qi, (q, opts, right, why) in enumerate(CHECKS[n]):
        r = (n + qi) % len(opts)
        order = list(range(len(opts))); order.remove(right); order.insert(r, right)
        opts, right = [opts[k] for k in order], r
        o = ''.join(f'<label><input type="radio" name="q{n}-{qi}" value="{i}"> {E(t)}</label>' for i, t in enumerate(opts))
        qs.append(f'<fieldset class="qz" data-right="{right}"><legend>{E(q)}</legend>{o}<button class="btn sm ghost" type="button" data-check>Check</button>'
                  f'<p class="fb" aria-live="polite"></p><details class="ans"><summary>Show the answer</summary><p>{E(opts[right])}. {E(why)}</p></details></fieldset>')
    return f'<div class="checks"><h3>Check yourself</h3>{"".join(qs)}</div>'


def notes(n):
    return f'<details class="nts"><summary>Notes for presenting this chapter</summary><p>{E(NOTES[n])}</p></details>'


def head(n, title, goal, mins):
    return (f'<header class="ch scene" id="ch{n}"><p class="chn">Chapter {n} of 5</p><h2 tabindex="-1">{E(title)}</h2>'
            f'<p class="goal">{E(goal)}</p><p class="mins">About {mins} minutes</p></header>')


def code(id_, text, label="Copy"):
    return f'<div class="code"><pre id="{id_}" tabindex="0">{E(text)}</pre><button class="btn sm" type="button" data-copy="{id_}">{E(label)}</button></div>'


def step_scene(st):
    cum = sum(s['minutes'] for s in STEPS if s['n'] <= st['n'])
    t = (f"About {st['minutes']} minutes. Running total: about {cum} of {TOTAL_MINUTES} (estimates)." if st['minutes']
         else "Repeats after the tool is in use: one addition at a time, each a change you can review in five minutes.")
    proof = ''.join(f'<li>{md(p)}</li>' for p in st['proof'])
    return (f'<article class="scene st" id="s{st["n"]}" data-step="{st["n"]}" data-cum="{cum}">'
            f'<p class="stage s{st["n"]}">{E(STAGE[st["n"]])}</p><p class="big">{st["n"]}</p><h3>{E(st["name"])}</h3><p class="gist">{E(st["gist"])}</p>'
            f'<dl><div><dt>Why it exists</dt><dd>{md(st["purpose"])}</dd></div><div><dt>What you write</dt><dd>{md(st["writes"])}</dd></div>'
            f'<div><dt>Time</dt><dd>{E(t)}</dd></div><div><dt>Done when</dt><dd><ul>{proof}</ul></dd></div></dl>'
            f'<p class="gate"><b>The gate.</b> {E(st["gate"])}</p></article>')


def flow(items, label, status):
    li = ''.join(f'<li style="--i:{i}"><b>{E(a)}</b><span>{E(b)}</span></li>' for i, (a, b) in enumerate(items))
    return f'<figure class="flow anim" aria-label="{E(label)}"><figcaption><b>{E(label)}</b> <span class="chip {"ok" if status.startswith("Tested") else "no"}">{E(status)}</span></figcaption><ol>{li}</ol></figure>'


def gates_svg():
    rows = ''
    for i, (name, what, at) in enumerate(GATES):
        y = 34 + i * 44
        rows += (f'<g class="gr" style="--at:{at}"><circle class="lt" cx="40" cy="{y}" r="11"/><text x="64" y="{y + 6}" font-size="18" font-weight="700" fill="#14202e">{name}</text>'
                 f'<text x="150" y="{y + 6}" font-size="16" fill="#48546a">{E(what)}</text><text x="660" y="{y + 6}" font-size="15" fill="#48546a" text-anchor="end">passes from step {at}</text></g>')
    return (f'<figure class="fig anim gates"><figcaption><b>The four gates in every new project, and when each one turns green</b></figcaption>'
            f'<svg viewBox="0 0 680 190" role="img" aria-label="Four gates: layout and links pass from step 5, filled from step 6, built from step 8" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif">'
            f'{rows}</svg>'
            f'<button class="btn sm ghost" type="button" data-replay>Play again</button></figure>')


def course_html(me, puppy, north_url, guide_url):
    ns_svg = (HERE / 'img/nine-steps.svg').read_text(encoding='utf-8').replace('<svg ', '<svg class="hero-svg" ', 1).replace('id="t"', 'id="ns-t"').replace('id="d"', 'id="ns-d"').replace('aria-labelledby="t d"', 'aria-labelledby="ns-t ns-d"')
    mist = ''.join(f'<div class="card"><b>{E(a)}</b><p>{E(b)}</p><p class="caught">Caught at step {n}</p></div>' for a, b, n in WHY['mistakes'])
    get = ''.join(f'<div class="card"><b>{E(a)}</b><p>{E(b)}</p></div>' for a, b in WHY['get'])
    ch1 = (head(1, "What it is, and why it exists", "See the problem this project solves, what you get from it, and what has been measured so far.", 6) +
      f'''<section class="scene body"><div class="analogy"><div><p class="lab">Think of it as</p><p class="big2">A building site with an inspector.</p>
  <p>You agree the drawing before you pour concrete, and nothing moves to the next stage until the current one is signed off. Here the stages are nine steps, the sign-off is a plain question called a gate, and the inspector at the end is an AI chat that has never seen your work.</p></div>
  <img src="data:image/jpeg;base64,{puppy}" alt="A puppy in a plaid suit and tie, sitting upright and looking serious: the inspector." width="260" height="260"></div></section>
<section class="scene body"><h3>The North Star</h3><p class="star">{E(NORTH_STAR)}</p>
  <h3>Three mistakes it stops</h3><div class="cards">{mist}</div></section>
<section class="scene body"><h3>What you leave with</h3><div class="cards">{get}</div>
  <h3>What has been measured</h3><p>Every test so far gave a fresh AI session only this project's files and one request, and counted the points that tripped it. They are AI sessions in Claude, not people, and nobody has been timed.</p>
  <div class="charts">{bars("Blocking points per coach test run, average of two runs", WHY["coach"], 5, "blocking points", "A blocking point is one where a different guess would change the result. Each round fixed the last round's points.")}
  {bars("Newcomer audit score out of 100, average of a beginner, a builder and a teacher", WHY["audits"], 100, "out of 100", "Fresh sessions read the whole project in each role after each round of fixes. The third and fourth were scored as if merged.")}</div></section>''' + check(1) + notes(1))
    scenes = ''.join(step_scene(st) for st in STEPS)
    ch2 = (head(2, "The nine steps, and why each one exists", "Scroll. The diagram stays at the top and walks with you: the stage, the gate, and the time so far.", 10) +
      f'''<div class="scrolly"><div class="sticky" aria-hidden="false">{track_svg()}<p class="now" aria-live="polite">Scroll to walk the nine steps.</p></div>
<div class="scenes"><article class="scene st intro" data-step="0" data-cum="0"><p class="big">9</p><h3>Nine steps, four stages, a gate after each</h3>
  <p><b>Decide</b> (steps 1 to 4): is it worth building at all? <b>Design</b> (5 to 7): the plan, before anything exists. <b>Build and test</b> (8): a stranger tests it. <b>Grow</b> (9): one addition at a time.</p>
  <p>A gate is a question worded so that yes means go on. No means fix the step. Stopping at step 2, because something already does the job, counts as a win.</p></article>
{scenes}
<article class="scene st outro" data-step="9" data-cum="{TOTAL_MINUTES}"><h3>That is the whole process</h3><p>About {TOTAL_MINUTES} minutes for steps 1 to 8 on a small job: an estimate. The short path, for one person turning one input into one result in a chat, uses seven of the plan's headings and skips nothing that matters.</p>
  <p>The same nine steps run at every level. What changes is who runs them and what checks them: chapters 3 and 4.</p></article></div></div>''' + check(2) + notes(2))
    pth = ''
    for P in PATHS:
        lane = ''.join(f'<i class="{"on" if n >= P["start"] else "pre" if P["start"] > 1 else ""}" title="Step {n}">{n}</i>' for n in range(1, 10))
        steps = ''
        for k, (txt, c) in enumerate(P['steps']):
            body = code(f'p-{P["key"]}-{k}', coach_prompt("[one job you do on your own, in one sentence]"), "Copy the coach prompt") if c == "COACH" else (code(f'p-{P["key"]}-{k}', c) if c else '')
            steps += f'<li><p>{E(txt)}</p>{body}</li>'
        legend = '<p class="small">Filled: the steps this path runs. Outlined: steps 1 to 6, checked against your spec instead of asked.</p>' if P['start'] > 1 else ''
        pth += (f'<article class="path scene" id="path-{P["key"]}"><p class="lvl">{E(P["level"])}</p><h3>{E(P["title"])}</h3><p class="needs">{E(P["needs"])}</p>'
                f'<div class="lane" aria-label="Starts at step {P["start"]}">{lane}</div>{legend}<ol class="howto">{steps}</ol>'
                f'<p class="chip {"ok" if P["status"].startswith("Tested") else "no"}">{E(P["status"])}</p></article>')
    ch3 = (head(3, "Run it: three ways in", "Pick the path that fits you and follow it step by step. Each one runs the same nine steps.", 5) +
           f'<div class="paths">{pth}</div>' + check(3) + notes(3))
    lad = ''.join(f'<tr><th scope="row">{E(a)}</th><td>{E(b)}</td><td>{E(c)}</td><td><span class="chip {"ok" if d.startswith("Tested") else "no"}">{E(d)}</span></td></tr>' for a, b, c, d in LADDER)
    ch4 = (head(4, "Automation and the advanced levels", "See what checks the work at each level, what can run without you, and what has actually been tried.", 4) +
      f'''<section class="scene body">{gates_svg()}<p>Run them all with one command at any time. A gate that cannot be answered without a person is open, not failed.</p>
  <figure class="fig"><figcaption><b>The fresh-run test: how step 8 works at every level</b></figcaption>{diagram("test")}</figure></section>
<section class="scene body">{flow([("Agent", "steps 1 to 6"), ("Agent", "prepares the tests"), ("Fresh sessions", "run each test"), ("Agent", "fixes, runs the gates again"), ("A person", "reads the hand-back and decides")], "An unattended run", "Tested: one run, in an empty repository")}
{flow([("A spec", "in workshop/plans or drafts"), ("A scheduler", "a routine, a scheduled task or an assigned issue"), ("The skill", "checks steps 1 to 6, runs 7 and 8"), ("The gates", "all pass"), ("A draft pull request", "with the four-heading note"), ("A person", "merges")], "From a spec to a pull request on a schedule", "Planned, not built")}</section>
<section class="scene body"><h3>The levels</h3><div class="tw" tabindex="0" role="region" aria-label="The levels"><table><thead><tr><th scope="col">Level</th><th scope="col">Who runs it</th><th scope="col">What checks it</th><th scope="col">Status</th></tr></thead><tbody>{lad}</tbody></table></div>
  <p class="rule">At every level, a person approves anything that is merged, posted, sent, paid or published.</p></section>''' + check(4) + notes(4))
    first = ''.join(f'<li><label><input type="checkbox"> {E(f)}</label></li>' for f in FIRST)
    ch5 = (head(5, "Your first tool", "Take one real job through the steps, and tell us how it went.", 0).replace('<p class="mins">About 0 minutes</p>', f'<p class="mins">About {COURSE["run"]} minutes, an estimate</p>') +
      f'''<section class="scene body"><ul class="first">{first}</ul>
  <p>If your reuse check finds something that already does the whole job, that is a finished result: write the two-line guide and pick a second job.</p>
  <p><a class="btn" href="{FORM}">Built one? Tell us in two minutes</a></p>
  <p class="small">The form records three numbers: whether a fresh chat finished the job, the minutes to a one-page plan, and whether someone else has used the tool.</p></section>''' + notes(5))
    teach = f'''<section class="scene body" id="teach"><h2 tabindex="-1">Presenting it</h2>
  <p>Press <b>Present</b>: the page goes full screen and the arrow keys, Page Down or the space bar move one scene at a time. Chapters 1 to 4 take about 45 minutes; then the lab is chapter 3's paths, about 60 minutes. Each chapter has its notes in a fold at the end. Esc leaves.</p>
  <p>Printing gives every chapter with its notes open.</p></section>'''
    nav = ''.join(f'<a href="#ch{n}">{n}<span> {E(t)}</span></a>' for n, t in [(1, "Why"), (2, "The steps"), (3, "Run it"), (4, "Automation"), (5, "Your tool")])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(COURSE["title"])}: {E(COURSE["subtitle"])}</title>
<!-- Written by projects/agentic-process/_build/build.py (course_page.py) from _build/course.py and _build/steps.py. Change the sources, not this file. -->
<style>{BASE_CSS}{CSS}</style>
</head>
<body>
<div class="bar" aria-hidden="true"><i id="prog"></i></div>
<nav class="top" aria-label="Chapters"><a class="home" href="#top">Agentic Process</a>{nav}<button class="btn sm" type="button" id="present">Present</button></nav>
<header class="hero scene" id="top"><div class="wrap">
  <p class="kick">{E(COURSE["subtitle"])}</p><h1>{E(COURSE["title"])}</h1><p class="sub">{E(COURSE["purpose"])}</p>
  <p class="facts"><span>About {COURSE["read"]} minutes to read</span><span>About {COURSE["run"]} minutes for your first run</span><span>Both estimates</span></p>
  {ns_svg}
  <p class="who">{E(COURSE["who"])}</p>
</div></header>
<main class="wrap">
{ch1}
{ch2}
{ch3}
{ch4}
{ch5}
{teach}
<p class="honest">{E(COURSE["honest"])} Also: <a href="{north_url}">the North Star page</a>, <a href="{guide_url}">the guide</a>, and <a href="{G}base/PROCESS.md">the nine steps with every prompt</a>.</p>
</main>
<footer class="wrap">{creator(me)}</footer>
<script>{JS}</script>
</body>
</html>
"""


CSS = """
.bar{position:fixed;top:0;left:0;right:0;height:4px;z-index:20}.bar i{display:block;height:100%;width:0;background:var(--hl)}
.top{position:sticky;top:0;z-index:15;display:flex;gap:4px;align-items:center;flex-wrap:wrap;padding:8px 14px;background:var(--navy)}
.top a{color:#fff;text-decoration:none;min-height:40px;display:inline-flex;align-items:center;padding:0 10px;border-radius:8px;font-weight:700}
.top a span{font-weight:400;margin-left:.35em}.top a.home{color:var(--hl);margin-right:auto}.top a:hover,.top a[aria-current]{background:var(--navy2)}
.top .btn{min-height:40px;margin:0;background:var(--hl);color:var(--navy)}
@media(max-width:720px){.top a span{display:none}.top a{padding:0 8px}}@media(max-width:520px){.top a.home{display:none}.top{justify-content:space-between}.top .btn{padding:0 12px}}
.wrap{max-width:980px;margin-inline:auto;padding-inline:18px}
.hero{background:var(--navy);color:#fff;padding:40px 0 36px}.kick{color:var(--hl);font-weight:700}
.hero h1{font-size:clamp(2rem,6vw,3.3rem);margin-top:8px}.sub{margin-top:14px;font-size:1.2rem;max-width:36em;color:#dfe6ef}
.facts{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}.facts span{background:var(--navy2);border-radius:999px;padding:6px 12px;font-size:.95rem}
.hero-svg{display:block;width:100%;height:auto;margin-top:22px;border-radius:18px}.who{margin-top:14px;color:#c9d6e6;max-width:44em}
.scene{scroll-margin-top:60px}.ch{padding:64px 0 10px}.chn{color:var(--blue);font-weight:700}.ch h2{font-size:clamp(1.7rem,4.6vw,2.5rem);margin-top:4px}
.ch h2:focus{outline:none}.goal{margin-top:10px;font-size:1.15rem;max-width:40em}.mins{color:var(--muted);margin-top:4px}
.body{margin-top:18px}.body h3,.checks h3{font-size:1.3rem;margin:26px 0 10px}.body>p{max-width:44em;margin-top:10px}
.analogy{display:grid;gap:18px;align-items:center;background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:20px}
@media(min-width:760px){.analogy{grid-template-columns:1fr 260px}}.analogy img{width:100%;max-width:260px;height:auto;border-radius:14px;justify-self:center}
.lab{color:var(--blue);font-weight:700;font-size:.92rem}.big2{font:800 clamp(1.4rem,4vw,2rem)/1.2 var(--sans);margin:6px 0 10px}
.star{font:700 clamp(1.15rem,3.2vw,1.45rem)/1.4 var(--sans);background:var(--navy);color:#fff;border-radius:14px;padding:18px 20px;max-width:40em}
.cards{display:grid;gap:12px}@media(min-width:760px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px}.card b{font-size:1.1rem}.card p{margin-top:6px}
.caught{color:var(--blue);font-weight:700;font-size:.92rem}
.charts{display:grid;gap:14px;margin-top:10px}@media(min-width:820px){.charts{grid-template-columns:1fr 1fr}}
.fig{margin:14px 0 0;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px}.fig figcaption{margin-bottom:8px}
.fig svg{display:block;width:100%;height:auto}.small{font-size:.9rem;color:var(--muted);margin-top:8px;max-width:44em}
/* the scrollyteller */
.scrolly{position:relative;margin-top:14px}
.sticky{position:sticky;top:56px;z-index:5;background:var(--bg);padding:8px 0}
.track{display:block;width:100%;height:auto;max-height:34vh}
.track .nd circle{fill:#1d4273;stroke:#5d86c0;stroke-width:3;transition:fill .4s,stroke .4s,transform .4s;transform-box:fill-box;transform-origin:center}
.track .nd text{fill:#fff}.track .nd .lbl{fill:#d5e2f5}
.track .nd.past circle{fill:#2f6fb5;stroke:#2f6fb5}.track .nd.cur circle{fill:#ffd23f;stroke:#ffd23f;transform:scale(1.18)}.track .nd.cur text{fill:#0c2340;font-weight:800}.track .nd.cur .lbl{fill:#ffd23f}
.track .gt{fill:#5d86c0;transition:fill .4s}.track .gt.past{fill:#ffd23f}
.track .mk{transition:transform .6s cubic-bezier(.3,.7,.3,1)}.track .tb{transition:width .6s}
@media(max-width:600px){.track .lbl,.track .tt{display:none}}
.now{font-weight:700;margin-top:6px;min-height:1.5em}
.scenes{display:grid;gap:22px;padding:20px 0 30px}
.st{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:22px 20px;min-height:58vh;display:flex;flex-direction:column;justify-content:center;gap:8px}
.st .big{font:900 4rem/1 var(--sans);color:var(--pale);margin:0}.st h3{font-size:clamp(1.5rem,4vw,2.1rem)}.st .gist{font-size:1.15rem;color:var(--muted)}
.stage{align-self:flex-start;font-weight:700;font-size:.9rem;padding:4px 10px;border-radius:999px;background:var(--navy);color:#fff}
.st dl{display:grid;gap:12px;margin:10px 0 0}@media(min-width:760px){.st dl{grid-template-columns:1fr 1fr}}
.st dt{font-weight:700;color:var(--blue);font-size:.92rem}.st dd{margin:4px 0 0}.st dd ul{padding-left:1.1em}
.gate{margin-top:8px;padding:12px 14px;border-left:5px solid var(--hl);background:#fff7d6;border-radius:0 10px 10px 0}
.st.intro,.st.outro{background:var(--navy);color:#fff;border:0}.st.intro .big{color:var(--hl)}.st.intro p,.st.outro p{max-width:40em}
/* the paths */
.paths{display:grid;gap:16px;margin-top:18px}
.path{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:20px}
.lvl{display:inline-block;background:var(--navy);color:#fff;border-radius:6px;padding:3px 8px;font-size:.85rem;font-weight:700}
.path h3{font-size:1.5rem;margin-top:8px}.needs{color:var(--muted);margin-top:4px}
.lane{display:flex;flex-wrap:wrap;gap:4px;margin-top:12px}.lane i{font-style:normal;width:30px;height:30px;display:grid;place-items:center;border-radius:8px;background:var(--pale);color:var(--muted);font-weight:700;font-size:.9rem}
.lane i.on{background:var(--navy);color:#fff}.lane i.pre{background:#fff;border:2px dashed var(--blue);color:var(--blue)}
.howto{margin-top:14px;padding-left:1.3em}.howto li{margin-top:12px}.howto li::marker{font-weight:800;color:var(--blue)}
.code{margin-top:8px}.code pre{font-size:.88rem}.btn.sm{min-height:44px;margin-top:8px;font-size:.95rem}
.chip{display:inline-block;margin-top:12px;padding:6px 12px;border-radius:999px;font-size:.9rem;font-weight:700}
.chip.ok{background:#e3f1e8;color:#1d6b3a}.chip.no{background:#fdeee0;color:#8a4a12}
/* automation */
.gates .lt{fill:#c9d1de}
.gates.play .lt{animation:lit .3s forwards;animation-delay:calc((var(--at) - 1) * .75s)}
@keyframes lit{to{fill:#1d6b3a}}
.flow{margin:16px 0 0;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px}
.flow ol{list-style:none;padding:0;margin:12px 0 0;display:flex;flex-wrap:wrap;gap:10px}
.flow li{flex:1 1 130px;background:var(--navy);color:#fff;border-radius:12px;padding:12px;display:grid;gap:4px;position:relative}
.flow li:last-child{background:var(--hl);color:var(--navy)}.flow li span{font-size:.92rem;opacity:.9}
.js .flow.anim li{opacity:0;transform:translateY(8px)}
.js .flow.anim.play li{animation:in .5s forwards;animation-delay:calc(var(--i) * .45s)}
@keyframes in{to{opacity:1;transform:none}}
.tw{overflow-x:auto;margin-top:10px}table{border-collapse:collapse;width:100%;min-width:640px;background:var(--panel)}
th,td{text-align:left;vertical-align:top;padding:10px;border-bottom:1px solid var(--line)}thead th{font-size:.86rem;color:var(--muted)}
.rule{margin-top:14px;font-weight:700}
.first{list-style:none;padding:0;display:grid;gap:8px}.first label{display:flex;gap:10px;min-height:44px;align-items:flex-start;padding:10px 12px;background:var(--panel);border:1px solid var(--line);border-radius:10px}
.first input{width:20px;height:20px;flex:none;margin-top:2px}
/* checks and notes */
.qz{border:1px solid var(--line);border-radius:12px;padding:14px;margin:12px 0 0;background:var(--panel)}.qz legend{font-weight:700;padding:0 6px}
.qz label{display:flex;gap:10px;align-items:center;min-height:44px;padding:4px 8px;border-radius:8px;cursor:pointer}.qz input{width:20px;height:20px;flex:none}
.fb{margin-top:8px;font-weight:700}.fb.ok{color:#1d6b3a}.fb.no{color:#9b2c1f}.js .ans{display:none}.ans summary{min-height:44px;display:flex;align-items:center;cursor:pointer}
.nts{margin-top:16px;border:1px dashed var(--line);border-radius:12px;padding:0 14px}.nts summary{min-height:48px;display:flex;align-items:center;cursor:pointer;color:var(--muted);font-weight:700}.nts p{padding-bottom:14px}
#teach h2{font-size:1.6rem;margin-top:50px}#teach h2:focus{outline:none}.honest{margin:40px 0 0;color:var(--muted)}
footer{padding:30px 18px 50px}
/* present mode: one scene a screen */
html.present .scene{min-height:100vh;scroll-margin-top:0}html.present .ch{display:flex;flex-direction:column;justify-content:center}
html.present .top{opacity:.15}html.present .top:hover,html.present .top:focus-within{opacity:1}
@media (prefers-reduced-motion:reduce){.js .flow.anim li{opacity:1;transform:none;animation:none!important}.gates .lt{fill:#1d6b3a}}
@media print{.top,.bar,.sticky,[data-copy],[data-check],[data-replay],#present{display:none!important}.st{min-height:0;break-inside:avoid}.nts{display:block}.js .flow.anim li{opacity:1;transform:none}.hero{background:#fff;color:#000}}
"""

JS = """
(()=>{document.documentElement.classList.add('js');
const prog=document.getElementById('prog');addEventListener('scroll',()=>{const h=document.documentElement;prog.style.width=(100*h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight))+'%'},{passive:true});
/* the scrolling diagram */
const steps=[...document.querySelectorAll('.st[data-step]')],nodes=[...document.querySelectorAll('.track .nd')],gts=[...document.querySelectorAll('.track .gt')],
 mk=document.querySelector('.track .mk'),tb=document.querySelector('.track .tb'),tt=document.querySelector('.track .tt'),now=document.querySelector('.now');
const X0=70,DX=95,TOTAL=60;
function set(el){const n=+el.dataset.step,cum=+el.dataset.cum;
 nodes.forEach(g=>{const k=+g.dataset.n;g.classList.toggle('cur',k===n);g.classList.toggle('past',k<n)});
 gts.forEach(g=>g.classList.toggle('past',+g.dataset.n<n));
 mk.style.transform='translate('+(n?(n-1)*DX:0)+'px,0)';tb.setAttribute('width',760*Math.min(cum,TOTAL)/TOTAL);
 const h=el.querySelector('h3');tt.textContent='Time so far: about '+cum+' of '+TOTAL+' minutes (an estimate)';
 now.textContent=(n&&!el.classList.contains('outro')?'Step '+n+' of 9: '+h.textContent:h.textContent)+(cum?' · about '+cum+' of '+TOTAL+' min so far':'')}
if('IntersectionObserver' in window){const io=new IntersectionObserver(es=>{for(const e of es)if(e.isIntersecting)set(e.target)},{rootMargin:'-45% 0px -50% 0px'});steps.forEach(s=>io.observe(s));
 const play=new IntersectionObserver(es=>{for(const e of es)if(e.isIntersecting){e.target.classList.add('play');play.unobserve(e.target)}},{threshold:.4});document.querySelectorAll('.anim').forEach(a=>play.observe(a));
 const chs=[...document.querySelectorAll('.ch')],navs=[...document.querySelectorAll('.top a[href^="#ch"]')];
 const cio=new IntersectionObserver(es=>{for(const e of es)if(e.isIntersecting)navs.forEach(a=>a.getAttribute('href')==='#'+e.target.id?a.setAttribute('aria-current','true'):a.removeAttribute('aria-current'))},{rootMargin:'0px 0px -70% 0px'});chs.forEach(c=>cio.observe(c))}
else document.querySelectorAll('.anim').forEach(a=>a.classList.add('play'));
document.querySelectorAll('[data-replay]').forEach(b=>b.addEventListener('click',()=>{const f=b.closest('.anim');f.classList.remove('play');void f.offsetWidth;f.classList.add('play')}));
/* copy buttons */
document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',async()=>{const w=b.textContent;try{await navigator.clipboard.writeText(document.getElementById(b.dataset.copy).textContent);b.textContent='Copied'}catch(e){b.textContent='Select the text and copy it'}setTimeout(()=>b.textContent=w,2200)}));
/* checks */
document.querySelectorAll('.qz').forEach(f=>f.querySelector('[data-check]').addEventListener('click',()=>{const c=f.querySelector('input:checked'),fb=f.querySelector('.fb');
 if(!c){fb.textContent='Choose an answer first.';fb.className='fb';return}const ok=c.value===f.dataset.right;fb.className='fb '+(ok?'ok':'no');fb.textContent=(ok?'Right. ':'Not quite. ')+f.querySelector('.ans p').textContent}));
/* present: one scene a screen, moved by the keys */
const pb=document.getElementById('present'),scenes=()=>[...document.querySelectorAll('.scene')];
function go(d){const s=scenes();
 if(d>0){const t=s.find(e=>e.getBoundingClientRect().top>8);if(t)t.scrollIntoView({behavior:'smooth'})}else{const t=[...s].reverse().find(e=>e.getBoundingClientRect().top<-8);if(t)t.scrollIntoView({behavior:'smooth'})}}
function toggle(on){document.documentElement.classList.toggle('present',on);pb.textContent=on?'Stop presenting':'Present';
 try{if(on&&!document.fullscreenElement)document.documentElement.requestFullscreen();if(!on&&document.fullscreenElement)document.exitFullscreen()}catch(e){}}
pb.addEventListener('click',()=>toggle(!document.documentElement.classList.contains('present')));
document.addEventListener('fullscreenchange',()=>{if(!document.fullscreenElement)toggle(false)});
document.addEventListener('keydown',e=>{if(!document.documentElement.classList.contains('present')||e.target.closest('input,textarea')||(e.key===' '&&e.target.closest('button,summary')))return;
 if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){e.preventDefault();go(1)}else if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();go(-1)}else if(e.key==='Escape')toggle(false)});
addEventListener('beforeprint',()=>document.querySelectorAll('details').forEach(d=>d.open=true));
})();
"""
