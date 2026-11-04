---
id: lighting-rs-area-light-size-and-spread-for-falloff
title: In Redshift area lights, bigger size means more intensity, and Spread sets how soft the falloff is; shrink the light for a concentrated key
domain: lighting
tags: [redshift, area light, size, intensity, spread, falloff, key light, deep-read]
applies_to: Redshift area light, C4D
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=BlEM9iOzqMI, src:yt-transcripts, https://www.youtube.com/watch?v=RpiCCLHjlWQ]
feeds: [redshift, coach]
conflicts: none
---
Presenter's observation: scaling an area light down also changes how bright it reads, so size and intensity must be rebalanced together [04:52]. Spread at its minimum gives a completely sharp edge; a middle value is soft but pinpointed [05:24]. He shortened shadows that looked too long by moving the key higher and lowering intensity ("kissing" the subject) [07:06]. Check against the Redshift ledger at the gate.

**Use it:** when a key looks too hot or too long, change size, spread and height together, not intensity alone.
Transcript support: area light size changes intensity and shadow softness; Normalize Intensity removes the size effect; default intensity 100 too bright, about 10 used (https://www.youtube.com/watch?v=RpiCCLHjlWQ [41:21-42:28])
