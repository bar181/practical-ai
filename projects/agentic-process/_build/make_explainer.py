"""Writes ../base/explainer.html. Run it after you change the text below: python3 _build/make_explainer.py
The page follows Artifact Studio's instructions: scrolling explainer recipe, teacher voice, the Practical AI colours."""
import base64, pathlib, html
R = pathlib.Path(__file__).resolve().parents[3]
b64 = lambda p: base64.b64encode((R/p).read_bytes()).decode()
puppy = b64('projects/artifact-studio/_build/photos/puppy.jpg'); me = b64('projects/artifact-studio/_build/photos/creator-144.jpg')
PROMPT = "Read the build coach at https://raw.githubusercontent.com/bar181/practical-ai/main/projects/agentic-process/base/AI-INSTRUCTIONS.md and follow it.\n\nMy idea: every Monday I turn last week's sales notes into an email for my team. I want an AI to draft it."
stages = [
 ('Decide', 'Steps 1 to 4', 'Scope, reuse check, outside help, cost.', 'You and the AI, in a chat.', 'You name one user and one job. The AI looks for what already exists and what it would cost.', 'If something existing already does the whole job, you stop here and write a guide to it.'),
 ('Design', 'Steps 5 to 7', 'Simplest design, plan and front door, review.', 'The AI drafts. You cut.', 'The folder layout is fixed. The first screen a user sees is written before the tool is. Someone else reads the plan.', 'Project one changed its folder layout four times. This stage exists so that happens zero times.'),
 ('Build and test', 'Step 8', 'The smallest version, then a test by a stranger.', 'The AI builds. A fresh AI session tests.', 'A new session gets only your instructions and one request. It does the job and writes down every place it tripped.', 'Thirteen such sessions ran in parallel on project one. Each took 5 to 11 minutes.'),
 ('Grow', 'Step 9', 'One addition at a time.', 'You approve each one.', 'Each addition is its own small change. You move up a level only when the level below is in use.', 'Project one put three additions into one change of more than 60 commits. Nobody could review it.'),
]
steps_html = '\n'.join(f'''    <li><span class="who">{html.escape(s[1])}</span><h3>{html.escape(s[0])}</h3><p class="what">{html.escape(s[2])}</p><p><b>Who:</b> {html.escape(s[3])}</p><p>{html.escape(s[4])}</p><p class="fact">{html.escape(s[5])}</p></li>''' for s in stages)
levels = [
 ('Beginner', 'Turn a job you repeat into a prompt you can reuse', 'An afternoon of trial and error in a chat. A prompt that worked on the day.', 'About 45 minutes with the coach. A one-page plan, a prompt and a test.', 'An estimate. Not yet timed with a real learner.'),
 ('Advanced', 'Build a small tool with a coding agent', 'Project one: 3 days, 4 folder layouts, one change of more than 60 commits.', 'Project two: one sitting, one layout, by following the steps.', 'Measured on two projects by one author. Project two is the simpler tool.'),
 ('Expert', 'Find the faults before your users do', 'Two days of the author reviewing their own work found 2 faults in the instructions.', '13 fresh sessions in parallel logged about 230 points of friction and one broken server.', 'Measured on project one, 16 November 2026.'),
]
lev_html = '\n'.join(f'''    <article class="lv"><p class="tag">{l[0]}</p><h3>{html.escape(l[1])}</h3><dl><div><dt>Without it</dt><dd>{html.escape(l[2])}</dd></div><div class="with"><dt>With it</dt><dd>{html.escape(l[3])}</dd></div></dl><p class="basis">{html.escape(l[4])}</p></article>''' for l in levels)
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
section>.wrap>p,.wrap>p{{max-width:36em}}section .wrap>p+p{{margin-top:12px}}
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
/* the worked example */
figure{{margin:22px 0 0;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 18px 16px}}
.bars{{display:grid;gap:12px;font:400 1rem/1.25 var(--display)}}.bars div{{display:grid;gap:4px}}
.bars i{{display:flex;align-items:center;justify-content:flex-end;min-width:2.6em;width:var(--v);height:28px;border-radius:0 6px 6px 0;background:var(--data);font-style:normal}}
.bars .cmp i{{background:var(--line)}}.bars b{{padding-right:9px;color:#fff;font-weight:700}}.bars .cmp b{{color:var(--ink)}}
.go .bars i{{width:2.6em;transition:width 1s cubic-bezier(.2,.8,.2,1);transition-delay:calc(var(--i,0)*120ms)}}.go .bars.in i{{width:var(--v)}}
figcaption{{margin-top:14px;font:400 .88rem/1.4 var(--display);color:var(--muted)}}
.so{{margin-top:16px;padding:14px 16px;border-left:5px solid var(--data);background:var(--panel);border-radius:0 10px 10px 0;max-width:38em}}.so b{{font-family:var(--display)}}
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
@media (prefers-reduced-motion:reduce){{.pic i{{animation:none}}.stage .go,.steps li{{transition:none}}.go .bars i{{width:var(--v);transition:none}}}}
</style>
</head>
<body>
<main>
<header class="wrap">
  <span class="tag">A guide to Agentic Process</span>
  <h1>How do you stop an AI building the wrong thing three times?</h1>
  <p class="lede">An AI agent will build whatever you ask, quickly and with confidence. The first tool in this repository changed its folder layout four times before its shape was right. This guide is the order of work that came out of that.</p>
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
  <g><circle cx="377" cy="42" r="26"/><text class="n" x="377" y="49">8</text><text x="377" y="108">Test</text></g>
  <g><circle cx="530" cy="42" r="26"/><text class="n" x="530" y="49">9</text><text x="530" y="108">Grow</text></g></svg></div>
<ol class="steps">
{steps_html}
</ol>
</div>

<section class="wrap"><span class="tag">A worked example</span><h2>One fresh session found three times as many faults as the author.</h2>
  <p>On project one, the author reviewed the instructions for two days. Then a new AI session, given only those instructions and one request, was asked to do the job and say where it tripped.</p>
  <figure>
    <div class="bars" role="list" aria-label="Faults found in the instructions of project one">
      <div class="cmp" role="listitem" style="--i:0"><span>Found by the author, over two days</span><i style="--v:33.3%"><b>2</b></i></div>
      <div role="listitem" style="--i:1"><span>Found by one fresh session</span><i style="--v:100%"><b>6</b></i></div>
    </div>
    <figcaption>Unit: contradictions, where the instructions told the AI two different things. Source: this repository's final review, 15 and 16 November 2026.</figcaption>
  </figure>
  <p class="so"><b>So what.</b> You cannot see your own gaps, because you know what you meant. Step 8 is the only step that finds them, so it comes before any polish.</p>
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
  <ul class="where">
    <li><b>Beginner:</b> the coach above. Nothing to install.</li>
    <li><b>Advanced:</b> the skill and the project template, in level-2-files.</li>
    <li><b>Expert:</b> gates, the fresh-run test and the score sheet, in level-3-files.</li>
  </ul>
  <a class="btn" href="https://github.com/bar181/practical-ai">Open Practical AI on GitHub</a>
</div></div>

<section class="wrap"><span class="tag">Check yourself</span><h2>Three questions before you go</h2>
  <details><summary>Your reuse check finds a free tool that already does the whole job. What now?</summary><p>Stop. Write a short guide to that tool. The second gate exists to save you from building what already exists.</p></details>
  <details><summary>Why fix the folder layout at step 5, before anything is built?</summary><p>Because every file you write afterwards points at other files. Moving them later breaks those links and costs a day. Project one did it four times.</p></details>
  <details><summary>A fresh session finishes the job and its log lists twelve problems. Did the test pass?</summary><p>It passed the gate, and it gave you the next hour's work. Fix the points that appear in more than one log first. Then run it again.</p></details>
</section>

<section class="wrap"><span class="tag">So</span>
  <p class="recap" style="margin-top:14px">Build like a site with an inspector: <mark>one step, one gate</mark>, and let a stranger test it before a person sees it.</p>
</section>

<div class="start" style="margin-top:56px"><div class="wrap">
  <div class="me" style="margin-top:0;padding-top:0;border-top:0"><img src="data:image/jpeg;base64,{me}" width="72" height="72" alt="Bradley Ross">
    <div><b>Made by Bradley Ross</b><p style="margin-top:6px">Bradley is an agentic AI architect and developer for businesses of every size, from start-up to enterprise. He builds and teaches practical AI.</p><a href="https://www.linkedin.com/in/bradaross/">Connect with Bradley on LinkedIn</a></div></div>
</div></div>
</main>
<footer class="wrap">Made on 16 November 2026 by following Artifact Studio's instructions. Recipe: scrolling explainer. Voice: teacher. Look: the Practical AI colours. The nine steps are grouped into four stages because the recipe allows seven stages at most. Figures marked as measured come from this repository's history, on two projects by one author. The Beginner figure is an estimate. The puppy was made by the repository's owner with an AI image tool.</footer>
<script>
/* Everything above reads without this script. It adds three things: the diagram that follows your scrolling, bars that grow, and the copy button. */
(()=>{{const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const stage=document.getElementById('stage'),gs=[...stage.querySelectorAll('g')],steps=[...document.querySelectorAll('.steps li')];
  const set=k=>{{stage.style.setProperty('--k',k);gs.forEach((g,i)=>{{g.classList.toggle('done',i<k);g.classList.toggle('now',i===k)}});steps.forEach((s,i)=>s.classList.toggle('on',i===k))}};
  if('IntersectionObserver' in window){{const io=new IntersectionObserver(es=>{{for(const e of es)if(e.isIntersecting)set(steps.indexOf(e.target))}},{{rootMargin:'-50% 0px -45% 0px'}});steps.forEach(s=>io.observe(s));
    if(!reduce){{document.documentElement.classList.add('go');const bo=new IntersectionObserver((es,ob)=>{{for(const e of es)if(e.isIntersecting){{e.target.classList.add('in');ob.unobserve(e.target)}}}},{{threshold:.3}});document.querySelectorAll('.bars').forEach(b=>bo.observe(b))}}}}
  set(0);
  const btn=document.getElementById('copy');btn.addEventListener('click',async()=>{{try{{await navigator.clipboard.writeText(document.getElementById('prompt').textContent);btn.textContent='Copied'}}catch(e){{btn.textContent='Select the text and copy it'}}setTimeout(()=>btn.textContent='Copy the prompt',2200)}});
}})();
</script>
</body>
</html>
'''
out = R/'projects/agentic-process/base/explainer.html'; out.write_text(page); print('explainer:', len(page)//1024, 'KB -> base/explainer.html')
