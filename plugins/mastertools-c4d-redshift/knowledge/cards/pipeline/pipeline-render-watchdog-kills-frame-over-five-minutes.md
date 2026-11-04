---
id: pipeline-render-watchdog-kills-frame-over-five-minutes
title: DillonGoo's render manager kills and restarts a frame that runs past a timeout (about five minutes), after overnight queues stalled on frame three
domain: pipeline
tags: [cody winchester, dylan goo, dillongoo studios, blender conference 2024, render farm, timeout, frozen render, watchdog, flamenco, overnight, deep-read]
applies_to: Blender, Python/Rust tool
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aDsyNfISVLA, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
Winchester [11:20-12:53]: they used to queue 30 shots, sleep, and find that only two had rendered because the third froze. A Rust module now checks elapsed time per frame; past a threshold, about five minutes, it kills the frame and restarts, then carries on.
The manager also writes render status to their tracker (Coda), supports selective render passes (backgrounds first, since they finish before character animation), and a worker mode on teammates' machines was in progress.

**Use it:** estimator and farm advice: set a per-frame time-out well above the normal frame time and auto-retry, so stalls cost minutes, not a night.
