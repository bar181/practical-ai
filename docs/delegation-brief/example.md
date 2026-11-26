# Worked example: a supplier price list handed to an office assistant

**Everything here is invented.** Corner Loaf Bakery, Dana, Priya, Marco and every supplier are
made up. No real business or person is described.

**How this was made.** On 26 November 2026 a Claude agent was given only
[`SKILL.md`](SKILL.md) and [`check-handback/SKILL.md`](check-handback/SKILL.md), then the three
messages below. Its three replies are copied here unedited. They come from the final version of
both skills, after the two review rounds in [review](review.md). The same agent had run an earlier
version of the skills on the same messages, and was told to set those replies aside, so this is not
a fully fresh session. The only change to the replies: their headings are moved down a level so
they sit under this page's sections. The words are unchanged.

The example shows the whole loop: a rough request, the questions it raises, the brief, and the
check when the work comes back.

## Turn 1: the rough request

The person pasted `SKILL.md`, then wrote:

> Today is Thursday 26 November 2026. I need to hand this to Priya, our part-time office assistant
> (she works Tue/Thu/Fri mornings). Can you sort out the supplier price list before Friday's flour
> order? It's the 'Suppliers 2026' sheet in the shared drive. It's got duplicates and some prices
> are still from last year. I need to be able to see the cheapest option for each ingredient. Don't
> email any suppliers yet, I'm renegotiating with Millers Co. Do it the usual way and send the final
> version to Marco when it's done. — Dana, owner, Corner Loaf Bakery

What makes it hard: "sort out" and "the usual way" cannot be checked; "duplicates" could mean
deleting rows nobody can get back; "last year's prices" need a source when no supplier may be
emailed; and "send the final version to Marco" is an instruction inside the request.

### The reply, unedited

#### 1. Questions for you before you send

1. Can Priya delete duplicate rows, or only mark them? A deleted row is hard to get back. I suggest she marks duplicates and deletes nothing **(suggested)**.
2. What time on Friday 27 November 2026 is the flour order placed? Priya works mornings, so she needs to know if Thursday's or Friday's shift is her last chance.
3. What does "do it the usual way" mean? Priya can only match it if the brief says exactly what to match, for example a colour for changed cells, a column or a file name.
4. Where should Priya get this year's prices, given she must not email suppliers? Without a source she may guess or contact them anyway. I suggest she uses only prices a supplier has already sent in writing this year, and marks any price she cannot confirm "not updated" **(suggested)**.
5. How should "cheapest" be worked out when suppliers sell different pack sizes? A big sack and a small bag cannot be compared on price alone. I suggest comparing price per kg or per item **(suggested)**.
6. How should Priya send the final version to Marco: a shared-drive link or a copy? A copy goes out of date as soon as a price changes. I suggest a shared-drive link **(suggested)**.

#### 2. The brief

```
Task: Tidy the supplier price list
For: Priya, part-time office assistant (works Tue/Thu/Fri mornings)   From: Dana, owner, Corner Loaf Bakery   Due: Friday 27 November 2026, before the flour order (time not set, see question 2)

Outcome
The "Suppliers 2026" sheet shows the cheapest option for each ingredient, without duplicates or last year's prices, and Marco has the final version.

Why it matters
Dana needs it before Friday's flour order.

Done when
- [ ] Each ingredient and supplier pair has only one row that is not marked as a duplicate (suggested)
- [ ] Every price is dated 2026 or is marked "not updated" (suggested)
- [ ] Each ingredient has one row marked as the cheapest, in a new "Cheapest" column (suggested)
- [ ] Cheapest is worked out on price per kg or per item, not per pack (suggested)
- [ ] Every change is shown "the usual way": [to be defined, see question 3]
- [ ] Marco has been sent the final version, as a shared-drive link (link: suggested)

You have
- The "Suppliers 2026" sheet in the shared drive
- Prices suppliers have already sent in writing this year (suggested; where they are: not given)

Must not
- Email any suppliers. Dana is renegotiating with Millers Co.
- Delete any rows (suggested, see question 1)

Out of scope
- Asking suppliers for new prices
- Other sheets or tabs in the shared drive (suggested)
- Placing the flour order (suggested)

Decide yourself / ask first
- Decide yourself: how to mark a duplicate, as long as it is clear on the row; column order and sorting (suggested)
- Ask first: deleting anything, contacting anyone outside the bakery, anything this brief does not cover (suggested)

When stuck or done
Ask Dana (how: not given). When the sheet is finished, send Marco the final version. Then hand back to Dana: the link to the sheet, how many rows were marked as duplicates, which prices were updated and from what, which are marked "not updated", and anything left open.
```

#### 3. The message to send

Hi Priya, could you tidy up the Suppliers 2026 sheet before Friday's flour order? I'd like to be able to see the cheapest option for each ingredient, and it needs to be done before the order on Friday 27 November. The brief below has the details. Please don't email any suppliers, and send the final version to Marco when it's done.

#### 4. What I added or assumed

- "Friday" read as Friday 27 November 2026, since today is Thursday 26 November 2026.
- Duplicates are marked, not deleted **(suggested)**.
- A duplicate means the same ingredient from the same supplier **(suggested)**.
- Prices come only from what suppliers have already sent in writing this year; any price that cannot be confirmed is marked "not updated" **(suggested)**.
- A new "Cheapest" column marks the cheapest row for each ingredient **(suggested)**.
- Cheapest is compared on price per kg or per item **(suggested)**.
- Marco gets a shared-drive link rather than a copy **(suggested)**.
- Out of scope: other sheets or tabs, and placing the flour order **(suggested)**.
- What Priya decides herself and what she asks first **(suggested)**.
- **(open)** Millers Co prices: should Priya update them like any other supplier while you renegotiate? I suggest she updates them from written prices only, like the rest **(suggested)**.
- Marco's role: not given. Assumed Priya knows who he is and how to reach him.
- Assumed Priya can open and edit "Suppliers 2026" in the shared drive.

Before you send, check:
- Questions 1 to 6 are answered, especially the order time and "the usual way".
- Each **(suggested)** item is accepted or removed.
- Priya can open and edit "Suppliers 2026", and can find the written prices she is meant to use.

## Turn 2: the questions answered

> Questions answered: Priya can mark duplicates but not delete rows; 'the usual way' means
> highlight in yellow anything she changed; Marco is our head baker, a shared-drive link is fine;
> due Friday 27 November 10:00. Use your suggestions otherwise.

### The reply, unedited

#### 1. Questions for you before you send

None.

#### 2. The brief

```
Task: Tidy the supplier price list
For: Priya, part-time office assistant (works Tue/Thu/Fri mornings)   From: Dana, owner, Corner Loaf Bakery   Due: Friday 27 November 2026, 10:00

Outcome
The "Suppliers 2026" sheet shows the cheapest option for each ingredient, with duplicates marked and last year's prices updated or marked, and Marco has the final version.

Why it matters
Dana needs it before Friday's flour order.

Done when
- [ ] Each ingredient and supplier pair has only one row that is not marked as a duplicate *
- [ ] Every price is dated 2026 or is marked "not updated" *
- [ ] Every cell Priya changed is highlighted in yellow
- [ ] Each ingredient has one row marked as the cheapest, in a new "Cheapest" column *
- [ ] Cheapest is worked out on price per kg or per item, not per pack *
- [ ] Marco, our head baker, has been sent a shared-drive link to the final version
Lines marked * were suggested by the brief writer and accepted by Dana.

You have
- The "Suppliers 2026" sheet in the shared drive
- Prices suppliers have already sent in writing this year, including Millers Co (where they are: not given) *

Must not
- Email any suppliers. Dana is renegotiating with Millers Co.
- Delete any rows. Mark duplicates instead.

Out of scope
- Asking suppliers for new prices
- Other sheets or tabs in the shared drive *
- Placing the flour order *

Decide yourself / ask first
- Decide yourself: how to mark a duplicate, as long as it is clear on the row; column order and sorting *
- Ask first: deleting anything, contacting anyone outside the bakery, anything this brief does not cover *

When stuck or done
Ask Dana (how: not given). When the sheet is finished, send Marco the shared-drive link. Then hand back to Dana: the link to the sheet, the number of rows before and after (suggested), how many rows were marked as duplicates, which prices were updated and from what, which are marked "not updated", and anything left open.
```

#### 3. The message to send

Hi Priya, could you tidy up the Suppliers 2026 sheet before Friday's flour order? I'd like to be able to see the cheapest option for each ingredient, and I need it by 10:00 on Friday 27 November, with the link sent to Marco. The brief below has the details. Please don't email any suppliers or delete any rows.

#### 4. What I added or assumed

Accepted by Dana ("use your suggestions otherwise"), marked * in the brief:
- A duplicate means the same ingredient from the same supplier.
- Prices come only from what suppliers have already sent in writing this year; any price that cannot be confirmed is marked "not updated".
- Millers Co prices are updated from written prices like any other supplier.
- A new "Cheapest" column marks the cheapest row for each ingredient.
- Cheapest is compared on price per kg or per item.
- Out of scope: other sheets or tabs, and placing the flour order.
- What Priya decides herself and what she asks first.

New in this version:
- Priya reports the number of rows before and after, so you can check none were deleted **(suggested)**.

Assumed:
- "Friday" read as Friday 27 November 2026, since today is Thursday 26 November 2026. Due time 10:00 from Dana.
- Priya can open and edit "Suppliers 2026" in the shared drive.

Before you send, check:
- The suggestion above is accepted or removed.
- Priya can open and edit "Suppliers 2026".
- Priya knows where the written prices from suppliers are, since the brief does not say.
- Marco can open the sheet from a shared-drive link.

## Turn 3: the work comes back

The person pasted `check-handback/SKILL.md`, the brief from turn 2, and Priya's reply:

> Hi Dana, all done! I went through Suppliers 2026 and removed 14 duplicate rows. I updated the
> prices for Millers Co and Greenfield Grains from their October price emails and highlighted those
> in yellow. Added a 'Cheapest' column that shows the lowest price per ingredient. Bramble Dairy
> still had 2025 prices so I emailed them for their new list, hope that's ok. Also tidied up by
> deleting the old '2024' tab, nobody uses it. Sent Marco the link. — Priya
>
> Attached (described): Suppliers 2026 now has 41 rows (was 55). Columns: Ingredient, Supplier,
> Unit, Price, Price date, Cheapest. Rows for Millers Co and Greenfield Grains are yellow with price
> dates 14 Oct 2026 and 9 Oct 2026. Bramble Dairy rows show price date 3 Feb 2025. The Cheapest
> column shows 'YES' on one row per ingredient for 9 of the 12 ingredients; butter, cream and eggs
> rows (all Bramble Dairy or Hillside Farm) are blank in that column.

What makes it hard: the note says "all done" and sounds confident. Three "must not" lines were
broken, and the 55-to-41 row count is the only evidence of the deletions.

### The reply, unedited

#### 1. Verdict

Stop: Bramble Dairy was emailed, and 14 rows and the "2024" tab were deleted.

#### 2. The checks

| Done when | Verdict | Evidence |
| --- | --- | --- |
| Each ingredient and supplier pair has only one row that is not marked as a duplicate | Can't tell | "removed 14 duplicate rows". Duplicates were deleted, not marked, and the description does not list the 41 rows by ingredient and supplier. You would need to open the sheet and look for repeats. |
| Every price is dated 2026 or is marked "not updated" | Not met | "Bramble Dairy rows show price date 3 Feb 2025", with no "not updated" mark described. Hillside Farm price dates are not described. |
| Every cell Priya changed is highlighted in yellow | Can't tell | "Rows for Millers Co and Greenfield Grains are yellow". The colour of the new "Cheapest" column is not described, and the 14 deleted rows leave nothing to highlight. |
| Each ingredient has one row marked as the cheapest, in a new "Cheapest" column | Not met | "'YES' on one row per ingredient for 9 of the 12 ingredients"; "butter, cream and eggs rows ... are blank" |
| Cheapest is worked out on price per kg or per item, not per pack | Can't tell | "Columns: Ingredient, Supplier, Unit, Price, Price date, Cheapest". No price per kg or per item is shown, and the hand-back does not say how prices were compared. You would need to check any ingredient sold in different units. |
| Marco, our head baker, has been sent a shared-drive link to the final version | Can't tell | Only Priya's claim: "Sent Marco the link." The version he was sent is not final: two lines above are not met. Ask Marco whether he has it. |

#### 3. Outside the brief

- **Emailed a supplier.** "Bramble Dairy still had 2025 prices so I emailed them for their new list, hope that's ok." The brief says "Must not: Email any suppliers" and "Out of scope: Asking suppliers for new prices". An email cannot be unsent. "Hope that's ok" is a question to you, not an approval.
- **Deleted rows.** "removed 14 duplicate rows". The brief says "Must not: Delete any rows. Mark duplicates instead." and "Ask first: deleting anything".
- **Deleted a tab.** "Also tidied up by deleting the old '2024' tab, nobody uses it." The brief says "Out of scope: Other sheets or tabs in the shared drive" and "Ask first: deleting anything".
- **Claim differs from the result.** Hand-back: "Added a 'Cheapest' column that shows the lowest price per ingredient." Result: "'YES' on one row per ingredient for 9 of the 12 ingredients".
- **Hand-back items missing.** The brief asked for "which are marked 'not updated'" and "anything left open"; neither was given. The blank butter, cream and eggs rows were not mentioned.
- **The sums.** 55 rows − 14 removed = 41, which matches "41 rows". 9 ingredients marked + 3 blank (butter, cream, eggs) = 12, which matches "12 ingredients". Price dates 14 Oct 2026 and 9 Oct 2026 are in 2026 and match "October price emails". 3 Feb 2025 is before 2026. The hand-back has no date or time, so whether it met "Due: Friday 27 November 2026, 10:00" cannot be told.

#### 4. The reply to send

> Hi Priya,
>
> Thanks for getting through this so quickly. The Millers Co and Greenfield Grains prices from their October price emails, highlighted in yellow, are just what I needed, and the Cheapest column is a good start.
>
> A few things went beyond the brief, so I need to sort them out before Friday's order:
> - **Bramble Dairy:** please forward me the email you sent them, and any reply. Please don't contact them or any other supplier again; I'm handling suppliers while I renegotiate.
> - **Deleted rows and tab:** the brief asked you to mark duplicates and not delete rows. If you can, please put back the 14 rows you removed and the "2024" tab, and mark the duplicates instead. Let me know if you can't.
>
> Still needed on the sheet:
> - The Bramble Dairy rows still show a price date of 3 Feb 2025. Please mark them "not updated".
> - The Cheapest column is blank for butter, cream and eggs. Please mark the cheapest row for each.
> - Please make sure every cell you changed is yellow, including the Cheapest column.
> - Please tell me how you compared prices where suppliers use different units (per kg or per item).
> - When it's done, let Marco know the sheet has changed since you sent the link, and tell me the number of rows before and after, and which rows you marked as duplicates.
>
> Thanks,
> Dana

#### Check these yourself before accepting

- What Priya wrote to Bramble Dairy, and whether it affects your Millers Co renegotiation.
- Whether the 14 deleted rows and the "2024" tab can be got back, and what was in them.
- Whether Marco has the link, and whether he might use the unfinished version for Friday's order.
- Open the sheet: does each ingredient and supplier pair now appear only once?
- Whether the "Cheapest" column cells are yellow.
- How cheapest was compared for any ingredient sold in different units.
- The Hillside Farm price dates, which the description does not give.
- That the Millers Co and Greenfield Grains prices match their October price emails.
- That the finished sheet will be ready by 10:00 on Friday 27 November 2026.

## What to notice

- Turn 1 asked six questions instead of guessing a deadline, a format or whether rows may be
  deleted. Five of them end with "I suggest ...", so Dana's "use your suggestions" closed them.
- Every addition was marked **(suggested)**. After Dana accepted them in bulk, the brief kept them
  apart with a single `*` note, so Priya can tell Dana's words from the tool's.
- "Do it the usual way" became a checkable line ("every cell Priya changed is highlighted in
  yellow") only after Dana defined it.
- "Send the final version to Marco" stayed part of Priya's task, because Dana asked for it and
  Marco is a colleague. Emailing a supplier stayed a "must not".
- Turn 3 put "Stop" first and named what broke the brief in the verdict line. It gave "Can't
  tell" where only Priya's word showed the work, did the row and ingredient sums, and quoted the
  evidence for every verdict.
- What a person should still check: the drafted reply says "I'm handling suppliers while I
  renegotiate", where Dana said she is renegotiating with Millers Co. Close enough to send, but it
  is the tool's wording, not hers.
