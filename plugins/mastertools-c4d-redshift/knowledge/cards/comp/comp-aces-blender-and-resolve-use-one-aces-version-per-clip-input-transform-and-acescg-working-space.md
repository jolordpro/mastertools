---
id: comp-aces-blender-and-resolve-use-one-aces-version-per-clip-input-transform-and-acescg-working-space
title: ACES from camera to Blender: same ACES version in Resolve and Blender, set the clip's camera input transform in Resolve, export ACEScg EXR (half, DWAA) for comp or sRGB video for reference, and set Blender's working space to ACEScg
domain: comp
tags: [jacob-zirkle, aces, aces 1.3, aces 2.0, blender, davinci resolve, input transform, acescg, exr, deep-read]
applies_to: Blender 5.0, Resolve, ACES 1.3/2.0
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=P09gBP0swlA, src:yt-transcripts]
feeds: [composition, redshift]
conflicts: none
---
Blender 5.0 view menu holds ACES 1.3 or 2.0; he picks 1.3 because Nuke has it natively, and says use the same version everywhere [00:43-01:35]. Working space (file and sequencer) set from Rec.709 default to ACEScg, applied to nodes; the view is what you see, the working space is the math [01:35-02:05]. Check the footage: natural-looking means sRGB/Rec.709; washed-out is log, e.g. S-Log3 S-Gamut3.Cine [03:09-04:10]. Blender has no camera log spaces, so in Resolve set colour science to ACES with the same version, leave project input blank, put the camera IDT on each clip, output sRGB for an H.264 reference or ACEScg for EXR (RGB half DWAA) [05:44-09:19]. Imported EXR is read as ACEScg; the video as ACES sRGB [10:23-11:56]. Quirk: solid view looks right but rendered view looks too dark unless the clip colour space is ACES sRGB; trust rendered view [09:51-10:23]. Captions mishear ACES as ASUS.

**Use it:** Use as the setup checklist for a Blender or Resolve leg of an ACES pipeline. Overlaps comp-aces-resolve-project-level-input-no-input-transform-for-linear; this adds the Blender side.
