---
id: redshift-2027-aces2-default
title: C4D 2027 and Redshift 2027.0 make ACES 2.0 native, with an ACES 2 config as the default
domain: redshift
tags: [aces 2.0, ocio, colour management, redshift 2027, default config]
applies_to: Redshift 2027.0, C4D 2027
status: V2
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.vfxer.com/maxon-fall-2026-release-cinema-4d-2027-breakdown/, https://www.cgchannel.com/?p=179414, src:research-agency-pipelines, src:research-youtube]
feeds: [version-match check, CHECKS 5]
conflicts: none
---
Reseller and press summaries say the Oct 2026 release makes ACES 2.0 native and uses an ACES 2 config by default. The earlier OCIO config with ACES v2.0 support arrived in 2026.8 (ledger section 8).
A desk on 2027 and a farm node on an older build can therefore use different ACES versions for the same file.

**Use it:** the version-match check compares ACES version as well as the Redshift build, not only the build number.
