---
id: c4d-procedural-craters-target-effector-repel-then-delta-mush-smooth
title: Craters on a sphere: clone circles over the surface, push points away with a Target effector in Repel and field direction mode, then clean up with Connect and Delta Mush at stiffness 0
domain: c4d
tags: [craters, target effector, repel, delta mush, smoothing, connect object, instance, cloner, volume builder, deep-read]
applies_to: Cinema 4D 2022 (Maxon Ask the Trainer, Apr 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cCCgPVurWjQ, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Trainer (Nosman) [29:06-35:25]. Habit: keep a hidden source sphere and deform an instance of it; hide the source by grouping it under a null (the instance still shows, a plain visibility toggle would hide both). Clone circles on the sphere surface, drop the cloner into a Target effector's field list as a spline object (only its weights come across), set Repel, deform points, switch distance from Along to Radius.
The raw result looks ugly; smooth with a Connect object and Delta Mush (a different kind of smoothing from the Smoothing deformer) with Stiffness 0 and few iterations to stay fast while hiding artefacts [32:45-33:50]. A Random effector on the circle cloner varies crater size [35:05]. A second copy of the cloner with spheres in Multi-Instance, under Volume Builder and Measure, gives a blobby organic form [34:20-36:27].
Caveat: if MoGraph dynamics feed a Volume Builder, bake the dynamics first (cache); the order of evaluation breaks live [35:56].

**Use it:** Fast crater and pitted-surface looks with no sculpting; Delta Mush low iterations is the cleanup.
