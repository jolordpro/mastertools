---
id: gpu-cloud-render-farm-time-math-1500-frames-100-nodes
title: Farm math from a farm explainer: 1 minute at 25 fps is 1,500 frames; at 10 min/frame that is about 10 days on one machine and about 2.5 hours on 100 nodes
domain: gpu-cloud
tags: [render farm, render time, frames, nodes, cost calculator, estimator, 25 fps, deep-read, kent trammell, cg cookie, diy farm, frame time, payback]
applies_to: any renderer
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=SiEclygP_f8, src:yt-transcripts, https://www.youtube.com/watch?v=FNhUnPWzVaw, https://www.youtube.com/watch?v=cm4sPe1nLjU, https://www.youtube.com/watch?v=hIxnygxsdmc]
feeds: [estimator]
conflicts: none
---
A render farm is a data centre of nodes, each with the 3D software, renderer and plugins installed [00:00][01:35]. One second needs at least 25 frames; a minute is 1,500 frames [00:30]. At 10 seconds per frame a machine is busy about 4 hours per minute of film; 30 minutes per frame is described as very common for high quality; at an average 10 minutes per frame one local machine needs about 10 full days [01:02][01:35]. With 100 nodes the same job takes about 2.5 hours (frames render in parallel) [02:06]. Farm owners pay hardware refresh, licences, infrastructure, power, and per-frame software fees; renting passes a small share to the user [02:06][02:40]. Flow: install the farm's plugin, scene is checked and uploaded, distributed, frames download as done, progress viewable online; pricing is credit-based (RenderPoints), with calculators [02:40][03:12]. Service and fairness matter as much as price [03:44]. Promotional explainer.
Merged from `gpu-cloud-farm-math-divide-frames-by-nodes`: Worked example: 1037 frames x 10 min = 10,370 min = 173 h = 7.2 days on one machine; divide by four nodes and it finishes in under two days [00:32-01:04]. His payback claim: a six-node CPU farm (8 cores, 16 GB each) cost under $3,000 in 2019 and paid for itself after two freelance projects [02:07, 01:04]. Prices are dated. Cores matter more than clock for farm rendering, and node boards used onboard graphics, so it was CPU-only [03:42, 04:14]. Tested result: a 48-frame job took about 11 min wall time but about an hour of cumulative node time, roughly one sixth [56:47].

**Use it:** the formula frames x minutes per frame / nodes for the cost estimator's sanity check; ignores upload and queue time.
Transcript support: 2000-frame overnight job on 50 machines versus 2000 nodes finishing in about one frame's time; demo 36 frames on 36 nodes at about 3 min 40 s each (https://www.youtube.com/watch?v=cm4sPe1nLjU [13:40])
Transcript support: Bailey: nodes times time is roughly constant, so go as wide as the frames (https://www.youtube.com/watch?v=hIxnygxsdmc [22:34-23:05])
