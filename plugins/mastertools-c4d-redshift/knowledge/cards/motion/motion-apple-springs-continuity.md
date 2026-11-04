---
id: motion-apple-springs-continuity
title: Springs are the only common curve that keeps position and velocity continuous from rest, from a gesture hand-off and when retargeted
domain: motion
tags: [motion-tokens, product, jacob-apple-springs, springs, continuity]
applies_to: any
status: V
confidence: high
decay: slow
read: 2026-10-30
recheck_by: 2028-10-30
sources: [https://developer.apple.com/videos/play/wwdc2023/10158/, https://www.youtube.com/watch?v=HaZ2jw9rx9M, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Apple's WWDC23 argument: ease-in-out has no way to take an initial velocity, so a thrown knob jerks to a halt; a spring picks up where the gesture ended and, if retargeted mid-flight, uses current velocity. Linear suits only things like spinners. Different properties may finish at different times, and that is expected.

**Use it:** Use springs wherever a gesture can end mid-motion or a target can change.
