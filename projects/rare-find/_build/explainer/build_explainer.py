"""build_explainer.py: makes docs/reports/rare-find.html from explainer.src.html and the pictures.

Pictures come from _build/img/explainer/ (screens of the game from a test run) and _build/img/.
Run: python3 projects/rare-find/_build/explainer/build_explainer.py
"""
import base64, os, re

here = os.path.dirname(os.path.abspath(__file__))
img = os.path.join(here, "..", "img")
repo = os.path.abspath(os.path.join(here, "..", "..", "..", ".."))
src = open(os.path.join(here, "explainer.src.html"), encoding="utf-8").read()

def data(path, kind):
    return f"data:{kind};base64," + base64.b64encode(open(path, "rb").read()).decode()

def pic(m):
    name = m.group(1)
    for folder in (os.path.join(img, "explainer"), img):
        p = os.path.join(folder, name + ".webp")
        if os.path.exists(p):
            return data(p, "image/webp")
    raise SystemExit("missing picture: " + name)

html = re.sub(r"\{\{img:([a-z0-9-]+)\}\}", pic, src)
html = re.sub(r"\{\{svg:([a-z0-9-]+)\}\}", lambda m: data(os.path.join(img, m.group(1) + ".svg"), "image/svg+xml"), html)
assert "{{" not in html
out = os.path.join(repo, "docs", "reports", "rare-find.html")
open(out, "w", encoding="utf-8").write(html)
print("built", os.path.relpath(out, repo), len(html) // 1024, "KB")
