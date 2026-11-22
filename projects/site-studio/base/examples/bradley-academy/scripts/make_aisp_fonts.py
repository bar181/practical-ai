"""make_aisp_fonts.py: small fonts for the AISP code panels (generated files: app/fonts/aisp-*.woff2).

Reads every character in app/content/aisp.ts and cuts two subsets: DejaVu Sans Mono (free licence,
installed with most Linux systems; set DEJAVU_MONO to its path elsewhere) for letters, digits, sub-
and superscripts and the symbols it has, then Noto Sans Math from node_modules (SIL Open Font
License) for the rest. Rerun after changing aisp.ts:  python3 scripts/make_aisp_fonts.py
"""
import os
from fontTools import subset
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
FS = os.path.join(SITE, "node_modules", "@fontsource")
text = open(os.path.join(SITE, "app", "content", "aisp.ts"), encoding="utf-8").read()
chars = sorted(set(text))

def cmap(path):
    return TTFont(path).getBestCmap()

def cut(src_files, wanted, out):
    # Merge coverage from every subset file of one family, then cut from the file that has each glyph.
    have = {}
    for f in src_files:
        for cp in cmap(f):
            have.setdefault(cp, f)
    groups = {}
    for c in wanted:
        if ord(c) in have:
            groups.setdefault(have[ord(c)], []).append(c)
    # One output per family: use the file covering the most characters.
    src = max(groups, key=lambda f: len(groups[f]))
    opts = subset.Options(); opts.flavor = "woff2"; opts.layout_features = ["*"]; opts.name_IDs = ["*"]
    font = TTFont(src)
    sub = subset.Subsetter(opts); sub.populate(text="".join(groups[src])); sub.subset(font)
    font.flavor = "woff2"; font.save(out)
    return "".join(groups[src]), [c for c in wanted if ord(c) not in have]

def files(family):
    d = os.path.join(FS, family, "files")
    return [os.path.join(d, f) for f in os.listdir(d) if f.endswith("400-normal.woff2")]

out_dir = os.path.join(SITE, "app", "fonts")
os.makedirs(out_dir, exist_ok=True)
dejavu = os.environ.get("DEJAVU_MONO", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")
mono_wanted = [c for c in chars if c.isprintable()]
mono, mono_missing = cut([dejavu], mono_wanted, os.path.join(out_dir, "aisp-mono.woff2"))
math_wanted = [c for c in chars if not c.isascii() and c not in mono]
math, math_missing = cut(files("noto-sans-math"), math_wanted, os.path.join(out_dir, "aisp-math.woff2"))
for f in ("aisp-mono.woff2", "aisp-math.woff2"):
    print(f, os.path.getsize(os.path.join(out_dir, f)), "bytes")
print("Not in either font (the system font draws these):", "".join(c for c in math_missing if c not in mono) or "none")
