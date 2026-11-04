---
id: ai-models-relit-live-framediffuser-video-relight
title: Video relighting research: Relit-LiVE (SIGGRAPH 2026) needs no camera poses; FrameDiffuser makes frames from G-buffers plus the previous frame
domain: ai-models
tags: [relit-live, framediffuser, video relighting, g-buffer, controlnet, temporal]
applies_to: 2025-2026 papers
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://arxiv.org/abs/2605.06658, https://arxiv.org/abs/2512.16670, src:research-verticals, https://www.youtube.com/watch?v=u6xhzA40Af0]
feeds: [research track phase 3]
conflicts: none
---
Relit-LiVE predicts the relit video and per-frame environment maps together (repo zhuxing0/Relit-LiVE; licence unconfirmed). FrameDiffuser uses ControlNet plus ControlLoRA, trained per environment, aimed at consumer GPUs; no code link seen.

**Use it:** watch list for time-consistent relighting.
