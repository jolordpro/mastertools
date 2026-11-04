---
id: gpu-cloud-5090-redshift-farm-benchmarks
title: iRender 5090 tests: one card 21.3 s/frame on a 301-frame 1080p cloth scene, 4x 5090 40.84 s/frame on another scene
domain: gpu-cloud
tags: [rtx 5090, benchmark, redshift, render time, irender, frame time, octane]
applies_to: RTX 5090, Redshift 2026, Sept-Oct 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PJ3eNgTMNKo, https://www.youtube.com/watch?v=9mvpps1TuWg, https://www.youtube.com/watch?v=u5eoWCQvegI, src:research-youtube]
feeds: [estimator, PLAN 0A]
conflicts: none
---
Test 1: 301 frames at 1920x1080, cloth sim, one 5090: 21.3 s per frame, 1 h 46 m 30 s total, GPU up to 94%. Test 2: 150 frames, 4x 5090: 40.84 s per frame, about 1 h 42 m, a different scene so GPU scaling cannot be read from it.
Test 3: same scene on 4x 5090: Octane 18:13 against Redshift 27:57; the author says it is one scene, not a ranking. All vendor tests with one scene each.

**Use it:** key the time estimate on scene features, not GPU count alone; use test 1 only as an anchor.
