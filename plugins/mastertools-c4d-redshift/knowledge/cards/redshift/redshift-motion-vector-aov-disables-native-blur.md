---
id: redshift-motion-vector-aov-disables-native-blur
title: Turning on the Motion Vector AOV switches off Redshift's own blur in the beauty
domain: redshift
tags: [motion vector, motion blur, aov, post blur, comp, redshift]
applies_to: Redshift 2026-2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Motion+Blur+-+Advanced.html.md, src:research-vfx-pipelines, https://www.youtube.com/watch?v=uKRqHwVr0F4, src:yt-transcripts, https://www.youtube.com/watch?v=w3HGJ2KuGfo]
feeds: [comp-fix planner, PLAN comp-first planner]
conflicts: none
---
With the Motion Vector AOV enabled the beauty comes out without native blur, for blur in post. Practitioners say vector blur matches well for straight moves but rotation never works well; raw and clamped vector modes differ. There is no published Redshift quality comparison between native and post blur.
Merged from `comp-vector-aov-disables-native-blur`: Deformation blur is off by default and costs memory on dense or displaced geometry; more transformation steps give more accurate trails and more memory. So a vector AOV means the blur must be added in comp.

**Use it:** treat post blur as a per-shot choice that needs a measured comparison, not a default saving.
Transcript support: Motion blur in post is a normal way to save render time. (https://www.youtube.com/watch?v=uKRqHwVr0F4 [08:51])
Transcript support: Same vector data is used to reproject neighbouring frames for temporal denoising. (https://www.youtube.com/watch?v=w3HGJ2KuGfo [05:46])
