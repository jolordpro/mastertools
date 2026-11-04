---
id: c4d-ocio-convert-scene-only-once
title: Convert a scene to OpenColorIO only once; converting again messes up colour, and materials are not "in ACES space"
domain: c4d
tags: [ocio, convert scene, aces, color management, old scene]
applies_to: Cinema 4D 2024 + OCIO
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [CHECKS 5]
conflicts: none
---
Old basic-colour-management scenes need conversion once; the message appears only then [08:40-09:10]. The trainers call the question "are new materials in ACES" ill-formed, since the setup is about working and display spaces [22:47]. Baking colour into the render differs from keeping data for comp [23:27].

**Use it:** Detect if a scene was already converted before offering conversion.
