---
id: pipeline-milk-value-clips-for-crowd-and-time-varying-data
title: Value clips stitch a huge crowd or sim sequence into a light USD that tells the renderer what to load
domain: pipeline
tags: [milk vfx, value clips, crowd, manifest, template, simulation cache, deep-read]
applies_to: Houdini Solaris, ShotGrid (Milk VFX, FMX HIVE 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=XfMp13jOSxE, src:yt-transcripts]
feeds: []
conflicts: none
---
Enrico (co-head of VFX, Milk VFX; surname not caught). Crowd is where they began using value clips: stuffing a massive animation into one USD was not an option. Value clips create a stitched version whose dependencies are resolved at render time [25:20-26:54]. Crowd agents are built twice, a SOP agent for simulation and a LOP agent for casting [25:20-25:52]. After crowd, a ROP was made for all time-varying data that writes the clip sequence, a manifest USD and a template USD, which is what is loaded, cast and rendered from; first used on Heads of State [26:54-27:26].

**Use it:** For sims over many frames, think sequence plus manifest plus template rather than one file.
