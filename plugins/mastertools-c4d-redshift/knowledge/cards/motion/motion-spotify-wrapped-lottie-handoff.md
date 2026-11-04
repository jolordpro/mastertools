---
id: motion-spotify-wrapped-lottie-handoff
title: Spotify Wrapped animation: After Effects to Lottie served from backend, with trade-offs
domain: motion
tags: [motion-tokens, product, ade-omole, lottie, handoff]
applies_to: any
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://engineering.atspotify.com/2024/1/exploring-the-animation-landscape-of-2023-wrapped]
feeds: [studies/motion-leaders]
conflicts: none
---
Spotify (2023 Wrapped) built animations in After Effects, uploaded the Lottie file to the backend, and served one file to Android, iOS and web. Gains: visual parity and less repeat engineering. Costs: download payload, failure risk, and designer-engineer sync on edits. Native code stays for user-triggered or data-driven visuals.

**Use it:** When describing a toolkit, state what ships as a file, what stays native, and the cost of each.
