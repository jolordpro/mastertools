---
id: pipeline-spring-frame-range-starts-at-101-with-5-frame-handles
title: Spring shot files start at frame 101 for sim pre-roll and add 5-frame handles
domain: pipeline
tags: [pipeline, frame range, pre-roll, handles, 101, simulation, motion blur, shot setup, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=aR3yNNGK_sc, src:yt-transcripts]
feeds: [CHECKS, estimator]
conflicts: none
---
Shot length is copied from the tracker, which reads it from the sequencer; blend files start at frame 101 to leave room to pre-roll simulations [24:27]. A handle of 5 frames is added so edit changes or motion blur at the start do not show a static first frame; characters entering the shot already move [24:27] [24:54].
Compare with pipeline-vfx-frame-count-starts-at-1001, which uses 1001 on film VFX.

**Use it:** Default shot setup: start at 101 (or 1001 on VFX jobs), keep handles of 5 or more, and pre-roll simulations inside the head frames.
