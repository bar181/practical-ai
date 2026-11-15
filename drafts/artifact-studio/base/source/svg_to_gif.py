"""svg_to_gif.py: write a GIF of each animated SVG, for places that do not accept SVG (email, some slide tools).

Each frame is taken by pausing the SVG's own animations at an exact time, so the GIF matches the file.
Writes ../templates/components/gif/NAME.gif on a white background. The wave divider is left out: its two
layers only line up again after two minutes, so it cannot loop cleanly as a GIF.
Needs: playwright, pillow, and a Chrome binary (set CHROME to its path).
"""
import asyncio, glob, io, os
from PIL import Image
from playwright.async_api import async_playwright
HERE=os.path.dirname(os.path.abspath(__file__)); SVG=os.path.join(HERE,'..','templates','components','svg'); OUT=os.path.join(HERE,'..','templates','components','gif')
FPS=12; SKIP={'wave-divider'}; LOOP_MS={'orbit':16000/3}        # three points 120 degrees apart: a third of a turn loops cleanly
async def main():
    os.makedirs(OUT,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=os.environ.get('CHROME','/usr/bin/google-chrome'),args=['--no-sandbox'])
        for f in sorted(glob.glob(os.path.join(SVG,'*.svg'))):
            name=os.path.basename(f)[:-4]
            if name in SKIP: continue
            vb=[float(x) for x in open(f).read().split('viewBox="')[1].split('"')[0].split()]; w=360; h=round(w*vb[3]/vb[2])
            pg=await b.new_page(viewport={'width':w,'height':h}); await pg.goto('file://'+os.path.abspath(f)); await pg.wait_for_timeout(150)
            t=await pg.evaluate("(()=>{const a=document.getAnimations();a.forEach(x=>x.pause());const tm=a.map(x=>x.effect.getComputedTiming());return {loop:tm.some(x=>x.iterations===Infinity),end:Math.max(...tm.map(x=>x.iterations===Infinity?0:x.endTime)),iter:Math.max(...tm.map(x=>x.iterations===Infinity?x.duration:0))}})()")
            total=LOOP_MS.get(name) or (min(t['iter'],4000) if t['loop'] else t['end']); n=max(2,round(total/1000*FPS)); frames=[]
            for i in range(n if t['loop'] else n+1):
                await pg.evaluate("t=>document.getAnimations().forEach(a=>{a.currentTime=t})",total*i/n)
                frames.append(Image.open(io.BytesIO(await pg.screenshot())).convert('P',palette=Image.ADAPTIVE,colors=32))
            dur=[round(1000/FPS)]*len(frames)
            if not t['loop']: dur[-1]=1800                         # hold the finished picture before repeating
            frames[0].save(os.path.join(OUT,name+'.gif'),save_all=True,append_images=frames[1:],duration=dur,loop=0,optimize=True)
            print(f"{name}: {len(frames)} frames, {os.path.getsize(os.path.join(OUT,name+'.gif'))//1024} KB, {'loops' if t['loop'] else 'plays once and holds'}"); await pg.close()
        await b.close()
asyncio.run(main())
