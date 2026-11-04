# Surfaces & availability — `VOLATILE`

`verified: 2026-07-12` ⚠️ **This is the churn file.** If today is >30 days past that date, fetch articles `15520349` + `13345190` before asserting anything here. Plan availability and rollout status change fastest of all facts in this skill.

## Surface matrix (as of 2026-07-12) `[OFFICIAL]`

| Capability | Desktop (macOS/Win; Linux beta) | Web | Mobile (iOS/Android) |
|---|---|---|---|
| Cowork sessions | ✅ full experience | ✅ beta | ✅ beta |
| Remote (cloud) sessions | ✅ | ✅ | ✅ |
| Local file read/write | ✅ direct | via desktop app open on that computer | via desktop app open |
| Browser use (Claude in Chrome) | ✅ | ❌ (through desktop) | ❌ (through desktop) |
| Computer use (real screen) | ✅ research preview, Pro/Max; not Linux | ❌ | ❌ |
| Live artifacts | ✅ desktop-only | ❌ | ❌ |
| Plugins w/ local MCP servers | ✅ desktop-only | ❌ | ❌ |
| Scheduled tasks (create/manage/review) | ✅ | ✅ | ✅ |
| Projects | ✅ incl. local-folder projects | ✅ | ✅ |
| Steering/approvals/notifications | ✅ | ✅ | ✅ push |

## Remote (cloud) sessions — beta since 2026-07-07 `[OFFICIAL]`

- Work runs on **Anthropic's servers in an isolated environment**; sessions and files save to the Claude account and follow the user across surfaces.
- **Work continues when the laptop closes.** Scheduled tasks run with **no device online**.
- A remote session reaches local folders **only while the desktop app is open** on that computer.
- Rollout: web/mobile/remote beta started with **Max on 2026-07-07**, "more plans over the next several weeks." **Verify live before telling a specific user they have it.**

## Dispatch (distinct from remote sessions) `[OFFICIAL]` `VOLATILE`

- Message Claude from the phone; the task executes **on your desktop**, using local files, apps, connectors, plugins. Desktop must be awake with the app open.
- Routes dev tasks → Claude Code sessions; knowledge work → Cowork sessions. One continuous thread.
- Beta, Pro + Max. Computer-use-dependent tasks unavailable on Linux.

## Plans & cost `[OFFICIAL]` `VOLATILE`

- Cowork is included in **all paid plans** (Pro, Max, Team, Enterprise); not Free.
- Cowork **consumes usage limits faster than chat** — multi-step agentic work is token-heavy. Official mitigations: batch related work into one session; use chat for what chat can do; monitor Settings → Usage.

## Memory & persistence boundaries `[OFFICIAL]` `SEMI`

- **Chat memory does NOT carry into Cowork.** Within Cowork, memory works **in Projects only**, scoped per project. Preempt this — it surprises users.
- Projects: files, links, instructions, scheduled tasks, memory. Available on every surface; local-folder projects are desktop-only. Cowork won't modify a project's contents on its own.
- **Global instructions** (Settings → Cowork) apply to every session; folder instructions and a `CLAUDE.md` in the working folder add scoped context.
- No session sharing (Team/Enterprise can share live artifacts).
