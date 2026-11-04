---
id: comp-position-camera-is-a-real-world-depth-so-values-change-when-the-camera-moves
title: Position camera acts as a depth pass in scene units: five metres away reads 5, and moves to 2 when the camera pushes in
domain: comp
tags: [mitchell-woodin, depth, position camera, z pass, scene units, deep-read]
applies_to: Blender
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=tB5-Oe7pTUs, src:yt-transcripts]
feeds: [[post-composite]]
conflicts: none
---
Woodin skipped the built-in Z pass because the position camera pass carries real distance from the camera; to see it, push the viewer's exposure down in colour management [11:15][11:47]. If a pixel is five metres from the camera the value is 5; push in to two metres and it becomes 2 [11:47]. This differs from a normalised depth that is rescaled per shot. He notes this method saves studios time at deadlines, and part 2 covers rendering and Nuke [12:20]. The speaker does not give a unit scale setting; "metres" is his example.

**Use it:** use camera-space position or real-unit depth for fog and DOF in comp, and check the value scale when the shot camera changes.
