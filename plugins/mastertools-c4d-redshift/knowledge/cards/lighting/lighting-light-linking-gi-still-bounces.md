---
id: lighting-light-linking-gi-still-bounces
title: Light linking with exclude still lets excluded objects pick up bounce light from GI
domain: lighting
tags: [light linking, include, exclude, gi, bounce, rim light, shadows, project tab]
applies_to: Redshift
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=t9hy0YCq0I8, https://www.youtube.com/watch?v=kN00Z7UsW5U, src:yt-transcripts, https://www.youtube.com/watch?v=KbuUzj0Yj4A, https://www.youtube.com/watch?v=CNVFYFGW9Qo]
feeds: [redshift, coach]
conflicts: none
---
Light Project tab, include or exclude lists (Maxon [47:41-48:44]; Effectatron: lights set to Include only the product group [D 16:10]). Excluded gummies still got lit through GI bounce off the lit object [48:44].
Adding a new object means adding it to the include list, or placing it inside the included folder [D 16:10].
Question [51:20]: keep shadows from excluded objects while not lighting them. Trainer was unsure; suggested lowering the light's diffuse and reflection, which keeps shadows but not light on the object (not verified). Redshift Live ignores light linking (existing card).

**Use it:** the scene check lists lights with include/exclude lists and warns when a new object sits outside every list and renders unlit.
