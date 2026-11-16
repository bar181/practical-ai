"""build.py [--check]: writes everything that repeats the nine steps, from steps.py and the text below.

    base/PROCESS.md and base/explainer.html     the steps in detail, and the guide
    the step tables in base/AI-INSTRUCTIONS.md and level-2-files/agentic-process/SKILL.md
    the template's checks, copied from the repository's workshop/tools/ so a new project needs nothing else

    python3 _build/build.py           write both files
    python3 _build/build.py --check   write nothing; exit 1 if either file differs from what would be written

The nine steps are written once, in steps.py. The explainer follows Artifact Studio's instructions:
scrolling explainer recipe, teacher voice, the Practical AI colours. Its two pictures are in img/.
"""
import base64, pathlib, html, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from steps import STEPS, LEVELS, WHO, TOTAL_MINUTES, COACH, SKILL, coach_prompt, COACH_FILE
import re
P = pathlib.Path(__file__).resolve().parents[1]          # the project folder
b64 = lambda p: base64.b64encode((P/p).read_bytes()).decode()
puppy = b64('_build/img/inspector.jpg'); me = b64('_build/img/creator.jpg')
E = html.escape
import re
PLAN_ROWS = re.findall(r"^\| (?!Heading |---)([^|]+?) \|", (P/'level-2-files/agentic-process/template/base/plan.md').read_text(encoding='utf-8').split('\n## Status')[0], re.M)
assert 'Part' not in PLAN_ROWS and len(PLAN_ROWS) >= 10, PLAN_ROWS
for _st in STEPS:                                                  # the step 6 prompt lists the plan's own headings
    _st['prompts'] = tuple((lab, txt.replace('{PLAN_HEADINGS}', ', '.join(r[0].lower() + r[1:] for r in PLAN_ROWS))) for lab, txt in _st['prompts'])
PROMPT = coach_prompt("every Monday I turn last week's sales notes into an email for my team. I want an AI to draft it.")
stages = [
 ('Decide', 'Steps 1 to 4', 'Scope, reuse check, outside help, cost.', 'You and the AI, in a chat.', 'You name one user and one job. The AI looks for what already exists and what it would cost.', 'Expect about 25 minutes. If something existing already does the whole job, you stop here and write a guide to it.'),
 ('Design', 'Steps 5 to 7', 'Simplest design, plan and front door, review.', 'The AI drafts. You cut.', 'The folder layout is fixed. The first screen a user sees is written before the tool is. Someone else reads the plan.', 'Expect about 20 minutes. Fix the layout here: moving files after the build breaks every link that points at them.'),
 ('Build and test', 'Step 8', 'The smallest version, then a test by a stranger.', 'The AI builds. A fresh AI session tests.', 'A new session gets only your instructions and one request. It does the job and writes down every place it tripped.', 'Expect about 15 minutes for the first round, and a list of problems. The list is the point.'),
 ('Grow', 'Step 9', 'One addition at a time.', 'You approve each one.', 'Each addition is its own small change. You move up a level only when the level below is in use.', 'Expect most of the additions you planned to turn out unnecessary once you use the tool.'),
]
steps_html = '\n'.join(f'''    <li><span class="who">{html.escape(s[1])}</span><h3>{html.escape(s[0])}</h3><p class="what">{html.escape(s[2])}</p><p><b>Who:</b> {html.escape(s[3])}</p><p>{html.escape(s[4])}</p><p class="fact">{html.escape(s[5])}</p></li>''' for s in stages)
levels = [
 ('Beginner', 'Turn a job you repeat into a prompt you can reuse', 'Trial and error in a chat until something works on the day. Next week you start again.', f'About an hour the first time. You leave with a one-page plan, a prompt you can reuse and a test that tells you when it breaks.', 'The hour is an estimate: the step times added up. Not yet timed with a learner.'),
 ('Advanced', 'Build a small tool with a coding agent', 'The agent builds fast and you find the shape by rebuilding. Folders move, links break, and the first screen is written last.', 'The layout is fixed before the first file. The front page is written before the tool. A fresh session tests it before you polish.', 'What the author saw on the first two tools built this way. One author, not a study.'),
 ('Expert', 'Find the faults before your users do', 'The author reviews their own work and passes it, because they know what they meant.', 'Fresh sessions run side by side, about ten minutes each, and each returns a numbered list of where it had to guess.', 'Ten minutes is what the tests on this process took. Yours will differ.'),
]
assert TOTAL_MINUTES == 60, 'the page says "about an hour": change that wording if the step times change'
lev_html = '\n'.join(f'''    <article class="lv"><p class="tag">{l[0]}</p><h3>{html.escape(l[1])}</h3><dl><div><dt>Without it</dt><dd>{html.escape(l[2])}</dd></div><div class="with"><dt>With it</dt><dd>{html.escape(l[3])}</dd></div></dl><p class="basis">{html.escape(l[4])}</p></article>''' for l in levels)
def card(st):
    stories = ''.join(f'<li data-lvl="{LEVELS[i]}"><b class="lvl">{LEVELS[i]}</b> As {E(WHO[i])}, {E(t)}</li>' for i, t in enumerate(st['stories']))
    proof = ''.join(f'<li>{E(x)}</li>' for x in st['proof'])
    prompts = ''.join(f'<p class="lab">{E(lab)}</p><pre id="p{st["n"]}-{k}" tabindex="0">{E(txt)}</pre><button class="btn sm" type="button" data-copy="p{st["n"]}-{k}">Copy this prompt</button>' for k, (lab, txt) in enumerate(st['prompts']))
    return f'''  <details class="step"{" open" if st["n"] == 1 else ""}>
    <summary><span class="num">{st["n"]}</span><span class="nm">{E(st["name"])}</span><span class="gist">{E(st["gist"])}</span></summary>
    <div class="in">
      <p class="lab">Purpose</p><p>{E(st["purpose"])}</p>
      <p class="lab">User stories</p><ul class="stories">{stories}</ul>
      <p class="lab">What to expect</p><p>{E(st["expect"])}</p>
      <p class="lab">Proof you are done</p><ul class="proof">{proof}</ul>
      <p class="gate"><b>The gate.</b> {E(st["gate"])}</p>
      {prompts}
    </div>
  </details>'''
cards_html = '\n'.join(card(st) for st in STEPS)

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agentic Process: a guide</title>
<style>
/* Recipe: scrolling explainer  Voice: teacher  Look: the Practical AI colours */
:root{{
  --bg:#f3f5f9;--panel:#ffffff;--line:#c9d1de;--muted:#48546a;--ink:#14202e;
  --accent:#0c2340;  /* what to act on, and the dark bands */
  --hl:#ffd23f;      /* the one highlight */
  --data:#2f6fb5;    /* the data colour */
  --display:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--text:Georgia,"Iowan Old Style","Times New Roman",serif;--mono:ui-monospace,Menlo,Consolas,monospace;
  color-scheme:light;
}}
*,*::before,*::after{{box-sizing:border-box}}html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--bg);color:var(--ink);font:400 1.12rem/1.55 var(--text)}}
h1,h2,h3{{font-family:var(--display);margin:0;line-height:1.06;letter-spacing:-.02em;text-wrap:balance}}p{{margin:0}}
a{{color:var(--accent)}}:focus-visible{{outline:3px solid var(--data);outline-offset:3px}}
.wrap{{max-width:880px;margin-inline:auto;padding-inline:20px}}
.tag{{display:inline-block;font:700 .84rem/1 var(--display);background:var(--accent);color:#fff;border-radius:4px;padding:6px 9px}}
header{{padding:48px 0 0}}
h1{{font-size:clamp(2.2rem,8.6vw,4.4rem);margin-top:14px;max-width:12em}}
.lede{{margin-top:16px;max-width:34em;font-size:1.22rem;color:var(--muted)}}
section{{padding-top:60px}}
h2{{font-size:clamp(1.6rem,5.6vw,2.4rem);max-width:17em;margin-top:12px}}
section>.wrap>p,.wrap>p{{max-width:36em}}h2+p{{margin-top:12px}}section .wrap>p+p{{margin-top:12px}}
/* the analogy, very large, with one picture that moves slowly */
.analogy{{margin-top:60px;background:var(--accent);color:#fff;padding:60px 0}}
.analogy .tag{{background:var(--hl);color:var(--accent)}}
.analogy .big{{font:700 clamp(2.4rem,10vw,5rem)/1 var(--display);letter-spacing:-.03em;margin-top:14px;max-width:9em}}
.analogy p{{color:#dfe6ef;margin-top:16px;max-width:30em}}
.duo{{display:grid;gap:26px;align-items:center}}
.pic{{position:relative;border-radius:14px;overflow:hidden;aspect-ratio:4/3;background:#222}}
.pic i{{position:absolute;inset:0;background:url(data:image/jpeg;base64,{puppy}) 50% 35%/cover no-repeat;animation:pan 26s ease-in-out infinite alternate}}
.pic span{{position:absolute;left:0;right:0;bottom:0;padding:30px 16px 12px;background:linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.85));color:#fff;font:700 1.15rem/1.2 var(--display)}}
@keyframes pan{{from{{transform:scale(1)}}to{{transform:scale(1.14) translate(-1.5%,-2%)}}}}
@media(min-width:800px){{.duo{{grid-template-columns:1.1fr .9fr}}}}
/* four stages, with a diagram that stays on screen */
.stage{{position:sticky;top:0;z-index:3;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 12px;margin-top:24px}}
.stage svg{{display:block;width:100%;max-width:600px;margin-inline:auto;height:auto}}
.stage .rail{{fill:none;stroke:var(--line);stroke-width:4}}
.stage .go{{fill:none;stroke:var(--data);stroke-width:4;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:calc(1 - var(--k,0)/3);transition:stroke-dashoffset .8s cubic-bezier(.3,.7,.2,1)}}
.stage g circle{{fill:var(--panel);stroke:var(--ink);stroke-width:3;transition:fill .4s,stroke .4s}}
.stage g text{{font:700 21px var(--display);fill:var(--muted);text-anchor:middle;transition:fill .4s}}
.stage g text.n{{fill:var(--ink);font-size:20px}}
.stage g.done circle{{stroke:var(--data)}}
.stage g.now circle{{fill:var(--accent);stroke:var(--accent)}}.stage g.now text{{fill:var(--ink)}}.stage g.now text.n{{fill:#fff}}
.steps{{list-style:none;margin:0 auto;padding:0 20px;max-width:640px}}
.steps li{{min-height:min(64svh,520px);display:flex;flex-direction:column;justify-content:center;gap:9px;padding-left:14px;border-left:4px solid transparent;color:var(--muted);transition:color .4s}}
.steps li.on{{color:var(--ink);border-left-color:var(--hl)}}
.steps .who{{font:700 .9rem/1.2 var(--display)}}
.steps h3{{font-size:clamp(1.8rem,7vw,2.6rem);color:inherit}}
.steps .what{{font:700 1.08rem/1.3 var(--display)}}
.steps .fact{{background:var(--panel);border-left:5px solid var(--data);border-radius:0 10px 10px 0;padding:12px 14px;font:400 1rem/1.4 var(--display);color:var(--ink)}}
/* the nine steps, one card each */
.steplist{{margin-top:22px;display:grid;gap:10px}}
.step{{background:var(--panel);border:1px solid var(--line);border-radius:14px}}
.step summary{{list-style:none;cursor:pointer;display:flex;flex-wrap:wrap;align-items:center;gap:6px 12px;min-height:60px;padding:10px 16px;font-family:var(--display)}}
.step summary::-webkit-details-marker{{display:none}}
.step summary::before{{content:"";flex:none;width:.62em;height:.62em;border-right:3px solid var(--data);border-bottom:3px solid var(--data);rotate:-45deg;transition:rotate .2s}}
.step[open]>summary::before{{rotate:45deg}}
.step .num{{flex:none;display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--accent);color:#fff;font:700 1.05rem/1 var(--display)}}
.step .nm{{font:700 1.22rem/1.15 var(--display);color:var(--ink)}}
.step .gist{{font:400 1rem/1.3 var(--display);color:var(--muted)}}
.step .in{{padding:2px 16px 20px;display:grid;gap:8px;border-top:1px solid var(--line)}}
.step .in>p,.step li{{max-width:38em}}
.lab{{font:700 .92rem/1.2 var(--display);color:var(--accent);margin-top:12px}}
.stories,.proof{{margin:0;padding:0;list-style:none;display:grid;gap:8px}}
.stories li{{padding:10px 12px;background:var(--bg);border-radius:10px;font:400 1rem/1.45 var(--display)}}
.lvl{{display:inline-block;margin-right:6px;padding:3px 7px;border-radius:4px;background:var(--panel);border:1px solid var(--line);font:700 .8rem/1 var(--display);color:var(--accent)}}
.proof li{{position:relative;padding-left:26px;font:400 1rem/1.45 var(--display)}}
.proof li::before{{content:"";position:absolute;left:4px;top:.32em;width:.42em;height:.74em;border-right:3px solid var(--data);border-bottom:3px solid var(--data);rotate:45deg}}
.gate{{margin-top:12px;padding:12px 14px;border-left:5px solid var(--hl);background:#fff7d6;border-radius:0 10px 10px 0;font:400 1rem/1.4 var(--display)}}
.step pre{{margin:0;padding:14px;background:var(--bg);border:1px solid var(--line);border-radius:10px;white-space:pre-wrap;overflow-wrap:anywhere;font:400 .92rem/1.5 var(--mono)}}
.btn.sm{{justify-self:start;min-height:44px;margin-top:2px;padding:0 18px;font-size:.95rem;background:var(--accent);color:#fff}}
.lvpick{{margin:18px 0 0;padding:0;border:0;display:flex;flex-wrap:wrap;gap:8px;font:400 1rem/1.2 var(--display)}}.lvpick legend{{font:700 .92rem/1.2 var(--display);color:var(--accent);margin-bottom:8px}}
.lvpick label{{display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0 14px;border:1px solid var(--line);border-radius:999px;background:var(--panel);cursor:pointer}}.lvpick label:has(input:checked){{border-color:var(--accent);background:#e6ecf4;font-weight:700}}
.steplist[data-lvl="Beginner"] .stories li:not([data-lvl="Beginner"]),.steplist[data-lvl="Advanced"] .stories li:not([data-lvl="Advanced"]),.steplist[data-lvl="Expert"] .stories li:not([data-lvl="Expert"]){{display:none}}
.all{{margin-top:18px;background:var(--panel);color:var(--accent);border:2px solid var(--accent)}}
/* three levels */
.levels{{display:grid;gap:14px;margin-top:22px}}
.lv{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 18px}}
.lv h3{{font-size:1.3rem;margin-top:12px}}
.lv dl{{margin:14px 0 0;display:grid;gap:10px}}.lv dl div{{padding:12px 14px;border-radius:10px;background:var(--bg)}}
.lv dl .with{{background:#fff7d6;border-left:5px solid var(--hl)}}
.lv dt{{font:700 .9rem/1.2 var(--display)}}.lv dd{{margin:4px 0 0;font:400 1rem/1.4 var(--display)}}
.lv .basis{{margin-top:12px;font:400 .88rem/1.4 var(--display);color:var(--muted)}}
@media(min-width:900px){{.levels{{grid-template-columns:repeat(3,1fr)}}}}
/* start */
.start{{margin-top:60px;background:var(--accent);color:#fff;padding:52px 0 54px}}.start h2{{color:#fff}}.start p{{color:#dfe6ef;margin-top:10px;max-width:34em}}
.start pre{{margin:18px 0 0;padding:16px;background:#fff;color:var(--ink);border-radius:10px;white-space:pre-wrap;overflow-wrap:anywhere;font:400 .95rem/1.5 var(--mono);max-width:42em}}
.btn{{display:inline-flex;align-items:center;min-height:48px;margin-top:14px;padding:0 24px;border-radius:999px;border:0;background:var(--hl);color:var(--accent);font:700 1.05rem/1 var(--display);cursor:pointer;text-decoration:none}}
.where{{list-style:none;margin:22px 0 0;padding:0;display:grid;gap:8px;font:400 1rem/1.4 var(--display)}}.where b{{color:var(--hl)}}
details{{border-top:1px solid var(--line);padding:4px 0}}details:last-of-type{{border-bottom:1px solid var(--line)}}
summary{{cursor:pointer;min-height:48px;display:flex;align-items:center;font:700 1.05rem/1.3 var(--display)}}details p{{padding:0 0 14px;color:var(--muted)}}
.recap{{font:700 clamp(1.5rem,5.4vw,2.5rem)/1.14 var(--display);letter-spacing:-.015em;max-width:20em}}.recap mark{{background:var(--hl);padding:0 .12em}}
.me{{display:flex;gap:18px;align-items:flex-start;margin-top:40px;padding-top:30px;border-top:1px solid rgba(255,255,255,.25)}}
.me img{{flex:none;width:72px;height:72px;border-radius:50%;border:3px solid var(--hl)}}.me b{{display:block;font:700 1.25rem/1.15 var(--display)}}
.me a{{color:var(--hl);font:700 1rem/1.3 var(--display);display:inline-flex;align-items:center;min-height:44px}}
footer{{padding:26px 0 44px;font:400 .88rem/1.45 var(--display);color:var(--muted)}}
@media (prefers-reduced-motion:reduce){{.step summary::before{{transition:none}}.pic i{{animation:none}}.stage .go,.steps li{{transition:none}}}}
</style>
</head>
<body>
<main>
<header class="wrap">
  <span class="tag">A guide to Agentic Process</span>
  <h1>How do you stop an AI building the wrong thing three times?</h1>
  <p class="lede">An AI agent will build whatever you ask, quickly and with confidence. That is how people end up with the wrong tool, built well. This guide is the order of work that stops it: nine steps, each with a purpose, a proof and a prompt you can paste.</p>
</header>

<div class="analogy"><div class="wrap duo">
  <div><span class="tag">Think of it as</span><p class="big">A building site with an inspector.</p>
    <p>You agree the drawing before you pour concrete. You put up the frame before you choose curtains. An inspector signs off each stage before the next one starts.</p>
    <p>Here the stages are nine steps, the sign-off is a plain question called a gate, and the inspector at the end is an AI that has never seen your work.</p></div>
  <div class="pic"><i role="img" aria-label="A puppy in a plaid suit and tie, sitting upright and looking serious."></i><span>The inspector. Friendly, brief, and nothing gets past.</span></div>
</div></div>

<section class="wrap"><span class="tag">What it is</span><h2>Nine steps in four stages. Scroll, and the diagram keeps your place.</h2>
  <p>Every step ends at a gate: a question you must be able to answer before you go on. The AI does the drafting. You make the decisions.</p></section>
<div class="walk">
<div class="stage" id="stage"><svg viewBox="0 0 600 124" role="img" aria-label="Four stages in a row: decide, design, build and test, grow. The current stage is highlighted.">
  <path class="rail" d="M70,42 H530"/><path class="go" pathLength="1" d="M70,42 H530"/>
  <g><circle cx="70" cy="42" r="26"/><text class="n" x="70" y="49">1-4</text><text x="70" y="108">Decide</text></g>
  <g><circle cx="223" cy="42" r="26"/><text class="n" x="223" y="49">5-7</text><text x="223" y="108">Design</text></g>
  <g><circle cx="377" cy="42" r="26"/><text class="n" x="377" y="49">8</text><text x="377" y="108">Build, test</text></g>
  <g><circle cx="530" cy="42" r="26"/><text class="n" x="530" y="49">9</text><text x="530" y="108">Grow</text></g></svg></div>
<ol class="steps">
{steps_html}
</ol>
</div>

<section class="wrap" aria-labelledby="steps-h"><span class="tag">Step by step</span><h2 id="steps-h">The nine steps, one at a time</h2>
  <p>Open a step to see why it exists, who it helps, what you should be holding when it is done, and a prompt to paste into your chatbot. The times are estimates and add up to about an hour for steps 1 to 8.</p>
  <fieldset class="lvpick" id="lvpick" hidden><legend>Show user stories for</legend>
    <label><input type="radio" name="lv" value="" checked> Every level</label><label><input type="radio" name="lv" value="Beginner"> Beginner</label><label><input type="radio" name="lv" value="Advanced"> Advanced</label><label><input type="radio" name="lv" value="Expert"> Expert</label></fieldset>
  <button class="btn all" type="button" id="all" aria-expanded="false">Open all nine steps</button>
  <div class="steplist">
{cards_html}
  </div>
</section>

<section class="wrap"><span class="tag">Why you should care</span><h2>What changes at your level</h2>
  <p>The same nine steps, used three ways. Each card says what the comparison rests on.</p>
  <div class="levels">
{lev_html}
  </div>
</section>

<section class="wrap"><span class="tag">A harder case</span><h2>What if nobody is watching?</h2>
  <p>An agent working alone will pass its own work. So the Expert level adds three things it cannot talk its way past.</p>
  <p><b>Gates a script runs.</b> Each is one command that fails when the thing is not true: the layout is wrong, a link is broken, the template does not produce a valid folder.</p>
  <p><b>The fresh-run test.</b> A new session, your instructions, one request, and a log of every place it had to guess.</p>
  <p><b>A score sheet.</b> Ten measures, each with what 80 looks like. A score needs evidence you can point to. An AI testing the tool is a test, not real use.</p>
</section>

<div class="start"><div class="wrap">
  <span class="tag" style="background:var(--hl);color:var(--accent)">Quick start</span>
  <h2 style="margin-top:12px">Try it on your own idea in five minutes</h2>
  <p>Paste this into the chatbot you already use. Change the last line to a job you repeat. Five minutes is an estimate.</p>
  <pre id="prompt" tabindex="0">{html.escape(PROMPT)}</pre>
  <button class="btn" type="button" id="copy">Copy the prompt</button>
  <p>If your chatbot says it cannot open the link, open <a href="https://github.com/bar181/practical-ai/blob/main/projects/agentic-process/base/AI-INSTRUCTIONS.md" style="color:#fff">the coach on GitHub</a>, copy all of it, and paste it in before your idea.</p>
  <ul class="where">
    <li><b>Beginner:</b> the coach above, or the nine prompts one at a time. Nothing to install.</li>
    <li><b>Advanced:</b> <a href="https://github.com/bar181/practical-ai/tree/main/projects/agentic-process/level-2-files" style="color:#fff">one skill folder</a> to copy into your coding agent. It works in any repository.</li>
    <li><b>Expert:</b> <a href="https://github.com/bar181/practical-ai/tree/main/projects/agentic-process/level-3-files" style="color:#fff">gates, the fresh-run test and the score sheet</a>.</li>
    <li><b>Teaching or learning it properly:</b> <a href="https://raw.githack.com/bar181/practical-ai/main/projects/agentic-process/base/course.html" style="color:#fff">the course</a>: how this project works, why each step exists and how to run it, told visually.</li>
  </ul>
  <a class="btn" href="https://github.com/bar181/practical-ai">Open Practical AI on GitHub</a>
</div></div>

<section class="wrap"><span class="tag">Check yourself</span><h2>Three questions before you go</h2>
  <details><summary>Your reuse check finds a free tool that already does the whole job. What now?</summary><p>Stop. Write a short guide to that tool. The second gate exists to save you from building what already exists.</p></details>
  <details><summary>Why fix the folder layout at step 5, before anything is built?</summary><p>Because every file you write afterwards points at other files. Moving them later breaks those links, and you pay for the move again each time the shape changes.</p></details>
  <details><summary>A fresh session finishes the job and its log lists twelve problems. Did the test pass?</summary><p>It passed the gate, and it gave you the next hour's work. Fix first every point that appears in two or more logs, then every blocking point. Then run it again.</p></details>
</section>

<section class="wrap"><span class="tag">So</span>
  <p class="recap" style="margin-top:14px">Build like a site with an inspector: <mark>one step, one gate</mark>, and let a stranger test it before a person sees it.</p>
</section>

<div class="start" style="margin-top:56px"><div class="wrap">
  <div class="me" style="margin-top:0;padding-top:0;border-top:0"><img src="data:image/jpeg;base64,{me}" width="72" height="72" alt="Bradley Ross">
    <div><b>Made by Bradley Ross</b><p style="margin-top:6px">Bradley is an agentic AI architect and developer for businesses of every size, from start-up to enterprise. He builds and teaches practical AI.</p><a href="https://www.linkedin.com/in/bradaross/">Connect with Bradley on LinkedIn</a></div></div>
</div></div>
</main>
<footer class="wrap">Made on 16 November 2026 by following Artifact Studio's instructions. Recipe: scrolling explainer. Voice: teacher. Look: the Practical AI colours. The nine steps are grouped into four stages in the diagram because the recipe allows seven stages at most. Every time on this page is an estimate. Nobody outside its author has yet built a tool with this process. The puppy was made by the repository's owner with an AI image tool.</footer>
<script>
/* Everything above reads without this script. It adds three things: the diagram that follows your scrolling, the copy buttons, and the button that opens every step. */
(()=>{{const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const stage=document.getElementById('stage'),gs=[...stage.querySelectorAll('g')],steps=[...document.querySelectorAll('.steps li')];
  const set=k=>{{stage.style.setProperty('--k',k);gs.forEach((g,i)=>{{g.classList.toggle('done',i<k);g.classList.toggle('now',i===k)}});steps.forEach((s,i)=>s.classList.toggle('on',i===k))}};
  if('IntersectionObserver' in window){{const io=new IntersectionObserver(es=>{{for(const e of es)if(e.isIntersecting)set(steps.indexOf(e.target))}},{{rootMargin:'-50% 0px -45% 0px'}});steps.forEach(s=>io.observe(s));}}
  set(0);
  const copy=(btn,id)=>btn.addEventListener('click',async()=>{{const was=btn.textContent;try{{await navigator.clipboard.writeText(document.getElementById(id).textContent);btn.textContent='Copied'}}catch(e){{btn.textContent='Select the text and copy it'}}setTimeout(()=>btn.textContent=was,2200)}});
  copy(document.getElementById('copy'),'prompt');document.querySelectorAll('[data-copy]').forEach(b=>copy(b,b.dataset.copy));
  /* one button opens or closes every step. Its state follows the cards, which also open one by one */
  const all=document.getElementById('all'),cards=[...document.querySelectorAll('details.step')];
  const sync=()=>{{const open=cards.every(d=>d.open);all.setAttribute('aria-expanded',open);all.textContent=open?'Close all nine steps':'Open all nine steps'}};
  all.addEventListener('click',()=>{{const open=all.getAttribute('aria-expanded')!=='true';cards.forEach(d=>d.open=open);sync()}});
  cards.forEach(d=>d.addEventListener('toggle',sync));sync();
  /* show only one level's user stories. Without the script every level shows */
  const pick=document.getElementById('lvpick'),list=document.querySelector('.steplist');pick.hidden=false;
  pick.addEventListener('change',e=>{{if(e.target.value)list.dataset.lvl=e.target.value;else delete list.dataset.lvl}});
}})();
</script>
</body>
</html>
'''

def process_md():
    L = ["<!-- Written by _build/build.py from _build/steps.py. Change the source, not this file. -->",
         "# The nine steps in detail", "",
         "Nine steps from an idea to a tool someone else can try. Each step ends at a gate: a plain",
         "question you must be able to answer before you go on. For every step this page gives the purpose,",
         "a user story for each level, what to expect, what proves the step is done, and a prompt to paste.", "",
         "**Think of it as** building a deck in the garden. Decide what it is for. Check whether a kit",
         "already exists. Price the wood. Pick the spot. Draw it. Have someone check the drawing. Build the",
         "smallest platform you can stand on. Extend it only once you are using it.", "",
         "**Two ways to use this page.** Paste the [build coach](AI-INSTRUCTIONS.md) into a chatbot and it",
         "walks you through all nine. Or take the steps one at a time with the prompts below.", "",
         "## The steps at a glance", "",
         "| # | Step | You write down | The gate | Time |", "| --- | --- | --- | --- | --- |"]
    for st in STEPS:
        anchor = f"{st['n']}-" + st['name'].lower().replace(' ', '-')
        L.append(f"| {st['n']} | [**{st['name']}**](#{anchor}) | {st['writes']} | {st['gate']} | {('about ' + str(st['minutes']) + ' min') if st['minutes'] else 'repeats'} |")
    L += ["", f"Steps 1 to 8 add up to about {TOTAL_MINUTES} minutes the first time. Every time on this page is an estimate: nobody",
          "has yet been timed.", "",
          "**A small job can take the short path:** steps 1, 6 and 8 in full, steps 2 to 5 in a line each, step 7 folded into the test, and step 9 left open.",
          "The coach offers it when the job is one person turning one kind of input into one result in a chat.", "",
          "## Who does what", "",
          "| Step | The AI does | You do |", "| --- | --- | --- |",
          "| 1 to 4 | Asks the questions, searches for what exists, lists costs | Answer honestly. Say no to anything outside the one job |",
          "| 5 to 6 | Drafts the design, the plan and the first screen | Cut it down. Fix the layout and do not change it later |",
          "| 7 | Plays the reviewer if no person is free, in a fresh session | Find a real person if you can |",
          "| 8 | Builds, and runs the fresh-session test | Read what the test tripped on. Decide what to fix |",
          "| 9 | Makes each addition | Approve each one. Use the tool yourself |", ""]
    for st in STEPS:
        L += [f"## {st['n']}. {st['name']}", "", f"**Purpose.** {st['purpose']}", "", "**User stories**", ""]
        L += [f"- **{LEVELS[i]}.** As {WHO[i]}, {t}" for i, t in enumerate(st['stories'])]
        L += ["", f"**What to expect.** {st['expect']}", "", "**Proof you are done**", ""]
        L += [f"- {x}" for x in st['proof']]
        L += ["", f"**The gate.** {st['gate']}", ""]
        if COACH[st['n']][1]: L += [f"*In a chat with the coach:* {COACH[st['n']][1]}.", ""]
        for lab, txt in st['prompts']:
            L += [f"**{lab}**", "", "```", txt, "```", ""]
    plan = (SKILL_DIR/'template/base/plan.md').read_text(encoding='utf-8').replace('{{TITLE}}', '[name of the tool]')
    plan = plan.split('\n## Status')[0].strip().split('\n', 1)[1].strip()
    L += ["## The one-page plan", "",
          "Fill this in as you go. Copy it into a document, or ask your chatbot to fill it in from your",
          "answers. An agent finds the same template in each new project folder as `base/plan.md`.", "",
          "```", "Plan: [name of the tool]", "", plan, "```", ""]
    L += ["## Five rules that save the most time", "",
          "1. **Name the wow first.** Decide the one thing that makes people stop, and build it first.",
          "2. **Fix the layout before you build.** Moving files later breaks every link that points at them.",
          "3. **Test in a fresh session early.** A stranger finds what the author cannot see.",
          "4. **Say what a result really is.** A page built by hand is a reference. A page a chat made is an example.",
          "5. **One addition, one change request.** Small changes get reviewed. Big ones get waved through.", ""]
    return "\n".join(L)

from pages import north_star_html
from course_page import course_html
GH = "https://raw.githack.com/bar181/practical-ai/main/projects/agentic-process/base/"

def nine_steps_svg():
    """The README picture: nine steps in a row with a gate after each. A marker walks them and waits at each gate."""
    W, x0, dx = 820, 58, 88
    split = {'Reuse check': ('Reuse', 'check'), 'Outside help': ('Outside', 'help'), 'Simplest design': ('Simplest', 'design'),
             'Plan and front door': ('Plan and', 'front door'), 'Build and test': ('Build and', 'test')}
    stages = [('Decide', 1, 4), ('Design', 5, 7), ('Test', 8, 8), ('Grow', 9, 9)]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 270" role="img" aria-labelledby="t d" font-family="system-ui,-apple-system,\'Segoe UI\',Roboto,Helvetica,Arial,sans-serif">',
           '<title id="t">Nine steps, a gate after each</title>',
           '<desc id="d">Nine steps in a row, from scope to grow, grouped into four stages: decide, design, test and grow. A marker moves along them and stops at the gate after each step. The eighth step, build and test, is highlighted.</desc>',
           '<!-- Written by projects/agentic-process/_build/build.py from _build/steps.py. -->',
           '<style>', '.mk{animation:walk 27s infinite}']
    keys = []
    for i in range(9):
        a, b = i * 100 / 9, (i + .55) * 100 / 9
        keys += [f'{a:.2f}%{{transform:translate({i*dx}px,0)}}', f'{b:.2f}%{{transform:translate({i*dx + 34}px,0)}}']
    keys.append(f'100%{{transform:translate({8*dx + 34}px,0)}}')
    out += ['@keyframes walk{' + ''.join(keys) + '}', '@media (prefers-reduced-motion:reduce){.mk{animation:none;transform:translate(' + str(7*dx) + 'px,0)}}', '</style>',
            f'<rect width="{W}" height="270" rx="20" fill="#0c2340"/>']
    for name, a, b in stages:
        xa, xb = x0 + (a-1)*dx - 30, x0 + (b-1)*dx + 30
        out += [f'<rect x="{xa}" y="30" width="{xb-xa}" height="30" rx="15" fill="#17365f"/>', f'<text x="{(xa+xb)/2}" y="51" fill="#ffd23f" font-size="16" font-weight="700" text-anchor="middle">{name}</text>']
    out.append(f'<path d="M{x0},120 H{x0 + 8*dx + 34}" stroke="#2f5a8f" stroke-width="4"/>')
    for st in STEPS:
        i = st['n'] - 1; cx = x0 + i*dx; hi = st['n'] == 8
        out += [f'<circle cx="{cx}" cy="120" r="24" fill="{"#ffd23f" if hi else "#1d4273"}" stroke="{"#ffd23f" if hi else "#5d86c0"}" stroke-width="3"/>',
                f'<text x="{cx}" y="127" fill="{"#0c2340" if hi else "#fff"}" font-size="20" font-weight="800" text-anchor="middle">{st["n"]}</text>',
                f'<rect x="{cx + 34 - 7}" y="113" width="14" height="14" fill="#ffd23f" transform="rotate(45 {cx + 34} 120)"/>']
        l1, l2 = split.get(st['name'], (st['name'], ''))
        col = '#ffd23f' if hi else '#d5e2f5'
        out.append(f'<text x="{cx}" y="174" fill="{col}" font-size="15" font-weight="{"700" if hi else "500"}" text-anchor="middle">{l1}</text>')
        if l2: out.append(f'<text x="{cx}" y="193" fill="{col}" font-size="15" font-weight="{"700" if hi else "500"}" text-anchor="middle">{l2}</text>')
    out += [f'<g class="mk"><circle cx="{x0}" cy="84" r="9" fill="#fff"/><path d="M{x0-6},94 L{x0},104 L{x0+6},94 Z" fill="#fff"/></g>',
            f'<text x="{x0 - 30}" y="238" fill="#d5e2f5" font-size="16"><tspan fill="#ffd23f">&#9670;</tspan> a gate: a question you answer before you go on</text>',
            f'<text x="{W - 30}" y="238" fill="#ffd23f" font-size="16" font-weight="700" text-anchor="end">Step 8: a stranger tests it</text>', '</svg>']
    return '\n'.join(out) + '\n'

SKILL_DIR = P/'level-2-files/agentic-process'
TOOLS = P.parents[1]/'workshop/tools'
def cell(x): return x.replace('|', '\\|')
def coach_table():
    rows = ["| # | Step | What you do | Gate question |", "| --- | --- | --- | --- |"]
    for st in STEPS:
        do, note = COACH[st['n']]
        rows.append(f"| {st['n']} | {st['name']} | {cell(do)} | \"{cell(st['gate'])}\"" + (f" {cell(note)}." if note else "") + " |")
    return "\n".join(rows)
def skill_table():
    rows = ["| # | Step | You do | Gate | Check |", "| --- | --- | --- | --- | --- |"]
    for st in STEPS:
        do, check = SKILL[st['n']]
        rows.append(f"| {st['n']} | {st['name']} | {cell(do)} | {cell(st['gate'])} | {cell(check) if check else 'Your answer, written in the plan'} |")
    return "\n".join(rows)
def fill(path, table, name='steps', text=None, inline=False):
    text = text if text is not None else path.read_text(encoding='utf-8')
    sep = '' if inline else '\n'
    pat = r"(<!-- " + name + r":start[^>]*-->)" + ("" if inline else r"\n") + r".*?(<!-- " + name + r":end -->)"
    assert re.search(pat, text, flags=re.S), f'no {name} markers in {path}'
    return re.sub(pat, lambda m: m.group(1) + sep + table + sep + m.group(2), text, flags=re.S)

outputs = {P/'base/explainer.html': page, P/'base/PROCESS.md': process_md(),
           P/'base/north-star.html': north_star_html(me, 'explainer.html', 'course.html'), P/'base/course.html': course_html(me, puppy, 'north-star.html', 'explainer.html'),
           P/'base/AI-INSTRUCTIONS.md': fill(P/'base/AI-INSTRUCTIONS.md', '. '.join(PLAN_ROWS) + '.', 'plan', fill(P/'base/AI-INSTRUCTIONS.md', coach_table()), inline=True),
           P/'README.md': fill(P/'README.md', '```\n' + PROMPT + '\n```', 'prompt'),
           P/'_build/img/nine-steps.svg': nine_steps_svg(),
           SKILL_DIR/'SKILL.md': fill(SKILL_DIR/'SKILL.md', skill_table())}
for name in ('gates.py', 'check_project.py', 'check_links.py', 'check_filled.py'):
    outputs[SKILL_DIR/'template/_build/checks'/name] = (TOOLS/name).read_text(encoding='utf-8')
if '--check' in sys.argv:
    stale = [str(f.relative_to(P)) for f, text in outputs.items() if not f.exists() or f.read_text(encoding='utf-8') != text]
    sys.exit(('Out of date, run python3 _build/build.py: ' + ', '.join(stale)) if stale else print(f'build: all {len(outputs)} files are up to date'))
for f, text in outputs.items():
    f.parent.mkdir(parents=True, exist_ok=True); f.write_text(text, encoding='utf-8'); print(f'{f.relative_to(P)}: {len(text)//1024} KB')
