---
id: motion-nabors-timing-scale
title: A timing scale works like a type scale: stay within about 70-700 ms, use ~200-300 ms as the workhorse, in milliseconds
domain: motion
tags: [motion-tokens, product, rachel-nabors, timing, tokens]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2028-10-30
sources: [https://www.youtube.com/watch?v=teQkx1SVq4g, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Rachel Nabors credits Amy Lee (Salesforce Lightning) with the idea of timing values that combine like a modular scale, generated like a type scale with ms in place of px. Notice range cited as about 70-700 ms; shorter for fades and color, longer for large moves; ms not seconds to match web animation APIs. Figures are her talk's, not a Salesforce spec.

**Use it:** Generate duration tokens from a ratio and cap the range; store in ms.
