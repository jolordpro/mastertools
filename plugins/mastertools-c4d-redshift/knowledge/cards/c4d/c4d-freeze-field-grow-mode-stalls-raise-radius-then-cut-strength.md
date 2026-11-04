---
id: c4d-freeze-field-grow-mode-stalls-raise-radius-then-cut-strength
title: A Freeze field in Grow mode with a random subfield on its radius stalls where the random value is low; raise the radius, then lower effect strength to slow it back down
domain: c4d
tags: [fields, freeze field, grow, random field, radius, effect strength, stall, deep-read]
applies_to: Cinema 4D 2022 (Maxon Ask the Trainer, Apr 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cCCgPVurWjQ, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Freeze layer set to Grow spreads a selection outward from a small spherical field [08:31-09:02]. With a Random field in its Radius subfield, growth stops partway: where the random output is 0% the radius collapses to zero and cannot reach the next clone, which sat 10 cm away in the demo [10:03-10:35].
Fixes shown: raise the freeze radius (a demo used 20), or change the random field's scale [10:35-11:06]. Trainer's habit: push the radius up, then counter the extra speed by dropping Effect Strength to about 50%; shape stays, growth slows [11:06-11:40].

**Use it:** If a Grow reveal freezes mid-way, treat it as a radius threshold problem first; lift radius, then tune speed with strength.
