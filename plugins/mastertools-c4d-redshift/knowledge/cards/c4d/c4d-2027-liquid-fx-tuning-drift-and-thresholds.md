---
id: c4d-2027-liquid-fx-tuning-drift-and-thresholds
title: Liquid FX particles follow the water through 'drift', so wind needs huge values until drift is lowered
domain: c4d
tags: [liquid fx, drift, wind, buoyancy, initial age, threshold, foam, bubbles]
applies_to: C4D 2027.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
[02:03:00] Wind of 5 or 500 did nothing to the bubbles, 55,000 finally pushed them. Cutting drift to about 17% made them fly backwards fast [02:03:34].
Initial age threshold stops births for the first 15 frames; lower it to see splash pops [02:05:06]. Higher bubble buoyancy (10 times) makes them crest and splash [02:07:11]. More foam surface offset makes fluffier foam.
Resolution near 500% is a good default; going lower gives far fewer particles.

**Use it:** when a user complains FX particles ignore forces, tell them to lower drift first.
