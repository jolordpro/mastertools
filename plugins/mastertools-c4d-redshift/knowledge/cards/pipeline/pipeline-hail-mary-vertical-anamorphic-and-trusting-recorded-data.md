---
id: pipeline-hail-mary-vertical-anamorphic-and-trusting-recorded-data
title: Vertical anamorphic broke automatic lens solves, so recorded camera data replaced camera sheets and the solver as the trusted record
domain: pipeline
tags: [michael zaman, framestore, project hail mary, anamorphic, lens data, 3de, camera sheets, metadata, encoders, tracking, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Aa7UvqgMDKM, src:yt-transcripts]
feeds: []
conflicts: none
---
Main camera was an Alexa 65 (Gen 1) with a vertical anamorphic for space shots; Unreal does not support it, so the team computed a film back and de-squeeze in the opposite direction, giving roughly a 1.43:1 frame [14:03, 14:33].
Camera sheets are rarely trusted unless metadata is encoded in the frame [37:49]. Here, automatic 3D solves in 3DE gave bizarre values, so recorded VCam/Simulcam data (focus, aperture, zoom through encoders) became the trusted truth, handed to trackers with everything else [38:21, 38:51].
The camera tracker also had to calibrate to the entrance pupil (no-parallax point), which a CG pinhole camera lacks [33:43].
Re-housed vintage lenses change focal length with focus, adding more error [35:16].
Transfers: when working with unusual lenses or formats, record lens data live and give it to comp, rather than relying on a solver.

**Use it:** Include lens, focus and film-back data with any camera handoff, and mark which source is the authority when two disagree.
