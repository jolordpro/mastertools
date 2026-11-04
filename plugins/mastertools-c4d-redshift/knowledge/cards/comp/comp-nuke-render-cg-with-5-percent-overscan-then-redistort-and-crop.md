---
id: comp-nuke-render-cg-with-5-percent-overscan-then-redistort-and-crop
title: Render CG with about 5% overscan, shrink it to plate size keeping the bounding box, apply the plate's lens distortion to the CG, then crop
domain: comp
tags: [alfie-vaughan, nuke, overscan, lens distortion, redistort, reformat, preserve bounding box, deep-read]
applies_to: Nuke
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=fxfuhl8Q7ys, src:yt-transcripts]
feeds: [composition, CHECKS]
conflicts: none
---
Alfie Vaughan (Nuke tutor, single creator) rendered at 105% of HD so distortion has pixels to pull in [02:05]. Reformat with resize type none and Preserve Bounding Box on keeps the extra pixels as a dashed region outside 1080p [02:35]. Distortion is applied to the CG (undistort off), not removed from the plate [04:40]. Then crop the leftover overscan so Nuke runs faster [05:11].
He calculated distortion with the legacy LensDistortion node (type X, name it, case-sensitive) and line analysis, because the newer node cropped the overscan and had no setting to stop it [03:38]. A lens grid is the most accurate way but is about 12 ft long [03:06]. Group the setup as a backdrop (he labels it rd for redistort) and copy it onto the shadow render [05:11]. Without overscan the pulled-in edges go black.

**Use it:** Add an overscan margin (about 5%) to the turnover spec for CG that will be redistorted; in a comp check, look for missing edges after redistort.
