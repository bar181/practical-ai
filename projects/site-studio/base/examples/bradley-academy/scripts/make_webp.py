"""make_webp.py: light versions of the site's photos, for faster pages.

Reads every JPEG in projects/artifact-studio/_build/photos/ and writes two WebP files to
projects/site-studio/_build/photos-webp/ (copied to media/photos-webp/ by sync.mjs): NAME.webp (at most 1600 pixels wide) and NAME-800.webp (at most 800).
Scene pictures use them through srcset. Run after adding or changing a photo, then commit the
output. Needs Pillow: pip install pillow
"""
import glob, os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "..", "..", "..", "artifact-studio", "_build", "photos")
OUT = os.path.join(HERE, "..", "..", "..", "..", "_build", "photos-webp")
os.makedirs(OUT, exist_ok=True)
for path in sorted(glob.glob(os.path.join(SRC, "*.jpg"))):
    name = os.path.splitext(os.path.basename(path))[0]
    im = Image.open(path).convert("RGB")
    for width, suffix in ((1600, ""), (800, "-800")):
        copy = im.copy()
        if copy.width > width:
            copy = copy.resize((width, round(copy.height * width / copy.width)), Image.LANCZOS)
        copy.save(os.path.join(OUT, f"{name}{suffix}.webp"), "WEBP", quality=78, method=6)
    print(name, os.path.getsize(path) // 1024, "KB ->", os.path.getsize(os.path.join(OUT, name + ".webp")) // 1024, "KB,",
          os.path.getsize(os.path.join(OUT, name + "-800.webp")) // 1024, "KB at 800")
