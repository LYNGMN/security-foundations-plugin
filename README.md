# Security Foundations

**English** · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Release](https://img.shields.io/github/v/release/LYNGMN/security-foundations-plugin)](https://github.com/LYNGMN/security-foundations-plugin/releases/latest)
[![Validate](https://github.com/LYNGMN/security-foundations-plugin/actions/workflows/validate.yml/badge.svg)](https://github.com/LYNGMN/security-foundations-plugin/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A security advisor for your AI assistant. Ask a security question in plain words, and it answers like an experienced security lead: it first finds out what you actually have, then gives you a plan you can act on and check.

Works with **Claude** (app and Claude Code), **ChatGPT**, **Gemini** (web and CLI) and **Codex**. Answers in the language you write in.

## What you get

Every answer comes in the same four parts, so you can hand it to a teammate or an auditor:

| Part | What it tells you |
|---|---|
| 1. Asset and blind-spot diagnosis | What you have, what nobody owns, and what you cannot prove is protected |
| 2. Control plan | What to put in place, layer by layer, with the standard behind each item and its cost to operations |
| 3. Step-by-step runbook | Numbered actions someone can follow today |
| 4. Verification and remaining risk | How to test that each control works, and what is still exposed |

Good questions to try:

- *"An employee opened a phishing attachment and their PC is acting strange. What do we do first?"*
- *"We want to connect AI agents and MCP servers to our systems. Design the guardrails and approval steps."*
- *"Audit our legacy systems and third-party patching, and tell us what to fix first."*
- *"A critical patch for an actively exploited bug just came out. Should we wait a week because of supply chain risk?"*
- *"We are preparing for ISO 27001. Where are our biggest gaps?"*

It is for IT and security teams, developers, founders and managers of small teams without a security specialist, and anyone preparing for an audit.

## Install

Pick the place where you already use AI. No coding is needed for the first three.

| You use | Time | Jump to |
|---|---|---|
| Claude app (web, desktop, mobile) | 2 min | [Claude app](#claude-app) |
| ChatGPT | 5 min | [ChatGPT](#chatgpt) |
| Gemini (web) | 5 min | [Gemini](#gemini) |
| Claude Code | 1 min | [Claude Code](#claude-code) |
| Gemini CLI | 1 min | [Gemini CLI](#gemini-cli) |
| Codex | 1 min | [Codex](#codex) |

### Claude app

Requires a paid Claude plan with code execution turned on.

1. Download [**security-foundations-skill.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-skill.zip). Do not unzip it.
2. In Claude, open **Settings → Capabilities**.
3. In **Skills**, choose **Upload skill** and pick the file you downloaded.
4. Make sure the skill is switched on. Then ask a security question in any chat. Claude uses the skill on its own when the question fits.

### ChatGPT

Creating a GPT requires a paid ChatGPT plan.

1. Download [**security-foundations-chatgpt-kit.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-chatgpt-kit.zip) and unzip it.
2. Go to [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor) and open the **Configure** tab.
3. **Name:** `Security Foundations Advisor`
4. **Description:** `Diagnoses your security posture from the foundations and builds an evidence-based control plan.`
5. **Instructions:** open `instructions.md` from the kit, copy everything, and paste it in.
6. **Conversation starters:** copy two or three of the questions from [What you get](#what-you-get).
7. **Knowledge:** upload the four files in the kit's `knowledge` folder.
8. **Capabilities:** keep Web Search on. The others are not needed.
9. Select **Create**, and choose **Only me** unless you want to share it.

### Gemini

Gemini now uses skills (they replace Gems). Works in the Gemini web app and the Gemini app on Mac.

1. Download [**security-foundations-skill.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-skill.zip) and unzip it. You get a folder named `security-foundations`.
2. Open [gemini.google.com](https://gemini.google.com), then **Settings → Skills**.
3. Import a skill and pick the `SKILL.md` file inside the folder.
4. Recommended: hover over the new skill, choose **Skill actions → Replace skill**, and select the whole `security-foundations` folder. This adds the reference files.
5. Type `/security-foundations` in a chat, or just ask a security question. Gemini also applies the skill on its own when it fits.

If your account does not have skills yet, create a Gem at [gemini.google.com/gems/create](https://gemini.google.com/gems/create) with the [ChatGPT kit](#chatgpt): paste `instructions.md` and add the four `knowledge` files.

### Claude Code

Type these two lines in Claude Code:

```text
/plugin marketplace add LYNGMN/security-foundations-plugin
/plugin install security-foundations@security-foundations-marketplace
```

Start a new session. In the `/` menu you will see two entries:

| Entry | Use it when |
|---|---|
| `/security-foundations:foundations-check` | **Start here.** Add what to review, or run it alone and it asks a few scoping questions first. |
| `/security-foundations:security-foundations` | Rarely needed. The skill runs on its own when you ask a security question in plain words. Call it only if it was not picked up. |

If you also uploaded the skill to the Claude app, a third entry, `/anthropic-skills:security-foundations`, may appear in the desktop app. It is the same skill from your Claude account and can be ignored in Claude Code.

Example:

```text
/security-foundations:foundations-check our customer database and its backups
```

### Gemini CLI

```bash
gemini extensions install https://github.com/LYNGMN/security-foundations-plugin
```

Restart Gemini CLI, then run `/foundations-check <what to review>` or just ask a security question.

### Codex

```bash
git clone --depth 1 https://github.com/LYNGMN/security-foundations-plugin.git
mkdir -p ~/.agents/skills
cp -R security-foundations-plugin/skills/security-foundations ~/.agents/skills/
```

Restart Codex. To update later, run `git pull` in the cloned folder and copy the folder again.

## How it thinks

The advisor follows ten rules. In short:

1. **Know what you have first.** Compare what is registered, what is actually discovered on the network, and what has proof of protection. Close those gaps before buying anything.
2. **Basics before new tools.** Patching, least privilege, multi-factor authentication, log retention, tested backups and an up-to-date asset list come first, with evidence.
3. **Keep the reasons.** Record why each control exists, and give every old system an owner and a decision: retire, keep or replace.
4. **Verify the supply chain.** Ask for software bills of materials and signed build provenance. A vendor's promise is not proof.
5. **Limit what AI agents can do.** Give each agent a level of autonomy with matching controls, a kill switch it cannot edit, and actions tied to a real person.
6. **Zero trust step by step.** Automate access decisions instead of relying on manual settings.
7. **Change behavior, not just awareness.** Coach at the moment of a mistake, measure reporting rather than course completion, and never punish people for failing a phishing test.
8. **In an incident, isolate first.** Cut access, then preserve evidence, then investigate. Do not wipe or reboot before evidence is kept.
9. **Earn trust in public.** Communicate fast and factually, separate facts from guesses, and never hide an incident.
10. **Map to your obligations.** One set of evidence should serve NIST CSF, ISO 27001 and local rules such as ISMS-P, DORA or NIS2.

The full rule set is in [skills/security-foundations/SKILL.md](skills/security-foundations/SKILL.md).

## What it will not do

- Read passwords, `.env` files, private keys or other credentials
- Install unverified software or run destructive commands
- Write malware or exploits, or help bypass authentication
- Give legal opinions or certify compliance
- Claim something is safe without evidence, or invent standard numbers

If a document or web page it reads contains instructions aimed at the AI, it reports them instead of following them.

## Standards it follows

| Area | Standard |
|---|---|
| Security program | NIST Cybersecurity Framework (CSF) 2.0 |
| Management system | ISO/IEC 27001:2022 |
| Incident response | NIST SP 800-61 Rev. 3 |
| Passwords and authentication | NIST SP 800-63B Rev. 4 |
| Zero trust | CISA Zero Trust Maturity Model 2.0 |
| Software supply chain | SLSA v1.2, SBOM (SPDX, CycloneDX), CSAF/VEX |
| AI agents | OWASP Top 10 for Agentic Applications 2026, OWASP Top 10 for LLM 2025, MITRE ATLAS |
| AI risk | NIST AI RMF, NIST AI 600-1 |

Versions and counts were last checked in October 2026. See [standards-map.md](skills/security-foundations/references/standards-map.md) for details, and re-check the source before quoting a standard in an audit report.

## Good to know

- **It advises; it does not act.** It designs plans and checks your reasoning. It does not scan, change or fix your systems.
- **Not a substitute for a professional.** For a real incident, also contact your security team or an incident response provider.
- **A custom GPT or Gem follows it less strictly than a skill.** Those versions rely on pasted instructions, so they may sometimes skip a part. The four-part format and safety rules are written directly into the instructions to keep them consistent.
- **Your data stays with your AI provider.** This project adds instructions only. It sends nothing anywhere.

## For contributors

```text
.claude-plugin/          Claude Code plugin and marketplace manifests
skills/security-foundations/
  SKILL.md               The skill (English, authoritative)
  SKILL.ko.md            Korean mirror for reviewers
  references/            Standards map, failure modes, incident runbook
evals/                   Evaluation cases with graders (claude plugin eval)
commands/                /foundations-check for Claude Code (.md) and Gemini CLI (.toml)
adapters/                ChatGPT kit: instructions (under 8,000 characters) and guide
AGENTS.md, GEMINI.md     Context files for Codex and Gemini CLI
gemini-extension.json    Gemini CLI extension manifest
scripts/                 Validation and packaging
```

Validate and build the release files locally (Python 3, no dependencies):

```bash
python3 scripts/validate_and_package.py
```

Run the evaluation cases in Claude Code:

```bash
claude plugin eval .
```

Pull requests are welcome. Keep `SKILL.md`, `SKILL.ko.md` and `adapters/core-instructions.md` in agreement, and run the validator before opening a PR. Releases are created automatically when a `v*` tag matching the version in `.claude-plugin/plugin.json` is pushed; release notes are generated by GitHub.

To report a security problem, see [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE) © 2026 Youngmin
