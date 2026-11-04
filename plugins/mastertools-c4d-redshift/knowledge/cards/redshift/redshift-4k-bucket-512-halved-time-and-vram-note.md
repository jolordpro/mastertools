---
id: redshift-4k-bucket-512-halved-time-and-vram-note
title: One 4K test went from 4:48 to 2:26 with a 512 bucket, and 512 wants at least 11 GB of VRAM
domain: redshift
tags: [bucket size, 512, vram, 4k, render time, restart]
applies_to: Redshift GPU (Windows, NVIDIA)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=AFecCpLTUBI, https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=zFBuUVbGli8]
feeds: [estimator, redshift]
conflicts: [transcript-zFBuUVbGli8]
---
Polygon Division: default bucket 128 to 256 saved about 4 s of 21 s, 512 saved 6 s; at 4K output 512 halved 4:48 to 2:26 [J 02:45-04:19]. Advice: restart (not shut down) to clear GPU memory before 512, and have at least 11 GB of VRAM [J 03:15].
Maxon trainer: 128 is the safe default, 256 usually fine, Cryptomatte forces 256 or crashes, and 512 can be slower on complex scenes [C 47:57-49:30, 59:05].

**Use it:** supports the existing bucket-size test card with numbers; keep bucket choice as a measured per-machine setting.
Transcript contradicts: this card says Cryptomatte forces 256 (Maxon trainer); Polygon Division says it dropped to 128 on his GTX 1080 and 2080 setup. Different hardware and VRAM, so likely not a true conflict. (https://www.youtube.com/watch?v=zFBuUVbGli8 [05:17])
