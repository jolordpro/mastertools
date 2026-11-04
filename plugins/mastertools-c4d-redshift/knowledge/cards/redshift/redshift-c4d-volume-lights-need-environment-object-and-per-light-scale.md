---
id: redshift-c4d-volume-lights-need-environment-object-and-per-light-scale
title: C4D Redshift volume light needs a Redshift Environment object and a per-light volume contribution scale; 0.01 to 0.1 suited most lights, 0.01 for the sun
domain: redshift
tags: [volumetric, volume lighting, environment, contribution scale, c4d, maxon redshift, 2018, deep-read]
applies_to: C4D + Redshift, Maxon Redshift channel upload 2018
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vnHKQmvKYH8, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Maxon's own channel (2018): volumetric scattering only appears once a Redshift Environment object exists (Redshift menu > Objects) [01:08]. Every light's Volume tab has Contribution Scale, default 0, so nothing scatters until it is raised [01:39].
Values shown: softbox area light plus global scatter 0.1 looked right; street lights at 0.1 were far too strong and 0.01 worked; a text mesh light 0.01; a blue phone light 0.1; headlight spots 0.01 to 0.05 [15:28-17:51]. The physical sun needed 0.01 because 0.1 was overpowering [18:36].
A light can also be lowered globally by dropping the environment scattering value instead of editing every light [15:59].

**Use it:** volume checklist: environment object present, each wanted light's contribution above 0, and start near 0.01 for bright lights (sun, street) before scaling up. Supports `redshift-houdini-volume-needs-light-volume-contribution-scale-and-samples` for the C4D side.
