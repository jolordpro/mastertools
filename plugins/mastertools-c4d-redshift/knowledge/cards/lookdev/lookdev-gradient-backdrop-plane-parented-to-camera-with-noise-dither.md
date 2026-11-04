---
id: lookdev-gradient-backdrop-plane-parented-to-camera-with-noise-dither
title: A background plane under the camera with a ramp material gives a quick backdrop; add fine noise to kill banding
domain: lookdev
tags: [background, gradient, ramp, color correct, banding, noise, dither, backdrop plane, deep-read]
applies_to: Cinema 4D + Redshift material graph
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=kgZcffv-bZc, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Steps [06:23-10:43]: plane zeroed to the camera, rotated 90 degrees and pushed out so it follows every camera; BG material of a ramp into a colour-correct node into the output; pick a colour like the product's, and set the colour-correct level scale to 2 so the ramp runs from white through the colour to black. Strong colours crushed this way band; fix with a colour-mix node blending the ramp with a very fine procedural noise (overall scale about 0.5, noise contrast 1, lower scale if needed) at a mix of about 0.03; with the denoiser on the stepping disappears [09:04-10:43].
Tilt the plane a little so the gradient is not dead straight [10:43].

**Use it:** for style-frame backdrops, a noise dither at about 0.03 mix is the value to try for banding; Redshift names and values to be confirmed against the ledger.
