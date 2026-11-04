---
id: redshift-sampling-claim-dof-set-min-equal-max-then-samples-view-white-means-maxed
title: For depth-of-field noise one creator sets Samples Min equal to Max to test, then drops Min to 16-32 and reads the Samples view (white means the max was not enough); claim, check against the ledger
domain: redshift
tags: [depth of field, unified sampling, min samples, max samples, samples view, ledger-check, deep-read]
applies_to: Redshift in C4D, older version, uncertain
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Q5AZ7Xlh2I4, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Speaker's claim: with the scene clean of material noise, re-enable DOF, switch to clay render, find the noisiest area (the shallowest depth of field) and raise Min and Max together [15:52-16:57]. With equal values every pixel gets exactly that count until the threshold is hit [16:57-17:28].
Samples view in the render view: white = used the maximum and still missed the adaptive error threshold; grey = reached it early. It only reads usefully when Min and Max differ (16 and 512 shown) [17:28-18:32].
He reached Max 1024, then a larger value the captions garble as '248' (probably 2048), lowered the threshold, and finally dropped Min to 16 or 32 once the image looked right [18:32-20:57].
Ledger contrast: ledger [V] says with DOF or motion blur use at least 8-16 min samples and 256+ max for strong DOF; it does not endorse Min = Max as a final setting [see §2].

**Use it:** Treat the Samples view as a diagnostic for DOF-heavy shots, and keep Min at the ledger's 8-16 floor for finals.
