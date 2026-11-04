---
id: redshift-sprite-node-for-leaves-and-proxy-source-kept-in-scene-for-fast-iteration
title: Opacity-heavy foliage rendered in minutes with the Redshift Sprite node (he estimates 20 to 30 min without), and the proxy source stayed in the scene for re-export
domain: redshift
tags: [sprite node, opacity, redshift proxy, foliage, trees, re-export, iteration, inside the mind, deep-read]
applies_to: C4D R20 + Redshift (2019 upload)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cR5PCFKhVJc, src:yt-transcripts]
feeds: [redshift, c4d]
conflicts: none
---
Sprite node: plug the leaf textures into it so cutout leaves are cheap; his claim is that without it the render would take roughly 20 to 30 min on his machine, or might not finish [05:12-06:49]. Opacity-heavy things should use it, by his rule [06:18].
Proxies: keep the original tree in the project, hide from render and viewport, and re-export via File > Export Selected > Redshift Proxy when colours change; the file path list holds earlier proxy versions to swap between [03:40-05:12]. The tree material was darkened by re-rendering just that tree [04:42].

**Use it:** supports `redshift-proxy-display-materials-and-override-settings`; foliage checklist: sprite for alpha, proxy of the hero tree, source kept for edits.
