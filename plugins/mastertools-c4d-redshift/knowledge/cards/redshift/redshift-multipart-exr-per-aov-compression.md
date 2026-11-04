---
id: redshift-multipart-exr-per-aov-compression
title: Redshift's own multipart EXR output lets each AOV have its own compression and cut one test file from 22 MB to 3 MB
domain: redshift
tags: [multipart exr, direct output, aov, compression, half float, dwa, file size]
applies_to: Redshift in C4D, 2024 era
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts, https://www.youtube.com/watch?v=evwUXSqbysQ, https://www.youtube.com/watch?v=ARykOD6lG3c]
feeds: [estimator, CHECKS]
conflicts: none
---
Tick Multipart EXR in Redshift AOV settings, tick Direct Output on every AOV, untick the C4D multipass save; set half float and DWA [51:47-54:25].
Each AOV then gets its own compression (zip for detail, DWAA or DWAB for simple masks) inside one file, which C4D's Save multipass cannot do [53:20] [57:02].
Test frame: 22 MB (32-bit float, DWAA) became about 3 MB with the same comp [54:57]. Part of that drop is the move to half float, so it is not a pure compression gain.

**Use it:** when writing farm output settings, default to multipart half-float EXR with per-AOV compression and say what changed in file size.
Transcript support: Chad's single multichannel EXR preset: zip, 16 scan lines, half float, alpha on (https://www.youtube.com/watch?v=ARykOD6lG3c [12:33-13:04])
