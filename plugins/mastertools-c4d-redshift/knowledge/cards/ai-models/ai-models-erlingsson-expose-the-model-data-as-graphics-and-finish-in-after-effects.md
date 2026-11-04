---
id: ai-models-erlingsson-expose-the-model-data-as-graphics-and-finish-in-after-effects
title: "Ingi Erlingsson extracts data from generated video (depth, optical flow, labels) with custom ComfyUI nodes and composites it as graphics in After Effects"
domain: ai-models
tags: [ingi-erlingsson, golden-wolf, comfyui, optical flow, depth, after effects, motion graphics, polish, deep-read]
applies_to: ComfyUI, After Effects
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=XnaT-aJQZM0, src:yt-transcripts, src:polish-roster]
feeds: [motion-critique]
conflicts: none
---
Custom nodes pull information from the clip: depth, motion vectors shown as bright where most motion happens (the relationship between frames, not the content), tracked positions, text labels such as 'eye' [50:51-52:23]. He treats it as showing what an AI might see: the underlying information is put on top, not hidden [52:23-53:23]. Everything is sequenced, timed and layered in After Effects; about 50 percent of his ComfyUI use has no AI, and agents write the nodes [53:23; 1:00:05].

**Use it:** Overlay analysis passes (flow, depth, segmentation) as designed graphic layers to give AI-based or CG work a graphic signature.
