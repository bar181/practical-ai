# Decision support assistant: North Star

Stages 1 to 3 of the [project method](../../drafts/project-method/base/METHOD.md). Written
15 November 2026. **Not yet approved.** Complexity: intermediate.

**Think of it as** a junior consultant who never skips a step. It frames the question, breaks it
down, finds the evidence, checks every source still says what it is quoted as saying, and hands you
a recommendation with the working shown.

**North Star:** a person facing a real decision gets, in one sitting, a recommendation they can
defend: the question, the options, the evidence with working links, and what is still unknown.

## Understand

| | |
| --- | --- |
| Who it is for | As an owner, manager or consultant, I want a decision worked through the way a good consulting team would, so that I can decide and explain why |
| The one job | Take a decision from a loose question to a defended recommendation, in a fixed sequence, with every source checked |
| The finished thing is | A product: a sequence of steps, each with a template, ending in a deliverable |

## Research: what already exists

| Source | Checked | What we take from it |
| --- | --- | --- |
| [Deckary: problem-solving frameworks](https://deckary.com/blog/problem-solving-frameworks) | 15 Nov 2026 | The seven-step process it attributes to McKinsey: define, structure, prioritise, plan the work, analyse, synthesise, recommend. The named frameworks are tools used inside it. The sequence below follows these seven |
| [An existing consulting skill](https://skillselion.com/skills/appautomaton/presentation/consultant) | 15 Nov 2026 | It already structures a problem in six steps and writes memos and deck outlines in text, with a date and a confidence label on outside data. Its listing describes no step that opens a link to check it, and it makes no visuals. Those two gaps are what this tool is for |
| [MConsultingPrep: the issue tree](https://mconsultingprep.com/issue-tree) | 15 Nov 2026 | Break the question into branches, put a hypothesis on each branch, and test it with data |
| [Umbrex: the MECE principle](https://umbrex.com/resources/frameworks/strategy-frameworks/mece-principle/) | 15 Nov 2026 | Branches should not overlap and should leave nothing out. Ask "what is missing?" before calling a tree finished |
| [StrategyU: the issue tree in practice](https://strategyu.co/issue-tree) | 15 Nov 2026 | The tree and the problem statement are revisited again and again. The sequence is a loop, not a line |
| [PrepLounge: the Pyramid Principle](https://www.preplounge.com/en/case-interview-basics/issue-tree) | 15 Nov 2026 | Present answer first: the recommendation, then the reasons, then the evidence |
| The Deckary page above, on the hypothesis-driven approach | 15 Nov 2026 | Its known weakness is looking only for evidence that agrees. Seek the evidence against each hypothesis on purpose |
| SWOT, decision matrices and the pre-mortem | Long-standing practice, no single source | A short set of analyses chosen to fit the question, never all of them every time |

**Decision:** build on top. The frameworks are public and well described. What is built here is
the sequence, the templates, the checks, and the outputs.

## Scope

**In:** defining the question; an issue tree; a hypothesis on each branch; a short work plan; research with links;
**checking every link** resolves and supports what it is cited for; a small set of analyses (SWOT,
options against criteria, risks, a pre-mortem); a recommendation, answer first; what is not known.

**Out:** making the decision; legal, medical, tax or investment advice; analyses for their own sake.

**Where the data lives:** the working folder for a decision belongs to the person deciding.
Nothing private is kept in this repository.

### The sequence

| Step | Output |
| --- | --- |
| 1. Define | The decision in one sentence, who decides, by when, and what would change the answer |
| 2. Structure | An issue tree with no overlaps and no gaps |
| 3. Prioritise | A best guess on each branch, and the two or three branches that decide the answer |
| 4. Plan the work | For each of those: the evidence that would support the guess, and the evidence that would prove it wrong |
| 5. Analyse | Evidence gathered, each item with a link, the date checked and whether the link was verified. Only the analyses the question needs |
| 6. Synthesise | The answer in one sentence, and the three reasons that carry it |
| 7. Recommend | Actions with owners and dates, the options on one table, the risks. Delivered as a briefing deck or a one-page brief, with a plan of next steps |

### What is particular to this version

- Every source is fetched and checked before it is cited. A dead or changed link is marked.
- The evidence against the recommendation gets its own section.
- Each step has a template, so the work can be reviewed step by step.
- The deliverable is visual and ready to present, not a wall of text.

### Levels

| | Holds | Done when |
| --- | --- | --- |
| Base | The seven steps, a template for each, three invented decisions worked end to end (a hire, a price change, a new service), and a rubric for a good recommendation | Each invented decision can be read in ten minutes and its sources all resolve |
| Level 1 | You paste the instructions and describe the decision. The assistant walks the seven steps, stopping after step 1 and after step 2 for your correction. You get a brief and a deck | A real decision is worked in one sitting and every link in it opens |
| Level 2 | A skill that keeps the working folder, runs the link check itself and scores its own recommendation against the rubric | A recommendation with an unverified source cannot be marked finished |
| Level 3 | Connections: add your own material to the folder (transcripts, papers, spreadsheets) and have it indexed for retrieval. Reads from the core memory system | "Add these three transcripts" changes the evidence table, with each claim traced to its file |

## Depends on, and feeds

- **Reuses** the artifact studio's briefing deck and one-page report.
- **Uses** the [source and link verifier](../source-verifier/README.md) and the
  [rubric reviewer](../rubric-reviewer/README.md), if they are built as their own tools.
- **Ends in** a plan drawn by the [task graph](../task-graph/README.md).
- **Reads** the [core memory system](../core-memory/README.md) at level 3.

## Open questions

- How does the assistant keep from agreeing with its first guess? Proposed: step 4 must name the
  disproving evidence before step 5 starts.
- Which analyses make the short list? Start with four and add only on a real need.
- The existing consulting skill was read from its listing only. Install and try it before building,
  and decide whether to build beside it or on top of it.

## Approved

Not yet.
