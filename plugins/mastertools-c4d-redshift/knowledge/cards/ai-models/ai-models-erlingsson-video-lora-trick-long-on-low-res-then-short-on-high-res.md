---
id: ai-models-erlingsson-video-lora-trick-long-on-low-res-then-short-on-high-res
title: "Erlingsson: for video LoRAs, train about 2,000 steps on low-res clips then about 500 steps on high-res clips for higher-resolution results"
domain: ai-models
tags: [ingi erlingsson, video lora, training steps, low res, high res, wan, resolution, polish, ingi-erlingsson, deep-read]
applies_to: Wan-class video models
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ktSEt_8T9MA, src:yt-transcripts, src:polish-roster]
feeds: [estimator]
conflicts: none
---
He says a trick for video models is to train around 2,000 steps on very low-resolution videos, then around 500 steps on high-resolution ones, which gives much higher resolution results than the mix alone [53:53-54:23].

**Use it:** Try a staged schedule (many cheap low-res steps, few high-res steps) before raising the single-pass resolution.
