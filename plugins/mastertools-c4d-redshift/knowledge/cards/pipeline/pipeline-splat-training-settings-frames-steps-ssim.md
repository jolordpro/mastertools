---
id: pipeline-splat-training-settings-frames-steps-ssim
title: Gaussian splat training: pick about 150 sharp frames from a 988-frame video, train to about 30,000 steps, and trust an SSIM above about 0.9
domain: pipeline
tags: [gaussian splatting, postshot, training steps, ssim, frame extraction, structure from motion, deep-read]
applies_to: Postshot (Jawset), 4K video source
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ERuRMOVO58Q, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Source can be photos or a video; he used 4K video of a kitchen sink with reflective, transmissive areas [01:34]. Of 988 possible frames he asked for 150; the tool keeps the best ones with low noise and motion blur, so more frames is not better [02:06]. Pipeline order: frame extraction, feature extraction and camera matching (slower with more or larger images), then training [03:39]. Training is guess-and-refine over about 30,000 steps; a rough scene shows by 1,000-2,000 steps, and past about 30,000 gives diminishing returns or overtraining [03:08]. SSIM near 1 means low error; above 0.9 is good, he stopped at about 0.9 after 20,000 steps [05:44][08:48]. Hiding the splat in the viewport trains faster because the GPU is not drawing it [05:12]. Training can be paused and resumed.

**Use it:** reference numbers when a user plans a splat capture: frames kept, step count, and the quality readout to stop at.
