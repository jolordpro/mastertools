---
id: ai-models-hybrid-shot-control-3d-render-nuke-camera-gen-ai-image-splat-set-then-video-model
title: Amaru Zeas's hybrid shot: text prompts alone failed four times, so he built the shot with a CG car, a Nuke camera, generated splat set pieces, an agent that writes JSON prompts from camera widgets, then a video model and a depth-pass comp
domain: ai-models
tags: [amaru-zeas, griptape, nuke, gaussian splats, cgi, video model, hybrid pipeline, deep-read]
applies_to: Griptape, Nuke 17, video models (2026)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=OR6TYHY1Uag, src:yt-transcripts]
feeds: []
conflicts: none
---
Amaru Zeas (18 years in M&E, with Jason Schleifer at Griptape/Foundry). A months-built realistic car render with four plain text-prompt attempts failed to produce the shot [31:33-32:35]. Steps: sketch tool and base prompt via an agent for context [32:35]; a low-poly car and a quick tree from generative 3D [33:06]; Nuke to place the camera exactly [33:38]; a custom camera widget exposing parameters that an agent turns into JSON prompts [34:09]; Street View extraction and a local model changing sunny to winter [34:41-35:43]; batch regeneration with colour matching to fix drift [35:43-36:45]; image to splat, import splats into Nuke 17, crop and recolour a too-bright cave, place camera and car [36:45-38:19]; still back through an image-to-image flow; animate the camera against the low-LOD splat; final video model plus traditional comp with depth passes [38:19-39:50]. He always returns to Photoshop for the final pixel [35:43]. Conference demo; conclusions are his.

**Use it:** Reference for how CG, splats and generative tools can be combined under a real camera. Related: ai-models-four-levels-of-control-pixel-frame-shot-multishot.
