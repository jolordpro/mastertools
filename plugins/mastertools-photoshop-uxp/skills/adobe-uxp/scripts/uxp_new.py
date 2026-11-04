#!/usr/bin/env python3
"""Scaffold a UXP plugin project from the skill's template.

  uxp_new.py <project-dir> --name "My Panel" --id com.nesn.mypanel [--apps PS,ID,PR] [--perm fs,code,launch]

Creates <project-dir>/uxp.config.json and <project-dir>/src/ (index.html, panel.css, main.js, icons/). The template
already avoids UXP's UI traps and logs to /private/tmp/<id>.<app>.log. Refuses to overwrite an existing project.

--perm picks requiredPermissions (default: fs):
  fs      localFileSystem: fullAccess            (read/write arbitrary paths, e.g. Dropbox, /private/tmp)
  code    allowCodeGenerationFromStrings: true   (run script files with AsyncFunction / new Function)
  launch  launchProcess file + common script extensions  (uxp.shell.openPath)
Then: write src/, run uxp_check.py, then uxp_build.py --install.
"""
import json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "assets", "template", "src")
APPS = ("PS", "ID", "PR", "AE", "AI")
PERMS = {
    "fs": {"localFileSystem": "fullAccess"},
    "code": {"allowCodeGenerationFromStrings": True},
    "launch": {"launchProcess": {"schemes": ["file"], "extensions": [".jsx", ".js", ".psjs", ".idjs"]}},
}


def opt(argv, name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    project = os.path.abspath(argv[0])
    name, pid = opt(argv, "--name"), opt(argv, "--id")
    if not name or not pid:
        sys.exit("--name and --id are required (e.g. --name \"My Panel\" --id com.nesn.mypanel)")
    if not re.match(r"^[a-z0-9]+(\.[a-z0-9-]+)+$", pid):
        sys.exit("--id should be reverse-DNS, lowercase, e.g. com.nesn.mypanel")
    apps = [a.strip().upper() for a in opt(argv, "--apps", "PS,ID,PR").split(",") if a.strip()]
    bad = [a for a in apps if a not in APPS]
    if bad:
        sys.exit("Unknown app(s) %s; choose from %s" % (bad, ", ".join(APPS)))
    perms = {}
    for p in opt(argv, "--perm", "fs").split(","):
        p = p.strip()
        if p not in PERMS:
            sys.exit("Unknown --perm %r; choose from %s" % (p, ", ".join(PERMS)))
        perms.update(PERMS[p])
    if os.path.exists(os.path.join(project, "uxp.config.json")) or os.path.exists(os.path.join(project, "src")):
        sys.exit("%s already has a uxp.config.json or src/; not overwriting." % project)

    os.makedirs(project, exist_ok=True)
    shutil.copytree(TEMPLATE, os.path.join(project, "src"))
    # The template stores 2x icons as "-2x" (claude.ai rejects "@" in skill zips); UXP's scale [1, 2] wants "@2x".
    icons = os.path.join(project, "src", "icons")
    for f in os.listdir(icons):
        if f.endswith("-2x.png"):
            os.rename(os.path.join(icons, f), os.path.join(icons, f[:-len("-2x.png")] + "@2x.png"))
    for f in ("index.html", "main.js"):
        p = os.path.join(project, "src", f)
        with open(p, encoding="utf-8") as fh:
            s = fh.read().replace("__NAME__", name)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(s)
    cfg = {
        "name": name, "id": pid, "version": "1.0.0", "apps": apps,
        "entrypoint": {"type": "panel", "id": "main", "label": name, "width": 300, "height": 520},
        "permissions": perms,
    }
    with open(os.path.join(project, "uxp.config.json"), "w", encoding="utf-8") as fh:
        json.dump(cfg, fh, indent=2); fh.write("\n")
    with open(os.path.join(project, ".gitignore"), "a", encoding="utf-8") as fh:
        fh.write("dist/\n")
    if any(a in ("AE", "AI") for a in apps):
        print("Note: After Effects and Illustrator refused homemade UXP plugins as of Oct 2026 (UPIA -411).")
    print("Created %s (apps: %s). Next: edit src/, then uxp_check.py, then uxp_build.py --install." % (project, ", ".join(apps)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
