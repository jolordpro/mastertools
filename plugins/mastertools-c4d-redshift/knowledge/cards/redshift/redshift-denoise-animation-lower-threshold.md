---
id: redshift-denoise-animation-lower-threshold
title: For denoised animation use a lower threshold than for stills, and turn the random noise pattern off
domain: redshift
tags: [denoise, animation, flicker, threshold, random noise pattern]
applies_to: Redshift 3.x in C4D
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=G43QVR1TqXg, https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts, https://www.youtube.com/watch?v=jyGQIKOPwGA]
feeds: [coach, redshift]
conflicts: ledger
---
Denoised sequences can flicker even when stills look clean. Fix in two parts: untick random noise pattern, and set the threshold lower than for stills; Low or Medium is usually enough, not Very High [07:18, RT].
Same dragon scene: Medium with denoise and pattern off took about 1 minute vs 6 s for the still setting, and flicker was barely visible [08:19].
Greyscalegorilla's Chad leaves denoise off for sequences (no full temporal denoise) and cranks samples when plain backgrounds chatter [56:51, 58:56, GSG].

**Ledger conflict (2026-10-30):** the redshift skill (Law 3) names a lower threshold as the wrong first lever for a clean still that flickers in sequence; the cause is GI or the denoiser. The ledger wins. Also, "Low or Medium" here means the quality preset (Low 0.1, Medium 0.01), a higher threshold number, not a lower one. Treat this card as a tutor's habit, not a rule.

**Use it:** when a job is an animation, the coach warns that the still-tuned threshold will flicker; the estimator should price animation at the lower threshold.
