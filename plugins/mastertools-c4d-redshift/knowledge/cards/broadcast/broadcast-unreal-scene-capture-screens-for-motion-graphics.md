---
id: broadcast-unreal-scene-capture-screens-for-motion-graphics
title: Screen graphics were built in a separate space below the set and fed to the screens by Scene Capture cameras
domain: broadcast
tags: [unreal, scene capture, render target, screens, umg, motion graphics, deep-read]
applies_to: Unreal Engine 4.27 (concepts carry to UE5)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bcL001ZFHBQ, src:yt-transcripts]
feeds: []
conflicts: none
---
A second 'screen content' level sits about 10,000 units below the stage. Scene Capture cameras render it to textures that feed the screen materials above, so graphics are built like normal 3D scenes rather than scripted UI [08:07-08:38].
Chosen over UMG, which suits game UI and needs scripting [08:38-09:10]. Watch cost: limit number of capture cameras and their resolution, and turn off render features they do not need [08:38]. The GPU profile later showed the capture handling background text projected on the wall [51:53-52:24].

**Use it:** Keep screen content in its own space and limit captures; this is the cheap way to get a stack of animated wall graphics.
