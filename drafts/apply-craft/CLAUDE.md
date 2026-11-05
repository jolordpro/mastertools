# CLAUDE.md: Apply Craft build kit

This folder is the source kit for building the `apply-craft` skill suite: job-application skills for creative professionals, starting with motion design and big-company hiring.

## Where to start

1. `PLAN.md` is the approved (or pending) build plan. Follow its phases and the decisions recorded in §12.
2. `knowledge/00-principles-and-guardrails.md` holds the rules every skill inherits. Put a short version in each skill's `SKILL.md` and link to the full file.
3. To build a skill, use its `prompts/` file as the method, the relevant `knowledge/` files as references, and `templates/` for user data.

## Before building for a real person (AC-L-009)

Look for their existing system first: repos, a source-of-truth file, prior audits, an application ledger. Extend it; don't duplicate it. A candidate-specific handoff, if one exists, lives in a private bundle outside this kit.

## Build rules

- **Keep `SKILL.md` files lean.** Detail goes in `references/`. Use the `skill-creator` skill for structure, sizing, and evals.
- **Keep user data out of skills.** Per-person files live in `data/` (gitignored), created from `templates/`. Never hard-code a person's name, employer, history, or confidentiality specifics into a skill.
- **Never store client or third-party personal data anywhere in this repo.** That includes fixtures and examples. Use placeholders like `[CLIENT]`.
- **Load company facts from dossiers.** Read `data/dossiers/<company>.md`; don't hard-code them. Netflix's dossier is the worked example (`knowledge/02`).
- **Cite evidence by ID.** Use IDs from `knowledge/12-evidence-library.md` (e.g., "E06"). A claim past its recheck-by date must be re-verified at run time or labeled ASSUMED.
- **Promise honestly.** Descriptions say "maximizes interview odds," never "guarantees."
- **Never auto-submit.** Never mark an application submitted without the user confirming.
- **Name skills correctly.** Names never contain "claude" or "anthropic."

## Conventions

- **VERIFIED / ASSUMED** labels.
- **Evidence strength:** A–D, plus EST.
- **Actor tags:** `[AI]` / `[AI+WEB]` / `[ME]`.
- **Two stages with a STOP gate,** a fast lane, and a time budget.
- **Required outputs:** a consistency table and a change log.
- **New lessons** go in `knowledge/10` as AC-L-012 and up. The `AC-` prefix keeps them distinct from a project's own challenger ledger.

## Evals

Each skill ships with planted-defect fixtures (PLAN §10). Pass bar:
- 100% of critical defects caught;
- ≥ 90% of the rest caught;
- zero invented facts.
