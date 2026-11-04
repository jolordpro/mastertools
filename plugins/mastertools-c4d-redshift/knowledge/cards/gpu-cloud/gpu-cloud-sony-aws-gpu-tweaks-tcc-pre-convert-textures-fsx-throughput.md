---
id: gpu-cloud-sony-aws-gpu-tweaks-tcc-pre-convert-textures-fsx-throughput
title: Sony's cloud-render tweaks: TCC driver mode, pre-converted Redshift textures, GPU affinity, max clock, and watching FSx throughput
domain: gpu-cloud
tags: [sony, aws, tcc, wddm, redshift, textures, gpu affinity, fsx, caustics, photon, deep-read]
applies_to: Redshift on AWS p3/g4, Windows (2020)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=kACWEs-XJcI, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
From Andy Taylor's optimisation list [20:43-22:20]: (1) pre-convert textures to Redshift's format before submitting, otherwise every spot node converts them and the lead time adds up; (2) put the NVIDIA Tesla or GRID driver in TCC mode so the card is compute-only and skips WDDM [12:03-12:33, 21:16]; (3) both T4 and V100 default below max clock, so raise clocks; (4) Deadline GPU affinity lets one node take more than one frame and give each a subset of GPUs, using spare CPU headroom; (5) watch FSx throughput in CloudWatch when scaling out, since many nodes read and write at once. Also [18:12-19:00]: frame time includes CPU-only start-up (texture conversion, loading the C4D file, renderer init, some single-threaded), and caustics photon maps can add a minute or more per frame.

**Use it:** Scene-cost checks can count fixed per-frame start-up and caustic photon cost, not only GPU sampling time. Multi-GPU scaling in his 4K test was almost linear in pure GPU time [17:41].
