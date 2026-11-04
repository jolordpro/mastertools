---
id: motion-apple-projection
title: Pick a gesture's end point by projecting its velocity with scroll deceleration, not by nearest position
domain: motion
tags: [motion-tokens, product, nathan-de-vries, gestures, momentum]
applies_to: any
status: V
confidence: high
decay: slow
read: 2026-10-30
recheck_by: 2028-10-30
sources: [https://developer.apple.com/videos/play/wwdc2018/803/, https://www.youtube.com/watch?v=gttSJA-kDmQ, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Nathan de Vries uses a FaceTime picture-in-picture example: choosing the nearest corner ignores velocity and forces long drags. Instead take release velocity plus the system scroll deceleration rate, compute an imaginary landing position, then retarget the spring to the nearest corner of that. Works for scale and rotation too. Reusing scroll deceleration borrows what people already know.

**Use it:** For flick-to-snap behaviors, specify the projection rule and the deceleration constant.
