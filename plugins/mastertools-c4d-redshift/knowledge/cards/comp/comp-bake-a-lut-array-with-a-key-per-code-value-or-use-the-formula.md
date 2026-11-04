---
id: comp-bake-a-lut-array-with-a-key-per-code-value-or-use-the-formula
title: A 1D LUT array with few keys interpolates linearly and breaks a curve; bake one key per code value (256 for 8-bit, 1024 for 10-bit) or use the formula
domain: comp
tags: [lut, 1d lut, interpolation, bit depth, precision, whisper, deep-read]
applies_to: Nuke, any
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Hlj5ep-85ys, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Perez [46:19-53:17]: an 8-bit LUT array has up to 256 keys; applied to a 10-bit image only a quarter of values are precomputed and the rest are interpolated, losing precision. A three-key array for a power curve (0, 0.5 to 0.25, 1) gives a kinked, non-physical result; the formula is exact at every bit depth. Baking a curve means one key for every value in the target bit depth. A LUT output may exceed 1 (used to store super-white in log files) though the input is normalised 0 to 1. Not every LUT is a transfer function: some convert spaces, some are creative looks, and 1D LUTs act on all channels equally while 3D LUTs mix them.

**Use it:** When exporting a look as a LUT, avoid a sparse table and spot-check mid-tones.
