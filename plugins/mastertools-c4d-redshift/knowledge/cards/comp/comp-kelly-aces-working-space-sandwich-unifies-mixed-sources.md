---
id: comp-kelly-aces-working-space-sandwich-unifies-mixed-sources
title: Wrap the grade between an input transform into ACEScct and an output transform, so Log C and Rec.709 shots respond to the same controls
domain: comp
tags: [aces, acescct, idt, odt, davinci resolve, color management, cullen kelly, mixed sources, deep-read]
applies_to: DaVinci Resolve 17 ACES transform plugin
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=v8P3rshGgdM, src:yt-transcripts]
feeds: [post-composite]
conflicts: none
---
Cullen Kelly [03:42-10:21]: simplest colour management is one transform from the camera space (Alexa) to the display (Rec.709), grading to the left of it. It breaks when a shot comes from another source: his shot 13 was already Rec.709 and needed Rec.709 as the input setting [05:44-06:17]. Grading before the transform means the working space is each shot's own original space (Log C for one, Rec.709 for another), so controls, LUTs and looks act differently per shot [06:48-07:18]. The fix is a "sandwich": input transform (IDT) from camera space to ACEScct, grading in the middle, output transform (ODT) from ACEScct to the display space. The still looks identical to the single transform, but all shots now share one working space and a look can be pasted across them [08:18-10:21]. He builds it with the ACES Transform OpenFX on the colour page, not project settings, so each stage is visible [03:42].

**Use it:** For mixed-source timelines (render + camera plate + stock), always bring each to the common working space before grading or looks.
