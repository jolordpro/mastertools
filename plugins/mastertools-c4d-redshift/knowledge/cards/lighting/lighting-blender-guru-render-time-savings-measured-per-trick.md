---
id: lighting-blender-guru-render-time-savings-measured-per-trick
title: Blender Guru's measured render-time savings: thin glass shadow off 66%, noise threshold 0.03 vs 0.01 64%, fast GI 23-77%, instancing up to 95%
domain: lighting
tags: [blender, cycles, render time, noise threshold, fast gi, instancing, camera culling, thin glass, andrew price, blender guru, deep-read]
applies_to: Blender Cycles (2025)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=kIW648Cfo18, src:yt-transcripts]
feeds: [estimator, shakedown]
conflicts: none
---
Andrew Price's list, with the savings he reports on his own test scenes [00:19-07:58]: instance copies instead of duplicating (Alt+D), up to 95% on thousands of copies; camera culling with Simplify, about 30% [01:05]; lower indirect light clamp to tame glass and liquid fireflies, less accurate but fast [01:55]; for window glass untick shadow ray visibility, because thin glass makes no caustics, 66% faster in a classroom scene [02:23]; persistent data so animation frames reuse BVH and shader setup, "one of the biggest" animation optimisations [03:01]; noise threshold 0.03 instead of the 0.01 default gives 64% faster with no perceptible change, higher gives splotchy shadow animation [03:42-04:18]. These are Cycles numbers. In Redshift the scale differs: 0.05-0.10 is the layout-preview band and finals sit at about 0.003-0.01 (redshift ledger §2, working bands); don't carry Cycles numbers across.; textures at 4K not 8K, since 8K loads twice as slow and rarely shows [04:39]; fast GI approximation after 2 bounces 23% faster, after 1 bounce 77% faster but visible [06:07]; GPU only is better than CPU plus GPU when the CPU is slower (6% slower measured) [06:53-07:28]; decimate dense downloaded models, a 0.1 ratio gave 60% faster [07:44]. Each saving is scene-specific.

**Use it:** The principles carry to Redshift: share instances, stop rays at a noise target, cull off-camera, cap texture size, and keep thin glass out of caustics.
