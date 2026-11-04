---
id: lighting-light-groups-setup
title: Redshift light groups: name a group on every light, add a light-group beauty AOV, keep a remainder pass for unassigned light
domain: lighting
tags: [lighting, light groups, aov, redshift, remainder, other pass]
applies_to: Redshift (C4D 2026-2027)
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/r3d/cinema/en-us/Content/html/Light+Group+AOVs.html, src:research-vfx-pipelines, https://www.youtube.com/watch?v=cE-Bbdspu_8, https://www.youtube.com/watch?v=_jGC7_fRlfw, https://www.youtube.com/watch?v=sms_DSANx_s]
feeds: [PLAN Phase 1 light match]
conflicts: none
---
Group names are set per light; the AOV then splits beauty by group. Remainder mode catches light from unassigned sources in an other pass.
Some effects do not support light groups; their shading falls into other or all. Pair groups with Cryptomatte for per-object control.
From a search summary of the Maxon page, so check the current help before relying on details.

**Use it:** preflight flags lights with no group and effects that will land in the remainder.
Transcript support: Group set per light under Details, AOV Light Group; each AOV (beauty, diffuse, specular) has its own light-group selection; several lights can share one group (https://www.youtube.com/watch?v=sms_DSANx_s [02:31-05:43])
