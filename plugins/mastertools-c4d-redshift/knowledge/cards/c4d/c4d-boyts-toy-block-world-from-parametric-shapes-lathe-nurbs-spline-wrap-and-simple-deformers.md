---
id: c4d-boyts-toy-block-world-from-parametric-shapes-lathe-nurbs-spline-wrap-and-simple-deformers
title: Brock Boyts built a whole animated ad from parametric shapes, Lathe NURBS, Spline Wrap and deformers, with no rigs and almost no modelling
domain: c4d
tags: [brock-boyts, spline wrap, deformers, cloner, lathe nurbs, symmetry, bend, bulge, ffd, c4d, deep-read]
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
Only the legs of the cows and horse were modelled; everything else is parametric shapes, Lathe NURBS and wrapped splines [31:54]. Cow animation: Bend deformer for the head dip, a Bulge on the grass in the mouth, a Symmetry tag so both eyes blink, the head's deformer reused on the tail, an FFD box with the middle vertices moving in and out for chewing [32:57-34:31]. The farmer has position and rotation, a Bend for weight shift and a Twist for the spine [35:02]. Roller coaster and traffic: one cart (or colour cube) in a Cloner moving along a track spline, then the whole object deformed along the spline with Spline Wrap; copy the spline three times for three lanes of endless traffic [36:03-38:11]. Scenery pieces are cubes with Taper deformers, symmetry for repeated halves and a Boole for the tunnel [43:54-44:56]. A Loft NURBS gives bevel control by duplicating end circles and shrinking one [45:27].
Water: a plane with high subdivision (he says about 80 to 100), sized only as big as the shot, a Wind deformer for the main wave and two or three tiny-amplitude winds for ripples [51:12-51:44].
Wood: a library of about 10 tileable wood textures with matching bump, scaled consistently [49:39].

**Use it:** Pick this approach for stylised toy looks: fewer assets, deformers over rigs, procedural tiling.
