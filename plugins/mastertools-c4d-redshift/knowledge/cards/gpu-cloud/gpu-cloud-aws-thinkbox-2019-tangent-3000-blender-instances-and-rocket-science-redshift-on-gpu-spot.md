---
id: gpu-cloud-aws-thinkbox-2019-tangent-3000-blender-instances-and-rocket-science-redshift-on-gpu-spot
title: AWS Thinkbox 2019: Tangent scaled Blender work to 3,000 concurrent spot instances for Next Gen, and Rocket Science VFX rendered mostly with Redshift on GPU spot for The Expanse
domain: gpu-cloud
tags: [tangent animation, next gen, blender, rocket science vfx, the expanse, redshift, gpu spot, deadline, siggraph 2019, deep-read]
applies_to: AWS Deadline + Redshift on GPU spot, 2019
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=Fl_FdVgp2E0, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Tangent used Deadline and spot to reach 3,000 concurrent instances for Netflix's Next Gen with limited interruptions [11:57-12:29]. Rocket Science VFX used GPUs rather than CPUs on spot, mostly Redshift, and could get the GPU capacity they needed [12:50-13:00]. That freed them to take a second, CPU-based Arnold show on the same Deadline pipeline [13:00-13:31]. The talk gives no GPU prices.

**Use it:** supports the claim that Redshift GPU rendering on AWS spot with Deadline was in production by 2019; for C4D the gaps are the C4D plugin and licence route, not capacity.
