---
id: lighting-rs-lights-before-materials-name-by-position-solo-each-and-lock-render-view-camera
title: Maxon trainer's Redshift light routine: light before materials, name lights by position, solo each, lock the render view to the camera
domain: lighting
tags: [maxon, redshift, light order, area light, target tag, normalize intensity, render view camera, deep-read]
applies_to: Redshift 3.5 in Cinema 4D R26 (2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=RpiCCLHjlWQ, src:yt-transcripts]
feeds: [lighting, coach]
conflicts: none
---
Order: light first, then materials, because changing the light afterwards changes how every material looks and forces rework [18:13-18:44]. Base: dome plus HDRI, then area lights [19:14-19:47].
Area lights: Target tag onto a null so the light always faces it [39:17-40:19]. Intensity 100 was far too bright; she settled on about 10 [40:50-43:00]. Light size changes brightness and shadow softness; Normalize Intensity removes the size effect [41:21-42:28]. She uses a disc rather than a rectangle for fewer harsh lines. She names lights by position (left, right, top) not key/fill/rim, and does more than three [42:59]. Disable the others to see what each does [43:31-44:02]. Tint from a reference board (orange for steampunk).
Camera: create a camera with a Redshift camera tag (80 mm used), pick it in the render view dropdown so the view stays locked while lights are moved in a free viewport [46:10-47:43]. Camera menu, Use Camera, Selected Object As Camera lets you look through a light and aim it [47:43-48:48, 51:22-51:56]. Group lights and name the null [49:20].

**Use it:** Add to the lighting coach: lock the render view camera before moving lights. Supports lighting-target-tag-null-on-lights and lighting-rs-area-light-size-and-spread-for-falloff.
