---
id: redshift-trace-depth-start-low-noise-means-samples
title: Start trace depth at the bare minimum (about 3) and treat noise as a samples problem, not a bounce problem
domain: redshift
tags: [trace depth, combined depth, bounces, noise, reflection, refraction, volume]
applies_to: Redshift GPU
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=0amlKMClE4s]
feeds: [redshift, coach]
conflicts: none
---
Set reflection and refraction to 3 in the test interior and disable volume, since the scene had none [39:06-39:37]. Combined depth caps the sum, so raise it when raising the others [45:17]. More GI bounces make the scene brighter [46:24].
Rule of thumb from the trainer: grain means samples; missing bounce detail (dark glass, black reflections) means trace depth [41:41, 55:19].

Ledger agrees: §5 "Combined Depth caps the individual reflection and refraction depths".

**Use it:** the advisor decides between 'raise samples' and 'raise trace depth' from the symptom; scene check lists unused ray types still enabled.
