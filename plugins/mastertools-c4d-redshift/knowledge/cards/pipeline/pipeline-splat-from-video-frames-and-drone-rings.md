---
id: pipeline-splat-from-video-frames-and-drone-rings
title: Splats can be built from every 25th video frame; the result doubles as a camera track and a set survey
domain: pipeline
tags: [gaussian splat, video frames, drone, camera track, set survey, one camera one lens, deep-read]
applies_to: Gaussian splat capture
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=H4LW2fMtSN8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Chris describes taking phone video of a walk-through, keeping one frame per second (every 25th frame at 25 fps), and building a splat; because it is point-based, it can be brought into 3D software, with a camera run through it matching the footage, replacing manual tracking [11:05-11:38]. A drone gives smooth footage; his example splat came from three to four rings of drone passes [12:08-13:11]. Uses named: heritage preservation, directors spinning a set model, seeing time of day and the horizon [13:11-13:42].
For a splat shoot he wants one camera and one lens, kept simple, whereas the photogrammetry rig mixes cropped head cameras with wide body cameras [14:15-14:44]. The rig shoots 200+ stills; check for black or dropped frames before processing [15:47].

**Use it:** an input rule for any scan-based element: one lens, steady path, and a dropped-frame check before the solve.
