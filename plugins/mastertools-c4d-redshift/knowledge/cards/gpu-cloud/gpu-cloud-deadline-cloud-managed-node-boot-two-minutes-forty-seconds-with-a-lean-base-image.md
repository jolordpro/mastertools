---
id: gpu-cloud-deadline-cloud-managed-node-boot-two-minutes-forty-seconds-with-a-lean-base-image
title: Deadline Cloud service-managed nodes took up to about two minutes to start working; a clean, optimised base image got it to roughly 40 seconds
domain: gpu-cloud
tags: [aws, deadline-cloud, boot-time, base-image, licences, argo-casper, deep-read]
applies_to: AWS Deadline Cloud, webinar uploaded 2025-03
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PjafAJ0-6SA, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
After submitting to the managed queue the job sat at ready while the group grew, an instance came up and a worker went idle; he says plan for up to 2 minutes [47:41-49:46].
He has seen 40 seconds from a lean, well-optimised base image [48:12-48:43].
Managed nodes come with licences pre-installed, so the user does not manage them [47:41].
A trivial hello-world job finished in under a second once running [50:18].

**Use it:** add a fixed 40 s to 2 min start-up per burst in the cost/time estimator and count a saved image as the first optimisation.
