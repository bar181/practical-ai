# Friction: builder skill, PROCESS.md and template

## BLOCKING

1. **No fallback for the worked example when a fresh chat cannot be started.** Builder step 4 says
   "in a fresh chat if you can" and then "Save the result unedited", and `template/example.md`
   states the result was made by a new chat and nothing is edited. Nothing says what to ship when
   no fresh chat is possible: leave `example.md` out, leave it with the input only, or write a
   target result by hand. I guessed: I wrote the result by following the SKILL.md myself and
   changed the header to say plainly that it was not made by a fresh chat and is a target, not
   proof. The template has no wording for this case.

## MINOR

2. **Level numbers mean different things in the plan and in PROCESS.md.** The plan's Level 2 is a
   skill writing to Google Sheets through a connector; PROCESS.md's Level 2 is a saved skill or
   project and puts connections at Level 3. The builder skill does not say which wins. The owner's
   wording ("only if it removes repeated setup") matched PROCESS.md, so I followed that.
3. **"One job only" when the plan's job has two halves.** The plan's one job is "capture a
   learning ... and put the right ones in front of whoever starts similar work", plus a weekly
   review. The skill does not say whether to split a compound job into two tools or keep it in one
   file. I kept one file with two modes.
4. **Plan deliverables versus "nothing extra".** The plan's Base asks for a viewer page and twelve
   invented rows; the builder skill forbids scripts and extra files and fixes the folder shape.
   Nothing says whether the plan or the skill wins. I followed the skill.
5. **Unapproved plan.** The North Star page says "Not yet approved". The skill does not say
   whether to build from an unapproved plan, stop, or flag it. I built and flagged it.
6. **A plan that rewrites a tool you cannot see.** The plan says the existing `learning-log` skill
   is "rewritten, not replaced". The skill has no step for comparing against, or naming, an
   existing version. I reused the name and flagged that I could not compare.
7. **"If the skill-creator skill is available, use it".** It was listed in the session, but the
   test rules allowed reading only kit files. "Available" is not defined. I used the template.
8. **Reuse check has no depth or stopping rule.** "Anthropic's skills and plugins first" does not
   name where to look, how far to go when a listing cannot be fetched, or how to record a partial
   check. I recorded the partial check as partial.
9. **The quick-start shortcut needs a Raw link that does not exist yet.** The README template asks
   for the Raw link to SKILL.md, but a newly built tool has none. No placeholder wording is given;
   I left the template's bracketed placeholder.
10. **Short check item 3 has no input of its own.** "Confirm it asks for missing context in one
    reply" needs an input with something missing, but the check lists only the example input and
    one different input. I proposed a third input ("log that" alone) in the hand-back.
11. **No place in the README template for where the person's data lives.** The plan requires the
    data to stay outside the repository in a file the person owns, and pasting rows needs a short
    how-to. The template has no section for it; I put it under the quick start.
12. **Plan's fixed lists are referenced but not given.** The plan says labels come from "a fixed
    list" and topics from "a short tree" but defines neither. The builder skill's "invent no
    facts" left me unsure whether defining a starter list counts as inventing. I deferred to the
    person's own labels.
13. **PROCESS.md links point to paths outside the kit** (`builder/agentic-process/SKILL.md`,
    the plan's drafts and landscape review). Expected under the test rules, but the builder skill
    does say "If you cannot open it, these steps are enough", which helped.
