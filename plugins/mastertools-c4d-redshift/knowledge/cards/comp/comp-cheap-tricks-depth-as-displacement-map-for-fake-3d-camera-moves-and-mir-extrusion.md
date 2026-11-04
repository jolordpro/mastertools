---
id: comp-cheap-tricks-depth-as-displacement-map-for-fake-3d-camera-moves-and-mir-extrusion
title: A depth pass as a displacement map gives a fake 3D turn or parallax; soften the depth with a box blur first, or extrude it in Mir for a real camera
domain: comp
tags: [displacement map, depth, parallax, mir, stereo, 2.5d, after effects, deep-read]
applies_to: After Effects, Red Giant Mir
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=-32g9bYyZuc, src:yt-transcripts]
feeds: [comp, motion]
conflicts: none
---
Displacement: both layers in one comp, Displacement Map effect with the depth as map, 'effects and masks' ticked, luminance for both channels, then raise the horizontal amount for a 3D-turn look (used in stereo conversion) [49:52-50:54]. Add Fast Box Blur to the depth layer so edges stretch less, and a small blur on the footage; link x and y displacement to a null's position by expressions to drag the footage around like 3D [50:54-51:24]. Mir extrusion: a solid with Mir, size set to the comp, smooth material, the footage as texture, fractal frequency 1 so no noise, x/y amplitudes 0, and the depth pass as the amplitude layer: the footage is extruded and a real camera can orbit it, zoom changes perspective for a dolly-zoom [51:56-54:32]. Depth Wish has Create Stereo Comp (anaglyph with separation, convergence and depth blur) and Create Mir Comp buttons [54:32-56:09].
Body-horror variant: tint the depth to 50 percent grey, blur horizontally, displace with wiggle(120,50) and Force Motion Blur [56:43-58:20].

**Use it:** Quick parallax or camera-move on a still or a plate when a depth pass exists; blur the depth first.
