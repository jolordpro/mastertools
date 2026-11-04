---
id: pipeline-otio-shot-range-use-case
title: OpenTimelineIO has a written use case: read EDL or AAF, compare to the latest take, extend short shots and trim shots more than 12 frames too long (status: planned)
domain: pipeline
tags: [otio, opentimelineio, edl, aaf, shot ranges, handles, cut-aware rendering]
applies_to: OTIO beta 18
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://opentimelineio.readthedocs.io/en/latest/use-cases/animation-shot-frame-ranges.html, https://github.com/AcademySoftwareFoundation/OpenTimelineIO/releases, src:research-vfx-pipelines]
feeds: [cut-aware rendering]
conflicts: none
---
Beta 18 (6 Nov 2025) adds an enabled flag on Effect and per-track and per-clip colour; since beta 17 most adapters ship as separate PyPI packages (OpenTimelineIO-Plugins). OTIO carries cut data only, no media. No cut-aware render tool or savings figure was found.

**Use it:** render the used range plus a chosen handle; re-run on each new cut.
