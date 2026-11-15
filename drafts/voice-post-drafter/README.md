# Voice post drafter

A draft that sounds like you, for you to copy, edit and publish yourself.

**Think of it as:** a ghostwriter who has read everything you posted and remembers every time you
said "I would never say that". They hand you a draft. You still sign it.

**Who it is for:** people who know they should post and do not, because a blank page takes an hour
and generic AI drafts sound like nobody.

## What already exists

See the [landscape review](landscape-review.md): what the sources say, and what changed in the tool as a result.

## Status

Draft. First copy, not yet reviewed or tested by anyone else.

| Level | What it will hold | In this draft |
| --- | --- | --- |
| `level-demo` | A sample voice file, a topic, the draft it produced and the feedback given | [`index.html`](level-demo/index.html): one full loop you can step through, and the same example as text |
| `level-simple` | Instructions to paste into a chatbot Project, and a voice file to fill in | Both |
| `level-working` | One draft per channel, with feedback saved and applied every time | [Outline](level-working/) |
| `level-automated` | A daily topic scout that queues topics and drafts for your review | [Outline](level-automated/), with the [`voice-drafter`](../../skills/voice-drafter/) skill |
| `commercial-grade` | What a commercial build adds | [Explained](commercial-grade/) |

Start with [`STUDENT-GUIDE.md`](STUDENT-GUIDE.md).

Agents: start with [`AGENT-GUIDE.md`](AGENT-GUIDE.md).
