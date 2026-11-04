---
id: redshift-volume-gradients-density-tint-anisotropy-and-emission-ramp
title: Redshift volume gradients remap by density (left knot low, right knot high); anisotropy tilts scattering, and emission with a colour ramp turns a cloud into fire
domain: redshift
tags: [volume gradient, anisotropy, emission, color ramp, field tint, backlight, vdb, renderbaron, deep-read]
applies_to: C4D + Redshift (2023 upload, renderbaron)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=_5a-cWSjB7U, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Scatter, absorption and emission each carry a gradient that remaps their coefficient: the left knot affects low-density areas, the right knot high-density areas, and the gradient can also colour the volume [03:50]. A tint field gives density-independent colour [03:50-04:22].
Anisotropy 0 scatters evenly. His wording: a positive value scatters away from the light (a bright fringe, like a sunset), a negative value scatters bluntly back toward the light, useful for backlit shots [04:22-04:52].
Fire: assign the density channel to emission, set scatter and absorption to 1 with the absorption gradient narrowed toward low density, load a flame gradient and set emission mode to colour ramp [04:57-05:39].

**Use it:** backlit clouds and smoke: try positive anisotropy first. Note caption wording on direction is the speaker's; verify in a test.
