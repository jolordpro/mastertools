---
id: pipeline-netflix-vfx-round-trip-test-before-real-shots
title: Netflix VFX round trip: before real work, push a show-specific test pull through editorial, pulls facility, vendor and finishing, and require a one-to-one match in colour and framing
domain: pipeline
tags: [netflix, vfx round trip, pull, aces ap0, exr, dpx, framing chart, slate, burn-in, show lut, handles, deep-read]
applies_to: Netflix productions (2023)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=qlqiBNsqNps, src:yt-transcripts, https://www.youtube.com/watch?v=upUAulx7sGI, https://www.youtube.com/watch?v=pWT2nk1vCt8]
feeds: [[shakedown, CHECKS]]
conflicts: none
---
Netflix Production Technology (guidance video, medium). Purpose: test the image pipeline early so errors in scale, colour, frame count, naming, slates or burn-ins are found before work is done twice [00:18-02:47]. Use show-specific footage, framing charts and colour files, not stock [03:57]. Steps [04:00-07:21]: editorial requests a pull with standardised naming, frame and handle counts, proxy codec, an EDL and dailies-colour reference stills or clips; the pulls facility makes EXR or DPX frames and colour files per clip plus framing chart and reference media; the vendor ingests (no VFX work yet), uses the charts to verify framing, builds colour (ACES AP0 EXRs to log grading space, CDLs or look files baked to proxies, then the show LUT as output transform); vendor, editorial and finishing compare the output with the dailies reference, which must match one-to-one in colour and framing. Proxy MOVs carry slate and frame burn-ins in fixed-size fonts in the same place as the reference; EXRs return with no LUT or burn-ins, with a slate first frame; both go back (EXR to finishing, MOV to editorial). Test per camera format, at least the primary one [05:37]. Common faults: missing frames or wrong duration, naming and slate inconsistencies, colour mismatch, framing mismatch. It is a test, not a delivery: rerun after fixes [07:52]. Record errors and solutions [01:05-01:37].

**Use it:** Template for a platform delivery self-test: one real frame sequence through every hop before the job starts, matched one-to-one against the reference.
Transcript support: conform check: match EDL to clips by timecode and clip name and expect one match per entry; output EXR 16-bit float (https://www.youtube.com/watch?v=pWT2nk1vCt8 [03:45])
