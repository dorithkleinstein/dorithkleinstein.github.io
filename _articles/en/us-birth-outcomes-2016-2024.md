---
ref: us-birth-outcomes-2016-2024
order: 2
title: 'The averages moved. The structure did not.'
looker: true
github: true
description: 'Between 2016 and 2024, average birth weight in the United States fell by 25 grams, from 3,267 to 3,242.'
---

Between 2016 and 2024, average birth weight in the United States fell by 25 grams, from 3,267 to 3,242.

That is the least interesting thing in this data.

Twenty-five grams is almost nothing set against a healthy birth weight. What makes it worth a second look isn't the size of the fall, it's how evenly it happened: every region, every racial group, every education level, all tilting the same way over the nine years.

And underneath that small, even movement, almost nothing else moved at all. That turned out to be the finding.

## What this is built on

Nine years of [CDC WONDER](https://wonder.cdc.gov/natality.html) natality data: every registered birth in all fifty states and the District of Columbia, 2016 through 2024. Around 33 million births. Processed through dbt into BigQuery and visualised in Looker Studio. The full interactive report is linked at the end, and you can filter it yourself.

CDC WONDER records what happened at birth: weight, gestational age, delivery method, whether a birth was a multiple, when prenatal care began, and the mother's age, race and education. What it does not record shapes everything below, and I come back to it at the end rather than hedging every paragraph.

## The decline, and how even it is

The fall is not smooth, and the shape is not the one I expected. 2020, the pandemic year, actually ticked up very slightly. The declines came before it and after it: a steady drift down from 2016 to 2019, then the two largest single-year falls of the whole series in 2021 and 2022. Since 2022 it has been flat, sitting at the bottom rather than climbing back out.

A national average falling 25 grams over nine years could be a lot of things. What narrows it is that the fall shows up in every dimension the dataset can cut by. Regional splits, racial groups, education levels: all of them tilt the same way. Whatever is behind it isn't confined to one community or one crisis.

That's the backdrop. The rest of this is about the things that sat still while it happened.

## Education: the middle behaves, the ends do not

I expected the education gradient to run cleanly from bottom to top. It doesn't. It breaks at both ends.

Through the middle of the range it does exactly what you would predict: as education rises from Some High School through Bachelor's, average birth weight rises with it, peaking at Bachelor's degree.

Then it reverses. Mothers with a Master's degree and mothers with a Doctorate or professional degree both average lower birth weights than mothers with a Bachelor's, consistently, in all nine years. Doctoral mothers tend to be older, with higher rates of IVF, multiple births and elective early delivery. Multiple births are recorded here, which is a cut I have not made. IVF and elective delivery are not recorded at all.

It breaks at the other end too, and harder than I first thought. Mothers with an eighth-grade education or less average higher birth weights than high-school graduates, in every one of the nine years, and higher than mothers with some college credit in eight of them. My best guess is that, like the older mothers at the top, these very young mothers are reached differently by healthcare and family support. But the reasons are not in this data.

Two unexpected reversals, one gradient. The middle behaves. The ends do not, and they have not in any of the nine years.

## Race: a gap that has not moved

Black mothers in the US average birth weights roughly 230 grams lower than White mothers, about 7 percent.

Across nine years, that gap has not narrowed meaningfully. The two lines move roughly in parallel. This isn't the residue of one bad period that the data is slowly working off; it is a difference that nine years of everything else changing did not touch.

It does not disappear in well-resourced places, either. New York, with some of the best-funded healthcare in the country, shows a 187-gram disparity across the nine years, and it is wider in 2024 than it was in 2016. The gap follows the population rather than the provision.

This dataset shows measurements at birth, not causes. It cannot show the documented pathways through which systemic inequity affects maternal health. What it does is make the pattern visible at a scale that is hard to look away from.

## Region: the South was already falling

The South's average birth weight fell 11 grams between 2016 and 2019. Then COVID arrived, and it fell another 4.

The point is the first number, not the second.

Every region declined in 2021. That much is visible everywhere in this data. But the South had been falling for three years before the pandemic reached it. By the time the crisis arrived, it had further to fall and less margin to lose.

When a decline predates the crisis, the crisis isn't the explanation. This data doesn't say what is. It just makes the timing impossible to miss.

What happened afterwards is not what I assumed. No region recovered. Between 2021 and 2024 the West fell another 13 grams and the Northeast another 9, while the South, already lowest, fell only 3.

So the one structural thing that did move is the regional gap, and it narrowed: 44 grams between the Northeast and the South in 2016, 40 by 2024. It closed because the other regions came down faster, not because the South came up. That is convergence, and it is the wrong kind.

## The rankings: frozen, end to end

Ranking all 51 jurisdictions on average birth weight each year produces the sharpest version of the pattern.

Nine states never leave the top ten in nine years: Alaska, New Hampshire, Vermont, Maine, Minnesota, Iowa, North Dakota, Oregon and Washington. Alaska is first in every single one. Nine never leave the bottom ten: Nevada, the District of Columbia, Alabama, Georgia, Wyoming, Colorado, New Mexico, Louisiana and Mississippi. Mississippi is 51st in all nine years. The two lists do not share a single name, and nothing has ever crossed between them.

I expected the middle to churn. It doesn't. Only three states move more than eight places across the whole period, and the widest swing in the table is thirteen.

The bottom ten is also not one region. It runs from Mississippi and Alabama to Colorado and Wyoming.

So it isn't that the ends are frozen and the middle moves. Almost nothing moves.

## What this data cannot tell you

Everything above is a description, not an explanation, and the distinction matters more than usual here.

CDC WONDER captures what was recorded at birth. It has nothing to say about income, insurance status, or distance to a hospital. It does carry things I did not use: delivery method, whether a birth was a multiple, and the month prenatal care began. None of those is a cause on its own, and none of them is in the analysis above. Anyone offering you a cause from this dataset alone is going beyond what it contains. Including me, which is why I have not.

What a dataset this size is genuinely good at is establishing that something is real, stable, and worth the cost of investigating properly.

## What I take from it

I started by asking whether US birth outcomes were getting worse. The answer is yes: slightly, and remarkably evenly. Which turned out to be the least useful question I could have asked.

The better question was what stayed still. A 230-gram gap that nine years did not touch. Nine states that never left the bottom ten and nine that never left the top. Two reversals at the ends of the education range that hold in every single year without exception.

Those are the things a dataset this large is actually good at showing: not movement, but the absence of it. And knowing precisely what did not change is a much sharper place to start than knowing that something got slightly worse.

## The report

The full interactive version, filterable by state, region, race and education, is at [US Birth Outcomes 2016-2024](https://datastudio.google.com/reporting/67893ee7-9da4-4c9b-ab32-6f7903caed08).

Built with CDC WONDER natality data, dbt, BigQuery and Looker Studio.

*First published on* [*LinkedIn*](https://www.linkedin.com/pulse/averages-moved-structure-did-dorith-kleinstein-zjamf) *on 1 September 2026 and corrected on 10 September 2026.*
