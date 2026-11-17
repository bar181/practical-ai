"""capture_tryit.py: records a page scrolling on a phone, as one looping animated WebP.

Used for the README captures: img/example-tryit.webp (the page a fresh AI session made from the
try-it prompt, unedited) and the scroll-*.webp showcase captures of the worked examples. Boxes
that explain how an example was made (<aside>) are hidden.
Run: python3 projects/artifact-studio/_build/capture_tryit.py PAGE.html OUT.webp [MAX_SCREENS]
(needs: playwright, Pillow)
"""
import io, os, sys
from PIL import Image
from playwright.sync_api import sync_playwright

here = os.path.dirname(os.path.abspath(__file__))
page = os.path.abspath(sys.argv[1])
out = sys.argv[2]
max_screens = float(sys.argv[3]) if len(sys.argv) > 3 else 99
W, H, STEP = 390, 760, 38  # phone width, frame height, pixels per frame

frames, durations = [], []
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2, is_mobile=True, has_touch=True)
    pg.goto("file://" + page)
    pg.add_style_tag(content="aside{display:none!important}")
    pg.wait_for_timeout(2500)
    total = min(pg.evaluate("document.documentElement.scrollHeight"), int(H * max_screens))
    step = max(STEP, (total - H) // 130)
    y = 0
    while True:
        pg.evaluate(f"window.scrollTo(0,{y})")
        pg.wait_for_timeout(120)
        img = Image.open(io.BytesIO(pg.screenshot())).convert("RGB").resize((W, H))
        frames.append(img)
        at_screen = y % H < step
        durations.append(900 if at_screen else 70)
        if y >= total - H:
            break
        y = min(y + step, total - H)
    durations[-1] = 1800
    b.close()

frames[0].save(out, "WEBP", save_all=True, append_images=frames[1:], duration=durations,
               loop=0, quality=70, method=6)
print("wrote", out, len(frames), "frames,", round(os.path.getsize(out) / 1e6, 2), "MB")
