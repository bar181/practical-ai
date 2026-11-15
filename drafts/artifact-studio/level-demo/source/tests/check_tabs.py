"""check_tabs.py [edition ...]

Opens every tab of each studio page at 320, 390 and 1280 pixels wide and reports script errors,
sideways scrolling and any state where exactly one view is not showing. At 390 it also runs an
accessibility scan (axe-core, WCAG 2 A and AA) if AXE_JS points at axe.min.js. Then it reloads
with scripts turned off and checks that the first tab shows and that tapping a tab changes it.

Needs: pip install playwright, and a Chrome or Chromium binary (set CHROME to its path).
Editions: all, beginner, advanced, expert. Default: all four. A clean run prints "problems []".
"""
import asyncio, sys, os
from playwright.async_api import async_playwright
R=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..'))+'/'
CHROME=os.environ.get('CHROME','/usr/bin/google-chrome')
F={'all':'level-demo/artifact-studio.html','beginner':'level-simple/artifact-studio-beginner.html','advanced':'level-working/artifact-studio-advanced.html','expert':'level-automated/artifact-studio-expert.html'}
AXE=open(os.environ['AXE_JS']).read() if os.environ.get('AXE_JS') else None
async def main(keys):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=CHROME,args=['--no-sandbox'])
        for key in keys:
            for w in (320,390,1280):
                pg=await b.new_page(viewport={'width':w,'height':780}); errs=[]
                pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e: errs.append(str(e)))
                await pg.goto('file://'+R+F[key]); await pg.wait_for_timeout(700)
                ids=await pg.evaluate("[...document.querySelectorAll('.tabr')].map(r=>r.id)"); bad=[]
                for i in ids:
                    await pg.evaluate("scrollTo(0,0)")
                    lab=pg.locator(f'.tabs label[for="{i}"]').last
                    if not await lab.is_visible(): await pg.locator(f'.tabs .tabs-g label[for="{i}"]').click() if await pg.locator(f'.tabs .tabs-g label[for="{i}"]').count() else await pg.evaluate(f"(()=>{{const g=[...document.querySelectorAll('.tabs-s')].find(s=>s.querySelector('label[for=\"{i}\"]'));document.querySelector('.tabs-g label.'+g.className.split(' ')[1].replace('s','g')).click()}})()")
                    await pg.wait_for_timeout(120); await lab.click(); await pg.wait_for_timeout(450)
                    st=await pg.evaluate("(()=>{const v=[...document.querySelectorAll('.view')].filter(v=>getComputedStyle(v).display!=='none');return {n:v.length,id:v[0]&&v[0].id,h:v[0]&&v[0].offsetHeight,sw:document.documentElement.scrollWidth}})()")
                    if st['n']!=1 or st['id']!='v-'+i[2:] or st['h']<300 or st['sw']>w: bad.append((i,st))
                    if w==390 and AXE:
                        await pg.evaluate(AXE) if not await pg.evaluate("!!window.axe") else None
                        r=await pg.evaluate("axe.run(document,{runOnly:['wcag2a','wcag2aa']}).then(r=>r.violations.map(v=>v.id+' x'+v.nodes.length+' '+(v.nodes[0].target.join(' ')).slice(0,90)))")
                        if r: bad.append((i,'axe',r))
                print(key,w,'tabs',len(ids),'errors',errs[:3],'problems',bad[:6]); await pg.close()
            cx=await b.new_context(java_script_enabled=False,viewport={'width':390,'height':780}); pg=await cx.new_page()
            await pg.goto('file://'+R+F[key])
            v0=await pg.locator('.view:visible').count(); await pg.locator('.tabs .tabs-g label').nth(1).click(); await pg.wait_for_timeout(200)
            v1=await pg.locator('.view:visible').first.get_attribute('id'); await pg.screenshot(path=f'/tmp/nojs_{key}.png')
            print(key,'no script: visible views at load',v0,'after tapping 2nd tab ->',v1); await cx.close()
        await b.close()
asyncio.run(main(sys.argv[1:] or list(F)))
