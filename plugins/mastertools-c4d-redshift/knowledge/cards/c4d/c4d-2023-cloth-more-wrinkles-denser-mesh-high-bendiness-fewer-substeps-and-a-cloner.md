---
id: c4d-2023-cloth-more-wrinkles-denser-mesh-high-bendiness-fewer-substeps-and-a-cloner
title: For detailed liquid-looking cloth: double the segments (200 by 275 versus 75 by 100), bendiness near 9999, substeps down (default 20 to 15) and iterations at 1; the accuracy settings actually stiffen cloth
domain: c4d
tags: [cloth, wrinkles, segments, bendiness, substeps, smoothing iterations, damping, cloner, collision passes, deep-read]
applies_to: Cinema 4D 2023 new simulation system, cloth (School of Motion, EJ, Oct 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dHQWVXWbsEM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
EJ [24:32-31:21]. Cloner: drop the Cloth object onto the Cloner to simulate nine planes at once; if they intersect, raise Collision passes in Project settings, Simulation, at some speed cost [25:03-26:06].
More wrinkles come from: denser segments (75 x 100 raised to 200 x 275), very high bendiness (9999), and fewer substeps, because more substeps, iterations and smoothing iterations make a stiffer cloth as a side effect; iterations and smoothing can only go down to 1 [27:10-28:44]. Jitter still means raise smoothing iterations [28:44]. Damping makes it fluid and underwater-like [29:46-30:17]. Final: Phong angle up, Cloth Surface and subdivisions on [30:17].

**Use it:** Pick the look first: stiffer and cleaner means more substeps; wrinkly and loose means fewer, with a dense mesh.
