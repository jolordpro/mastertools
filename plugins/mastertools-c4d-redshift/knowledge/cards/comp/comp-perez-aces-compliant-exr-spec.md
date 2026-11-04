---
id: comp-perez-aces-compliant-exr-spec
title: An ACES-compliant EXR is one frame per file, 16-bit half float, compressed, in ACES2065-1, with no look or display transform baked in, and the metadata flag set
domain: comp
tags: [victor perez, foundry, fmx, aces, exr, delivery, metadata, deep-read]
applies_to: Nuke 13+ ACES
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Y2mcVM8c7cA, src:yt-transcripts]
feeds: [CHECKS, shakedown]
conflicts: none
---
Spec as Perez gives it [25:09-27:43]: one frame per file; RGB or RGBA; mono, stereo or multiview; 16-bit half float, compressed; colour space ACES2065-1 (AP0). No LMT or ODT may be embedded; the only transform allowed is the IDT that got the data in.
It also needs the ACES metadata flag. In Nuke that is one checkbox, but forgetting it is the trap [27:13].
To write one: set the output transform to ACES2065-1 and tick the write-ACES-compliant-EXR box. Data type and compression grey out because Nuke sets them [37:04-38:07].

**Use it:** A delivery check for ACES hand-offs tests bit depth, colour-space tag, the metadata flag and that no look is baked in.
