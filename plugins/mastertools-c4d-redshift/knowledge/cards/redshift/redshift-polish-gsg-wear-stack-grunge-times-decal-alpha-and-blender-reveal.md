---
id: redshift-polish-gsg-wear-stack-grunge-times-decal-alpha-and-blender-reveal
title: Wear is built by using one grunge map in several places: decal alpha, roughness, bump and a material blender that reveals the paint over metal
domain: redshift
tags: [chad-ashley, greyscalegorilla, wear, decal, material-blender, scratches, deep-read, polish]
applies_to: Redshift in Cinema 4D
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=yFCUHeTf0mQ, src:yt-transcripts, src:polish-roster]
feeds: [lookdev, elevate]
conflicts: none
---
Recipe [06:16-09:51]: split the decal PNG alpha with a color splitter, multiply a crust/grunge map into that alpha, and drop it into a color layer over the base colour, so the sticker looks worn. Then add a material blender: a clamped grunge reveals a white painted material over red; scratches drive both bump and a blend that reveals metal under the paint (a "dropped, scuffed" look); a final subtle dark-grime layer revealed by another grunge map [08:19-09:51]. Use different maps per job and keep dirt subtle.
**Use it:** For a wear/aged look on a hero object, suggest the layer order above and keep each map's strength low; verify it against the Redshift ledger.
