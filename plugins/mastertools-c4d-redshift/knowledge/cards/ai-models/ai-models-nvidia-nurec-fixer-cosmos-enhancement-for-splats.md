---
id: ai-models-nvidia-nurec-fixer-cosmos-enhancement-for-splats
title: NVIDIA NuRec pairs 3D Gaussian reconstruction, ray-traced rendering and a generative 'fixer' model to clean up weak splat views
domain: ai-models
tags: [nvidia, nurec, fixer, cosmos, gaussian splatting, 3dgrut, artifixer, ppisp, simulation, deep-read]
applies_to: 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=KZqv3Z5rRg8, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
An NVIDIA speaker describes NuRec as reconstruction libraries, a rendering API built on 3DGRUT (ray tracing with splatting efficiency) and generative enhancement models based on world foundation models such as Cosmos; the Fixer model is on Hugging Face and usable outside NuRec [21:36] [22:07] [22:40]. Main use is autonomous-vehicle and robot simulation: edit recorded scenes, such as slowing the car ahead or moving the vehicle six inches [23:12] [23:45].
Recent research: PPISP (physically plausible image signal processing; handles per-image exposure differences, permissive licence) [30:32]; Diffusion Harmonizer for lighting and domain gap; Artifixer for very sparse inputs (three views) [31:33] [32:05].
Code for the last two was not yet out at the time.

**Use it:** Note for any AI-cleanup tool: sparse capture plus generative repair is the direction; exposure compensation per image is a known problem for scans.
