---
id: pipeline-unreal-from-c4d-use-fbx-not-live-link
title: A broadcast team found C4D-to-Unreal direct export broke projects and gave poor textures, so used FBX and retextured in Unreal
domain: pipeline
tags: [unreal, fbx, c4d, direct link, texturing, nodes, broadcast, super bowl]
applies_to: Unreal 5.x (2024 talk)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=fmq6hNARJ9U, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
[42:06] Textures from the C4D export did not pop; projects sometimes lost items on re-save. They exported FBX, with modelling in C4D and Blender, then retextured with Unreal's own nodes.
[44:11] Unreal's node trees get large: texture scale and similar controls are separate nodes, built for game optimisation.
[45:47] Some elements were still rendered in C4D for quality, matched in Unreal by lighting and texturing.

**Use it:** if a client wants Unreal, plan FBX plus retexture time, not a one-click bridge.
