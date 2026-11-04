---
id: comp-tanzillo-glowier-sss-pass-painted-into-the-thin-parts
title: For stills, render a pass with lower SSS scale and paint it into thin parts such as fingers and ears
domain: comp
tags: [mike-tanzillo, critique, sss, pass, painting, exposure blending, deep-read, lighting-critique]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=TdTxV_ACVhU, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Mike Tanzillo TdTxV_ACVhU [12:55-14:26], calling it a hacky idea: if the output is a still, render a second pass with lower subsurface scale, which makes the character glowier, and paint that value in comp into fingers, ears and tendrils. A student advised a painted mask. He compares it with photography: shoot many exposures on a tripod and paint in the best one for each area.

**Use it:** Allow a local SSS pass for stills when there is no time for shader masks.
