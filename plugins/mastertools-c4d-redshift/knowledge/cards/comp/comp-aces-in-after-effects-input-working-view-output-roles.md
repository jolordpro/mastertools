---
id: comp-aces-in-after-effects-input-working-view-output-roles
title: In After Effects ACES, set the engine to OCIO, work in ACEScg, give each clip an input transform, and treat display space as view only
domain: comp
tags: [aces, after effects, ocio, acescg, input transform, display color space, output transform, remember interpretation, deep-read]
applies_to: After Effects 23.2 OCIO/ACES
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=x2sx-P5f-iM, src:yt-transcripts, https://www.youtube.com/watch?v=gSvBBw0k3PU]
feeds: [comp, CHECKS]
conflicts: none
---
Setup [01:03-02:26]: Project Settings, Color, engine OpenColorIO, ACES config, working space ACEScg (linear), display space ACES sRGB. Input transform per clip via Interpret Footage, Color: CG renders use ACEScg; log camera footage uses its camera transform (a GH5 V-Log example); a plain image that must keep its look uses Output sRGB or Output Rec.709 as the input [02:05-02:36]. Set one clip, then use Remember Interpretation and Apply Interpretation for the rest [03:06]. Alternative: Preserve RGB plus an OCIO Color Space Transform effect [03:38-04:09].
Display colour space is only a preview and is never in the export; the project-level value is only the default for new comps, and a linear ACEScg view looks harsh without a view transform [04:09-05:43]. Export two ways: output module Output Color Space set to Output sRGB, or a top adjustment layer with an OCIO transform (ACEScg to Output sRGB) with display space set to None, and then tick Preserve RGB in the output module to avoid doing it twice [06:14-07:48]. To return to the camera's flat profile for a colorist, choose that same input transform as the output transform (Show All lists it) and render EXR or DPX; he exported ACEScg OpenEXR for his own Resolve grade [07:48-08:51].

**Use it:** shakedown or coach check: no double transforms (adjustment layer plus output module plus a non-None display space); supports comp-aces-dont-bake-view-transform.
