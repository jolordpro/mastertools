---
id: pipeline-nightly-regression-renders-to-catch-drift
title: Render a fixed set of scenes automatically each night and compare with last week to catch silent look changes
domain: pipeline
tags: [render farm, nightly render, regression, shotgun, games cinematics, a cup of joe, pipeline drift, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=eb0QFXD3AaA, src:yt-transcripts]
feeds: [CHECKS, shakedown]
conflicts: none
---
A former wrangler now in games (name not clear in captions) describes a small automated farm that renders cinematics every night so the team can glance through them in Shotgun and see what changed, for example all night levels suddenly darker [16:01].
Compare to last week; regular renders track where the pipeline and content are over time [16:32].
The same idea runs distributed compiles and effects simulation on spare machines [16:32, 17:04].
A strong farm can empower a studio beyond any single artist [15:28].

**Use it:** Keep a small reference set of scenes and re-render it on every platform or version change, comparing output to the last known good.
