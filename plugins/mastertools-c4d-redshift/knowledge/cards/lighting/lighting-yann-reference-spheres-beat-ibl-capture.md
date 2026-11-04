---
id: lighting-yann-reference-spheres-beat-ibl-capture
title: On set, matching the chrome and gray reference spheres matters more than a perfect HDRI, because bright IBL values get replaced by lights anyway
domain: lighting
tags: [[yann dupont, cg supervisor, zoic, ibl, hdri, chrome ball, gray ball, reference spheres, on-set, arvid schneider], deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=gjgAZ0x29ag, src:yt-transcripts]
feeds: [lighting, redshift]
conflicts: none
---
Yann Dupont (CG supervisor at Zoic, ex-ILM): if only one thing gets effort on set it should be the reference spheres, not the IBL capture [08:21-09:55]. Reason: a plain 360 JPEG often gives enough, and in lighting, values above 1 in an IBL, which are the real light sources, are erased and replaced by directional lights anyway [08:52-09:22]. He judges lookdev and lighting by comparing against the spheres. Host Arvid Schneider tells of a sphere pole held with the sun three-quarters behind and a camera at 40 degrees to the shoot camera, making the spheres unreliable; he shot through a test camera rotated 45 degrees to match [06:49-07:50]. Yann prefers the term IBL over HDRI to avoid confusion with Photoshop "HDR" blending [10:25].

**Use it:** matches our HDRI health check: judge a dome by whether a grey and a chrome sphere match the plate, and replace clipped suns with a light.
