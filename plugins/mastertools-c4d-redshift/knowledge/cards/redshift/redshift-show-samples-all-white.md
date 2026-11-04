---
id: redshift-show-samples-all-white
title: In Show Samples, all-white pixels mean Max Samples was reached: raise max or raise the threshold
domain: redshift
tags: [show samples, max samples, noise, sampling, diagnosis, render view]
applies_to: Redshift 2026-2027
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Unified+Sampling.html.md, https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Sampling+-+Advanced.html.md, src:research-agency-pipelines, src:research-verticals, src:research-youtube, https://www.youtube.com/watch?v=Uk1_Cwi8BUQ, src:yt-transcripts, https://www.youtube.com/watch?v=kwFwyzjXsdM]
feeds: [draft reader]
conflicts: none
---
Show Samples paints how many samples each pixel used. White everywhere means the cap was hit, so the Max Samples budget is starved. Maxon advises looking at it before changing sampling settings.
Rays are not spread evenly, so it also shows where the cost sits.

**Use it:** the draft reader flags a mostly white Show Samples view as a starved max and proposes the fix with its time cost.
Transcript support: White = hit max samples; aim for grey. (https://www.youtube.com/watch?v=Uk1_Cwi8BUQ [01:04])
Transcript support: white = max samples, black = min samples; example max 64, min 1 (https://www.youtube.com/watch?v=kwFwyzjXsdM [07:00-07:31])
