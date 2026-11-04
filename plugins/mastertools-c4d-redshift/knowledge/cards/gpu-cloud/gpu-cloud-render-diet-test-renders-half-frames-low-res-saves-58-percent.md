---
id: gpu-cloud-render-diet-test-renders-half-frames-low-res-saves-58-percent
title: Render diet: run FX and lighting tests on every other frame at low res and QC at medium res to use only about 42 percent of a shot's core hours
domain: gpu-cloud
tags: [render footprint, core hours, test renders, every other frame, on tens, iron triangle, vfx, deep-read]
applies_to: any renderer; example is a 90-frame VFX shot
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=FStbueCu1f8, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
A Cup of Joe VFX (render-farm traffic engineer, 12 of 25 years) models one 90-frame shot: effects and lighting are about 99 percent of the 365,000 core hours, so only they are worth pruning [00:34-04:42]. Lighting alone was assumed 16 cores at 16 h per frame. Steps: early tests every other frame (minus 50 percent; big shops use every 10th), also at low res; QC renders full range at medium or low res; finals at full range and full res because artifacts only show there [09:18-11:21]. His model: saves up to 58 percent, leaving 42 percent. Frame count is the biggest cost factor (80 vs 200 frames is about 2.5x) [07:47-08:17]. If tests stay full, the alternative is delivering late and being seen as a fourth-quarter studio [14:59-16:03]. Even a 20-30 percent cut can decide on-prem vs cloud burst [17:06].

**Use it:** A cost estimator or coach can suggest a test ladder (every Nth frame at low res, QC range at medium, finals full) and show the core-hour saving. The numbers come from his own spreadsheet, not measured farm data.
