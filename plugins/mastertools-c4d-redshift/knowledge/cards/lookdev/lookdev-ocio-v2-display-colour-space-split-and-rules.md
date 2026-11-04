---
id: lookdev-ocio-v2-display-colour-space-split-and-rules
title: OCIO v2 splits scene-to-display into a view transform plus a display colour space, and adds file and viewing rules
domain: lookdev
tags: [ocio, view transform, display colour space, file rules, viewing rules, icc, hdr, deep-read]
applies_to: OpenColorIO v2 (2020 preview, feature complete Aug 2020)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=7e0SSka8Ar8, src:yt-transcripts]
feeds: []
conflicts: none
---
In v1 one colour space did the whole scene-linear to display step. In v2 it can be a view transform to a display reference space, then a display colour space; this matches ACES and HDR television practice and lets you switch displays without inverting a view transform [17:16-18:17]. ICC profiles can be linked so an app can emulate what ICC-based apps show on wide-gamut monitors [18:17-19:18].
Menu control: group colour spaces by category, hierarchical menus, hide spaces you keep but don't offer (the ACES config has over 300). File rules assign default colour spaces by path or extension; viewing rules suggest views for a colour space [16:14-17:16].

