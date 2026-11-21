# Friction with the guide

Blunt summary: the post preview is bolted on after the main method and the main method does not know it exists. Steps 2, 3 and 4 give the wrong answer for it if read literally. I had to overrule the numbered steps with one bullet near the bottom of the file.

Ordered by how much each one cost.

## 1. Step 2 sends a LinkedIn post to the one-page report

> "2. **Recipe.** Pick one from the table. If named, use it. If none fits, use the one-page report."

> "The same steps make three other things."

The post preview is not in the recipe table. Read literally, step 2 makes three LinkedIn drafts into a one-page report with numbers and a trend chart. The later section says "the same steps" apply, which makes it worse, not better. I ignored step 2 and treated "a post preview" as the recipe. The guide never says I may.

## 2. Step 3 has no answer for a post

> "3. **Voice.** Pick one from the table. If named, use it. Otherwise take the recipe's first voice."

> "Write in the person's own voice: ask for two or three posts they are proud of and match them."

A post preview has no "Voices" column, so there is no first voice. The person's own voice is not in the voice table, so "pick one from the table" cannot be followed. It is also unclear whether a table voice still applies underneath (Practical instructor fits this content well) and whether "the voice sets the order, the counts and the headings" means anything when each draft must have a different order. I used no table voice.

## 3. The guide tells me to ask for posts, and step 1 forbids the question

> "Ask at most two questions, only if you cannot tell the audience or the job."

> "ask for two or three posts they are proud of and match them."

Asking for sample posts is not a question about the audience or the job, so step 1 forbids it. There is also no fallback for a person who has no posts, which is exactly this person. He gave a description of his voice instead. The guide does not say a description is acceptable. I assumed it is.

## 4. "Side by side" against "design at 390 pixels first"

> "show three drafts side by side, each with a different way in"

> "Design at 390 pixels wide first. Nothing scrolls sideways except a table inside its own container."

Three feed posts cannot sit side by side at 390 pixels and stay readable. A swipe row would break the sideways rule. I stacked them on a phone and put them side by side from 1080 pixels. So at the width the guide says to design for first, the page does not do what the same guide says the page must do.

Related: the parts list offers a "swipe gallery", which is a thing that scrolls sideways and is not a table.

## 5. "An image they supplied" when there are three, and they are content, not branding

> "4. **Look.** In order: the person's design spec; colours taken from an image they supplied; the voice's default look."

> "Show each draft in a plain frame"

Three pictures were attached. The guide says "an image". No rule for which one. I took the first listed. That is a coin toss dressed as a rule.

Bigger problem: these pictures are the pictures in the posts, not the person's brand. Taking the page colours from one of them makes the frame match one draft and not the other two, which tilts a comparison that is meant to be fair. "A plain frame" suggests neutral colours, but step 4 puts the image above any default, so I followed step 4. I think the result is the wrong call and the guide forced it.

## 6. "Most vivid that is not skin or sky" does not survive a cartoon

> "The most vivid that is not skin or sky becomes the accent, used sparingly."

"Vivid" is not defined. By saturation, the most vivid colour in the cartoon is the teal (`#1c9ba8`), which is the same hue as the largest colour that already became the background. The characters' skin is blue. There is no sky, but the wall does the job of one. I chose the red and can defend it, but someone else following the same line would land on teal.

## 7. The contrast check has no "if it fails"

> "Check text contrast is 4.5 to 1 or better."

The red from the picture measured 3.44 to 1 on the frame. The guide says to check, not what to do next: darken it, pick another colour, or stop using it for text. I darkened it to `#a04e35` (5.40 to 1). The colour on the page is therefore not a colour in the picture.

## 8. "Cut after three lines" is not where the feed cuts

> "the text cut after three lines with a control to read the rest"

The person asked for the text "cut where the feed would cut it". The guide gives a fixed three lines. Three lines of what width and what type size? Do blank lines count? The real cut moves with the screen. I counted blank lines as lines and wrote each opening as three short lines so the cut falls in the same place at every width I tested. The guide says none of this. It also never says the lines before the cut should carry the way in, which is the whole point of showing the cut.

## 9. The name line has nothing to hold

> "a feed post (name, the text cut after three lines ..."

> "If the page would mislead without it, a number, a name, a date or a price the reader will act on, mark it on the page as `[needs: ...]`. Otherwise leave the page clean and list the gap under Missing."

The frame requires a name. The message does not give one. The rule offers two choices: mark it, or leave the page clean. A missing name in a private preview misleads nobody, so the rule says leave the page clean. But the slot cannot be empty. I wrote `[needs: your name]`, which the rule does not strictly call for. That sentence is also hard to parse: the list "a number, a name, a date or a price the reader will act on" is dropped into the middle of the condition with no connecting word.

## 10. "Actions as plain words" against "never copy its interface"

> "the actions as plain words"

> "Never draw a platform's logo or copy its interface"

Which words? The platform's own action names are its interface. I used Like, Comment, Repost and Send because the preview has to be recognisable. The guide should either list the words or say that naming the actions is allowed. It also does not say the words must not be buttons. I worked that out from "Every button does something".

## 11. The one required control has no build recipe

> "with a control to read the rest"

> "Build tabs from radio buttons and labels so they switch with scripts off"

> "Real controls for interaction: `button`, `input`, `details`, `select`."

The guide tells me how to build tabs without script. It does not tell me how to build the control it requires for every feed post, or whether that control must work with scripts off. `details` cannot cut text after three lines. A `button` needs script. I used a checkbox and a label with a line clamp. It works with scripts off and by keyboard, but I was guessing at what the guide wants.

## 12. "The picture", singular, with three pictures and three drafts

> "the picture"

One picture in each draft? The same picture in all three? All three in each? I put one in each and matched it to the way in. Silent in the guide.

## 13. Image cropping against showing the post as the feed shows it

> "Images: alt text that says what is shown, cropped to the subject at phone width"

A feed preview should show the picture the way the feed would, which is whole. The build rule says crop to the subject. The three pictures have three shapes (wide, less wide, square), so the three frames have three heights and the action rows do not line up. The card rule "The same padding and the same order in every card of a row" does not say whether the same height is wanted. I showed the pictures whole.

## 14. Two readers, one "job of the page"

> "Find the content, any media, the audience, the one job of the page, and where it will be seen."

A post preview has two audiences: the person choosing a draft, and the people who will see the post. The guide does not separate them. The page's job (choose one) and the post's job (get a reader to try the link) are different, and "where it will be seen" has two answers. I treated the page as for the person and the words as for the feed.

## 15. Writing a post means writing new sentences. Where is the line?

> "You add structure and craft. You never add facts."

> "Every number, name, date and quote is in the supplied content"

Three drafts in someone's voice cannot be made only from the notes' own sentences. Each needs joining words and an ending that is "a step or a question", which the notes do not supply. "So tell it three things" turns a note into an instruction. "That is how you start with Artifact Studio" ties two notes together. Are those facts? The guide gives no test. I listed every such sentence under Assumed.

## 16. This request fits none of the three rows

> "| One sentence (beginner) | ... |"
> "| Names recipe, voice, look, parts (advanced) | Follow them exactly |"
> "| "Use the artifact-studio skill" (expert) | ... the note in full |"

The message is longer than one sentence, names the kind of thing and the voice, names no look, and does not say "use the skill". The middle row says nothing about how long the note should be. I wrote a full note.

## 17. Loading the front-end design skill starts an argument the guide does not settle

> "If a front-end design skill is available (for example `frontend-design`), load it as well."

I loaded it. It tells me to make opinionated, distinctive choices, to avoid "unnecessary typographic labels above content", and to use what is known about the client. The guide wants "a plain frame", requires two labels above every frame (the way in and the platform), and takes the colours from a picture. The guide does not say which wins. I let the guide win everywhere and used the skill only for type choices and to remove decoration.

## 18. No word on helping the person take the chosen draft away

> "Stop at the preview: nothing is posted or sent."

> "One main action."

The obvious next move for the person is to copy the draft they pick. The guide does not say whether a copy button is wanted or whether it counts as going past the preview. I left it out. The person has to open the text and select it by hand.

## 19. "Show the page as a rendered page if you can"

> "Show the page as a rendered page if you can: an artifact, a canvas or a preview. A bare HTML file opens as code on many phones."

Not a contradiction in the guide. In this test the output had to be a file, so the person gets the bare HTML file the guide warns about. I said so at the top of the note.

## One slip of my own

When I listed my run folder I also listed the top level of `/tmp/runs` and saw the names of the other run folders. I opened none of them and read nothing in them.
