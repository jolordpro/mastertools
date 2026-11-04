---
id: ai-models-conditioning-makes-outputs-statistically-unique
title: Stellar's test: depth map plus a trained style LoRA moved outputs into their own cluster away from the base model (FID 100+)
domain: ai-models
tags: [[stellar-creative-lab, human-authorship, lora, depth, copyright, fid], deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bWvxBu_vVes, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Fermi Perumal (head of production technology, Stellar Creative Lab) described a scripted experiment of 12,000 images: A1 base model plus prompt, B same prompt plus human-made conditioning (LoRA style and depth map from a 3D scene), A2 base model plus a detailed prompt written by Florence 2 from a B image [1:30:06-1:31:40].
An FID of 100 or higher marks distinct image populations and theirs showed strong separation; LPIPS plus a t-test gave very low p-values; a t-SNE plot showed B in its own area while A1 and A2 overlapped [1:32:14-1:35:26]. Three trial sets (style, character, city/landscape/portrait).
Point: curated data plus a built 3D world gives something the model cannot make alone, which supports a human-authorship argument. Bert Van Brande stresses a lawyer must make any copyright claim; US Copyright Office gray area [1:28:02][1:55:20].

**Use it:** If a client asks for copyright-safe AI, log the 3D scene, depth passes and trained style as the authored inputs.
