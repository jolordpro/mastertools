---
id: lighting-flag-a-light-with-a-black-blocker-and-balance-per-light-sampling
title: Fake a spotlight by flagging a disc light with a black blocker tube, and scale sampling rate with light size
domain: lighting
tags: [light blocker, spotlight, volume fog, light sampling rate, noise balance, fog density, deep-read]
applies_to: Octane lights and volumes
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=TuKDhZU7ySE, src:yt-transcripts, https://www.youtube.com/watch?v=J5KwV7GfbEQ]
feeds: [redshift]
conflicts: none
---
With fog added (density about 0.1) a light makes a visible blob [09:52]. To turn it into a spot: make it a disc light, then drop a tube around it with a black, non-participating diffuse material so it only blocks light; a longer tube makes a narrower beam [10:26-11:59].
Octane's per-light sampling rate does not mainly raise brightness; it balances noise between lights of different size. A light three times smaller needed three times the samples to resolve at the same speed as the big one [11:59-13:01].

**Use it:** a noise tip: when one small light stays noisy while large ones are clean, raise that light's sample setting (Redshift has per-light samples; verify against the ledger).
