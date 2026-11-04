---
id: pipeline-approve-render-copies-to-shared-then-final-png-plus-audio-mux
title: Approve-and-push copies reviewed renders to shared; the final film is written as a PNG sequence plus separate audio, then muxed
domain: pipeline
tags: [nick alberelli, blender studio, kitsu, editorial, render review, final render, png sequence, mux, flamenco, exr, deep-read]
applies_to: Blender Studio pipeline (2023)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jiXB5X1S1AI, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Alberelli [27:57-36:34]: Flamenco renders a job in chunks across workers, writes image sequence and preview video to a timestamped folder (output path mirrors three levels of folder names). A render-review step then copies the approved preview to the playblast folder and the frames to a frames folder.
The edit can load the image sequence, JPEG for real-time review or EXR for grading; stacking both and toggling works, since the edit is locked by then [34:28, 38:20-39:54].
Final delivery: render the film from the edit as PNG sequence, audio separately, into a deliver folder, then a script muxes them. Late fixes then redo only changed frames [36:02-36:34].

**Use it:** deliver as an image sequence plus audio file so late changes re-render only a few frames.
