---
id: lighting-hdri-key-rim-fill-same-recipe-in-any-renderer
title: The same HDRI, key, rim, fill recipe works across Maya, Blender and Marmoset; rim a bit stronger than fill, fill never beats key
domain: lighting
tags: [hdri, key light, rim light, fill light, agx, punchy, arnold, deep-read]
applies_to: Maya Arnold, Blender Cycles, Marmoset
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=fMV-XUhjw4A, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
Order used in all three apps: lock camera and resolution (2K) first, HDRI for soft ambient and reflection, then key (defines shape and form), then rim (separates silhouette from background), then fill [00:02]. He keeps rim slightly stronger than fill so edges stay readable, and fill only softens shadows and recovers dark detail [01:07]. In Blender he used Cycles over Eevee for realism, AgX colour management and optionally the Punchy look for more contrast [01:39]. In Marmoset he adjusts camera and post (exposure, contrast, bloom, tone mapping) before touching lights [03:13]. Raise samples only as far as needed.

**Use it:** supports the key-rim-fill build order cards; the sample-only-as-needed note matches the quality-versus-time trade.
