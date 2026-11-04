---
id: c4d-pyro-2023-1-voxel-size-smoothing-dissipation-and-caching-before-render
title: C4D 2023.1 Pyro voxel size starts at 5, drop to 3 then 2; smooth density, shorten dissipation and cache the timeline before rendering
domain: c4d
tags: [pyro, cinema-4d-2023, voxel, cache, vram, simulation, deep-read]
applies_to: Cinema 4D 2023.1 Pyro with Redshift
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=TLlITrj5A_4, src:yt-transcripts]
feeds: [coach, estimator]
conflicts: none
---
Effectatron, 2022 [05:42-18:38].
- Voxel size is a 3D pixel. Default 5; blocky look means lower it, but lower is much slower. He sets tag (object) voxel size and Pyro voxel size to match; worked at 3 for tests and 2 for the final [05:42-07:48, 16:04].
- Density smooth factor to max removes chunky blocks in the smoke [15:33].
- Dissipation controls how long things last; he turned it down because the shot only needed 24 frames, noting calc time rises as nothing disappears [14:31-15:01].
- Cache the scene before render: bakes the sim, frees GPU space, makes scrubbing smooth. Cache only the needed 24 frames, not the 240 timeline [17:05-18:07].
- On caching a "maximum VRAM allocated" and "determinism not guaranteed" notice appeared late in the run; he says accept it, or back off the settings if it happens early [18:07].
- Save often; Pyro can crash [16:04].

**Use it:** A Pyro budget order: test at voxel 3, finish at 2, shorten the frame range, cache, then render.
