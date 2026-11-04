---
id: c4d-convert-to-ocio-once
title: 'Convert to OCIO' should be pressed once on an old scene; never twice, and do not merge an unconverted scene afterwards
domain: c4d
tags: [ocio, convert to ocio, colour picker, brand colour, merge, project settings]
applies_to: Cinema 4D 2024 OCIO colour management
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts]
feeds: [CHECKS, lookdev]
conflicts: none
---
It reverse-transforms the colour-chip values in an old scene so they look about the same under OCIO. A second press drifts them further [09:18] [58:40].
New colours in a new project need no conversion [1:30:32]. Convert the two scenes separately, save, then merge, because converting after a merge changes the merged part too [1:31:03-1:32:03].
Brand colours are the hard case: the conversion is an educated guess, not an exact science. Use a calibrated screen and controlled light [1:37:55-1:38:59].

**Use it:** a scene check can warn on an older file with unconverted colours, and the coach must say 'once only'.
