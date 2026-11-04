---
id: ai-models-rife-interpolation-target-30-or-60-with-a-60-ceiling-and-slow-motion-use
title: RIFE frame interpolation in Contenta's tool offers only 30 or 60 fps targets, stops at 60, and for slow motion you interpolate to 60 then play back at the original rate
domain: ai-models
tags: [contenta-software, rife, frame interpolation, 60 fps, slow motion, deep-read]
applies_to: AI Video Enhancer Studio (Contenta), RIFE
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=nFR0ZXwaD4o, src:yt-transcripts]
feeds: []
conflicts: none
---
Vendor video. Choose 30 (gentle) or 60 (smoothest) as the target; RIFE adds exactly the frames needed [00:33]. Clips already at or above the target are untouched; the ceiling is 60 [01:36]. A 9 s clip took a little over a minute on an RTX 3080 [00:33]. Use cases: 24 or 25 fps to 30 or 60, 30 to 60, 15 to 30; for slow motion, interpolate to 60 then play back at the original rate [01:05]. Claims no ghosting and no duplication; runs on Vulkan on any GPU, offline. Vendor claims, unverified.

**Use it:** Quick fact for the interpolation options. See ai-models-rife-mlx-frame-interpolation for Apple Silicon.
