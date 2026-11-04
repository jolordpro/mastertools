---
id: gpu-cloud-octane-network-animation-needs-octane-object-tag-and-render-queue
title: Octane network animation in C4D: add an Octane Object tag to moving objects and render through the Render Queue, not the Picture Viewer
domain: gpu-cloud
tags: [octane, network rendering, octane object tag, render queue, picture viewer, animation, freeze, deep-read]
applies_to: OctaneRender 2.23 + C4D (about 2019)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Vvf_-toAOU8, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Brandon Clemens [07:21-10:24]: for an animated object the Octane Object tag tells Octane to re-read its position every frame. He renders animation through Add to Render Queue instead of the Picture Viewer because the viewer froze after a couple hundred frames in his experience; the queue also drops C4D out of the loop, sending jobs straight to Octane. Set the output path and an alpha channel, then Start. Frames go into an After Effects comp at 24 fps. Simple test scene rendered at about 4 s a frame on several GPUs.

**Use it:** Octane-specific; keep for Octane farm jobs. The Picture Viewer freeze is one user's report.
