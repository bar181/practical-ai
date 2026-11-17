# Review: package X vs package Y (document to action brief)

**Verdict.** Y 93/100, X 73/100. Corrections before acting: Y 0, X 2. Hand Y to a busy owner.

Method: read notice.md, then X-result.md and Y-result.md on their own, then ANSWER-KEY.md, then both packages. Every quoted string in both results (34 in X, 34 in Y) was checked by script against notice.md with whitespace normalised for line wraps. All 68 are word for word in the notice. The only non-match is Y's template line "I will ... by ...", which is not a quote.

---

## 1. As the recipient (first screen, about 25 lines)

### X, lines 1 to 25
What the owner sees: a title, a "Watch out" count (2 penalties, 3 things you must do, 6 dates, 7 open questions), a Key facts table, the "What you must do" table (pay in 30 days with the 2% charge, 14 days' notice for standing orders, discontinued items by 15 December 2026), and the start of Dates.

- Could they act? Partly. The three listed actions are right and quoted. The missing Effective Date is visible, but only as a clause inside a cell (F1: "No date is given for it (see Q1)").
- What is missing from screen one: the Account Update Form is filed as a Key fact ("Request, with no date or consequence given"), not as something to do, and the "Watch out" line tells the owner there are 3 things to do. The fact that the form is not attached appears only at line 41 (Q4). Nothing tells the owner who to ask about the Effective Date.
- What they would do first: most likely note 15 December 2026 for discontinued stock and assume 30-day terms "soon". They would probably not return the form, and would not know to chase the Effective Date until they reached Q1.

### Y, lines 1 to 25
What the owner sees: sender and date, an "In short" line (four things to do, earliest dated deadline 15 December 2026, every penalty listed), a **Warning** naming three gaps (no Effective Date, form not attached, orphan asterisk on the charge), the full "What you must do" table including the form, and Dates D1 to D4, where D2 says "Cannot be worked out ... Northfield (your account manager) can supply it."

- Could they act? Yes. Every key item and both gaps are on screen one, with who to ask.
- Weaknesses: the tables are wide (six columns including an empty tick column), and penalties are numbered as their own "must do" rows (O2, O4), which reads slightly oddly.
- What they would do first: email the account manager or accounts@northfield.example asking for the Effective Date and the missing form, then decide on discontinued stock before 15 December 2026.

---

## 2. Against the key

Quote check: every quote below was matched word for word against notice.md.

### X

| Key item | Found | Quote exact | Right place | Notes |
| --- | --- | --- | --- | --- |
| Obligation: pay within 30 days from the Effective Date | Yes (O1) | Yes | Yes | "By" names the Effective Date as not given |
| Obligation: 14 days' written notice for standing orders | Yes (O2) | Yes | Yes | Consequence quoted as well |
| Obligation: return the Account Update Form | Yes (F4) | Yes | **No** | Filed under Key facts as a "Request", left out of "What you must do" and out of the "3 things you must do" count |
| Date: price list 1 December 2026 | Yes (D2, F2) | Yes | Yes | |
| Date: legacy stock by 15 December 2026 | Yes (D3, O3) | Yes | Yes | |
| Buried penalty: 2% per month, calculated daily | Yes (O1, D6, Q6) | Yes | Yes | Inside O1 as "Penalty:", as the brief requires |
| Ambiguous line: legacy agreements at our discretion | Yes (Q2) | Yes | Yes | Under questions, not facts |
| Missing Effective Date | Yes (F1, D1, Q1) | Yes | Yes | Flagged three times. No next step (see section 3) |
| Missing form ("attached" but not included) | Yes (Q4) | Yes | Yes, but buried | Only at line 41, not on screen one |

Result: 9 of 9 found, 9 of 9 quotes exact, 8 of 9 in the right place.

### Y

| Key item | Found | Quote exact | Right place | Notes |
| --- | --- | --- | --- | --- |
| Obligation: pay within 30 days from the Effective Date | Yes (O1) | Yes | Yes | "By when: From the Effective Date (not stated)" |
| Obligation: 14 days' written notice for standing orders | Yes (O3) | Yes | Yes | |
| Obligation: return the Account Update Form | Yes (O5) | Yes | Yes | "By when: Not stated" |
| Date: price list 1 December 2026 | Yes (D3) | Yes | Yes | |
| Date: legacy stock by 15 December 2026 | Yes (D6, O6) | Yes | Yes | Correctly framed as "If" |
| Buried penalty: 2% per month, calculated daily | Yes (O2, D7, Q3, Q4, In short) | Yes | Yes | Also in the "In short" summary |
| Ambiguous line: legacy agreements at our discretion | Yes (Q8) | Yes | Yes | |
| Missing Effective Date | Yes (In short, Warning, D2, Q1) | Yes | Yes | With who can supply it |
| Missing form ("attached" but not included) | Yes (Warning, Q6) | Yes | Yes | On screen one |

Result: 9 of 9 found, 9 of 9 quotes exact, 9 of 9 in the right place.

---

## 3. Failures caught

| Check | X | Y |
| --- | --- | --- |
| Flags that the Effective Date is never given | Yes, in F1, D1 and Q1 | Yes, in "In short", the Warning, D2 and Q1 |
| Says what to do about it | **No.** Q1 asks "When is the Effective Date?" but never says to ask the supplier. The owner has to connect it to F5 ("Questions go to your account manager") on their own | Yes. D2: "Northfield (your account manager) can supply it." Q1: "Your account manager or the Customer Accounts Team" |
| Guessed the Effective Date (for example 1 December) | No. Q3 explicitly says the notice does not say whether 1 December is before or after the Effective Date | No. Effective Date marked "Cannot be worked out" |
| Invented any date or fact | None found | None found |
| Other errors | The form is mis-classified as a fact, so the "Watch out" count of "3 things you must do" understates the obligations. Minor: the "Check it yourself" heading is repeated as bold text under itself | Minor: penalties are numbered as "must do" rows (O2, O4). F7 reports the notice's "fictional, written for a test" line, which is true but noise for an owner. "Assumed: You are the customer, as you said" could not be checked against the run prompt (not supplied) |

Useful extras, both grounded in the text: X Q3 (does the price list appear before or after the Effective Date) and Q6 (the asterisk is attached to nothing). Y Q2 (two readings of whether existing unpaid invoices shorten to 30 days) and Q4 (two readings of "calculated daily").

---

## 4. Corrections needed before acting

### X: 2 edits
1. Move F4 (Account Update Form) into "What you must do" with "By: No date given", and change the "Watch out" count to 4 things you must do. Without this, the owner's action list omits one of the three key obligations.
2. Add the next step for the Effective Date to Q1 (or D1): ask the account manager or Customer Accounts Team for the date before relying on 30-day terms or new prices.

Optional, not required: bring the "form not attached" note (Q4) to the top so it is seen on screen one.

### Y: 0 edits
Nothing must change before acting. Optional cosmetic: delete F7 (the "fictional" line) and relabel O2 and O4 as penalties of O1 and O3 rather than separate tasks.

---

## 5. The packages

### X

| Aspect | Finding |
| --- | --- |
| Files | 12 files: README.md (153 lines), AGENTS.md, LICENSE, base/SKILL.md (129), base/supplier-notice.md, base/check-sheet.md, base/examples/worked-example.md (131), and _build/ with README, two Python scripts, a JSON key and a test brief |
| Quick start | 5 steps, claimed 5 minutes. Realistic 10 to 15 minutes for a first-time user: open and copy SKILL.md, open the notice and copy "from QUILLMOOR PROVISIONS down", paste plus a line, then open a separate check sheet (print or copy it beside the chat) and fill a 5-column table, then read a 131-line worked example to find a planted error |
| What a user must read or do | Two files to start, a third (check sheet) to finish, a fourth (worked example) recommended |
| Extra or confusing | README carries builder material a busy owner does not need: a "North Star" line, "If you are an AI agent", a "Why not just use a tool that already cites?" section that points to `workshop/plans/...` (not in the package), a status table, a layout tree, "What comes next". The `_build/` folder and AGENTS.md add files the owner is told to ignore. The practice notice has a date for everything, so it never trains the user on a missing date, which is exactly what tripped X on the unseen notice |
| Root cause of X's two misses, in SKILL.md | "What you must do" is defined by "must", "shall", "required" or "an action with a consequence"; "Please" with no consequence is not in that list, so the form fell to Key facts. SKILL.md has no rule to warn about missing dates or attachments or to say who can supply them |

### Y

| Aspect | Finding |
| --- | --- |
| Files | 4 files: README.md (99 lines), SKILL.md (130), example.md (58), practice-notices.md (97) |
| Quick start | 5 steps, claimed 5 minutes. Realistic 5 to 10 minutes: copy SKILL.md, paste, type one line, paste notice A, tick the empty column in the brief itself. No separate check sheet: the check is built into the output |
| What a user must read or do | One file to paste, one notice to copy. The check steps arrive inside the result |
| Extra or confusing | "press **Raw**" assumes GitHub. The status paragraph has builder jargon ("The plan's gates 2 and 7 are still open with the owner") and a broken line break around the plan path. "Level 2" and "There is no Level 3" are internal terms. The "How it was checked" table is all "Not yet run" and means nothing to an owner. practice-notices.md holds two notices, so the user must pick out notice A between the lines. example.md has an empty slot ("The result is not yet run") |
| Why Y caught the gaps, in SKILL.md | The output shape has a **Warning** for "no date, an attachment not included"; Dates must say "cannot be worked out, what is missing and who can supply it"; step 2 explicitly counts "please" as an ask; step 5 sends missing attachments to questions. Practice notice B rehearses exactly this failure (no date, missing attachment) |

### Which to hand to a busy owner
**Y.** Fewer files (4 vs 12), one file to paste, the check lives in the brief rather than a separate sheet, and its instructions produced a first screen that tells the owner what is missing and who to ask. X's package is longer, aimed partly at agents and builders, and its instructions caused both of its result's errors. Y's README would still benefit from deleting the status jargon, the "How it was checked" table and the "Raw" step.

---

## 6. Scores

| Criterion (max) | X | Reason | Y | Reason |
| --- | --- | --- | --- | --- |
| Accuracy against the key (35) | 28 | All 9 items found with exact quotes, but one of the three key obligations (the form) is misplaced as a fact and missing from the action list and count | 34 | All 9 found, exact and correctly placed; 1 off for penalties numbered as separate "must do" rows |
| Catches the missing Effective Date with a next step (20) | 13 | Flagged clearly three times and not guessed, but never says to ask the supplier | 20 | Flagged on screen one, marked "cannot be worked out", names the account manager or Customer Accounts Team to ask |
| Recipient would act on it as it is (20) | 13 | Screen one gives three correct actions but omits the form and has no warning block; owner must read to line 41 to learn the form is missing | 17 | Screen one has every action, every penalty and all three gaps; wide tables, penalty-as-task rows and the "fictional" fact add friction |
| Package simple to start (15) | 9 | 12 files, a 153-line README with builder and agent sections, a separate check sheet, and a 131-line worked example | 12 | 4 files and one paste, check built into the output; loses points for "press Raw", builder jargon in the status and checks table, and choosing notice A from a two-notice file |
| Nothing invented (10) | 10 | All 34 quotes verbatim; no dates or facts invented | 10 | All 34 quotes verbatim; no dates or facts invented |
| **Total (100)** | **73** | | **93** | |
