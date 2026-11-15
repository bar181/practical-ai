# The studio becomes a library

A report on two hours of work on the artifact studio, 15 November 2026. Eight additions were
proposed. Each was scored, all eight were built, and this page says what exists, how to use it
and what nobody has checked yet.

**Think of it as** a shop that used to have a good window display. It now has shelves, a
catalogue, someone at the counter who can recommend, a suggestions box, and a side door for
deliveries.

## The short version

- The studio is now a **template library** with an index: 18 templates, 36 parts, 9 looks.
- It makes **decks and social posts** as well as pages.
- It can **pick for you**: say the job, the reader and the shape, and it names the best
  combination and says why.
- An assistant can use it **as tools**, through an MCP server.
- Agents have a **front door**: `AGENTS.md`.
- New ideas have a **way in** that does not copy anyone's work.
- Everything passes its automated checks. **Nothing new has been used by a person on a real job.**

## What was proposed, and the verdict

Scores are the author's, out of 100, for value to this product.

| Proposal | Score | Verdict | What was built |
| --- | --- | --- | --- |
| A templates folder with an index | 92 | Built | `base/templates/`, with one index for people and one for agents, both generated from the templates |
| Options listed for each template, linked from an index | 88 | Built | Each template in the index carries what can be changed, its fit scores and the sentence that asks for it |
| Recommend outputs from requirements | 84 | Built | Rules in one file, used by a Pick tab, an MCP tool and the skill |
| An MCP server and a front door for agents | 82 | Built, partly proven | Eight tools, tested with a client. `AGENTS.md`. Not yet tried in a real assistant |
| More than pages: decks, social formats | 80 | Built | Two decks on one engine. Five social formats as seven pictures, with PNG download |
| Animated SVG and other formats | 80 | Built | Twelve SVG files with no script, and eleven GIF copies |
| A way to take in new components and inspiration | 78 | Built, unused | A card, a process, an MCP tool. No real find has been through it |
| A list of outside skills, open source and services | 70 | Built | One dated page. Prices left out because sources disagreed |

All eight were worth doing. The lowest score went to the outside list, because it starts going
stale the day it is written.

## How it fits together

```mermaid
flowchart TD
  A[1. A request: the job, the reader, the shape] --> B[2. Pick: scores in the catalogue choose a combination]
  B --> C[3. Read the template's reference code and the rules]
  C --> D[4. Build one file from the person's own content]
  D --> E[5. Check against the checklist]
  E --> F[6. Return the file and a delivery note]
```

| Piece | Where | In one line |
| --- | --- | --- |
| Library | `base/templates/` | Every template and part as a working file |
| Index | `base/templates/README.md` and `index.json` | The list, for people and for agents. Generated, so it cannot drift |
| Catalogue | `base/source/catalog.py` | Fit scores and the rule that picks. One file feeds the page, the server and the index |
| Studio page | `base/studio.html` | Everything in tabs, with a picker |
| Skill | `skills/artifact-studio/` | How an assistant builds and checks |
| Agents' door | `AGENTS.md` | Seven steps from request to file |
| Intake | `base/inspiration/` | How a design you like becomes a note, a change or a new part |
| Outside help | `base/RESOURCES.md` | What to use when the studio is the wrong tool |
| Tools | `level-3/mcp/` | The library as eight tools an assistant can call |

## What is in the library

| Kind | Count | Examples |
| --- | --- | --- |
| Pages | 4 | Report, proposal, scrolling explainer, landing page |
| Voices | 7 | Keynote, storyteller, teacher, pitch, practical instructor, analyst, executive brief |
| Decks | 2 | Visionary (black, one idea a slide), story (the customer as hero). Each has speaker notes and prints to PDF |
| Social formats | 5 | Square, portrait stat, story, three-slide carousel, link preview |
| Page parts | 12 | Big numbers, timeline, price table, questions |
| Photo parts | 12 | Pan and zoom, scrolling tour, line art |
| Animated SVG | 12 | Line that draws, bars that grow, ring, tick, pulse, flow. Eleven also come as GIF |
| Looks | 9 | Clean, cinematic, dashboard, editorial, keynote black |

These counts are written by the build, not typed.

## How you would use it

**You need a deck for a room on Thursday.**

1. Open the studio page, tap Pick, choose "make people feel a change", "my own team", "a slide deck".
2. It suggests the visionary deck and says why. Tap to open it and page through.
3. Copy the sentence under it, paste it into your assistant with your notes.
4. Present the file from a browser with the arrow keys.

**You need a week of posts from one result.**

1. Open Social. Seven pictures show the same message cut to five shapes.
2. Copy the full ask, paste it with your notes and your colours.
3. Download each picture as a PNG.

**You see a page you admire.**

1. Tell your assistant what you saw and why it works, in your own words.
2. It files a card in the inspiration inbox.
3. Later you decide: keep the note, adjust a template, or build a new part.

**You want your assistant to do the choosing.**

1. Start the MCP server and add it to your assistant.
2. Say "I need something to win over a customer". The assistant calls `recommend`, reads the
   template and the rules, and builds.

## What was checked

| Check | Result |
| --- | --- |
| Every tab of the studio page and every template file, at three widths | 57 of 57 checks clean: 19 files at 320, 390 and 1280 pixels wide. No script errors, no sideways scrolling, one view showing, no empty photo frame |
| The same with scripts turned off | Each page shows its content. The studio's tabs still switch |
| Accessibility scan (axe-core, WCAG 2 A and AA) | No violations. An automated scan covers part of the standard |
| The picker in the page against the same rules in Python | The same answer for all 120 combinations of goal, reader and shape |
| The decks | Buttons and arrow keys move between slides, and Notes shows what to say. With scripts off the slides are a readable column |
| Printing a deck to PDF | The visionary deck gives 8 pages and the story deck 7, one slide each, with its text |
| Social pictures saved as PNG | Full size, with the fonts inside. Square 1080 by 1080, story 1080 by 1920, link preview 1200 by 630 |
| The MCP server | All eight tools called through a real client. A wrong input returns a message saying what to send. It also starts over HTTP |
| Links in every Markdown file in the repository | No broken links |

## What was not checked

- **Any real use.** Nobody has presented a deck, posted a picture or filed a real find.
- **The MCP server inside an assistant.** It has only met a test client on the machine that
  built it. Nothing is hosted, so ChatGPT cannot reach it yet.
- **The fit scores.** They are the author's judgement. They produce sensible answers and have not
  been compared with what people would choose.
- **A phone, Safari or Firefox.** Chrome only.
- **The outside list.** Read from comparison sites in one sitting. Nothing on it was installed.

## Self-score

| Item | Score | Why |
| --- | --- | --- |
| One place for each thing, one source of truth | 86 | The catalogue feeds the index, the page and the server. Two indexes are generated |
| Usable by an agent | 82 | A front door, a machine index and tools. Unproven inside a real assistant |
| Correct and checked | 84 | Automated checks pass. They cannot judge taste |
| Honest and current documents | 85 | Every status line says who has and has not tried it |
| Usable today by a person | 80 | Open, pick, copy, ask. The first run by someone else will find something |
| Range and quality of templates | 74 | Two decks and one family of social pictures is a start |
| Evidence from real use | 35 | The owner has looked at the pages. Nothing else |

**Overall 75**, the plain average of the seven. The number that matters is the last one.

## Better ways found along the way, and done

- **One catalogue file.** The first draft had the picking rules in the page and again in the
  server. They now live in one file, and a test proves the page agrees with it.
- **Styles scoped inside each SVG.** As first written, pasting two of them into one page would
  have made them fight over class names. Each now keeps to its own id.
- **GIF copies.** SVG is not accepted in email or in some slide tools.
- **A read-only switch on the server.** Seven tools only read. The eighth writes a file, and can
  be left out when the server is reachable from outside.
- **Errors that teach.** A wrong word to `recommend` returns the list of right ones.
- **Slides that are a page first.** A deck is a readable column until its script runs.
- **A deck that prints.** One slide a page, for a handout.
- **Notes for the speaker.** Each slide carries a line on what to say. Tap Notes or press N.
- **Counts the build writes.** The numbers in the READMEs are counted from the library each time it is built, so they cannot be wrong.

## Decisions waiting for you

| Decision | Options | Recommendation |
| --- | --- | --- |
| The name | Keep "artifact studio", or rename now that it makes decks and posts | Keep it until someone other than us is confused by it |
| Hosting the server | Leave it local, or put it at a web address so ChatGPT can use it | Try it in a desktop assistant first. Host only after that works, and with a sign-in |
| The fit scores | Leave them, or tune them | Run five real requests through the picker and change the scores that gave a wrong answer |
| The other nine tools | Convert them to the base-plus-levels layout, or leave them | Convert once this one has been used for a real job |
| Three level artifacts from the first night | Delete or leave | Delete. They describe a layout that no longer exists |

## What to do first

1. Open the studio artifact on your phone and tap through Decks, Social and Pick.
2. Give your assistant one real set of notes and the short ask for a deck.
3. Add the MCP server to a desktop assistant and ask it to recommend something.

Each takes under ten minutes, and each replaces a guess in this report with a fact.
