---
id: pipeline-openusd-26-03-gaussian-splat-particle-field-schema
title: OpenUSD 26.03 adds a native particle-field schema so splats and polygon/PBR geometry share one scene graph
domain: pipeline
tags: [usd, openusd, gaussian splatting, particle field, schema, apple, adobe, nvidia, gltf, khronos, deep-read]
applies_to: OpenUSD 26.03 (Mar 2026)
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=KZqv3Z5rRg8, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
The host announces OpenUSD 26.03 released the day of the stream: a collaboration of Apple, Adobe and NVIDIA that moves splats from a custom plug-in to a native standard via a particle-field schema in the core repo [00:20] [00:51]. Result: polygons with PBR materials and photoreal volumetric splats mix in one scene graph; API schemas favour composition over inheritance [00:51] [01:22]. Sample assets work in usdview [01:22].
Elsewhere: Khronos has a release candidate for a glTF Gaussian-splatting extension (KHR) with ratification hoped for spring 2026; the MPEG and JPEG associations are discussing it too [29:00] [29:30] [30:01]. 3DGRUT can convert a trained PLY to USDZ in one line or export during training; a same-day update added a mesh for collisions, invisible if wanted [26:20] [27:24]. XGrids scanners export USDZ directly [26:53].

**Use it:** Record for pipeline planning: splats can ride inside USD from 26.03. Check actual DCC support (Nuke added native splat support the same week [49:13]).
