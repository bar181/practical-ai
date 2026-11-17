# Two tools for better work with your AI

<p align="center">
  <img src="../assets/images/practical-ai-pitch.svg" width="720" alt="Animation: Practical AI, better work from the AI you already use, with a proven process for the jobs you repeat, and faster. Two tools light up in turn. Artifact Studio, design for your reports: rough notes in, a report, deck or post out. Agentic Process, structure for repeat jobs: a job you repeat in, a tested tool out. The AI drafts; you check and decide.">
</p>

<h3 align="center">Better results on the jobs you repeat, every time, and faster.</h3>

<p align="center"><b>Want your reports to look professional?</b> Artifact Studio. &nbsp;·&nbsp; <b>Repeat a job with AI and want it done the same way every time?</b> Agentic Process.</p>

Neither replaces the features, plugins or skills already in your AI. Each adds what they are
missing for one practical job.

## Artifact Studio: professional design for the reports your AI already makes

**Your AI can already make scrollytelling pages, photo effects, animated diagrams, a visionary
keynote or a lesson to teach from.** Most people never ask, because they do not know these exist.
Artifact Studio puts them on a menu: name one in a sentence, and your AI adds the design. The same
notes become a presentation, a lesson or a report, fitted to the reader.

<p align="center">
  <a href="artifact-studio/"><img src="artifact-studio/_build/img/style-visionary-page.webp" width="49%" alt="Animated screen capture of the visionary page on a phone: black screens of huge white type, a house in fog behind the words, a dog at a laptop beside the words Meet your smart intern, and bars that count what is in the library"></a>
  <a href="artifact-studio/"><img src="artifact-studio/_build/img/style-emotional.webp" width="49%" alt="Animated screen capture of the emotional page on a phone: the line My mother kept a drawer in italic type, three keepsakes shown as crooked photographs with handwritten captions, then a painted portrait filling the screen"></a>
</p>

**The captures, in words:** the same idea told two ways. Left, a keynote: one idea per screen in
huge type. Right, a personal story: one memory, a few keepsakes, the offer only at the end.

<p align="center"><a href="artifact-studio/"><b>See what it makes</b></a></p>

## Agentic Process: a mini harness for work that is not code

**Developers give AI coding agents a harness: a spec, steps and tests.** Everyday work with AI has
none of that. Agentic Process adds it to the jobs you repeat: a clear result, written steps, the
one mistake to catch, and a test in a fresh session before you rely on it.

<p align="center">
  <a href="agentic-process/"><img src="agentic-process/_build/img/pilot-brief-direct.webp" width="49%" alt="Screen capture of a reply from a tool built the usual way: the facts of a supplier notice in a table, with the missing effective date buried among them"></a>
  <a href="agentic-process/"><img src="agentic-process/_build/img/pilot-brief.webp" width="49%" alt="Screen capture of a reply from the tool built with Agentic Process: a warning first that the notice never gives its effective date and leaves out a form, and who to ask"></a>
</p>

**In one blind pilot, a tool built with Agentic Process scored 93/100. The direct-build version
scored 73/100 on the same brief.** Left, the usual build buries the missing date. Right, Agentic
Process warns first and says who to ask. One task, one notice, one blind reviewer.

<p align="center"><a href="agentic-process/"><b>See how it works</b></a></p>

## Side by side

| | Artifact Studio | Agentic Process |
| --- | --- | --- |
| **Adds to your AI** | Design it already supports but you would not know to ask for | Structure: a clear result, written steps, a test |
| **You bring** | Your notes, and who will read them | A job you repeat, and who uses the result |
| **You get** | A report, deck, post or page | A tested tool, a guide and a real example |
| **Works with** | The chatbot you already use | A coding agent, or any chatbot by hand |
| **Proof** | [22 fresh-session runs](artifact-studio/quality-results/README.md) | [The blind pilot](agentic-process/quality-results/README.md) |

Both were built and checked by their author, in Claude. Nobody else has used them yet.

<details>
<summary>How every project is laid out</summary>

`base/` is enough to try the tool. The other folders appear only when they hold something you can use.

```
a-project/
  README.md          the landing page: the value, examples, Get started, Status
  AGENTS.md          instructions for AI agents
  CLAUDE.md          points Claude Code at AGENTS.md
  LICENSE
  base/              the few files you need to try it, and examples/
  level-2-files/     Advanced: what you add to make it yours
  level-3-files/     Expert: connections for agents
  quality-results/   the evidence: what was checked, by whom, with the raw results
  _build/            what the project is built from. Not needed to use it
```

`python3 workshop/tools/check_project.py projects/<name>` checks a folder against this.

</details>
