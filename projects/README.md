# Projects: two tools, ready to use

<p align="center">
  <img src="../assets/images/practical-ai-pitch.svg" width="720" alt="Animation: Practical AI saves time on the work you repeat, with one file for the chatbot you already use, a guide and a worked example. Two projects light up in turn. Artifact Studio: rough notes in, a report, deck or post out. Agentic Process: a job you repeat in, a tested README, SKILL.md and example out. The AI drafts; you check and decide.">
</p>

<h3 align="center">Pick the one that matches what you want to do today.</h3>

<p align="center"><b>Have notes to share?</b> Make your first report. &nbsp;·&nbsp; <b>Build with a coding agent?</b> Build a tool.</p>

## Make your first report: Artifact Studio

**For anyone with rough notes and something to share.** Paste one prompt into the chatbot you
already use and get a one-page report your reader takes in on a phone. Then the same notes as a
slide deck, a social post or a page that opens with your photo.

<p align="center">
  <a href="artifact-studio/"><img src="artifact-studio/_build/img/example-report.webp" width="49%" alt="Screen capture of a one-page monthly report made by an AI chatbot from eight lines of invented notes: the headline October beat September, three key numbers and a bar chart"></a>
  <a href="artifact-studio/"><img src="artifact-studio/_build/img/social-three-drafts.webp" width="49%" alt="Screen capture of three drafts of one LinkedIn post side by side, as they would look in a feed, each with its own opening and picture"></a>
</p>

**The pictures, in words:** left, a report an AI chatbot made from eight lines of notes, unedited.
Right, three drafts of one post from the same notes, shown the way the feed will show them.

<p align="center"><a href="artifact-studio/#try-it-make-your-first-report-in-5-minutes"><b>Make your first report in 5 minutes</b></a></p>

## Build a tool: Agentic Process

**For anyone who builds tools or workflows with a coding agent** such as Claude Code or Codex.
Paste one build request with a job you repeat. Get back a tool someone else can start in five
minutes: a README, one `SKILL.md` that works in any chatbot, and a worked example, tested first.

<p align="center">
  <a href="agentic-process/"><img src="agentic-process/_build/img/pilot-score.svg" width="49%" alt="Animated chart: in one blind pilot, the tool built with Agentic Process scored 93 out of 100 with 0 corrections; the direct build scored 73 with 2 corrections"></a>
  <a href="agentic-process/"><img src="agentic-process/_build/img/pilot-brief.webp" width="49%" alt="Screen capture of the tool built with Agentic Process: a warning that the notice never gives its effective date and leaves out a form, before any table"></a>
</p>

**The pictures, in words:** left, the blind pilot: 93/100 for the tool built with Agentic Process,
73/100 for the direct build, on the same brief. Right, that tool at work, warning first about what
the notice leaves out. One build task, one notice, one blind reviewer.

<p align="center"><a href="agentic-process/#try-it-build-a-tool-in-about-10-minutes"><b>Build your first tool in about 10 minutes</b></a></p>

## Both projects

| | Artifact Studio | Agentic Process |
| --- | --- | --- |
| **You bring** | Rough notes, and who will read them | A job you repeat, and who uses the result |
| **You get** | A report, deck, post or page | A README, one `SKILL.md`, a worked example |
| **You need** | The chatbot you already use | A coding agent, or any chatbot by hand |
| **First run** | About 5 minutes | About 10 minutes |
| **Evidence** | [22 fresh-session runs](artifact-studio/quality-results/README.md) | [The blind pilot](agentic-process/quality-results/README.md) |

Both were built and checked by their author, in Claude. Nobody else has used them yet, so tell us
what you find. The times are estimates.

<details>
<summary>How every project is laid out</summary>

`base/` is enough to try the tool. The other folders appear only when they hold something you can use.

```
a-project/
  README.md          the landing page: the job, a capture of the result, a quick start
  AGENTS.md          instructions for AI agents
  CLAUDE.md          points Claude Code at AGENTS.md
  LICENSE
  base/              the few files you need to try it, and examples/
  level-2-files/     Advanced: what you add to make it yours, with its own README
  level-3-files/     Expert: connections for agents, with its own README
  quality-results/   the evidence: what was checked, by whom, with the raw results
  _build/            what the project is built from. Not needed to use it
```

`python3 workshop/tools/check_project.py projects/<name>` checks a folder against this.

</details>
