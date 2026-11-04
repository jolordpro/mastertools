---
id: comp-relight-normals-detail
title: Normal-pass relighting looks plastic when the normals pass lacks bump and normal-map detail
domain: comp
tags: [comp, relight, normals, position pass, nuke, plastic, bump]
applies_to: Nuke Relight
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=M-iKJu9hYBk, https://learn.foundry.com/NUKE/content/comp_environment/3d_compositing/lighting.html, src:research-youtube, src:research-vfx-pipelines, https://www.youtube.com/watch?v=NaCJiquNnYY]
feeds: []
conflicts: none
---
Compositing Academy video (2026-04-06): check that the normals pass carries surface detail, which is a Redshift setting.
Nuke's Relight takes normal and position passes plus 3D lights; shadows were not confirmed and a baked AO pass is the usual workaround.

**Use it:** before promising a comp relight, check the normals pass for detail.
