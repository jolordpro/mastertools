---
id: gpu-cloud-zync-2016-keeps-renders-in-a-cloud-bucket-so-nuke-comp-jobs-skip-the-upload
title: Zync (2016): finished frames come back to your folder and also stay in a private cloud bucket, so a cloud comp job does not upload the CG again
domain: gpu-cloud
tags: [zync, nuke, comp, cloud storage, render output, cinema 4d, 3d and 2d workflow, ibc 2016, deep-read]
applies_to: Zync for Cinema 4D and Nuke, 2016
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=aAjOM-JqnHI, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
Each render lands in your local output folder and also in the project's cloud storage bucket, which doubles as an archive for people in other locations [10:00-10:26]. A Nuke comp run on the same service then uses the cloud copies, so none of the CG renders go up again [10:26-10:56]. Prives says the service works best for a combined 3D and 2D workflow, though either alone works [10:56]. Frames download as they finish, not at the end [28:33-29:36].

**Use it:** supports an AE or Nuke comp-on-cloud path: keep the EXR passes where the comp runs, and download only the final.
