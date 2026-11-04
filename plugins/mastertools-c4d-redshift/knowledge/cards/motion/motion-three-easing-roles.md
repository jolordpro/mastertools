---
id: motion-three-easing-roles
title: A starter easing palette is three custom curves: standard, enter (decelerate), exit (accelerate)
domain: motion
tags: [motion-tokens, product, val-head, easing]
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
Val Head (2023) notes most systems define three curves: a standard ease-in-out for whole on-screen moves, a decelerate for entrances, an accelerate for exits. Fluent, Spectrum and REI Cedar do this. Use own cubic-beziers, not CSS keywords.

**Use it:** Name roles by job (enter, exit, standard) and publish the cubic-bezier for each.
