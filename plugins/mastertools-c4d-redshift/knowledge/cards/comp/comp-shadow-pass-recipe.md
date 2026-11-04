---
id: comp-shadow-pass-recipe
title: Shadow pass recipe: multiply Shadow by the Diffuse Filter, add into the diffuse total, then dial shadows back with opacity
domain: comp
tags: [shadow pass, diffuse filter, diffuse raw, vfx match, redshift]
applies_to: Redshift AOVs, After Effects
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts, https://www.youtube.com/watch?v=5hQKHD8fSs8]
feeds: [comp-fix planner]
conflicts: none
---
It needs the raw and filter diffuse passes [15:00]. Shadow x filter = shadow total; adding it removes shadow from the whole image, so raise it with a layer opacity; at 100% it is no shadow, which he calls backwards [1:12:08-1:14:15]. Exposure and Gamma shape it further. Useful for matching live-action shadows, rarely for motion design [1:15:16]. A viewer says Redshift shadows are harder than the standard renderer; he agrees [1:28:59]. Captions are partly garbled here.

**Use it:** Treat as a VFX-only tool; verify on a real shot before the coach teaches it.
Transcript support: Shadows pass is a mask (white where shadow) on a Levels adjustment layer, not an Add layer (https://www.youtube.com/watch?v=5hQKHD8fSs8 [05:44-06:46])
