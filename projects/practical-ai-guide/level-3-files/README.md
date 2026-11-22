# Level 3: a chat window on the website

**The core idea:** a visitor opens a chat from Bradley's illustrated avatar and gets office hours
without leaving the site.

**Status, 22 November 2026:** planned, not built. Build it only if Level 1 and Level 2 show people
want it. The full plan, with its sources, is
[`workshop/plans/practical-ai-guide/`](../../../workshop/plans/practical-ai-guide/README.md).

## The shape

| Part | Choice |
| --- | --- |
| Window | A small panel on the website, opened from the avatar, labelled "AI guide" |
| Server | One function (for example on Cloudflare Workers, as in Site Studio's Level 3) that holds the model key. The key never reaches the browser |
| Knowledge | The whole index and the files it links, sent with every question. The repository is about 50,000 tokens, under the size where retrieval is needed |
| Rules | [`../base/SKILL.md`](../base/SKILL.md), unchanged |

## Before it goes live

- The first message says it is an AI, clearly. Behind an avatar this matters most.
- A limit on questions per visitor, and a monthly spending cap at the model provider.
- No conversations kept, unless the visitor agrees.
- The three questions in the worked example still pass, plus ten more with three it must decline.
- Bradley approves the window, the label and the launch.

Part of the [Practical AI guide](../README.md).
