---
id: redshift-area-light-normalize-intensity-and-size-vs-shadow
title: Area light with Normalize Intensity on: size no longer changes brightness, so shadow sharpness is a size choice, not a power choice
domain: redshift
tags: [area light, normalize intensity, shadow softness, light size, ledger-check, lionel, maxon, deep-read]
applies_to: Redshift 3.x in C4D R26 (2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=TonSU8Ljm5c, src:yt-transcripts]
feeds: [lighting, redshift, coach]
conflicts: none
---
With normalize intensity on, scaling the light leaves brightness alone: 5 x 5 cm gave a dense hard shadow, 100 cm almost fill [30:14-31:16]. It killed the light at first, so he raised the intensity value by a factor of ten (and says it should be automatic) [30:15].
A very large light placed close to a small part lost most of its light, because the part is too small relative to the light [31:16-31:48]. He settled on 20 x 20 cm for a sharp key shadow.
After that he balanced by exposure because raw intensity numbers were huge [34:26].

**Use it:** coach: when a light's size is changed and the picture goes dark, check normalize intensity.
