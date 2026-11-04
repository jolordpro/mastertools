---
id: c4d-octane-render-particles-with-sticks-and-rocks-weighted-by-duplicates-not-spheres
title: Render advected particles as long thin cubes and rocks, weight the rare big ones by duplicating the small ones, and watch Octane flicker with several particle objects in one object tag
domain: c4d
tags: [octane, particle objects, cubes, rocks, instances, flicker, lighting, area light, particle render, deep-read]
applies_to: Octane in Cinema 4D 2025 (Sketchy Visuals, uploaded Dec 2025)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vrE2wrqq0TM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Sketchy Visuals (Octane, not Redshift; his comment says Redshift did not flicker, unverified) [47:18-54:00]. Spheres look boring; use cubes, platonics, rocks or leaves. Long thin cubes (stretched on Y) catch and bounce light and change the whole read from a distance [48:49-49:21]. In Octane at that time, scale variation did not hold in animation, so he adds many scaled duplicates; the more small copies against one big one, the rarer the big one (two objects is 50/50; many copies approach 5/95), and a metal material on the rare one gives sparkle [52:27-53:29]. Putting more than one particle object in an Octane object tag flickered between objects in the then-current build [24:31].
Lighting: dark environment, camera at 200 mm aimed straight down, one area light above, stretch it to cover the particle bed; duplicate the visible environment so background black and shadow grey are separate; ACES tone mapping with vignette; no HDRI needed [47:18-49:21; 50:55-51:56].

**Use it:** For particle shots, vary the particle shape before spending hours on the sim; test any multi-object particle tag for flicker in the exact renderer build.
