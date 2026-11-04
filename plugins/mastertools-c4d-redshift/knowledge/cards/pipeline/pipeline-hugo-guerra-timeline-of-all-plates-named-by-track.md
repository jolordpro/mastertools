---
id: pipeline-hugo-guerra-timeline-of-all-plates-named-by-track
title: Build one conform timeline from the raw plates with tracks named by plate type, and convert camera formats to EXR before Nuke
domain: pipeline
tags: [hugo guerra, nuke studio, conform, edl, plates, track naming, clean plate, exr, raw, deep-read]
applies_to: Nuke Studio
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=FW942ZgK8Ic, src:yt-transcripts]
feeds: [pipeline plan, CHECKS]
conflicts: none
---
Hugo Guerra's turning point was getting the actual raw plates through the editor's EDL, not just the graded takes [17:05-17:35]. Compositors usually never see unused takes, clean plates, grain plates or flares, so he met the editor and asked [18:06, 20:09].
He matches the offline, then names each track by plate (background, foreground, extra or clean plate, HDR, green screen, grid) and builds the folder structure from track names: project, shot number, plate type [18:06-21:44]. Lines up speed ramps and slow motion so VFX is not done on frames that get cut [18:37].
He converts camera raw (Blackmagic, Sony) to EXR first, since reading them directly in Nuke often fails on colour space or speed [21:44-22:17]. Keeps stock and B-camera leftovers in bins [22:47].
Transfers: same shot-naming and plate-class discipline for sports packages with camera footage.

**Use it:** Turnover checklist: raw plates, clean plates, EXR conversion, shot names equal to the editor's.
