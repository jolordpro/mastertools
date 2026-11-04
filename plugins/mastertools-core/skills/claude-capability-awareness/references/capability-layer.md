# The capability layer: skills, plugins, connectors — `SEMI`

`verified: 2026-07-12`

## Agent Skills

- A skill = a folder with `SKILL.md` (YAML frontmatter name+description, markdown body; optional `scripts/`, `references/`, `assets/`). **Open standard, portable** across Claude apps (chat), Cowork, Claude Code, and the API `[OFFICIAL]`.
- **Progressive disclosure:** metadata always in context; body loads on trigger; bundled resources load on demand.
- **The description IS the trigger.** Claude matches requests against descriptions; documented tendency to **undertrigger**, so good descriptions are pushy and enumerate concrete phrases `[OFFICIAL]`.
- Cowork ships built-in skills for **pdf, docx, pptx, xlsx, canvas-design**, auto-loading for those types `[3P, consistent w/ official]`.
- Requires **code execution enabled**. Available on all plans in chat; org plans add owner toggles, org-wide provisioning, and sharing (sharing **off by default**, owner must enable) `[OFFICIAL]` `VOLATILE`.
- Managed in **Customize → Skills** (unified directory with Connectors and Plugins). Directory installs are view-only — download, modify, re-upload to edit `[OFFICIAL]`.
- Invocation: automatic on relevance, or manual via the **"/" slash menu** in chat and Cowork.
- `[3P, unverified]`: skill metadata shares a context budget ≈2% of the context window; a large installed stack can crowd triggering. Use as a debugging heuristic only.
- Skills can carry Excel/PowerPoint templates that **Claude in Excel / Claude in PowerPoint** load into the currently open file `[OFFICIAL]`.

## Plugins

- A plugin **bundles skills + connectors + sub-agents + hooks + slash commands** into one installable package `[OFFICIAL]`.
- **Asymmetry that matters for routing:** plugin skills work in chat *and* Cowork; **hooks and sub-agents run only in Cowork** (grayed out in chat) `[OFFICIAL]`.
- Marketplaces: Anthropic's **Knowledge Work** (default), Financial Services, Legal, Life Sciences; GitHub-repo marketplaces; **private org marketplaces** with installed-by-default / available / required / hidden states (Enterprise: per-group) `[OFFICIAL]` `VOLATILE`.
- Anthropic's plugins are open-source (`github.com/anthropics/knowledge-work-plugins`). "Plugin Create" plugin scaffolds custom ones. `/setup-cowork` runs guided onboarding (role-matched plugin + connectors) `[OFFICIAL]`.

## Connectors

- MCP-based integrations: Gmail, Google Drive/Calendar, Slack, Notion, DocuSign, Microsoft 365 (incl. **write tools** — draft/send mail, manage calendar, create/update OneDrive & SharePoint files, July 2026), and more `[OFFICIAL]` `VOLATILE`.
- **In Cowork, connectors reach services through Anthropic's cloud**, not the local network; custom connectors must be publicly reachable — matters behind VPNs/firewalls `[OFFICIAL]`.

## Tool-preference order when acting `[OFFICIAL]`

Cowork uses the most precise tool first:
1. **Connectors** — fastest, most reliable.
2. **Browser (Claude in Chrome)** — when no connector exists for the site/tool.
3. **Screen interaction (computer use)** — last resort; slower, more error-prone.

## Computer use `[OFFICIAL]` `VOLATILE`

- Research preview: **Pro and Max only**, Cowork + Claude Code in the desktop app, macOS + Windows (not Linux, not Team/Enterprise).
- Operates **outside the sandbox VM**, directly on the real desktop: clicking, typing, navigating, screenshots to read the screen.
- Safeguards: per-app permission prompts; app blocklist (investment/trading/crypto blocked by default); injection-scanning action review. Desktop must be awake with the app open.
