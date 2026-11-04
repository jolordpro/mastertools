---
id: lighting-marks-unbiased-render-samples-only
title: Raoul Marks used an unbiased GPU renderer to avoid flicker and set noise by one number, samples, from a single test frame
domain: lighting
tags: [polish, raoul marks, octane, unbiased, flicker, samples, gi, semi-permanent]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.maxon.net/en/article/title-design-challenging-art, src:polish-roster]
feeds: [polish-coach]
conflicts: ledger
---
Marks says the old trade-off was speed against lighting accuracy. With biased GI he would render a sequence, return hours later and find flicker he had not seen in tests, then raise quality and restart. Octane is unbiased, so there is no flicker and no AA settings [§2]. His method: "There's really only one setting to be concerned with: samples." Render one image to a noise level you like, note the sample count, and set the entire sequence to that number [§3]. This is his Octane workflow; Redshift settings follow the redshift skill ledger.

**Use it:** For animation, judge noise on a representative frame and lock one quality number; test for flicker on a short range first.

Page spot: §2-3.
