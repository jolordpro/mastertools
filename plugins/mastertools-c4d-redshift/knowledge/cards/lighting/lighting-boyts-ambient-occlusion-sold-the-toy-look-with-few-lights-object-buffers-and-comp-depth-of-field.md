---
id: lighting-boyts-ambient-occlusion-sold-the-toy-look-with-few-lights-object-buffers-and-comp-depth-of-field
title: Boyts' render set-up for the toy ad: one sun plus glints, ambient occlusion to sell it, object buffers per light, DOF and chromatic aberration in comp
domain: lighting
tags: [brock-boyts, ambient occlusion, object buffers, depth of field, chromatic aberration, comp, c4d standard, deep-read]
applies_to: Cinema 4D standard render (2014 era)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=27b5cFk-Pjk, src:yt-transcripts]
feeds: [comp, elevate]
conflicts: none
---
Asked about lighting, Boyts says one main sunset light plus a few extra lights for glints and highlights, soft shadows and no very dark shadows; ambient occlusion is what sold the scene because everything is fake and AO adds dark edges where geometry nears itself, with controllable falloff [48:38-49:39]. For comp he creates object buffers per light (two or three lights at most: main and fills), one shadow caster so shadows run the same way in every scene, so he can adjust each in After Effects; he adds chromatic aberration at the screen edge, depth of field from the camera focus with the focus animated for rack focus [49:39-50:41]. A tilt-shift look gave miniature scale, so he separated all passes (AO, specular, bump) for control and used depth of field to direct the eye [51:44-52:46].
Faces: black and white eye and mouth cut-outs animated with masks in After Effects, rendered as a TIFF sequence with alpha and frontal-projected onto the face [51:44].
Transfers: light as few sources as possible, keep AO as a separate pass.

**Use it:** Cross-check against the redshift AO-trap card before suggesting an AO pass.
