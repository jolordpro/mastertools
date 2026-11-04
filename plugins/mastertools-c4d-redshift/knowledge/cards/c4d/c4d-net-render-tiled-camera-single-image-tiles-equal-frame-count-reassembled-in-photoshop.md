---
id: c4d-net-render-tiled-camera-single-image-tiles-equal-frame-count-reassembled-in-photoshop
title: Old method for splitting one still across machines in C4D: a Tiled Camera expression with N x N tiles, a frame range of 0 to N squared minus 1, and tiles reassembled in Photoshop
domain: c4d
tags: [tiled camera, net render, single frame, tiles, still, legacy, deep-read]
applies_to: Cinema 4D R13-era (video 2011)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=09hP2XAi0Rk, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Load the Tiled Camera preset (Cinema 4D expressions), set Tiles per axis (4 means 16 tiles), drop in the real camera as Reference Camera and tick Use Tiling [13:34-15:43].
Output frame range must be 0 to tiles squared minus 1 (0-15 for 16 tiles); each frame is one tile image [15:39-16:10].
Submit through Net Render (two clients got 0-7 and 8-15), then rebuild in Photoshop at the original render size (1024 x 768 in the demo), tiles placed like a jigsaw [18:14-19:50].
Superseded for Redshift by Team Render still-image rendering (see c4d-redshift-team-render-single-image-since-3-0-14-each-machine-needs-a-licence).

**Use it:** Only for engines with no distributed single-frame mode; check the engine first.
