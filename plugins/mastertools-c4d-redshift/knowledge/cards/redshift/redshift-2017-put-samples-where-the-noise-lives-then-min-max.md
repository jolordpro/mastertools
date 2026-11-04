---
id: redshift-2017-put-samples-where-the-noise-lives-then-min-max
title: Chad Ashley (2017): fix noise at its source with min 1 max 1 and GI off, then set unified-sampling min and max; samples mode shows white as max
domain: redshift
tags: [chad-ashley, greyscalegorilla, unified sampling, samples mode, light samples, brute force, ledger-check, deep-read]
applies_to: Redshift 2.x for C4D (2017)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=LcxjkHFS-2k, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Method: set min and max samples to 1 and turn GI off; any grain left must come from the light, so raise the dome light samples first, doubling each time (64, 128, 256, 512, 1024) until a render region is clean; he says powers of two are easier for the maths "from what I've been reading" [24:23-26:56]. Then GI on with brute force: raise rays the same way (256 up to 2048) [26:56-28:00].
Only then give the unified sampler min 8 and max 16; the sampler then has less to do [28:00-29:04]. Samples mode: white pixels get max, black get min; raising max to 256 got faster, not slower, as areas dropped to min [29:04-30:07]. Higher adaptive threshold (0.05 to 0.1) hands more pixels the min [30:41-31:11]. DOF and motion blur need much higher min and max [31:11-31:42].
Global sampling overrides can replace or scale glossy, light and volume samples in one place [33:15-33:46]. For a bokeh shot he replaced glossy and light overrides with 8, cut bounces to 2 and raised max [48:15-49:45].
Old version and a different workflow from today's automatic sampling; the ledger wins.

**Use it:** Keep as the 'find which source is noisy' teaching order. Check against redshift-targeted-sample-overrides-vs-global and the ledger before reuse.
