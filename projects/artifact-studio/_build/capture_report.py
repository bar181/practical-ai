"""capture_report.py: makes img/example-report.webp, the screen capture at the top of the README.

It opens base/examples/report.html (the unedited page an AI made from the sample prompt), hides
the boxes that explain how the example was made, and captures the report's first screen.
Run: python3 projects/artifact-studio/_build/capture_report.py   (needs: playwright, Pillow)
"""
import io, os
from PIL import Image
from playwright.sync_api import sync_playwright

here = os.path.dirname(os.path.abspath(__file__))
page = os.path.join(here, "..", "base", "examples", "report.html")
out = os.path.join(here, "img", "example-report.webp")
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 900, "height": 1000}, device_scale_factor=2)
    pg.goto("file://" + os.path.abspath(page))
    pg.add_style_tag(content="aside{display:none!important}")
    pg.wait_for_timeout(1500)
    png = pg.screenshot(clip={"x": 0, "y": 0, "width": 900, "height": 1000})
    b.close()
Image.open(io.BytesIO(png)).resize((900, 1000)).save(out, "WEBP", quality=82)
print("wrote", out)
