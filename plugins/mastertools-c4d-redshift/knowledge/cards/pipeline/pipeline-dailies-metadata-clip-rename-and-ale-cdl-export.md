---
id: pipeline-dailies-metadata-clip-rename-and-ale-cdl-export
title: Dailies metadata drives clip names and burn-ins, and exports as ALE-CDL plus a CSV so the grade and notes reach downstream
domain: pipeline
tags: [metadata, ale, cdl, csv, clip rename, burn-in, davinci resolve, dailies, deep-read]
applies_to: DaVinci Resolve
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=uaynELBZdSE, src:yt-transcripts, https://www.youtube.com/watch?v=rgZjL2e8yEg]
feeds: [pipeline design]
conflicts: none
---
Sound takes carry scene, take and comment, which copy into the synced clip; keywords, descriptions and the LUT name (technical tab) are added by hand [12:57][13:28][14:01]. Rename clips in bulk from metadata with a template of variable tokens such as shot_scene_goodtake, agreed with editorial; reel name and file name remain untouched so conform is safe [15:06][16:12]. Auto-sync audio by timecode, or manually by clap frame; if audio drifts, sync on the clapper waveform and link [09:47][10:49]. Exports: ALE-CDL from the timeline carries metadata plus CDL values in the ASC field; Resolve can't read ALEs back, so also export a CSV of media pool metadata for the later conform [27:26][28:30][29:02].

**Use it:** model for a clean turnover: every note, take flag and grade value gets its own field and a file that survives the handoff.
Transcript support: Resolve project setting to use real names from source clip file name, so Avid does not see the camera extension (https://www.youtube.com/watch?v=rgZjL2e8yEg [05:13])
