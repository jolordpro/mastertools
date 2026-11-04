---
id: c4d-time-effector-delayed-start-needs-a-time-field-with-a-negative-offset
title: To delay a Time effector animation, keys on strength jump; use a Time field (total time, offset such as -100) instead
domain: c4d
tags: [double motion design, time effector, time field, offset, cloner, delay, loop mode, mograph, cinema 4D, deep-read]
applies_to: Cinema 4D (version not stated; video uploaded 2026-04, so a 2026 build is likely)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=mq2eMicxJZ4, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Speaker: Double Motion Design (channel; speaker not named). Problem: Time effector offsets a clone's baked animation, but starting it at frame 100 fails. Keying strength 0 then full at frame 100 makes the bird snap; keying at 99/100 snaps too; keying position X has the same jump [02:44-04:23].
Working fix: add a Time field to the effector [04:23-04:57]. Set its total time to 250 (the rate is the total frame count), which by default gives a parabolic acceleration; fix it by setting the field's curve to none so speed matches the plain version [04:57-06:01]. Then offset the field by -100: the clone stays still until frame 100, then moves [06:01-06:33].
A second cloner copy with a different offset and count gives two groups with independent timing [07:04-07:42]. Captions are rough (97 words/min), so numbers other than 250 and -100 are not certain.

**Use it:** for staggered starts of cloned cycles, add a Time field with the curve off, set total time to the shot length and slide the offset, not strength keys.
