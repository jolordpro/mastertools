---
id: comp-grade-before-view-transform-keeps-highlight-rolloff
title: Exposure and saturation changes made before the ACES view transform keep highlight roll-off; push a light up and the red desaturates toward white without clipping
domain: comp
tags: [Zak, i_go_by_zak, ACES, OCIO, exposure, After Effects, highlights, deep-read]
applies_to: After Effects with OCIO plug-in
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=7uY4-bPvRKs, src:yt-transcripts]
feeds: [comp-fix planner, elevate]
conflicts: none
---
Zak: put grade layers (exposure, hue/saturation) above the ACEScg input and below the output transform, so the extra light feeds ACES and is then compressed to sRGB [27:19-27:49].
A test shot with coloured lights, taken five stops down to well up, showed the lights desaturate toward white and still show detail [36:06-37:06]. With exposure applied before the transform the edge of an eraser stayed visible over a stop up [26:47].
A little saturation goes a long way in this space, with gradations kept [28:20]. He suggests masking with object buffers or Cryptomatte to grade single objects [28:20].

**Use it:** Comp: order the stack as grade first, view transform last; test a grade by pushing exposure a stop and watching whether highlights roll off or clip.
