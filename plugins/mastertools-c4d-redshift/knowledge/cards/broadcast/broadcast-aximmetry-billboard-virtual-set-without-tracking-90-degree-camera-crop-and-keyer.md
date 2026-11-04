---
id: broadcast-aximmetry-billboard-virtual-set-without-tracking-90-degree-camera-crop-and-keyer
title: Aximmetry billboard workflow: key a rotated 90-degree camera onto a flat plane, check the matte, place it in 3D
domain: broadcast
tags: [aximmetry, composer, billboard, virtual set, keyer, difference keyer, chroma keyer, matte, 90 degree camera, no tracking, deep-read]
applies_to: Aximmetry Composer (2018)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=IWoq_ezCoTY, src:yt-transcripts]
feeds: []
conflicts: none
---
No-tracking virtual studios place the person on a flat object called a billboard in the 3D set, so it picks up shadow and reflection like any object [08:48-09:20]. Each camera has its own row: input, crop, keyed, mat, final [09:20-10:55].
Rotating the camera 90 degrees gives a standing presenter more resolution for zoom; only suits someone who stays upright and moves little [09:52-10:23]. Crop removes junk from the green area. Two keyers: a difference keyer (pick green, blue or red backdrop, set black level first, then white to fix holes; keep prefilter low) and a chroma keyer (pick hue with a pipette; shift or ctrl averages a bigger patch; hue tolerance, min saturation, min/max brightness) [14:04-18:17]. Shrink and soften cure edge outlines; a dB parameter removes green spill [16:10]. Check the mat view, since holes hide in the colour image [18:49].
Place via numeric transform or by dragging on a second monitor with Edit scene on; scale with the white sphere, not an axis arrow, so the person is not distorted [19:20-20:54]. Copy and paste settings between cameras' identical boxes and save per control board [25:05-26:36].

**Use it:** Use the row order and mat-view check as a keying QC pass in any green-screen virtual set.
