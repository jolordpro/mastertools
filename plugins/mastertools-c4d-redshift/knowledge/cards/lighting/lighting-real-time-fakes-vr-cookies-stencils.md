---
id: lighting-real-time-fakes-vr-cookies-stencils
title: When real-time budget forbids baked light, fake it: cookies for shadows, emissive stencils for light cones, distance and angle fades
domain: lighting
tags: [[nora shramek, vr, real-time, cookies, spherical harmonics, emissive, performance, shipping, insomniac], deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=r2PXd6l7kBg, src:yt-transcripts]
feeds: [lighting]
conflicts: none
---
Nora Shramek on a VR game with no baked lighting [20:44-23:52]. Spherical harmonics bake is good for indirect but bad for direct light, giving blobs and no light shaping [21:46]. She made emissive stencils shaped like light cones on walls, faded lights by distance and by angle when off camera, and used cookies where shadow casting was unaffordable [22:19-23:20]. She says a portfolio piece can do anything while shipping on Xbox One needs cheaper tricks, and you must understand what engineers built to avoid breaking it [23:23-24:22]. VR target was 90 fps per eye [21:16].

**Use it:** transfers to light-count and render-budget advice: fake the look cheaply where the audience cannot tell, keep the quality bar.
