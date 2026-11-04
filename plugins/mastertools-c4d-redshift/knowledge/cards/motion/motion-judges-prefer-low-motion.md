---
id: motion-judges-prefer-low-motion
title: Automated video judges tend to prefer low-motion clips, so a motion score needs a check against that bias
domain: motion
tags: [motion, critique, reward hacking, video judge, bias, low motion]
applies_to: 2025-2026 papers
status: V2
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://arxiv.org/pdf/2511.22974v1, src:research-frontier-ai]
feeds: []
conflicts: none
---
Reward-hacking warning from a search-summary read; also WorldJen (1-5 score with reason) and GT-SVJ judge generated video.
No benchmark tests motion, lighting and continuity critique together.

**Use it:** pair any learned motion score with a measured energy check so calm clips do not win by default.
