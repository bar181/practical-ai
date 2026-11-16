# Estimator: demo

Open [`index.html`](index.html) in any browser. It is one self-contained file and needs no
connection, account or install.

## What it shows

- Three kinds of business: management consulting, kitchen renovation and employment services.
- A job you can change on the left, and the quote it produces on the right.
- For every line: the quantity, the price, and the price list row or rule it came from.
- Assumptions, what was not priced, and the questions to settle before a quote is sent.
- The numbered rules each business wrote down.

## What to notice

1. The starting values reproduce the three worked examples in
   [`../level-simple/examples/`](../level-simple/examples/): totals of 39,000, 30,900 and 68,280.
2. Untick "Scope is not yet fixed" in the consulting example. One rule switches off and the total drops.
3. In employment services, raise permanent placements to 3. The fee falls by 2 points for each.
4. No figure appears without its source. That is the habit the chatbot version is built to keep.

## How the demo differs from the real thing

The demo is a calculator with the rules built in, so the numbers are exact and repeatable. The
simple level gives the same price list and rules to a chatbot as a file. That version can read a
customer's request in their own words and ask about what is missing, and a business can change its
rules without touching code. It should always be checked by a person.

Figures are illustrative units, not market prices. No real company is described.
