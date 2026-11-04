---
id: motion-perry-engine-switch
title: Motion picks the best engine per animation: hardware-accelerated WAAPI when possible, JS otherwise
domain: motion
tags: [motion-tokens, product, matt-perry, tooling, performance]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=r6oXsC1gGHc, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Matt Perry (Syntax, 2024-11-29): animations that can run off the main thread (opacity, filter, clip-path, transform) use the browser's Web Animations API; features it lacks (e.g. repeat delay) fall back to a JS engine; scroll uses scroll timeline when supported. He also wants adaptive switching-off of animation classes on weak devices, and says to measure with tools, not rules.

**Use it:** Specs can say which properties are cheap to animate and what the fallback is.
