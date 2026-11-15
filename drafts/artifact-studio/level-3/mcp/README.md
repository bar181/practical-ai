# The studio as tools: an MCP server

A small server that lets an assistant use the template library directly. It reads
[`base/templates/index.json`](../../base/templates/index.json), so it always matches the library.

**Think of it as** the studio's front desk. The assistant asks "what do you have for a customer
proposal?" and gets an answer, where before it had to be handed the files.

## What the assistant can do

| Tool | What it returns | Writes anything? |
| --- | --- | --- |
| `studio_overview` | Counts, the kinds of template, the words to use for goal, audience and format | No |
| `recommend` | The best combinations for a goal, an audience and a format, with the reason for each | No |
| `list_templates` | Every template, or one kind | No |
| `get_template` | One template's options, or its reference code | No |
| `list_components` | Page parts, photo parts and animated SVG files | No |
| `get_component` | One part: its use, the sentence that asks for it, and its code | No |
| `get_rules` | The build rules, the checklist, or the recipe, voice and look cards | No |
| `add_inspiration` | Files a short note about a design you like in `base/inspiration/inbox/` | One small text file |

Start the server with `--read-only` to leave the last tool out.

## Set it up on your own computer

You need Python 3.10 or later.

```
pip install "mcp>=2"
python server.py
```

The second line should sit and wait. That means it is working. Stop it with Ctrl+C.

Then tell your assistant about it. For desktop assistants that run local servers, such as Claude
Desktop, add this to the assistant's MCP settings, with the real path to this file:

```json
{
  "mcpServers": {
    "artifact-studio": {
      "command": "python",
      "args": ["/full/path/to/drafts/artifact-studio/level-3/mcp/server.py"]
    }
  }
}
```

Where that settings file lives, and what the menu is called, changes between versions. Check the
assistant's own help for "MCP server".

## Use it from an assistant on the web, such as ChatGPT

An assistant that runs on someone else's computers cannot reach a file on yours. It needs a web
address.

```
python server.py --http --read-only
```

This serves the same tools at `http://127.0.0.1:8000/mcp`. To use it from the web you must put it
at an HTTPS address, by hosting it or by using a tunnel, and then add that address as a custom
connector. What ChatGPT needs for that is in [`base/RESOURCES.md`](../../base/RESOURCES.md).

**This server has no sign-in.** Anyone who has the address can call it. Use `--read-only` whenever
it is reachable from outside your computer, and take the address down when you are done.

## Check it works

```
python test_client.py
```

This starts the server, calls every tool through a real client and prints what came back.

## What has and has not been tested

| | |
| --- | --- |
| Every tool, through the SDK's client, over stdio | Done, 2026-11-15, with `mcp` 2.3.0 |
| A wrong input returns a message that says what to send | Done |
| The server starts over HTTP and answers a first request | Done, on the same machine |
| Inside Claude Desktop or any desktop assistant | **Not done** |
| At an HTTPS address, from ChatGPT or any web assistant | **Not done.** Nothing has been hosted |
| With a sign-in | Not built |

## What stays manual

The server chooses and describes. It does not build the page, and it never sends or publishes. A
person reviews the inspiration inbox.
