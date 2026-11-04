---
id: c4d-team-render-total-time-sums-frames-and-first-node-frame-is-slow
title: Team Render reports the sum of all frame times, so a 3 h reading can be 1.5 h real; the node's first frame is slow because the scene is sent
domain: c4d
tags: [team render, render time, benchmark, speed, first frame, asset transfer, deep-read]
applies_to: Cinema 4D 2023 Team Render (2023)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=1Gtp3BjlTjY, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
In Team Render the Picture Viewer's total render time adds up each frame's time across machines; it is not a stopwatch [16:38-17:41]. His overnight job read 3 h on the combined machines, same as one 3090 Ti alone, yet finished in about half the wall time. Compare frames per machine, or run a stopwatch for an hour on one machine then an hour with both [17:41-18:13]. The first frame on the second machine is slow (it took about 20 s vs 4 s on the host in his tiny test) because all project data is transferred; later frames jump to about 1-3 s [15:37-16:38].

**Use it:** When logging farm speed-ups use wall-clock, not the summed render time, and exclude the first node frame from per-frame averages.
