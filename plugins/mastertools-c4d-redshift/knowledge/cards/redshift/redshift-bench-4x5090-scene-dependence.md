---
id: redshift-bench-4x5090-scene-dependence
title: Four RTX 5090s took 40.84 s per frame on a different scene, so scene content beats GPU count in time
domain: redshift
tags: [benchmark, 4x rtx 5090, render time, scaling, estimator, irender]
applies_to: Redshift on RTX 5090, 2026
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=9mvpps1TuWg, src:research-youtube]
feeds: [estimator]
conflicts: none
---
150 frames at 1080p took about 1 h 42 m (iRender, 2026-10-01). Because the scene differs from the single-card test, the two cannot show GPU scaling.

**Use it:** key the time model on scene features and log the scene with every timing.
