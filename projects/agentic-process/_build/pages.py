"""Writes two pages for build.py: base/north-star.html (the North Star, purpose and value) and base/course.html
(the course: modules, step-by-step lessons, a lecture deck per module, knowledge checks).

Both follow Artifact Studio's instructions: the North Star page uses the teacher voice and the explainer recipe; the
course decks use the briefing manner, light, for a lecture hall. Look: the Practical AI colours.
"""
import html, re, pathlib, math
from steps import STEPS, LEVELS, WHO, coach_prompt, pasted_prompt, COACH_FILE
from course import COURSE, MODULES, CAPSTONE, INSTRUCTOR, MEMORY_OFF, PRIVACY, module_minutes, total_minutes

E = html.escape
G = "https://github.com/bar181/practical-ai/blob/main/projects/agentic-process/"
STEP = {s['n']: s for s in STEPS}
_PLAN = (pathlib.Path(__file__).resolve().parents[1] / "level-2-files/agentic-process/template/base/plan.md").read_text(encoding="utf-8").split("\n## Status")[0]
PLAN_ROWS = re.findall(r"^\| (?!Heading |---)([^|]+?) \|", _PLAN, re.M)
def hours():
    """The course time, rounded up to the half hour, as words a reader expects."""
    h = math.ceil(total_minutes() / 30) / 2
    return f"{int(h)}" if h == int(h) else f"{int(h)} and a half"


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
    <div><p class="lab" style="margin-top:0">For this project</p><p>People who are not its author use it on real work and report back. On 16 November 2026 that number is zero: every test so far was an AI session, in Claude.</p></div>
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


# ---------------------------------------------------------------- the course
def step_lesson(L):
    """A lesson that teaches one or two of the nine steps: content from steps.py, the do-list from where the learner works."""
    nums = L['step'] if isinstance(L['step'], tuple) else (L['step'],)
    sts = [STEP[n] for n in nums]
    title = L.get('title') or ' and '.join(s['name'] for s in sts)
    part, many = L.get('part'), len(sts) > 1
    lab = lambda s, t: f"Step {s['n']}: {t[0][0].lower() + t[0][1:]}" if many else t[0]
    timed = lambda t: re.sub(r"^About (\d+) minutes?", r"The step itself takes about \1 minutes", t)
    out = dict(id=L['id'], minutes=L['minutes'], title=title, steps=nums, chat=L.get('chat'), links=L.get('links'),
               objective=' '.join(s['purpose'] for s in sts) if not part else (sts[0]['purpose'].split('. ')[0] + '.' if part == 'build' else "Hand the first version to a stranger, a new chat with only your instructions, and collect where it had to guess."),
               stories=[(LEVELS[i], WHO[i], s['stories'][i]) for s in sts for i in range(3)] if not part else [],
               expect=' '.join(timed(s['expect']) for s in sts) if not part else ("Expect a first version that is smaller than you imagined: instructions, rules, the format of the result, and one worked example beside them." if part == 'build' else timed(sts[0]['expect'])),
               proof=[p for s in sts for p in s['proof']] if not part else (sts[0]['proof'][:1] if part == 'build' else [sts[0]['proof'][1], "Its list of where it had to guess"]),
               gate=[(s['n'], s['gate']) for s in sts] if part != 'build' else [],
               prompts=[(lab(s, pr), pr[1]) for s in sts for pr in s['prompts']] if not part else ([sts[0]['prompts'][0]] if part == 'build' else [sts[0]['prompts'][1]]))
    plural = "s, one after the other" if len(out['prompts']) > 1 else ""
    if L.get('chat') == 'new':
        do = ["Open a new chat. " + MEMORY_OFF,
              "Paste the prompt below, then " + ("your instructions and one real input. " + PRIVACY if part == 'test' else "your plan and front door") + ".",
              "Do not help it or explain anything. Wait for its answer and its list of where it had to guess.",
              "Read the list of guesses before anything else. Each guess is a gap in what you wrote.",
              "Answer the gate question, then take the fixes back to the coach chat."]
    elif part == 'build':
        do = ["In the coach chat, paste the prompt below with your plan in the brackets.",
              "Build only the beginner version. Keep the worked example beside the instructions, not inside them.",
              "Ask the chat: What did you decide, what did you assume and what did you not check?",
              "Save the instructions where your plan says they live. Lesson 4.2 tests them."]
    else:
        do = ["Read what this lesson is for (above) and what to expect (below).",
              f"In the coach chat from lesson 1.3, paste the prompt{plural}. Fill in the brackets. If you closed that chat, open a new one and paste your plan first.",
              "Check what comes back against \"Proof you are done\". Tick each one you have.",
              "Answer the gate question. If the answer is no, fix the step before you go on.",
              "Add the result to your plan."]
    out['do'] = do
    return out


def lesson_view(L, m):
    if 'step' in L: L = step_lesson(L)
    if L.get('prompt_from_step'):
        L['prompts'] = [("Prompt for the addition, on the date you decide", STEP[L['prompt_from_step']]['prompts'][0][1])]
        L['gate'] = [(L['prompt_from_step'], STEP[L['prompt_from_step']]['gate'])]
    rid = f"l{L['id']}"
    parts = [f'<section class="pg" id="{rid}" aria-labelledby="{rid}-h" data-lesson="{L["id"]}">',
             f'<p class="crumb"><a href="#m{m["n"]}">Module {m["n"]}: {E(m["title"])}</a> · Lesson {L["id"].replace("-", ".")}' + (f' · {E(L["track"])} track, optional' if L.get("track") else '') + '</p>',
             f'<h2 id="{rid}-h" tabindex="-1">{E(L["title"])}</h2>',
             f'<p class="meta">This lesson: about {L["minutes"]} minutes' + (f' · Step{"s" if len(L["steps"]) > 1 else ""} {" and ".join(map(str, L["steps"]))} of nine' if L.get("steps") else f' · Teaches step {L["step_ref"]} of nine' if L.get("step_ref") else '') + ('' if not L.get("chat") else ' · In a new chat that remembers nothing' if L["chat"] == "new" else ' · In the coach chat') + '</p>',
             f'<p class="obj"><b>You will:</b> {md(L["objective"])}</p>']
    if L.get('body'):
        parts.append('<div class="body">' + ''.join(f'<p>{md(b)}</p>' for b in L['body']) + '</div>')
    parts.append('<h3>Do this</h3><ol class="do">' + ''.join(f'<li>{md(d)}</li>' for d in L['do']) + '</ol>')
    if L.get('expect'):
        parts.append(f'<h3>What to expect</h3><p>{md(L["expect"])}</p>')
    if L.get('stories'):
        parts.append('<h3>Who it helps</h3><ul class="stories">' + ''.join(f'<li><b class="lvl">{a}</b> As {E(w)}, {E(t)}</li>' for a, w, t in L['stories']) + '</ul>')
    for k, (lab, txt) in enumerate(L.get('prompts', [])):
        pid = f"{rid}-p{k}"
        parts.append(f'<h3>{E(lab)}</h3><pre id="{pid}" tabindex="0">{E(txt)}</pre><button class="btn sm" type="button" data-copy="{pid}">Copy this prompt</button>')
    if L.get('prompt'):
        parts.append(f'<h3>The prompt</h3><pre id="{rid}-p" tabindex="0">{E(L["prompt"])}</pre><button class="btn sm" type="button" data-copy="{rid}-p">Copy this prompt</button>')
    if L.get('fallback'):
        parts.append(f'<p class="note">If your chatbot cannot open the link: open the coach on GitHub ({E(COACH_FILE)}), press Raw, copy all of it, paste it into the chat, then send this instead:</p><pre id="{rid}-f" tabindex="0">{E(L["fallback"])}</pre><button class="btn sm ghost" type="button" data-copy="{rid}-f">Copy the second prompt</button>')
    if L.get('links'):
        parts.append('<h3>Open</h3><ul class="links">' + ''.join(f'<li><a href="{E(u)}">{E(t)}</a></li>' for t, u in L['links']) + '</ul>')
    parts.append('<h3>Proof you are done</h3><ul class="proof">' + ''.join(f'<li><label><input type="checkbox" data-proof="{L["id"]}-{i}"> {md(p)}</label></li>' for i, p in enumerate(L['proof'])) + '</ul>')
    for n, g in L.get('gate', []):
        parts.append(f'<p class="gate"><b>The gate for step {n}.</b> {E(g)}</p>')
    parts.append(f'<div class="done"><button class="btn" type="button" data-done="{L["id"]}" aria-pressed="false">Mark this lesson complete</button></div>')
    parts.append('</section>')
    return '\n'.join(parts)


def deck_view(m):
    core = module_minutes(m)[1]
    slides = []
    for i, (kind, title, body, notes) in enumerate(m['slides'], 1):
        if kind == 'title':
            inner = f'<p class="k">{E(COURSE["subtitle"])}</p><h3>{E(title)}</h3><p class="sm">{E(body[0])}</p>'
        elif kind == 'two':
            lt, lp, rt, rp = body
            col = lambda t, ps: f'<div><p class="k">{E(t)}</p><ul>' + ''.join(f'<li>{E(p)}</li>' for p in ps) + '</ul></div>'
            inner = f'<h3>{E(title)}</h3><div class="cols">{col(lt, lp)}{col(rt, rp)}</div>'
        elif kind == 'diagram':
            inner = f'<h3>{E(title)}</h3><div class="fig">{diagram(body)}</div>'
        elif kind == 'quote':
            inner = f'<h3>{E(title)}</h3><p class="q">{E(body[0])}</p>'
        elif kind == 'lab':
            inner = f'<p class="k">Lab</p><h3>{E(title)}</h3><ol>' + ''.join(f'<li>{E(p)}</li>' for p in body) + '</ol>'
        else:
            inner = f'<h3>{E(title)}</h3><ul>' + ''.join(f'<li>{E(p)}</li>' for p in body) + '</ul>'
        slides.append(f'<section class="sl {kind}" aria-roledescription="slide" aria-label="Slide {i} of {len(m["slides"])}"><div class="si">{inner}</div>'
                      f'<p class="sf">Module {m["n"]} · {i} / {len(m["slides"])}</p><aside class="nt"><b>Instructor notes.</b> {E(notes.replace("{LAB}", str(core)))}</aside></section>')
    return (f'<div class="deck" data-m="{m["n"]}" tabindex="0" role="region" aria-roledescription="slide deck" aria-label="Lecture slides for module {m["n"]}, {len(m["slides"])} slides">'
            f'<div class="stage">{"".join(slides)}</div>'
            '<div class="dbar"><button type="button" class="prev" aria-label="Previous slide">&#8592;</button><span class="cnt" aria-live="polite"></span>'
            '<button type="button" class="next" aria-label="Next slide">&#8594;</button><button type="button" class="nts" aria-pressed="false">Instructor notes</button><button type="button" class="pw">Presenter window</button>'
            '<button type="button" class="fs">Full screen</button></div></div>')


def quiz_view(m):
    qs = []
    for qi, (q, opts, right, why) in enumerate(m['quiz']):
        name = f"q{m['n']}-{qi}"
        r = (m['n'] + qi) % len(opts)                                   # move the right answer so it is not always in one place
        order = list(range(len(opts))); order.remove(right); order.insert(r, right)
        opts, right = [opts[k] for k in order], r
        o = ''.join(f'<label><input type="radio" name="{name}" value="{i}"> {E(t)}</label>' for i, t in enumerate(opts))
        qs.append(f'<fieldset class="qz" data-right="{right}"><legend>{qi + 1}. {E(q)}</legend>{o}'
                  f'<button class="btn sm ghost" type="button" data-check>Check</button><p class="fb" aria-live="polite"></p>'
                  f'<details class="ans"><summary>Show the answer</summary><p>{E(opts[right])}. {E(why)}</p></details></fieldset>')
    return ''.join(qs)


def module_view(m):
    total, core = module_minutes(m)
    lessons = ''.join(f'<li><a href="#l{L["id"]}">{L["id"].replace("-", ".")} {E(L.get("title") or step_lesson(L)["title"])}</a> <span class="mins">{L["minutes"]} min{", optional" if L.get("optional") else ""}</span>'
                      f'<span class="tick" data-tick="{L["id"]}" aria-hidden="true"></span></li>' for L in m['lessons'])
    return f'''<section class="pg" id="m{m["n"]}" aria-labelledby="m{m["n"]}-h">
<p class="crumb"><a href="#home">Course home</a> · Module {m["n"]} of {len(MODULES)}</p>
<h2 id="m{m["n"]}-h" tabindex="-1">Module {m["n"]}: {E(m["title"])}</h2>
<p class="meta">About {total} minutes: a {m["lecture"]}-minute lecture ({len(m["slides"])} slides), {core} minutes of lessons, and a three-question check</p>
<p class="obj"><b>Purpose.</b> {E(m["purpose"])}</p>
<h3>By the end you can</h3><ul class="outc">{"".join(f"<li>{E(o)}</li>" for o in m["outcomes"])}</ul>
<h3>1. The lecture</h3><p>Click through on your own, or present it: press Full screen for the room and Presenter window for your notes. Press Instructor notes (or N) to show the notes under the slide.</p>
{deck_view(m)}
<h3>2. The lessons, step by step</h3><ol class="lessons">{lessons}</ol>
<h3>3. Check yourself</h3>{quiz_view(m)}
<h3>4. Assignment</h3><p class="assign">{E(m["assignment"])}</p>
</section>'''


def course_html(me, north_url, guide_url):
    all_lessons = [(m, L) for m in MODULES for L in m['lessons']]
    core_ids = [L['id'] for m, L in all_lessons if not L.get('optional')]
    nav = ['<li><a href="#home">Course home</a></li>']
    for m in MODULES:
        sub = ''.join(f'<li><a href="#l{L["id"]}">{L["id"].replace("-", ".")} {E(L.get("title") or step_lesson(L)["title"])}</a></li>' for L in m['lessons'])
        nav.append(f'<li><a href="#m{m["n"]}"><b>Module {m["n"]}</b> {E(m["title"])}</a><ol>{sub}</ol></li>')
    nav.append('<li><a href="#capstone"><b>Capstone</b></a></li><li><a href="#teach">For instructors</a></li>')
    mods = ''.join(f'<li><a class="mc" href="#m{m["n"]}"><span class="mn">Module {m["n"]}</span><b>{E(m["title"])}</b><span>{E(m["purpose"])}</span><span class="mins">About {module_minutes(m)[0]} minutes · {len(m["lessons"])} lessons</span></a></li>' for m in MODULES)
    rub = ''.join(f'<tr><th scope="row">{E(a)}</th><td>{E(b)}</td><td>{c}</td></tr>' for a, b, c in CAPSTONE['rubric'])
    fmts = ''.join(f'<tr><th scope="row">{E(a)}</th><td>{E(b)}</td></tr>' for a, b in INSTRUCTOR['formats'])
    watch = ''.join(f'<tr><th scope="row">{E(a)}</th><td>{E(b)}</td></tr>' for a, b in INSTRUCTOR['watch'])
    lessons_html = '\n'.join(lesson_view(dict(L), m) for m, L in all_lessons)
    order = [f"l{L['id']}" for m, L in all_lessons]
    needs = [n.replace("{HOURS}", hours()) for n in COURSE["needs"]]
    css = BASE_CSS + """
.top{background:var(--navy);color:#fff}.top .in{max-width:1240px;margin:0 auto;padding:14px 16px;display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center}
.top .t{font:800 1.15rem/1.2 var(--sans)}.top .t span{display:block;font-weight:400;font-size:.9rem;color:#c9d6e6}
.prog{margin-left:auto;display:flex;align-items:center;gap:10px;font-size:.92rem}.bar{width:140px;height:10px;border-radius:5px;background:#2b4a75;overflow:hidden}.bar i{display:block;height:100%;width:0;background:var(--hl)}
.top a{color:var(--hl)}
.lay{max-width:1240px;margin:0 auto;padding:16px;display:grid;gap:20px}@media(min-width:980px){.lay{grid-template-columns:290px 1fr}}
nav.side{font-size:.95rem}nav.side details{background:var(--panel);border:1px solid var(--line);border-radius:12px}
nav.side summary{min-height:48px;display:flex;align-items:center;padding:0 14px;font-weight:700;cursor:pointer}
nav.side ol,nav.side ul{list-style:none;padding:0 8px 10px;margin:0}nav.side ol ol{padding:0 0 4px 10px}
nav.side a{display:block;min-height:40px;padding:9px 8px;border-radius:8px;color:var(--ink);text-decoration:none;line-height:1.3}
nav.side a:hover{background:var(--pale)}nav.side a[aria-current="page"]{background:var(--navy);color:#fff}
nav.side a b{margin-right:6px;white-space:nowrap}
@media(min-width:980px){nav.side{position:sticky;top:12px;align-self:start;max-height:calc(100vh - 24px);overflow:auto}}
main{min-width:0}
.pg{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:22px 20px 26px;margin-bottom:20px}
.js .pg{display:none}.js .pg.on{display:block}
.pg h2{font-size:clamp(1.5rem,4vw,2.1rem)}.pg h3{font-size:1.18rem;margin-top:26px;margin-bottom:8px}
h2[tabindex="-1"]:focus{outline:none}.crumb{font-size:.9rem;color:var(--muted);margin-bottom:8px}.meta{color:var(--muted);margin-top:6px}
.obj{margin-top:14px;padding:14px 16px;background:var(--pale);border-radius:12px;max-width:46em}
.pg p,.pg li{max-width:46em}.pg ul,.pg ol{padding-left:1.3em}.pg li+li{margin-top:6px}
.do li::marker{font-weight:700;color:var(--blue)}
.stories{list-style:none;padding:0!important;display:grid;gap:8px}.stories li{background:var(--bg);border-radius:10px;padding:10px 12px}
.lvl{display:inline-block;margin-right:6px;padding:3px 7px;border-radius:4px;background:var(--navy);color:#fff;font-size:.78rem}
.btn.sm{min-height:44px;margin-top:8px;font-size:.95rem}
.note{margin-top:12px;color:var(--muted)}
.proof{list-style:none;padding:0!important}.proof label{display:flex;gap:10px;align-items:flex-start;min-height:44px;padding:8px 10px;border-radius:10px;background:var(--bg);cursor:pointer}
.proof input{width:20px;height:20px;margin-top:2px;flex:none}
.gate{margin-top:16px;padding:12px 14px;border-left:5px solid var(--hl);background:#fff7d6;border-radius:0 10px 10px 0}
.done{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.done .btn[aria-pressed="true"]{background:#1d6b3a}
.pn{display:flex;justify-content:space-between;gap:10px;margin-top:20px;flex-wrap:wrap}
.home-hero{background:var(--navy);color:#fff;border-radius:16px;padding:26px 22px;margin:-22px -20px 0}.home-hero h2{font-size:clamp(1.7rem,5vw,2.6rem)}.home-hero p{margin-top:12px;color:#dfe6ef;max-width:40em;font-size:1.1rem}
.facts{display:grid;gap:10px;margin-top:18px}@media(min-width:760px){.facts{grid-template-columns:repeat(3,1fr)}}.facts div{background:var(--bg);border-radius:12px;padding:14px}.facts b{display:block}.facts ul.needs{padding-left:1.1em}
ol.mods{list-style:none;padding:0!important;display:grid;gap:10px}@media(min-width:760px){ol.mods{grid-template-columns:1fr 1fr}}
.mc{display:grid;gap:4px;padding:16px;border:1px solid var(--line);border-radius:12px;color:var(--ink);text-decoration:none;background:var(--panel);height:100%}.mc:hover{border-color:var(--blue)}
.mc .mn{font:700 .84rem/1 var(--sans);color:var(--blue)}.mc b{font-size:1.15rem}.mins{color:var(--muted);font-size:.9rem}
.lessons{padding-left:0!important;list-style:none}.lessons li{display:flex;gap:10px;align-items:center;flex-wrap:wrap;min-height:44px;border-bottom:1px solid var(--line)}
.tick{width:20px;height:20px;border-radius:50%;border:2px solid var(--line);margin-left:auto}.tick.on{background:#1d6b3a;border-color:#1d6b3a}
.qz{border:1px solid var(--line);border-radius:12px;padding:14px;margin:12px 0 0}.qz legend{font-weight:700;padding:0 6px;max-width:44em}
.qz label{display:flex;gap:10px;align-items:center;min-height:44px;padding:4px 8px;border-radius:8px;cursor:pointer}.qz label:hover{background:var(--bg)}
.qz input{width:20px;height:20px;flex:none}.fb{margin-top:8px;font-weight:700}.fb.ok{color:#1d6b3a}.fb.no{color:#9b2c1f}
.js .ans{display:none}.ans{margin-top:8px}.ans summary{min-height:44px;display:flex;align-items:center;cursor:pointer}
.assign{padding:14px 16px;border-left:5px solid var(--blue);background:var(--pale);border-radius:0 10px 10px 0}
table{border-collapse:collapse;width:100%;min-width:520px}.tw{overflow-x:auto}th,td{text-align:left;vertical-align:top;padding:10px;border-bottom:1px solid var(--line)}thead th{font-size:.86rem;color:var(--muted)}
/* the lecture decks: light, for a lecture hall */
.deck{margin-top:10px;border-radius:14px;outline-offset:4px}
.stage{position:relative;aspect-ratio:16/9;container-type:inline-size;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.sl{position:absolute;inset:0;display:none;flex-direction:column;padding:5cqw 6cqw 4cqw;background:#fff}
.sl.cur{display:flex}
.sl .si{flex:1;display:flex;flex-direction:column;justify-content:center;gap:2cqw;min-height:0}
.sl h3{margin:0;font:800 4.4cqw/1.12 var(--sans);color:var(--navy);max-width:22em}
.sl .k{font:700 1.9cqw/1.2 var(--sans);color:var(--blue)}
.sl ul,.sl ol{margin:0;padding-left:1.2em;font:400 2.7cqw/1.4 var(--sans);color:var(--ink)}.sl li+li{margin-top:1cqw}.sl li::marker{color:var(--blue);font-weight:700}
.sl .sm{font:400 2.6cqw/1.3 var(--sans);color:var(--muted)}
.sl.title{background:var(--navy)}.sl.title h3{color:#fff;font-size:6.2cqw}.sl.title .k{color:var(--hl)}.sl.title .sm{color:#c9d6e6}.sl.title .sf{color:#9fb2c9}
.sl.recap{background:#fff7d6}.sl.lab .k{color:#1d6b3a}
.sl .q{font:600 3.3cqw/1.35 Georgia,"Iowan Old Style",serif;color:var(--ink);border-left:1cqw solid var(--hl);padding-left:2.4cqw;max-width:30em}
.sl .cols{display:grid;grid-template-columns:1fr 1fr;gap:3cqw}.sl .cols>div{background:var(--bg);border-radius:1.4cqw;padding:2.2cqw}
.sl .fig{flex:1;min-height:0;display:flex;align-items:center}.sl .fig svg{width:100%;height:100%;max-height:34cqw}
.sl p,.sl li{max-width:none}.sl .sf{margin:0;font:400 1.5cqw/1 var(--sans);color:var(--muted);text-align:right}
.nt{display:none}.deck.notes .sl.cur+.nt,.deck.notes .nt{}
.dbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:10px}
.dbar button{min-height:44px;min-width:48px;border-radius:999px;border:1px solid var(--line);background:var(--panel);color:var(--ink);font:700 1rem/1 var(--sans);padding:0 16px;cursor:pointer}
.dbar button[aria-pressed="true"]{background:var(--navy);color:#fff}.cnt{font-variant-numeric:tabular-nums;color:var(--muted);min-width:5em;text-align:center}
.notebox{margin-top:10px;padding:12px 14px;border-radius:10px;background:var(--pale);display:none}.deck.notes .notebox{display:block}
.deck:fullscreen{background:#fff;padding:0;display:flex;flex-direction:column;justify-content:center}.deck:fullscreen .stage{border:0;border-radius:0;width:min(100vw,177.78vh);margin:auto}
.deck:fullscreen .dbar{position:fixed;bottom:10px;right:10px;opacity:.25}.deck:fullscreen .dbar:hover,.deck:fullscreen .dbar:focus-within{opacity:1}
/* without the script every slide shows, one under the other */
html:not(.js) .stage{aspect-ratio:auto;overflow:visible;border:0;background:none;display:grid;gap:14px}
html:not(.js) .sl{position:relative;display:flex;aspect-ratio:16/9;border:1px solid var(--line);border-radius:14px}
html:not(.js) .nt{display:block;position:absolute;left:-9999px}html:not(.js) .dbar{display:none}
.dg{display:block}
footer{max-width:1240px;margin:0 auto;padding:10px 16px 40px}
/* print a module page: every slide, each with its notes, one to a page */
@media print{.top,nav.side,.dbar,.notebox,.done,.pn,footer,[data-copy],[data-check]{display:none!important}.lay{display:block;padding:0}.pg{border:0;padding:0}
  .stage{aspect-ratio:auto;overflow:visible;border:0;background:none;display:block}
  .sl{position:relative;display:flex!important;aspect-ratio:16/9;border:1px solid #999;border-radius:0;break-inside:avoid;page-break-inside:avoid;margin-bottom:2mm}
  .sl .nt{display:block;position:absolute;top:100%;left:0;right:0;padding-top:3mm;font-size:11pt}.sl{margin-bottom:60mm;break-after:page;page-break-after:always}
  .js .ans{display:block}}
"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(COURSE["title"])}: {E(COURSE["subtitle"])}</title>
<!-- Written by projects/agentic-process/_build/build.py from _build/course.py and _build/steps.py. Change the sources, not this file.
     Made with Artifact Studio's instructions: the lecture decks use the briefing manner, light; the Practical AI colours. -->
<style>{css}</style>
</head>
<body>
<header class="top"><div class="in"><p class="t">{E(COURSE["title"])}<span>{E(COURSE["subtitle"])} · {len(MODULES)} modules · {len(core_ids)} core lessons · about {hours()} hours</span></p>
<p class="prog"><span id="progtxt">0 of {len(core_ids)} core lessons done</span><span class="bar" aria-hidden="true"><i id="progbar"></i></span></p><p><a href="{north_url}">North Star</a> · <a href="{guide_url}">The guide</a></p></div></header>
<div class="lay">
<nav class="side" aria-label="Course"><details open id="navd"><summary>Course contents</summary><ol>{"".join(nav)}</ol></details></nav>
<main id="main">
<section class="pg" id="home" aria-labelledby="home-h">
  <div class="home-hero"><h2 id="home-h" tabindex="-1">{E(COURSE["title"])}</h2><p>{E(COURSE["purpose"])}</p></div>
  <div class="facts"><div><b>Who it is for</b>{E(COURSE["audience"])}</div><div><b>What you need</b><ul class="needs">{"".join(f"<li>{E(x)}</li>" for x in needs)}</ul></div><div><b>How it runs</b>Each module has a lecture deck, step-by-step lessons, a three-question check and an assignment. It ends with a capstone: your own tool through steps 1 to 8, with step 9 planned.</div></div>
  <h3>By the end of the course you can</h3><ol>{"".join(f"<li>{E(o)}</li>" for o in COURSE["outcomes"])}</ol>
  <h3>The modules</h3><ol class="mods">{mods}<li><a class="mc" href="#capstone"><span class="mn">Capstone</span><b>{E(CAPSTONE["name"])}</b><span>{E(CAPSTONE["purpose"])}</span></a></li></ol>
  <p class="note">{E(COURSE["honest"])} Your progress is kept in this browser only.</p>
  <div class="pn"><span></span><a class="btn" href="#m1">Start Module 1</a></div>
</section>
{"".join(module_view(m) for m in MODULES)}
{lessons_html}
<section class="pg" id="capstone" aria-labelledby="cap-h">
  <p class="crumb"><a href="#home">Course home</a> · Capstone</p><h2 id="cap-h" tabindex="-1">{E(CAPSTONE["title"])}: {E(CAPSTONE["name"])}</h2>
  <p class="obj"><b>Purpose.</b> {E(CAPSTONE["purpose"])}</p>
  <p class="gate"><b>If you stop at step 2.</b> {E(CAPSTONE["stop"])}</p>
  <h3>Hand in</h3><ul class="proof">{"".join(f'<li><label><input type="checkbox" data-proof="cap-{i}"> {E(d)}</label></li>' for i, d in enumerate(CAPSTONE["deliver"]))}</ul>
  <h3>How it is marked, out of 100</h3><div class="tw" tabindex="0" role="region" aria-label="Capstone rubric"><table><thead><tr><th scope="col">Measure</th><th scope="col">What full marks looks like</th><th scope="col">Points</th></tr></thead><tbody>{rub}</tbody></table></div>
  <p class="note">{E(CAPSTONE["alone"])} The nine steps, with a prompt for each, are in <a href="{G}base/PROCESS.md">the steps page</a> and <a href="{guide_url}">the guide</a>.</p>
</section>
<section class="pg" id="teach" aria-labelledby="teach-h">
  <p class="crumb"><a href="#home">Course home</a> · For instructors</p><h2 id="teach-h" tabindex="-1">For instructors</h2>
  <p class="obj">{E(INSTRUCTOR["how"])}</p>
  <h3>Presenting</h3><p>{E(INSTRUCTOR["present"])} Without a second screen, press <b>Instructor notes</b> (or N when the deck has focus) to show the notes under the slide.</p>
  <h3>Three ways to run it</h3><div class="tw" tabindex="0" role="region" aria-label="Formats"><table><thead><tr><th scope="col">Format</th><th scope="col">How</th></tr></thead><tbody>{fmts}</tbody></table></div>
  <h3>Before the first session</h3><ul>{"".join(f"<li>{E(b)}</li>" for b in INSTRUCTOR["before"])}</ul>
  <h3>What to watch for</h3><div class="tw" tabindex="0" role="region" aria-label="What to watch for"><table><thead><tr><th scope="col">You see</th><th scope="col">Say or do</th></tr></thead><tbody>{watch}</tbody></table></div>
  <p class="note">{E(COURSE["honest"])}</p>
</section>
</main></div>
<footer>{creator(me)}</footer>
<script>
/* Everything above reads without this script. It adds: one page at a time, the slide decks, the checks, and progress kept in this browser. */
(()=>{{document.documentElement.classList.add('js');
const ORDER={order!r},CORE={core_ids!r},LESSONS=CORE.length,KEY='ap-course-v1';
let st={{done:{{}},proof:{{}}}};try{{st=JSON.parse(localStorage.getItem(KEY))||st}}catch(e){{}}
const save=()=>{{try{{localStorage.setItem(KEY,JSON.stringify(st))}}catch(e){{}}}};
const pages=[...document.querySelectorAll('.pg')],links=[...document.querySelectorAll('nav.side a')];
function show(){{const id=(location.hash||'#home').slice(1);const pg=document.getElementById(id)&&document.getElementById(id).classList.contains('pg')?document.getElementById(id):document.getElementById('home');
  pages.forEach(p=>p.classList.toggle('on',p===pg));links.forEach(a=>a.getAttribute('href')==='#'+pg.id?a.setAttribute('aria-current','page'):a.removeAttribute('aria-current'));
  if(innerWidth<980)document.getElementById('navd').open=false;const h=pg.querySelector('h2');if(h&&location.hash)h.focus({{preventScroll:true}});scrollTo(0,0)}}
addEventListener('hashchange',show);
/* previous and next under each lesson */
ORDER.forEach((id,i)=>{{const pg=document.getElementById(id),d=document.createElement('div');d.className='pn';
  d.innerHTML=(i?'<a class="btn ghost" href="#'+ORDER[i-1]+'">&#8592; Previous lesson</a>':'<span></span>')+(i<ORDER.length-1?'<a class="btn" href="#'+ORDER[i+1]+'">Next lesson &#8594;</a>':'<a class="btn" href="#capstone">The capstone &#8594;</a>');pg.appendChild(d)}});
/* progress */
function paint(){{const n=CORE.filter(k=>st.done[k]).length;document.getElementById('progtxt').textContent=n+' of '+LESSONS+' core lessons done';document.getElementById('progbar').style.width=(100*n/LESSONS)+'%';
  document.querySelectorAll('[data-done]').forEach(b=>{{const on=!!st.done[b.dataset.done];b.setAttribute('aria-pressed',on);b.textContent=on?'Done: mark as not done':'Mark this lesson complete'}});
  document.querySelectorAll('[data-tick]').forEach(t=>t.classList.toggle('on',!!st.done[t.dataset.tick]));
  document.querySelectorAll('[data-proof]').forEach(c=>c.checked=!!st.proof[c.dataset.proof])}}
document.addEventListener('click',e=>{{const b=e.target.closest('[data-done]');if(b){{st.done[b.dataset.done]=!st.done[b.dataset.done];save();paint()}}}});
document.addEventListener('change',e=>{{const c=e.target.closest('[data-proof]');if(c){{st.proof[c.dataset.proof]=c.checked;save()}}}});
/* copy buttons */
document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',async()=>{{const was=b.textContent;try{{await navigator.clipboard.writeText(document.getElementById(b.dataset.copy).textContent);b.textContent='Copied'}}catch(e){{b.textContent='Select the text and copy it'}}setTimeout(()=>b.textContent=was,2200)}}));
/* knowledge checks */
document.querySelectorAll('.qz').forEach(f=>f.querySelector('[data-check]').addEventListener('click',()=>{{const c=f.querySelector('input:checked'),fb=f.querySelector('.fb');
  if(!c){{fb.textContent='Choose an answer first.';fb.className='fb';return}}const ok=c.value===f.dataset.right;fb.className='fb '+(ok?'ok':'no');
  fb.textContent=(ok?'Right. ':'Not quite. ')+f.querySelector('.ans p').textContent}}));
/* slide decks */
document.querySelectorAll('.deck').forEach(d=>{{const sl=[...d.querySelectorAll('.sl')],cnt=d.querySelector('.cnt'),nb=d.querySelector('.nts');let i=0;
  const box=document.createElement('div');box.className='notebox';box.setAttribute('aria-live','polite');d.appendChild(box);
  const go=k=>{{i=Math.max(0,Math.min(sl.length-1,k));sl.forEach((s,j)=>s.classList.toggle('cur',j===i));cnt.textContent=(i+1)+' / '+sl.length;box.innerHTML=sl[i].querySelector('.nt').innerHTML;if(typeof paintPw==='function')paintPw()}};
  d.querySelector('.prev').addEventListener('click',()=>go(i-1));d.querySelector('.next').addEventListener('click',()=>go(i+1));
  const notes=()=>{{const on=!d.classList.contains('notes');d.classList.toggle('notes',on);nb.setAttribute('aria-pressed',on)}};nb.addEventListener('click',notes);
  d.querySelector('.fs').addEventListener('click',()=>{{try{{document.fullscreenElement?document.exitFullscreen():d.requestFullscreen()}}catch(e){{}}}});
  /* the presenter window: notes, the next slide and a timer on the instructor's screen; it moves the slides too */
  let pw=null,t0=0;const pb=d.querySelector('.pw');
  const paintPw=()=>{{if(!pw||pw.closed)return;const q=x=>pw.document.getElementById(x),nx=sl[i+1];q('c').textContent='Slide '+(i+1)+' of '+sl.length;
    q('n').innerHTML=sl[i].querySelector('.nt').innerHTML;q('x').textContent=nx?'Next: '+nx.querySelector('h3').textContent:'Last slide'}};
  pb.addEventListener('click',()=>{{try{{pw=window.open('','ap-presenter-'+d.dataset.m,'width=900,height=640')}}catch(e){{pw=null}}
    if(!pw){{if(!d.classList.contains('notes'))notes();pb.textContent='Pop-ups are blocked: notes are below the slide';return}}
    pw.document.title='Presenter: module '+d.dataset.m;
    pw.document.body.innerHTML='<style>body{{font:1.25rem/1.5 system-ui,sans-serif;margin:24px;color:#14202e}}#c,#tm{{font-weight:700}}#x{{color:#48546a;margin-top:18px}}button{{font:700 1.1rem system-ui;min-height:48px;padding:0 20px;margin:16px 8px 0 0}}</style><p><span id="c"></span> · <span id="tm">0:00</span></p><div id="n"></div><p id="x"></p><button id="b">Previous</button><button id="f">Next</button>';
    pw.document.getElementById('b').onclick=()=>go(i-1);pw.document.getElementById('f').onclick=()=>go(i+1);
    pw.document.addEventListener('keydown',e=>{{if(['ArrowRight','PageDown'].includes(e.key))go(i+1);else if(['ArrowLeft','PageUp'].includes(e.key))go(i-1)}});
    t0=Date.now();const tick=setInterval(()=>{{if(!pw||pw.closed){{clearInterval(tick);return}}const s=Math.floor((Date.now()-t0)/1000);pw.document.getElementById('tm').textContent=Math.floor(s/60)+':'+String(s%60).padStart(2,'0')}},1000);paintPw()}});
  d.addEventListener('keydown',e=>{{if(e.target.closest('button')&&(e.key===' '||e.key==='Enter'))return;
    if(['ArrowRight','PageDown',' '].includes(e.key)){{e.preventDefault();go(i+1)}}else if(['ArrowLeft','PageUp'].includes(e.key)){{e.preventDefault();go(i-1)}}
    else if(e.key==='Home'){{go(0)}}else if(e.key==='End'){{go(sl.length-1)}}else if(e.key==='n'||e.key==='N'){{notes()}}}});
  let x0=null;d.querySelector('.stage').addEventListener('pointerdown',e=>x0=e.clientX);d.querySelector('.stage').addEventListener('pointerup',e=>{{if(x0===null)return;const dx=e.clientX-x0;x0=null;if(Math.abs(dx)>40)go(i+(dx<0?1:-1));else go(i+1)}});
  go(0)}});
paint();show()}})();
</script>
</body>
</html>
"""


def course_outline_md(course_url):
    L = [f"**[{COURSE['title']}]({course_url})**: {COURSE['purpose']} {len(MODULES)} modules, about "
         f"{hours()} hours, each with a lecture deck, step-by-step lessons, a three-question check and an",
         "assignment, then a capstone. It has not been taught yet.", "",
         "| Module | Purpose | Lessons | Time |", "| --- | --- | --- | --- |"]
    for m in MODULES:
        names = '; '.join((Lx.get('title') or step_lesson(Lx)['title']) + (' (optional)' if Lx.get('optional') else '') for Lx in m['lessons'])
        L.append(f"| {m['n']}. {m['title']} | {m['purpose']} | {names} | about {module_minutes(m)[0]} min |")
    L.append(f"| Capstone | {CAPSTONE['purpose']} | {CAPSTONE['name']}, step 9 planned | homework |")
    return "\n".join(L)
