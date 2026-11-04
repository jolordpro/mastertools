---
id: lighting-eevee-three-point-values-fill-50w-back-100w-with-warm-fill-and-cool-back
title: A Blender three-point starter: area-light key, fill near 50 W and warm, back near 100 W and cool, plus a non-zero world so shadows are not pure black
domain: lighting
tags: [three point lighting, blender, eevee, area light, world strength, track to, cgplus, deep-read]
applies_to: Blender Eevee
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=8hDAGhUJJL0, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
CGplus (Eevee) [3:18-7:38]: Eevee render quality 1024 samples, viewport 256, viewport denoising on [0:34]. Area lights suit indoor, soft shadow; larger size = softer shadow, smaller = clearer [4:22]. Aim every light with a Track To constraint on an empty target [2:42]. Key sits upper right, near the camera direction. Fill: duplicate the key, put it lower on the opposite side at over 90 degrees from the key, about 50 W, bigger, with a little yellow [5:27]. Back light: duplicate, from behind or above, about 100 W, tinted blue [5:58]; it lights the floor too. Triangle in top view [6:34]. With all lights off, the monkey still shows because the world colour is dark grey; world strength 0 gives real black, and the default 1 is used [7:05]. Coordinates were on his blog, not in the video; "no right answer".

**Use it:** A teachable starting rig for new users; remember watts here are Blender units, not comparable to Redshift.
