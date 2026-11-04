---
id: redshift-ic-load-and-flythrough
title: A loaded Irradiance Cache is invalid after any camera, object, light or material change; Flythrough is only for moving cameras
domain: redshift
tags: [irradiance cache, load cache, flythrough, gi cache, camera move]
applies_to: Redshift 2026-2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/The+Irradiance+Cache+GI+Engine.html.md, src:research-agency-pipelines]
feeds: [advisor]
conflicts: none
---
Load mode reuses a saved cache, so any change to camera, objects, lights or materials makes it wrong. Flythrough is for a moving camera only. A per-object option forces Brute Force.
Stale caches are a source of "it looked different on the farm" reports.

**Use it:** if a job loads a cache, check that its scene fingerprint still matches.
