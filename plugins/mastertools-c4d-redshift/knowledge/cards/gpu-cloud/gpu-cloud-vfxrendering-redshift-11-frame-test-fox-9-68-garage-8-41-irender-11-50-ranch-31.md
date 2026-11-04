---
id: gpu-cloud-vfxrendering-redshift-11-frame-test-fox-9-68-garage-8-41-irender-11-50-ranch-31
title: VFXRendering's 11-frame Redshift test (Dec 2025): Fox $9.683 in 16 min, GarageFarm $8.41 in 40 min, iRender 4x4090 $11.50 in 23 min, RANCH 14 min 21 s for 26.51 points; RebusFarm could not run
domain: gpu-cloud
tags: [render farm, cost, redshift, fox renderfarm, garagefarm, irender, ranch, rebusfarm, vfxrendering, deep-read]
applies_to: Cinema 4D + Redshift 2026.2.0, test published 2025-12-31
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=mK3nXETuNII, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Test scene: 11 frames, 512 progressive passes, noise threshold 0.005; the caption reads '1920p x 1810p', most likely Full HD [00:00]. Redshift 2026.2.0 [01:47].
Fox Renderfarm: 4090/5090 node, 128 GB RAM, with a 20% extra charge; about 2 hours of node time spread over nodes, 16 min wall clock, $9.683 [01:47-02:48]. GarageFarm: Low priority, 121 GB RAM, nodes A5000/L40S/RTX 4000, about 40 min, $8.41 [02:48-04:24]. iRender: rented 4x RTX 4090 package, 5-7 min boot, 23 min, $11.50; includes a free C4D and Redshift licence [04:24-05:43]. RANCH Computing: Medium priority, 14 min 21 s, 26.51 render points = $31.21 in the narration but shown as 26.51 EUR on the results slide [06:21-07:57].
Verdict from the channel: Fox and iRender best balance; RANCH fastest and dearest; GarageFarm cheapest but slowest [07:57].
Prices are the farms' list rates on the day; the channel is a render-farm review channel (read as a promotional voice).

**Use it:** Cost estimator reference points (our arithmetic): about $0.76-$1.05 per frame on three farms and about $2.84 on RANCH, with wall-clock and price pulling opposite ways.
