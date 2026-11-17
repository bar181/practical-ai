"""capture.py: makes img/pilot-brief.webp and img/pilot-brief-direct.webp, the captures on the README.

It renders the two unedited replies from the builder pilot (quality-results/2026-11-16-builder-pilot/
runs/agentic-process-result.md and direct-result.md) as chat replies, and captures each first screen.
Run: python3 projects/agentic-process/_build/capture.py   (needs: markdown, playwright, Pillow)
"""
import io, os, markdown
from PIL import Image
from playwright.sync_api import sync_playwright

here = os.path.dirname(os.path.abspath(__file__))
runs = os.path.join(here, "..", "quality-results", "2026-11-16-builder-pilot", "runs")
jobs = [("agentic-process-result.md", "pilot-brief.webp", "built with Agentic Process"),
        ("direct-result.md", "pilot-brief-direct.webp", "built directly, without Agentic Process")]
css = """body{margin:0;background:#0c2340;font:16px/1.5 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color:#14202e}
.bar{color:#ffd23f;font-weight:700;padding:18px 28px 10px;font-size:18px}
.bar span{color:#cfd8e6;font-weight:400}
.card{background:#fff;margin:0 20px 20px;border-radius:14px;padding:22px 26px}
h3{margin:20px 0 8px;font-size:18px} p{margin:0 0 12px}
table{border-collapse:collapse;font-size:13.5px;width:100%} th,td{border:1px solid #d3d8e2;padding:5px 7px;text-align:left;vertical-align:top}
th{background:#eef2f8}"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for src, name, label in jobs:
        body = markdown.markdown(open(os.path.join(runs, src), encoding="utf-8").read(), extensions=["tables"])
        page = f'<!doctype html><meta charset="utf-8"><style>{css}</style><div class="bar">Chat reply, unedited <span>&middot; the tool {label}, on a notice it had never seen</span></div><div class="card">{body}</div>'
        pg = b.new_page(viewport={"width": 1000, "height": 760}, device_scale_factor=2)
        pg.set_content(page)
        png = pg.screenshot(clip={"x": 0, "y": 0, "width": 1000, "height": 760})
        out = os.path.join(here, "img", name)
        Image.open(io.BytesIO(png)).resize((1000, 760)).save(out, "WEBP", quality=82)
        print("wrote", out)
    b.close()
