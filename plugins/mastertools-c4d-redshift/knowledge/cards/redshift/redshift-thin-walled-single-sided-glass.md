---
id: redshift-thin-walled-single-sided-glass
title: Single-sided geometry with transmission looks wrong until Thin Walled is switched on
domain: redshift
tags: [thin walled, refraction, transmission, single sided, glass, plastic, ior]
applies_to: Redshift 2026 standard material
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=t9hy0YCq0I8, src:yt-transcripts, https://www.youtube.com/watch?v=Bbj18-933Vg, https://www.youtube.com/watch?v=DmeiTnrqp3I]
feeds: [shakedown, redshift, coach]
conflicts: none
---
A clear-plastic jar modelled as one surface refracted wrongly at first [1:00:19]. In the material's base properties, Thin Walled tells Redshift the mesh is single-sided, so no double-surface refraction is computed [1:00:50].
The trainer set IOR by material (PVC plastic said as 1.575, from memory; captions were clear but treat the number as unverified), then Thin Walled, and the result read as plastic. The library's Clear Glass preset already has base colour off and transmission weight 1.

**Use it:** a scene check can flag transmission materials on open or zero-thickness meshes with Thin Walled off; the coach suggests Thin Walled when the mesh has no volume.
Transcript support: Thin Wall greys out depth and scatter on the Standard material but Extra Roughness still works (https://www.youtube.com/watch?v=DmeiTnrqp3I [05:50-06:22])
