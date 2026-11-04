---
id: pipeline-nineb-sim-usd-one-time-sampled-file-or-per-frame-and-flush
title: Write one time-sampled USD for a whole range; use a file per frame or 'flush after each frame' when the sim is too large for RAM
domain: pipeline
tags: [nine between, houdini, solaris, usd, simulation, time samples, ram, per frame, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Do not put $F in the name for a normal sim: the single USD file holds all frames [2:08:49-2:09:20]. For big sims a file per frame helps, and 'flush data after each frame' clears memory each frame instead of holding the sequence, avoiding a RAM failure during export [2:09:20-2:10:24]. Read the cache back through a reference node.

**Use it:** A cache publish rule: single file for small FX, per-frame files and flush for heavy ones.
