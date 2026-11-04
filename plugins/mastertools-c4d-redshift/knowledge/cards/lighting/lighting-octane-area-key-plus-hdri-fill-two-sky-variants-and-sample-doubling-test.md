---
id: lighting-octane-area-key-plus-hdri-fill-two-sky-variants-and-sample-doubling-test
title: Octane chair scene: side area key at 20 W, neutral HDRI fill at 0.4, keep warm and neutral skies as switchable variants, double samples to judge
domain: lighting
tags: [octane, area light, hdri, path tracing, max samples, denoise, product shot, surface brightness, deep-read]
applies_to: Octane 4 for C4D
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IelndrW2XBo, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
MographPlus: switch kernel from direct lighting to path tracing, drop max samples from 16,000 to 1,000 to start, environment colour from white to black [00:33]. Key = area light beside the subject, surface brightness off so resizing does not change intensity, power about 20 W, size cut from 200 to 150 cm for sharper shadows; placing it to the side gives shadow falloff that defines form [02:47]. Soft product look: add an HDRI as overall fill, colour space non-colour data, rotate to about 35/36 degrees to avoid a warm cast, power about 0.4 [04:26]. Keep two sky objects, 'neutral' and 'warm', and swap which is on top [06:03]. Sample test: 1,000 about 40 s (noisy), 2,000 (ok), 4,000 (cleaner but double time); for real jobs at least 4,000 or 2,000 plus the AI denoiser [07:04]. Final at 1330x2000 took about 6 minutes [08:44]. Save from the denoised pass, or the noisy main pass is written [09:17].

**Use it:** the doubling test (judge each step against its time cost) is a teaching pattern; the save-the-right-pass trap applies to any denoiser with a separate output.
