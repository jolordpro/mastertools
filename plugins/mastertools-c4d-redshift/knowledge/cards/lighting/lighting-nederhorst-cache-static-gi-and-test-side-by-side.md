---
id: lighting-nederhorst-cache-static-gi-and-test-side-by-side
title: Cache GI on a static environment and prove it with a five-frame side-by-side before accepting the saving
domain: lighting
tags: [rob nederhorst, radiance cache, gi, irradiance cache, static environment, render time, v-ray, draft first, deep-read]
applies_to: V-Ray (principle applies to any cached-GI renderer)
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=qlNn8Gim3qU, src:yt-transcripts]
feeds: []
conflicts: none
---
On a small-team commercial (about 30 render machines, PAL 720x576 at 25 fps), a supervisor radiance-cached the environment in V-Ray and saved large render time [40:09].
Nederhorst's points: GI cached once is not recalculated each frame, is noise-free and interpolated, and loses a little accuracy that does not matter when objects move through the scene [41:13].
His test: render five frames side by side with and without the cache; if you cannot tell them apart, ship the cached version [41:43].
His wider rule: do not render everything at full resolution on the first take [40:09].
Equivalent in Redshift terms: irradiance cache for static cameras and scenes (not stated by the speaker).

**Use it:** When a shot has a static environment, recommend a cached-GI render and require a five-frame A/B before the cheaper setting is used for the full range.
