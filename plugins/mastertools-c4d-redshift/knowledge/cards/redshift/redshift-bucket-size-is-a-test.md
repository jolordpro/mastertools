---
id: redshift-bucket-size-is-a-test
title: Bucket size is worth testing per machine; a claimed 50 percent saving comes from one scene, and Cryptomatte limits how big it can go
domain: redshift
tags: [bucket size, cryptomatte, speed, polygon division, elly wade]
applies_to: Redshift 2024+
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=AFecCpLTUBI, https://www.youtube.com/watch?v=L4riSkE7FwA, src:research-youtube, https://www.youtube.com/watch?v=wnJGABcUCh0, src:yt-transcripts, https://www.youtube.com/watch?v=Uk1_Cwi8BUQ, https://www.youtube.com/watch?v=s5ElfI1q8uU, https://www.youtube.com/watch?v=zFBuUVbGli8]
feeds: [advisor]
conflicts: none
---
Polygon Division claims 75% faster overall, half from bucket size alone, on one scene and one machine. Maxon's stream shows bucket 512 and a chapter on Cryptomatte limits (48:49). Both are description or chapter evidence only.

**Use it:** try sizes on the 640 px draft and log the winner per machine; do not assume a big bucket is safe with Cryptomatte.
Transcript support: Maxon measured 128 vs 512 on one frame: 3:24 vs 2:02, identical look, GPU-dependent (https://www.youtube.com/watch?v=wnJGABcUCh0 [00:32])
Transcript support: Two creators measured bucket effects; big buckets faster on simple scenes, slower when one region is heavy. (https://www.youtube.com/watch?v=Uk1_Cwi8BUQ [11:38])
Transcript support: larger buckets go faster at the cost of memory; adjust on low-VRAM cards (https://www.youtube.com/watch?v=s5ElfI1q8uU [03:10-03:41])
Transcript support: Cryptomatte job rendered at bucket 128 while beauty ran at 512 on the same machine. (https://www.youtube.com/watch?v=zFBuUVbGli8 [05:17-05:48])
