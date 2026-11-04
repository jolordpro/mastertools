---
id: broadcast-unreal-56-psd-import-rasterized-layers
title: UE 5.6 imports a layered PSD as rasterized layers into a Material Designer material; live text is not kept yet
domain: broadcast
tags: [unreal, psd import, material designer, photoshop, layers, 5.6, deep-read]
applies_to: Unreal Engine 5.5-5.6 Motion Design
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=QWT8IAUfWSk, src:yt-transcripts]
feeds: []
conflicts: none
---
Speaker is David Grownick, Epic senior product specialist and ex Fox Sports real-time graphics, so vendor view. PSD import [24:42-28:31]: drag a layered PSD in and each element arrives as a rasterized piece; layer effects mostly work but not all are verified; smart objects were not yet tested. Layers can be offset in depth, and the PSD can be dropped into a Material Designer material where each layer stays tweakable and repositionable.
Roadmap: recognise text as text so it can be edited, aiming to save the redo step where design hands a Photoshop file to a graphics operator who must rebuild it [42:38-43:39].

**Use it:** Know this when a client hands over a PSD: layers survive as images only, so text still needs rebuilding.
