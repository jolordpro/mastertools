---
id: motion-wcag-three-baselines
title: Three baseline motion accessibility rules to write into a system: pause after 5 s, no flashing over 3x per second, honor reduced motion
domain: motion
tags: [motion-tokens, product, val-head, accessibility]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2028-10-30
sources: [https://www.youtube.com/watch?v=jq6WYJ4Mra4, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Val Head (2023) summarises the WCAG baseline: give pause/play for motion lasting over 5 seconds (loaders excluded), do not flash more than three times a second, respect the reduced-motion setting. Reduced version swaps travel and scale for opacity or cross-fades and keeps feedback and loaders. Intuit's QuickBooks section is her best example.

**Use it:** Put these three as checkable lines in a motion spec, plus what is kept in reduced mode.
