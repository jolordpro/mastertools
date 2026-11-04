---
id: gpu-cloud-unified-memory-cannot-be-upgraded-and-spilling-slows-render
title: Apple Silicon RAM is fixed at purchase, the OS takes part of it, and a scene that does not fit renders much more slowly
domain: gpu-cloud
tags: [unified memory, ram, apple silicon, 8gb, out of core, internal storage, thunderbolt, deep-read]
applies_to: Apple Silicon, Blender
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NktbQIDHvAA, src:yt-transcripts]
feeds: [estimator, redshift]
conflicts: none
---
RAM sits on the chip and cannot be upgraded later [11:36-12:06]; the 8 GB entry mini shares that with macOS (James sees about 2 GB free at startup on his laptop) [12:06-12:38]. When the scene does not fit, Blender on macOS still renders but swaps between RAM and disk and slows a lot [12:38-13:43]. Entry Studio had four times the RAM of the mini [14:13].
Keep scene data on the local disk, since pulling a gigabyte per node over a network share costs time; internal Apple storage is dear (about AU$300 for 256 GB to 512 GB), and Thunderbolt/10 GbE differences matter only if data moves at render time [14:45-16:48, 20:59-22:33].

**Use it:** the advisor should warn that Apple GPU renders spill slowly when the scene exceeds unified memory, and size RAM at purchase time.
