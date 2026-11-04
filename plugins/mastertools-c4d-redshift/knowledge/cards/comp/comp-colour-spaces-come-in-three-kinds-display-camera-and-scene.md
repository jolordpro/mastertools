---
id: comp-colour-spaces-come-in-three-kinds-display-camera-and-scene
title: Three kinds of colour space: display (Rec 709, Rec 2020), camera log (LogC, S-Log, Red Log) and scene (DaVinci Intermediate, ACES)
domain: comp
tags: [team-2-films, color management, rec709, rec2020, log, aces, davinci-intermediate, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=w0ubDSzEEYg, src:yt-transcripts]
feeds: [[post-composite, shakedown]]
conflicts: none
---
Team 2 Films (Resolve masterclass, 2023): a colour space fixes a range of colours and how brightness is encoded, often with a gamma or log curve [01:34][02:06]. Display spaces (Rec 709, Rec 2020) are for delivery; camera spaces like LogC or S-Log are made to squeeze the most from one sensor and are not for display; scene spaces such as DaVinci Intermediate and ACES are so wide they hold all visible colours without being limited by any camera or display [05:17][05:48][06:18]. Rec 709 dates from the early 1990s and assumed CRT displays of about 100 nits, which is why it is limiting [04:12]. Viewing log on a Rec 709 display looks flat because the languages do not match [02:37]. Color management is reconciling all of these into the delivery (or archive) space [06:18][06:50].

**Use it:** a plain-words primer for the coach; before debugging a flat or oversaturated frame, ask which of these three spaces each stage is in.
