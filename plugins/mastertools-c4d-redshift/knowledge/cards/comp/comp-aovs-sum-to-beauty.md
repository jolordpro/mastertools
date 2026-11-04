---
id: comp-aovs-sum-to-beauty
title: AOVs should sum back to the beauty; test one frame before the full sequence
domain: comp
tags: [comp, aov, beauty, sum, pre-delivery test, light groups, exr]
applies_to: any
status: V2
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://irendering.net/houdini-to-nuke-and-beyond-getting-aovs-and-exrs-right-the-first-time/, https://help.otoy.com/hc/en-us/articles/33731716535067-Render-AOV-Checklist-for-Post, src:research-vfx-pipelines, src:research-youtube, https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts, https://www.youtube.com/watch?v=q5Pyx7Jb5Xo, https://www.youtube.com/watch?v=CXx75LxGxOw, https://www.youtube.com/watch?v=ARykOD6lG3c]
feeds: [PLAN comp readiness]
conflicts: none
---
Half float is fine for data passes, full float for lighting.

**Use it:** add a sum-to-beauty check on the draft before the full run.
Transcript support: rebuild must match the beauty exactly; a brighter or more contrasty result means the rebuild is wrong (https://www.youtube.com/watch?v=IcLiz8e8ffc [30:13])
Transcript support: Both material-AOV and light-group rebuilds must add up to beauty separately. (https://www.youtube.com/watch?v=q5Pyx7Jb5Xo [52:21])
Transcript support: Rebuild is close to the beauty but not identical when reflection/refraction are split into raw and filter. (https://www.youtube.com/watch?v=CXx75LxGxOw [42:00])
Transcript support: Chad rebuilt a beauty from the manual formula in Fusion and it matched; says it works in Nuke, After Effects, even Photoshop (https://www.youtube.com/watch?v=ARykOD6lG3c [02:39-05:18])
