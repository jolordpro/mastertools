---
id: pipeline-valentic-export-the-look-as-cubes-33-point-for-set-65-point-scene-referred-for-dailies
title: "Valentic's look exports: 33-point cube for on-set monitoring, camera-specific variants, and a 65-point scene-referred cube for dailies and final"
domain: pipeline
tags: [dado-valentic, colourlab, lut, cube, dailies, on-set, whisper, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=JWa0YpS98-w, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
On-set monitoring LUT: 33-point (sets cannot handle 65-point), with the camera's input transform (his example ARRI Log C) and a Rec 709 output [40:44-41:19]. An HDR10 version of the same look; and a B-camera version with its own input transform, since a look defined this way is camera- and display-independent [41:19-43:05].
Dailies cube: 65-point, Log C in and Log C out (scene-referred), so the dailies platform applies display colour management; this same cube also starts the final grade [43:05-44:12].
A full-pipeline LUT (input transform, CDL, printer lights baked in) is exported from the timeline [44:12-45:05].
To export a CDL separately you must start the project in the tool's "standard" mode; switching later deletes work [47:24-48:29]. Set the approved show look as the shot default so dailies always get it [49:01-49:35].

**Use it:** Delivery checklist for looks: size by use (33 on set, 65 for dailies/final), keep dailies scene-referred, name by camera and output.
