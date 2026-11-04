---
id: pipeline-blender-farm-split-layers-into-scenes-and-test-three-frames
title: Blender-to-farm workflow: mirror folders, split layers into scenes with indirect-only, set samples per scene, test first/middle/last frame, then run the full job
domain: pipeline
tags: [blender, cycles, fox render farm, render farm, view layers, indirect only, holdout, openexr, to animate, vlad, deep-read]
applies_to: Blender 4.3 Cycles, Fox Render Farm (2025)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=t32M1_7u_HA, src:yt-transcripts, https://www.youtube.com/watch?v=RCCaQmwxNB4]
feeds: [shakedown, estimator]
conflicts: none
---
Vlad (technical director, To Animate) [01:03-09:56]: upload assets with the local directory structure kept so paths resolve on the farm. Split the shot into separate scenes per layer (background, character, hero object); in each scene put the other collections on Indirect Only (they still bounce light) or Holdout (acts as a mask) [02:35-03:06]. Each scene has its own settings, so check all are set to GPU; he used 2,000 samples on the busy layer and 1,000 on the cleaner one [03:39-04:40]. Output OpenEXR (multilayer if passes are needed). The farm analyses the file first and lists missing assets [05:43]. Test frames: first, middle and last frame of every scene before committing [06:14]. A failed test frame was ticked and re-rendered [07:17]. Full job ran 123 nodes at once (about 41 per layer): 5 h 44 min of node time finished in under 10 minutes [08:21-08:53]. He forgot to set output file names per scene, so the downloads shared an odd name [09:56].

**Use it:** Template for a farm submit checklist: mirrored paths, per-layer scenes, per-scene sample budget, three test frames, named output per layer.
Transcript support: same first/middle/last habit stated as industry practice while iterating on look, not only before a farm job (https://www.youtube.com/watch?v=RCCaQmwxNB4 [20:33])
