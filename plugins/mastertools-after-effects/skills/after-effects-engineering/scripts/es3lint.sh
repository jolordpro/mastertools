#!/bin/bash
# Ships with aerun.py in the after-effects-engineering skill. Source sha256 prefix 2a48000d97b51717, copied unchanged below this line.
# es3lint.sh — static QC gate for ExtendScript deliveries (Build Plan §8).
# Usage: qc/es3lint.sh file.jsx [file2.jsx ...]
# Checks: node syntax, ES3 feature lint, reserved-word-as-member grep,
# undo-group pairing, suppression pairing. Exit 0 = clean.

set -u
FAIL=0
TMPDIR_QC="$(mktemp -d)"
trap 'rm -rf "$TMPDIR_QC"' EXIT

for f in "$@"; do
  echo "== $f"
  if [ ! -f "$f" ]; then echo "   MISSING FILE"; FAIL=1; continue; fi

  cp "$f" "$TMPDIR_QC/check.js"
  if node --check "$TMPDIR_QC/check.js" 2>"$TMPDIR_QC/err"; then
    echo "   syntax: OK"
  else
    echo "   syntax: FAIL"; cat "$TMPDIR_QC/err" | head -5; FAIL=1
  fi

  # ES3 feature lint (word-boundary where it matters).
  # JSON.* is permitted ONLY in files that ship the guarded polyfill
  # (signature: "if (!JSON.stringify)") — everywhere else it is the
  # phantom-polyfill trap.
  # Accept the REAL guard (the self-verifying probe's function definition,
  # WO-16) or an explicit, deliberate opt-in marker. The old test matched
  # the literal string "if (!JSON.stringify)" anywhere - including inside
  # a COMMENT, which meant a file could whitelist itself just by talking
  # about the guard. Found during the Jul 27 finalization sweep.
  # Anchored to line-start so a mention inside a COMMENT no longer counts.
  if grep -qE 'function NOTES_JSON_HEALTHY\(|^[[:space:]]*if \(!JSON\.stringify\)|QC: JSON-OK' "$f"; then JSONPAT=''; else JSONPAT='JSON\.|'; fi
  if grep -nE '(^|[^A-Za-z0-9_])(let|const)[[:space:]]|=>|`|for[[:space:]]*\([^)]*[[:space:]]of[[:space:]]|async[[:space:]]|await[[:space:]]|\byield\b|'"$JSONPAT"'Object\.(keys|assign|values|entries|create|freeze)|\.(forEach|map|filter|reduce|some|every|find|findIndex|includes|trim|startsWith|endsWith|padStart|padEnd)\(|Date\.now|Promise|new[[:space:]]+(Set|Map|WeakMap)\b' "$f"; then
    echo "   ES3 lint: FAIL (matches above)"; FAIL=1
  else
    echo "   ES3 lint: OK"
  fi

  # Reserved words as bare keys/members (ES3 forbids; node --check permits)
  if grep -nE '\.(delete|default|class|new|return|in|for|with|case|typeof|instanceof)\b[[:space:]]*[^A-Za-z0-9_(]|[{,][[:space:]]*(default|delete|class|case|new|return|in|for|with)[[:space:]]*:' "$f"; then
    echo "   reserved-word grep: FAIL (matches above)"; FAIL=1
  else
    echo "   reserved-word grep: OK"
  fi

  BU=$(grep -c "beginUndoGroup" "$f" || true)
  EU=$(grep -c "endUndoGroup" "$f" || true)
  if [ "$BU" -eq "$EU" ]; then echo "   undo pairing: OK ($BU/$EU)"; else echo "   undo pairing: FAIL ($BU begin / $EU end)"; FAIL=1; fi

  BS=$(grep -c "beginSuppressDialogs" "$f" || true)
  ES=$(grep -c "endSuppressDialogs" "$f" || true)
  if [ "$BS" -eq "$ES" ]; then echo "   suppression pairing: OK ($BS/$ES)"; else echo "   suppression pairing: FAIL ($BS begin / $ES end)"; FAIL=1; fi
done

[ "$FAIL" -eq 0 ] && echo "== ALL CLEAN" || echo "== FAILURES PRESENT"
exit $FAIL
