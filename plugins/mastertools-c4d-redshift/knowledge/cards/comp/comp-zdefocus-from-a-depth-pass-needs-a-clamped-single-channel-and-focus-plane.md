---
id: comp-zdefocus-from-a-depth-pass-needs-a-clamped-single-channel-and-focus-plane
title: Z-defocus from a CG depth pass fails until depth is copied to its own channel, and edge artifacts are fixed by clamping the depth first
domain: comp
tags: [zdefocus, depth pass, clamp, edge artifacts, nuke, vfx vibe, whisper, deep-read]
applies_to: Nuke
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=b0hbVd9aZkA, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Steps given [38:40-44:23]: copy the depth (red channel) into a new "depth" layer, set Z-defocus to use it, then move the focus plane so near and far read as sharp and soft; green and blue stay unused. Edge artifacts appear because the depth values run far above 1, so add a Clamp before defocus. Also: vignette with a radial mask inverted onto a grade [44:23]; a low-opacity heavy blur (about 500) merged over the frame as fog [37:42]; scratches or dirt through an STMap fed from the UV pass [45:29]. Low-confidence beginner session in mixed languages.

**Use it:** When adding DOF in comp, clamp the depth AOV first (see also the existing post-DoF card) and keep the focus plane adjustable.
