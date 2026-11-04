---
id: gpu-cloud-redshift-2-5-vs-v-ray-2019-student-render-time-claims-maya-houdini
title: 2019 student claims: Redshift 2.5 vs V-Ray render times in Maya and Houdini (pyro 336 s vs about 7.5 min; god-ray pass 1-2 min vs 25-35 min)
domain: gpu-cloud
tags: [redshift, v-ray, render time, gpu rendering, maya, houdini, 2019, pny, student, deep-read]
applies_to: Maya and Houdini + Redshift 2.5/2.6, V-Ray (video Aug 2019)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=YPpJ9GNHeW0, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Josh Harrison, an effects student, in a PNY presentation (Aug 2019). He says a Houdini pyro final frame took 336 s in Redshift 2.5 against about 7.5 min in V-Ray [08:00-08:30], and a god-ray pass in a 1080 shot with fog took about 1-2 min in Redshift versus 20-35 min in V-Ray [06:25-06:57]. His reasoning: a single GPU machine replaces several CPU machines for a freelancer, so iteration is cheap (render in five minutes, check, redo; a 115-frame wedge in under five minutes) [09:01-14:10]. One AOV forgotten means a short re-render, not hours [15:12]. Student, single data point, scenes not given; treat as anecdote. Features he listed as new or coming: Optix denoising, AOV and Cryptomatte, subsample motion blur on deformation (curved arcs vs straight-line blur), render-view post effects, caustics, one-slider automatic sampling, and toon shading planned for 3.0 [17:48-22:57] (his statement; compare release notes).

**Use it:** do not use as an estimator input; it shows what a 2019 speaker believed, and prices and speeds have moved.
