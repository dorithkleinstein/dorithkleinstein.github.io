---
ref: why-are-the-babies-of-mothers-with-a-doctorate-lighter
order: 5
title: 'Why are the babies of mothers with a Doctorate lighter?'
github: true
description: 'Across more than 33 million US births from 2016 to 2024, average birth weight rises with the mother’s education, up to a Bachelor’s degree.'
---

Across more than 33 million US births from 2016 to 2024, average birth weight rises with the mother’s education, up to a Bachelor’s degree. Then it drops. Babies of mothers with a Master’s degree are 8 grams lighter on average than babies of mothers with a Bachelor’s. Babies of mothers with a Doctorate or a professional degree, such as a degree in medicine or law, are 31 grams lighter than babies of mothers with a Bachelor’s. Those 31 grams, between Doctorate and Bachelor’s mothers, are the gap this piece is about.

Age looks like the answer. Mothers with higher degrees have their children later, and birth weight falls for older mothers. So age is where I started, and I tested four other explanations the same way: twins, the state the mother lives in, the timing of the birth, and the mix of mothers. For each one, I compared Doctorate and Bachelor’s mothers who are alike in one thing, for example the same age, and looked at how much of the 31-gram gap was left.

**Twins.** Twins and triplets are much lighter than single babies, and mothers with higher degrees have slightly more of them: 3.9 percent of births against 3.6. Leaving them out takes about 2 grams off the gap. Twins would blur every other comparison, so from here on I looked at single births only.

**Age.** Mothers with a Doctorate are about two and a half years older on average than mothers with a Bachelor’s. But when I compare mothers in the same age group, the gap is still there. Among mothers aged 30 to 34, the largest group, it is 40 grams. Comparing mothers of the same ages takes about 1 gram off the gap.

**State.** Comparing mothers of the same age in the same state changes nothing.

**Timing.** In “[Babies are not smaller. They are arriving earlier.](/en/articles/babies-are-not-smaller/)” the national fall in birth weight turned out to be about timing: babies born earlier, not smaller. So I checked whether the babies of mothers with a Doctorate are simply born earlier. They are not. The three groups are born at almost the same week of pregnancy, on average less than an hour apart. And at the same week, the babies of mothers with a Doctorate are still about 30 grams lighter. Here it is size, not timing.

**The mix of mothers.** The racial mix of mothers differs a lot between education levels. Average birth weight also differs between the race groups that CDC reports. So two education levels with a different mix of mothers have different averages for that reason alone. When I compare mothers of the same race and the same age, the Master’s gap disappears, and the Doctorate gap goes from 28 grams to 18. This is about who is in each of the groups I am comparing. It is not a finding about the babies of any group.

After testing all five, 18 grams are left unexplained, and that is small: about half of one percent of a birth weight.

So the gap does not go away, and it is small. It is not age, it is not twins, it is not timing and it is not where the mothers live. About a third of it is the mix of mothers. What the rest is, this data does not say. The database I used, CDC WONDER’s Natality 2007-2024, records the mother’s education, age, race and state. It does not record income, occupation or how a pregnancy began, so I cannot test those.

The full data is shown in the following two tables.

## Where the Doctorate gap goes

Difference in average birth weight from mothers with a Bachelor’s degree, in grams, after each comparison, and how much of the gap each comparison accounts for. From the third row down, the Bachelor’s average is adjusted to the Doctorate mothers’ mix: of ages, of weeks of pregnancy, of ages and states, then of ages and races. The row for the same week of pregnancy comes from a separate extract that leaves out births with an unknown week, so its starting gap is 29.3 grams, not 29.4.

| Step | Bachelor’s average | Doctorate average | Doctorate gap from Bachelor’s | Accounted for |
|---|---|---|---|---|
| As measured, all births | 3,319.2 | 3,287.9 | −31.3 |  |
| Single births only | 3,353.6 | 3,324.2 | −29.4 | Twins: 1.9 |
| Single births, same age | 3,352.6 | 3,324.2 | −28.4 | Age: 1.0 |
| Single births, same age and same state | 3,353.9 | 3,324.3 | −29.6 | State: none |
| Single births, same week of pregnancy | 3,354.2 | 3,323.9 | −30.3 | Timing: none |
| Single births, same age and same race | 3,342.4 | 3,324.2 | −18.2 | Mix of mothers: 10.2 |
| Not explained |  |  | −18.2 |  |

## Inside each age group

Single births, average birth weight in grams by the mother’s age group and education. Read across any row: the Doctorate average is below the Bachelor’s average in every age group, and the difference is largest where most of the births are.

| Age of mother | Bachelor’s | Master’s | Doctorate | Doctorate minus Bachelor’s | Doctorate births |
|---|---|---|---|---|---|
| 20-24 | 3,306 | 3,304 | 3,282 | −23.5 | 2,283 |
| 25-29 | 3,354 | 3,342 | 3,323 | −31.0 | 103,133 |
| 30-34 | 3,369 | 3,359 | 3,329 | −40.4 | 421,687 |
| 35-39 | 3,349 | 3,352 | 3,331 | −17.8 | 325,471 |
| 40-44 | 3,287 | 3,293 | 3,284 | −3.3 | 70,544 |
| 45-49 | 3,197 | 3,201 | 3,182 | −15.2 | 5,892 |

Source: CDC WONDER Natality 2007-2024, years 2016 to 2024 pooled. Cells with fewer than 25 births are left out. Mothers aged under 20 and aged 50 or over are not shown: very few of them hold these degrees.

The notebook, with every number in this post, is on [GitHub](https://github.com/dorithkleinstein/us-birth-outcomes-2016-2024/blob/main/validation/Education%20Dip%20-%20Twins%2C%20Age%2C%20State%2C%20Race.ipynb).
