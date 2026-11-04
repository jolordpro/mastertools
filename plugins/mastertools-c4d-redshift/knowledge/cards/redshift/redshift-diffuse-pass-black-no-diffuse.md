---
id: redshift-diffuse-pass-black-no-diffuse
title: A black Diffuse Lighting pass means the scene has no diffuse component (for example only reflective materials)
domain: redshift
tags: [diffuse lighting pass black, no diffuse, reflective, aov troubleshooting]
applies_to: Redshift 2024
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [advisor]
conflicts: none
---
If objects are fully reflective or only rough specular, there is nothing to put in the diffuse pass [1:01:32]. Make sure at least one material has a base colour and diffuse weight above zero. The captions say "above one"; likely a weight, not sure.

**Use it:** Symptom-first answer for a black diffuse pass: check the materials for a diffuse weight.
