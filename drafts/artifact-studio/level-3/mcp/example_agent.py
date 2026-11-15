"""example_agent.py: what an assistant does with this server, written out as a script.

It asks the server to pick, fetches the starter it picked, fills it with new content and saves the
result. No model is involved: the content is typed below. The point is to prove that the tools give
an agent everything it needs to finish a file. Run from drafts/artifact-studio:

    python3 level-3/mcp/example_agent.py OUT_DIR
"""
import asyncio, json, os, re, sys
from mcp import ClientSession, StdioServerParameters, stdio_client

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
TITLE = "The studio becomes a library"
SLIDES = [  # (slide markup, speaker's note)
    ("<div><h2>An assistant guesses three things.</h2></div>", "What kind of piece is this, how should it speak, what should it look like. It guesses all three, every time."),
    ('<div><p class="big">3</p><p>guesses. Each one makes the work more generic.</p></div>', "Say the number and stop. Everyone in the room has received the generic version."),
    ("<div><h2>So everything it makes looks the same.</h2></div>", "One example from your own week. Do not show a slide of it."),
    ("<div><h2>So we made one rule.</h2><p>Stop guessing. Pick from a shelf.</p></div>", "The whole project is this slide: a shelf of working templates, and rules that pick."),
    ('<div class="three"><div><b>Pick</b><span>Say the job, the reader and the shape.</span></div><div><b>Build</b><span>The assistant fills a template with your content.</span></div><div><b>Check</b><span>A checklist runs before you see it.</span></div></div>', "Ten seconds each. Pick is a score: three times the goal fit plus twice the reader fit."),
    ('<div><p class="big">{n}</p><p>templates on the shelf. <span class="was">11 this morning.</span></p></div>', "Pages, voices, decks and social formats. And 36 parts, twelve of them animated."),
    ('<div><p class="big">8</p><p>tools an assistant can call. No pasting.</p></div>', "The MCP server. Be plain: it has only been tried with a test client so far."),
    ("<div><h2>One more thing.</h2><p>Nobody else has used it yet. You are first.</p></div>", "End on the ask: one real job this week, and tell us where it broke."),
]
CARD = {"lines": ["Stop guessing.", "Pick from", "a shelf."], "sub": "{n} templates for pages, decks and posts.", "name": "Practical AI: artifact studio"}


async def main():
    async with stdio_client(StdioServerParameters(command=sys.executable, args=[os.path.join(HERE, "server.py"), "--read-only"])) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            call = lambda name, **a: s.call_tool(name, a)
            shelf = (await call("list_templates")).content
            count = str(len(json.loads(shelf[0].text)) if len(shelf) == 1 and shelf[0].text.lstrip().startswith("[") else len(shelf))   # the count comes from the server, not from this file
            rec = json.loads((await call("recommend", goal="inspire", audience="team", format="deck")).content[0].text)
            rec = rec[0] if isinstance(rec, list) else rec
            tid = rec["templates"][0]
            print("picked:", tid, "|", rec["why"])
            files = json.loads((await call("get_template", id=tid, part="starter")).content[0].text)["files"]
            doc = next(iter(files.values()))
            n = len(re.findall(r'<section class="dk-s', doc))
            assert n == len(SLIDES), f"the starter has {n} slides and this script has {len(SLIDES)}"
            it = iter(SLIDES)
            doc = re.sub(r'<section class="dk-s([^"]*)">.*?</section>', lambda m: (lambda b, note: f'<section class="dk-s{m.group(1)}">{b.replace("{n}", count)}<aside class="dk-note">{note}</aside></section>')(*next(it)), doc, flags=re.S)
            doc = re.sub(r"<title>.*?</title>", f"<title>{TITLE}: the deck</title>", doc)
            doc = re.sub(r'aria-label="The [a-z]+ deck, [a-z]+ slides"', f'aria-label="{TITLE}, {len(SLIDES)} slides"', doc)
            open(os.path.join(OUT, "deck.html"), "w", encoding="utf-8").write(doc)
            svg = next(iter(json.loads((await call("get_template", id="social-square", part="starter")).content[0].text)["files"].values()))
            tsp = iter(CARD["lines"])
            svg = re.sub(r"(<tspan[^>]*>)[^<]*(</tspan>)", lambda m: m.group(1) + next(tsp) + m.group(2), svg)
            svg = svg.replace("Your company name", CARD["name"]).replace("We answer within the hour.", CARD["sub"].replace("{n}", count))
            svg = re.sub(r'aria-label="[^"]*"', f'aria-label="Square post: {" ".join(CARD["lines"])} {CARD["sub"].replace("{n}", count)}"', svg, count=1)
            open(os.path.join(OUT, "card.svg"), "w", encoding="utf-8").write(svg)
            print("wrote deck.html", len(doc), "and card.svg", len(svg))

asyncio.run(main())
