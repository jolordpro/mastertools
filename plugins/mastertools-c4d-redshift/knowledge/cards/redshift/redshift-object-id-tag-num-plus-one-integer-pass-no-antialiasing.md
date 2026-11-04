---
id: redshift-object-id-tag-num-plus-one-integer-pass-no-antialiasing
title: Chad Ashley: number every Redshift object tag in sequence for an integer Object ID pass, but it has no anti-aliasing so edges are rough
domain: redshift
tags: [chad-ashley, object id, integer aov, redshift object tag, clown pass, fusion, deep-read]
applies_to: Redshift 2.x for C4D (2018)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ARykOD6lG3c, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Put a Redshift Object tag on every object and fill Object ID with sequential numbers. A tip from a viewer in chat (name garbled in captions, written as Merk Wilson): select all tags, type num and +1 in the ID field and they number themselves [28:43-30:18].
Render in a multi-channel EXR. The pass looks all white in the IPR; in comp each object has a unique value (he hovers 106, 130 and so on). Shuffle it into an Object ID channel and Fusion's colour corrector can pick an object by clicking it, so one canister goes blue without keying clown colours [30:49-34:29].
Catch: it is an integer channel so it has no anti-aliasing and edges are cleaner from a puzzle matte or a normal clown pass. Fine for a slight grade, not for hard isolation [34:29-35:00]. Store Integer To AOV is the route for IDs of your own [37:15-37:45].
Transfer: quick per-object grading of a product or helmet in comp without rendering a matte per piece.

**Use it:** Offer Object ID for small per-object tweaks, a puzzle matte or Cryptomatte for hero edges. Cryptomatte now exists in Redshift; check the ledger before recommending either as current.
