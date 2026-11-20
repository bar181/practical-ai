# Worked example: a café team meeting

**Invented.** The café, the supplier and the people are made up. This is the reply a fresh Claude
session gave on 20 November 2026 when given [`../SKILL.md`](../SKILL.md) and the meeting below.
It was graded against the [answer key](../../_build/eval/t1-key.md) and passed.

## The meeting (input)

Meeting date: Monday 23 November 2026.

```
[09:02] Dana (owner): Morning. Main thing today is the Kestrel Fold letter. They're changing our terms from January.
[09:03] Priya (manager): I read it. Minimum order goes up to 400 pounds, and late payment fee is now 5 percent.
[09:04] Dana: Right. I think we stay with them for coffee beans, the quality's too good to switch. Agreed?
[09:04] Priya: Agreed.
[09:04] Marco (head barista): Agreed.
[09:05] Dana: Good, decision made, we stay with Kestrel Fold for beans.
[09:06] Priya: We should combine the bean and milk orders so we clear the 400 minimum. I'll set that up in the order system by Friday.
[09:07] Dana: Perfect, thanks Priya.
[09:08] Marco: The new form they mention, the account update form, wasn't attached to the letter.
[09:08] Dana: Someone should ring Kestrel Fold and ask for that form.
[09:09] Priya: Mm.
[09:10] Dana: Also, we're moving the opening time to 7:30 from next month. That's decided, people have been asking.
[09:10] Marco: Fine by me.
[09:11] Marco: I'll update the opening hours on the website and the door sign by Wednesday.
[09:12] Dana: We need to tell the regulars about the new hours too.
[09:12] Priya: Could go in the newsletter.
[09:13] Dana: And I'll check the late fee with our accountant before the first January invoice.
[09:14] Priya: Should we look at a second bean supplier as a backup?
[09:14] Dana: Let's revisit that soon.
[09:15] Marco: One more: the grinder's making that noise again.
[09:15] Dana: Can somebody book the repair? Not urgent.
[09:16] Dana: OK, thanks all.
```

## The reply (output, unedited)

**In short:** 2 decisions, 6 actions, 3 flagged: all 3 with no agreed owner and no date.

**Assumed:** meeting date Monday 23 November 2026, taken from the transcript; no reader named, so the follow-up is written to the whole team.

### Flags: agree these before you send

| Action | What is missing | The words |
| --- | --- | --- |
| Ring Kestrel Fold and ask for the account update form | Owner not agreed, no date | Dana [09:08]: "Someone should ring Kestrel Fold and ask for that form." Priya [09:09]: "Mm." |
| Tell the regulars about the new opening hours | Owner not agreed, no date | Dana [09:12]: "We need to tell the regulars about the new hours too." Priya [09:12]: "Could go in the newsletter." |
| Book the grinder repair | Owner not agreed, no date | Dana [09:15]: "Can somebody book the repair? Not urgent." |

### Decisions

1. Stay with Kestrel Fold for coffee beans. Dana [09:05]: "Good, decision made, we stay with Kestrel Fold for beans." (Priya and Marco both said "Agreed." at 09:04.)
2. Move the opening time to 7:30 from next month (December 2026). Dana [09:10]: "Also, we're moving the opening time to 7:30 from next month. That's decided, people have been asking."

### Actions

| Action | Owner | Due | The words |
| --- | --- | --- | --- |
| Combine the bean and milk orders in the order system to clear the 400 pound minimum | Priya | Fri 27 Nov (said: by Friday) | Priya [09:06]: "We should combine the bean and milk orders so we clear the 400 minimum. I'll set that up in the order system by Friday." |
| Update the opening hours on the website and the door sign | Marco | Wed 25 Nov (said: by Wednesday) | Marco [09:11]: "I'll update the opening hours on the website and the door sign by Wednesday." |
| Check the late fee with the accountant | Dana | Before the first January invoice (as said; no calendar date given) | Dana [09:13]: "And I'll check the late fee with our accountant before the first January invoice." |
| Ring Kestrel Fold and ask for the account update form | **not agreed** | **not set** | Dana [09:08]: "Someone should ring Kestrel Fold and ask for that form." |
| Tell the regulars about the new hours | **not agreed** | **not set** | Dana [09:12]: "We need to tell the regulars about the new hours too." |
| Book the grinder repair | **not agreed** | **not set** | Dana [09:15]: "Can somebody book the repair? Not urgent." |

### Open questions

- Should there be a second bean supplier as a backup? Priya [09:14]: "Should we look at a second bean supplier as a backup?" Dana [09:14]: "Let's revisit that soon." No owner or date.
- How to tell the regulars. Priya [09:12]: "Could go in the newsletter." Suggested, not settled.

### Follow-up to send

> Hi all, thanks for this morning.
>
> Decided:
> - We stay with Kestrel Fold for coffee beans.
> - We open at 7:30 from next month (December).
>
> Actions:
> - Priya: combine the bean and milk orders in the order system by Fri 27 Nov.
> - Marco: update the opening hours on the website and door sign by Wed 25 Nov.
> - Dana: check the late fee with our accountant before the first January invoice.
>
> Still need an owner and a date:
> - Who will ring Kestrel Fold for the account update form, and by when?
> - Who will tell the regulars about the new hours, and by when?
> - Who will book the grinder repair, and by when?
>
> Open: do we want a backup bean supplier?

Check the flags first, then send it yourself.
