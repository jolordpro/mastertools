#!/usr/bin/env python3
"""Build (and optionally install) a UXP plugin as one .ccx per Adobe app, from <project>/uxp.config.json + <project>/src/.

  uxp_build.py <project>                 bump patch version, build dist/<Name>-<APP>.ccx for every app in the config
  uxp_build.py <project> --install       ...then install each through Adobe's UPIA (per user, no admin) and report
  uxp_build.py <project> --apps PS,PR    only these apps
  uxp_build.py <project> --no-bump       keep the version (UPIA will NOT update an installed copy of the same version)
  uxp_build.py <project> --list          what UPIA has installed for this plugin
  uxp_build.py <project> --remove        uninstall this plugin (all apps)

Why one package per app: each gets its own id (<id>.<app>), so an app that refuses the plugin can't block the others.
Why the bump is the default: UPIA prints "Installation Successful" for an unchanged version and keeps the OLD files.

uxp.config.json:
  { "name": "My Panel", "id": "com.nesn.mypanel", "version": "1.0.0", "apps": ["PS", "ID", "PR"],
    "entrypoint": {"id": "main", "label": "My Panel", "width": 300, "height": 520},
    "permissions": {"localFileSystem": "fullAccess"},
    "minVersions": {"PS": "24.0.0"},            (optional overrides)
    "appConfig": {"PS": {"types": [".jsx"]}} }  (optional, merged into window.UXP_CFG for that app)
"""
import json, os, re, subprocess, sys, zipfile

# key: (manifest host id, default minVersion, display name). Accepting homemade plugins as of Oct 2026: PS, ID, PR.
HOSTS = {
    "PS": ("PS", "24.0.0", "Photoshop"),
    "ID": ("ID", "18.5.0", "InDesign"),
    "PR": ("premierepro", "25.6.0", "Premiere Pro"),
    "AE": ("aftereffects", "26.0.0", "After Effects"),
    "AI": ("AI", "30.0.0", "Illustrator"),
}
UPIA = ("/Library/Application Support/Adobe/Adobe Desktop Common/RemoteComponents/UPI/UnifiedPluginInstallerAgent/"
        "UnifiedPluginInstallerAgent.app/Contents/MacOS/UnifiedPluginInstallerAgent")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def load_config(project):
    p = os.path.join(project, "uxp.config.json")
    if not os.path.isfile(p):
        sys.exit("No uxp.config.json in %s (scaffold one with uxp_new.py)" % project)
    with open(p, encoding="utf-8") as f:
        cfg = json.load(f)
    for k in ("name", "id", "version", "apps"):
        if k not in cfg:
            sys.exit("uxp.config.json is missing '%s'" % k)
    if not SEMVER.match(cfg["version"]):
        sys.exit("version must look like 1.2.3, got %r" % cfg["version"])
    bad = [a for a in cfg["apps"] if a not in HOSTS]
    if bad:
        sys.exit("Unknown app key(s) %s; use %s" % (bad, ", ".join(HOSTS)))
    return p, cfg


def bump(version):
    a, b, c = (int(x) for x in version.split("."))
    return "%d.%d.%d" % (a, b, c + 1)


def icon_list(src, base, species, size):
    if not os.path.isfile(os.path.join(src, "icons", base + ".png")):
        return None
    return [{"width": size, "height": size, "path": "icons/%s.png" % base, "scale": [1, 2], "theme": ["all"], "species": [species]}]


def manifest(cfg, key, src):
    host, minv, _ = HOSTS[key]
    ep = cfg.get("entrypoint", {})
    w, h = ep.get("width", 300), ep.get("height", 520)
    entry = {
        "type": ep.get("type", "panel"), "id": ep.get("id", "main"), "label": {"default": ep.get("label", cfg["name"])},
    }
    if entry["type"] == "panel":
        entry.update({
            "minimumSize": {"width": ep.get("minWidth", 200), "height": ep.get("minHeight", 220)},
            "maximumSize": {"width": 1200, "height": 2400},
            "preferredDockedSize": {"width": w, "height": h}, "preferredFloatingSize": {"width": w, "height": h},
        })
        icons = icon_list(src, "icon", "generic", 23)
        if icons:
            entry["icons"] = icons
    m = {
        "manifestVersion": 5, "id": "%s.%s" % (cfg["id"], key.lower()), "name": cfg["name"], "version": cfg["version"],
        "main": cfg.get("main", "index.html"),
        "host": {"app": host, "minVersion": cfg.get("minVersions", {}).get(key, minv)},
        "entrypoints": [entry],
        "requiredPermissions": cfg.get("permissions", {}),
    }
    plugin_icons = icon_list(src, "plugin", "pluginList", 48)
    if plugin_icons:
        m["icons"] = plugin_icons
    return m


def safe(name):
    return re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-") or "plugin"


def build(project, cfg, keys):
    src = os.path.join(project, cfg.get("src", "src"))
    dist = os.path.join(project, cfg.get("dist", "dist"))
    os.makedirs(dist, exist_ok=True)
    outs = []
    for key in keys:
        out = os.path.join(dist, "%s-%s.ccx" % (safe(cfg["name"]), key))
        app_cfg = {"key": key, "id": "%s.%s" % (cfg["id"], key.lower()), "name": cfg["name"], "version": cfg["version"],
                   "app": HOSTS[key][2]}
        app_cfg.update(cfg.get("appConfig", {}).get(key, {}))
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("manifest.json", json.dumps(manifest(cfg, key, src), indent=2))
            z.writestr("config.js", "window.UXP_CFG = %s;\n" % json.dumps(app_cfg))
            for root, dirs, files in os.walk(src):
                dirs[:] = [d for d in dirs if not d.startswith(".")]
                for f in files:
                    if f.startswith(".") or (root == src and f in ("manifest.json", "config.js")):
                        continue
                    p = os.path.join(root, f)
                    z.write(p, os.path.relpath(p, src))
        outs.append((key, out))
        print("built %s  (v%s)" % (os.path.relpath(out, project), cfg["version"]))
    return outs


def upia(*args):
    if not os.path.exists(UPIA):
        sys.exit("Adobe's plugin installer (UPIA) isn't on this Mac; install Creative Cloud first.")
    r = subprocess.run([UPIA] + list(args), capture_output=True, text=True)
    return (r.stdout + r.stderr).strip()


def install(outs):
    ok = []
    for key, path in outs:
        last = upia("--install", path).splitlines()[-1:] or [""]
        last = last[0]
        if "Successful" in last:
            print("%s: installed. Restart %s to load it." % (key, HOSTS[key][2])); ok.append(key)
        elif "-411" in last:
            print("%s: %s doesn't accept homemade UXP plugins (UPIA -411). Package kept in dist/." % (key, HOSTS[key][2]))
        else:
            print("%s: %s" % (key, last))
    return ok


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    project = os.path.abspath(argv[0])
    flags = argv[1:]
    path, cfg = load_config(project)
    keys = cfg["apps"]
    if "--apps" in flags:
        keys = [k.strip().upper() for k in flags[flags.index("--apps") + 1].split(",") if k.strip()]
    if "--list" in flags:
        head, show = "", False
        for line in upia("--list", "all").splitlines():
            if "installed for" in line:
                head = line
            elif cfg["name"] in line:
                print(head.strip()); print("   " + line.strip()); show = True
        if not show:
            print("Not installed in any app.")
        return 0
    if "--remove" in flags:
        print(upia("--remove", cfg["name"])); return 0
    if "--no-bump" not in flags:
        cfg["version"] = bump(cfg["version"])
        with open(path, "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=2); f.write("\n")
    outs = build(project, cfg, keys)
    if "--install" in flags:
        install(outs)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
