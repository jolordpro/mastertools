---
id: pipeline-union-splat-crowd-cryptomatte-variation
title: Splat crowds get cryptomattes from image segmentation, so comp can recolour clothes and vary clones like normal CG
domain: pipeline
tags: [cryptomatte, segmentation, crowd variation, gaussian splat, comp, union vfx, deep-read]
applies_to: Houdini, Nuke
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Ybln1zAQDVc, src:yt-transcripts]
feeds: [comp handoff]
conflicts: none
---
On ingest Union runs machine-learning image segmentation on the captures, finding jacket, trousers, shirt, hair, skin [05:12]. The labels are seen from many angles and projected back into the splat data, then rendered out as cryptomattes [05:43]. Compositors use those mattes for colour correction and colour variation so neighbours do not read as copies [08:52]. Props such as caps or flags can be added later because hand and head positions are known [11:28]. The splats also carry high-definition surface normals from the training pipeline, so no normals have to be estimated afterwards [12:30]. Fine detail like hair is helped by raising splat count and primitive size, with 2D cleanup on top [14:32].

**Use it:** for crowd shots, ask for a cryptomatte per clothing region; vary hue and value in comp rather than re-rendering.
