---
id: pipeline-spring-linked-task-files-anim-lighting-sim-comp
title: Spring built a separate linked file per task (anim, lighting, sim, comp) and never appended assets
domain: pipeline
tags: [pipeline, linking, task files, animation, lighting, simulation, compositing, library, blender studio, deep-read]
applies_to: Blender 2.8
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aR3yNNGK_sc, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
The layout file is too messy for animators, so each shot gets an anim file started from empty and linking collections for characters, props and sets [22:47] [23:18]. Sets link environment assets; nothing is appended [18:05]. Lighting starts roughly after first blocking in its own file, links the same assets and re-links the actions from the anim file so animation updates arrive automatically [27:32] [28:04] [28:34].
A simulation file is allowed to be messy: it links the animation, makes needed objects local while keeping mesh data linked, and writes caches [29:26] [29:39]. Smoke was the heaviest data, cached as VDB with the domain appended; generic simulations cached as Alembic; particles stayed in the blend file and were linked in as collections [30:10] [30:40] [31:43].
Compositing is a separate file that links no animation, only rendered frame sequences [34:48].

**Use it:** Reference chain for estimating hand-offs: layout, anim, lighting, sim, comp, each file linking upstream outputs. Use as a checklist for what breaks when an upstream file changes.
