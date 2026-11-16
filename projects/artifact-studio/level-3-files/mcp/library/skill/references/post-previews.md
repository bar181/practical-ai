# Post previews

Read this when the person asks for social posts, an email or a blog post. The rule: never hand
back a list of text. Show each draft the way its audience will see it, so the person reviews the
deliverable and not a document.

## What to build

One HTML file. Each draft sits in a plain frame in the shape of the place it is going.

| Going to | Frame | Show |
| --- | --- | --- |
| LinkedIn, Facebook | Feed post | Name and one line about the person. The text, cut after three lines with a control to read the rest. The picture. The row of actions as plain words |
| Instagram | Picture-first post | The picture first, square or four by five, with a few words on it. Then the caption and at most three tags. A carousel is pictures the reviewer can swipe |
| TikTok, other short video | Upright frame, nine by sixteen | One frame per beat with the words that will be on screen, and the words the person says underneath. Three beats is enough |
| Email | Inbox line, then the message | Sender, subject and preview text above an HTML message at phone width, with one picture and one button |
| Blog | A finished page | The picture, a title that makes a claim, a one-line summary, the author, the text, one line worth quoting |

Working code for every frame is in the library: `sources/02-posts-lib.html` holds the styles and
the two behaviours, `sources/86-socials.html` shows three drafts side by side, and
`sources/87-post-linkedin.html` to `92-post-blog.html` hold one platform each.

## Rules

1. **The person's voice.** Ask for two or three posts they are proud of and match them: sentence
   length, the words they use, how they open and how they end. With none to match, say so in the
   delivery note.
2. **Three drafts when there is a choice to make.** Give each a different way in, such as the
   problem, an analogy or an objection. Name the way in above each frame. Put them side by side
   on a wide screen and in a row to swipe on a phone.
3. **One idea, told differently in each place.** For two platforms, change the picture and the
   way into the story, not only the length.
4. **Their content only.** Facts, numbers and credentials come from the person's notes. Mark a
   gap as `[needs: ...]`.
5. **No invented engagement.** Never show likes, comments, views or follower counts.
6. **Name the platform in words above the frame.** Never draw a platform's logo, and do not copy
   its interface. A plain frame in the right shape is the point.
7. **Stop at the preview.** Nothing is posted, scheduled or sent. A person presses post.

## Running it every day

If the assistant can run on a schedule, the person can ask for the previews to be ready each
morning: draft from a notes folder, save one page, post nothing. Offer this once, after the
first preview has gone well. Do not set it up unasked.

## Delivery note

Use the usual four headings. Under "Chose", name the platform and the way in for each draft.
Under "Check before sharing", list every claim and number in the drafts, and remind the person
that the real feed may cut the text at a different line.
