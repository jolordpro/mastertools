---
id: pipeline-unreal-ocio-config-asset-ndisplay-linear-srgb-to-led-pq
title: Unreal OCIO for nDisplay: add only the needed colour spaces, set Utility Linear sRGB to the LED wall PQ output, repeat on every ICVFX camera, and zero out bloom, vignette and tone curve
domain: pipeline
tags: [[ocio, ndisplay, unreal, config, icvfx, post-process, color-pipeline], deep-read]
applies_to: Unreal Engine 4.27 OpenColorIO plugin
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bh5wD1YapJo, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Epic's steps [07:25-12:49]: first neutralise the post-process volume (bloom true with value 0, vignette intensity 0, tone curve, expand gamut, blue correction off) so no camera look touches the wall content [07:25-07:56]. Show engine and plugin content, copy the supplied OCIO folder (config.ocio plus its LUTs folder together) into the project [08:26-08:57]. Create Miscellaneous, OpenColorIO Configuration, browse to the file, then add each colour space you will use, since Unreal builds shaders for every permutation [09:32-10:10]: source Utility Linear sRGB, destination "Output LED walls PQ" [10:10-11:11]. On the nDisplay config actor enable Viewport OCIO and set source and destination, then repeat for every ICVFX camera component and the outer frustum [11:43-12:49]. A camera colour-transform matrix is a later calibration step, not covered.

**Use it:** The same pattern (explicit source and destination, set per camera/view) applies to any OCIO viewer chain.
