---
id: lookdev-use-the-renderers-own-displacement-with-a-one-segment-plane
title: Terrain from a height map is cheaper and better when the render engine displaces a one-segment plane than when the C4D displacer does
domain: lookdev
tags: [displacement, height map, 8k texture, octane, vram, io studios, deep-read]
applies_to: C4D Octane
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=kb1q3hi-NEs, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
IO Studios [0:35-2:45]: the plane has 1 by 1 segments because the renderer's own displacement (Octane) generates the geometry from the height map, which he says renders faster and looks better than the Cinema 4D displacer. Level of detail 4k was used for speed on a tutorial, 8k would be best for a final; amount about 100. The textures are 8K and can need lots of RAM, so reduce resolution in an image editor if the machine cannot load them; it takes a moment to load into memory before the render appears [2:09]. Octane-only controls, but the principle (renderer-side displacement; matching map resolution to need) transfers; check Redshift's own displacement and tessellation settings.

**Use it:** Flag 8K textures and heavy displacement maps in scene checks, and prefer renderer-side displacement over modelled subdivision.
