---
id: redshift-gi-engine-speed-differs-by-scene
title: Whether brute force or point cloud is faster depends on the scene, as two tests went opposite ways
domain: redshift
tags: [brute force, irradiance point cloud, gi engine, render time, scene dependent, benchmark]
applies_to: Redshift GPU
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=L4riSkE7FwA, https://www.youtube.com/watch?v=AFecCpLTUBI, src:yt-transcripts]
feeds: [estimator, redshift]
conflicts: none
---
Polygon Division 2024: default (point cloud secondary) 1:23, switching GI to brute force gave 1:01 [J 01:10-01:41]. Maxon trainer 2024: on an interior, switching from brute-force to point cloud halved the time [C 36:54].
Both stress it is one scene each; the Polygon Division video does not say which scene or settings.

**Use it:** never auto-apply one GI engine; time both on a representative frame (two drafts) and let the estimator record the winner per scene type.
