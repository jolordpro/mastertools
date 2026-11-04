---
id: pipeline-gen-ai-3d-depth-reproject-matte-backgrounds
title: Stellar's AI background route: proxy 3D scene, Z-depth, LoRA, then reproject onto geometry and render with a camera move
domain: pipeline
tags: [[matte-painting, depth, reprojection, stellar-creative-lab, mask, inpainting], deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bWvxBu_vVes, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Bert Van Brande: artists hit a Slingshot button in Maya or Blender; the Z-depth (plus a mask from a selected object for in-painting) feeds Stable Diffusion 1.5 or SDXL for painterly 2.5D backgrounds, Flux for photoreal [1:25:27][1:39:03]. A proxy of the environment is enough, no detail needed [1:40:39]. One large Blender environment used six cameras and six generated paintings [1:41:42].
Reason for reprojecting the images onto the 3D scene and rendering traditionally: frame-to-frame consistency of the video models was poor then (about 1.5 years before the talk), so camera moves came from 3D [1:42:14]. Next: light placement controls, cryptomattes driving prompts, AI video as a "probabilistic renderer" fed by proxy animation [1:43:49-1:44:52].

**Use it:** Same trick for C4D: depth AOV plus object mattes as AI conditioning, projected back for parallax.
