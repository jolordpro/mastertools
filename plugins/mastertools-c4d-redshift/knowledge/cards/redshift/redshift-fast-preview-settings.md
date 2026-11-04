---
id: redshift-fast-preview-settings
title: Fast-preview settings: progressive passes 32, undersampling 2-5, small window, 75% resolution
domain: redshift
tags: [ipr, progressive passes, undersampling, preview, render view, laptop]
applies_to: Redshift in C4D
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=uKRqHwVr0F4, https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
Progressive passes default to 1024; dropping to 32 lets the frame finish and frees the GPU [05:15, RF]. Greyscalegorilla's Chad uses 32 too, and says 512 makes a laptop chug and fans run [57:55, GSG].
Undersampling (IPR) 5 improves response while orbiting [04:44, RF]; Chad uses 2 and 75% resolution, and a small window set to fit [53:45, GSG].
Bucket mode ignores progressive passes and uses the unified-sampling threshold (default 0.01), so raise that for quick bucket previews [06:16, RF].

Ledger agrees: §4 "Progressive Passes applies to Production Progressive and Live only".

**Use it:** scene advisor: preview settings are a separate profile from final settings; the 640 px draft can follow this.
