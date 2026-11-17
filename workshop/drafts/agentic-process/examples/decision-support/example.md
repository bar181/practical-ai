# Example: should an invented bakery start office catering?

This is what a good result looks like. Made on 16 November 2026 in Claude by a new AI session
that had only the tool's instructions and the message below. It could search the web and could not
ask questions. The bakery is invented; the sources are real and were read that day. Nothing below
the line is edited.

It was made with the earlier version of the instructions. [`SKILL.md`](SKILL.md) has the same
steps and rules, plus three later changes: the **Start** section, an option must score above
"do nothing" to lead, and a score that rests on a fact not found counts as 0 and is listed as a
judgement call. Its log is in
[round 6](../../../../plans/archive/agentic-process/v1-project/level-3-files/test-runs/decision-support/round-6/friction.md).

**The message:**

> Here is my business profile, then my question.
>
> Business profile: Harbour Lane Bakery. We sell bread, pastries and coffee to walk-in customers. Three shops in Hamilton, Ontario, 22 staff, about 1.4 million dollars in sales a year. Goals for the next twelve months: grow sales 10 percent, raise weekday afternoon sales, keep the team from burning out. Limits: up to 25,000 dollars to invest, no new building, the head baker already works six days. Risk: medium. My business partner has a say in big decisions.
>
> My question: should we start a weekday catering service for offices near our shops?

---

## Business profile

- **Business:** Harbour Lane Bakery. Bread, pastries and coffee, sold to walk-in customers.
- **Where and size:** three shops in Hamilton, Ontario; 22 staff; about $1.4 million in sales a year.
- **Goals for the next twelve months (in your order):** 1. grow sales 10 percent; 2. raise weekday afternoon sales; 3. keep the team from burning out.
- **Limits:** up to $25,000 to invest; no new building; the head baker already works six days.
- **Risk:** medium.
- **Who else decides:** your business partner, on big decisions.

Save this profile and paste it at the top of your next question (or save it as a file in this project if you are using one), so I never have to ask again.

---

## 1. Frame the decision

**Question:** Should Harbour Lane Bakery start a weekday catering service for offices near its three shops?

**Options**
- **A. Do nothing.** Stay walk-in only.
- **B. Full weekday office catering** from all three shops: take orders, prepare platters, deliver to nearby offices.
- **C. Eight-week pilot from one shop** (proposal). Pre-order breakfast and meeting boxes made from your existing menu, ordered by 2 pm the day before, delivered or picked up, a cap of 3 orders a day, spending cap $2,000 for packaging, insulated carriers, flyers and a simple order form. It tests the riskiest part: whether nearby offices order often enough, and whether the team can fill orders without the head baker working more.

## 2. Research

| Fact | Source and date |
|---|---|
| Canada's national office vacancy fell for the fourth quarter in a row, to 13.4% in Q2 2026 (Colliers). | CP24, 9 Jul 2026 |
| Stricter office attendance rules are sending more workers to employer food services; Aramark's business-and-industry unit was its fastest-growing segment for seven quarters. Mostly US and Europe. | Bloomberg via Insurance Journal, 25 Aug 2025 |
| A Toronto office-catering startup (launched Oct 2025) reports "strong volume"; its target is workplaces of 20 to 200 staff with recurring orders. No figures given. | Retail Insider, 3 Jun 2026 |
| Hamilton Convention Centre breakfast (croissants, muffins, yogurt, fruit, coffee): $19.95 per person, plus 17% facility fee and 13% HST, minimum 25 guests. | HCC Breakfast Menu, prices valid to 31 Dec 2026; read 16 Nov 2026 |
| A business directory lists 20 caterer companies in Hamilton. | Scott's Directories, read 16 Nov 2026 |
| Potentially hazardous food must be kept at 4°C or lower or 60°C or higher, including during transport; at least one trained food handler or supervisor on site every hour the premises operates. | O. Reg. 493/17 (Ontario e-Laws), read 16 Nov 2026 |
| A food premises in Hamilton needs a business licence; tell Public Health and Building and Licensing before building or renovating. | City of Hamilton, page modified 3 Feb 2026 |
| Ontario general minimum wage is $17.95 an hour from 1 Oct 2026. | Hicks Morley, 1 Apr 2026 |
| Number of offices and office workers near your three shops; Hamilton office vacancy | not found |
| Fees on catering marketplaces such as ezCater | not found (page did not load) |
| One-time cost of a full catering setup (vehicle, equipment) | not found (not researched) |
| Whether your shops' current licence covers delivered catering | not found |

**Estimates**
- 10% sales growth = 0.10 × $1,400,000 = **$140,000 a year**. Over 260 weekdays (52 × 5, holidays not removed) that is about **$538 a weekday** across all three shops (estimate).
- At the convention centre's $19.95 a person, $538 is about 27 people a day (538 ÷ 19.95). Your own prices will differ (estimate).
- Every hour a staff member spends delivering costs at least $17.95 in wages before payroll costs (estimate, from the minimum wage).

## 3. Compare and recommend

**Limits**
| Test | A | B | C |
|---|---|---|---|
| No option may spend more than $25,000 | pass | unknown (setup cost not found) | pass ($2,000 cap, proposal) |
| No option may need a new building | pass | pass | pass |
| No option may add to the head baker's hours (assumed: you check this first) | pass | unknown | pass (order cap; orders filled by other staff, proposal) |

No option dropped.

**Scores** (against doing nothing, next twelve months)
| Goal | B. Full catering | C. Pilot |
|---|---|---|
| 1. Grow sales 10% | +1: a new source of sales | +1: some new sales, small |
| 2. Weekday afternoon sales | 0: office orders are mostly for morning and lunch meetings (assumed) | 0: same |
| 3. Avoid burnout | -1: new work across three shops | -1: new work, though capped |
| **Total** | **0** | **0** |

Do nothing scores 0 on every goal, total 0.

**Leading option:** a three-way tie at 0. Goal 1 breaks it: B and C (+1) beat doing nothing (0). Goals 2 and 3 are tied. The smaller, easier option wins: **C, the pilot.**

**Check first:** yes. The number of offices near your shops is "not found", and if there are few, the pilot would not add sales and doing nothing would lead. Cheapest check: count offices within about ten minutes of each shop and ask ten office managers or regular customers whether they would order, and how often. Same week: ask City of Hamilton Public Health and Licensing whether your licence covers delivered orders, and ask your insurance broker about staff delivering in their own cars.

**Judgement calls** (check these first)
1. *Head baker.* I read "already works six days" as a rule: no option may add to his or her hours. Other reading: it is background only. Would not change the leading option.
2. *Afternoon sales.* I read this as sales made on weekday afternoons, which office catering mostly is not. Other reading: afternoon meeting orders count. Both B and C would gain +1; C still leads.
3. *Burnout.* I scored any new work as worse. Other reading: a capped pilot using quiet afternoon hours is neutral. C would then score +1 and lead outright. No change.
4. *Budget.* I read $25,000 as one-time spending. Other reading: it includes first-year wages. B becomes more likely to fail; C still leads.
5. *Longer view.* Over two to three years full catering could add more sales than a pilot. No change: if the pilot works, it leads into B.

## 4. SWOT for the recommended option (C, the pilot)

| **Strengths** | **Weaknesses** |
|---|---|
| Uses products you already make (option) | Adds work for a team you want to protect (profile) |
| Three shops already near offices (profile) | One shop only, so small sales at first (option) |
| Capped at $2,000 and eight weeks (proposal) | Head baker already at six days; little spare baking capacity (profile) |
| **Opportunities** | **Threats** |
| Office vacancy falling four quarters in a row (CP24, 9 Jul 2026) | Office demand near your shops: not found |
| Employers using food to bring staff back (Insurance Journal, 25 Aug 2025; Retail Insider, 3 Jun 2026) | 20 caterers already listed in Hamilton (Scott's Directories) |
| Convention-centre breakfast costs $19.95 a person plus fees, 25-guest minimum; room for smaller orders (HCC menu; assumed) | Food safety in transport and licence rules (O. Reg. 493/17; City of Hamilton); delivery wages at least $17.95/h (Hicks Morley) |

---

## 5. The brief

**Decision:** Should Harbour Lane Bakery start a weekday catering service for offices near its shops?

**Recommendation:** Run an eight-week, pre-order office catering pilot from one shop, after a one-week check that enough nearby offices would order.

**Why**
- It is the only option that adds sales while staying well inside the $25,000 limit and away from the head baker's hours.
- Full catering and the pilot score the same against your goals; the pilot wins as the smaller, easier option.
- Office demand near your shops is unknown. The pilot finds out for $2,000 (proposal), not tens of thousands.

**SWOT**

| **Strengths** | **Weaknesses** |
|---|---|
| Existing products (option); shops near offices (profile); capped cost and time (proposal) | More work for the team (profile); small sales from one shop (option); head baker already at six days (profile) |
| **Opportunities** | **Threats** |
| Office vacancy falling (CP24, 9 Jul 2026); employers using food to bring staff back (Insurance Journal, 25 Aug 2025); convention-centre price $19.95 a person, 25-guest minimum (HCC menu) | Local office demand not found; 20 Hamilton caterers listed (Scott's); food-safety and licence rules (O. Reg. 493/17; City of Hamilton) |

**Risks and how to reduce them**
1. *Too few orders.* Check offices first; stop at eight weeks if fewer than 10 orders a week (proposal).
2. *Team overload.* Cap at 3 orders a day; the head baker takes no catering work; stop if overtime rises.
3. *Food safety, licence or insurance gap.* Keep cold items at 4°C or lower in transport; confirm with City of Hamilton Public Health and Licensing and your insurance broker.

**Next steps (next 30 days)**
1. Pick the shop. Count offices within ten minutes and ask ten office managers or regulars if they would order.
2. Call City of Hamilton (Public Health, Licensing) and your insurance broker. Ask your accountant how HST applies to delivered orders.
3. Set two boxes, prices from your own costs, an order form and the cap; book the first orders.

**What would change this recommendation**
- The office check finds little interest: do nothing.
- Licence or insurance changes cost more than the pilot budget: do nothing for now.
- The pilot reaches 10 orders a week with repeat offices (proposal): plan full catering, costed within $25,000.
- None of the judgement calls would change it.

**Assumptions**
- The head baker's six days is a hard limit.
- Office orders fall mostly in morning and lunch, not afternoons.
- $25,000 means one-time spending.
- Staff other than the head baker can fill and deliver three orders a day.

**Sources**
- Colliers via CP24, "Office, industrial real estate vacancies dropping amid strong demand", https://www.cp24.com/news/money/2026/07/09/office-industrial-real-estate-vacancies-dropping-amid-strong-demand-colliers-report/ , 9 Jul 2026
- Bloomberg via Insurance Journal, "Stricter Return-to-Office Policies Are Boosting Growth for Catering Providers", https://amp.insurancejournal.com/news/international/2025/08/25/836685.htm , 25 Aug 2025
- Retail Insider, "Toronto startup Nüu Catering bets office catering can help drive return-to-office culture", https://retail-insider.com/retail-insider/2026/06/toronto-startup-nuu-catering-bets-office-catering-can-help-drive-return-to-office-culture/ , 3 Jun 2026
- Hamilton Convention Centre, "HCC Breakfast Menu", https://hccevents.ca/wp-content/uploads/2025/08/HCC-Breakfast-Menu.pdf , prices valid to 31 Dec 2026; read 16 Nov 2026
- Scott's Directories, "Caterers Companies in Hamilton, Ontario", https://www.scottsdirectories.com/canada-b2b-database/ontario/hamilton/naics722320-caterers , read 16 Nov 2026
- Government of Ontario, "O. Reg. 493/17: Food Premises", https://www.ontario.ca/laws/regulation/170493 , read 16 Nov 2026
- City of Hamilton, "Food Premises & Food Handling Requirements", https://www.hamilton.ca/build-invest-grow/operating-business/health-requirements-inspections/food-premises-food-handling , modified 3 Feb 2026
- Hicks Morley, "Ontario Minimum Wage to Increase October 1, 2026", https://hicksmorley.com/2026/04/01/ontario-minimum-wage-to-increase-october-1-2026/ , 1 Apr 2026

This is not legal or tax advice: licensing and food safety go to City of Hamilton Public Health and Licensing, insurance to your broker, and HST to your accountant.

---

## 6. Check list for you

- **Figures to check:** 13.4% office vacancy (CP24), $19.95 convention-centre price (HCC menu), 4°C / 60°C rule (O. Reg. 493/17), $17.95 minimum wage (Hicks Morley), and my $140,000 and $538-a-weekday estimates.
- **Assumptions to confirm:** the head baker limit, morning-and-lunch ordering, $25,000 as one-time spend, and staff able to fill three orders a day.
- **People who should see this:** your business partner, the head baker, and the manager of the pilot shop.
