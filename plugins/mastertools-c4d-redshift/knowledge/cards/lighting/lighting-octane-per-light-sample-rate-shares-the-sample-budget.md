---
id: lighting-octane-per-light-sample-rate-shares-the-sample-budget
title: Raising one light's sample rate lowers noise from that light but leaves the others noisier, because the scene's samples are shared
domain: lighting
tags: [octane, new-plastic, sampling, noise, light sampling, per-light, deep-read]
applies_to: Octane for Cinema 4D (2022 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=J5KwV7GfbEQ, src:yt-transcripts]
feeds: [[redshift, estimator]]
conflicts: none
---
Test he showed: two lights, one at 1 sample and one at 10,000 (versus 1,000), both rendered at 512 overall samples; the light with more samples gave a nearly noise-free wall, while the other light's areas stayed noisy [10:56][11:28]. His rule: a light with higher samples takes samples from the others, so it is a balance among all lights [11:28]. Glass stayed noisy either way, partly lit by the other light [11:28]. Figures as heard in the auto captions (10,000 and 1,000 may be rounded).

**Use it:** an estimator reminder: boosting one problem light shifts noise elsewhere; check the whole frame after raising a light's samples. Same idea as in lighting-flag-a-light-with-a-black-blocker-and-balance-per-light-sampling.
