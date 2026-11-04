---
id: gpu-cloud-runpod-2026-network-volume-then-cheap-gpu-install-then-big-gpu
title: RunPod (2026): make a network volume first, install on a cheap GPU, then swap in a big one on the same volume
domain: gpu-cloud
tags: [runpod, comfyui, network volume, pod, gpu swap, cuda 13, jupyter lab, vram, ai art pipeline, deep-read]
applies_to: RunPod web console, ComfyUI template, May 2026
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=FJrxD-BG0pg, src:yt-transcripts]
feeds: []
conflicts: none
---
Order the creator uses [02:36-08:52]: 1) create a network volume (pods alone lose their container data; size can grow, not shrink; pick the data centre because GPU stock differs, he uses a European one). 2) deploy a pod on the volume with the cheapest GPU (RTX A4000) and install ComfyUI, 5 to 10 minutes, billed while installing. 3) stop that pod and deploy a bigger one (RTX 5090) on the same volume, about a minute to start; checkpoints and outputs stay on the volume. Failure points: the CUDA 13 template targets Blackwell cards and may break some custom nodes [04:10]; 24 GB VRAM was not enough for the Flux tool model [06:46]; the volume had to be enlarged to 80 GB for models [05:43-06:15]. Idle pods warn about charges when stopping. Files browsed through Jupyter Lab [05:11]. He claims a sandbox and encrypted volumes for client work [01:03]; not checked.

**Use it:** same shape applies to any pod host (Redshift tests on rented GPUs): keep data on a persistent volume, set up on cheap hardware, rent the big GPU only for the run.
