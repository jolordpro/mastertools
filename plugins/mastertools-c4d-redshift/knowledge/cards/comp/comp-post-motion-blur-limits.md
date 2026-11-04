---
id: comp-post-motion-blur-limits
title: Blur from vectors in comp matched Arnold's blur for straight moves, but rotation, transparency, occlusion and big parallax are weak
domain: comp
tags: [comp, motion blur, rsmb, vectors, post blur, rotation, transparency]
applies_to: Nuke/RSMB practice
status: V2
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2026/en-us/Content/html/MOTIONBLUR.html, https://novedge.com/blogs/design-news/cinema-4d-tip-efficient-motion-blur-workflow-for-cinema-4d-and-redshift, src:research-vfx-pipelines, https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: []
conflicts: none
---
Practitioner reports: rotation never works well; Raw and Clamped vector modes differ.
One guide says post blur misses camera blur; that conflicts with how vectors are normally built, so unconfirmed.
No public quality comparison against native Redshift blur exists.

**Use it:** keep blur in the render for spin, glass, heavy overlap and rotation; measure the gap with ꟻLIP on the hero frame.
Transcript support: Motion blur and depth of field in post depend on the scene; can pass a quick test but not hold up if pushed. (https://www.youtube.com/watch?v=CXx75LxGxOw [1:27:26])
