---
id: comp-passes-pick-aov-list-from-the-materials
title: Pick the AOV list from what the scene contains: emission, shadow matte, specular direct and indirect, one transmission pass, SSS, a custom AO, Z depth
domain: comp
tags: [aov list, render passes, exr, arnold, emission, transmission, shadow matte, sarkamari, deep-read]
applies_to: Arnold in Maya, Nuke
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=4A9kbUZpqIU, src:yt-transcripts]
feeds: []
conflicts: none
---
Reza's list for a robot on a plate: Z depth, diffuse direct and indirect, emission (glowing parts), shadow matte, specular direct and indirect (metal), a single transmission pass because the goggles are small and only a little transparent, SSS for the teeth [02:49-04:56]. AO was added as a custom AOV with an AO shader at 16 samples and spread about 0.8 [04:56-05:26]. EXR throughout to keep dynamic range for grading [05:26-05:56]. Do not raise AA samples to cure time: render time triples on a deadline [02:17].

**Use it:** Use as a worked example of 'ask what each object needs' rather than ticking every AOV.
