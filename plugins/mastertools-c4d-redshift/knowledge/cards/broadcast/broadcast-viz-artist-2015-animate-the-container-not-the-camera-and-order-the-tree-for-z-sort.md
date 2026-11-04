---
id: broadcast-viz-artist-2015-animate-the-container-not-the-camera-and-order-the-tree-for-z-sort
title: Viz Artist (about v2.8/3.x, 2015): animate containers, keep the tree in depth order, mind near and far clipping
domain: broadcast
tags: [vizrt, viz artist, container, scene tree, z sort, animation, billboard, near far clipping, window mask, shadow caster, deep-read]
applies_to: Viz Artist (video 2015-09-11, versions mentioned include 2.8)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=lU8HMOSgu6M, src:yt-transcripts]
feeds: []
conflicts: none
---
Omar Yusuf, a Viz-certified beginner tutorial. You animate containers in the tree, not the camera, and he compares a main container to a hand holding the object [20:30-21:35]. Order matters: containers lower in the tree draw nearer, so keep far-to-near order or Z-sort problems appear [22:06-23:07].
Scene settings: rendering near and far clipping have limits around 20,000 units; objects pushed beyond disappear; changing them badly causes Z-sort errors [14:38-16:44]. Keep camera settings default on air screens and use R to reset a parameter [13:36-14:38].
Use objects, not image backgrounds: PNG with alpha as scene background can look fine locally but cause trouble on air [17:14-18:51]. Importing: in v2.8 moving an image in the tree after import could break the scene link; later versions are safer [10:13]. A billboard plugin keeps an element facing camera when the main container rotates [31:44]. Window mask stays fixed to the screen [30:27]. Shadow caster and receiver plugins give a ground shadow [29:39].

**Use it:** If a Viz job is on the table, copy the tree-order and alpha-background cautions into the review checklist.
