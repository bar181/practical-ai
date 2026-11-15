"""check_pick.py: the picker in the studio page must give the same answers as catalog.py.

Runs every combination of goal, reader and shape through both and compares each result's
templates, score, strength and note. Needs playwright and a Chrome binary (set CHROME).
"""
import asyncio, json, os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'..'))
import catalog as C
from playwright.async_api import async_playwright
async def main():
    G=[g for g,_ in C.FACETS['goal']]; A=[a for a,_ in C.FACETS['audience']]; F=[f for f,_ in C.FACETS['format']]
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=os.environ.get('CHROME','/usr/bin/google-chrome'),args=['--no-sandbox'])
        pg=await b.new_page(); await pg.goto('file://'+os.path.abspath(os.path.join(HERE,'..','..','studio.html'))); await pg.wait_for_timeout(800)
        await pg.evaluate("document.getElementById('t-pick').click()"); await pg.wait_for_timeout(400)
        bad=[]; n=0; weak=0
        for g in G:
            for a in A:
                for f in F:
                    n+=1; py=[[r['templates'],r['score'],r['strength'],r['note'],r['ask']] for r in C.recommend(g,a,f)]
                    js=await pg.evaluate("([g,a,f])=>STUDIO.recommend(g,a,f).map(r=>[r.templates,r.score,r.strength,r.note,r.ask])",[g,a,f])
                    weak+=py[0][2]=='weak'
                    if py!=js: bad.append((g,a,f,py[:1],js[:1]))
        await b.close()
    print(f'{n-len(bad)} of {n} requests give the same answer in the page and in Python. Top answer is a weak fit in {weak}.')
    for x in bad[:5]: print('DIFFERENT',x)
    sys.exit(1 if bad else 0)
asyncio.run(main())
