# Level 3, Expert: your agents get the studio as tools

[Level 2](../level-2-files/), plus a connection. An MCP server lets an assistant or an agent
browse the library, get a scored recommendation and pull starter code by itself, so nobody has to
pick a template or attach a file.

**Think of it as** the studio's front desk. The assistant asks "what do you have for a customer
proposal?" and gets an answer, where before it had to be handed the files.

**Where it stands.** Tested with a client on the machine that built it, over stdio and local HTTP.
Not yet tried inside a desktop assistant or over the internet. Nothing is hosted, so there is no
one-click connector yet.

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

## Set it up on your own computer

You need Python 3.10 or later.

```
pip install "mcp>=2"
python mcp/server.py
```

The second line should sit and wait. That means it is working. Stop it with Ctrl+C.

For a desktop assistant that runs local servers, such as Claude Desktop, add this to its MCP
settings, with the real path:

```json
{
  "mcpServers": {
    "artifact-studio": {
      "command": "python",
      "args": ["/full/path/to/artifact-studio/level-3-files/mcp/server.py"]
    }
  }
}
```

Where that settings file lives changes between versions. Check the assistant's own help for "MCP
server".

## Use it from an assistant on the web

An assistant that runs on someone else's computers cannot reach a file on yours. It needs a web
address.

```
python mcp/server.py --http --read-only
```

This serves the same tools at `http://127.0.0.1:8000/mcp`. To use it from the web you must put it
at an HTTPS address, by hosting it or by using a tunnel, and then add that address as a custom
connector.

**This server has no sign-in.** Anyone who has the address can call it. Use `--read-only` whenever
it is reachable from outside your computer, and take the address down when you are done.

## Check it works

```
python mcp/test_client.py
```

This starts the server, calls every tool through a real client and prints what came back.

## What is in `mcp/`

| File | What it is |
| --- | --- |
| `server.py` | The server |
| `catalog.py` | The rules that choose a template. A copy the build makes |
| `library/` | What the tools return: `index.json`, reference code in `sources/`, and the animated SVG parts in `svg/`. Written by the build |
| `inspiration/` | Where a design you liked is filed as a card |
| `test_client.py` | The check above |

The server also reads the skill in [`../level-2-files/artifact-studio/`](../level-2-files/artifact-studio/)
for the rules and the starter files, so keep the two folders together.

## What stays manual at every level

Checking numbers, names and quotes. Answering the gaps the assistant lists. Deciding what is
published.
