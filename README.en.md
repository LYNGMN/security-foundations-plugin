# Security Foundations plugin

An advisory skill that diagnoses an organization's security posture from its foundations and produces evidence-based control plans. Each answer has four parts: asset and blind-spot diagnosis, layered control matrix with standard references, executable runbook, and verification with residual risk.

Aligned with NIST CSF 2.0, ISO/IEC 27001:2022, NIST SP 800-61r3, SP 800-63B Rev.4, OWASP Top 10 for Agentic Applications 2026, and SLSA v1.2.

## Where it runs

| Environment | Format | Files |
|---|---|---|
| Claude Code / Cowork | Plugin | `.claude-plugin/`, `skills/`, `commands/` |
| Claude apps | Skill upload | `claude-ai-upload/security-foundations.skill` |
| ChatGPT | Custom GPT | `adapters/core-instructions.md` plus four knowledge files |
| Gemini web app | Gem | same as ChatGPT |
| Gemini CLI | Extension | `gemini-extension.json`, `GEMINI.md`, `commands/*.toml` |
| Codex and other AGENTS.md readers | Context file | `AGENTS.md` plus the `skills/` folder |

Claude Code install:

```
/plugin marketplace add ./security-foundations-plugin
/plugin install security-foundations@security-foundations-marketplace
```

Setup details for ChatGPT and Gemini are in `adapters/*/README.md` (written in Korean). Install steps may differ by tool version. This package was validated for file format, versions and instruction length, but it was not test-installed in each product.

## Validate and package

```
python3 scripts/validate_and_package.py [output_dir]
```

Korean documentation is in `README.md`; the Korean skill mirror is `skills/security-foundations/SKILL.ko.md`.

## Verification notes

SLSA v1.2 and MITRE ATLAS v5.4.0 counts were checked against the publishers' sites; other versions in `references/standards-map.md` were not re-checked. A framework called "SHIELD" from the source draft could not be found as a published standard and was replaced with a neutral internal checklist. No license is set yet.
