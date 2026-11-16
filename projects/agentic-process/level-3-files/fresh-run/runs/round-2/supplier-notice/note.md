# Note

Tool: checked facts from a supplier notice or business report. Status: built, not used. Nobody has tried it, as of 16 November 2026.

## Decided

From your message:
- The users are the students in your small-business AI class.
- The input is a supplier notice or a business report.
- The result is key facts, obligations, dates and questions, with each item checked against the page it came from.
- You build with a coding agent and keep your tools in a git repository.
- Students use whatever chatbot they already have.

## Assumed

Choices I made because I could not ask. Change any of them.
- A notice and a report are one job, because they give the same result.
- "Extract, then check" is one result: a list where every item carries its quote and location. The student does the check by hand. A second check run by the assistant is out of the first version.
- The wow: every line arrives with the exact words behind it, and the assistant asks where the document is silent.
- The folder is called `checked-facts/` and holds the six files in the plan.
- Students paste the document as text, or attach it if their chatbot takes files.
- You hand the prompt and the front page to students in whatever way you already hand out class material. Your message does not say how.
- The output is plain numbered lines, not a table, so it survives in any chatbot.
- The worked example is an invented supplier notice. A business report example waits under "Next".
- The worked example stays out of the prompt, so the same notice can serve as the test input.
- Nobody was named to review the plan, so I reviewed it myself.
- All nine gates were answered yes on your behalf. The answers are in the session record in `out.md`. The gates at steps 2, 3 and 4 were answered without any facts behind them.
- The first addition, when the time comes, is the second invented example.

## Not checked

- Anything on the web. No search was run in this session.
- Whether any chatbot already does this job with no instructions written.
- Whether any chatbot has a built-in feature that quotes or cites a document.
- Paid options of any kind: what exists, what each covers, how each charges.
- The price and limits of your students' chatbots, your repository and your coding agent.
- Whether your students' chatbots accept attached files, or long documents.
- Whether the prompt works. It has not been run on any chatbot.
- Whether the six files exist in your repository. I cannot see it.

## Test this next

Nobody has tried this. In order:

1. **The bare test.** Open a new chat with no saved instructions or memory. Paste the invented notice from `example/notice.md`, from "[Page 1]" down, and ask only: "What do I need to know and do?" If the reply already has everything in the plan's test, stop: teach that, and drop this tool.
2. **The three checks.** After your coding agent writes the folder: every file the plan names exists; every quote in `example/result.md` appears word for word in `example/notice.md`; both example files say they are invented.
3. **The fresh-chat test.** Open a new chat with no saved instructions or memory. Paste the whole of `prompt.md` and nothing else from this project. Under it, paste the notice from "[Page 1]" down. Send. Go through the plan's test point by point, and search the notice for every quote. Write down the chatbot, the date, and pass or fail for each point. One fail means the first version is not ready.
4. **A second chatbot.** Repeat test 3 on a different chatbot, because your students do not all use the same one.
5. **One student, one real document.** Give a student the front page and the prompt and watch without helping. That is the first time this counts as used.
