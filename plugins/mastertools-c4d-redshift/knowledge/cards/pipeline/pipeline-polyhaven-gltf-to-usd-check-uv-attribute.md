---
id: pipeline-polyhaven-gltf-to-usd-check-uv-attribute
title: When importing downloaded assets as USD, check the UV attribute name; some assets use odd names
domain: pipeline
tags: [usd, uv, polyhaven, gltf, unreal, import, deep-read]
applies_to: Prism 2 (private beta mid-2023), QuiltiX early dev
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=GE6Af6hjYfI, src:yt-transcripts]
feeds: []
conflicts: none
---
Prism downloaded Poly Haven glTF assets and converted them to USD; in Unreal it created a USD stage actor pointing at the file with no custom changes. The one caveat: confirm the UV primvar name is right because some assets name it strangely [48:30-49:02].

**Use it:** Add UV-name check to asset-import QC.
