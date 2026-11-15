"""check_at_rest.py

Opens every other demo page (drafts/*/level-demo/index.html) with scripts turned off and prints how much
text is readable, so a page that is an empty shell until its script runs shows up as a small number.
Needs playwright and a Chrome binary (set CHROME to its path).
"""
import asyncio, glob, os
from playwright.async_api import async_playwright
REPO=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','..','..'))
CHROME=os.environ.get('CHROME','/usr/bin/google-chrome')
async def main():
    fs=sorted(glob.glob(REPO+'/drafts/*/level-demo/index.html'))
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=CHROME,args=['--no-sandbox'])
        for f in fs:
            cx=await b.new_context(java_script_enabled=False,viewport={'width':390,'height':780},device_scale_factor=1); pg=await cx.new_page(); await pg.goto('file://'+f)
            name=f.split('/')[-3]
            txt=len((await pg.locator('body').inner_text()).strip()); sel=await pg.locator('select').count(); btn=await pg.locator('button:visible').count()
            empties=await pg.locator('main :is(div,section,ul,ol,table,tbody,p,output)[id]:visible').evaluate_all("e=>e.filter(x=>!x.textContent.trim()&&!x.querySelector('img,svg,canvas,input,textarea')).map(x=>x.id)") if True else []
            print(f'{name:22} text {txt:5}  selects {sel}  buttons {btn}  empty ids {empties}'); await cx.close()
        await b.close()
asyncio.run(main())
