# Build files

You do not need this folder to use the studio. It is what the studio is built from.

```
python3 build.py
```

That rebuilds the two master pages, `../showcase.html` and `../components.html`, the nine worked
examples in `../base/examples/`, `../base/AI-INSTRUCTIONS.md`, the starter files in the skill and
the library the MCP server reads. It needs Python and the `markdown` package. The Pages workflow
runs it and fails if the committed pages differ from their source.

| Here | What it is |
| --- | --- |
| `catalog.py` | Every template, its fit scores and the rules that pick between them. The one source |
| `views/` | One file per tab of the master pages: style, markup, script. `build.py` lists the tabs and which views also become worked examples. The post preview views moved to Web Sections on 21 November 2026 |
| `examples/runs/` | Every recorded run: the prompt, the reply and the page, plus friction notes. The worked examples are built from `runs/*/prompt.txt` and `out.html`. [Index](examples/runs/README.md) |
| `capture_tryit.py` | Captures the try-it prompt's page as the animated picture on the README |
| `shell.html`, `base.css` | The page frame and shared styles |
| `svg/` | The twelve animated SVG parts |
| `forms/`, `sentences.md` | Text shown as tabs in the studio page. `sentences.md` is written by the build |
| `assets.json` | Fonts and photographs, already encoded, so the build needs nothing else |
| `photos/`, `prepare_assets.py` | The sixteen pictures, and a small portrait of the creator for the note at the foot of each page. `prepare_assets.py` encodes the lake and the sunset into `assets.json`; `build.py` reads the other fourteen straight from this folder, and each becomes a CSS variable named `--ph-NAME` |
| `licences/` | The licence for each embedded font |
| `img/` | The pictures on the landing page |
| `build.py` | The build |

Each worked example's finished page was made by a fresh AI session from its prompt, unedited. The build wraps it with the prompt and the sample input.

## Credits and licences

- Pictures: `lake.jpg` and `sunset.jpg` are photographs taken by the repository owner. The other fourteen were made by the owner with AI image tools. All are stored without location or camera data.
- Fonts: National Park, Crimson Pro, Instrument Sans, JetBrains Mono, Gloock, Big Shoulders, Work
  Sans and IBM Plex Serif, embedded as subsets under the SIL Open Font License 1.1.
- Code: Apache-2.0.

The tests and the earlier, larger layout are in the repository's history.
