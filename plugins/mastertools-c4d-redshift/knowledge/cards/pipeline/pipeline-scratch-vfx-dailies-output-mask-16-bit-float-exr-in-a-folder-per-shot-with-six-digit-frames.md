---
id: pipeline-scratch-vfx-dailies-output-mask-16-bit-float-exr-in-a-folder-per-shot-with-six-digit-frames
title: Scratch VFX dailies output - OpenEXR 16-bit float, a folder and file name from the clip's source (VFX shot) name, six-digit frame numbers, saved as a file mask
domain: pipeline
tags: [scratch, exr, 16-bit-float, file-naming, output-mask, vfx-plates, deep-read]
applies_to: Scratch (2021)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=pWT2nk1vCt8, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
[07:10-09:34] Configure an Image node to OpenEXR, 16-bit float. Output name uses the source-name token instead of the node name, so each clip renders separately; slash-separated gives a folder named for the shot, inside it files named shot, six-digit frame count, then .exr. More tokens are available. Save the mask template (here "VFX dailies file mask") and reload it in any project. Render includes the source metadata.

**Use it:** the naming pattern for plates: SHOT/SHOT.######.exr.
