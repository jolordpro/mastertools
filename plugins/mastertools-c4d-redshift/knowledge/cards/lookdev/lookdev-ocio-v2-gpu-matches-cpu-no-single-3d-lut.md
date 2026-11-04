---
id: lookdev-ocio-v2-gpu-matches-cpu-no-single-3d-lut
title: OCIO v2 GPU path runs every operator like the CPU; v1 collapsed the chain into one approximate 3D LUT
domain: lookdev
tags: [ocio, opencolorio, gpu, 3d lut, accuracy, tetrahedral, aces, deep-read]
applies_to: OpenColorIO v2 (2020 preview, feature complete Aug 2020)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=7e0SSka8Ar8, src:yt-transcripts]
feeds: []
conflicts: none
---
Patrick Hodoul (Autodesk): v1 CPU evaluated the operator chain exactly, but the GPU replaced all LUTs with a single 3D LUT, so results drifted [19:49-20:20]. v2 rewrote the GPU renderer to implement all operators; Sony Pictures Imageworks tests showed the v1 CPU-vs-GPU difference image with clear errors and the v2 one black [20:20-20:52]. Any number of LUTs become 1D, 2D or 3D textures [20:52-21:24].
GPU now allows tetrahedral as well as trilinear interpolation [40:50-41:21]. Bitwise equality between CPU and GPU is not possible (floats vary even across GPUs); unit tests compare the two within a threshold [44:58-45:31].

**Use it:** If a viewport or GPU preview disagrees with a CPU render, suspect an old OCIO v1 path that baked everything into one LUT.
