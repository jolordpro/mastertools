---
id: pipeline-prism-otio-timelines-rebuilt-from-latest-renders-in-a-daily-graph
title: Prism with OpenTimelineIO: an execution graph rebuilds or refreshes an editorial timeline with the latest render versions each day, loaded in Avid or RV
domain: pipeline
tags: [pipeline, prism, otio, openTimelineIO, editorial, review, avid, rv, resolve, deep-read]
applies_to: Prism 2, OpenTimelineIO
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
Richard (Prism founder) shows OpenTimelineIO inside Prism so timelines exchange with Resolve or Avid and Prism versions them [42:27-42:59]. Custom nodes in the execution graph create a timeline, add tracks, add clips and save; so a whole sequence timeline can be built from the latest versions, or an existing timeline refreshed so it can be re-run every day for review [42:59-44:00]. RV's timeline panel lets reviewers reorder versions, switch a clip to another department (e.g. animation playblast), search older versions, and publish a new timeline version, which also goes to Resolve or the Blender sequencer [44:00-45:01].

**Use it:** Automate the nightly cut: a graph that fetches latest approved renders into the reel before dailies.
