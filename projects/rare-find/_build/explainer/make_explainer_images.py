"""make_explainer_images.py: captures the game screens that the explainer page shows.

Writes _build/img/explainer/{home,result,gem,checked,challenged,hero}.webp from the built game
(base/game.html), playing 17 November 2026 at phone width with a mock of Claude's answer check.
v1-home.webp is the version 1 screen kept for the before-and-after, and is not touched.
The mock says yes to "The Phantom" with rarity 6; host comments fall back to the game's own lines.
Run after the game's look changes, then build_explainer.py:
  python3 projects/rare-find/_build/explainer/make_explainer_images.py
"""
import io, json, os
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "..", "img", "explainer")
game = "file://" + os.path.abspath(os.path.join(here, "..", "..", "base", "game.html"))

MOCK = r"""
(() => {
  window.__rfDay = '2026-11-17';
  const sample = async (input) => {
    const q = String(input);
    if (q.includes('You judge a family trivia game')) {
      const a = (q.match(/A player answered: "([^"]*)"/) || [])[1] || '';
      return { text: JSON.stringify({ correct: true, canonical: a, rarity: 6, why: 'A real superhero.' }), truncated: false };
    }
    throw { code: 'mock_off', message: 'host lines come from the game' };
  };
  window.claude = { use: async n => (n === 'sample' ? sample : null) };
})();
"""

def shot(pg):
    return Image.open(io.BytesIO(pg.screenshot())).convert("RGB")

def save(im, name):
    im.save(os.path.join(out, name + ".webp"), "WEBP", quality=80 if name != "hero" else 72, method=6)

def pack(pg):
    return pg.evaluate("window.__rf.dailyPacks('2026-11-17')[window.__rf.state().i]")

def answer(pg, text, wait):
    pg.fill("#answer", text); pg.press("#answer", "Enter"); pg.wait_for_timeout(wait)

def main():
    facts = {}
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=4 / 3, is_mobile=True, has_touch=True)
        ctx.add_init_script(MOCK)
        pg = ctx.new_page(); pg.goto(game); pg.wait_for_timeout(600)
        home = shot(pg); save(home, "home")
        pg.click("#b-daily"); pg.wait_for_timeout(500)
        # 1. Name a bird: typing, then the 9th most popular answer
        k = pack(pg); bird = next((r["a"] for r in k["ranked"] if r["a"] == "Flamingo"), k["ranked"][8]["a"])
        pg.type("#answer", bird[:5], delay=40); pg.wait_for_timeout(1200); typing = shot(pg)
        answer(pg, bird, 2200); result = shot(pg); save(result, "result")
        facts["result"] = [bird, pg.evaluate("window.__rf.state().cur")]
        pg.click("#b-next"); pg.wait_for_timeout(500)
        # 2. a Gem, caught while it celebrates
        k = pack(pg); gem = next((g["a"] for g in k["gems"] if g["a"] == "Shakshuka"), k["gems"][0]["a"])
        answer(pg, gem, 1000); gem_im = shot(pg); save(gem_im, "gem"); facts["gem"] = [k["prompt"], gem]
        pg.wait_for_timeout(2300); pg.click("#b-next"); pg.wait_for_timeout(500)
        # 3. an answer on no list, checked by the AI
        k = pack(pg); answer(pg, "The Phantom", 400); pg.click("#b-check"); pg.wait_for_timeout(2600)
        checked = shot(pg); save(checked, "checked"); facts["checked"] = [k["prompt"], pg.evaluate("window.__rf.state().cur")]
        # the rest of the seven: a mix of results
        picks = [lambda k: k["ranked"][3]["a"], lambda k: max(k["good"], key=lambda e: e["r"])["a"], lambda k: k["ranked"][0]["a"], lambda k: k["gems"][1]["a"]]
        for f in picks:
            pg.click("#b-next"); pg.wait_for_timeout(500); answer(pg, f(pack(pg)), 3200)
        pg.click("#b-next"); pg.wait_for_timeout(4000)
        pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(200)
        end = shot(pg); facts["end"] = pg.inner_text("#final")
        pg.fill("#share-name", "Bradley"); pg.dispatch_event("#share-name", "input"); pg.wait_for_timeout(300)
        code = pg.input_value("#share-link").split("#c-", 1)[1].split()[0]; facts["code"] = code
        # 4. a friend opens the challenge
        ctx2 = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=4 / 3, is_mobile=True, has_touch=True)
        ctx2.add_init_script(MOCK)
        pf = ctx2.new_page(); pf.goto(game + "#c-" + code); pf.wait_for_timeout(800)
        challenged = shot(pf); save(challenged, "challenged"); facts["challenged"] = pf.inner_text("#ch-title")
        b.close()
    # the hero: five phones, staggered, on the game's own background
    W, H = 2400, 1250; bg = Image.new("RGB", (W, H), (26, 21, 48)); d = ImageDraw.Draw(bg)
    phones = [home, typing, gem_im, checked, end]; pw, ph = 420, 908; gap = (W - 5 * pw) // 6
    for i, im in enumerate(phones):
        x = gap + i * (pw + gap); y = [170, 80, 170, 80, 170][i]
        d.rounded_rectangle((x - 10, y - 10, x + pw + 10, y + ph + 10), radius=46, fill=(14, 11, 28), outline=(70, 62, 110), width=3)
        sc = im.resize((pw, int(im.height * pw / im.width)), Image.LANCZOS).crop((0, 0, pw, ph))
        m = Image.new("L", (pw, ph), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, pw, ph), radius=38, fill=255)
        bg.paste(sc, (x, y), m)
    save(bg, "hero")
    print(json.dumps(facts, indent=1, default=str))

if __name__ == "__main__":
    main()
