"""Artifact studio MCP server.

Lets an assistant browse the template library, get a recommendation for a request, read a
template's reference code and the build rules, and file a note about a design the person likes.
It reads base/templates/index.json, so it never disagrees with the library.

Run:  python server.py            (stdio, for desktop assistants)
      python server.py --http     (streamable HTTP on port 8000, for assistants that need a web address)
      add --read-only to leave out the one tool that writes a file
Needs: Python 3.10 or later and the `mcp` package, version 2.
"""
import glob, json, os, re, sys, datetime
from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))                       # drafts/artifact-studio
SKILL = os.path.normpath(os.path.join(ROOT, "..", "..", "skills", "artifact-studio"))
sys.path.insert(0, os.path.join(ROOT, "base", "source"))
import catalog                                                                # the same rules the studio page uses

READ = ToolAnnotations(readOnlyHint=True, openWorldHint=False)
MAX = 60_000


def _index():
    with open(os.path.join(ROOT, "base", "templates", "index.json"), encoding="utf-8") as f:
        return json.load(f)


def _read(rel):
    path = os.path.normpath(os.path.join(ROOT, rel))
    if not path.startswith(ROOT + os.sep):
        raise ValueError("path is outside the studio")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return text if len(text) <= MAX else text[:MAX] + "\n[cut: the file is longer than this tool returns]"


mcp = MCPServer(
    "artifact-studio",
    instructions=(
        "A library of page, deck and social templates with rules for choosing between them. "
        "Typical order: recommend (or list_templates) to choose, get_template with part='source' to read the "
        "reference code, get_rules('build') before writing, get_rules('checklist') before showing the result. "
        "Build one self-contained HTML file from the person's own content. Invent no facts."
    ),
)


@mcp.tool(annotations=READ)
def studio_overview() -> dict:
    """What the studio holds and how to use it. Call this first."""
    idx = _index()
    return {
        "counts": idx["counts"],
        "kinds": {"page": "a whole web page", "voice": "how a piece speaks", "deck": "slides", "social": "a post picture"},
        "facets": idx["facets"],
        "how_to_choose": idx["read_me"],
        "next": "Call recommend(goal, audience, format), or list_templates(kind).",
    }


@mcp.tool(annotations=READ)
def list_templates(kind: str = "") -> list[dict]:
    """List templates. kind is one of: page, voice, deck, social. Leave it empty for all."""
    return [
        {k: t[k] for k in ("id", "kind", "title", "summary", "file")}
        for t in _index()["templates"]
        if not kind or t["kind"] == kind
    ]


@mcp.tool(annotations=READ)
def recommend(goal: str, audience: str, format: str = "any") -> list[dict]:
    """Suggest the best template combinations for a request, with the reason for each.

    goal: report, decide, sell, teach, inspire or announce.
    audience: customer, executive, team, public or learner.
    format: page, deck, social, or any for the best one of each.
    """
    try:
        return catalog.recommend(goal, audience, format)
    except ValueError:
        allowed = {f: [k for k, _ in v] for f, v in catalog.FACETS.items()}
        raise ToolError(f"Use one value for each of these: {json.dumps(allowed)}")


@mcp.tool(annotations=READ)
def get_template(id: str, part: str = "options") -> dict:
    """One template. part='options' for what it is and what can be changed. part='starter' for a small
    complete file to copy and fill (decks and social formats). part='source' for its reference code."""
    t = next((t for t in _index()["templates"] if t["id"] == id), None)
    if not t:
        raise ToolError("No template with that id. Call list_templates to see the ids.")
    if part == "options":
        return dict(t, styles=_index()["social_styles"]) if t["kind"] == "social" else t
    if part == "source":
        return {"id": id, "note": "Reference code: one style block, the markup, one script. It is not a complete file. Shared styles and helpers are in base/source/shell.html. For a deck or a social format, part='starter' is complete.", "source": _read(t["source"])}
    if part == "starter":
        st = t.get("starter")
        if not st:
            return {"id": id, "note": "Pages and voices have no starter. Build on the skeleton below, and read part='source' for this template's markup and styles.", "files": {"skills/artifact-studio/assets/page-skeleton.html": open(os.path.join(SKILL, "assets", "page-skeleton.html"), encoding="utf-8").read()}}
        return {"id": id, "note": "Complete files with system fonts and no photograph. Copy, then replace the text. The comment at the top of each says how.", "files": {f: _read(f) for f in ([st] if isinstance(st, str) else st)}}
    raise ToolError("part must be one of: options, starter, source.")


@mcp.tool(annotations=READ)
def list_components(group: str = "") -> list[dict]:
    """List components. group is one of: page, photo, svg. Leave it empty for all."""
    return [{k: c[k] for k in ("id", "group", "name", "use")} for c in _index()["components"] if not group or c["group"] == group]


@mcp.tool(annotations=READ)
def get_component(id: str) -> dict:
    """One component: what it is for, the sentence that asks for it, and its code."""
    c = next((c for c in _index()["components"] if c["id"] == id), None)
    if not c:
        raise ToolError("No component with that id. Call list_components to see the ids.")
    out = dict(c)
    if c["group"] == "svg":
        out["code"] = _read(c["file"])
    else:
        view = _read(c["source"])
        for sec in re.findall(r'<section class="spec".*?</section>', view, re.S):
            m = re.search(r"<h2>(.*?)</h2>", sec)
            if m and m.group(1) == c["name"]:
                out["code"] = sec
                out["note"] = "The markup for this part. Its styles and script are in the same source file."
                break
    return out


@mcp.tool(annotations=READ)
def get_rules(which: str = "build") -> str:
    """The studio's written rules. which is one of: build, checklist, recipes, voices, looks, skill."""
    files = {"build": "references/build-rules.md", "checklist": "references/pre-ship-checklist.md", "recipes": "references/recipes.md",
             "voices": "references/voices.md", "looks": "references/looks.md", "skill": "SKILL.md"}
    if which not in files:
        raise ToolError("which must be one of: " + ", ".join(files))
    with open(os.path.join(SKILL, files[which]), encoding="utf-8") as f:
        return f.read()


@mcp.tool(annotations=READ)
def list_inspiration(tag: str = "") -> list[dict]:
    """The person's saved finds: designs they liked, described in their own words. Read these before you
    choose, because they are the person's taste. tag filters by one tag, such as deck, social or number."""
    folder = os.path.join(ROOT, "base", "inspiration")
    out = []
    for path in sorted(glob.glob(os.path.join(folder, "inbox", "*.md")) + glob.glob(os.path.join(folder, "*.md"))):
        if os.path.basename(path) in ("README.md", "card-template.md"):
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        row = lambda k: (re.search(rf"^\| {k} \| (.*?) \|$", text, re.M) or [None, ""])[1]
        tags = [t.strip().lower() for t in row("Tags").split(",") if t.strip() and t.strip() != "none"]
        if tag and tag.strip().lower() not in tags:
            continue
        sec = lambda h: (re.search(rf"^## {h}\n\n(.*?)(?=\n## |\Z)", text, re.M | re.S) or [None, ""])[1].strip()
        out.append({"file": os.path.relpath(path, ROOT), "title": (re.search(r"^# (.+)$", text, re.M) or [None, ""])[1], "filed": row("Filed"), "tags": tags,
                    "status": row("Status"), "what_works": sec("What works")[:1500], "closest": sec("Closest thing in the library")[:400], "decision": sec("Decision")[:400]})
    return out


def add_inspiration(title: str, what_works: str, source: str = "", tags: str = "") -> dict:
    """File a note about a design the person likes, for review later. Writes one small text file and nothing else.

    title: a few words. what_works: in your own words, the structure, rhythm or idea worth keeping.
    Describe the idea. Do not paste the original's text, artwork or code.
    source: where it was seen, as a link or a description. tags: comma-separated.
    """
    title = " ".join(title.split())[:80]
    if not title or not what_works.strip():
        raise ToolError("title and what_works are both needed")
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:50] or "note"
    folder = os.path.join(ROOT, "base", "inspiration", "inbox")
    os.makedirs(folder, exist_ok=True)
    name = f"{datetime.date.today().isoformat()}-{slug}.md"
    path = os.path.join(folder, name)
    n = 2
    while os.path.exists(path):
        path = os.path.join(folder, name[:-3] + f"-{n}.md"); n += 1
    card = (f"# {title}\n\n| | |\n| --- | --- |\n| Seen | {source.strip()[:300] or 'not recorded'} |\n| Filed | {datetime.date.today().isoformat()} |\n"
            f"| Tags | {', '.join(x.strip() for x in tags.split(',') if x.strip())[:200] or 'none'} |\n| Status | Inbox. Not reviewed |\n\n"
            f"## What works\n\n{what_works.strip()[:4000]}\n\n## Closest thing in the library\n\nNot yet compared.\n\n## Decision\n\nNot yet decided: keep as a note, adapt an existing template, or build a new part.\n")
    with open(path, "w", encoding="utf-8") as f:
        f.write(card)
    return {"saved": os.path.relpath(path, ROOT), "next": "A person reviews the inbox using base/inspiration/README.md."}


if "--read-only" not in sys.argv:                                               # the one tool that writes a file
    mcp.tool(annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=False))(add_inspiration)

if __name__ == "__main__":
    mcp.run("streamable-http" if "--http" in sys.argv else "stdio")
