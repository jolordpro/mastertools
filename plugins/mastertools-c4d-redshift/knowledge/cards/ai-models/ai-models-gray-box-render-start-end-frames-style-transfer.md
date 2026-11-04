---
id: ai-models-gray-box-render-start-end-frames-style-transfer
title: Summers' on-ramp for motion people: render a gray box with the camera, make start and end images, then style-transfer the shot
domain: ai-models
tags: [ryan summers, gray box, style transfer, start frame, end frame, camera, comfyui, mcp, deep-read]
applies_to: any
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=dsYggO4lsSo, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
He calls the idea style transfer: do a gray-box render with the camera where you want it, prompt or photobash a start and an end image, and let a video model fill between them, knowing the shot length and camera [31:09-31:40].
He also described agents driving Comfy: stitch outputs three and four as first and last frame in a second pass, no need to hand-build each workflow [32:11-33:43]. Every output carries its workflow, so dragging it back in shows how it was made [33:11].

**Use it:** block with a gray-box C4D render first, then use it as the camera and layout guide for any generative pass.
