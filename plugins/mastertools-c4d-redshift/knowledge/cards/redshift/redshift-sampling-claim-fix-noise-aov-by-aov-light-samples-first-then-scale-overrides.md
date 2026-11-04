---
id: redshift-sampling-claim-fix-noise-aov-by-aov-light-samples-first-then-scale-overrides
title: A creator's Redshift noise routine: preview each AOV, raise dome and area light samples first, then use Sampling Overrides in Scale mode per effect (speaker's claim, check against the ledger)
domain: redshift
tags: [sampling, overrides, aov, dome light, scale, polybox, ledger-check, deep-read]
applies_to: Redshift in C4D, older version (pre-Live), uncertain
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Q5AZ7Xlh2I4, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Speaker's claim: the unified sampler is not what sets image quality; material and light samples do, so leave the sampler default unless there is depth of field, motion blur or another camera effect [01:42-02:14].
Order used: bucket rendering on, DOF and motion blur off, add the scene's AOVs (reflection, refraction, shadows, subsurface, emission) [02:44-04:22]. Fix dome-light noise first by raising its samples, judged on the Shadows AOV but confirmed on Beauty, since Shadows always looks dirtier than the final [04:22-06:30]. Large smooth area lights or tiny lights may need more samples too [05:59].
For reflection, refraction and SSS noise, use Sampling Overrides in Scale mode (multiplies the base, 16 becomes 32 at 2) rather than Replace [08:33-09:03]. Numbers he reached: reflections about 3,200, refractions about 500, with 'ridiculous numbers' sometimes needed [09:34-11:57]. He does not go per material unless rendering hundreds of images [07:01-08:02].
Use the Region (area) render tool on the noisiest patch to save time [14:49].
Ledger note: ledger says per-ray overrides only work with Automatic Sampling off (see redshift-per-ray-overrides); numbers here are one scene's, not a recommendation.

**Use it:** Coach: a sound order of work (isolate AOV, fix light samples, then overrides), but do not quote his sample counts as targets.
