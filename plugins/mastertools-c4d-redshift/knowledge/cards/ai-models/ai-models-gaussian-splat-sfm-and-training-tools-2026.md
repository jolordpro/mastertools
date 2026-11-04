---
id: ai-models-gaussian-splat-sfm-and-training-tools-2026
title: Splat pipeline steps and tools (2026): structure-from-motion (COLMAP, PyCuSfM, RealityScan, Metashape) then training (fVDB, 3DGRUT, gsplat, Postshot, Nerfstudio)
domain: ai-models
tags: [gaussian splatting, structure from motion, colmap, realityscan, metashape, fvdb, 3dgrut, gsplat, postshot, nerfstudio, licenses, deep-read]
applies_to: 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=KZqv3Z5rRg8, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Michael Rubloff (radiancefields.com). Order: capture images, run structure from motion to get camera poses, then train [10:35]. SfM options: COLMAP (permissive, the base most tools build on); NVIDIA PyCuSfM (CUDA, Apache 2, much faster, commercial use OK); RealityScan (Epic, formerly RealityCapture, free under $1M annual revenue); Agisoft Metashape (paid; Standard exports COLMAP format, Pro adds scripting and masking) [15:30] [15:48] [16:19] [16:49].
Local training: NVIDIA fVDB and its reality-capture module (Apache 2, fast, scalable); 3DGRUT (ray tracing plus the unscented transform, Apache 2); gsplat from the Nerfstudio group; later he names Postshot (closed), Nerfstudio and Lichtfeld Studio [17:35] [18:25] [19:27] [1:16:09]. For 10,000+ images: drone or 360 capture, then fVDB or the unscented-transform tools; sharp frames and parallax let it scale [1:14:34] [1:15:06] [1:16:09].
The unscented transform removes the pinhole-camera assumption so fisheye and robotics lenses work [25:47].
Licences and names are as spoken in auto-captions; confirm before use.

**Use it:** Starting list for any splat or scene-capture task; check licence per tool. Not a Redshift item, but useful for backgrounds and previs.
