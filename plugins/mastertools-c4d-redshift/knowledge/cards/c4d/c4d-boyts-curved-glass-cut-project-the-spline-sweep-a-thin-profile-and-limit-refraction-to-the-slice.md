---
id: c4d-boyts-curved-glass-cut-project-the-spline-sweep-a-thin-profile-and-limit-refraction-to-the-slice
title: A cut ring on a glass tube: project a circle spline onto the cylinder, sweep a thin rectangle along it, put refraction only on that slice
domain: c4d
tags: [brock-boyts, project spline, sweep, refraction, boole, glass, render time, c4d, deep-read]
applies_to: Cinema 4D (2014 era)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=27b5cFk-Pjk, src:yt-transcripts]
feeds: [CHECKS, redshift]
conflicts: none
---
Boyts needed a character to cut a perfect circle in curved glass, not flat [13:43-14:50]. He made a circle spline, used Mesh > Spline > Project (works from the current view; the spline and object must be editable with enough points to bend) so the circle wraps the tube [15:20-15:52, 47:32-48:38]. A tiny rectangle about the glass thickness is swept along it for the cut ring [15:52]. All the shots with the cylinder had refraction and blurry reflections, which distorted characters and cost render time; he removed refraction from the tube and put it only on the slice geometry, which kept the thick-glass look and rendered in seconds [16:23-17:25]. The piece that falls out is the same spline used in a Boole, switched on at one frame, so the ring remains [17:25-17:55]. The whole sequence is an illusion made of cuts: slice, poke, break.
Transfers: in Redshift too, give refractive properties to the small piece that needs them, not the whole large vessel; see existing glass depth cards.

**Use it:** Advice for glass shots: limit expensive refraction to the smallest geometry that sells the thickness.
