---
id: motion-hernan-curve-conversion
title: The hardest part of Bodymovin was converting After Effects influence/speed curves to Bezier easing
domain: motion
tags: [motion-tokens, product, hernan-torrisi, tooling, easing]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=rdwi-90Y8Do, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Hernan Torrisi (2021 interview) names the interpolation conversion as the worst roadblock, solved with outside help on the maths. His method: support a subset of After Effects that real-time playback can match, start with a square, and add a report of unsupported features to the exporter.

**Use it:** Treat easing translation between tools as its own spec item, and publish the unsupported list.
