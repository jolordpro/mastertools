---
id: lighting-octane-product-quick-settings-and-camera-focal-300-plus
title: For a flat product look, push the camera focal length to 300 mm or more; draft Octane at 2,000 samples, depth 8, GI clamp 1
domain: lighting
tags: [octane, product render, focal length, path tracing, samples, gi clamp, nikita kapustin, deep-read]
applies_to: Octane for Cinema 4D (2022)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=gMs_iu3cMoY, src:yt-transcripts, https://www.youtube.com/watch?v=8zCqKpeF5Uc, https://www.youtube.com/watch?v=mNcq8GD1mfI]
feeds: [[]]
conflicts: none
---
Kapustin raises focal length to about 300 mm (the original used 800) so the phone looks flat and nothing curves; 10 mm fish-eye or even a 35 mm standard view distorts the near edge against the back [02:40-03:45]. Draft settings [10:09]: path tracing instead of direct lighting, 2,000 samples instead of 16,000, diffuse depth 8, specular depth 8, GI clamp 1, adaptive sampling relaxed. Final run about 2,500 samples to a 16-bit PNG [40:05]. The camera is placed with the viewport on a separate view so the render camera does not move.

**Use it:** Remember the long-lens trick when a product frame looks bent, and note the draft versus final sample jump when budgeting.
Transcript support: GI clamp defaults to max; this creator sets it to 1 for faster, less firefly renders and pairs it with hot pixel removal. The existing lookdev-octane-blender-render-settings card uses GI clamp 10, so creators differ (1 vs 10). (https://www.youtube.com/watch?v=8zCqKpeF5Uc [03:10-04:48])
Transcript support: Focal length: a wide view puts the nose of an F1 car huge and the cockpit far away; 200 mm gives straight proportions, and Kapustin settles on 75 mm to keep some depth. (https://www.youtube.com/watch?v=mNcq8GD1mfI [02:10-03:44])
