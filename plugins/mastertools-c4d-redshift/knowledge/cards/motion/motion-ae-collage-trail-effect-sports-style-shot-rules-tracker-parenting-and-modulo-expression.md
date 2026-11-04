---
id: motion-ae-collage-trail-effect-sports-style-shot-rules-tracker-parenting-and-modulo-expression
title: After Effects collage trail (2023): choose one-direction camera moves, cut out frames with Roto Brush, parent each frame to a tracker and show every Nth with a modulo expression
domain: motion
tags: [after effects, collage trail, sports graphics, roto brush, track motion, parenting, expression, modulo, time remap, espn, nike, deep-read]
applies_to: After Effects (tutorial uploaded 2023-04-22)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=uJor5NsSohk, src:yt-transcripts]
feeds: [motion-critique, elevate]
conflicts: none
---
Creator unnamed; style compared to ESPN and Nike sports-adjacent work [00:02-02:06].
- Shot rules: camera move in one direction (push-in or pan, not whip handheld), subject crossing the frame, and no motion blur because it fights the cutout look [00:33-01:04].
- Time-remap first for slow-motion feel, render, Roto Brush the subject (rough is fine, scrapbook look), export a PNG sequence with alpha [01:04-02:06].
- Track motion, not a 3D camera: position, rotation and scale if the camera moves in z, position only for a pan; pick points near the subject, not distant trees [02:06-02:36].
- Layer order: last image on top when the subject comes toward the camera, bottom when it leaves [03:08]. Each frame is parented to the tracker data at its own frame, with start point set there [03:08-04:12].
- Expression: a Frame Rate slider on the tracking null; layer opacity is 100 when the layer index modulo the slider is 0, else 0, so 1 shows all, 3 every third and so on [04:12-05:45]. Then B&W to colour, posterised wiggle on position, scale and rotation, overlays [06:16-06:47].

**Use it:** A useful sports-promo trick that can be rebuilt as a C4D/AE hybrid; check the modulo expression before rendering long sequences.
