---
id: redshift-ao-aov-built-in-from-c4d-2025-3-1-replaces-utility-material-route
title: From Cinema 4D 2025.3.1 Redshift has a native AO AOV with the old utility-material options built in, so no custom AOV is needed
domain: redshift
tags: [ao, ambient occlusion, aov, 2025.3.1, mitch scott, deep-read]
applies_to: C4D 2025.3.1, Redshift 2025.3
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=OMTPokoFp5E, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: redshift-ao-aov-is-a-trap
---
Old route: build an ambient occlusion utility material and feed it into a custom AOV. New route: drag the new AO AOV (named AO, not the legacy one that used the AO node) into the AOV manager [00:33-01:04].
It carries the utility material's options (samples, bright and dark colours, spread, fall-off) in one AOV [01:04-01:34].
Check it in the Picture Viewer: Layer tab, Single Pass, pick the AOV [01:34-02:06]. Judge noise with bucket rendering on; turning it off is not a good idea for final-quality grain [02:37].
Mitch Scott (Behind the Button); posted 2025-06-26.

**Use it:** The AO check should look for the native AO AOV on 2025.3.1 and later, and not demand the custom-AOV workaround there.
