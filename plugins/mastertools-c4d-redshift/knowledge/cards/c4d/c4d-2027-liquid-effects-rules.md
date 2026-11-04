---
id: c4d-2027-liquid-effects-rules
title: C4D 2027 liquid effects make bubbles, spray and foam from neighbour counts; the emitter has a resolution percentage and age and speed thresholds
domain: c4d
tags: [liquid, foam, spray, bubbles, simulation, emitter, modifier, thresholds]
applies_to: Cinema 4D 2027.0
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=FmaKhqSITFQ, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
Two objects: Liquid Effects Modifier (turns existing particles into spray, foam, bubbles) and Liquid Effects Emitter (reproduces extra particles from a source group). Each makes three new particle groups [17:11-19:46].
Bubbles are particles surrounded by liquid, spray has few neighbours, and both become foam at the surface; the neighbour thresholds live in the simulation liquid settings [20:18-21:53].
Properties: foam drift and surface offset, bubble drift and buoyancy, lifetime decay [21:53-23:55]. Emitter: resolution percent (500 down to 100 for a slow machine), spread, age threshold (start at frame 15), speed threshold; trapped air and wave crest drive amount [26:30-29:37].

**Use it:** the coach tells users to keep emitter resolution low until the cache is final, and the estimator expects liquid scenes to be heavy.
