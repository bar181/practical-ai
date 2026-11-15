# Example: a palette from one brand colour

A worked example: what was asked, what came with it, what the studio chose and what came back. The business and every figure are invented.

## The request

> All I have is our pink, the one on the sign. I need the rest of the colours for our pages and posts.

## The notes that came with it

- We are a florist
- The pink on the sign is a deep pink, around 320 on the colour wheel
- No other brand colours have ever been chosen

## What the studio picked

No template was needed. This request is answered by one tool and one rule.

## How it was made

No template is involved. The assistant used the palette rule in the skill's design ideas: each role is a fixed lightness and strength, with the hue taken from the brand. With the MCP server connected this is one call to `make_palette` with a hue of 320.

## The output

- [`output.md`](output.md): seven colours with a job each, and a contrast table. Paste it into your design spec

## The note that came back with it

- **Chose:** a palette built from hue 320.
- **Assumed:** 320 for "deep pink". A phone photo of the sign would let me read it properly.
- **Missing:** the exact colour of the sign.
- **Check before sharing:** hold the accent colour next to the sign. If it is off, tell me warmer or cooler and I will move the hue.

## What a good result must have

1. There are seven colours, each with a named job
2. There is exactly one accent colour, for buttons and links
3. The greys carry a trace of the pink
4. Every text and background pair is listed with its ratio, and each passes
5. The result says how much of a page each colour should take

## Try it yourself

Give an assistant the request and the notes above. Score what comes back against the list above, one point for each. Record the result in [`../README.md`](../README.md).
