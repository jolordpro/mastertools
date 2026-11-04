---
id: comp-aces-gamut-compression-only-touches-pixels-outside-colorchecker-safety-gamut
title: ACES gamut compression leaves pixels inside the ColorChecker-24 safety gamut untouched and only pulls out-of-gamut ones in
domain: comp
tags: [aces 1.3, gamut compression, negative rgb, ap1, led lighting, blue light lmt, ocio 2.1, colorchecker, deep-read]
applies_to: ACES 1.3, OpenColorIO 2.1
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=FSzLwSTJjWo, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Carol Payne (OCIO TSC, co-chair of the ACES gamut compression group) at ASWF Open Source Days 2021. Cause: narrowband LED lights (police lights, neon) give very saturated bright colours the camera cannot handle; the problem starts in the input transform to ACES and worsens when converting to the smaller AP1 gamut, showing as negative RGB values that hurt comp and colour [10:35]. The 1.3 algorithm is a smarter successor to the ACES 1.1 blue-light LMT: it compresses only out-of-gamut pixels and leaves anything inside the safety gamut, set by the boundaries of the ColorChecker 24 values, alone [11:38]. Reference implementation by Remi Achard (DNEG); in OCIO it is a fixed function called by a built-in transform, shipping in 2.1 and the new ACES reference config [12:09, 12:41].

**Use it:** the 'negative AP1 values' symptom is a check to name when scanning comped CG with saturated lights; supports the existing RGC card.
