"""Writes two pages for build.py: base/north-star.html (the North Star, purpose and value) and base/course.html
(how to use this project: a visual guide and short course, written by course_page.py).

Both follow Artifact Studio's instructions: the North Star page uses the teacher voice and the explainer recipe; the
course decks use the briefing manner, light, for a lecture hall. Look: the Practical AI colours.
"""
import html, re, pathlib
from steps import STEPS, LEVELS, WHO, coach_prompt, pasted_prompt, COACH_FILE

E = html.escape
G = "https://github.com/bar181/practical-ai/blob/main/projects/agentic-process/"
STEP = {s['n']: s for s in STEPS}
_PLAN = (pathlib.Path(__file__).resolve().parents[1] / "level-2-files/agentic-process/template/base/plan.md").read_text(encoding="utf-8").split("\n## Status")[0]
PLAN_ROWS = re.findall(r"^\| (?!Heading |---)([^|]+?) \|", _PLAN, re.M)
NORTH_STAR = "Anyone who repeats a job at work can turn it into a small AI tool that someone else can use, and know it works before anyone relies on it."


def md(text):
    """The little Markdown the sources use: **bold** and `code`."""
    t = E(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", t)


BASE_CSS = """
:root{--bg:#f3f5f9;--panel:#fff;--line:#c9d1de;--muted:#48546a;--ink:#14202e;--navy:#0c2340;--navy2:#17365f;--hl:#ffd23f;--blue:#2f6fb5;--pale:#e6ecf4;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,Menlo,Consolas,monospace;color-scheme:light}
*,*::before,*::after{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:400 1.05rem/1.55 var(--sans)}
h1,h2,h3,h4{margin:0;line-height:1.15;letter-spacing:-.01em;text-wrap:balance}p{margin:0}ul,ol{margin:0}
a{color:var(--blue)}:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
code{font:400 .92em/1 var(--mono);background:var(--pale);padding:1px 5px;border-radius:4px}
pre{margin:0;padding:14px;background:#fff;border:1px solid var(--line);border-radius:10px;white-space:pre-wrap;overflow-wrap:anywhere;font:400 .92rem/1.5 var(--mono)}
.btn{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:999px;border:0;background:var(--navy);color:#fff;font:700 1rem/1 var(--sans);cursor:pointer;text-decoration:none}
.btn.ghost{background:var(--panel);color:var(--navy);border:2px solid var(--navy)}
.me{display:flex;gap:14px;align-items:flex-start}.me img{flex:none;width:56px;height:56px;border-radius:50%}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""


def creator(me):
    return (f'<div class="me"><img src="data:image/jpeg;base64,{me}" width="56" height="56" alt="Bradley Ross"><div><b>Made by Bradley Ross</b>'
            '<p>An agentic AI architect and developer for businesses of every size, from start-up to enterprise. He builds and teaches practical AI.</p>'
            '<p><a href="https://www.linkedin.com/in/bradaross/">Connect with Bradley on LinkedIn</a></p></div></div>')


# ---------------------------------------------------------------- diagrams (inline SVG, each with a title)
def svg(w, h, title, body):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{E(title)}" class="dg" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif">{body}</svg>')

def box(x, y, w, h, fill, text, col="#14202e", size=20, bold=True, sub=None):
    t = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}"/>'
    ty = y + h / 2 + (size * .35) - (12 if sub else 0)
    t += f'<text x="{x + w/2}" y="{ty}" text-anchor="middle" font-size="{size}" font-weight="{700 if bold else 400}" fill="{col}">{E(text)}</text>'
    if sub: t += f'<text x="{x + w/2}" y="{ty + 26}" text-anchor="middle" font-size="16" fill="{col}">{E(sub)}</text>'
    return t

def arrow(x1, y1, x2, y2, col="#48546a"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="3"/>'
            f'<path d="M{x2},{y2} l-10,-6 v12 z" fill="{col}" transform="rotate({0 if y1 == y2 else 90} {x2} {y2})"/>')

def diagram(name):
    if name == "cost":
        b = '<text x="40" y="40" font-size="18" fill="#48546a">An illustration, not data: where the time and the checking go</text>'
        for i, (lab, d, bld) in enumerate([("Before AI", 25, 75), ("With AI", 75, 25)]):
            y = 80 + i * 110
            b += f'<text x="40" y="{y + 38}" font-size="20" font-weight="700" fill="#14202e">{lab}</text>'
            b += f'<rect x="180" y="{y}" width="{d*6.4}" height="60" fill="#ffd23f"/><rect x="{180 + d*6.4}" y="{y}" width="{bld*6.4}" height="60" fill="#b8c2d1"/>'
            b += f'<text x="{188}" y="{y + 38}" font-size="18" font-weight="700" fill="#14202e">Deciding</text><text x="{180 + d*6.4 + 8}" y="{y + 38}" font-size="18" fill="#14202e">Building</text>'
        return svg(860, 300, "An illustration: before AI most effort went into building; with AI, building is quick and the costly part is deciding what to build", b)
    if name == "stages":
        st = [("Decide", "steps 1 to 4"), ("Design", "steps 5 to 7"), ("Build and test", "step 8"), ("Grow", "step 9")]
        b = ''.join(box(20 + i * 215, 70, 190, 110, "#0c2340" if i != 2 else "#ffd23f", a, "#fff" if i != 2 else "#0c2340", 22, True, s) for i, (a, s) in enumerate(st))
        b += ''.join(arrow(210 + i * 215, 125, 233 + i * 215, 125) for i in range(3))
        b += '<text x="430" y="230" text-anchor="middle" font-size="18" fill="#48546a">A gate after every step: a question you answer before you go on</text>'
        return svg(880, 260, "The nine steps in four stages: decide, design, build and test, grow", b)
    if name == "reuse":
        rows = [("1. Built in", "What your chatbot already does"), ("2. Open source", "Free tools, with licence and last update"), ("3. Established practice", "How people who do this well do it"), ("4. Providers", "Paid services, listed evenly, last")]
        b = ''
        for i, (a, s) in enumerate(rows):
            y = 14 + i * 68
            b += f'<rect x="20" y="{y}" width="600" height="58" rx="10" fill="{"#0c2340" if i == 0 else "#17365f" if i == 1 else "#2f6fb5" if i == 2 else "#48546a"}"/>'
            b += f'<text x="38" y="{y + 37}" font-size="21" font-weight="700" fill="#fff">{E(a)}</text><text x="602" y="{y + 37}" text-anchor="end" font-size="17" fill="#fff">{E(s)}</text>'
        b += arrow(640, 150, 680, 150, "#14202e")
        b += '<text x="692" y="132" font-size="20" font-weight="700" fill="#14202e">Stop as soon as</text><text x="692" y="158" font-size="20" font-weight="700" fill="#14202e">something does</text><text x="692" y="184" font-size="20" font-weight="700" fill="#14202e">the whole job</text>'
        return svg(900, 290, "The reuse check, cheapest first: built in, open source, established practice, then providers. Stop as soon as something does the whole job", b)
    if name == "plan":
        short = {"The job", "The user", "What is out", "The wow", "The steps", "The test", "Next three additions"}
        b = ''
        for i, r in enumerate(PLAN_ROWS):
            x, y = 20 + (i % 3) * 290, 20 + (i // 3) * 62
            on = r in short
            b += box(x, y, 270, 50, "#ffd23f" if on else "#e6ecf4", r, "#0c2340", 17, on)
        b += f'<text x="20" y="{40 + 5*62}" font-size="17" fill="#48546a">Highlighted: the seven headings on the short path. Five lines at most under each.</text>'
        return svg(900, 360, f"The one-page plan: {len(PLAN_ROWS)} headings; the seven on the short path are highlighted", b)
    if name == "test":
        b = box(20, 40, 210, 90, "#e6ecf4", "Your instructions", "#0c2340", 19, True, "and one real input")
        b += arrow(230, 85, 300, 85) + box(300, 40, 230, 90, "#0c2340", "A new chat", "#fff", 21, True, "no memory, no help")
        b += arrow(530, 85, 600, 85) + box(600, 20, 270, 60, "#e6ecf4", "The result", "#0c2340", 19)
        b += box(600, 100, 270, 60, "#ffd23f", "Where it had to guess", "#0c2340", 19)
        b += '<text x="600" y="200" font-size="17" fill="#48546a">Read the guesses before the result</text>'
        return svg(900, 220, "The fresh-chat test: your instructions and one real input go to a new chat with no memory; it returns the result and a list of where it had to guess", b)
    if name == "levels":
        lv = [("Beginner", "Any chatbot: paste the coach"), ("Advanced", "A coding agent and one skill folder"), ("Expert", "Agents work unattended, with gates")]
        b = ''.join(box(30 + i * 280, 190 - i * 70, 260, 70 + i * 70, ["#e6ecf4", "#2f6fb5", "#0c2340"][i], a, "#0c2340" if i == 0 else "#fff", 22, True, s) for i, (a, s) in enumerate(lv))
        return svg(880, 280, "Three levels of the same process: Beginner in any chatbot, Advanced with a coding agent and a skill folder, Expert with agents that work unattended", b)
    if name == "unattended":
        st = [("Agent", "steps 1 to 6"), ("Agent", "prepares the tests"), ("Fresh sessions", "run each test"), ("Agent", "fixes, re-runs gates"), ("A person", "reads and decides")]
        b = ''.join(box(10 + i * 176, 70, 160, 100, "#ffd23f" if i == 4 else "#0c2340", a, "#0c2340" if i == 4 else "#fff", 20, True, s) for i, (a, s) in enumerate(st))
        b += ''.join(arrow(170 + i * 176, 120, 184 + i * 176, 120) for i in range(4))
        b += '<text x="450" y="215" text-anchor="middle" font-size="17" fill="#48546a">Nothing is merged, posted, sent, paid or published before the last box</text>'
        return svg(900, 240, "An unattended run: the agent does steps 1 to 6 and prepares tests, fresh sessions run them, the agent fixes and re-runs its gates, and a person reads the hand-back and decides", b)
    raise KeyError(name)


# ---------------------------------------------------------------- the North Star page
def north_star_html(me, guide_url, course_url):
    lv = [("Beginner", "Someone with a job they repeat, using any chatbot",
           "Trial and error in a chat until something works on the day; next week you start again",
           "A one-page plan, a prompt they can reuse, and a test they can rerun whenever they change it"),
          ("Advanced", "A builder working with a coding agent",
           "The agent builds fast and the shape is found by rebuilding; folders move and links break",
           "A project folder with its own checks, a front page written before the tool, and a stranger's test before polish"),
          ("Expert", "A team whose agents work unattended",
           "The author reviews their own work and passes it, because they know what they meant",
           "Fresh-session tests, gates a script can run, and a hand-back a person reads before anything ships")]
    cards = ''.join(f'<article class="lv"><h3>{a}</h3><p class="who">{E(b)}</p><p class="lab">Without it</p><p>{E(c)}</p><p class="lab">With it</p><p>{E(d)}</p></article>' for a, b, c, d in lv)
    alt = [("Prompting alone", "Fast for one answer", "Nothing checks the job, what already exists, or whether anyone else can use the result"),
           ("Spec-driven toolkits such as GitHub Spec Kit, Kiro and BMAD", "Turn a specification into plans, tasks and code, inside a developer's tools", "Start once you have decided to build, and are made for developers"),
           ("Agentic Process", "Starts before the spec: should this be built at all? Written for any chatbot, tested in Claude so far, and works with a coding agent", "Small tools, one user and one job. Not a replacement for a full engineering method on a large codebase")]
    rows = ''.join(f'<tr><th scope="row">{E(a)}</th><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in alt)
    nine = ''.join(f'<li><b>{E(s["name"])}</b> <span>{E(s["gate"])}</span></li>' for s in STEPS)
    css = BASE_CSS + """
header{background:var(--navy);color:#fff;padding:44px 0 40px}.wrap{max-width:900px;margin-inline:auto;padding-inline:20px}
.kick{font:700 .92rem/1.2 var(--sans);color:var(--hl)}
.ns{margin-top:16px;font:800 clamp(1.7rem,5.6vw,2.8rem)/1.15 var(--sans);max-width:22em}
.ns em{font-style:normal;background:linear-gradient(transparent 62%,rgba(255,210,63,.55) 62%)}
.sub{margin-top:16px;max-width:36em;color:#dfe6ef;font-size:1.15rem}
section{padding-top:48px}h2{font-size:clamp(1.4rem,4.4vw,2rem);max-width:24em;margin-top:6px}section>p{max-width:40em;margin-top:12px}
.lab{font:700 .86rem/1.2 var(--sans);color:var(--blue);margin-top:12px}
.analogy{margin-top:16px;background:var(--panel);border-left:6px solid var(--hl);border-radius:0 12px 12px 0;padding:16px 18px;max-width:42em}
.three{display:grid;gap:12px;margin-top:18px}@media(min-width:760px){.three{grid-template-columns:repeat(3,1fr)}}
.three div{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px}.three b{display:block;font-size:1.1rem;margin-bottom:6px}
.vp{margin-top:16px;padding:20px;border-radius:14px;background:var(--navy);color:#fff;font:700 clamp(1.15rem,3.4vw,1.45rem)/1.35 var(--sans);max-width:40em}
.lvs{display:grid;gap:12px;margin-top:18px}@media(min-width:820px){.lvs{grid-template-columns:repeat(3,1fr)}}
.lv{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px}.lv h3{font-size:1.2rem}.lv .who{color:var(--muted);margin-top:4px}.lv p+p{margin-top:4px}
.measure{margin-top:16px;display:grid;gap:12px}@media(min-width:760px){.measure{grid-template-columns:1fr 1fr}}
.measure div{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px}
.tw{overflow-x:auto;margin-top:16px}table{border-collapse:collapse;width:100%;min-width:600px;background:var(--panel);border-radius:12px}
th,td{text-align:left;vertical-align:top;padding:12px;border-bottom:1px solid var(--line)}thead th{font-size:.86rem;color:var(--muted)}tbody tr:last-child th,tbody tr:last-child td{background:#fff7d6}
ul.not{margin-top:12px;padding-left:1.2em;max-width:40em}ul.not li+li{margin-top:6px}
.go{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
footer{margin-top:56px;background:var(--navy);color:#dfe6ef;padding:28px 0 36px}footer a{color:var(--hl)}footer .me{margin-top:16px}
.src{font-size:.88rem;color:var(--muted);margin-top:10px;max-width:46em}
ol.nine{margin-top:14px;padding-left:1.6em;max-width:44em}ol.nine li+li{margin-top:6px}ol.nine span{color:var(--muted)}ol.nine li::marker{font-weight:800;color:var(--blue)}
#cp{margin:10px 0}
"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Agentic Process: the North Star, the purpose and the value</title>
<!-- Written by projects/agentic-process/_build/build.py (pages.py). Made with Artifact Studio's instructions: explainer recipe, teacher voice, the Practical AI colours. -->
<style>{css}</style>
</head>
<body>
<header><div class="wrap">
  <p class="kick">Agentic Process · back to basics</p>
  <p class="ns">{E(NORTH_STAR)}</p>
  <p class="sub">That is the North Star. Everything in the project, the nine steps, the coach, the checks and the course, exists to move someone toward it.</p>
</div></header>
<main class="wrap">

<section aria-labelledby="purpose"><p class="lab">The purpose</p><h2 id="purpose">AI made building cheap. Deciding what to build is now the expensive part.</h2>
  <div class="analogy"><b>Think of it as</b> a building site with an inspector. You agree the drawing before you pour concrete, and nothing moves to the next stage until the current one is signed off. The inspector does not slow the build down. The inspector stops you pouring concrete in the wrong place.</div>
  <p>An AI will build whatever you ask, quickly and with confidence. So the costly mistakes now happen before the first line is written. Agentic Process puts cheap checks in front of the build so that three mistakes stop happening:</p>
  <div class="three">
    <div><b>The wrong job</b>Asked for five things, you get a tool that does none of them well. Step 1 cuts it to one user and one job.</div>
    <div><b>It already existed</b>A built-in feature or a free tool already did it. Step 2 checks first, and stopping counts as a win.</div>
    <div><b>Only you can use it</b>It works in your chat, with everything you said earlier. Step 8 hands it to a stranger before anyone relies on it.</div>
  </div>
</section>

<section aria-labelledby="value"><p class="lab">The value proposition</p><h2 id="value">Build the right small tool once, and prove it works with a stranger before you rely on it.</h2>
  <p class="vp">For anyone who uses AI at work: nine short steps that stop you building the wrong thing, check what already exists, and test the result with a fresh chat that knows nothing, in the chatbot you already have, for free.</p>
  <div class="lvs">{cards}</div>
  <p>We expect the larger gain to be quality, not speed. Every time in the project is an estimate, because nobody has been timed yet.</p>
</section>

<section aria-labelledby="done"><p class="lab">How you know it is working</p><h2 id="done">The test of the North Star is a stranger finishing the job.</h2>
  <div class="measure">
    <div><p class="lab" style="margin-top:0">For your tool</p><p>A fresh chat, with only your instructions and one real input, finishes the job, and its list of where it had to guess has no blocking points left.</p></div>
    <div><p class="lab" style="margin-top:0">For this project</p><p>Three numbers, from a two-minute form anyone fills in after building a tool: how many tools passed a fresh-chat test, the minutes from first paste to a one-page plan (aim: under 30), and how many tools someone other than their builder used.</p><p style="margin-top:10px"><a href="https://github.com/bar181/practical-ai/issues/new?template=i-built-one.yml">Built one? Tell us in two minutes</a></p></div>
  </div>
</section>

<section aria-labelledby="diff"><p class="lab">Where it fits</p><h2 id="diff">It starts earlier than spec-driven toolkits, and it works outside a code editor.</h2>
  <div class="tw" tabindex="0" role="region" aria-label="How Agentic Process compares"><table><thead><tr><th scope="col">Approach</th><th scope="col">What it does well</th><th scope="col">Where it stops</th></tr></thead><tbody>{rows}</tbody></table></div>
  <p class="src">Spec-driven toolkits, checked on 16 November 2026: <a href="https://github.github.com/spec-kit/">GitHub Spec Kit</a> runs specify, plan, tasks and implement with a coding agent; <a href="https://kiro.dev/docs/specs/">Kiro</a> writes requirements, a design and tasks; the <a href="https://github.com/bmad-code-org/BMAD-METHOD">BMAD Method</a> uses role-based agents from analyst to developer. They suit large builds by developers. Agentic Process is designed to sit in front of them; that has not been tried yet.</p>
</section>

<section aria-labelledby="not"><p class="lab">What it is not</p><h2 id="not">Four things this project does not claim.</h2>
  <ul class="not">
    <li>It is not a way to build large software. It is for small tools: one user, one job.</li>
    <li>It does not replace your judgement. A person approves anything that is sent, posted, paid or published.</li>
    <li>It does not promise time saved. The times are estimates until learners are timed.</li>
    <li>It is not proven outside Claude yet. It is written for any chatbot.</li>
  </ul>
</section>

<section aria-labelledby="steps"><p class="lab">The nine steps</p><h2 id="steps">Four stages, a gate after every step.</h2>
  <ol class="nine">{nine}</ol>
  <p>The quickest way to run them: paste this into any chatbot and change the last line to your job.</p>
  <pre id="cp" tabindex="0">{E(coach_prompt("[one job you do on your own, in one sentence]"))}</pre><button class="btn" type="button" data-copy="cp">Copy the coach prompt</button>
</section>

<section aria-labelledby="start"><p class="lab">Start</p><h2 id="start">Three ways in.</h2>
  <div class="go"><a class="btn" href="{guide_url}">Read the guide to the nine steps</a><a class="btn ghost" href="{course_url}">Take the course</a><a class="btn ghost" href="{G}base/AI-INSTRUCTIONS.md">Paste the coach</a></div>
</section>
</main>
<footer><div class="wrap"><p>Part of <a href="https://github.com/bar181/practical-ai">Practical AI</a>: tools a person can use with an AI assistant the same day. <a href="{G}README.md">Agentic Process on GitHub</a>. Written on 16 November 2026.</p>{creator(me)}</div></footer>
<script>document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',async()=>{{const w=b.textContent;try{{await navigator.clipboard.writeText(document.getElementById(b.dataset.copy).textContent);b.textContent='Copied'}}catch(e){{b.textContent='Select the text and copy it'}}setTimeout(()=>b.textContent=w,2200)}}));</script>
</body>
</html>
"""


