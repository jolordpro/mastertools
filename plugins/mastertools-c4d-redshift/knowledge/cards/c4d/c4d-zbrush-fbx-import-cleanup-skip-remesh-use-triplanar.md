---
id: c4d-zbrush-fbx-import-cleanup-skip-remesh-use-triplanar
title: ZBrush FBX import: delete the useless subdivision surface objects and override tags, group, rotate, skip remeshing when only shading
domain: c4d
tags: [fbx, zbrush, import, cleanup, subdivision, triplanar, no uv, lionel, maxon, deep-read]
applies_to: C4D R26 with Redshift (2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=TonSU8Ljm5c, src:yt-transcripts]
feeds: [pipeline, coach]
conflicts: none
---
Lionel (Maxon trainer) imported the ZBrush model as FBX with default options and cleaned up: the Subdivision Surface objects did nothing because an override tag set editor subdivision to zero and the geometry had no clean quads for smoothing; he deleted them with Delete Without Children plus the override weight tags, grouped, and rotated 90 degrees with Shift [05:54-09:35].
He tried ZRemesher and it worked but was slow, and since the job was shading only, not unwrap, deform or animate, he skipped it [32:19-33:21]. With no UVs and bad topology he used triplanar mapping only [43:30-44:34].

**Use it:** pipeline: for a still on a sculpted hard-surface prop, strip generated subdivision, keep the mesh, map with triplanar.
