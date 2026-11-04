---
id: c4d-plane-effector-with-a-linear-field-animates-an-object-instead-of-per-channel-f-curves
title: C4D slam animation - put the cube and a Plane effector in a group (Alt-G), set the effector to Object mode and animate one Linear field
domain: c4d
tags: [plane-effector, linear-field, delay-effector, f-curve, animation, non-destructive, cinema-4d-2021, deep-read]
applies_to: Cinema 4D (2021 tutorial, version not stated)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=EszcKrfwQlo, src:yt-transcripts]
feeds: [motion-critique, coach]
conflicts: none
---
Sketchy Visuals, uploaded 2021-02-24.
- Problem: with keyframes, lining up position, rotation and banking curves for one move is tedious. Instead the effector sets the values and a field controls when they apply [00:33-01:35, 09:22].
- Setup: deformation mode must be Object; group the cube and the Plane effector (Alt-G) so the effector affects the cube [04:40-05:44]. Plane Y about 800 to lift it, falloff via a Linear field set to -Y [05:44-06:15].
- The move happens when the field's edge crosses the object; once the field leaves, the cube returns to its true values. Animate the field over about 7 seconds with a slow push to 3.5 s and slam between 3.5 and 5 s [06:15-07:48].
- Inner offset smooths or kills the ease; stop the field just before it starts to affect the object, then shape one f-curve on the field only [08:20-09:54].
- Add small rotation (a Random effector rotated tabs in opposite directions) [07:48]. A Delay effector in Spring mode with the plane in it gives a cartoony bounce; strength must be moderate or it breaks through geometry [10:35-11:03].
- Camera: start the camera move about half a second before the landing (about 4.3 s here), then add a slow push-in by selecting all keys and scaling the curve [11:34-13:24].

**Use it:** A re-timeable impact or slam where the editor can change timing with one curve.
