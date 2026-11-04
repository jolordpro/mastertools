---
id: broadcast-xpression-2018-publish-attributes-so-each-take-can-override-materials-and-transforms
title: XPression (2018): publish an object attribute in Template Links to change image, material or scale per take without cloning the scene
domain: broadcast
tags: [ross xpression, publish object, template links, materials, full screen, sequencer, attribute, take id, lower third, deep-read]
applies_to: Ross XPression (2018)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=VZO7A0F7pZ0, src:yt-transcripts]
feeds: []
conflicts: none
---
For full-screen pictures: instead of one scene per image, turn on publish object for the picture quad and tick the attributes (position, rotation, scale, material) [18:07-18:48]. The sequencer then lets each take pick its own image and transform without affecting others, for example a camera shot at 0.5 scale and a rotated phone picture [18:48-20:25].
The same trick lets one lower-third box switch between blue and red material per take [20:25-21:59]. Materials are like wallpaper for an object; reusing one material across scenes means an edit hits all, so the Material editor warns when shared [03:41-04:44, 25:25].
Layout hygiene: group layers under a master group to move or hide a whole lower third in sync [24:44-25:16]. Effects such as a drop shadow can reorder layers, so fix layer mode afterwards [28:00-29:00].

**Use it:** Use publish-attribute thinking when designing templates: expose only what editors should change.
