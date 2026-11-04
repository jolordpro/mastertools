---
id: lookdev-tanzillo-hair-too-dark-lift-it-hair-dusty-darken-core-and-add-spec
title: Hair too dark: lift the shader value because light passes into hair. Hair dusty and flat: lower the core diffuse and push spec
domain: lookdev
tags: [mike-tanzillo, critique, hair, specular, subsurface, shader value, deep-read, lighting-critique]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=sjiuEeAp-JE, https://www.youtube.com/watch?v=sCDCs5At8uY, src:yt-transcripts]
feeds: [elevate, redshift]
conflicts: none
---
Two Mike Tanzillo calls with different causes. sjiuEeAp-JE [33:38-34:09] hair dark even on the key side: raise the hair shader value since hair has some subsurface and light penetrates, and too dense a base reads dead.
sCDCs5At8uY [08:32-09:03] hair reads dusty: darken the core diffuse and push specularity, because broad light sources should make spec highlights and the diffuse is flattening it. He also suggested whitening a shirt to separate it from a coat.

**Use it:** Diagnose hair by symptom: dead and dark means lift the base; dusty and flat means darken diffuse, raise spec.
