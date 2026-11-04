---
id: lighting-fmx-scatter-broken-rocks-by-dropping-them-through-a-rigid-body-sim
title: "FMX 2014 TD student: scatter fractured rock pieces by dropping them onto the ground in a rigid-body sim so nothing interpenetrates"
domain: lighting
tags: [fmx, lighting, scatter, rigid-body, houdini, student, manuel, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=8tW77BsgtPY, src:yt-transcripts]
feeds: [c4d]
conflicts: none
---
For Globos (full CG short) the ground had to be covered in broken rocks. He fractured a flat box in Houdini with noise on the fracture borders [19:40-20:12], then tried an ordinary scatter plugin but pieces penetrated each other [20:12-20:44].
Fix: place the pieces in the air above the ground, run a rigid-body simulation, let them settle, and use the result [20:44-21:14].
Transfers to C4D: MoGraph/Dynamics drop with settle, or a scatter with proximity checks.

**Use it:** For debris and rubble in a dressing shot, simulate the drop and freeze the settled state rather than hand-scatter.
