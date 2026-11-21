"""Measure a page's 60-30-10 colour balance.

A page declares its three colour roles in :root:
  --c60  the dominant colour (usually the background),        aim for 50 to 70 percent
  --c30  the secondary colour (text, structure, dark panels),  aim for 20 to 40 percent
  --c10  the one bold accent (actions and one emphasis),       aim for 3 to 12 percent
The script renders the page at 1280 px wide with photos and videos hidden, so it measures the
colour system rather than the pictures, and counts every pixel by its nearest role. Pixels far from
all three (tints, borders, greys) are reported as "other". It also shows the result at 390 px.

Usage:  python3 workshop/tools/check_colour_balance.py page.html [page2.html ...]
Needs:  Playwright for Python and Chrome (set CHROME=/path/to/chrome if not at /usr/bin/google-chrome).
"""
import asyncio, io, os, sys

from PIL import Image
from playwright.async_api import async_playwright

CHROME = os.environ.get("CHROME", "/usr/bin/google-chrome")
NEAR = 58  # how close (RGB distance) a pixel must be to count as one of the three roles


def hex_rgb(v):
    v = v.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))


async def measure(page, path, width):
    await page.set_viewport_size({"width": width, "height": 900})
    await page.goto("file://" + os.path.abspath(path))
    await page.wait_for_timeout(500)
    roles = await page.evaluate(
        "['--c60','--c30','--c10'].map(n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim())")
    if not all(roles):
        return None, "declare --c60, --c30 and --c10 in :root"
    await page.add_style_tag(content="img,video,picture,svg image{visibility:hidden!important}"
                             "*{background-image:none!important;animation:none!important;transition:none!important}")
    await page.wait_for_timeout(200)
    shot = Image.open(io.BytesIO(await page.screenshot(full_page=True))).convert("RGB")
    shot = shot.resize((max(1, shot.width // 4), max(1, shot.height // 4)))
    cols = [hex_rgb(r) for r in roles]
    counts = [0, 0, 0, 0]
    pixels = shot.get_flattened_data() if hasattr(shot, "get_flattened_data") else shot.getdata()
    for px in pixels:
        d = [sum((a - b) ** 2 for a, b in zip(px, c)) ** 0.5 for c in cols]
        i = min(range(3), key=lambda k: d[k])
        counts[i if d[i] <= NEAR else 3] += 1
    total = sum(counts)
    return [round(100 * c / total) for c in counts], roles


async def main(paths):
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)
        page = await browser.new_page(reduced_motion="reduce")
        failed = False
        for path in paths:
            for width in (1280, 390):
                shares, roles = await measure(page, path, width)
                if shares is None:
                    print(f"{path}: {roles}")
                    failed = True
                    break
                c60, c30, c10, other = shares
                ok = 45 <= c60 <= 75 and 15 <= c30 <= 45 and 2 <= c10 <= 13
                failed |= not ok
                print(f"{path} @{width}: 60 role {c60}%  30 role {c30}%  10 role {c10}%  other {other}%"
                      f"  ({', '.join(roles)})  {'ok' if ok else 'OUT OF BALANCE'}")
        await browser.close()
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    asyncio.run(main(sys.argv[1:]))
