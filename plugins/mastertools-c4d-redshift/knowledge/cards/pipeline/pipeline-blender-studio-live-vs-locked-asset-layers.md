---
id: pipeline-blender-studio-live-vs-locked-asset-layers
title: Blender Studio versions an asset by layer: a publish updates every version where that layer is still live, and a new version is made only for breaking changes, which locks the old layers
domain: pipeline
tags: [blender studio, asset pipeline, versioning, task layers, publish, backward compatibility, sprite fright, deep-read]
applies_to: Blender Studio pipeline (2022)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IBTEBhAouKc, src:yt-transcripts]
feeds: [[shakedown, CHECKS]]
conflicts: none
---
Paul (pipeline TD, Blender Studio, 2022 conference talk). An asset is split into task layers (rigging, shading, grooming), each owning a data domain, with dependencies (shading needs rigging objects) [09:42-10:31]. Each layer in each published version is live or locked. Publishing shading updates every version where shading is live (his example: versions 2 and 3), which differs from classic versioning [11:32-12:37]. A new version is created only on a breaking change, such as a rig change that would break animation; creating it locks the rig layer in all older versions so shots on old versions keep the legacy rig but still get shading updates [12:37-13:39]. Rule: one task per layer so artists work in parallel, and always pull other layers from the latest publish before publishing yours [14:11-15:15]. Metadata is a human-readable XML file next to each asset, no external database [16:21]. Merge picks a base container (the task file if the bottom layer is being published, otherwise the publish), duplicates it, and reapplies layers in order [17:57-18:30].

**Use it:** Model for versioning a shared look or graphics package: separate "breaking" changes (new version, lock old) from safe updates (push to all live versions). Check: shots on old versions must not change when a safe update lands.
