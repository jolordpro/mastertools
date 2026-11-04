---
id: lighting-cycles-render-speedups-measured-in-blender-threshold-bounces-instances
title: One Blender scene's measured speed-ups: noise threshold 0.01 to 0.1 (13:11 to 1:22), bounces 12 to lower (-27%), instances (-75%), persistent data (-1h08 on 240 frames)
domain: lighting
tags: [[render-time, noise-threshold, light-bounces, instancing, persistent-data, cycles, blender, wimpythekat], deep-read]
applies_to: Blender Cycles (principles map to Redshift adaptive error threshold, trace depth, instancing)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-z9qik8fa-Y, src:yt-transcripts]
feeds: [coach, estimator]
conflicts: none
---
Wimpythekat's figures from his own scenes, not a controlled test: GPU on took one scene from 17 hours to 13:11 [00:33-01:04]; noise threshold raised from default 0.01 to 0.1 cut 13:11 to 1:22, with a warning that too high gives smudgy denoise artifacts [01:35-02:38]. These are Cycles numbers. In Redshift the scale differs: 0.05-0.10 is the layout-preview band and finals sit at about 0.003-0.01 (redshift ledger §2, working bands); don't carry Cycles numbers across.; total light bounces from the default 12 down to 8 or 4 cut 1:22 to 1:00 (26.83%), but keep high for window-heavy interiors [02:38-03:39]; Persistent Data keeps the scene data from frame 1, saving 1h08 on a 240-frame (10 s) animation [03:39-04:42]; Alt+D linked duplicates (instances) on a 100-tree forest cut 2:18 to 34.35 s (75.14%) and save memory [04:42-05:42].
The same four levers exist in Redshift: adaptive error threshold, ray depth, instancing and (for animation) re-using scene translation.

**Use it:** In the estimator or advisor, list these as first knobs when a draft is slow; confirm any change on a 640 draft before booking a quality render.
