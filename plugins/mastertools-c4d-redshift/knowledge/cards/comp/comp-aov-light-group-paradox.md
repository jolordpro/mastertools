---
id: comp-aov-light-group-paradox
title: Material AOVs and light groups each sum to the beauty but slice it differently, so an edit in one does not show in the other
domain: comp
tags: [light groups, material aovs, paradox, compositing, rebuild]
applies_to: any (Nuke, Blender, Redshift, Arnold, Octane)
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=q5Pyx7Jb5Xo, src:yt-transcripts, https://www.youtube.com/watch?v=UCUXhXKDnWQ, https://www.youtube.com/watch?v=0amlKMClE4s, https://www.youtube.com/watch?v=IjFXi2axl-8]
feeds: [comp, coach]
conflicts: none
---
Both rebuilds sum to beauty. Imagine a layer cake: each material slice contains all lights; each light slice contains all materials. Removing speculars in the material rebuild leaves them in every light group; removing lights in the groups leaves them in the specular [00:53-05:41].

**Use it:** comp planner: do not let a user edit both rebuilds independently and expect one answer.
