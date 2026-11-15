"""check_examples.py: every worked example's output must open cleanly and keep its words inside the frame.

HTML: no script error, no request to the outside, no sideways scroll at 320 and 1280 pixels. A deck is paged
through and every piece of text must sit inside its slide. SVG: every piece of text must sit inside the picture with 40 pixels to spare.
Needs playwright and a Chrome binary (set CHROME).
"""
import asyncio, glob, os, sys
from playwright.async_api import async_playwright
EX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "examples")
INSIDE = "(sel,box)=>[...document.querySelectorAll(sel)].filter(e=>{const q=e.getBoundingClientRect();return q.width&&(q.left<box.left-1||q.right>box.right+1||q.top<box.top-1||q.bottom>box.bottom+1)}).map(e=>e.textContent.trim().slice(0,24))"
async def main():
    bad = []; n = 0
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"), args=["--no-sandbox"])
        for f in sorted(glob.glob(os.path.join(EX, "*", "*.html")) + glob.glob(os.path.join(EX, "*", "*.svg"))):
            name = os.path.relpath(f, EX)
            for w in ((320, 1280) if f.endswith(".html") else (1080,)):
                n += 1; pg = await b.new_page(viewport={"width": w, "height": 800}); errs = []; out = []
                pg.on("pageerror", lambda e: errs.append(str(e)[:80])); pg.on("request", lambda r: out.append(r.url[:60]) if not r.url.startswith(("file:", "data:")) else None)
                await pg.goto("file://" + os.path.abspath(f)); await pg.wait_for_timeout(350); problems = []
                if errs: problems.append(("script error", errs))
                if out: problems.append(("outside request", out))
                if f.endswith(".svg"):
                    spill = await pg.evaluate("(()=>{const r=document.documentElement.getBoundingClientRect(),m=40,s={left:r.left+m,right:r.right-m,top:r.top+m,bottom:r.bottom-m};return (" + INSIDE + ")('text',s)})()")
                    if spill: problems.append(("text outside the picture", spill))
                else:
                    if await pg.evaluate("document.documentElement.scrollWidth>innerWidth"): problems.append(("sideways scroll", w))
                    slides = await pg.locator(".dk-s").count()
                    for i in range(slides):
                        spill = await pg.evaluate("(()=>{const s=document.querySelector('.dk-s.cur').getBoundingClientRect();return (" + INSIDE + ")('.dk-s.cur :is(h2,p,b,span,li,td,th,small)',s)})()")
                        if spill: problems.append((f"text outside slide {i + 1}", spill))
                        if i < slides - 1: await pg.locator(".dk-next").click(); await pg.wait_for_timeout(60)
                if problems: bad.append((name, w, problems))
                await pg.close()
        await b.close()
    print(f"{n - len(bad)} of {n} example checks clean")
    for x in bad: print("  PROBLEM", x)
    sys.exit(1 if bad else 0)
asyncio.run(main())
