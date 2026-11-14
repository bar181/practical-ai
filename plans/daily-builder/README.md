# Daily builder

A scheduled agent that builds the next item on the priority list and asks for review.

**Think of it as:** A night-shift apprentice who leaves finished work on the bench with a note, and never ships it without a signature.

## What it includes

- Works the priority list from the top.
- Checks what already exists before building anything.
- Writes a spec, builds against synthetic samples, and has a separate agent score the result.
- Opens a pull request. Never pushes to the main branch.
- Works best with connections to the repository, file storage and a hosting route.

## Priority list entries this plan covers

- Daily builder

## Status

Plan only. No draft yet.

## Next steps

1. Agree the scoring rubric and the pass mark
2. Run it by hand for two builds before scheduling it
3. Schedule it once those two builds pass review
