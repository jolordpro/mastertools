---
id: pipeline-macos-preview-hydra-storm-browses-usd-by-object-name-before-a-dcc-opens-it
title: macOS Preview opens USD scenes instantly (Hydra Storm on Metal), with an object list searchable by name and export of single objects
domain: pipeline
tags: [pipeline, usd, macos, preview, hydra, blender, kitchen set, pixar, usdz, deep-read]
applies_to: macOS Monterey Preview; Blender 3.0 alpha USD import (2021 video)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=3Z4-9qN0KHg, src:yt-transcripts]
feeds: []
conflicts: none
---
Creator video (Blind Sushi, older Blender 3.0 alpha era), low confidence and dated. On macOS Monterey, Preview loads USD quickly using Hydra Storm over Metal, lists the hundreds of objects, lets you search by name (for example "bottle") and export one object as USD [02:06-04:10]. Pixar's Kitchen Set is a good test scene: about 3200 objects and 3 million triangles, loaded in a second in Blender 3.0 alpha, which imports cameras, curves, lights, materials, mesh, volume and UV but exports only basics (no material export yet) [04:44-05:15, 27:18-29:20]. Camera markers (Ctrl+B) bound to cameras export as USD cameras [09:25-10:26]. Apple's USDZ can be inspected in Xcode and exported to USD [29:52-31:00]; extracting loses animation and material links.

**Use it:** Quick-look a USD handoff with Preview before opening it; do not trust Blender USD material export unless rechecked on the current version.
