---
id: comp-c4d-physical-multipass-order-add-or-multiply-per-pass
title: Rebuild the C4D Physical-render beauty in AE: Add most passes, Multiply shadow and occlusion, then compare to the beauty
domain: comp
tags: [multipass, physical renderer, openexr, 32 bit, diffuse, specular, shadow, ambient occlusion, gi, rebuild beauty, deep-read]
applies_to: Cinema 4D Physical renderer to After Effects
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Xvw_vg3YxZA, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
Low confidence: the narration is heavily garbled (81 words per minute); numbers are not stated. Described flow [00:33-07:40]: Physical renderer with GI on a low preset for speed; multi-pass with diffuse, specular, shadow, ambient, caustics, GI, ambient occlusion, reflection and atmosphere; save as OpenEXR to a folder; in After Effects use 32-bit, an sRGB working space with linearize on, then extract each channel with an extractor effect. Blend modes: Add for diffuse, specular, ambient, caustics, GI and reflection; Multiply for shadow and occlusion; atmosphere also treated separately [05:02-06:49]. The rebuilt result is close but not identical to the original beauty, which he accepts [07:40-08:14]. Benefit named: bloom or grade on separate layers [08:14-08:51].

**Use it:** the same Add/Multiply split as comp-ae-aov-stack-order-add-passes-multiply-ao-shadow-adjustment-layer; treat a mismatch with the beauty as expected only when shadow and AO were multiplied.
