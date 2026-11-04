---
id: motion-unreal-hex-stripe-built-in-c4d-alembic-or-material
title: Hex stripe animation came from C4D via Alembic, then was rebuilt as a procedural material with a repeat function
domain: motion
tags: [unreal, alembic, c4d, procedural material, frac, stripes, deep-read]
applies_to: Unreal Engine 4.27 (concepts carry to UE5)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bcL001ZFHBQ, src:yt-transcripts, https://www.youtube.com/watch?v=cut-ZBaB1b0, https://www.youtube.com/watch?v=TEM9BU-Fp0E]
feeds: []
conflicts: none
---
Core hexagon-stripe animations were authored in C4D and brought into Unreal as Alembic, which had become more stable [14:41-15:30]. A later version is only a material on a plane: a hexagon with a gradient from the centre, multiplied up, run through a repeat (Frac) node, clipped to black and white and used as a mask [15:30-16:19]. Sidhu likens a material to an After Effects comp with layers and precomps.

**Use it:** If a C4D pattern must run in an engine, try the procedural-mask route; Alembic is the fallback.
Transcript support: 2020 Unreal 4.25 import settings for C4D Alembic: start at frame 1, geometry cache, 3ds Max preset (https://www.youtube.com/watch?v=cut-ZBaB1b0 [05:05])
Transcript support: Cloth reached Unreal as a native geometry cache via Cineware, with no Alembic file (https://www.youtube.com/watch?v=TEM9BU-Fp0E [07:11-07:42])
