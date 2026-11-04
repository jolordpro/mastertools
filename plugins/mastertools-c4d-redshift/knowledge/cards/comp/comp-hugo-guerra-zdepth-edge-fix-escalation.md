---
id: comp-hugo-guerra-zdepth-edge-fix-escalation
title: Hugo Guerra: fix z-depth defocus edges in order: edge-extend the pass, then render objects separately, then use deep renders with a deep-aware bokeh
domain: comp
tags: [hugo guerra, z-depth, defocus, edge extend, deep compositing, pg bokeh, render layers, deep-read]
applies_to: Nuke, VFXforFilmmakers Q&A (2019), guest Hugo Guerra
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=pKfKsUYpk4w, src:yt-transcripts]
feeds: [comp-post-dof, redshift, coach]
conflicts: none
---
Guest Hugo Guerra (ex-head of Nuke at The Mill London, 20 years comp) answered a viewer whose z-depth edges break when one object sits in front of another [46:07]. His order: first edge-extend the depth pass (his own tutorial); if that fails, go back to 3D and render the layers separately, which he says even the Mill does on big jobs. Three characters rendered apart can each get their own z-defocus, with the layers cloned and linked by expressions [46:39, 47:09]. The cleaner route is deep compositing: render deep and use a deep-aware bokeh (he names PG Bokeh) and the edge problem goes away [47:41]. He used deep comp on a Warhammer cinematic and planned a video on it [48:12]. Host Matt agrees with using non-default blur plugins [24:09].

**Use it:** For a Redshift post-DoF pass, name the escalation order: edge fix, then split layers, then deep EXR. Pair with the zone-render fringe card.
