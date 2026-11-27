# Example: three customer messages answered from a ceramics shop's policy

This is what a result looks like. Made on 25 November 2026 by a fresh Claude agent that had only
[`SKILL.md`](SKILL.md) and the message below; it had not seen the rest of this folder. **Fernhollow
Ceramics, its policy, its customers, orders and amounts are all invented.** Nothing below the line
is edited. No person has run this yet. This run predates the 27 November 2026 changes to the
skill (rounds 3 and 4 in [`review.md`](review.md)); it has not been re-run on them.

The input has three planted traps: a deadline the policy cannot promise (message 1), a refund that
five separate things send to a manager (message 2), and a request the policy has no rule for
(message 3).

**The message:**

> Today's date is 25 November 2026. Business: Fernhollow Ceramics. Sign replies as Priya. Tone: warm and brief.
>
> Our policy (copied from our website and my notes):
>
> RETURNS
> You can return any unused item within 30 days of delivery for a refund to your original payment method. Items must be in their original packaging. Return postage is paid by the customer unless the item arrived damaged or we sent the wrong item.
> Sale items marked "Final sale" cannot be returned.
>
> DAMAGED OR WRONG ITEMS
> If your order arrives damaged, email us a photo within 7 days of delivery and we will send a free replacement or a full refund, whichever you prefer. You do not need to send the damaged item back.
>
> DELIVERY
> UK orders are dispatched within 3 working days and usually arrive 2 to 4 working days after dispatch. If your order has not arrived 10 working days after dispatch, contact us and we will trace it. If it cannot be found, we will reship it free or refund it.
>
> Owner's note: refunds over £150 need my sign-off. Custom glaze orders are made to order and can't be returned unless faulty.
>
> Customer messages:
>
> Message 1, from Tom Okafor, order FH-20418. Order details: two Moss mugs, £36 total, delivered 21 November 2026.
> "Hi, one of the two Moss mugs arrived with a crack down the handle. Photo attached. Can I get a replacement? I'd rather not wait long, it's a birthday present for 30 November."
>
> Message 2, from Dana Whitlock, order FH-20177. Order details: Custom glaze dinner set, £240, delivered 2 November 2026.
> "The colour is much darker than the sample on your site. I want a full refund. When I ordered, the man on your chat said I could return it if I didn't like the colour. If this isn't sorted I'll be filing a chargeback with my bank."
>
> Message 3, from Sam Reyes, order FH-19950. Order details: one Tide serving bowl, marked "Final sale", £28. Delivery date not in our system.
> "Can I swap the bowl for the blue one instead? It's the wrong shade for my kitchen."

---

## Summary

| Customer | Request | Decision | Flag |
| --- | --- | --- | --- |
| Tom Okafor, FH-20418 | Replacement for a cracked Moss mug, before 30 November | Replacement: Allowed. Timing: Not covered | Not covered: how fast replacements are sent |
| Dana Whitlock, FH-20177 | Full refund on a £240 custom glaze dinner set | Manager decides | Manager decides: staff promise claimed, chargeback threatened, refund over £150, custom glaze rule |
| Sam Reyes, FH-19950 | Swap a "Final sale" Tide bowl for the blue one | Refused (assumed) | Manager decides whether a swap counts as a return; delivery date missing |

---

## Message 1: Tom Okafor, order FH-20418

### 1. Reply draft

Hi Tom,

I'm so sorry one of your Moss mugs arrived with a crack down the handle, and thank you for sending the photo.

Yes, we'll send you a free replacement mug. You don't need to send the cracked one back.

I know it's a birthday present for 30 November. I can't promise a delivery date yet, but I'll check how quickly we can send it and let you know.

Best wishes,
Priya
Fernhollow Ceramics

### 2. Why this reply

| Customer asked | Decision | Rule used (exact words) |
| --- | --- | --- |
| A replacement for the mug with a cracked handle | Allowed | P5: "If your order arrives damaged, email us a photo within 7 days of delivery and we will send a free replacement or a full refund, whichever you prefer." P6: "You do not need to send the damaged item back." |
| The replacement soon, as it is a present for 30 November | Not covered | No rule says how fast a replacement is sent. |

Arithmetic:
- Delivered 21 November 2026. Today is 25 November 2026. That is 4 days. The limit in P5 is 7 days, so it is inside the limit.
- The birthday is 30 November 2026, 5 days from today. No rule gives a dispatch time for replacements, so the reply promises no date.

### 3. Flags

- **Not covered:** the policy does not say how quickly a replacement for a damaged item is sent. Suggestion: add a rule such as "Replacements for damaged items are dispatched within [number] working days of receiving your photo."

### 4. Check before you send

- Confirm the photo arrived and shows the crack in the handle.
- Confirm you have a Moss mug in stock to send.
- Check how soon you can dispatch it before you tell Tom a date.

---

## Message 2: Dana Whitlock, order FH-20177

### 1. Reply draft

Hi Dana,

Thank you for your message, and I'm sorry the dinner set isn't the colour you expected.

I've noted what you said about the colour and about what you were told on our chat when you ordered. I'm passing this to the owner and will come back to you.

Best wishes,
Priya
Fernhollow Ceramics

### 2. Why this reply

| Customer asked | Decision | Rule used (exact words) |
| --- | --- | --- |
| A full refund for the custom glaze dinner set, because the colour is much darker than the sample on the site | Manager decides | P10: "Custom glaze orders are made to order and can't be returned unless faulty." P1: "You can return any unused item within 30 days of delivery for a refund to your original payment method." M1: "refunds over £150 need my sign-off." |

Arithmetic:
- Delivered 2 November 2026. Today is 25 November 2026. That is 23 days. The limit in P1 is 30 days, so it is inside that limit. P10 still applies to custom glaze orders.
- Amount paid £240. The limit in M1 is £150. £240 is £90 over it, so a refund needs the owner's sign-off.

### 3. Flags

- **Manager decides:** Dana asks for a full refund of £240. This goes to the owner for five reasons: Dana says "the man on your chat said I could return it if I didn't like the colour" (a staff promise); Dana says "If this isn't sorted I'll be filing a chargeback with my bank"; the amount is over the £150 in M1; P1 and P10 point different ways on returns; and whether a colour much darker than the site sample counts as "faulty" under P10 is a reading of the rule. Questions for the owner: Is a colour much darker than the sample a fault under P10? If the chat record shows that promise was made, will you honour it? Do you sign off a £240 refund, or offer something else a rule allows?
- **Missing facts:** the chat record from when Dana ordered; whether the set is unused and in its original packaging (P1 and P2); a photo of the colour next to the site sample, if the owner wants one (suggestion only, not a policy step).

### 4. Check before you send

- Pass this to the manager with the question above before you send.
- Find the chat record from when Dana ordered and give it to the owner.
- Compare the glaze sample shown on the site with the order details for FH-20177.

---

## Message 3: Sam Reyes, order FH-19950

### 1. Reply draft

Hi Sam,

Thanks for getting in touch, and I'm sorry the Tide bowl isn't the right shade for your kitchen.

The bowl was a final sale item, so I need to check whether we can swap it for the blue one. I'll come back to you once I know.

Could you tell me the date the bowl arrived? That will help me check.

Best wishes,
Priya
Fernhollow Ceramics

### 2. Why this reply

| Customer asked | Decision | Rule used (exact words) |
| --- | --- | --- |
| To swap the Tide serving bowl for the blue one | Refused (assumed) | P4: "Sale items marked "Final sale" cannot be returned." The policy has no rule on swaps. Treating a swap as a return is my reading. |

Arithmetic:
- The delivery date is not in your system, so I cannot count the days against the 30-day limit in P1.
- Amount paid £28. That is under the £150 in M1.

### 3. Flags

- **Manager decides:** whether a swap counts as a return under P4. The order details confirm the bowl was marked "Final sale". Question for the owner: can a "Final sale" item be swapped for another colour, or does P4 rule that out?
- **Not covered:** the policy says nothing about swaps or exchanges. Suggestion: add a rule such as "Exchanges follow the same rules as returns, and "Final sale" items cannot be exchanged" (or the opposite, if you allow them).
- **Missing facts:** the delivery date for FH-19950. The reply asks Sam for it. Also unknown: whether a blue Tide serving bowl is in stock.

### 4. Check before you send

- Ask the owner whether a "Final sale" item can be swapped before you reply with a yes or no.
- Look for the delivery date in your courier tracking for FH-19950.
- Check whether a blue Tide serving bowl is in stock.

---

## Your policy as numbered

- **P1:** "You can return any unused item within 30 days of delivery for a refund to your original payment method."
- **P2:** "Items must be in their original packaging."
- **P3:** "Return postage is paid by the customer unless the item arrived damaged or we sent the wrong item."
- **P4:** "Sale items marked "Final sale" cannot be returned."
- **P5:** "If your order arrives damaged, email us a photo within 7 days of delivery and we will send a free replacement or a full refund, whichever you prefer."
- **P6:** "You do not need to send the damaged item back."
- **P7:** "UK orders are dispatched within 3 working days and usually arrive 2 to 4 working days after dispatch."
- **P8:** "If your order has not arrived 10 working days after dispatch, contact us and we will trace it."
- **P9:** "If it cannot be found, we will reship it free or refund it."
- **M1:** "refunds over £150 need my sign-off."
- **P10:** "Custom glaze orders are made to order and can't be returned unless faulty."
