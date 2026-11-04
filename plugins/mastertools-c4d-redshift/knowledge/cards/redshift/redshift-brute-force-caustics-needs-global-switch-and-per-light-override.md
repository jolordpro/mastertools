---
id: redshift-brute-force-caustics-needs-global-switch-and-per-light-override
title: Redshift's newer caustics (speaker, 2025-era): set caustics to Brute Force, tick Global Caustics, then override intensity per light (1 is weak, 2-4 used)
domain: redshift
tags: [caustics, brute force, global caustics, photon, light override, denoising, overhead, ledger-check, deep-read]
applies_to: Redshift in C4D, two RTX 4090s (version not stated; about 2025)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=FYq8sdCtsoY, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Vincent Schwenk [00:33-04:40]. In render settings Advanced the old caustics mode was Photon; he changes it to Brute Force and turns on Global Caustics (both may be off in a new scene). Each light then needs its Caustics override on; default intensity 1 is too weak for him, he uses 2 and often 3-4. He found the brute-force caustic ray count (256 default) made no visible or timing difference from 8 to 30,000 under the denoiser, and thinks it is tied to the GI brute-force rays [07:48-10:26]. A small hard rim light gives defined caustics like the old workflow; a large soft dome gives subtle ones. Denoiser delay: Denoising overhead 0/0 means denoise starts after 128 progressive passes (about 8.6 s in his scene) [03:08-03:38]. Speaker's claims, not the ledger; confirm in the docs.

**Use it:** Tag ledger-check before turning this into a coach rule. Also check Global Caustics and per-light override before concluding caustics 'don't work'.
