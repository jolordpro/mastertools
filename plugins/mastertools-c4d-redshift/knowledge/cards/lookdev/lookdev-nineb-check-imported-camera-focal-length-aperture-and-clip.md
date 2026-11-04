---
id: lookdev-nineb-check-imported-camera-focal-length-aperture-and-clip
title: Check imported cameras: Solaris cameras can arrive with absurd focal length (about 5000) or aperture, and a raised near clip cuts the foreground
domain: lookdev
tags: [nine between, houdini, solaris, usd, camera, focal length, aperture, clipping, depth of field, f-stop, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS, shakedown]
conflicts: none
---
A camera placed in Solaris sometimes comes out with a focal length around 5000 and a blown aperture; reset to defaults, 50 mm and 20.955 mm horizontal aperture [2:27:22-2:27:52]. Near clip of 1 m removes everything closer than a metre, which you may want for a leaf in front but not for a normal shot; the far limit rarely matters until about 2000 m [2:27:52-2:28:53].
F-stop 0 turns depth of field off; any value above 0 is used; 1.6-3.2 was good for his small scene. Focus distance is in scene units and a focus plane can be shown and set with a click [2:28:53-2:30:56].

**Use it:** Add a camera sanity check to scene validation: focal length range, sensor size, clip planes, f-stop 0 or not.
