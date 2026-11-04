---
id: ai-models-switchx-mask-plus-one-reference-image
title: SwitchX takes a mask (keep versus replace) plus one reference image; the reference quality sets the result and the mask can be rough
domain: ai-models
tags: [beeble, hoon kim, conrad curtis, siggraph 2026, switchx, reference image, mask, video to video, matte anyone, deep-read]
applies_to: SwitchX (2026)
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=weXc-JGwewo, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Inputs [12:24-12:56]: white mask region is kept and relit, black is replaced; a reference image gives lighting and background. Only one reference image is accepted so it stays exactly the same; to use five characters, composite them into one reference first [38:10-38:40].
Conrad Curtis: the reference image's quality drives the result [37:38]. Masks come from Beeble's semantic mask plus Matte Anyone propagation, or from roto brush or on-set Ultimatte frames [43:00-44:32].
A roto artist called one mask bad, yet the generated shot looked good, so mask accuracy needed is lower than for a normal key [44:32-45:04]. No mask means the whole frame is preserved [58:30].

**Use it:** when planning an AI relight, spend time on the reference frame; a rough mask is acceptable.
