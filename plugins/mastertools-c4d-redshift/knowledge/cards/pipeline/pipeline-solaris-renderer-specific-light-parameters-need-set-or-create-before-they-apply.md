---
id: pipeline-solaris-renderer-specific-light-parameters-need-set-or-create-before-they-apply
title: Renderer-only light parameters in Solaris (for example Arnold's area-light spread) show greyed 'do nothing' until set to Set or Create, and other renderers ignore them
domain: pipeline
tags: [solaris, usd override, arnold, spread, light parameters, set or create, deep-read]
applies_to: Houdini 18.0 Solaris, 2020
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=lidw4rllGV4, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
A light's parameters include per-renderer tabs; each parameter has a left-hand control showing whether it will be modified, default 'do nothing' [16:07-17:42].
Set it to Set or Create to edit it, which follows USD's concept of override [17:42]. Lowering Arnold's spread focuses an area light into a spot-like square of light; Karma and others ignore this setting [17:42-18:45].

**Use it:** Keep shot looks in the generic parameters; park renderer-only overrides where they are visible.
