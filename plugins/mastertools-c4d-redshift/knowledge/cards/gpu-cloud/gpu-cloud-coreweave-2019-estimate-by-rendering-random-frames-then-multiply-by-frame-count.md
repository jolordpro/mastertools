---
id: gpu-cloud-coreweave-2019-estimate-by-rendering-random-frames-then-multiply-by-frame-count
title: CoreWeave's cost estimator: sample random frames across the shot, average, then multiply by frames (example 35 cents a frame, 250 frames)
domain: gpu-cloud
tags: [coreweave, blender, estimate, sampling, cloud-render, marco, deep-read]
applies_to: CoreWeave Concierge, Blender Conference talk uploaded 2019-10
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sh8UhQ1zofg, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Marco: the estimate button renders sample frames picked across the whole range, because a camera that turns to a very different view at frame 10 would make a first-frame estimate wrong [34:38-35:43].
He averages these to a per-frame number (35 cents in the demo) and the user multiplies by frame count; the estimate is free and he calls it close to exact [35:43-36:14].
The job manager also streams a preview of the animation as frames land, so wrong motion can be caught before the job finishes [36:48-37:20].

**Use it:** same method as the existing late-frame sampling card: pick frames from early, middle and late, never frame 1 alone.
