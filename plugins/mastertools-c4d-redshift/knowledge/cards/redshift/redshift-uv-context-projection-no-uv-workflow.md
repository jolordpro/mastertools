---
id: redshift-uv-context-projection-no-uv-workflow
title: UV Context Projection re-projects any texture as triplanar with a real-world size, so a still can skip UV unwrapping
domain: redshift
tags: [uv context projection, triplanar, uv, physical size, texture, node, still]
applies_to: Redshift 2026 (node added about Dec 2025)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=t9hy0YCq0I8, https://www.youtube.com/watch?v=KoL7OAANlJ8, src:yt-transcripts, https://www.youtube.com/watch?v=74lleTzTfC4, https://www.youtube.com/watch?v=u6j9yrpgRhU]
feeds: [redshift, coach]
conflicts: none
---
Add the node by command/ctrl-clicking the UV Context input at the bottom of a texture node [1:03:28]. UV Source Pass-through uses the mesh UVs; overriding the projection to Triplanar ignores them [1:03:58].
A physical size field (cm) scales the texture to the object; 200 cm gave fingerprint smudges that fit a bottle [1:04:29]. It can also go on the Standard Material's Advanced UV Context slot or the output, so one node drives every texture [B 16:23].
Trainer's limit: fine for stills; for animation or simulation textures may slip, so UV unwrap then [1:16:02].

**Use it:** when a texture looks stretched on a still, the coach offers UV Context Projection triplanar before sending the artist to UV; flag it for animated or simulated geometry.
Transcript support: Plugging UV Context into the Standard Material (Advanced) rather than the Output lets one of several stacked displacements keep its own mapping. (https://www.youtube.com/watch?v=74lleTzTfC4 [16:17-18:22])
Transcript support: Camera projection on the material tag flattens an unwrapped model's texture to the lens (https://www.youtube.com/watch?v=u6j9yrpgRhU [16:45-17:16])
