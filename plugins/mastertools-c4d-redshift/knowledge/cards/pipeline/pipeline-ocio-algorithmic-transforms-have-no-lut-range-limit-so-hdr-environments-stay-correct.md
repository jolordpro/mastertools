---
id: pipeline-ocio-algorithmic-transforms-have-no-lut-range-limit-so-hdr-environments-stay-correct
title: OCIO v2 algorithmic transforms beat v1 LUTs because LUTs have a finite range; very bright HDR environment values can run off the top
domain: pipeline
tags: [ocio v2, lut, algorithmic, built-in transform, hdr, environment map, accuracy, icc, metal, deep-read]
applies_to: OpenColorIO 2.x
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=FSzLwSTJjWo, src:yt-transcripts]
feeds: []
conflicts: none
---
Answering a Q&A: v2 added operators that implement the maths more precisely than a LUT; the ACES output transforms are more accurate in v2 since v1 used LUTs with a finite range, and an HDR environment map with very bright values could run past the top of the LUT [35:44]. Algorithmic also removes external files, making configs portable, compact and readable [36:15]. No metadata extraction from image files (embedded ICC) in OCIO yet [37:17]. Metal support has no near-term plan; open GitHub issues exist for Metal and CUDA [33:40]. Conformance program for apps is only an idea, after the UX guidelines [31:56].

**Use it:** supports the no-3D-LUT config card with the HDR-overflow reason.
