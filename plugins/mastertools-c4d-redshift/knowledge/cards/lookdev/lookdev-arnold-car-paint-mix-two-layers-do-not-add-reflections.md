---
id: lookdev-arnold-car-paint-mix-two-layers-do-not-add-reflections
title: Car paint as two layers: a blurry base and a clear coat, mixed rather than added, so energy is conserved
domain: lookdev
tags: [manuel-casasola-merkle, car paint, layered material, energy conservation, arnold, reflections, deep-read, polish]
applies_to: Arnold C4DtoA (2015); principle for any renderer
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=sxNf7Ei5Ezc, src:yt-transcripts, src:polish-roster]
feeds: [coach, elevate]
conflicts: none
---
Speaker: Manuel Casasola Merkle (Aixsponza). Metallic car paint has a blurry paint coat under a clear gloss coat. He built it as two standard shaders (a base and a gloss layer) combined with a mix node [24:42-26:49].
His warning: people add the reflections on top of each other, but a photon reflected is not left to enter the material, so adding emits more energy than comes in [26:49-27:50].
Adding is only correct if the specular weight is first halved to 0.5, which gives the same result as a 50/50 mix. Save the finished network to the library and reuse it. A single flat colour node feeding four nodes changes all four at once [27:50-28:50].

**Use it:** In a layered material check, flag two reflective layers summed at full weight; blend them or reduce weights so total reflectance stays at or under 1.
