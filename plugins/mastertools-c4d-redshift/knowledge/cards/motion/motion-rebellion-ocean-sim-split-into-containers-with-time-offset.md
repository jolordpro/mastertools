---
id: motion-rebellion-ocean-sim-split-into-containers-with-time-offset
title: Split a large water shot into several sim containers, reuse one with a time offset, and keep iterations manageable
domain: motion
tags: [rebellion vfx, evil genius 2, ocean, flip, simulation, containers, houdini, deep-read]
applies_to: Houdini
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NNUtKYRmcjY, src:yt-transcripts]
feeds: []
conflicts: none
---
Alexander studied the shot first (the analysis is as important as the effect). He used procedural ocean tools for distant waves and separate water containers instead of one huge sim, which kept iterations manageable and directable, and let one sim be reused with a time offset between the first and second halves of the shot [26:57-28:00].
The mid-shot transition let him split the task so seams did not need solving all at once [28:00].
Process: collider prep (watertight, converted to volumes), sources, sim, whitewater, meshing [28:00-29:02].

**Use it:** principle for any heavy sim - divide into reusable regions and cut at transitions; transfers to C4D particle or Pyro work in spirit only.
