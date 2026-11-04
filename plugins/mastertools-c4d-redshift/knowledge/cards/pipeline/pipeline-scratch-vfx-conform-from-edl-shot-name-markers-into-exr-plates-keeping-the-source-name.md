---
id: pipeline-scratch-vfx-conform-from-edl-shot-name-markers-into-exr-plates-keeping-the-source-name
title: Scratch VFX conform - match the EDL to source clips by timecode and clip name, rename clips from the EDL's locator marker, keep the source name in a Real ID column
domain: pipeline
tags: [scratch, assimilate, edl, vfx-conform, shot-name, dailies, avid, deep-read]
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
Assimilate tutorial (2021) [00:01-07:10]. An Avid EDL lists clip name, source in/out, record in/out, a comment line with the source file name, and a locator holding the VFX shot name.
1. Import clips; in the media browser copy the source name into a Real ID column first (or have the new-timeline dialog do it) [01:39-03:15].
2. Load the EDL, match against the timeline by timecode and clip name; one match per entry expected [03:45].
3. Assemble into a new timeline so the source timeline is untouched; "import comments" brings yellow notes, "import markers" blue notes, but the useful option is the Update Name drop-down with "markers" so each clip takes the VFX shot name [04:18-06:56].
4. The Real ID keeps the link back to the original files.

**Use it:** shot-naming rule: rename to the VFX shot name but keep the original source name as metadata.
