---
id: c4d-mcp-relink-broken-textures-absolute-vs-local
title: Asked to relink broken textures, the assistant fixed 364 references in 1:06 but used absolute paths until told 'local'
domain: c4d
tags: [mcp, broken textures, relink, project asset inspector, absolute path, local path, dome light]
applies_to: C4D 2027.0 MCP
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: [preflight asset check, coach]
conflicts: none
---
[02:36:34] Test: 22 assets with 275 missing materials in the Project Asset Inspector, which can also fix by editing a path section by hand.
[02:39:07] First pass fixed 364 references in 1:06 but with a new absolute path, and also fixed a dome light's path. A follow-up asking for a local path finished in 38 s with all green in the inspector [02:40:40].
Real-world version: a project that meant deleting paths by hand for 156 materials took the assistant about 2 min [02:38:06].

**Use it:** prompt must state absolute or relative; verify in the asset inspector afterwards.
