---
id: pipeline-union-manifest-per-shot-versioned-usd
title: A shot 'manifest' is a versioned ASCII USD hierarchy published to the tracker, previewable in usdview
domain: pipeline
tags: [union vfx, manifest, usd, shotgrid, custom entity, usdview, shot description, deep-read]
applies_to: USD, ShotGrid
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=nUXfEdZ-7Xs, src:yt-transcripts, https://www.youtube.com/watch?v=Dd1eYWpgpkw]
feeds: [pipeline plan]
conflicts: none
---
Union calls its shot or sequence description a manifest [12:01]. It is a hierarchy of ASCII USD files saved beside the scene data, version-controlled: each change makes a new version published to ShotGrid, so any past state of a shot can be restored [12:01-12:32].
It is a custom ShotGrid entity with slots for each data type filled by the normal publishers. A small custom app converts it to USD and a preview button opens usdview, useful for leads and supervisors [17:38, 29:37-30:08].
They plan a standalone Qt app extending usdview to build manifests with a live 3D view [33:14].

**Use it:** Pattern: one versioned text file lists exactly which assets and versions make a shot.
