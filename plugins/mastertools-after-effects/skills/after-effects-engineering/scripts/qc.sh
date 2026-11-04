#!/usr/bin/env bash
# =============================================================================
# qc.sh — portable static QC gate for After Effects ScriptUI panels & CEP
#         extensions. Generalized from a production CEP project's qc.sh.
#
# Usage:   bash qc.sh [PATH ...]      (default PATH = current directory)
#          bash qc.sh --help
#
# Scans for ExtendScript hosts (*.jsx), CEP clients (*.js), CEP HTML
# (index.html), and CEP manifests (manifest.xml), then runs:
#   1. Host syntax        — node --check (after stripping #target/#include)
#   2. Client syntax      — node --check
#   3. ES3 purity (hosts) — no let/const/=>/template-literals/ES5 methods
#   4. Polyfill presence  — a host using JSON.* should ship a guarded polyfill
#   5. Called-vs-defined  — every bare call resolves (catches the ReferenceError
#                           that node --check misses, e.g. an undefined helper)
#   6. Undo-group pairing — beginUndoGroup count <= endUndoGroup count
#   7. HTML integrity     — <div> balance + every getElementById() id exists
#   8. Manifest           — well-formed XML + ExtensionBundleVersion parity
#
# Static checks are NECESSARY BUT NOT SUFFICIENT. The real DOM test is the
# human running the tool in the actual app (no DOM unit-test harness exists),
# plus the cold-start test (quit app, reopen with no Libraries/Learning panels).
# Exits non-zero if any check fails.
# =============================================================================
set -u

if [ "${1:-}" = "--help" ] || [ "${1:-}" = "-h" ]; then
  sed -n '2,25p' "$0" | sed 's/^# \{0,1\}//'
  exit 0
fi

ROOT="${1:-.}"
[ -e "$ROOT" ] || { echo "qc.sh: no such path: $ROOT"; exit 2; }
FAIL=0
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

c_red=$'\033[31m'; c_grn=$'\033[32m'; c_yel=$'\033[33m'; c_bold=$'\033[1m'; c_off=$'\033[0m'
ok(){   printf '  %s✓%s %s\n' "$c_grn" "$c_off" "$1"; }
bad(){  printf '  %s✗%s %s\n' "$c_red" "$c_off" "$1"; FAIL=1; }
note(){ printf '  %s•%s %s\n' "$c_yel" "$c_off" "$1"; }
hdr(){  printf '\n%s== %s ==%s\n' "$c_bold" "$1" "$c_off"; }

command -v node >/dev/null 2>&1 || { echo "qc.sh needs Node.js (node) on PATH."; exit 2; }

# ---- gather files (skip vendored CSInterface.js, node_modules, .git, *.min.js)
HOSTS=(); CLIENTS=(); HTMLS=(); MANIFESTS=()
while IFS= read -r f; do HOSTS+=("$f"); done < <(find "$ROOT" -type f -name '*.jsx' \
  -not -path '*/node_modules/*' -not -path '*/.git/*' 2>/dev/null)
while IFS= read -r f; do CLIENTS+=("$f"); done < <(find "$ROOT" -type f -name '*.js' \
  -not -name 'CSInterface.js' -not -name '*.min.js' \
  -not -path '*/node_modules/*' -not -path '*/.git/*' 2>/dev/null)
while IFS= read -r f; do HTMLS+=("$f"); done < <(find "$ROOT" -type f -name 'index.html' \
  -not -path '*/node_modules/*' -not -path '*/.git/*' 2>/dev/null)
while IFS= read -r f; do MANIFESTS+=("$f"); done < <(find "$ROOT" -type f -name 'manifest.xml' \
  -not -path '*/node_modules/*' -not -path '*/.git/*' 2>/dev/null)

printf '%sQC scan of:%s %s   (hosts:%d clients:%d html:%d manifests:%d)\n' \
  "$c_bold" "$c_off" "$ROOT" "${#HOSTS[@]}" "${#CLIENTS[@]}" "${#HTMLS[@]}" "${#MANIFESTS[@]}"
if [ $(( ${#HOSTS[@]} + ${#CLIENTS[@]} + ${#HTMLS[@]} + ${#MANIFESTS[@]} )) -eq 0 ]; then
  echo "qc.sh: nothing to check under $ROOT (no .jsx, .js, index.html or manifest.xml). Wrong folder?"
  exit 2
fi

# ---------------------------------------------------------------- 1. host syntax
hdr "Host syntax (ES3 .jsx -> node --check)"
if [ "${#HOSTS[@]}" -eq 0 ]; then note "no .jsx hosts found"; fi
for h in ${HOSTS[@]+"${HOSTS[@]}"}; do
  strip="$TMP/$(echo "$h" | tr '/ ' '__').js"
  grep -v -E '^[[:space:]]*#(target|targetengine|include|script|engine)' "$h" \
    | grep -v -E '^[[:space:]]*//@(include|target)' > "$strip"
  if node --check "$strip" 2>"$TMP/err"; then ok "$h"; else bad "$h syntax: $(head -1 "$TMP/err")"; fi
done

# -------------------------------------------------------------- 2. client syntax
hdr "Client syntax (.js -> node --check)"
if [ "${#CLIENTS[@]}" -eq 0 ]; then note "no .js clients found"; fi
for c in ${CLIENTS[@]+"${CLIENTS[@]}"}; do
  if node --check "$c" 2>"$TMP/err"; then ok "$c"; else bad "$c syntax: $(head -1 "$TMP/err")"; fi
done

# ------------------------------------------------------------- 3. ES3 purity (hosts)
hdr "ES3 purity (hosts only — no let/const/arrow/ES5 methods)"
ES3_RE='\b(let|const)\b|=>|`|\b(async|await)\b|\b(Set|Map|WeakMap|Promise)\b|\bArray\.(from|of|isArray)\b|\bObject\.(keys|values|entries|assign|create)\b|\.(forEach|map|filter|reduce|some|every|find|findIndex|includes)[[:space:]]*\(|\.(trim|startsWith|endsWith|padStart|padEnd|repeat)[[:space:]]*\('
for h in ${HOSTS[@]+"${HOSTS[@]}"}; do
  # strip line + block comments before grepping to avoid false hits in prose
  nocom="$TMP/$(echo "$h" | tr '/ ' '__').nocom"
  node -e 'const fs=require("fs");let s=fs.readFileSync(process.argv[1],"utf8");s=s.replace(/\/\*[\s\S]*?\*\//g,m=>m.replace(/[^\n]/g," ")).replace(/\/\/[^\n]*/g,"");process.stdout.write(s);' "$h" > "$nocom"
  if grep -nE "$ES3_RE" "$nocom" > "$TMP/hits" 2>/dev/null; then
    bad "$h: ES5+ construct(s):"; sed 's/^/      /' "$TMP/hits"
  else ok "$h: ES3-clean"; fi
done

# ------------------------------------------------------- 4. polyfill presence (hosts)
hdr "Guarded-polyfill presence (hosts using JSON)"
for h in ${HOSTS[@]+"${HOSTS[@]}"}; do
  if grep -qE '\bJSON\.(parse|stringify)\b' "$h"; then
    if grep -qE 'typeof[[:space:]]+JSON|JSON[[:space:]]*===[[:space:]]*"undefined"|!.?JSON|JSON[[:space:]]*=[[:space:]]*\{|JSON[[:space:]]*=[[:space:]]*JSON' "$h"; then
      ok "$h: uses JSON with a guard"
    else
      note "$h: uses JSON.* but no guarded polyfill found — Adobe panels inject JSON, so this fails cold-start. Ship a guarded JSON polyfill at the top."
    fi
  fi
done

# ----------------------------------------------------- 5. called-vs-defined (hosts)
hdr "Called-vs-defined (hosts — catches undefined-helper ReferenceErrors)"
cat > "$TMP/cvd.js" <<'NODE'
const fs = require("fs");
const ALLOW = new Set([
 // keywords / control
 "if","for","while","switch","catch","return","function","typeof","new","delete","void","in",
 "instanceof","with","throw","else","do","var","case","try","finally","break","continue",
 // ES3 globals & ctors
 "Array","Object","String","Number","Boolean","Math","Date","RegExp","Error","TypeError",
 "RangeError","ReferenceError","SyntaxError","EvalError","URIError",
 "parseInt","parseFloat","isNaN","isFinite","eval","encodeURI","decodeURI",
 "encodeURIComponent","decodeURIComponent","escape","unescape",
 // ExtendScript / ScriptUI / AE host globals commonly *called*
 "File","Folder","Window","UnitValue","ScriptUI","XML","Namespace","QName","localize",
 "alert","confirm","prompt","isXMLName","CompItem","Layer","FootageItem","SolidSource",
 // JSON is polyfilled
 "JSON",
]);
function line(src, i){ return src.slice(0, i).split("\n").length; }
let bad = 0;
for (const f of process.argv.slice(2)) {
  let src;
  try { src = fs.readFileSync(f, "utf8"); } catch (e) { continue; }
  // rough strip of comments + string/regex-ish literals so we don't match inside them
  src = src.replace(/\/\*[\s\S]*?\*\//g, " ")
           .replace(/\/\/[^\n]*/g, " ")
           .replace(/"(?:\\.|[^"\\])*"/g, '""')
           .replace(/'(?:\\.|[^'\\])*'/g, "''");
  const defined = new Set();
  let m;
  const re1 = /function\s+([A-Za-z_$][\w$]*)/g;          while ((m = re1.exec(src))) defined.add(m[1]);
  const re2 = /([A-Za-z_$][\w$]*)\s*=\s*function\b/g;    while ((m = re2.exec(src))) defined.add(m[1]);
  const re3 = /([A-Za-z_$][\w$]*)\s*:\s*function\b/g;    while ((m = re3.exec(src))) defined.add(m[1]);
  // bare calls: NAME( not preceded by '.' or an identifier char
  const rec = /(^|[^.\w$])([A-Za-z_$][\w$]*)\s*\(/g;
  const seen = new Set();
  while ((m = rec.exec(src))) {
    const n = m[2];
    if (seen.has(n)) continue; seen.add(n);
    if (defined.has(n) || ALLOW.has(n)) continue;
    console.log(`  ✗ ${f}: call to undefined '${n}(' near line ${line(src, m.index)}`);
    bad = 1;
  }
}
process.exit(bad);
NODE
if [ "${#HOSTS[@]}" -gt 0 ]; then
  if node "$TMP/cvd.js" "${HOSTS[@]}"; then ok "every bare call resolves"; else FAIL=1; fi
fi

# ----------------------------------------------------- 6. undo-group pairing (hosts)
hdr "Undo-group pairing (beginUndoGroup <= endUndoGroup)"
for h in ${HOSTS[@]+"${HOSTS[@]}"}; do
  b=$(grep -c 'beginUndoGroup' "$h"); e=$(grep -c 'endUndoGroup' "$h")
  if [ "$b" -eq 0 ] && [ "$e" -eq 0 ]; then continue; fi
  if [ "$b" -gt "$e" ]; then bad "$h: $b beginUndoGroup but only $e endUndoGroup (unclosed group)";
  else ok "$h: $b begin / $e end (a catch+success pair making end>begin is fine)"; fi
done

# ----------------------------------------------------------- 7. HTML integrity
hdr "HTML integrity (div balance + getElementById resolution)"
if [ "${#HTMLS[@]}" -eq 0 ]; then note "no index.html found (ScriptUI tool? — skip)"; fi
for html in ${HTMLS[@]+"${HTMLS[@]}"}; do
  o=$(grep -o '<div' "$html" | wc -l | tr -d ' '); cl=$(grep -o '</div>' "$html" | wc -l | tr -d ' ')
  if [ "$o" -eq "$cl" ]; then ok "$html: <div> balanced ($o)"; else bad "$html: <div>=$o vs </div>=$cl"; fi
  dir="$(dirname "$html")"
  missing=0
  for c in ${CLIENTS[@]+"${CLIENTS[@]}"}; do
    [ "$(dirname "$c")" = "$dir" ] || continue
    while IFS= read -r id; do
      [ -n "$id" ] || continue
      if ! grep -qE "id=[\"']${id}[\"']" "$html"; then
        bad "$html: getElementById(\"$id\") has no matching element (in $(basename "$c"))"; missing=1
      fi
    done < <(grep -oE 'getElementById\(["'"'"']([^"'"'"']+)' "$c" | sed -E 's/.*\(["'"'"']//')
  done
  [ "$missing" -eq 0 ] && ok "$html: every getElementById resolves"
done

# ------------------------------------------------------------- 8. manifests
hdr "Manifests (well-formed XML + version parity)"
if [ "${#MANIFESTS[@]}" -eq 0 ]; then note "no manifest.xml found"; fi
ver=""
for mf in ${MANIFESTS[@]+"${MANIFESTS[@]}"}; do
  if python3 -c 'import sys,xml.dom.minidom as x; x.parse(sys.argv[1])' "$mf" 2>"$TMP/xerr"; then
    ok "$mf parses"
  else bad "$mf XML error: $(head -1 "$TMP/xerr")"; continue; fi
  v=$(grep -oE 'ExtensionBundleVersion="[^"]+"' "$mf" | head -1 | sed -E 's/.*="([^"]+)".*/\1/')
  if [ -n "$v" ]; then
    if [ -z "$ver" ]; then ver="$v"; ok "ExtensionBundleVersion=$v";
    elif [ "$ver" != "$v" ]; then bad "version parity: $v != $ver"; else ok "version parity: $v"; fi
  fi
done

# ---------------------------------------------------------------- summary
printf '\n'
if [ "$FAIL" -eq 0 ]; then
  printf '%sALL STATIC CHECKS PASSED.%s Necessary, not sufficient — now run it in the app (and the cold-start test).\n' "$c_grn$c_bold" "$c_off"
  exit 0
else
  printf '%sQC FAILED — fix the ✗ items above.%s\n' "$c_red$c_bold" "$c_off"
  exit 1
fi
