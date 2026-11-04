---
id: redshift-texture-displacement-bake-resolution
title: Texture displacement bakes at 1K by default; raise it for detail, and it never exceeds the source texture size
domain: redshift
tags: [texture displacement, tessellation free, bake resolution, vram, displacement]
applies_to: Redshift 2026.2 (C4D 2026.1)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ZAom6DvSi3s, src:yt-transcripts, https://www.youtube.com/watch?v=Xh8A767yA1U, https://help.maxon.net/r3d/cinema/en-us/Content/html/Tessellation+And+Displacement.html]
feeds: [redshift, CHECKS]
conflicts: none
---
New tessellation-free displacement: Render Settings > Advanced > Globals > Displacement offers Vertex (legacy) or Texture [40:55]. Bake resolution default 1024 up to 16K; higher means more detail, more VRAM and render time [42:37].
Smart bake: a 4K texture with an 8K setting is cut to 4K [45:01]. Override per object with the Redshift object tag [43:26]. A single 1x1-segment plane displaced with no tag.

**Use it:** scene check: list bake resolution versus texture size; warn if bake is above source.
Transcript support: Adds default bake 1024 x 1024, options 64 x 64 to 16K, per-object tag override, smart bake drops 8K to the 4K source. (https://www.youtube.com/watch?v=Xh8A767yA1U [42:25-45:32])
Maxon check (2026-10-31): Maxon docs: Bake Resolution runs 64 to 16k. It is capped at the source texture size only with Smart Bake on; procedural textures use the full value. A 1024 default is not stated. (https://help.maxon.net/r3d/cinema/en-us/Content/html/Tessellation+And+Displacement.html)
