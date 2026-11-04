---
id: c4d-cache-simulations-before-farm
title: Cache or bake simulations before a multi-machine render; uncached sims can give different frames on different machines
domain: c4d
tags: [simulation cache, bake, render farm, determinism, cloth, dynamics, multiple machines]
applies_to: Cinema 4D 2025
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KnfiJy2ND2o, src:yt-transcripts, https://www.youtube.com/watch?v=1Gtp3BjlTjY, https://www.youtube.com/watch?v=_6toVWN7NMo, https://www.youtube.com/watch?v=dHQWVXWbsEM, https://www.youtube.com/watch?v=TEM9BU-Fp0E]
feeds: [CHECKS farm, shakedown]
conflicts: none
---
Caching also stops C4D recalculating the sim per frame while you work [1:02:21]. Without it, render servers or different laptops give different results per frame; he does not know why [1:02:51].

**Use it:** Fail the farm preflight when simulation tags are not cached.
Transcript support: uncached sims calculate differently per Team Render machine and give errors; also Render Network wizard flags uncached cloth/soft/rigid sims [H7_meR9AGkU 03:08-03:39] (https://www.youtube.com/watch?v=1Gtp3BjlTjY [14:03-15:05])
Transcript support: Starting a render at frame 95 gives a different sim; calculate the cache first, then render from any frame (School of Motion, C4D 2024 rigid body) (https://www.youtube.com/watch?v=_6toVWN7NMo [36:51-37:32])
Transcript support: Run the sim light and cache first; add Cloth Surface and Subdivision after (https://www.youtube.com/watch?v=dHQWVXWbsEM [09:57])
Transcript support: Cloth is cached then baked to point-level animation via Bake Objects, giving a keyed copy that does not need re-simulation (https://www.youtube.com/watch?v=TEM9BU-Fp0E [02:05-03:39])
