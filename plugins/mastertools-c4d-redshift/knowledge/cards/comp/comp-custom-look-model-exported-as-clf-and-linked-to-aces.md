---
id: comp-custom-look-model-exported-as-clf-and-linked-to-aces
title: A custom look model (film print emulation) was authored with meaningful parameters, exported as a portable CLF, and reconciled with ACES 1.3 or 2.0 as a look transform
domain: comp
tags: [[clf, aces look transform, print emulation, film restoration, parameterised model, ocio, studio ghibli, imagica, tomohiro hasegawa, amf], deep-read]
applies_to: OCIO, ACES
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-g6JTD8cge4, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Hasegawa's second case, a 4K restoration of three Studio Ghibli films from old camera-negative scans [10:00-15:45]: the target was the look approved at the first answer print, which came from the whole process from negative to projection, so the team modelled the print stage as a parameterised, film-process-informed model whose controls map to meaningful film-colour behaviour, and checked behaviour at different brightness levels in an internal tool [11:04-13:40].
Inputs were sorted as documented, measured, inferred or creative judgement; a 3x3 mapping from a status-M-like scan to an ADX-like density space was adjusted and encoded as a CLF; reference images and cinematographers' reviews acted as constraints [11:35-12:39].
Later the model became an ACES look transform reconciled with ACES 1.3 or 2.0 display rendering and exported as portable CLF; he stresses this does not mean the whole production used a standard ACES workflow [15:13-15:45].
CLF, AMF and ACES transform IDs communicate version and applied state; he wants evidence and decision provenance recorded too [16:20-16:51].

**Use it:** for house looks, export them as CLF with a note on what evidence supported each parameter, so the look survives a change of software.
