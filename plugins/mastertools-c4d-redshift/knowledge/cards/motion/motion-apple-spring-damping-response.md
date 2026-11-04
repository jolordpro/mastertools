---
id: motion-apple-spring-damping-response
title: Apple design spring knobs (2018): damping and response, with no duration for elastic behavior
domain: motion
tags: [motion-tokens, product, nathan-de-vries, springs, tokens]
applies_to: any
status: V
confidence: high
decay: slow
read: 2026-10-30
recheck_by: 2028-10-30
sources: [https://developer.apple.com/videos/play/wwdc2018/803/, https://www.youtube.com/watch?v=gttSJA-kDmQ, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Nathan de Vries: mass, stiffness and damping stay hidden. Designers get two controls: damping (100% = no overshoot, 0% = endless oscillation) and response (how fast it reaches the target). He avoids duration for springs because the spring is always ready to move again. Technical names: damping ratio and frequency response. (Apple's 2023 session later moved public guidance to duration and bounce; see motion-apple-spring-duration-bounce.)

**Use it:** Pick one parameter pair per system and say why; do not mix pairs between teams.
