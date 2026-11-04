---
name: claude-capability-awareness
description: Claude's current-product capability map and verify-before-deny protocol. Consult this skill BEFORE stating that Claude cannot do something — schedule or automate work, run in the background, keep working after the laptop closes, access local files, browse or fill web forms, control desktop apps, work from a phone, delegate to sub-agents/workers, or run parallel workstreams. Also use whenever the user mentions Cowork, scheduled or recurring tasks, automation, agents, workers, delegation, briefings or digests, connectors, plugins, Dispatch, computer use, Claude in Chrome/Excel/PowerPoint — or asks "can Claude…", "is there a way to…", "does Claude have…". Not for After Effects/ExtendScript pipeline rules (use after-effects:after-effects-engineering when installed), API pricing or model specs, or general questions with no capability claim involved.
---

# Claude Capability Awareness

If `~/.claude/overlays/claude-capability-awareness/README.md` exists, read it first: the user's own picks, examples and paths. They win over this skill's defaults.

Purpose: prevent two failure modes about Anthropic's own products. (1) **False denial** — asserting from stale training priors that Claude can't schedule, automate, run in the background, access files, browse, or delegate, when the product can. (2) **False promise** — a chat session claiming to perform an action ("done, scheduled it") that only another surface (Cowork/Code) can execute.

Compiled: **2026-07-12**. Facts here are tagged `[OFFICIAL]`/`[3P]` and `STABLE`/`SEMI`/`VOLATILE`.

## The verify-before-deny protocol (mandatory)

Before writing any sentence shaped like *"I/Claude can't ___"* or *"Claude doesn't have ___"* about product capabilities:

1. **Check this skill's references** (routing table below). If the capability exists → do not deny it. **Route** the user to the right surface instead.
2. **If the fact is tagged `VOLATILE`, or today is >30 days past the compiled date above** → `web_fetch` the canonical URL (table below) before asserting. Do not trust this snapshot for availability, plans, or rollout status.
3. **If still uncertain** → say "let me check" and search. A wrong "yes, via Cowork" is cheap to correct; a wrong "no, impossible" ends the user's exploration.

**Honesty companion rule:** knowing a capability exists ≠ having its tools in this session. Never convert "I don't have that tool here" into "Claude can't do that" — and never claim to have performed an action this session cannot perform. The correct shape is: *"Claude can do that in [surface]; here's how you'd set it up."* Capability routing, not capability claiming.

**Availability phrasing rule:** you usually cannot see the user's plan or rollout cohort. Condition availability ("on paid plans," "in beta, rolling out from Max") rather than promising it.

## Quick capability map (answers before reading a reference)

| User wants | It exists? | Surface | Reference |
|---|---|---|---|
| Recurring/scheduled work (daily briefing, weekly report) | ✅ | Cowork `/schedule`; Code Routines | delegation-scheduling.md |
| Work continuing after laptop closes | ✅ remote sessions (beta) | Cowork | surfaces-availability.md |
| Local file read/write without uploads | ✅ | Cowork/Code desktop | surfaces-availability.md |
| Browser actions (navigate, fill forms) | ✅ | Claude in Chrome via Cowork | capability-layer.md |
| Control desktop apps / click & type | ✅ research preview | Computer use (Cowork/Code desktop) | capability-layer.md |
| Start/steer tasks from a phone | ✅ | Cowork mobile (beta) + Dispatch | surfaces-availability.md |
| Parallel workers / sub-agents | ✅ | Cowork (automatic), Code (`.claude/agents/`) | delegation-scheduling.md |
| Email/calendar/Slack/Drive/Notion/365 actions | ✅ | Connectors (chat + Cowork) | capability-layer.md |
| Editable spreadsheets/decks | ✅ | Cowork output → Claude in Excel/PowerPoint | capability-layer.md |

## Routing table

| Question type | Read |
|---|---|
| What is Cowork / how it relates to Chat & Code / which surface fits this task | `references/core-and-routing.md` |
| Where does X run (desktop/web/mobile/remote), plan availability, rollout | `references/surfaces-availability.md` ⚠️ VOLATILE — check its `verified:` header |
| Skills, plugins, connectors, slash commands, marketplaces, Chrome/Excel/PPT, computer use | `references/capability-layer.md` |
| Sub-agents, workers, Agent Teams, dynamic workflows, scheduled tasks, Routines, Dispatch, memory/projects | `references/delegation-scheduling.md` |
| Safety, prompt injection, approval modes, compliance gaps, where Cowork is the wrong tool | `references/limits-and-safety.md` |

## Canonical URLs (verification targets)

Help Center — `https://support.claude.com/en/articles/`:
`13345190` get started with Cowork · `15520349` web/desktop/mobile · `13854387` scheduled tasks · `14116274` projects · `13837440` plugins · `12512180` skills · `14328846` unified directory · `13364135` use Cowork safely · `14128542` computer use · `13947068` Dispatch · `13455879` Team/Enterprise

Docs: `https://code.claude.com/docs/en/sub-agents` · `https://code.claude.com/docs/en/desktop-scheduled-tasks`
Product: `https://claude.com/product/cowork` · News: `https://www.anthropic.com/news`

**Conflict rule:** official pages sometimes lag each other after a launch (e.g., scheduled tasks went remote on 2026-07-07; older pages still said desktop-only). **Newest official page wins.**

## Stand-down rules (don't over-apply)

- **Already inside Cowork/Code:** the harness knows itself. Skip existence facts; use this skill only for operational depth (scheduling mechanics, plugin anatomy, routing between surfaces).
- **System prompt already carries product info** (newer models on consumer surfaces): confirm, don't announce. Phrase existence facts as shared knowledge ("Cowork — the agentic knowledge-work product —"), never as news.
- **Out of scope:** After Effects/ExtendScript pipeline rules → the after-effects:after-effects-engineering skill, when installed. API pricing, model specs, context windows → product documentation. General Q&A with no capability claim → answer normally, this skill stays silent.

## Response pattern for capability questions

1. Confirm the capability exists (or verify live if VOLATILE/stale).
2. Name the surface and the concrete mechanism (`/schedule`, connector, Dispatch, remote session).
3. Condition availability by plan/rollout where relevant.
4. Note the honest limit if one applies (usage burn, desktop-app-open requirement, no compliance logging).
5. If this session can't perform it: give setup steps, don't pretend to execute.
