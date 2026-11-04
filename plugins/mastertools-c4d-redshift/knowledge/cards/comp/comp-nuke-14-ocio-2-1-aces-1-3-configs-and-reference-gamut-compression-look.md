---
id: comp-nuke-14-ocio-2-1-aces-1-3-configs-and-reference-gamut-compression-look
title: Nuke 14 adds OCIO 2.1, light CG and full studio ACES 1.3 configs, and applies the reference gamut compression through an OCIO Look Transform
domain: comp
tags: [nuke 14, ocio, aces 1.3, reference gamut compression, named transform, config, foundry, deep-read]
applies_to: Nuke 14.0, OpenColorIO 2.1
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=f6-bPIWNdac, src:yt-transcripts]
feeds: [post-composite]
conflicts: none
---
Foundry's Nuke 14.0 release notes [00:04-02:41]: the family moved to OpenColorIO 2.1 for VFX Reference Platform 2022. Two new ACES 1.3 configs: a light CG config for animation without the many camera input transforms, and a full studio config for VFX with live action. A new OCIO Named Transform node (beta) supports standalone transforms with no fixed reference space, e.g. emulating older 1D-curve colour management [01:07-01:39]. The ACES reference gamut compression fixes artifacts from out-of-gamut source values; add an OCIO Look Transform node and the compression loads automatically as the first and only look in the config [01:39-02:11].

**Use it:** For CG-only work pick the CG config; for plate work use the studio one and add the gamut-compress look node when saturated sources clip.
