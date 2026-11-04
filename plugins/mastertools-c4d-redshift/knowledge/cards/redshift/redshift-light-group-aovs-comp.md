---
id: redshift-light-group-aovs-comp
title: Light groups added to the beauty AOV can be summed and rebalanced in comp, with a Remainder mode for unassigned light
domain: redshift
tags: [light groups, aov, comp, remainder, beauty, relight, cryptomatte]
applies_to: Redshift 2026-2027
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/r3d/cinema/en-us/Content/html/Light+Group+AOVs.html, src:research-vfx-pipelines, https://www.youtube.com/watch?v=q5Pyx7Jb5Xo, src:yt-transcripts, https://www.youtube.com/watch?v=CXx75LxGxOw, https://www.youtube.com/watch?v=0amlKMClE4s, https://www.youtube.com/watch?v=ZrOiwMSGmIw, https://www.youtube.com/watch?v=IjFXi2axl-8, https://www.youtube.com/watch?v=oANXbk9OUbI]
feeds: [comp-fix planner, Phase 1 light match]
conflicts: none
---
Name a light group on each Redshift light and add a beauty AOV with light groups. Change gain or colour per group instead of re-rendering. Remainder collects unassigned light.
Some effects do not support light groups; their shading lands in the "other" or "all" pass. Pair with Cryptomatte for per-object control.

**Use it:** use as the exact light-mix route and warn about effects that fall outside the groups.
Transcript support: Multiply per pass to keep light groups editable. (https://www.youtube.com/watch?v=q5Pyx7Jb5Xo [47:45])
Transcript support: Light groups sit in the diffuse lighting AOV only; every group multiplies the passes and file size. (https://www.youtube.com/watch?v=CXx75LxGxOw [1:23:13])
Transcript support: Roberts rebuilds light groups with Add and rebalances by percent (75/30/30/20 in his example) and says camera exposure must be matched (https://www.youtube.com/watch?v=oANXbk9OUbI [34:44])
