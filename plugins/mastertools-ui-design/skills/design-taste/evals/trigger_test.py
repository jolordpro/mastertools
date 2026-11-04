#!/usr/bin/env python3
"""Does design-taste fire when it should, next to frontend-design and all the user's other skills?

Loads an unreleased copy of the skill as a temporary plugin (--plugin-dir) on top of everything
installed, runs each prompt in `claude -p` with Skill as the only tool, and records every Skill
call made in the first assistant turns (stops after 3 calls or 4 turns).
usage: trigger_test.py <skill_dir> [--runs N] > results.jsonl
"""
import argparse, json, os, shutil, subprocess, tempfile, time
from concurrent.futures import ThreadPoolExecutor

PROMPTS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "trigger_prompts.json")))
# Optional: a folder of uploaded skills to load as well (DT_TRIGGER_UPLOADS).
UPLOADS = os.path.expanduser(os.environ.get("DT_TRIGGER_UPLOADS", ""))
KEEP_ENV = ("HOME", "PATH", "USER", "LOGNAME", "SHELL", "TMPDIR", "LANG", "TERM")
# frontend-design is not loaded in headless runs by default; load it so the test is "alongside frontend-design".
FRONTEND = os.path.expanduser("~/.claude/plugins/marketplaces/claude-plugins-official/plugins/frontend-design")
# An installed plugin that carries design-taste under the same name must be off for the run, or a pass may
# come from the installed copy instead of the one under test. Name them in DT_TRIGGER_DISABLE ("plugin@marketplace,...").
DISABLE = [p for p in os.environ.get("DT_TRIGGER_DISABLE", "").split(",") if p.strip()]
SETTINGS = json.dumps({"disableAllHooks": True, "disableClaudeAiConnectors": True,
                       "enabledPlugins": {p.strip(): False for p in DISABLE}})

def run(prompt, plugin, cwd):
    env = {k: os.environ[k] for k in KEEP_ENV if k in os.environ}
    cmd = ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose", "--max-turns", "4",
           "--tools", "Skill", "--allowedTools", "Skill", "--no-session-persistence", "--strict-mcp-config",
           "--settings", SETTINGS, "--plugin-dir", plugin]
    if os.path.isdir(FRONTEND):
        cmd += ["--plugin-dir", FRONTEND]
    if UPLOADS and os.path.isdir(UPLOADS):
        cmd += ["--plugin-dir", UPLOADS]
    p = subprocess.Popen(cmd, cwd=cwd, env=env, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    skills, listed = [], None
    t0 = time.time()
    for line in p.stdout:
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "system" and ev.get("subtype") == "init":
            listed = [s for s in (ev.get("skills") or []) if "design-taste" in s or "frontend-design" in s]
        if ev.get("type") == "assistant":
            for b in ev.get("message", {}).get("content", []):
                if b.get("type") == "tool_use" and b.get("name") == "Skill":
                    skills.append(b.get("input", {}).get("skill"))
        if len(skills) >= 3:
            p.terminate(); break
    try:
        p.wait(timeout=240)
    except subprocess.TimeoutExpired:
        p.kill()
    return {"skills": skills, "listed": listed, "secs": round(time.time() - t0, 1)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skill_dir")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--only", help="comma-separated prompt ids")
    a = ap.parse_args()
    plugin = tempfile.mkdtemp(prefix="dt-plugin-")
    os.makedirs(os.path.join(plugin, ".claude-plugin"))
    json.dump({"name": "dt-test", "description": "unreleased design-taste"}, open(os.path.join(plugin, ".claude-plugin", "plugin.json"), "w"))
    shutil.copytree(a.skill_dir, os.path.join(plugin, "skills", "design-taste"))
    cwd = tempfile.mkdtemp(prefix="dt-cwd-")
    prompts = [p for p in PROMPTS if not a.only or p["id"] in a.only.split(",")]
    jobs = [(p, r) for p in prompts for r in range(a.runs)]
    def work(j):
        p, r = j
        res = run(p["prompt"], plugin, cwd)
        fired = any(s and s.endswith("design-taste") for s in res["skills"])
        res.update({"id": p["id"], "run": r, "expect": p["expect"], "pass": fired == p["expect"],
                    "frontend_too": any(s and s.endswith("frontend-design") for s in res["skills"])})
        print(json.dumps(res), flush=True)
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(work, jobs))

if __name__ == "__main__":
    main()
