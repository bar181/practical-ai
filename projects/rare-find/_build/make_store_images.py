"""make_store_images.py: makes the App Store style screens for the README.

Plays base/game.html in a phone-sized browser (no AI: the offline web copy), captures four
screens, and frames each one under a short caption. Run it after any change to the game's look.

Run: python3 projects/rare-find/_build/make_store_images.py   (needs: playwright, Pillow)
Writes _build/img/store-1-today.webp ... store-4-settings.webp
"""
import functools, http.server, io, os, socketserver, threading
from PIL import Image
from playwright.sync_api import sync_playwright

here = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(here, "img")

class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(("127.0.0.1", 0), functools.partial(_Quiet, directory=os.path.join(os.path.dirname(here), "base")))
threading.Thread(target=srv.serve_forever, daemon=True).start()
GAME = f"http://127.0.0.1:{srv.server_address[1]}/game.html"

# Caption, small line, background tint: one per screen, in the order they are captured.
CARDS = [
    ("store-1-today", "Seven prompts a day", "The same for everyone, new every day", "#3a2d7a"),
    ("store-2-result", "The rare answer wins", "A Gem scores 100. The crowd pick, 25", "#5b3b8f"),
    ("store-3-scorecard", "See where you stand", "Your score, your week, your streak", "#2d4f7a"),
    ("store-4-settings", "Play it your way", "Timer, hosts and party mode", "#3d3570"),
]

FRAME = """<!doctype html><html><head><style>
html,body{margin:0}
body{width:600px;height:1140px;background:radial-gradient(120% 70% at 50% 0%,{tint} 0%,#1a1530 70%);
 font-family:ui-rounded,"SF Pro Rounded",Nunito,"Segoe UI",system-ui,sans-serif;color:#f5f2ff;
 display:flex;flex-direction:column;align-items:center;overflow:hidden}
h1{margin:64px 40px 0;font-size:50px;line-height:1.05;font-weight:800;text-align:center;letter-spacing:-.5px}
p{margin:16px 48px 0;font-size:25px;line-height:1.3;color:#d8d2f2;text-align:center;font-weight:600}
.phone{margin-top:44px;width:410px;border-radius:58px;background:#0d0a1c;padding:14px;
 box-shadow:0 30px 70px rgba(0,0,0,.55),inset 0 0 0 2px #463d7a}
.phone img{display:block;width:100%;border-radius:46px}
</style></head><body><h1>{title}</h1><p>{sub}</p><div class="phone"><img src="data:image/png;base64,{shot}"></div></body></html>"""

def main():
    import base64
    shots = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
        ctx.add_init_script("window.__rfDay='2026-11-19';")
        pg = ctx.new_page()
        pg.goto(GAME); pg.wait_for_timeout(400)
        shots.append(pg.screenshot())                                   # 1. home: today's game
        pg.click("#b-daily"); pg.wait_for_timeout(300)
        pid = pg.evaluate("()=>{const t=document.querySelector('#prompt-text').textContent;return window.__rf.packs.find(p=>p.prompt===t).id}")
        pk = pg.evaluate("p=>window.__rf.packs.find(x=>x.id===p)", pid)
        pg.fill("#answer", pk["gems"][0]["a"]); pg.press("#answer", "Enter"); pg.wait_for_timeout(3500)  # let the confetti settle
        pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(200)
        shots.append(pg.screenshot())                                   # 2. a Gem result
        picks = [lambda k: k["ranked"][2]["a"], lambda k: max(k["good"], key=lambda e: e.get("r", 0))["a"], lambda k: k["ranked"][0]["a"],
                 lambda k: k["ranked"][7]["a"], lambda k: k["ranked"][4]["a"], lambda k: k["ranked"][9]["a"]]
        for pick in picks:
            pg.wait_for_function("!document.querySelector('#b-next').disabled", timeout=20000)
            pg.click("#b-next"); pg.wait_for_timeout(250)
            pid = pg.evaluate("()=>{const t=document.querySelector('#prompt-text').textContent;return window.__rf.packs.find(p=>p.prompt===t).id}")
            k = pg.evaluate("p=>window.__rf.packs.find(x=>x.id===p)", pid)
            pg.fill("#answer", pick(k)); pg.press("#answer", "Enter"); pg.wait_for_timeout(700)
        pg.wait_for_function("!document.querySelector('#b-next').disabled", timeout=20000)
        pg.click("#b-next"); pg.wait_for_timeout(900)
        pg.click("#b-tocard"); pg.wait_for_timeout(500); pg.evaluate("window.scrollTo(0,0)")
        shots.append(pg.screenshot())                                   # 3. the scorecard
        pg.click("#tab-play"); pg.wait_for_timeout(300)
        pg.click("#b-settings"); pg.wait_for_timeout(500)
        pg.evaluate("document.querySelector('#b-settings').scrollIntoView({block:'start'})"); pg.wait_for_timeout(200)
        shots.append(pg.screenshot())                                   # 4. settings, open
        card = b.new_page(viewport={"width": 600, "height": 1140}, device_scale_factor=2)
        for (name, title, sub, tint), shot in zip(CARDS, shots):
            card.set_content(FRAME.replace("{tint}", tint).replace("{title}", title).replace("{sub}", sub)
                             .replace("{shot}", base64.b64encode(shot).decode()))
            card.wait_for_timeout(150)
            im = Image.open(io.BytesIO(card.screenshot())).convert("RGB").resize((600, 1140), Image.LANCZOS)
            im.save(os.path.join(img_dir, name + ".webp"), "WEBP", quality=86, method=6)
            print("wrote", name + ".webp")
        b.close()

if __name__ == "__main__":
    main()
