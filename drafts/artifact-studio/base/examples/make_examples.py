"""make_examples.py: build the worked examples from the library, so they never fall out of step with it.

Each example is a request, the notes that came with it, what the picker chose, and the finished output.
The outputs are made the way an assistant is told to make them: pick with the catalogue's rules, copy the
starter (or the page skeleton), fill it with the notes and nothing else, mark what is missing.
The content is typed in this file. No model runs here. Run after build.py:

    python3 base/examples/make_examples.py
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(HERE); ROOT = os.path.dirname(BASE)
sys.path.insert(0, os.path.join(BASE, "source"))
import catalog as C
STARTERS = os.path.join(BASE, "templates", "starters")
LABEL = {f: dict(v) for f, v in C.FACETS.items()}


def deck(starter, title, slides):
    doc = open(os.path.join(STARTERS, starter), encoding="utf-8").read()
    found = re.findall(r'<section class="dk-s[^"]*">', doc)
    assert len(found) == len(slides), f"{starter} has {len(found)} slides, the example has {len(slides)}"
    it = iter(slides)
    doc = re.sub(r'(<section class="dk-s[^"]*">).*?</section>', lambda m: (lambda body, note: f'{m.group(1)}<div>{body}</div><aside class="dk-note">{note}</aside></section>')(*next(it)), doc, flags=re.S)
    doc = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", doc)
    doc = re.sub(r'aria-label="The [a-z]+ deck, [a-z]+ slides"', f'aria-label="{title}, {len(slides)} slides"', doc)
    return re.sub(r"<!-- [A-Z][a-z]+ deck: starter\..*?-->", "<!-- A worked example. Made from the starter of the same name by base/examples/make_examples.py. -->", doc, flags=re.S)


def picture(starter, texts, style="studio", label=""):
    svg = open(os.path.join(STARTERS, starter), encoding="utf-8").read(); it = iter(texts)
    def fill(m):
        inner = m.group(2)
        if "<tspan" in inner:
            inner = re.sub(r"(<tspan[^>]*>)[^<]*(</tspan>)", lambda t: t.group(1) + next(it, "") + t.group(2), inner)
        else:
            inner = next(it, "")
        return m.group(1) + inner + "</text>"
    svg = re.sub(r"(<text[^>]*>)(.*?)</text>", fill, svg, flags=re.S)
    swap = next(s for s in C.SOCIAL_STYLES if s["id"] == style)["swap"]
    svg = re.sub(r"#[0-9a-fA-F]{6}\b", lambda m: swap.get(m.group(0).lower(), m.group(0)), svg)
    svg = re.sub(r'aria-label="[^"]*"', f'aria-label="{label}"', svg, count=1)
    return re.sub(r"<!-- Social starter.*?-->", "<!-- A worked example. Made from the starter of the same name by base/examples/make_examples.py. -->", svg, flags=re.S)


def write(folder, name, text):
    os.makedirs(os.path.join(HERE, folder), exist_ok=True)
    open(os.path.join(HERE, folder, name), "w", encoding="utf-8").write(text)


EX = []
def example(folder, title, ask, notes, facets, outputs, made, checks, note):
    goal, audience, fmt = facets
    r = C.recommend(goal, audience, fmt)[0] if facets[0] else None
    picked = (f"For \"{LABEL['goal'][goal].lower()}\", \"{LABEL['audience'][audience].lower()}\" and \"{LABEL['format'][fmt].lower()}\", the picker chose **{r['title']}** ({r['strength']} fit, {r['score']} of {15 * len(r['templates'])}). {r['why']}" if r else "No template was needed. This request is answered by one tool and one rule.")
    md = [f"# Example: {title}", "", "A worked example: what was asked, what came with it, what the studio chose and what came back. The business and every figure are invented.", "",
          "## The request", "", f"> {ask}", "", "## The notes that came with it", ""] + [f"- {n}" for n in notes] + ["", "## What the studio picked", "", picked, "", "## How it was made", "", made, "",
          "## The output", ""] + [f"- [`{o}`]({o}): {d}" for o, d in outputs] + ["", "## The note that came back with it", ""] + [f"- **{k}** {v}" for k, v in note] + ["", "## What a good result must have", ""] + [f"{i + 1}. {c}" for i, c in enumerate(checks)]
    md += ["", "## Try it yourself", "", "Give an assistant the request and the notes above" + (", with the starter attached" if "starter" in made else "") + ". Score what comes back against the list above, one point for each. Record the result in [`../README.md`](../README.md).", ""]
    write(folder, "request.md", "\n".join(md))
    EX.append(dict(id=folder, title=title, prompt=ask + "\n\nNotes:\n" + "\n".join("- " + n for n in notes), expected=checks, reference_output=[f"drafts/artifact-studio/base/examples/{folder}/{o}" for o, _ in outputs],
                   request=f"drafts/artifact-studio/base/examples/{folder}/request.md", picked=r["title"] if r else "", shape=fmt or "note"))


# ---- 1. a briefing deck -------------------------------------------------------------------------------------------------------
write("01-briefing-deck", "output.html", deck("deck-briefing.html", "Saturday opening: a decision", [
    ('<p class="k">The recommendation</p><h2>Open Saturday mornings for an eight-week trial.</h2><p>Evening appointments are booked three weeks ahead, and 41 people are waiting.</p>', "Say the answer first. If the partners agree here, skip to the last slide."),
    ('<p class="k">Why</p><ol><li>Evening appointments are full three weeks ahead.</li><li>41 people are on the waiting list.</li><li>58 of the 90 patients we asked said they would use a Saturday.</li></ol>', "Three reasons. The third comes from the spring survey."),
    ('<p class="k">The numbers</p><div class="two"><div><b>41</b><span>people waiting</span><small>For an evening or weekend appointment.</small></div><div><b>58</b><span>of 90 would use a Saturday</span><small>From the spring survey.</small></div></div>', "Two numbers only. Say where each comes from."),
    ('<p class="k">The options</p><table><thead><tr><th scope="col">Option</th><th scope="col">Staff time a week</th><th scope="col">What we expect</th></tr></thead><tbody><tr><td>Do nothing</td><td>None</td><td>The list keeps growing</td></tr><tr><td>Later weekday evenings</td><td>6 hours</td><td>The same staff, longer days</td></tr><tr class="pick"><td>Saturday mornings (recommended)</td><td>12 hours</td><td>8 more appointments a week</td></tr></tbody></table>', "Give doing nothing a fair line. Name the one you recommend."),
    ('<p class="k">What we do not know</p><ul><li>Whether Saturday patients are new, or weekday patients moving.</li><li>Whether two physiotherapists can keep it up past eight weeks.</li></ul><p>The trial answers both. We count every week.</p>', "Say this before they ask. It is why the ask is a trial."),
    ('<p class="k">The decision</p><h2>Approve 12 staff hours a week for eight weeks.</h2><span class="cta">Start date: [needs: a date]</span>', "One decision. The notes gave no start date, so the slide says so."),
]))
example("01-briefing-deck", "a deck for a decision",
        "I need to get the partners to agree to Saturday opening at the clinic. Make me a short deck for Thursday's meeting from these notes.",
        ["We are a physiotherapy clinic with four physiotherapists", "Evening appointments are booked three weeks ahead", "41 people are on the waiting list for an evening or weekend appointment",
         "Spring survey: 58 of 90 patients said they would use a Saturday", "Proposal: Saturday 9 to 1, two physiotherapists (8 hours) and reception (4 hours), which gives 8 appointments",
         "Other option we discussed: later weekday evenings, about 6 extra staff hours a week", "Not sure if Saturday people would be new patients or just weekday ones moving",
         "Not sure the two who volunteered will want to keep doing it", "Want an eight-week trial"],
        ("decide", "executive", "deck"), [("output.html", "the deck, six slides. Open it in a browser. Arrow keys move, N shows the speaker's notes")],
        "The assistant copied the briefing deck starter, [`deck-briefing.html`](../../templates/starters/deck-briefing.html), and replaced the words on each slide with the notes. Nothing was added that is not in the notes.",
        ["The first slide states the recommendation in one sentence", "Every number on the slides appears in the notes: 41, 58 of 90, 12 hours, 8 appointments, eight weeks",
         "The options slide includes doing nothing, and marks the recommended option", "A slide says what is not known", "The missing start date is marked as missing, not invented",
         "The file opens with no internet connection and arrow keys move between slides"],
        [("Chose:", "the briefing deck, because the job is a decision and the readers are the people who decide."), ("Assumed:", "12 staff hours is the sum of 8 hours of physiotherapy and 4 of reception, as the notes give them."),
         ("Missing:", "a start date for the trial. The last slide shows the gap."), ("Check before sharing:", "the survey figures, and whether the partners have seen the waiting list.")])

# ---- 2. a workshop deck -------------------------------------------------------------------------------------------------------
write("02-workshop-deck", "output.html", deck("deck-workshop.html", "The allergen check", [
    ('<p class="k">By the end</p><h2>You will be able to check any order for allergens in under a minute.</h2><p>And know what to do when you are not sure.</p>', "One promise. Ask who has packed an order this week."),
    ('<p class="k">Think of it as</p><h2>A seat belt.</h2><p>It takes a second. You do it every time. You only find out why on the one day it matters.</p>', "Give the picture before the steps."),
    ('<p class="k">The three steps</p><ol><li>Read the allergen line on the order label.</li><li>Match it against the tray card.</li><li>If they differ, or one is missing, stop and ask the shift lead.</li></ol>', "Read each step once, slowly. The example does the explaining."),
    ('<p class="k">Watch one</p><div class="pair"><div><b>The order</b><span>&#8220;Two loaves, no sesame.&#8221;</span></div><div><b>The check</b><span>The tray card says: seeded batch, contains sesame. Stop. Ask.</span></div></div>', "Point at the two things being compared: the label and the tray card."),
    ('<p class="k">Your turn</p><h2>Check this order. One minute.</h2><p class="q">&#8220;Six rolls for a nut-free school.&#8221; Tray card: plain white, baked after the almond croissants.</p>', "Stop talking. One minute on a timer."),
    ('<p class="k">Check yourself</p><ul><li>Did you read the label before the tray?</li><li>Did you look at what was baked before it?</li><li>Did you ask, or did you guess?</li></ul>', "Ask two people what they decided and why."),
    ('<p class="k">Keep this</p><h2>Label. Tray card. Differ? Stop.</h2><p>This card goes on the wall by the packing bench.</p>', "End on the card. Say when you will check in."),
]))
example("02-workshop-deck", "a deck that teaches one skill",
        "New staff start Monday. I want ten minutes at the start of the shift to teach the allergen check before anyone packs an order. Here is how we do it.",
        ["We are a bakery. Orders are packed at the bench from trays", "Every order label has an allergen line. Every tray has a tray card saying what is in the batch",
         "The check: read the allergen line on the label, match it against the tray card, and if they differ or one is missing, stop and ask the shift lead",
         "Real case we use in training: an order for two loaves with no sesame, and the tray was a seeded batch",
         "The one people miss: what was baked on the tray before. Plain rolls baked after almond croissants are not safe for a nut-free order",
         "It should take under a minute", "I want a card for the wall by the packing bench"],
        ("teach", "team", "deck"), [("output.html", "the deck, seven slides, with an exercise on the fifth")],
        "The assistant copied the workshop deck starter, [`deck-workshop.html`](../../templates/starters/deck-workshop.html), and replaced the words. The comparison on the second slide is the assistant's, and the note that came back says so.",
        ["The first slide promises one skill the person can use that day", "There are three steps or fewer, each something a person can do", "One worked example is shown whole, taken from the notes",
         "One slide is an exercise with a time limit, and it looks different from the others", "The last slide can be printed as a card", "Nothing about allergens is stated that is not in the notes"],
        [("Chose:", "the workshop deck, because the job is to teach and the readers are the team."), ("Assumed:", "the seat belt comparison on slide two. It is mine, not from your notes. Change it if it does not fit."),
         ("Missing:", "nothing. The notes covered every slide."), ("Check before sharing:", "the wording of the three steps against your written procedure. This deck is training, not the procedure itself.")])

# ---- 3. a set of social pictures ----------------------------------------------------------------------------------------------
NAME = "Your shop name"
write("03-social-set", "square.svg", picture("social-square.svg", ["Get ready", "for the", "wet months.", "Winter service, $60. 12 to 18 January.", NAME], "bold", "Square post: Get ready for the wet months. Winter service, $60, 12 to 18 January."))
write("03-social-set", "carousel-1.svg", picture("social-carousel-1.svg", ["1 of 3", "What a", "winter service", "covers.", "", "Swipe to see"], "bold", "Carousel, slide 1: What a winter service covers."))
write("03-social-set", "carousel-2.svg", picture("social-carousel-2.svg", ["2 of 3", "1", "Brakes", "Pads checked, cables adjusted.", "2", "Gears", "Cleaned, indexed and oiled.", "3", "Tyres", "Checked for cuts and pumped."], "bold", "Carousel, slide 2: brakes, gears, tyres."))
write("03-social-set", "carousel-3.svg", picture("social-carousel-3.svg", ["3 of 3", "$60 this week.", "Usually $85.", "", "Book at the counter"], "bold", "Carousel, slide 3: $60 this week, usually $85. Book at the counter."))
example("03-social-set", "a week of social pictures",
        "We are running winter service week. I need a square post and a three-slide carousel for it. Make them stand out. Our colours are navy and yellow.",
        ["We are a bike shop", "Winter service week is 12 to 18 January", "A full winter service is $60 that week. It is usually $85",
         "It covers brakes (pads checked, cables adjusted), gears (cleaned, indexed, oiled) and tyres (checked for cuts, pumped)", "People book at the counter"],
        ("announce", "public", "social"), [("square.svg", "the square post, 1080 by 1080"), ("carousel-1.svg", "carousel slide 1, the hook"), ("carousel-2.svg", "carousel slide 2, the three things"), ("carousel-3.svg", "carousel slide 3, the price and the ask")],
        "The assistant copied the social starters from [`templates/starters/`](../../templates/starters/) and replaced the words. \"Navy and yellow\" matched the Bold style, so each colour was swapped for that style's, using the list under `social_styles` in the index.",
        ["Each picture has one idea and a headline of seven words or fewer", "The dates and both prices match the notes exactly", "The carousel runs hook, then the three things, then the ask",
         "The colours are navy and yellow, and every text can be read against its background", "The shop's name is a placeholder, because the notes did not give one"],
        [("Chose:", "the square post and the three-slide carousel you asked for, in the Bold style because you said navy and yellow."), ("Assumed:", "that \"book at the counter\" is the only way to book."),
         ("Missing:", "the shop's name. The square post shows a placeholder."), ("Check before sharing:", "the dates and the two prices. To post, open each file in the Social tab's download, or export it as a PNG.")])

# ---- 4. a one-page report -----------------------------------------------------------------------------------------------------
P = {r["id"]: r["hex"] for r in C.palette(140)["roles"]}
write("04-one-page-report", "output.html", f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>October in one page</title>
<!-- A worked example. Recipe: one-page report. Voice: executive brief. Look: a palette built from the owner's green (hue 140).
     Built on skills/artifact-studio/assets/page-skeleton.html. No script: everything is on the page when it loads. -->
<style>
:root{{--bg:{P['surface']};--panel:{P['surface2']};--line:{P['line']};--muted:{P['muted']};--ink:{P['ink']};--accent:{P['accent']};--soft:{P['accentsoft']};
  --display:system-ui,-apple-system,"Segoe UI",sans-serif;--text:Georgia,"Iowan Old Style",serif}}
*,*::before,*::after{{box-sizing:border-box}}html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--bg);color:var(--ink);font:400 1.1rem/1.55 var(--text)}}
h1,h2,h3{{font-family:var(--display);margin:0;line-height:1.1;text-wrap:balance}}p{{margin:0}}
.wrap{{max-width:860px;margin-inline:auto;padding-inline:20px}}section{{padding-top:44px}}
header{{padding:48px 0 0}}.kicker{{font:700 .95rem/1 var(--display);color:var(--accent)}}
h1{{font-size:clamp(2.1rem,7.5vw,3.6rem);letter-spacing:-.02em;margin-top:12px;max-width:14em}}.lede{{margin-top:14px;max-width:34em;font-size:1.2rem}}
h2{{font-size:1.5rem}}.cards{{display:grid;gap:12px;margin-top:18px}}@media(min-width:680px){{.cards{{grid-template-columns:repeat(3,1fr)}}.cards.two{{grid-template-columns:repeat(2,1fr)}}}}
.card{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px;display:flex;flex-direction:column;gap:6px}}
.card .lab{{font:700 .9rem/1.2 var(--display);color:var(--muted)}}.card b{{font:700 2.5rem/1 var(--display);letter-spacing:-.03em;font-variant-numeric:tabular-nums}}.card .was{{font:400 .95rem/1.3 var(--display);color:var(--muted)}}
.card h3{{font-size:1.15rem}}.card p{{font:400 1rem/1.45 var(--display);color:var(--muted)}}.chip{{align-self:flex-start;background:var(--soft);border-radius:999px;padding:5px 10px;font:700 .8rem/1 var(--display)}}
.bars{{margin-top:18px;display:grid;gap:10px;font:400 .98rem/1.2 var(--display)}}.bars div{{display:grid;grid-template-columns:5.5em 1fr;gap:10px;align-items:center}}
.bars i{{display:flex;align-items:center;justify-content:flex-end;height:34px;border-radius:0 6px 6px 0;padding-right:10px;font-style:normal;font-weight:700;background:var(--line);color:var(--ink)}}.bars .now i{{background:var(--accent);color:#fff}}
ul.plain{{margin:14px 0 0;padding:0 0 0 1.1em;max-width:36em}}ul.plain li{{margin-top:6px}}
.gap{{background:var(--panel);border-left:4px solid var(--accent);border-radius:8px;padding:14px 16px;margin-top:16px;max-width:38em;font:400 1rem/1.45 var(--display)}}
footer{{padding:44px 0 56px;font:400 .9rem/1.4 var(--display);color:var(--muted)}}
</style>
</head>
<body>
<main>
  <header class="wrap"><p class="kicker">October report</p><h1>October was our best month this year.</h1>
    <p class="lede">Revenue rose to $84,200 from $71,500 in September. The main cause: quotes now go out in two days, and more of them turn into jobs.</p></header>
  <section class="wrap" aria-labelledby="n"><h2 id="n">The numbers</h2>
    <div class="cards"><div class="card"><span class="lab">Revenue</span><b>$84,200</b><span class="was">Up from $71,500 in September</span></div>
      <div class="card"><span class="lab">Jobs completed</span><b>23</b><span class="was">Up from 19</span></div>
      <div class="card"><span class="lab">Quotes that became jobs</span><b>46%</b><span class="was">Up from 38%</span></div></div>
    <div class="bars" role="img" aria-label="Revenue: September $71,500, October $84,200"><div><span>September</span><i style="width:85%">$71,500</i></div><div class="now"><span>October</span><i style="width:100%">$84,200</i></div></div></section>
  <section class="wrap" aria-labelledby="c"><h2 id="c">What changed</h2>
    <ul class="plain"><li>Quotes now go out within two days of a visit. It used to take six.</li><li>One van was off the road for four days. Both crews shared the other, and no job was moved.</li></ul></section>
  <section class="wrap" aria-labelledby="x"><h2 id="x">What is next</h2>
    <div class="cards two"><div class="card"><span class="chip">This month</span><h3>Hire one seasonal worker</h3><p>For leaf clearance in November.</p></div>
      <div class="card"><span class="chip">Decide by 15 November</span><h3>A second van, or not</h3><p>One van was off the road for four days in October.</p></div></div></section>
  <section class="wrap" aria-labelledby="g"><h2 id="g">What this report does not have</h2>
    <p class="gap">[needs: profit for October] The notes give revenue but not costs, so this page says nothing about profit.</p></section>
  <footer class="wrap">Made from the owner's notes for October. This is a worked example: the business and its figures are invented.</footer>
</main>
</body>
</html>
""")
example("04-one-page-report", "a one-page report",
        "Turn my October notes into one page I can send to my business partner. She reads on her phone and wants the answer first. Our colour is green.",
        ["We are a landscaping company with two crews", "October revenue $84,200. September was $71,500", "Jobs completed: 23 in October, 19 in September",
         "Quotes that became jobs: 46%, up from 38%", "We started sending quotes within two days of the visit. It used to take six", "One van was off the road for four days. Crews shared. No jobs moved",
         "November: hire one seasonal worker for leaf clearance", "Need to decide about a second van by 15 November"],
        ("report", "executive", "page"), [("output.html", "the page. One file, no script, reads on a phone")],
        "The assistant built on the skill's page skeleton. The colours come from the palette rule with a green hue of 140, which gives seven colours and checks each text and background pair. The three figures are stat cards and the two next steps are action cards, both from the design ideas.",
        ["The headline is the answer, not a title such as \"October report\"", "The three figures match the notes, and each says what it was before", "Change is written in words, not shown by colour alone",
         "Profit is marked as missing, because the notes gave no costs", "On a phone nothing scrolls sideways and all text is readable", "The page shows everything with scripts turned off"],
        [("Chose:", "the one-page report in the executive brief voice, because she wants the answer first. Colours built from your green."), ("Assumed:", "that faster quotes are the main cause of the rise. Your notes put the two side by side but do not say so."),
         ("Missing:", "profit. The page says so in its last section."), ("Check before sharing:", "the sentence that says why revenue rose. It is the one claim on the page that is an inference.")])

# ---- 5. a palette from one colour ---------------------------------------------------------------------------------------------
pal = C.palette(320)
write("05-brand-palette", "output.md", "\n".join(["# Colours, from hue 320", "", "| Use | Colour |", "| --- | --- |"] + [f"| {r['use']} | `{r['hex']}` |" for r in pal["roles"]] +
      ["", "## Contrast", "", "| Pair | Ratio | Needs | Result |", "| --- | --- | --- | --- |"] + [f"| {c['pair']} | {c['ratio']:.1f} to 1 | {c['needs']:g} | {'Passes' if c['passes'] else 'Fails'} |" for c in pal["checks"]] + ["", "## Rule", "", pal["rule"], ""]))
example("05-brand-palette", "a palette from one brand colour",
        "All I have is our pink, the one on the sign. I need the rest of the colours for our pages and posts.",
        ["We are a florist", "The pink on the sign is a deep pink, around 320 on the colour wheel", "No other brand colours have ever been chosen"],
        ("", "", ""), [("output.md", "seven colours with a job each, and a contrast table. Paste it into your design spec")],
        "No template is involved. The assistant used the palette rule in the skill's design ideas: each role is a fixed lightness and strength, with the hue taken from the brand. With the MCP server connected this is one call to `make_palette` with a hue of 320.",
        ["There are seven colours, each with a named job", "There is exactly one accent colour, for buttons and links", "The greys carry a trace of the pink", "Every text and background pair is listed with its ratio, and each passes",
         "The result says how much of a page each colour should take"],
        [("Chose:", "a palette built from hue 320."), ("Assumed:", "320 for \"deep pink\". A phone photo of the sign would let me read it properly."),
         ("Missing:", "the exact colour of the sign."), ("Check before sharing:", "hold the accent colour next to the sign. If it is off, tell me warmer or cooler and I will move the hue.")])

# ---- 6. taking in a design you like -------------------------------------------------------------------------------------------
write("06-inspiration-card", "output.md", """# A report that opens on one number

| | |
| --- | --- |
| Seen | A charity's annual review, on its website |
| Filed | 2026-11-15 |
| Tags | page, number, report |
| Status | Inbox. Not reviewed |

## What works

The first screen is one number and seven words saying what it counts. Nothing else: no menu, no logo
above it, no photograph. You understand the year before you scroll. Each section after it opens the
same way, with a smaller number, so the page has a rhythm you can feel by the third one. The last
section breaks the pattern with a sentence and no number, which makes it land.

## Closest thing in the library

The one-page report, which opens with a headline and then three stat cards. This differs by giving
the whole first screen to a single figure and repeating that shape down the page.

## Decision

Change an existing template: offer the one-page report with a "one number first" opening.
""")
example("06-inspiration-card", "keeping a design you like",
        "I just saw an annual review that opened with one huge number and nothing else. Every section did the same with a smaller one. Loved it. Keep that for me.",
        ["It was a charity's annual review, on their website", "The first screen was one number and a few words", "Each section opened with a smaller number", "The last section had no number, just a sentence"],
        ("", "", ""), [("output.md", "the card, as it would be filed in `base/inspiration/inbox/`")],
        "No template is involved. The assistant wrote a card from [`card-template.md`](../../inspiration/card-template.md) in its own words. It recorded the idea: the structure and the rhythm. It copied nothing: no text, no figures, no name. With the MCP server connected this is one call to `add_inspiration`.",
        ["The card describes structure and rhythm in the assistant's own words", "It names no organisation and copies no text, figure or picture from the original", "It names the closest template in the library and how this differs",
         "It proposes one of three outcomes: keep as a note, change a template, or build a new part", "It has tags, so it can be found when a report is next made"],
        [("Chose:", "to file a card, not to build anything."), ("Assumed:", "that what you liked was the structure, not the charity's colours or wording."),
         ("Missing:", "a link to the page. Add it to the card if you want to find it again."), ("Check before sharing:", "nothing. The card is for you.")])

# ---- the index and the skill's evals ------------------------------------------------------------------------------------------
rows = [f"| [{e['title'][0].upper() + e['title'][1:]}]({e['id']}/request.md) | {e['picked'] or 'No template: one rule'} | " + ", ".join(f"[`{os.path.basename(o)}`]({e['id']}/{os.path.basename(o)})" for o in e["reference_output"]) + " | Not yet |" for e in EX]
write(".", "README.md", "\n".join(["# Worked examples", "", "Six requests, each with the notes that came with it, what the studio picked, and what came back. Read one to see what to expect. Run one to test the studio.", "",
    "**Think of them as** the photographs on a menu. They show what the dish looks like when it is made properly.", "",
    "| Example | What was picked | Output | Tested in a fresh chat |", "| --- | --- | --- | --- |"] + rows + ["",
    "## How to test one", "", "1. Open the example's `request.md`.", "2. Give a fresh assistant the request and the notes. Attach the starter if the example names one. At level 1, paste [`AI-INSTRUCTIONS.md`](../../level-1/AI-INSTRUCTIONS.md) first.",
    "3. Score what comes back against \"What a good result must have\", one point for each line.", "4. Change \"Not yet\" in the table above to the score and the date, in [`make_examples.py`](make_examples.py), which writes this file.", "",
    "## What these are and are not", "", "- Every business and figure is invented.", "- The outputs were made by the assistant that built this repository, following the skill, with the content typed into [`make_examples.py`](make_examples.py). **No fresh assistant has been given these requests yet.** That is what the last column is for.",
    "- They are rebuilt from the starters each time the script runs, so they cannot fall out of step with the library.", "- The same six requests are the skill's test cases, in [`skills/artifact-studio/evals/evals.json`](../../../../skills/artifact-studio/evals/evals.json).", ""]))
ev = os.path.join(ROOT, "..", "..", "skills", "artifact-studio", "evals"); os.makedirs(ev, exist_ok=True)
json.dump({"skill": "artifact-studio", "how_to_run": "Give a fresh assistant the skill and one prompt. Score the result one point for each line in expected. The reference output shows one result that scores full marks.",
           "status": "Written. Not yet run against a fresh assistant.", "evals": [{k: e[k] for k in ("id", "prompt", "expected", "reference_output", "request")} for e in EX]}, open(os.path.join(ev, "evals.json"), "w", encoding="utf-8"), indent=1)
print(f"{len(EX)} examples written:", ", ".join(e["id"] for e in EX))
