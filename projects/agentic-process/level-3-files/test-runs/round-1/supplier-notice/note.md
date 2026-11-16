# Hand-over note: notice checker

Who has tried it: nobody. The first version is written, not used. No chatbot has run the prompt and no student has seen it.

## Decided

These follow from your message or are plain drafting choices.

- The first version is a prompt a student pastes into a chat, in plain text, tied to no one chatbot, because your students use whatever chatbot they already have. No code.
- The tool is a small folder of text files that your coding agent can create in your git repository from section 2 of the hand-over.
- Every fact, obligation and date carries the exact words from the document and where they are, so a student can search for them.
- The chatbot must keep and mark an item that fails its check. It may not quietly fix or drop it.
- The chatbot reports the last sentence it received, so a student can see when a long document was cut short.
- The worked example uses an invented supplier, with invented prices and dates, and says so.
- The tool sends, posts, pays and publishes nothing. Handing the prompt to students is your action.

## Assumed

I could not ask you anything. Each line below is a question or a gate I answered for you. Change any of them and tell the coach.

1. The one user is a student, not you. You are the builder.
2. Both kinds of document (supplier notice, business report) and both halves (make the list, check the list) count as one job. Only the supplier notice has a worked example.
3. The wow is that each item shows the exact words it rests on, so a student can tell in seconds whether the chatbot made something up.
4. "The page it came from" means the place in the document: the page number when the text shows one, otherwise the heading or paragraph.
5. The check has two layers. The chatbot checks its own list, then the student searches the document for each quote. The student's check is the one that counts.
6. Step 2 gate, "Does something existing do the whole job?": answered no. This was not checked. If the true answer is yes, this build should stop and become a short guide to that thing.
7. Step 3 gate: you build the prompt and buy nothing for the first version.
8. Step 4 gate: the cost is acceptable, because the first version adds no new paid thing to what you and your students already have. No price was checked.
9. You have no project template. The folder is called `notice-checker` and sits at the top of your tools repository. The name and place are mine.
10. Students get the text of the prompt and the invented notice from you by hand. They never need the repository.
11. Students have their documents as text they can paste or attach. Scanned pages and photos are out of the first version.
12. Nobody is available to review the plan, so I reviewed it as a stranger.
13. Gates 1, 5, 6 and 7 are answered yes.
14. Gate 8, "Did the fresh chat finish the job, and what did it trip on?", is open. No fresh chat was run. I went on to step 9 only so the hand-over is complete.
15. Gate 9, "Is the first version in use?": no.
16. You fit the second kind of person (you build with agents and keep a repository) and your students fit the first (new, a prompt they can paste). I combined the two rows.

## Not checked

- The web. Nothing was searched, so steps 2, 3 and 4 give no links and no dates. The lists of what to look up are in those steps.
- Whether any chatbot or free tool already does the whole job.
- Any paid option, and any price or limit: chatbots, your repository host, your coding agent.
- Whether the prompt works in any chatbot. The "good result" in the worked example was written by hand by the coach. It is not the output of a chatbot run.
- What each student's chatbot does with a pasted document: who can see it and how long it is kept. Check this before a real supplier document goes in.
- Whether your repository has a template or naming rules.
- Checks 1, 3 and 4 in the test sheet, because the folder does not exist yet. You named no repository path, so I created nothing in it.

One thing was checked: all 14 quotes in the worked example appear word for word in the invented notice (check 2, run mechanically on the hand-over file).

## Test this next

1. Run the fresh-chat test yourself on the invented notice in one chatbot. Write down what it tripped on.
2. Run it again in a second chatbot that your students use.
3. Give the prompt and the invented notice to one student with no help. Watch where they stop.
4. Do the step 2 lookups. If something existing does the whole job, stop and write the guide instead.
5. Only then try a real document, after the privacy check above.
