---
id: pipeline-solaris-usd-rop-copy-assets-before-relative-paths-so-the-exported-folder-is-portable
title: Solaris: in the USD ROP's output processors, move copy-all-assets above relative paths so textures land in an assets folder and the whole folder moves anywhere
domain: pipeline
tags: [houdini, solaris, usd rop, output processors, relative paths, copy assets, textures, portable, handoff, deep-read]
applies_to: Houdini Solaris (Sept 2026 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=XUsleR7wJhk, src:yt-transcripts]
feeds: [CHECKS, coach]
conflicts: none
---
The ROP's output processing list runs in order and by default only has "use relative paths". Add "copy all assets to referencing layer directory", then move it up so it runs before relative paths, and name the output subfolder assets [16:07-18:16].
Result: textures from other drives (his test image sat on C) are copied into the export folder, and the shader's path is rewritten to ./assets/..., checked by reading the USDA [18:16-19:22]. Copy the whole folder and nothing is missing [19:22].
Order matters because replacing paths first would leave them pointing at the original place.

**Use it:** an export-to-render-farm rule: copy first, then relativise. Fits a packaging check before a scene leaves the machine.
