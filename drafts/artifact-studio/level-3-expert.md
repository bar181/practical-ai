# Level 3, Expert: your agents get the studio as tools

Level 2, plus a connection. An MCP server lets an assistant or an agent browse the library, get a
scored recommendation and pull starter code by itself, so nobody has to pick a template or attach
a file.

**Think of it as** plumbing. The kitchen works with buckets. Pipes save carrying, and a badly
fitted pipe floods the floor, so each one is tested before it is trusted.

**One connection is built.** It has been tested with a client on the machine that built it, over
stdio and local HTTP. It has not yet been tried inside a desktop assistant or over the internet.
Nothing is hosted.

## What the assistant can do

| Tool | What it returns | Writes anything? |
| --- | --- | --- |
| `studio_overview` | Counts, the kinds of template, the words to use for goal, audience and format | No |
| `recommend` (each answer says strong, fair or weak, and a weak one names a better shape) | The best combinations for a goal, an audience and a format, with the reason for each | No |
| `list_templates` | Every template, or one kind | No |
| `get_template` | One template's options, a small complete starter file to copy and fill, or its reference code | No |
| `list_components` | Page parts, photo parts and animated SVG files | No |
| `get_component` | One part: its use, the sentence that asks for it, and its code | No |
| `get_rules` | The build rules, the checklist, or the recipe, voice and look cards | No |
| `make_palette` | Seven colours from one brand colour, with the contrast of every text and background pair | No |
| `list_inspiration` | The person's saved finds, in their own words, so their taste shapes the choice | No |
| `add_inspiration` | Files a short note about a design you like in `base/inspiration/inbox/` | One small text file |

Start the server with `--read-only` to leave the last tool out.

## Set it up

Everything is in [`base/connectors/mcp/`](base/connectors/mcp/). Its
[README](base/connectors/mcp/README.md) has the steps for a desktop assistant and for an assistant
on the web.

```
pip install "mcp>=2"
python base/connectors/mcp/server.py               # local, over stdio
python base/connectors/mcp/server.py --http --read-only   # over HTTP, with the one writing tool removed
```

## Why it is built this way

| What you get | Why it matters |
| --- | --- |
| A recommendation with a strength | Every answer is rated strong, fair or weak. When the shape someone asked for is a weak fit, the tool names a better one |
| Selection you can read and change | A template's score is three times its goal fit plus twice its audience fit. The numbers are in [`base/source/catalog.py`](base/source/catalog.py) |
| One source of truth | The studio page, both indexes, the skill and the server all read one catalogue. Tests prove the page and the server give the same answers |
| Safe by default | `--read-only` removes the one tool that writes |

## Connections not yet built

| Connection | What it would do | Needs |
| --- | --- | --- |
| Content in | Read notes, documents or a spreadsheet from where they live | A connector to your file store |
| Brand in | Read colours, type and logo from your design system | A connector to that tool |
| Page out | Put the finished page at a web address | A hosting route |
| One-step install | The skill, the preferences file and a command as one plugin | An assistant that supports plugins |
| On a schedule | Rebuild a page from fresh content each week and wait for approval | Scheduled tasks, and "content in" |

A new connection is added only after it has been walked end to end once on real content, says what
it depends on and what it may do, stops for a person before anything is sent or published, and
leaves level 2 working when it is taken away.

## What stays manual at every level

Checking numbers, names and quotes. Answering the gaps the assistant lists. Deciding what is
published.
