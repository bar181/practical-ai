# Workflow card: decision support

This card is the spec. Everything else in this folder was built from it.

**The request, as it came in:** "I make a lot of decisions for the business on gut feel. I want
something in my chatbot that knows my business, and when I ask a question it does the research,
a SWOT and gives me a recommendation I can take to my partner."

| | |
| --- | --- |
| **For** | An owner or manager of a small business who uses a chatbot |
| **The job** | Turn one business question into a one-page decision brief: research, a SWOT and a recommendation |
| **Trigger** | The person has a decision to make, and types the question |
| **Inputs** | A business profile, written once and saved with the tool; the question; any facts the person adds |
| **Steps** | 1. Check the business profile. 2. Frame the decision: "do nothing", the person's idea, and a smaller version of it where one exists. 3. Research, with a source and date for every fact. 4. Compare and recommend by a written rule: limits are pass or fail; each goal scores +1, 0 or -1 against doing nothing over twelve months; the highest total leads; it gets a "check first" step when risk is low, a deciding fact is not found, or a limit is unknown. 5. SWOT for the recommended option. 6. Write the brief, then a check list for the person |
| **Output** | A brief you can read in two minutes: the decision, the recommendation, why, the SWOT, risks, next steps, what would change it, assumptions, sources |
| **A person checks** | Every figure against its source, every assumption, and whether the recommendation fits the goals in the profile. The person decides |
| **When something is missing** | No profile: ask six questions once and write a profile to save. No web access: say so, research nothing, and list what to look up. A fact not found: write "not found", never a guess |
| **Out of scope** | Contacting anyone, spending money, legal or tax advice, more than one decision at a time |
| **Already exists** | Any chatbot will write a SWOT when asked. What it lacks is a saved business profile, a fixed workflow, sources for every fact and a written rule for recommending. So this wraps the chatbot; it builds no software |
| **Acceptance test** | The invented profile and question in [`example.md`](example.md) give a brief where every figure has a source or is labelled an estimate, "not now" is compared, the recommendation follows the written rule from the scores shown, and the brief names what would change it. A second, different decision passes the same checks |
| **Where it runs** | A chatbot project: a Claude Project, a ChatGPT Project or a Gemini Gem. Or a folder the chatbot can read |
| **The demo** | One run by a fresh chat on the invented business, unedited |
| **Saves time or improves quality?** | Measure on the first three real decisions: minutes from question to a brief you would share, and how many points you had to correct |
| **Last tested** | 16 November 2026, by fresh AI sessions in Claude: nine runs on two decisions (a bakery's catering idea, a landscaper's truck). In the last run of each, the recommendation followed the scores and the rule, with 1 blocking point each, both since fixed and not re-tested. Not yet used on a real decision |
