---
id: lighting-redshift-light-group-per-aov-diffuse-spec-then-add-and-tint-each-light-in-comp
title: Redshift light groups can be chosen per AOV (beauty, diffuse, specular), then each light is added and tinted separately in comp
domain: lighting
tags: [light groups, aov, comp, relight, add, client notes, deep-read]
applies_to: Redshift in C4D
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sms_DSANx_s, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
Set the group on each light under Details, AOV Light Group, add a new group and name it like the light [02:31-03:41]. Several lights can share one group, for example two domes called dome [03:10-03:41].
In the AOV manager each AOV (Beauty, Diffuse, Specular and others) has its own light-group choice: all groups or selected ones, giving extra passes per group [04:42-05:43].
Test scene: four area lights and two domes gave five groups; in comp each group's beauty is added and a tint per layer recolours that light [05:43-08:48].
Benefit named: a client's 'make his face more red' becomes a comp change, not a re-render [09:18].
He also faded one light's pass with a subtract to bring a character out of the dark, but says he had not tried it before and parts may look bad [09:51-11:24].

**Use it:** Lighting changes late in a broadcast package: render light groups once and let comp serve the alternate looks.
