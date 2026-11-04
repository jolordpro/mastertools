---
id: comp-ao-multiply-inside-diffuse-total
title: Apply the AO pass by multiplying it inside the diffuse total, not over the whole image
domain: comp
tags: [ambient occlusion, multiply, diffuse total, exposure, gamma, grade ao]
applies_to: Redshift AOVs, After Effects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts, https://www.youtube.com/watch?v=4A9kbUZpqIU]
feeds: [comp-fix planner]
conflicts: none
---
A top-level multiply works but darkens lights too [1:08:23]. Put AO as a multiply layer inside the diffuse total beside the filter [1:08:55]. Soften or deepen it with Exposure, Gamma (keeps black and white), opacity, or a per-channel tint for a slight colour in shadows [1:09:59-1:11:36]. View raw passes with display set to raw; AE still uses the true values [1:07:21].

**Use it:** Put AO in the diffuse branch in the planner; it is a cherry on top when lighting is already good [46:37].
