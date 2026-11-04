---
id: redshift-uv-context-output-node-triplanar
title: One UV Context Projection on the Output node retiles or triplanar-blends the whole material at once
domain: redshift
tags: [uv context projection, triplanar, output node, seams, tiling]
applies_to: Redshift 2026.2
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ZAom6DvSi3s, src:yt-transcripts, https://www.youtube.com/watch?v=Xh8A767yA1U]
feeds: [redshift, coach]
conflicts: none
---
Plug it into the Output node's UV context input and it applies to color, normal, displacement together [1:00:06-1:01:40]. Triplanar mode blends seams via axis blend, blend curve and noise, hiding repeats without UV work [55:57-57:30]. Noise textures cannot drive its transform inputs [58:33].

**Use it:** coach: tip for scenes with no or poor UVs.
Transcript support: Second upload; adds shrink-wrap projection, wrap/mirror on U and V, and that noise textures can't drive its inputs but the texture's own scale/offset still can. (https://www.youtube.com/watch?v=Xh8A767yA1U [53:49-1:01:40])
