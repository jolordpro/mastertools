---
id: pipeline-usd-variants-hold-only-overrides
title: A USD variant should store only the changed attribute, not the whole material or mesh, and watch which variant you author into
domain: pipeline
tags: [usd, variants, overrides, pixar, george elkoura, scott keating, sidefx, solaris, nested variants, deep-read]
applies_to: USD, Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=TLJPDt4YpYM, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Pixar's George Elkoura: references plus 'overs' change a copy non-destructively, and variants can nest (a shoe style plus a low-complexity version) [03:43-05:47]. Gotcha: the composed stage shows only selected variants, so you can author into a variant when you meant the global level, or the reverse [06:17].
SideFX's Scott Keating keeps variants lean: override only base colour, not the entire material or geometry again, so 15 or 100 variants stay light [14:08-14:39]. Variants can hold anything, including shaders [39:29].

**Use it:** Variants for logo or team-colour looks: store the override, not the asset. Check where an edit lands.
