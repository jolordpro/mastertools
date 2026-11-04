---
id: comp-change-an-object-colour-at-the-diffuse-colour-pass-with-a-cryptomatte-matte
title: Recolour an object at the diffuse-colour pass using a cryptomatte matte, not on the finished beauty
domain: comp
tags: [cryptomatte, diffuse color, recolor, transmission tint, visor, comp, deep-read]
applies_to: Fusion cryptomatte node, Blender cryptomatte passes
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=evwUXSqbysQ, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Pick the object by material or asset in a cryptomatte node, output to alpha [13:32]. Use it as a mask on a colour corrector inserted after the diffuse-colour pass; doing it at the very end would tint lighting too [14:02]. The new colour then blends with the sun and shadows correctly [15:03]. For a coloured visor he rendered it on its own view layer, merged it over, and multiplied its colour into the face's transmission-colour pass so a purple visor casts a little pink on the pilot [17:40]. Cheaper than cryptomatte: set object pass index to 1 on the objects and output an Object Index pass [25:32].

**Use it:** when a client asks for a colour change late, edit the colour pass and the right matte, not the final grade.
