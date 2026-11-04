---
id: c4d-voronoi-fracture-directed-by-fields-and-held-dynamics
title: Direct a fracture with fields and effectors, or use rigid-body dynamics with scene dynamics at 0% and follow-position strength to hold pieces
domain: c4d
tags: [bas helmig, bart brinkman, italian giants, voronoi fracture, mograph, fields, dynamics, follow position, cinema 4d, deep-read]
applies_to: Cinema 4D R22-era
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Cf9t-bPQkb0, src:yt-transcripts, https://www.youtube.com/watch?v=cCCgPVurWjQ, https://www.youtube.com/watch?v=_6toVWN7NMo, https://www.youtube.com/watch?v=7-q1JKG8638]
feeds: []
conflicts: none
---
Bas Helmig and Bart Brinkman (Italian Giants, Dutch 3D studio; Maxon 3D and Motion Design Show): Voronoi Fracture reads point sources, noises or splines; offsetting and inverting it, then a volume builder with a small voxel size and dilate/erode, makes a coral base that stays procedural [47:17-50:24].
To art-direct the head break, any MoGraph effector with a field can move pieces (e.g. a plane effector pointing backward), and a push-apart effector works point-based so low-poly pieces may intersect [52:28-54:03].
Dynamics option: rigid-body tag with scene dynamics set to 0% so nothing falls, then follow position and rotation with strength 10 hold it where you directed [54:34-55:36].

**Use it:** Technique note for destruction shots: fields for art direction, held dynamics for believability.
Transcript support: Adds the exact tag settings: rigid body Follow Position and Rotation at 5/5 or 1/1, and that the default 0 ignores cloner animation (https://www.youtube.com/watch?v=cCCgPVurWjQ [1:09:49-1:12:31])
Transcript support: Follow Position and Rotation at 1 tracks the cloner exactly; 0.5 is loose (C4D 2024 rigid body) (https://www.youtube.com/watch?v=_6toVWN7NMo [26:03-27:07])
Transcript support: Fields drive effectors and dynamics the same way; one linear field across several Plane effectors (https://www.youtube.com/watch?v=7-q1JKG8638 [10:25])
