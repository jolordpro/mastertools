---
id: motion-camera-rigs-null-parent-and-bezier-path
title: Spin a camera with a parent null; fly it along a spline with few control points
domain: motion
tags: [camera rig, turntable, null, parent, spline path, bezier, control points, deep-read]
applies_to: Maya demo, applies to any DCC
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=43ID41Jrhjs, src:yt-transcripts]
feeds: [c4d]
conflicts: none
---
For a 360 turntable do not key the camera itself: parent it to a locator/empty/null and animate only the null through 360 degrees on the vertical axis [16:06]. The same null trick moves the camera from one point to another.
To follow a moving subject, parent or constrain the camera to it (a head-cam parented to a face helps lip-sync checks, but is not what the render camera sees) [14:34].
For long travelling moves attach the camera to a curve (motion path): set the front axis correctly, optionally enable banking, and draw the curve with Bezier handles, not a dense hand-drawn line, since a few points are far easier to edit [17:09-18:42].

**Use it:** in C4D the same ideas map to a null with a camera child and an Align to Spline tag (mapping is our inference); prefer few spline points so the move can be revised in notes.
