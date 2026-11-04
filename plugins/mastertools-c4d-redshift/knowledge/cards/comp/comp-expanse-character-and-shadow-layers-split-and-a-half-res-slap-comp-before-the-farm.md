---
id: comp-expanse-character-and-shadow-layers-split-and-a-half-res-slap-comp-before-the-farm
title: Expanse render layers: character and shadow split to avoid DOF edge problems in comp, with a half-res low-sample slap comp checked before the full render
domain: comp
tags: [comp, expanse, render layers, slap comp, dof, nuke, aov, farm, deep-read]
applies_to: Houdini Solaris, Nuke
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
Setup for the mouse film was a character layer with a default AOV set and a shadow layer holding mostly shadows. Splitting them avoids edge issues, since depth of field is done in comp and a combined layer gives bad edges with Nuke's bokeh node [40:51-41:21]. Before the heavy renders go out, a preview slap comp render runs at half resolution with low samples; it finishes quickly on the farm and finds scene faults before render time is wasted [41:21-41:51]. Each Prism render version carries a comment listing the render layers inside, so comp sees what's in it [41:51].

**Use it:** Run a half-res low-sample preview through comp first; list layers in the version comment.
