#!/bin/bash
# PreCompact (auto only): postpones automatic compaction while the project's checkpoint says "Safe to compact: no".
# Safety valves, so a forgotten "no" can't block forever:
#   - the checkpoint is older than 2 hours: allow
#   - the context is past a hard cap (threshold + 200k, at most 800k): allow
#   - anything unreadable or unknown: allow (fail open)
# Exit 2 blocks; Claude Code then skips this compaction and the conversation continues uncompacted.
command -v jq >/dev/null 2>&1 || exit 0
. "$(dirname "$0")/context-lib.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null || true)
TRIGGER=$(printf '%s' "$INPUT" | jq -r '.trigger // empty' 2>/dev/null)
[ "$TRIGGER" = "auto" ] || exit 0
CWD=$(printf '%s' "$INPUT" | jq -r '.cwd // empty' 2>/dev/null)
SESSION=$(printf '%s' "$INPUT" | jq -r '.session_id // empty' 2>/dev/null)
TRANSCRIPT=$(printf '%s' "$INPUT" | jq -r '.transcript_path // empty' 2>/dev/null)

[ -n "$CWD" ] && [ "$(checkpoint_busy "$CWD")" = "no" ] || exit 0

AGE=$(file_age "$CWD/PROGRESS.md")
[ -n "$AGE" ] && [ "$AGE" -lt 7200 ] || exit 0

WINDOW=$(compact_window); WINDOW=${WINDOW:-400000}
CAP=$(( WINDOW + 200000 )); [ "$CAP" -gt 800000 ] && CAP=800000
TOKENS=$(context_tokens "$TRANSCRIPT")
[ -n "$TOKENS" ] && [ "$TOKENS" -lt "$CAP" ] || exit 0

S=$(state_file "$SESSION")
N=$(( $(cat "$S.deferred" 2>/dev/null || echo 0) + 1 )); echo "$N" > "$S.deferred" 2>/dev/null
echo "mastertools-core: compaction postponed ($N) because PROGRESS.md says \"Safe to compact: no\". Finish the current step, save, and set it to yes." >&2
exit 2
