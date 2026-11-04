---
id: lighting-octane-area-light-shapes-disc-is-softer-sphere-is-omni
title: Octane area light shape changes the reflection look: disc is rounder and softer, rectangle and disc throw 180 degrees one way, sphere lights all around
domain: lighting
tags: [octane, new-plastic, area light, disc, rectangle, sphere, reflections, deep-read]
applies_to: Octane for Cinema 4D (2022 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=J5KwV7GfbEQ, src:yt-transcripts, https://help.maxon.net/r3d/cinema/en-us/Content/html/Redshift_C4D_Light.html]
feeds: [[redshift, elevate]]
conflicts: [maxon-docs]
---
A light is a Cinema 4D light with an Octane tag; only Details area shape and size matter [04:46]. Disc gives a round highlight, softer reflection edges and less total light because it has less surface area; he uses disc and rectangle most [05:16][05:48]. Sphere, cube and cylinder emit in all directions (sphere like a bulb); a long thin cylinder works as a fluorescent tube [05:16][05:48]. Rectangle and disc emit one way over 180 degrees [05:16]. Power defaults to 100 watts [05:48].

**Use it:** a rule for light shape choice in any engine: pick the shape for the reflection it paints, not only for the spill. Applies to Redshift area lights (rect, disc, sphere, tube).
Maxon check (2026-10-31): CORRECTION for Redshift: the area light shapes are Rectangle, Disc, Sphere and Cylinder. Redshift calls it Cylinder, not tube. (https://help.maxon.net/r3d/cinema/en-us/Content/html/Redshift_C4D_Light.html)
