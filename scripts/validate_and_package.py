#!/usr/bin/env python3
"""Validate the Security Foundations plugin and build its release assets.

Usage: python3 scripts/validate_and_package.py [output_dir]

Writes two files to output_dir (default: dist/):
  security-foundations-claude-skill.zip  Claude app upload (the skill folder)
  security-foundations-gpt-gemini-kit.zip ChatGPT GPT / Gemini Gem setup kit

Uses only the standard library. Exits non-zero if any check fails.
Archives are reproducible: entries are sorted and timestamps are fixed.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "security-foundations"
OUT_DIR = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "dist"
GPT_LIMIT = 8000
LANGUAGES = ("README.md", "README.ko.md", "README.zh-CN.md", "README.ja.md")
KNOWLEDGE = (
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "references" / "standards-map.md",
    SKILL_DIR / "references" / "failure-modes.md",
    SKILL_DIR / "references" / "incident-runbook.md",
)
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
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

version = plugin.get("version", "")
check(bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), f"plugin version is semver ({version})")
check(gemini.get("version") == version, "gemini-extension version matches plugin version")
check(evals.get("version") == version, "evals.json version matches plugin version")
check(market.get("plugins", [{}])[0].get("name") == plugin.get("name"), "marketplace lists the plugin by name")
check(bool(plugin.get("license")), "plugin.json declares a license")

# --- skill files -----------------------------------------------------------
allowed = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
for fname in ("SKILL.md", "SKILL.ko.md"):
    fm = frontmatter(SKILL_DIR / fname)
    check(fm is not None, f"{fname} has YAML frontmatter")
    if not fm:
        continue
    desc = fm.get("description", "")
    check(fm.get("name") == "security-foundations", f"{fname} name is security-foundations")
    check(0 < len(desc) <= 1024, f"{fname} description length {len(desc)} <= 1024")
    check("<" not in desc and ">" not in desc, f"{fname} description has no angle brackets")
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
for fname in ("AGENTS.md", "GEMINI.md", "LICENSE", "SECURITY.md", "adapters/README.md",
              "commands/foundations-check.md", "commands/foundations-check.toml"):
    check((ROOT / fname).exists(), f"{fname} exists")

# --- documentation -----------------------------------------------------------
for fname in LANGUAGES:
    path = ROOT / fname
    check(path.exists(), f"{fname} exists")
    if path.exists():
        text = path.read_text(encoding="utf-8")
        others = [n for n in LANGUAGES if n != fname]
        check(all(n in text for n in others), f"{fname} links to every other language")

# --- unverified claims must not come back ------------------------------------
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts or "dist" in path.parts:
        continue
    if "SHIELD" in path.read_text(encoding="utf-8"):
        check(False, f"no unverified SHIELD citation in {path.relative_to(ROOT)}")

if errors:
    print(f"\n{len(errors)} check(s) failed. Nothing written.")
    sys.exit(1)


# --- packaging ---------------------------------------------------------------
def write_zip(zip_path, entries):
    """entries: iterable of (archive_name, source_path)."""
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, src in sorted(entries):
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, src.read_bytes())
    print(f"Wrote {zip_path}")


OUT_DIR.mkdir(parents=True, exist_ok=True)

skill_entries = [
    (f"security-foundations/{p.relative_to(SKILL_DIR).as_posix()}", p)
    for p in SKILL_DIR.rglob("*")
    if p.is_file() and "evals" not in p.relative_to(SKILL_DIR).parts and p.name != ".DS_Store"
]
write_zip(OUT_DIR / "security-foundations-claude-skill.zip", skill_entries)

kit_entries = [
    ("security-foundations-kit/README.md", ROOT / "adapters" / "README.md"),
    ("security-foundations-kit/instructions.md", ROOT / "adapters" / "core-instructions.md"),
] + [(f"security-foundations-kit/knowledge/{p.name}", p) for p in KNOWLEDGE]
write_zip(OUT_DIR / "security-foundations-gpt-gemini-kit.zip", kit_entries)

print(f"\nAll checks passed. Version {version}.")
