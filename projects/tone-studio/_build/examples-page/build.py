"""Build base/examples/index.html: the seven tone examples on one page.

Run from anywhere:  python3 projects/tone-studio/_build/examples-page/build.py
It reads each tone's landing.html (embedded as it is), post.md and notes.md, and the word counts
in base/examples/README.md, so the page never drifts from the examples. Edit this file, not the
output.
"""
import html, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
EX = HERE.parent.parent / "base" / "examples"
OUT = EX / "index.html"
RAW = "https://raw.githubusercontent.com/bar181/practical-ai/main/projects"
GH = "https://github.com/bar181/practical-ai/blob/main/projects/tone-studio/base/examples"

# slug, name, reader should, opens with, Artifact Studio look, look in plain words
TONES = [
    ("visionary", "Visionary", "feel that something new is possible", "one painful number, then the idea in a few words",
     "Keynote", "black, one typeface, enormous type, one idea per screen"),
    ("storyteller", "Storyteller", "see themselves in the problem", "a moment with a time and a place",
     "Storyteller", "colours from the photograph, a large serif and slow push-ins"),
    ("emotional", "Emotional", "feel something and remember it", "a true memory, in the first person",
     "Personal story", "faded film, warm, first person"),
    ("explainer", "Explainer", "understand how it works", "a question, then an everyday analogy",
     "Teacher", "white with one highlight colour, monospace for the worked example"),
    ("practical-instructor", "Practical instructor", "do it today", "the idea in one sentence, then timed steps",
     "Practical instructor", "a field guide: two colours, tick boxes, numbered timed steps"),
    ("analyst", "Analyst", "be convinced by evidence", "the conclusion as the title",
     "Analyst", "quiet, one data colour, grey for comparison, a source under each number"),
    ("executive-brief", "Executive brief", "decide in three minutes", "the decision, then the options",
     "Executive brief", "a paper memo, serif, one accent, no images and no motion"),
]

def esc(s):
    return html.escape(s, quote=True)

def inline(s):
    s = esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s

def md(text):
    """A small Markdown subset: paragraphs, bold, code, links, lists and code blocks."""
    out, para, lst, code, in_code = [], [], None, [], False
    def flush():
        nonlocal para, lst
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
        if lst:
            tag = lst[0]; out.append(f"<{tag}>" + "".join(f"<li>{inline(i)}</li>" for i in lst[1]) + f"</{tag}>"); lst = None
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            if in_code:
                out.append("<pre tabindex=\"0\"><code>" + esc("\n".join(code)) + "</code></pre>"); code = []; in_code = False
            else:
                flush(); in_code = True
            continue
        if in_code:
            code.append(line); continue
        m = re.match(r"\s*(?:(-|\*)|(\d+)\.)\s+(.*)", line)
        if m:
            tag = "ul" if m.group(1) else "ol"
            if para: flush()
            if lst and lst[0] != tag: flush()
            if not lst: lst = (tag, [])
            lst[1].append(m.group(3)); continue
        if not line.strip():
            flush(); continue
        if lst: flush()
        para.append(line.strip())
    flush()
    return "\n".join(out)

def post(slug):
    t = (EX / slug / "post.md").read_text()
    title = t.split("\n", 1)[0].lstrip("# ").split(":", 1)[-1].strip()
    words = re.search(r"\*\*Words:\*\*\s*(\d+)", t)
    body = "\n".join(re.sub(r"^> ?", "", l) for l in t.split("\n") if l.startswith(">"))
    return title[0].upper() + title[1:], words.group(1) if words else "", md(body)

def story(slug):
    t = (EX / slug / "notes.md").read_text()
    part = t.split("## How the order follows the tone", 1)[1].strip()
    return inline(" ".join(part.split()))

def page_words():
    words = {}
    for line in (EX / "README.md").read_text().split("\n"):
        m = re.match(r"\| \*\*(.+?)\*\* \|.*?\| about (\d+) \|", line)
        if m: words[m.group(1)] = m.group(2)
    return words

def post_phrase(title):
    """'LinkedIn post' -> 'a LinkedIn post'; 'Blog article' -> 'a blog article'; keeps names capitalised."""
    t = title if title.split()[0] in ("LinkedIn", "Facebook") else title[0].lower() + title[1:]
    return t if t.startswith(("a ", "an ")) else "a " + t

def prompt(name, look_voice, look, post_title):
    return (
        "Read the instructions at these two links and follow them for the rest of this chat:\n"
        f"{RAW}/tone-studio/base/SKILL.md\n"
        f"{RAW}/artifact-studio/base/AI-INSTRUCTIONS.md\n\n"
        f"First, with Tone Studio, write my content in the {name.lower()} tone as a landing page "
        f"(200 to 400 words) and {post_phrase(post_title)}. Show me the facts check.\n"
        f"Then, with Artifact Studio, build the landing page as one cinematic HTML file in the "
        f"{look_voice.lower()} look: {look}.\n"
        "Use only the facts I give you. Mark anything missing as [needs: ...].\n\n"
        "My content:\n[Paste what it is, who it is for, the facts and any real quotes]"
    )

ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'

def build():
    words = page_words()
    nav = "".join(f'<li><a href="#{s}">{n}</a></li>' for s, n, *_ in TONES)
    toc = "".join(
        f'<li><a href="#{s}"><b>{n}</b><span>For a reader who should {r}.</span></a></li>' for s, n, r, *_ in TONES)
    secs = []
    for i, (s, n, reader, opens, voice, look) in enumerate(TONES, 1):
        ptitle, pwords, pbody = post(s)
        pid = f"prompt-{s}"
        secs.append(f'''
<section class="tone" id="{s}" aria-labelledby="{s}-h">
  <h2 id="{s}-h">{n}</h2>
  <p class="lead">Your reader should {reader}. It opens with {opens}.</p>
  <div class="browser">
    <div class="browser-bar"><span>{n} landing page, about {words.get(n, "")} words</span><a href="{s}/landing.html">Open it full screen</a></div>
    <iframe src="{s}/landing.html" title="The {n.lower()} landing page, live" loading="lazy"></iframe>
  </div>
  <div class="cols">
    <div>
      <h3>The story order</h3>
      <p>{story(s)}</p>
      <p class="small"><a href="{GH}/{s}/notes.md">The facts check</a>: every fact on the page and in the post, against the source.</p>
    </div>
    <div>
      <h3>The post: {esc(ptitle)}, {pwords} words</h3>
      <div class="post">{pbody}</div>
    </div>
  </div>
  <div class="prompt">
    <h3>Use this prompt to create a page like this</h3>
    <p>Copy it into your chatbot, then replace the last line with your own content.</p>
    <pre id="{pid}">{esc(prompt(n, voice, look, ptitle))}</pre>
    <button class="copy" type="button" data-copy="{pid}" hidden>Copy the prompt</button>
  </div>
</section>''')
    page = f'''<!DOCTYPE html>
<!-- Generated by projects/tone-studio/_build/examples-page/build.py from each tone's landing.html, post.md and notes.md. Do not edit: change the source and rebuild. Invented example: the course, the people and the numbers are made up. -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tone Studio: seven tones, one story</title>
<meta name="description" content="One invented course written in seven tones, each as a full cinematic landing page and a social post, with the prompt to make a page like it.">
<style>
:root{{--bg:#ffffff;--panel:#f0f1f4;--ink:#16181d;--muted:#545862;--accent:#9e1b32;--line:#dcdee4;
  --display:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;--text:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --c60:var(--bg);--c30:var(--panel);--c10:var(--accent)}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}*{{transition:none!important}}}}
body{{margin:0;background:var(--bg);color:var(--ink);font:400 1.0625rem/1.6 var(--text);overflow-x:clip}}
h1,h2,h3{{font-family:var(--display);line-height:1.12;margin:0 0 .4em;text-wrap:balance}}
h1{{font-size:clamp(2.2rem,1.4rem + 3.6vw,3.8rem)}}
h2{{font-size:clamp(1.9rem,1.3rem + 2.4vw,3rem)}}
h3{{font-size:1.2rem}}
p{{margin:0 0 1em;max-width:68ch}}
a{{color:var(--accent)}}
:focus-visible{{outline:3px solid var(--accent);outline-offset:3px;border-radius:4px}}
[id]{{scroll-margin-top:76px}}
.wrap{{max-width:1080px;margin-inline:auto;padding-inline:20px}}
.lead{{font-size:1.15rem;color:var(--muted)}}
.small{{font-size:.92rem;color:var(--muted)}}
.toggle{{position:absolute;opacity:0;width:1px;height:1px}}
.bar{{position:sticky;top:0;z-index:40;display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:60px;padding:0 16px;background:#fff;border-bottom:1px solid var(--line)}}
.bar a{{font:700 1.05rem/1 var(--display);color:var(--ink);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}}
.open,.close{{display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 16px;border:1px solid var(--line);border-radius:999px;font-weight:700;cursor:pointer;background:var(--panel)}}
.open svg{{width:18px;height:18px}}
.toggle:focus-visible~.bar .open{{outline:3px solid var(--accent);outline-offset:3px}}
.side{{position:fixed;inset:0 auto 0 0;z-index:60;width:min(86vw,300px);overflow-y:auto;background:#fff;border-right:1px solid var(--line);padding:16px 14px 40px;transform:translateX(-102%);transition:transform .25s ease}}
.scrim{{display:none;position:fixed;inset:0;z-index:55;background:rgb(22 24 29/.45)}}
.toggle:checked~.layout .side{{transform:none}}
.toggle:checked~.layout .scrim{{display:block}}
.side-top{{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:0 6px 10px;border-bottom:1px solid var(--line)}}
.side-top b{{font:700 1.05rem/1.2 var(--display)}}
.side h2{{font:700 .8rem/1.2 var(--text);color:var(--muted);margin:20px 10px 4px}}
.side ul{{list-style:none;margin:0;padding:0}}
.side a{{display:flex;align-items:center;min-height:44px;padding:0 10px;border-radius:8px;color:var(--ink);text-decoration:none}}
.side a:hover{{background:var(--panel)}}
.side a[aria-current="true"]{{background:var(--panel);color:var(--accent);font-weight:700;box-shadow:inset 3px 0 0 var(--accent)}}
@media(min-width:960px){{
  .bar{{display:none}}
  .layout{{display:grid;grid-template-columns:260px minmax(0,1fr)}}
  .side{{position:sticky;top:0;height:100svh;width:auto;transform:none;transition:none;z-index:1}}
  .close{{display:none}}
  .toggle:checked~.layout .scrim{{display:none}}
}}
main{{min-width:0}}
.intro{{background:var(--panel);padding-block:clamp(40px,6vw,72px) 36px}}
.toc{{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));list-style:none;padding:0;margin:24px 0 0}}
.toc a{{display:block;height:100%;padding:14px 16px;border:1px solid var(--line);border-radius:12px;background:#fff;color:var(--ink);text-decoration:none}}
.toc a:hover{{border-color:var(--accent)}}
.toc b{{display:block;font:700 1.1rem/1.2 var(--display);margin-bottom:4px}}
.toc span{{font-size:.92rem;color:var(--muted)}}
.tone{{padding-block:clamp(48px,7vw,88px);border-bottom:1px solid var(--line)}}
.tone:nth-of-type(even){{background:var(--panel)}}
.tone:nth-of-type(even) .browser,.tone:nth-of-type(even) .browser-bar{{background:#fff}}
.tone>*{{max-width:1080px;margin-inline:auto;padding-inline:20px}}
.browser{{width:calc(100% - 40px);max-width:1040px;margin:24px auto 0;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--panel);padding:0}}
.browser-bar{{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:4px 16px;padding:6px 16px;font-size:.92rem;color:var(--muted);border-bottom:1px solid var(--line)}}
.browser-bar a{{font-weight:700;min-height:44px;display:inline-flex;align-items:center}}
.browser iframe{{display:block;width:100%;height:min(78svh,760px);min-height:520px;border:0;background:#fff}}
.cols{{display:grid;gap:32px;margin-top:32px}}
.cols>div{{min-width:0}}
@media(min-width:860px){{.cols{{grid-template-columns:1fr 1.2fr}}}}
.post{{border:1px solid var(--line);border-radius:12px;padding:20px;background:#fff;font-size:1rem}}
.post p{{max-width:none}}
.post pre{{overflow-x:auto;background:var(--panel);padding:12px;border-radius:8px;font-size:.85rem}}
.prompt{{margin-top:32px}}
.prompt>*{{max-width:none}}
.prompt pre{{white-space:pre-wrap;overflow-wrap:anywhere;margin:0 0 12px;padding:18px;border-radius:12px;background:var(--ink);color:#eef0f4;font:500 .9rem/1.55 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
.copy{{min-height:48px;padding:0 22px;border-radius:999px;border:2px solid var(--accent);background:var(--accent);color:#fff;font:700 1rem/1 var(--text);cursor:pointer}}
.foot{{padding:40px 20px;color:var(--muted);font-size:.92rem}}
</style>
</head>
<body>
<input type="checkbox" id="menu" class="toggle" aria-label="Show the list of tones" aria-controls="side">
<div class="bar"><a href="#top">Seven tones</a><label for="menu" class="open">{ICON}Tones</label></div>
<div class="layout">
<nav class="side" id="side" aria-label="The seven tones">
  <div class="side-top"><b>Seven tones, one story</b><label for="menu" class="close">Close</label></div>
  <h2>Start</h2><ul><li><a href="#top">Contents</a></li></ul>
  <h2>Tones</h2><ul>{nav}</ul>
</nav>
<label for="menu" class="scrim" aria-hidden="true"></label>
<main>
<header class="intro" id="top">
  <div class="wrap">
    <h1>Seven tones, one story</h1>
    <p class="lead">One invented course, Spreadsheets Without Fear, written seven ways. The facts never change. The order, the rhythm and the look do. Each tone below is the full landing page, live, then its post and the prompt to make one like it.</p>
    <p class="small">The course, Priya, Marta and every number are invented. <a href="{GH}/source-content.md">The source facts</a>.</p>
    <ul class="toc">{toc}</ul>
  </div>
</header>
{"".join(secs)}
<p class="foot">Invented examples for Tone Studio, part of Practical AI. Each page was made by a fresh Claude agent from the skill and the source on 21 November 2026.</p>
</main>
</div>
<script>
(()=>{{
  const t=document.getElementById('menu');
  document.querySelectorAll('.side a').forEach(a=>a.addEventListener('click',()=>{{t.checked=false}}));
  const links=new Map([...document.querySelectorAll('.side a')].map(a=>[a.hash.slice(1),a]));
  if('IntersectionObserver' in window){{
    const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{links.forEach(a=>a.removeAttribute('aria-current'));const a=links.get(e.target.id);if(a)a.setAttribute('aria-current','true')}}}}),{{rootMargin:'-30% 0px -60% 0px'}});
    links.forEach((a,id)=>{{const el=document.getElementById(id);if(el)io.observe(el)}});
  }}
  if(!navigator.clipboard)return;
  document.querySelectorAll('.copy').forEach(b=>{{b.hidden=false;b.addEventListener('click',()=>{{
    navigator.clipboard.writeText(document.getElementById(b.dataset.copy).textContent).then(()=>{{b.textContent='Copied';setTimeout(()=>{{b.textContent='Copy the prompt'}},1600)}});
  }})}});
}})();
</script>
</body>
</html>
'''
    OUT.write_text(page)
    print("wrote", OUT)

if __name__ == "__main__":
    build()
