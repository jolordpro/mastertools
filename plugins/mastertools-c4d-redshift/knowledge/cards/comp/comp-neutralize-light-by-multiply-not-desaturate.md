---
id: comp-neutralize-light-by-multiply-not-desaturate
title: To neutralise a light group, shift its colour with a multiply or pick a white point; desaturating also strips the material colours
domain: comp
tags: [tony lines, white balance, light group, desaturate, white point, nuke, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ZrOiwMSGmIw, src:yt-transcripts]
feeds: [comp, coach]
conflicts: none
---
A light group image contains material colour as well as light colour, so a saturation node desaturates the whole scene [45:11-45:41]. Dividing by the diffuse colour first helps but breaks (specular remains, texture is imperfect), so he does not recommend it [46:13-47:15].
Better: multiply the light group toward neutral by eye, or pick a spot that should be white, then use Gain to restore brightness [47:15-48:17]. Fails when one group mixes several coloured lights [48:17].

**Use it:** Coach tip for LED-wall or colour-cast fixes on a single light group.
