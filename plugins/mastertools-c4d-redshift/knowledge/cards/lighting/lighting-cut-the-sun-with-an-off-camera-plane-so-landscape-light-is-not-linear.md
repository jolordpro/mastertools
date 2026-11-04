---
id: lighting-cut-the-sun-with-an-off-camera-plane-so-landscape-light-is-not-linear
title: A single sun on terrain falls too evenly; a plane placed near the land to cast shadow from imagined mountains breaks it up
domain: lighting
tags: [landscape lighting, gobo, cutter, fog volume, sun temperature, io studios, octane, deep-read]
applies_to: C4D Octane
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=kb1q3hi-NEs, src:yt-transcripts]
feeds: [elevate]
conflicts: none
---
IO Studios [4:52-6:26]: with one area light as sun on a displaced mountain, light fell "too linearly". Fix: hold a plane close to the landscape between light and ground so part of the sun is blocked and a patch of shadow appears, as if other peaks surrounded it. He notes the cutter's edge is a bit harsh and a real landscape mesh would be more accurate. Other settings he used: sun colour via temperature (lower is yellow-red, higher blue) set to an orange [5:00]; area light moved farther away for less harsh shadows [4:52]; daylight sky power about 0.7 with blue colour for an artistic look [3:46]; an atmospheric fog volume (disabled in the viewport) with density raised, a blue-ish absorption and scattering, and the light and sky powers raised to compensate for the dark volume [7:28-11:46]; render with the path tracing kernel whenever volumes are used [8:32]; shallow depth of field and a little bloom plus a LUT to finish [12:16-13:49]. Octane-specific numbers (voxel size, 4k/8k displacement detail 100) are his.

**Use it:** In C4D + Redshift, add a flag plane (or light linking) as a cheap cutter to give a lone key a believable broken shadow; add fog only after light powers are matched.
