---
id: lookdev-bepic-barbule-tubes-and-vex-ribbons-add-soft-feather-detail-under-houdini-procedural
title: bEpic feather close-ups: two ways to add barbules the Houdini feather procedural lacks, widened barb tubes with facing-ratio noise, or VEX-generated ribbons
domain: lookdev
tags: [lookdev, bepic, houdini, feathers, barbules, vex, shading, deep-read]
applies_to: Houdini feather procedural, Karma
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=4D9GDZsCzy0, src:yt-transcripts]
feeds: []
conflicts: none
---
Houdini's feather system keeps feathers condensed (barbs as vectors stored on the shaft) and generates them at render time, which is performant, but it has no barbules, the softer detail beneath [21:36-23:08]. Technique 1, barbule tubes: generate the barbs twice, the second set wider, randomize UV offsets, offset UVs by a facing-ratio mask, sample noise and blend with a facing-ratio remap; softer and detailed, and still performant for big feathers [23:40-25:44]. Technique 2: the procedural's VEX expression parameter is an attribute wrangle at primitive level; a small script made ribbon meshes beside the feathers, randomly rotated outward for light directionality (ostrich feathers are loose), with UVs, noise and bump in shading, used for the closest shots [26:16-27:55].

**Use it:** Near-camera fur or feather needs a second detail layer; start with the cheap shader-only version.
