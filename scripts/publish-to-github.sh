#!/usr/bin/env bash
# Publish this plugin folder to GitHub with the GitHub CLI.
# Run from anywhere:  bash scripts/publish-to-github.sh [repo-name] [--private|--public]
# Defaults: repo name "security-foundations-plugin", private. Public needs a LICENSE file.
set -euo pipefail
cd "$(dirname "$0")/.."

REPO="${1:-security-foundations-plugin}"
VIS="${2:---private}"

command -v git >/dev/null || { echo "git is required."; exit 1; }
command -v gh  >/dev/null || { echo "GitHub CLI (gh) is required. Install it, or push manually (see README.md)."; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "Not logged in. Run 'gh auth login' first."; exit 1; }

if [ "$VIS" = "--public" ] && [ ! -f LICENSE ]; then
  echo "Add a LICENSE file (and a license field in .claude-plugin/plugin.json) before publishing publicly."
  exit 1
fi

# Validate before publishing; the zip goes to a temp folder and is discarded.
python3 scripts/validate_and_package.py "$(mktemp -d)"

[ -d .git ] || git init -b main
git add -A
VERSION="$(python3 -c 'import json; print(json.load(open(".claude-plugin/plugin.json"))["version"])')"
git commit -m "security-foundations v${VERSION}" || echo "Nothing new to commit."
gh repo create "$REPO" "$VIS" --source=. --push

OWNER="$(gh api user -q .login)"
echo
echo "Published: https://github.com/${OWNER}/${REPO}"
echo "Claude Code : /plugin marketplace add ${OWNER}/${REPO}"
echo "              /plugin install security-foundations@security-foundations-marketplace"
echo "Gemini CLI  : gemini extensions install https://github.com/${OWNER}/${REPO}"
echo "Codex       : clone the repo and copy skills/security-foundations to ~/.agents/skills/"
