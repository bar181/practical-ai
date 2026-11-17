"""capture.py: makes img/pilot-brief.webp, the screen capture on the README.

It renders the unedited reply from the builder pilot (quality-results/2026-11-16-builder-pilot/
runs/agentic-process-result.md) as a chat reply, then takes a screenshot of its first screen.
Run: python3 projects/agentic-process/_build/capture.py   (needs: markdown, playwright, Pillow)
"""
import io, os, markdown
from PIL import Image
from playwright.sync_api import sync_playwright

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "..", "quality-results", "2026-11-16-builder-pilot", "runs", "agentic-process-result.md")
body = markdown.markdown(open(src, encoding="utf-8").read(), extensions=["tables"])
page = f"""<!doctype html><meta charset="utf-8"><style>
body{{margin:0;background:#0c2340;font:16px/1.5 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color:#14202e}}
.bar{{color:#ffd23f;font-weight:700;padding:18px 28px 10px;font-size:18px}}
.bar span{{color:#cfd8e6;font-weight:400}}
.card{{background:#fff;margin:0 20px 20px;border-radius:14px;padding:22px 26px}}
h3{{margin:20px 0 8px;font-size:18px}} p{{margin:0 0 12px}}
table{{border-collapse:collapse;font-size:13.5px;width:100%}} th,td{{border:1px solid #d3d8e2;padding:5px 7px;text-align:left;vertical-align:top}}
th{{background:#eef2f8}}
</style><div class="bar">Chat reply, unedited <span>&middot; the tool built with Agentic Process, run on a notice it had never seen</span></div>
<div class="card">{body}</div>"""
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1000, "height": 760}, device_scale_factor=2)
    pg.set_content(page)
    png = pg.screenshot(clip={"x": 0, "y": 0, "width": 1000, "height": 760})
    b.close()
out = os.path.join(here, "img", "pilot-brief.webp")
os.makedirs(os.path.dirname(out), exist_ok=True)
Image.open(io.BytesIO(png)).resize((1000, 760)).save(out, "WEBP", quality=82)
print("wrote", out)
