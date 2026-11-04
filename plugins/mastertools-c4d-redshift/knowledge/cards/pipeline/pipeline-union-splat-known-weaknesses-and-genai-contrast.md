---
id: pipeline-union-splat-known-weaknesses-and-genai-contrast
title: 4D splats have no frame-to-frame stability or fixed point count, so Union mitigates with denoise and 2D; it argues splats beat gen-AI on control
domain: pipeline
tags: [gaussian splat, temporal stability, jitter, gen ai, directability, denoise, deep-read]
applies_to: 4D Gaussian splats
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Ybln1zAQDVc, src:yt-transcripts]
feeds: [challenger]
conflicts: none
---
Known limits of animated splats: jitter or noise from frame to frame, and inconsistent point counts that block UV workflows [04:10]. Union's answer is a blend of mature denoisers and 2D techniques across the pipeline, not one fix [04:41]. Schneider calls the process closer to deterministic than gen-AI: long takes will not drift, reverse cars or pop hands [24:52]. Directability: the crowd can be rearranged freely [25:23]. Host opinion (Seymour): control is gen-AI's weak point; treat that as low confidence.

**Use it:** when someone proposes gen-AI for a long shot, ask about drift and re-direction; splats trade look for control.
