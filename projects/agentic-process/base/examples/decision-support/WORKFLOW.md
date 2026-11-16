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
| **Steps** | 1. Check the business profile. 2. Frame the decision and its options. 3. Research, with a source for every fact. 4. SWOT for the leading option. 5. Compare the options and recommend. 6. Write the brief |
| **Output** | A one-page brief: the decision, the recommendation, why, the SWOT, risks, next steps, assumptions, sources |
| **A person checks** | Every figure against its source, every assumption, and whether the recommendation fits the goals in the profile. The person decides |
| **When something is missing** | No profile: ask six questions once and write a profile to save. No web access: say so, research nothing, and list what to look up. A fact not found: write "not found", never a guess |
| **Out of scope** | Contacting anyone, spending money, legal or tax advice, more than one decision at a time |
| **Acceptance test** | The invented profile and question in [`example.md`](example.md) give a brief where every figure has a source or is labelled an estimate, the option "do nothing" is compared, and the recommendation names what would change it |
| **Where it runs** | A chatbot project: a Claude Project, a ChatGPT Project or a Gemini Gem. Or a folder the chatbot can read |
| **The demo** | One run by a fresh chat on the invented business, unedited |
| **Saves time or improves quality?** | Measure on the first three real decisions: minutes from question to a brief you would share, and how many points you had to correct |
