---
id: pipeline-nineb-usd-component-asset-is-geo-layer-material-layer-and-wrapper
title: A component-built USD asset is a small wrapper file that references a geometry layer and a material layer, with slots for proxy, sim proxy and a bounding-box payload
domain: pipeline
tags: [nine between, houdini, solaris, usd, component builder, asset, proxy, payload, thumbnail, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts, https://www.youtube.com/watch?v=jfH7JpjDO_w]
feeds: [CHECKS, coach]
conflicts: none
---
Saving a component writes several files: the asset (1 KB in his test) that just references a Geo layer (203 KB) and a Material layer (6 KB), plus a payload file that stores a bounding box so the asset can be unloaded from the scene [1:05:21-1:06:23]. The asset can carry a render geometry, a low-res proxy for preview and a sim proxy used as collider [1:01:13-1:01:45]. Preview mode switches to proxy, final to the full-res geometry [1:57:32-1:58:33].
Naming that works: call the geometry node '<thing>_variant', the material '<thing>_material_variant' and the output '<thing>_asset' [1:02:15-1:05:21]. A thumbnail can be rendered and saved to show in the asset gallery [1:07:24].

**Use it:** Define an asset spec: render geo, proxy, material layer, thumbnail; make a heavy-scene check flag assets with no proxy.
