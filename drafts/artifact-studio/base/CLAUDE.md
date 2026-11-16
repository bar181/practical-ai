# Artifact studio

You are in the base of the artifact studio: a library of templates for web pages, slide decks and
social post pictures, with rules for choosing between them.

- **To make something for a person,** follow [`AGENTS.md`](AGENTS.md) in this folder. It is the path
  from a request to a finished file, with the output contract.
- **If you can load skills,** load [`skills/artifact-studio/SKILL.md`](skills/artifact-studio/SKILL.md).
- **To change the library,** edit [`source/`](source/), run `python3 source/build.py`, then run
  `python3 ../../../tools/gates.py .` and do not stop until it says "All gates that ran passed".
- **Never edit a generated file.** Each one says so at the top.
- Use the person's content only. Invent no facts. Nothing is published without a person saying so.

People start at the [landing page](../README.md).
