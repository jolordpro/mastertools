---
id: redshift-ao-node-needs-bucket-mode
title: The AO node and individual AOV previews only work properly in bucket mode, not progressive
domain: redshift
tags: [ao, ambient occlusion, bucket, progressive, aov preview, render view, picture viewer]
applies_to: Redshift in C4D 2024
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts, https://www.youtube.com/watch?v=-lpj38Cql4c]
feeds: [coach, CHECKS]
conflicts: none
---
In the Redshift render view you must enable buckets to see each AOV; some passes just go black or white in progressive [1:22:07].
The AO node uses the final sampling only in bucket mode; in progressive it takes about one sample per pixel, so the AO is poor [1:22:35].
Direct-output AOVs do not show in the Picture Viewer multipass tab; C4D's own multipass save does [1:45:21].

**Use it:** a draft check should render in bucket mode when AO or AOVs are being judged.
