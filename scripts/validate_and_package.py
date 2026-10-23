#!/usr/bin/env python3
"""Validate the security-foundations plugin and build a distributable zip.

Usage: python3 scripts/validate_and_package.py [output_dir]

Uses only the standard library. Exits non-zero if any check fails.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "security-foundations"
OUT_DIR = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT.parent
GPT_LIMIT = 8000
errors = []


def check(ok, msg):
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok:
        errors.append(msg)


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        check(False, f"{path.relative_to(ROOT)} is valid JSON ({exc})")
        return {}


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if km:
            fm[km.group(1)] = km.group(2).strip().strip('"')
    return fm


# --- manifests -------------------------------------------------------------
plugin = load_json(ROOT / ".claude-plugin" / "plugin.json")
market = load_json(ROOT / ".claude-plugin" / "marketplace.json")
gemini = load_json(ROOT / "gemini-extension.json")
evals = load_json(SKILL_DIR / "evals" / "evals.json")
check(bool(plugin) and bool(market) and bool(gemini) and bool(evals), "all JSON files parse")

version = plugin.get("version")
check(gemini.get("version") == version, f"gemini-extension version matches plugin version ({version})")
check(evals.get("version") == version, "evals.json version matches plugin version")
check(market.get("plugins", [{}])[0].get("name") == plugin.get("name"), "marketplace lists the plugin by name")

# --- skill files -----------------------------------------------------------
for fname in ("SKILL.md", "SKILL.ko.md"):
    fm = frontmatter(SKILL_DIR / fname)
    check(fm is not None, f"{fname} has YAML frontmatter")
    if not fm:
        continue
    desc = fm.get("description", "")
    check(fm.get("name") == "security-foundations", f"{fname} name is security-foundations")
    check(0 < len(desc) <= 1024, f"{fname} description length {len(desc)} <= 1024")
    check("<" not in desc and ">" not in desc, f"{fname} description has no angle brackets")
    allowed = {"name", "description", "license", "allowed-tools", "metadata", "compatibility", "version", "language"}
    check(set(fm) <= allowed | {"version", "language"}, f"{fname} frontmatter keys are allowed")
skill_text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
check(len(skill_text.splitlines()) < 500, "SKILL.md is under 500 lines")
check('version: "%s"' % version in skill_text, "SKILL.md metadata version matches plugin version")

for ref in re.findall(r"`(references/[\w.-]+\.md)`", skill_text):
    check((SKILL_DIR / ref).exists(), f"referenced file exists: {ref}")

# --- cross-platform adapters ----------------------------------------------
core = (ROOT / "adapters" / "core-instructions.md").read_text(encoding="utf-8")
check(len(core) <= GPT_LIMIT, f"core-instructions.md is {len(core)} characters (limit {GPT_LIMIT})")
for needle in ("Isolate", "ASI01-ASI10", "SLSA v1.2", "STOP RULES"):
    check(needle in core, f"core-instructions.md contains '{needle}'")
for fname in ("AGENTS.md", "GEMINI.md", "commands/foundations-check.md", "commands/foundations-check.toml"):
    check((ROOT / fname).exists(), f"{fname} exists")

# --- unverified claims must not come back ------------------------------------
for path in ROOT.rglob("*.md"):
    # These files document why the claim was removed, so they may name it.
    if path.name in {"standards-map.md", "README.md", "README.en.md"}:
        continue
    if "SHIELD" in path.read_text(encoding="utf-8"):
        check(False, f"no unverified SHIELD citation in {path.relative_to(ROOT)}")

if errors:
    print(f"\n{len(errors)} check(s) failed. No zip written.")
    sys.exit(1)

# --- packaging ---------------------------------------------------------------
EXCLUDE = {"__pycache__", ".DS_Store"}
OUT_DIR.mkdir(parents=True, exist_ok=True)
zip_path = OUT_DIR / f"security-foundations-plugin-v{version}.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT)
        if path.is_dir() or any(p in EXCLUDE for p in rel.parts) or path.suffix == ".pyc":
            continue
        zf.write(path, Path(ROOT.name) / rel)
print(f"\nAll checks passed. Wrote {zip_path}")
