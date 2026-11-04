---
id: comp-vector-blend-denoise-cuts-noise-by-frame-count-and-costs-edge-frames
title: Vector-blending neighbour frames cuts noise by the number of frames averaged (3 frames about 66%, 5 frames to a fifth), costs extra edge frames, and ghosts on fast moves
domain: comp
tags: [denoise, vector blending, motion vector, averaging, boiling, fusion, after effects, robin squares, deep-read]
applies_to: Blender Cycles render, Fusion or After Effects (2026)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=yAbuPpbbATA, src:yt-transcripts]
feeds: []
conflicts: none
---
Robin Squares [03:40-07:10]. Render the motion vector pass; in post, shift frame n-1 and n+1 onto frame n using the vectors and average: the same point is sampled three times, so noise falls by about 66% (his figure); with two frames each side, 5 samples, a factor of five, but then four extra frames must be rendered because the first and last two frames cannot be fully denoised. Because it averages real pixels, there is no AI boiling. Limits: ghosting and fringing when things move fast or perspective changes a lot (a median filter instead of a naive average helps with edge fringing); not aggressive, so usually only three frames, and it is best as a first step before another denoiser. He says it is common in high-end production and should be a step in any big production.

**Use it:** The comp planner can offer 'render 1 extra frame each side and vector-blend' as the first cheap step against noise, and warn about ghosting on fast moves.
