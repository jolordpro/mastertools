---
id: pipeline-farm-pack-external-files-and-read-per-node-results
title: Pack external files for farm jobs, run a 5-frame test first, and read per-node frame times to find a bad node
domain: pipeline
tags: [kent trammell, cg cookie, render farm, test job, packed textures, chunk size, node timing, deep-read]
applies_to: Blender network render
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=FNhUnPWzVaw, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Start with a tiny job (5 frames, low samples) to confirm every node renders and returns frames [32:46]. Chunk size 2 means each node takes two frames, then asks the master again; keep it small on a short test so every node participates [45:05-45:36].
Reading the monitor: frames 3 and 4 were wrong, and the per-frame view showed they came from the Windows node, which had not found the HDRI path after the file was copied. Packing the HDRI into the file fixed it [51:29-53:34]. The monitor can blacklist a node that keeps failing [41:55].
Timing spread on near-identical hardware: 48 s versus 82 s per frame, and a 2008 laptop at 191 s, so slowest-node frames dominate the wait [48:19, 57:19].

**Use it:** a QC rule for farm output: view the sequence, then trace any bad frame back to its node, and pack or relink assets before queueing.
