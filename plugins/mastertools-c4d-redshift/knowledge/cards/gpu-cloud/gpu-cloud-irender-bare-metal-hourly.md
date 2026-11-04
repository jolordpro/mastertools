---
id: gpu-cloud-irender-bare-metal-hourly
title: iRender rents bare-metal multi-GPU boxes by the hour, e.g. 8x RTX 4090 about $65.60/h, idle billed
domain: gpu-cloud
tags: [irender, remote desktop, bare metal, 4090, 5090, price, idle, idle billing, hourly]
applies_to: prices as of 2026-10
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://irendering.net/cinema-4d-redshift-render-farm/, https://irendering.net/cinema-4d-render-farm-redshift-octane-speed-test-on-8x-rtx-4090-3/, src:research-render-farms, https://www.youtube.com/watch?v=PJ3eNgTMNKo, src:yt-transcripts, https://www.youtube.com/watch?v=RsG8DYWmlM8, https://www.youtube.com/watch?v=EuUroqBPANo]
feeds: [competitor table]
conflicts: none
---
You get a remote machine with 2x, 4x or 8x RTX 4090 or 5090 and 256 GB RAM, open C4D, test in Redshift IPR and render. No queue, no estimator, a written 10-point checklist, idle time billed.
Its Maxon partner claim is unverified, and licensing is not stated on the page.
Merged from `pipeline-irender-remote-machine-model`: Not a queue: the user opens C4D on the box, tests in Redshift IPR, then renders. Options are 2x, 4x or 8x RTX 4090 or 5090 with 256 GB RAM. Preflight is a written 10-point checklist, nothing automatic, and there is no estimator. Licensing is not stated on the page. Trustpilot data looked unreliable.

**Use it:** a different model from queue farms; its main cost risk is idle billing.
Transcript support: Single-5090 package 3i with 256 GB RAM; licence is pulled on the server so none is needed from the user [03:17]. (https://www.youtube.com/watch?v=PJ3eNgTMNKo [10:01])
Transcript support: 2x RTX 4090 server priced 15 points per hour, 10% off for 3-hour blocks (Jul 2026, vendor video) (https://www.youtube.com/watch?v=RsG8DYWmlM8 [01:09-01:44])
Transcript support: billing stops at shutdown; 8x4090 360-frame job used 1 h 21 min, about 71 IR (https://www.youtube.com/watch?v=EuUroqBPANo [03:24])
