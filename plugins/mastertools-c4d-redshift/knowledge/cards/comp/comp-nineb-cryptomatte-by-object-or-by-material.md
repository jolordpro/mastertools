---
id: comp-nineb-cryptomatte-by-object-or-by-material
title: Add Cryptomatte per object or per material name: material-based mattes select everything that shares a material
domain: comp
tags: [nine between, houdini, solaris, usd, cryptomatte, masks, aov, hue shift, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS, comp]
conflicts: none
---
Extra render files include cryptomatte object and cryptomatte material name. Each object gets a unique colour; with the material option, anything sharing a material shares a matte [2:35:37-2:37:10]. His example: select all gumdrops with the matte and hue-shift them to green in comp [2:36:09-2:36:40].

**Use it:** Add both crypto types by default on the render; use material IDs for recolouring one finish across several objects.
