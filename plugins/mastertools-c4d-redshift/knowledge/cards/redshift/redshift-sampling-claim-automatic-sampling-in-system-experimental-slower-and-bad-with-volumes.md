---
id: redshift-sampling-claim-automatic-sampling-in-system-experimental-slower-and-bad-with-volumes
title: In an older Redshift build, a creator found Automatic Sampling (then under System, Experimental) slower and weak on extreme DOF and volumes; claim, check against the ledger
domain: redshift
tags: [automatic sampling, experimental, volumes, depth of field, polybox, ledger-check, deep-read]
applies_to: Redshift in C4D, older build with the experimental switch
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=Q5AZ7Xlh2I4, src:yt-transcripts, https://www.youtube.com/watch?v=vnHKQmvKYH8]
feeds: [redshift]
conflicts: ledger
---
Speaker's claim: enabling Automatic Sampling under System, Experimental ignores the Basic-tab sampling settings and uses only the adaptive error threshold [24:05-24:37].
His findings: usually a bit slower, less control, trouble clearing noise in extreme DOF, and problems with volumes; fine for quick previews [24:37-25:39].
He says a manual setup takes him 10 to 15 minutes even for complex scenes.
Ledger: Automatic Sampling is now a normal control that hides Min and Max and leaves threshold as the only driver, so his 'experimental' location is out of date.

**Use it:** Log as one more voice in the automatic-versus-manual split; do not tell users to avoid it.
Transcript support: for volume grain, local light volume samples are the most efficient control. (https://www.youtube.com/watch?v=vnHKQmvKYH8 [12:21-12:51])
