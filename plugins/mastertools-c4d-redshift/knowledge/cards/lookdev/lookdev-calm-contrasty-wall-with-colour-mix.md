---
id: lookdev-calm-contrasty-wall-with-colour-mix
title: Calm a contrasty textured wall by mixing its base colour map with a solid warm colour at about half, then turn the normal down
domain: lookdev
tags: [[wall material, color mix, texture contrast, normal strength, uv repeat, displacement, redshift, greyscalegorilla, chad ashley], deep-read]
applies_to: Cinema 4D with Redshift
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=nwBpkCPFG0s, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
Chad Ashley's wall fix in a desk scene [50:00-52:04]: repeat the UVs (tile of 4), skip displacement ("dumb it down"), then pipe the texture's base colour through a Color Mix node against a light warm solid (about 75% white plus warm) at roughly 0.5 mix, then back into the material colour. The mix washes out some texture contrast but keeps the tooth.
The normal strength went down so the surface texture would not distract [53:07]. After the wall colour changed (to a light blue, then a warm tone) the coloured accent light had to be retuned, because it conflicted [53:07-53:40].
A shiny desk was fixed the same way in spirit: raise roughness a lot, keep IOR at 1.5, and lower the reflection weight, since his real desk is white and matte [41:34-42:06].

**Use it:** when a background surface fights the hero, the coach can suggest lowering its texture contrast and reflection before changing the light.
