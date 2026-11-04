---
id: ai-models-ai-render-chunking-and-tradeoffs
title: The AI renderer makes about 5 s per run (81 frames per chunk, 11 frames overlapped) and trades control for speed
domain: ai-models
tags: [ai render, chunk, overlap, frames, vram, physics, explore options]
applies_to: Open-source ComfyUI workflow, 2026
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=0WkixvqnPXw, src:yt-transcripts]
feeds: [ai-models plan]
conflicts: none
---
[11:55] A run gives up to 120 frames at 24 fps, about 5 seconds; the advanced version splits long shots into chunks, 41-121 frames, 81 recommended, with 11 last frames as the next start.
[14:00] Ten visual directions in the time of one traditional render, but physics are unsimulated and re-runs are the only fix.

**Use it:** label AI output as a pitch tool, with the caveat about control.
