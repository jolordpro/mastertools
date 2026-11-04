---
id: redshift-toon-watercolor-camera-projected-wash-texture-and-bleed-shell
title: Redshift Toon watercolor: project a painted texture through the camera, vary it with Jitter, and add a Fresnel-transparent shell behind the model for paint bleed
domain: redshift
tags: [redshift toon, watercolor, camera projection, jitter, halftone, bleed, c4d, greyscalegorilla, deep-read]
applies_to: Cinema 4D + Redshift Toon (video May 2024)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=u6j9yrpgRhU, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
Greyscalegorilla's setup [15:30-31:23]. Texture: copy a watercolor base-colour node into the Toon colour; the model has no UVs, so set the material tag to Camera projection (film aspect changed from 4:3 to 1:1 to match the square wash) so the paint is flat to the lens and swims by design [16:13-17:48]. A Hue shift before a Jitter node (hue about 20, small value variance, change seed until pleasing) varies colour per object [17:48-21:00]. Halftone: a Tone Map Pattern rotated 45 degrees, dot colour 50 percent grey, scale driven by a second clamped noise through Change Range (to about 0.8 range); a second sine-wave pattern blended with Color Layer in Lighten breaks it up [21:00-25:36]. Dropping the material opacity lets detail show through, which sells the painterly look [25:36-26:08].
Bleed: duplicate the geometry through Volume Builder and Volume Mesher, displace it into a blob, put it behind the model with a standard material using the same wash in colour and emission, and a Fresnel driving transparency so only the camera-facing part is opaque [28:05-31:23]. Overlapping edges give artefacts; a smoother proxy shape would be better, and pushing it into the model makes odd harsh lines.
Render prep he used: GI off, bucket quality low, hardware ray tracing off, triangle filter size 2.5 for sharpness, an S-curve in the viewer colour controls [00:33-01:36]. Treat those as his choices for this look, not general settings (ledger-check).

**Use it:** for hand-painted broadcast looks, flat camera-projected paper textures and a soft bleed shell are cheap ways to avoid per-frame texture swimming complaints (or invite them on purpose).
