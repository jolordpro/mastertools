---
id: redshift-deformation-blur-default-off
title: Deformation motion blur is off by default and is costly on dense or displaced geometry
domain: redshift
tags: [deformation blur, motion blur, memory, displacement, default]
applies_to: Redshift 2026-2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Motion+Blur+-+Advanced.html.md, src:research-agency-pipelines, src:research-vfx-pipelines, https://www.youtube.com/watch?v=tsx8Isq6m-s]
feeds: [advisor]
conflicts: none
---
Leave it off when nothing deforms. It adds memory on dense or displaced meshes.

**Use it:** only suggest turning it on when a deforming object is visibly blurred in the draft.
Transcript support: animated displacer with no transform shows no blur until Enable Deformation Blur is ticked (https://www.youtube.com/watch?v=tsx8Isq6m-s [08:46-09:28])
