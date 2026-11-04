---
id: redshift-hwrt-off-for-ipr-on-for-final
title: Switching hardware ray tracing off can make IPR faster on some scenes; switch it back on for final frames
domain: redshift
tags: [hardware ray tracing, hwrt, ipr, optix rt, displacement, preparing hierarchy]
applies_to: Redshift on RTX cards (2023)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=le17-h6tUD0, src:yt-transcripts]
feeds: [redshift, CHECKS]
conflicts: none
---
Changing a tessellated or displaced object makes Redshift rebuild its ray-tracing hierarchy, which slows IPR; with the toggle off the scene came back sooner [32:12-33:14].
Greyscalegorilla does not claim it always helps, only 'sometimes', and says to turn it back on for the final frame [03:07] [34:17].

**Use it:** a check that compares IPR draft settings with the final preset should flag hardware ray tracing left off.
