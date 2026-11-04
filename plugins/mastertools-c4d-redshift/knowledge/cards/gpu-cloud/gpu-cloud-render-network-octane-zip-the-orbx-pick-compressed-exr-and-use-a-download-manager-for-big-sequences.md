---
id: gpu-cloud-render-network-octane-zip-the-orbx-pick-compressed-exr-and-use-a-download-manager-for-big-sequences
title: Render Network (Octane) 2023: a zipped ORBX uploads and distributes faster; heavy multi-layer EXR sequences need a download manager
domain: gpu-cloud
tags: [render network, octane, orbx, zip, exr, dwaa, multilayer exr, download manager, review frames, brilly, gpu-cloud, deep-read]
applies_to: Render Network web app (Jan 2023), Octane
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=MghPaVl9aM0, src:yt-transcripts]
feeds: [CHECKS, coach]
conflicts: none
---
Brilly [12:07-14:45, 16:19-17:51, 22:33-25:40]: zipping the ORBX as a standard .zip makes upload and node distribution quicker. Output options include PNG, EXR and deep; choose compression (DWAA, DWAB or zip) on EXR or files get very heavy. Multi-layer EXR on long sequences can be heavy to download, so he points to a free download manager recommended by the network's team.
Review step: the job page shows frame progress; open the review view, scroll every frame for missing materials or lighting errors, select bad frames and re-render them (use sparingly), accept the rest, then download the pass you want, such as the denoised beauty [23:05-25:09].
Jobs and scenes stay on the account, so a lost local drive can be re-exported or resubmitted [11:03-12:07].
Bonus: your own GPUs are free for other work while the job runs [19:57-20:28].

**Use it:** farm-side QC step: look at every returned frame before accepting and downloading; plan bandwidth for multi-layer EXR.
