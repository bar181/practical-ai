# Build files

You do not need this folder to use the studio. It is what the studio is built from.

```
python3 build.py
```

That rebuilds `../base/studio.html`, `../base/AI-INSTRUCTIONS.md`, the starter files in the skill,
and the library the MCP server reads. It needs Python and the `markdown` package.

| Here | What it is |
| --- | --- |
| `catalog.py` | Every template, its fit scores and the rules that pick between them. The one source |
| `views/` | One file per tab of the studio page: style, markup, script |
| `shell.html`, `base.css` | The page frame and shared styles |
| `svg/` | The twelve animated SVG parts |
| `forms/`, `sentences.md` | Text shown as tabs in the studio page. `sentences.md` is written by the build |
| `assets.json` | Fonts and photographs, already encoded, so the build needs nothing else |
| `photos/`, `prepare_assets.py` | The ten pictures. `prepare_assets.py` encodes the lake and the sunset into `assets.json`; `build.py` reads the other eight straight from this folder, and each becomes a CSS variable named `--ph-NAME` |
| `licences/` | The licence for each embedded font |
| `img/` | The pictures on the landing page |
| `build.py` | The build |

`base/example.html` is written by hand on the skill's page skeleton and is not rebuilt.

## Credits and licences

- Pictures: `lake.jpg` and `sunset.jpg` are photographs taken by the repository owner. The other eight were supplied by the owner as finished images. All are stored without location or camera data.
- Fonts: National Park, Crimson Pro, Instrument Sans, JetBrains Mono, Gloock, Big Shoulders, Work
  Sans and IBM Plex Serif, embedded as subsets under the SIL Open Font License 1.1.
- Code: Apache-2.0.

The tests and the earlier, larger layout are in the repository's history.
