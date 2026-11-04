---
id: pipeline-usd-camera-change-without-re-export-chain
title: With layered USD, a camera fix is edited in place and merged into the layout layer, then the container is re-rendered, no other department redoes work
domain: pipeline
tags: [pipeline, usd, camera, layout, edit, merge, layer, deadline, deep-read]
applies_to: Houdini Solaris, Maya, Deadline
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CpiumJctktM, src:yt-transcripts, https://www.youtube.com/watch?v=jfH7JpjDO_w]
feeds: [estimator]
conflicts: none
---
In many pipelines a camera change means layout builds a new camera, animation and effects re-import it and lighting starts a new render [26:19] [26:49]. In the demo layout opened the shot in Houdini even though it was authored in Maya, unmuted downstream departments, used a camera node in edit mode to move it, and could view the effect in the renderer [27:19] [27:51].
The export node had a merge option to add the camera into the existing layout layer, which also holds asset references, instead of replacing it [28:22]. A new render was submitted from layout straight from the shot container, which already held all other departments' layers [28:22] [28:52].
By default the import node mutes downstream and the current departments [27:19].

**Use it:** Selling point for layered scene hand-offs: late camera changes cost one edit plus one render. Add a pipeline check that edit exports merge rather than overwrite.
