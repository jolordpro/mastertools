---
id: redshift-openpbr-coat-tints-layers-below-fuzz-is-topmost-darkening-default-1
title: Redshift OpenPBR layer order and coat: Fuzz sits on top of everything, coat colour tints what is beneath it, and coat Darkening defaults to 1
domain: redshift
tags: [openpbr, coat, fuzz, sheen, darkening, layer order, deep-read]
applies_to: Redshift 2025.2.1-2025.4.2, C4D
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ieWk4U63EBw, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
Standard material has coat as the top layer; in OpenPBR Fuzz is the top layer, above coat. Fuzz replaces Sheen, is a new BSDF for microfibre reflection (peach fuzz, textile strands, dust), and stays on top even when coat and specular are raised [08:02-08:32, 12:28-13:32].
Coat differs: with the same 0.3 base roughness and coat weight 1, the two materials look quite different, and OpenPBR's coat influences the base specular roughness more [09:06-10:08].
Coat colour: in Standard it recolours the coat reflections; in OpenPBR coat reflections stay white and the colour tints the layers under the coat [10:08-10:38].
New coat Darkening, default 1, is the physically correct value (a coat darkens what is under it); lower it for art direction [11:17-11:56].

**Use it:** Car paint or lacquered-type work: re-check coat roughness and colour after converting from Standard, and use Darkening to bring the base back up.
