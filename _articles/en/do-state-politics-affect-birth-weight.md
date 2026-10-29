---
ref: do-state-politics-affect-birth-weight
order: 4
title: 'Do state politics affect birth weight?'
github: true
image: /assets/images/card-state-politics.png
image_alt: 'A chart from the article'
description: 'I matched each state’s births with the party of its governor, year by year, and looked at what happened when the party changed.'
---

[Yori Lavi](https://www.linkedin.com/in/yorilavi/), someone I work with and trust, reviewed my work on US birth outcomes and suggested checking whether politics, and the social agendas that come with it, have anything to do with birth weight. It made me curious, so I took a look.

I matched each state’s births with the party of its governor, year by year, and looked at what happened when the party changed.

The first check was simple: for every state that switched, compare the last year under the old party to the first year under the new one. Average change, across 22 switches: −6.6 grams.

And the decline happened whichever way the switch went. Both directions, almost always down: 19 of the 22. That hinted that party wasn’t the cause: if it doesn’t matter which party you switch *to*, party probably isn’t what’s doing the work. But a hint is not a measurement.

Birth weight was falling everywhere across those nine years: nationally, from 3,267 to 3,242 grams. So a state that switched party and then declined hasn’t shown you anything yet. It’s a state doing what every state was doing.

Why birth weight was falling is a story of its own, and I told it in “[Babies are not smaller. They are arriving earlier.](/en/articles/babies-are-not-smaller/)”

So I compared each switching state with the states that didn’t switch, over the same years. Whatever both groups did together is the background. What’s left is the part that might belong to the switch. In statistics, this comparison is called difference-in-differences.

What’s left is −2.4 grams.

Two-thirds of the first number was the national decline, turning up in the switching states because it was turning up everywhere.

And those 2.4 grams aren’t clean either. Two standard significance tests disagree about them: one lands just under the conventional line (p=0.048), the other just over (p=0.068). A result that changes depending on which reasonable test you pick isn’t strong evidence in either direction.

So the answer is the uncomfortable one. Not “party affects birth weight.” Not “party doesn’t.” A small residual effect, roughly two grams, too uncertain to act on and too present to wave away.

And it leaves a question open. Twenty-two switches is a small number, and one year either side is short: if a governor’s policies reach birth weight at all, they would take longer than a year to reach a delivery room. Several years either side of each switch is the obvious next version, and the data supports it.

## The 22 switches

Change in average birth weight from the last year under the old party to the first year under the new one, in grams. Year is the first year under the new party. The fifth column is the change over the same two years in the states where the governor’s party stayed the same.

| State | Year | Switch | This state | States that did not switch | Difference |
|---|---|---|---|---|---|
| Missouri | 2017 | Democratic to Republican | −8.0 | −4.5 | −3.4 |
| New Hampshire | 2017 | Democratic to Republican | −19.6 | −4.5 | −15.1 |
| North Carolina | 2017 | Republican to Democratic | −7.7 | −4.5 | −3.1 |
| Vermont | 2017 | Democratic to Republican | −2.9 | −4.5 | +1.7 |
| West Virginia | 2017 | Democratic to Republican | +1.5 | −4.5 | +6.0 |
| New Jersey | 2018 | Republican to Democratic | +0.2 | −0.5 | +0.7 |
| Alaska | 2019 | Independent to Republican | −15.0 | −7.1 | −7.9 |
| Illinois | 2019 | Republican to Democratic | −4.7 | −7.1 | +2.4 |
| Kansas | 2019 | Republican to Democratic | −10.0 | −7.1 | −2.9 |
| Maine | 2019 | Republican to Democratic | −3.6 | −7.1 | +3.5 |
| Michigan | 2019 | Republican to Democratic | −14.1 | −7.1 | −7.0 |
| Nevada | 2019 | Republican to Democratic | −11.5 | −7.1 | −4.4 |
| New Mexico | 2019 | Republican to Democratic | −13.0 | −7.1 | −5.9 |
| Wisconsin | 2019 | Republican to Democratic | −5.5 | −7.1 | +1.6 |
| Kentucky | 2020 | Republican to Democratic | +7.2 | +1.3 | +5.9 |
| Montana | 2021 | Democratic to Republican | −3.8 | −5.9 | +2.1 |
| Virginia | 2022 | Democratic to Republican | −9.0 | −8.1 | −1.0 |
| Arizona | 2023 | Republican to Democratic | −1.1 | −0.4 | −0.7 |
| Maryland | 2023 | Republican to Democratic | −8.4 | −0.4 | −8.0 |
| Massachusetts | 2023 | Republican to Democratic | −1.2 | −0.4 | −0.8 |
| Nevada | 2023 | Democratic to Republican | −9.8 | −0.4 | −9.4 |
| Louisiana | 2024 | Democratic to Republican | −5.9 | +0.9 | −6.8 |
| Average of the 22 |  |  | −6.6 | −4.2 | −2.4 |

The notebook, with every number in this post, is on [GitHub](https://github.com/dorithkleinstein/us-birth-outcomes-2016-2024/tree/main/validation).
