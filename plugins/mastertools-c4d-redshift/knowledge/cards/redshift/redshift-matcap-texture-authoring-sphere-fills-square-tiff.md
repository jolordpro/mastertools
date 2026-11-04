---
id: redshift-matcap-texture-authoring-sphere-fills-square-tiff
title: Make your own matcap: render a lit sphere that touches all four edges of a square frame (2K, 16 or 32-bit TIFF)
domain: redshift
tags: [matcap, texture authoring, redshift, c4d, tiff, npr, eyedesyn, deep-read]
applies_to: Cinema 4D + Redshift (video July 2023)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=rE_15TwtY5A, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
EJ [18:37-20:51]: build a sphere in a 2K x 2K square comp so it fills the frame edge to edge (no gap, no overflow; use safe-frame opacity to check), apply any look including the Standard renderer cell shader, light it, render a TIFF at 16 or 32 bit. Maxon's own matcaps were TIFFs. A plain grey diffuse sphere works well as a neutral matcap through the ramp, as do halftone dot and line matcaps (they stretch on some models). Photoshop can paint a circle too.

**Use it:** keep a small library of matcaps with a note on which ramp settings suit each.
