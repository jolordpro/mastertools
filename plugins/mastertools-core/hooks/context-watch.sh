#!/bin/bash
# PostToolUse: tells Claude when automatic compaction is close, so it can reach a safe point first.
# Speaks once at 85% of the threshold, then again for each 25k tokens past the threshold. Silent otherwise.
command -v jq >/dev/null 2>&1 || exit 0
. "$(dirname "$0")/context-lib.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null || true)
SESSION=$(printf '%s' "$INPUT" | jq -r '.session_id // empty' 2>/dev/null)
TRANSCRIPT=$(printf '%s' "$INPUT" | jq -r '.transcript_path // empty' 2>/dev/null)
CWD=$(printf '%s' "$INPUT" | jq -r '.cwd // empty' 2>/dev/null)

WINDOW=$(compact_window); [ -n "$WINDOW" ] || exit 0
TOKENS=$(context_tokens "$TRANSCRIPT"); [ -n "$TOKENS" ] || exit 0
WARN=$(( WINDOW * 85 / 100 ))
S=$(state_file "$SESSION")
# Below the warning line (including right after a compaction): reset, so the next climb warns again.
[ "$TOKENS" -ge "$WARN" ] || { rm -f "$S.band" "$S.deferred" 2>/dev/null; exit 0; }

# Band 0 = the 85% warning; band 1+ = each 25k step past the threshold.
if [ "$TOKENS" -lt "$WINDOW" ]; then BAND=0; else BAND=$(( (TOKENS - WINDOW) / 25000 + 1 )); fi
LAST=$(cat "$S.band" 2>/dev/null || echo -1)
[ "$BAND" -gt "$LAST" ] || exit 0
echo "$BAND" > "$S.band" 2>/dev/null

if [ "$BAND" -eq 0 ]; then
  MSG="mastertools-core: compaction is close (about ${TOKENS} of ${WINDOW} tokens). Finish the current atomic step, save, and update the ## Now checkpoint in PROGRESS.md. Don't start a new multi-step operation until compaction has run."
else
  MSG="mastertools-core: past the compaction threshold (about ${TOKENS} tokens)."
  [ "$(checkpoint_busy "${CWD:-.}")" = "no" ] && MSG="$MSG Compaction is postponed while PROGRESS.md says \"Safe to compact: no\". Finish the step, save, and set it to yes as soon as you can."
fi
jq -n --arg m "$MSG" '{hookSpecificOutput: {hookEventName: "PostToolUse", additionalContext: $m}}'
exit 0
