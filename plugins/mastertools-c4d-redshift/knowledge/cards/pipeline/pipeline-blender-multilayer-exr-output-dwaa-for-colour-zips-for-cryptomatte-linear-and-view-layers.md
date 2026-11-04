---
id: pipeline-blender-multilayer-exr-output-dwaa-for-colour-zips-for-cryptomatte-linear-and-view-layers
title: Render EXR output set-up: DWAA for beauty, ZIP/ZIPS for cryptomatte, linear Rec.709, separate view layers so one part can be re-rendered
domain: pipeline
tags: [exr, dwaa, zips, cryptomatte levels, view layers, transparent glass, linear rec709, file output, deep-read]
applies_to: Blender 4.x
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=evwUXSqbysQ, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
The Industrial AOV Connector add-on wires file-output nodes automatically [20:49]. Compression: DWAA for colour (tiny files), a lossless setting for data layers, ZIP or ZIPS for cryptomatte, which does not work in other compressions [21:20]. Cryptomatte levels: 2 is the lowest, 6 gives more selection depth but huge files [22:23]. Output colour management should be set to linear Rec.709; other spaces break comp maths [22:53]. Split into view layers (interior, exterior, character); he rendered only the exterior again with clouds in about a tenth of the time [26:36]. To composite glass over a plate, enable both Transparent and Transparent Glass under Film [27:09].

**Use it:** supports the per-AOV compression cards and shows view-layer splitting as a late-fix tool.
