---
id: c4d-boyts-hand-drawn-shards-wrapped-to-curved-glass-plus-an-invisible-breaker-collider-on-the-character
title: Breaking glass on a cylinder with control: hand-drawn shards, a Wrap deformer, cloth NURBS thickness, and a big collision sphere instead of making the character dynamic
domain: c4d
tags: [brock-boyts, glass break, wrap deformer, cloth nurbs, dynamics, collision, breaker, c4d, deep-read]
applies_to: Cinema 4D (2014 era)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=27b5cFk-Pjk, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
He wanted the break to look exactly as designed, so he drew the crack pattern as a spline, extruded it flat and cut it with the Knife to get a spider crack starting at the centre [18:28-18:59]. Flat shards were bent with a cylindrical Wrap deformer to the tube [19:30-20:01] and given thickness with a Cloth NURBS [20:01-20:35]; the shard meshes are separated, a Dynamics body tag is set on the parent so all children are affected [20:35]. He did not make the character dynamic, to save RAM and time; he added what he calls a 'breaker', a large sphere or circle attached to the body, big enough that every shard is knocked clear with no jitter [20:35-21:38]. The spike arm follows the surface with a null at the body centre (like a moon orbiting), an aim target that follows the cut spline with align to path, and its height animated to touch the glass [21:38-23:16].
Transfers: collision proxies instead of dynamic hero meshes keep sim cost low.

**Use it:** Suggest a proxy collider for sim shots, and bake before render.
