---
id: comp-render-passes-data-passes-stay-32-bit-and-are-never-filtered-and-albedo-carries-texture-edits
title: Data passes (normals, depth, position) need 32-bit and must not be filtered, blurred, reformatted or transformed; edit texture and colour on the diffuse albedo pass, not on direct and indirect
domain: comp
tags: [pramod-vfx, aov, albedo, data passes, 32 bit, nuke, multipass, deep-read]
applies_to: Nuke, Arnold/Redshift/V-Ray
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=o5jVaCqV9Hw, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Whisper transcript of an accented, partly garbled lesson, so low confidence. Names differ between Arnold, Redshift and V-Ray but diffuse, specular, emission are common; each has its own beauty formula [01:03-01:34]. Diffuse splits into albedo, direct and indirect; change texture or colour on the albedo (multiply/divide), light on direct/indirect [03:19-03:50]. Utility/data passes carry information (not a picture), must render 32-bit, and any filter, reformat, transform or blur changes the pixel data [04:51-05:23].

**Use it:** A QC rule for pass handling in comp. Compare comp-four-pass-categories-material-light-utility-id.
