---
id: c4d-nested-proxy-one-level
title: C4D's asset detection finds Redshift proxies only one level deep, so proxy-of-proxy textures are missed
domain: c4d
tags: [nested proxy, redshift proxy, assets, farm, missing textures, asset inspector]
applies_to: C4D 2025-2026
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://developers.maxon.net/forum/post/54181, https://irendering.net/cinema-4d-redshift-proxy-render-farm, src:research-agency-pipelines, src:research-render-farms, src:research-gaps-deep]
feeds: [CHECKS 1]
conflicts: none
---
Source is a Maxon developer forum post. Deadline Cloud's docs state the same limit for nested Redshift proxies, and farm parsers that read only the root .c4d show empty boxes.

**Use it:** preflight walks nested proxies itself instead of trusting the packager.
