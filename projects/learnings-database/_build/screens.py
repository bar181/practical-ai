"""screens.py: makes the README and explainer pictures from real test output and the template.

Writes to _build/img/ (each picture is generated; change this script, then rerun):
  example-reply.webp   the top of a real, unedited reply from a fresh Claude session (case V2 of
                       the final behaviour run), shown as a chat
  before-i-start.webp  the "before I start" reply from the same run (case V6), shown as a chat
  the-log.webp         the template's invented rows, shown as a spreadsheet
Needs: playwright with Chrome, markdown, Pillow.
Run: python3 projects/learnings-database/_build/screens.py
"""
import csv, html, io, os

import markdown
from PIL import Image
from playwright.sync_api import sync_playwright

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
replies = open(os.path.join(here, "eval", "run-8-behaviour-replies.md")).read()
cases = open(os.path.join(here, "eval", "behaviour-cases.md")).read()


def part(text, case):
    return text.split(f"## {case}\n", 1)[1].split("\n## ", 1)[0].strip()


def said(case):
    block = part(cases, case)
    for line in block.splitlines():
        if line.startswith("Message:"):
            return line[len("Message:"):].strip().strip('"')
    return ""


CSS = """
body{margin:0;background:#f4f6fa;font:15px/1.5 system-ui,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:#14212b}
.wrap{width:430px;padding:18px}
.tag{font-size:12px;color:#5a6478;margin:0 0 10px}
.me{margin:0 0 14px auto;max-width:82%;background:#1f4a5c;color:#fff;border-radius:16px 16px 4px 16px;padding:12px 14px}
.ai{background:#fff;border:1px solid #d6dce5;border-radius:16px 16px 16px 4px;padding:6px 16px}
.ai pre{background:#f4f6fa;border-radius:8px;padding:10px;white-space:pre-wrap;word-break:break-word;font-size:12px}
.ai table{border-collapse:collapse;font-size:13px;width:100%}.ai td:first-child{white-space:nowrap}.ai td,.ai th{border-bottom:1px solid #e2e6ec;padding:4px 6px;text-align:left;vertical-align:top}
.ai code{font-size:12.5px}
"""


def chat(page, case, out, height, keep_rows=None):
    reply = part(replies, case)
    if keep_rows:  # shorten a long table to the rows a reader needs, and say so
        lines, kept = reply.splitlines(), []
        for ln in lines:
            if ln.startswith("| ") and not ln.startswith(("| Column", "| ---", "| id |")) and ln.split("|")[1].strip() not in keep_rows:
                continue
            kept.append(ln)
        reply = "\n".join(kept)
    reply = reply.replace(":\n- ", ":\n\n- ")  # markdown needs a blank line before a list
    body = markdown.markdown(reply, extensions=["tables", "fenced_code"])
    note = "A real, unedited reply from a fresh Claude session in testing" + (", with some table rows hidden" if keep_rows else "") + ". Invented data."
    page.set_content(f"<style>{CSS}</style><div class='wrap'><p class='tag'>{note}</p>"
                     f"<p class='me'>{html.escape(said(case))}</p><div class='ai'>{body}</div></div>")
    shot(page, out, height)


def shot(page, out, height):
    png = page.locator(".wrap").screenshot()
    im = Image.open(io.BytesIO(png)).convert("RGB")
    if im.height > height * 2:
        im = im.crop((0, 0, im.width, height * 2))
    im.save(os.path.join(here, "img", out), "WEBP", quality=88)


def sheet(page):
    rows = list(csv.DictReader(open(os.path.join(root, "base", "template", "learnings.csv"))))[:7]
    cols = ["id", "kind", "area", "project", "rule", "status", "seen"]
    head = "".join(f"<th>{c}</th>" for c in cols)
    body = "".join("<tr>" + "".join(f"<td>{html.escape(r[c])}</td>" for c in cols) + "</tr>" for r in rows)
    css = CSS + """.wrap{width:900px}.grid{border-collapse:collapse;background:#fff;font-size:13px}
    .grid th{background:#e8e4f7;border:1px solid #c9cfd9;padding:6px 8px;text-align:left}
    .grid td{border:1px solid #d6dce5;padding:6px 8px;vertical-align:top}.grid td:first-child{white-space:nowrap}.grid td:nth-child(5){width:430px}"""
    page.set_content(f"<style>{css}</style><div class='wrap'><p class='tag'>The starter spreadsheet, learnings.xlsx: "
                     f"the first rows of its invented examples (7 of 18 columns shown).</p><table class='grid'><tr>{head}</tr>{body}</table></div>")
    shot(page, "the-log.webp", 1000)


with sync_playwright() as p:
    b = p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"))
    page = b.new_page(device_scale_factor=2)
    chat(page, "V2", "example-reply.webp", 720,
         keep_rows={"kind", "area", "project", "lesson_type", "rule", "status", "seen", "sensitive"})
    chat(page, "V6", "before-i-start.webp", 900)
    sheet(page)
    b.close()
print("pictures: ok")
