---
id: comp-denoise-undistort-before-tracking-and-track-helpers
title: Prepare a plate for tracking: denoise, undistort, boost contrast; choose between stabilising and match-moving first
domain: comp
tags: [courtney price, nuke, foundry, tracking, undistort, denoise, vector warp, model builder, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=yl28HkA-qyo, src:yt-transcripts]
feeds: [composition]
conflicts: none
---
Courtney Price [25:06-27:43]: first decide whether to stabilise the plate or match-move the element. Denoise the plate (she uses a temporal denoiser at about 10 with edge preservation on), then undistort: tracking accuracy drops away from the centre, so comp in the undistorted space and re-add distortion to the elements.
If a track is hard, raise contrast: grade, band-pass, or key a channel or luma. If roto arrives, she has tracked it by eye. Vector warping suits cloth and faces. For points the camera tracker missed, she adds an axis in a model-builder node with two keyframes snapped to the point.
Nuke 12 grid-warp tracker exports 2D tracks; the 2D tracker has keyframe tracking for occlusions.

