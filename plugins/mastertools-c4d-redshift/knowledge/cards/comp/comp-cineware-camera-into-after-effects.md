---
id: comp-cineware-camera-into-after-effects
title: Cineware can recreate a C4D camera move inside After Effects without re-rendering, handling the coordinate difference for you
domain: comp
tags: [cineware, after effects, camera, c4d, 3d data, compositing project file, coordinate system]
applies_to: Cinema 4D / After Effects with Cineware (2025)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=1oUhyg3LwoM, src:yt-transcripts]
feeds: [comp planner]
conflicts: none
---
Set Angle (Maxon NAB 2025): save from C4D with Save for Compositing Project File and Include 3D Data [13:01]; the AE Cineware layer then lists the scene camera or an AE camera and rebuilds the animation as keyframes [24:39 to 26:13].
The two apps use different coordinate systems and Cineware converts automatically [25:11].
Put the C4D layer under 2D layers; a flat layer, a 3D phone and a C4D scene share one camera [26:13].

**Use it:** use for fast 2D plus 3D comps and ad specs, and for exporting matched cameras to flat layers.
