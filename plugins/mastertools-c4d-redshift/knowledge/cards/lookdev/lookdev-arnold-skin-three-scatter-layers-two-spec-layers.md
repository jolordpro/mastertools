---
id: lookdev-arnold-skin-three-scatter-layers-two-spec-layers
title: Skin as five layers: shallow, mid and deep scatter plus a blurry and a sharp specular for oily skin
domain: lookdev
tags: [manuel-casasola-merkle, skin, subsurface, specular, arnold, shading, deep-read, polish]
applies_to: Arnold C4DtoA (2015); principle for any SSS renderer
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=sxNf7Ei5Ezc, src:yt-transcripts, src:polish-roster]
feeds: [elevate]
conflicts: none
---
Speaker: Manuel Casasola Merkle. He describes a skin shader as three subsurface layers (the red-blooded flesh, then two skin layers: his terms shallow, mid and deep scatter, tied to dermis, epidermis and the flesh beneath) and two specular layers, because skin is oily: first a blurry spec, then a harsher one [35:58-38:41].
He used a scanned head from a UK photogrammetry studio that came with all the maps, and says even the default colours look photoreal. Because the setup is nodal, it can be altered or replaced with a studio shader [36:28-38:41].

**Use it:** When a skin render looks waxy, check it has more than one scatter depth and both a broad and a tight highlight.
