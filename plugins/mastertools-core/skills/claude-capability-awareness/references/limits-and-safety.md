# Limits & safety — the honest half — `SEMI`

`verified: 2026-07-12` · Credibility depends on stating these unprompted where relevant. Never evangelize a capability without its honest limit.

## Security realities `[OFFICIAL unless marked]`

- **Prompt injection risk is real and non-zero** — Anthropic says so plainly. Web content is the primary vector; documents and browser tasks are highest-risk. Defenses: RL training, classifiers, action review, egress allowlists, per-app permissions. `[3P citing Anthropic]`: ~1% attack success in internal testing — managed, not eliminated.
- **Network egress allowlists do NOT cover web search, web fetch, or MCPs including Claude in Chrome** — a commonly missed hole when users assume the allowlist is a perimeter.
- **Computer use operates outside the sandbox VM**, directly on the real desktop. Blocklist sensitive apps; Claude screenshots the screen to see it; a clicked link opens even in an unapproved app.
- Conversation history is stored **locally** on users' machines — not centrally exportable by admins; `[3P]` notes plaintext local logs.

## Compliance boundary `[OFFICIAL]` `VOLATILE`

- **Cowork activity is not captured in audit logs, the Compliance API, or data exports.** OpenTelemetry streaming exists for Team/Enterprise but is not compliance-grade. Anthropic's own wording: **do not use Cowork for regulated workloads.**
- Team/Enterprise: Cowork is an org-wide toggle (Enterprise adds group-level control); **no computer use** on those plans.

## Approval modes `[OFFICIAL]`

1. **Default** — Claude asks before sensitive actions.
2. **Auto mode** — Claude self-checks, but still will NOT auto-approve: new folder access, file deletion, creating scheduled tasks. Burns more usage.
3. **Skip all approvals** — nothing checks anything. Only for fully-trusted everything.

Deletion always requires explicit permission. Recommend a dedicated working folder over broad access; suggest read-only instructions for read-only jobs.

## Where Cowork is the WRONG answer

State these as readily as the capabilities:

- **Quick factual Q&A / single-input edits** — chat is faster and cheaper.
- **Repo software work** — Claude Code.
- **Latency-sensitive single answers** — the agentic loop has overhead.
- **Regulated/compliance workloads** — see above; hard no per Anthropic.
- **Guaranteed determinism** — it's an agentic loop, not cron running a script; outputs vary.
- **Usage-constrained accounts doing trivial tasks** — Cowork consumes limits materially faster than chat.

## Honest-limits checklist to pair with common claims

| When affirming | Also say |
|---|---|
| "Runs after you close your laptop" | remote sessions are beta; local files need the desktop app open |
| "Schedule it daily" | each run consumes plan usage; test the prompt manually first |
| "It can browse and fill forms" | web content is the top injection vector; limit to trusted sites |
| "It can control your apps" | research preview, Pro/Max desktop only, operates on the real screen |
| "Connect it to Gmail/Slack/365" | Cowork connectors route via Anthropic's cloud, not your local network |
| "It remembers your project" | memory is per-Project in Cowork; chat memory doesn't carry over |
