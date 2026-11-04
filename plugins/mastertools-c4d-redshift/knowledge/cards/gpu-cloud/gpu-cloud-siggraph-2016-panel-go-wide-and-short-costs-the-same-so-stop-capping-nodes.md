---
id: gpu-cloud-siggraph-2016-panel-go-wide-and-short-costs-the-same-so-stop-capping-nodes
title: Kevin Bailey (Atomic Fiction, Conductor): cloud cost is nodes times time, so a short wide render costs about what a long narrow one does, and capping at 100 nodes makes no sense
domain: gpu-cloud
tags: [kevin bailey, atomic fiction, conductor, siggraph 2016, burst rendering, wide and short, deadpool, cloud cost, deep-read]
applies_to: cloud rendering in general, 2016 panel
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hIxnygxsdmc, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
Bailey says the habit from a local farm is to cap how many nodes a job may use. In the cloud a studio that knows the work total should go to something like 2,000 nodes for a shorter time rather than 100 nodes for longer, because the bill is similar [22:34]. Comparing cloud to local cost is hard because you can be as wide and as short as you like and pay only for use; it can cost more or far less depending on how you use it [23:05]. His risk argument: on Deadpool the studio left nearly all rendering to the last month because assets were not final until then, which a fixed local farm could not have absorbed [27:44].
He also makes the case that the benefit is a better creative result and less overtime, more than the cost saving [23:36].

**Use it:** the estimator should show node-hours (cost) next to wall-clock (iteration time) and suggest 'as wide as frames' as the default for a deadline job. For broadcast sports work with late assets, this is the argument for booking cloud capacity at the end, not the start.
