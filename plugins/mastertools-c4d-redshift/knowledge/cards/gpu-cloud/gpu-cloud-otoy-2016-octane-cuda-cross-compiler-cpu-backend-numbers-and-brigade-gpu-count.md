---
id: gpu-cloud-otoy-2016-octane-cuda-cross-compiler-cpu-backend-numbers-and-brigade-gpu-count
title: OTOY 2016 (Octane): OpenCL dropped for a CUDA cross-compiler; a CPU backend would need a 20-core Xeon for about 50 OctaneBench; Brigade moved from 80 GPUs to one 980
domain: gpu-cloud
tags: [otoy, octane, octanebench, cuda, cpu backend, brigade, real-time path tracing, denoiser, 2016, deep-read, gpu-cloud]
applies_to: Octane 3/4 and Brigade (2016)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=yc6Mfxt9bCc, src:yt-transcripts]
feeds: []
conflicts: none
---
From OTOY's talk [12:03-14:07, 15:35, 20:45-21:56]: the OpenCL port had been built but OpenCL "basically disappeared" as a viable path on the Mac, so OTOY wrote a compiler that takes its CUDA source to other platforms; each new back end costs about two to eight weeks of optimisation.
A CPU back end was promised for people with no GPU; do not expect much: a 20-core Xeon might score about 50 on OctaneBench.
A denoiser demo (16 samples before and after) was shown as a coming plugin; the vendor name is garbled in the captions. Brigade (real-time path tracer) had needed about 80 GPUs, roughly 3,200 OctaneBench units, to render a scene noise-free a year earlier; now one GTX 980 ran it in real time with noise, which they said is a different problem from raw speed. Octane 4 was to merge Brigade interactivity with Octane quality.
Octane scale numbers; do not transfer to Redshift.

**Use it:** background for conversations about benchmark scores and why one engine's points do not convert to another's.
