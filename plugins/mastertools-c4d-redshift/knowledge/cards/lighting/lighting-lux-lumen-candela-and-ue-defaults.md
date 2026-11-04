---
id: lighting-lux-lumen-candela-and-ue-defaults
title: Lux is light arriving on a surface, lumen is light emitted, candela is light per direction; in Unreal only the sun uses lux
domain: lighting
tags: [sean gobi, gameloft, unreal fest, lux, lumen, candela, directional light, albedo, deep-read]
applies_to: Unreal Engine 5
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=nlbJwMoj1Dg, src:yt-transcripts]
feeds: [lighting]
conflicts: none
---
Lux = lumen per square metre falling on a surface; lumen = total light emitted by a source in all directions; candela = light per angle, so a spotlight has more in its cone [04:14-05:47]. Many lights on a surface raise lux while each light's lumen stays the same [04:45].
In Unreal the directional light uses lux because lumen numbers for a sun would need too many zeros; its default 10 lux comes from a white diffuse surface reflecting that illuminance [05:47-07:21].
Local lights use lumen: an interior point light of about 1,000 lumen at 1900 K, a candle-like warm tone [13:34-14:06].

**Use it:** unit glossary for the coach; extends the existing exposure-units card.
