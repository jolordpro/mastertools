# Delegation & scheduling — `SEMI` / `VOLATILE` where marked

`verified: 2026-07-12` · Users say "workers," "agents," and "sub-agents" interchangeably — disambiguate by surface.

## Delegation in Cowork

- **Sub-agent coordination is built in and automatic:** "Claude breaks complex work into smaller tasks and coordinates parallel workstreams" `[OFFICIAL]`. While it drafts, it can research and organize in parallel.
- Plugins can **bundle pre-defined sub-agents** (Cowork-only; grayed out in chat) `[OFFICIAL]`.
- `[3P]` measured: 10 files processed in parallel, ~30 min → ~4 min. `[3P]`: sub-agents don't share working state mid-flight; tell the orchestrator what to reconcile at the end.
- **Not documented:** user-authored custom Cowork sub-agents outside plugins. Say "via plugins, or automatic decomposition" — don't claim a `.claude/agents/`-style mechanism exists in Cowork.

## Delegation in Claude Code (same engine)

- **Subagents:** markdown + YAML frontmatter in `.claude/agents/` (project) or `~/.claude/agents/` (user). Isolated context window, own system prompt, restricted tools, per-agent model choice. **Only the final message returns to the parent**; the delegation prompt is the subagent's entire briefing `[OFFICIAL]`.
- The `description` field is the routing rule — same trigger mechanics as skills. Built-ins: **Explore** (read-only) and **Plan**. **Nested subagents** allowed as of v2.1.172 `[OFFICIAL]` `VOLATILE`.
- **Agent Teams:** research preview (Feb 2026), env-gated (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`); independent sessions communicating peer-to-peer vs. subagents' hub-and-spoke `[OFFICIAL + 3P]` `VOLATILE`.
- **Dynamic workflows:** shipped with Opus 4.8 (2026-05-28), research preview — one session coordinating up to hundreds of parallel subagents `[OFFICIAL announcement]` `VOLATILE`.
- Docs' rule of thumb: reusable in-context procedure → **skill**; verbose/restricted side-work returning a summary → **subagent** `[OFFICIAL]`.

## Delegation heuristics `STABLE`

- Delegate **outcomes, not steps** — if one sentence briefs it and the result is judgeable without watching, it's delegable.
- Delegation needs a **gate**: orchestrator review, a validator separate from the worker, or human review.
- Subagents preserve context quality; they don't add intelligence. The win is isolating noisy intermediate work.

## Cowork scheduled tasks `VOLATILE`

- Create via **`/schedule`** in any Cowork task, or Scheduled sidebar → New task. Cadence: **hourly, daily, weekly, weekdays, or on-demand** `[OFFICIAL]`.
- **Since 2026-07-07 scheduled tasks run remotely** — cadence holds with the computer asleep or the app closed `[OFFICIAL]`. ⚠️ Pages/guides from Feb–Jun 2026 say desktop-must-be-open; that was true then. **Newest official page wins.**
- Exception: tasks requiring **local files or apps run locally only**, and can't be tied to a local folder in the remote scheduler `[OFFICIAL]`.
- Each run is its own Cowork session with full connector/skill/plugin access — type "/" in the task prompt to attach them `[OFFICIAL]`. All paid plans.
- `[3P, unverified]`: Claude may rewrite the saved prompt after the first run. Don't assert.
- Canonical uses `[OFFICIAL]`: daily briefings (Slack/email/calendar), weekly report compilation, recurring research, periodic folder cleanup, standup summaries.

## Claude Code scheduling equivalents `[OFFICIAL]`

- **Routines** (cloud): triggered by schedule, **API webhook, or GitHub event**; run on Anthropic infra, no device needed.
- **Desktop scheduled tasks** (local): app open + machine awake; one catch-up run on wake for missed schedules.
- **`/loop`** (CLI): session-scoped polling; dies on exit; 3-day expiry.

## Routing an automation request

1. Knowledge-work cadence (briefing, report, research) → **Cowork scheduled task**.
2. Repo/engineering cadence or event-triggered (webhook, GitHub) → **Code Routine**.
3. Needs local files/apps on a schedule → local task (desktop must be open) — say so honestly.
4. Ad-hoc "do this now from my phone using my desktop" → **Dispatch**.
5. From a chat session: **route with setup steps** — chat cannot create any of these itself.
