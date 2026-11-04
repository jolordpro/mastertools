---
id: lookdev-denoiser-cuts-samples-by-95-percent-but-flickers-in-animation
title: An AI denoiser cut one still from about 20,000 samples (69 min) to 1,500 (under 6 min), but single-frame denoisers flicker in animation
domain: lookdev
tags: [denoiser, optix, samples, render time, animation flicker, edges, neat video, temporal window, deep-read]
applies_to: Blender Cycles with OptiX (2020-era)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=eGAjsSNtX6E, src:yt-transcripts, https://www.youtube.com/watch?v=OJWzYNwgj3c, https://www.youtube.com/watch?v=sjiuEeAp-JE, https://www.youtube.com/watch?v=mLMXWCLX4SY]
feeds: [redshift, estimator]
conflicts: none
---
Interior still: roughly 20,000 samples needed without a denoiser took 1 h 09 min per frame on dual 1080 Ti; with OptiX 1,500 samples took under 6 minutes, about a 95 percent cut [04:10-05:06]. Settings noted: render the passes separately for the denoiser (the 'extra passes' option) to keep texture detail, which blocks compositor use; the HDR training option helps in low light but can smooth detail [02:07-03:08]. The default Blender denoiser gave blotchy flat areas and smeared texture; OptiX kept texture but lost razor-thin edges at low sample counts [00:54, 03:39-04:10].
Animation: both denoisers disagree frame to frame, giving flicker and dark blips even with the animated-seed option off [05:06-06:15]. Studios use a temporal window (Pixar/Disney in-house reported at seven frames) [06:15]. His workaround for photoreal animation: render about 3000 samples (still around 10 minutes a frame), then use the Neat Video plugin, which keeps detail and is consistent across frames but fails on very noisy frames; use OptiX only for stills and stylised work [06:45-07:46].

**Use it:** supports the Redshift cards that treat the denoiser as a finisher: never feed a denoiser a very noisy animation frame; for sequences test a temporal option and scrub for blips.
Transcript support: a noisy SSS patch denoised into splotches on one pose; turn the denoiser off or add samples to test (https://www.youtube.com/watch?v=sjiuEeAp-JE [16:39])
Transcript support: Arnold: denoiser let camera AA drop 8 to 2 (render 1:43 to 0:44) before adaptive sampling; still check DOF artifacts (https://www.youtube.com/watch?v=mLMXWCLX4SY [09:53])
