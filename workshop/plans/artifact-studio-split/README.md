# Plan: split Artifact Studio into three projects

Written on 20 and 21 November 2026 at the owner's request. It covers the evaluation, the decisions,
the order of work and a checklist of every folder and file that changes. Each checkbox is ticked
only when the change is in the branch and the checks pass.

**Think of it as** a film crew. Web Sections is the set builder: walls, doors and rooms in the right
place. Tone Studio is the writer: what is said, in what order, to whom. Artifact Studio is the
cinematographer: light, colour, movement. One person can still shoot a whole film alone, but each
craft now has its own room, its own tools and its own examples.

## The proposal in one line each

| Project | Job | Level 1 | Level 2 | Level 3 |
| --- | --- | --- | --- | --- |
| **Artifact Studio** (project 1, kept) | Design and style: looks, effects, components, motion | A basic artifact from a paste-in skill | Your brand: logo, colours, fonts | Design from intent through one entry point (skill front door or MCP) |
| **Tone Studio** (new) | The words: tone, story order, structure of the argument | One source rewritten in the tone that fits the reader | A custom tone or brand voice, saved | Tone plus Artifact Studio design, from intent |
| **Web Sections** (new) | The structure: responsive sections and post formats to start from | Pick the sections for a site or page and get the skeleton | Your own section set, saved | Sections, tone and design chained |

The order a person or an agent works in: **structure** (Web Sections), then **words** (Tone Studio),
then **design** (Artifact Studio). Each project still works alone.

## Evaluation

**Score: 84 out of 100. Do it, as an additive split, in two phases.**

| Item | Score | Why |
| --- | --- | --- |
| Clarity of each project's job | 90 | Structure, words, design is how professional web work is already divided: wireframe, copy, visual design. Each project can say what it does in one line |
| Fit with the repository rule "each tool does one job" | 92 | Artifact Studio today does four jobs: 37 views, 339 files, two master pages that mix voices, recipes, decks, social posts and effects |
| Value at Level 1 | 82 | Tone Studio is useful with no design at all: most people need better words before better pixels. Web Sections at Level 1 is useful for anyone starting a site. The risk is that three projects feel like more work than one |
| Reuse | 85 | Tone Studio reuses the seven voice cards and four deck manners. Its Level 2 reuses Write and edit in my voice. Web Sections reuses the social formats and the site's section patterns. Free section libraries already exist; ours is the AI-ready, single-file version with a skill, not a competitor |
| Risk to what works | 70 | Artifact Studio is in user testing. Its try-it prompt, its build, the Pages site and the MCP server all depend on one catalogue. Moving files out in one step would break them. Hence the additive first phase |
| Maintenance | 80 | Three projects can drift apart: the same voice written twice. One owner per thing fixes it (below) |
| Effort in this session | 85 | Phase 1 fits in two hours. Phase 2 needs its own session |

**The three honest risks, and what this plan does about each**

1. **Three projects to make one page.** A beginner will not chain three skills. Artifact Studio
   keeps its one-paste front door that makes a whole page, and the other two are where you go
   for depth. Level 3 is where the chain is automatic.
2. **The same content in two places.** Each thing gets one owner. Tone Studio owns the voice and
   story cards. Web Sections owns section blocks and post formats. Artifact Studio owns looks,
   effects, components and motion, and keeps finished examples that show all three together,
   because a design example needs real words.
3. **Breaking a project in user testing.** Phase 1 adds and links; nothing the testers use moves.
   Phase 2 moves files out only after the new projects pass their own tests.

## Decisions

| Decision | Choice | Reason |
| --- | --- | --- |
| Names | Artifact Studio, Tone Studio, Web Sections | The first is known to testers. The other two say what they hold in plain words |
| Artifact Studio's name and front door | Unchanged | Testers and the root README link to it |
| Voice cards | Owned by Tone Studio from Phase 2. In Phase 1 both copies exist and Tone Studio's is the fuller one | Moving the file breaks the Artifact Studio build, which reads it |
| The seven voice examples and four decks in Artifact Studio | Stay as design examples | The owner asked for good tone examples inside project 1 |
| Social formats and post previews | Copied to Web Sections in Phase 1; removed from Artifact Studio in Phase 2 | They are structure, not style. Removing them needs build, catalogue and MCP changes |
| Recipes (report, proposal, explainer, landing) | Stay in Artifact Studio as finished designs. Web Sections holds the bare skeletons | A recipe is the finished dish; a section is the ingredient |
| New effects from the website | Added to Artifact Studio as a new tab, "Cinematic effects", and an effects index by use case | They are design |
| Tone Studio Level 2 | Uses Write and edit in my voice for a person's own voice, and adds a brand tone file | Reuse first |
| Web Sections quality bar | Clean, responsive, accessible, no build step. Not state of the art | The owner's call. Many fine section libraries exist; this one is for an AI to start from |

## Phase 1 (this session): add, link, do not break

Create the two new projects with working Level 1 skills, examples and tests. Add the website's
cinematic effects to Artifact Studio with an effects index. Point each project at the others.
Nothing that Artifact Studio's testers use moves. The checklist below marks what is in Phase 1.

## Phase 2: move and slim

**Done on 21 November 2026:** post previews moved to Web Sections (views, reference, run, page);
Artifact Studio's skill, agent file and README now describe the design step only; its voice cards
defer to Tone Studio for the words; 18 unused images, six unread files and two duplicate reports
deleted; a build bug fixed (`sys` was never imported); the four new tools added to the website;
Web Sections published on the Pages site; a shared design-set diagram and full visual headers on
all three READMEs. **Decided against for now:** splitting Artifact Studio's skill into one skill per
effect family. A newcomer would have more to load and choose; the effects index routes by job
instead. **Still open:** items 3 to 5 below, and the social picture sizes, which stay in Artifact
Studio as well because its catalogue, picker and MCP server depend on them.



1. Remove social formats and post previews from Artifact Studio: views 02, 85 to 92, the social
   starters, the catalogue's social entries, the MCP library copies, `post-previews.md`, and the
   README gallery section. Point every link to Web Sections.
2. Make Tone Studio the owner of the voice cards. Artifact Studio's build reads a short voice
   table (name, look, effects) and links to Tone Studio for the rest.
3. Split Artifact Studio's skill into a master "design from intent" skill and small skills per
   effect family (photo, scroll, cinematic, charts), with the effects index as the router.
4. Level 2 brand kit for Artifact Studio: logo, colours and fonts in one file, applied to every
   output, tested with an invented brand.
5. Level 3: one entry point that takes an intent and chains Web Sections, Tone Studio and Artifact
   Studio. Decide then between an MCP tool and a skill front door.
6. Rebuild the Pages index so each project has its own gallery, and add Tone Studio and Web Sections to the Bradley Academy site's tool list.
7. Rerun the Web Sections tests with the placeholder box, and the Tone Studio t2 and t3 tests with the new rules.

## Checklist: every folder and file

Legend: **A** add, **C** change, **M** move, **D** delete. Phase 1 unless marked.

### Artifact Studio (`projects/artifact-studio/`)

- [x] C `README.md`: says it is the design project; a "Where the words and structure come from" note linking Tone Studio and Web Sections; the new cinematic effects in the gallery; status line kept true
- [x] C `AGENTS.md`: routes tone work to Tone Studio and section work to Web Sections; names the effects index
- [x] A `_build/views/23-cinema.html`: the cinematic effects tab (split-word titles, sticky statement, clip reveal, card stack, letterbox and grade, film grain, credits, page transitions), each with a use case and the sentence that asks for it
- [x] C `_build/build.py`: registers the new tab in the showcase, with its label, file and title
- [x] C `showcase.html`, `components.html`, `base/`: rebuilt by `build.py` (generated)
- [x] A `level-2-files/artifact-studio/references/effects-index.md`: every effect by use case, where it is shown, how to ask for it
- [x] C `level-2-files/artifact-studio/SKILL.md` and `SKILL-single-file.md`: hand tone to Tone Studio and structure to Web Sections when they are loaded; point to the effects index
- [x] C `level-3-files/mcp/library/skill/`: the same skill copy, kept in step (the MCP serves it)
- [x] C `quality-results/README.md`: what was checked for the new tab
- [ ] Phase 2: register the cinematic effects in the catalogue and the MCP library index. D social views and starters; C catalogue, MCP library, `post-previews.md`; C skill split; A brand kit

### Tone Studio (`projects/tone-studio/`, new)

- [x] A `README.md`, `AGENTS.md`, `CLAUDE.md`, `LICENSE`
- [x] A `base/SKILL.md`: tone from intent; the seven tones and the story orders; four deck manners; executive one-pager, investor deck and HTML slide show outlines; facts kept
- [x] A `base/examples/`: three worked examples (investor deck, board one-pager, goodbye email) from the test runs, with a link to the designed voice examples in Artifact Studio. Deviation: three tones shown, not all seven
- [x] A `level-2-files/README.md` and `brand-tone-template.md`: a custom tone, reusing Write and edit in my voice
- [x] A `_build/eval/`: test cases and answer keys
- [x] A `quality-results/README.md` and the fresh-run replies
- [x] A `workshop/plans/tone-studio/README.md`

### Web Sections (`projects/web-sections/`, new)

- [x] A `README.md`, `AGENTS.md`, `CLAUDE.md`, `LICENSE`
- [x] A `base/SKILL.md`: pick the sections for the intent, then fill them; responsive rules; no invented facts
- [x] A `base/template/sections.html`: one self-contained library page: six heroes, gallery, about, features, steps, testimonial slot, pricing, questions, contact, footer, and three page assemblies
- [x] A `base/template/social/`: the seven social format starters, copied from Artifact Studio. The post previews (LinkedIn and others) stay in Artifact Studio until Phase 2
- [x] A `base/examples/`: one invented business assembled from the sections
- [x] A `level-2-files/README.md` and `section-set-template.md`: your own saved section set
- [x] A `_build/eval/`, `quality-results/README.md` and the fresh-run replies
- [x] A `workshop/plans/web-sections/README.md`

### Repository

- [x] C `AGENTS.md`: two new route rows; Artifact Studio's row says design
- [x] C `README.md`: the project list and a short line on the three-step flow
- [x] C `docs/README.md`: the two new projects and their status
- [x] C `workshop/plans/README.md`: the two new rows and this plan
- [x] Check `workshop/tools/build_site.py` and `.github/workflows/pages.yml`: no change needed in Phase 1, because no Artifact Studio file moves
- [x] Run `check_links.py .` and `check_project.py` for all three projects

## How it is verified (the loop)

1. Rebuild Artifact Studio and confirm the generated files carry their header and the workflow's
   "pages match their source" step would pass.
2. Open the new tab and the sections library in a browser at phone and desktop width, with
   reduced motion on and with scripts off; fix and repeat.
3. Run each new skill in fresh agents on invented cases, grade against answer keys, fix the skill,
   rerun.
4. Run the link and layout checks until both pass.
