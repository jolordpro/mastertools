---
id: pipeline-hail-mary-scene-snapshot-database-per-take
title: Snapshot every scene change per take to JSON so any take can be rolled back, because assets change a lot over a long show
domain: pipeline
tags: [michael zaman, connor ling, framestore, project hail mary, scene database, json snapshot, versioning, rollback, props layout, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Aa7UvqgMDKM, src:yt-transcripts]
feeds: []
conflicts: none
---
A tool set recorded a database alongside every take: scene changes were snapshotted and written as JSON capturing every property [23:54].
At turnover there is always a version of that scene to return to, including asset versions; starting a year early meant almost every asset was different by the last shoot, so versioning was heavy [24:24].
Shot-specific art direction (a chair lifted 6 inches for one shot, back for the next) is why a per-take record is needed [23:23].
They also answered only specific questions with the virtual tools; other departments answered the rest [24:57].

**Use it:** Record layout/camera/light state per shot as versioned data so any approved state can be restored and compared.
