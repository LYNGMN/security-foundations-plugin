# Security policy

## Reporting a vulnerability

Please report security problems privately through GitHub:
**Security** tab → **Report a vulnerability** on
[LYNGMN/security-foundations-plugin](https://github.com/LYNGMN/security-foundations-plugin/security/advisories/new).

Do not open a public issue for a vulnerability. You can expect a first reply within 7 days.

Examples of what to report:

- Wording in the skill or the ChatGPT / Gemini instructions that leads the assistant to read secrets, run destructive commands, or follow instructions hidden in retrieved content
- A release asset whose contents do not match this repository
- Incorrect security guidance that could cause real harm if followed

## Supported versions

Only the latest release receives fixes.

## Verifying a release

Release assets are built by GitHub Actions from the tagged commit and carry a signed
[build provenance attestation](https://docs.github.com/actions/security-for-github-actions/using-artifact-attestations).
With the GitHub CLI you can confirm a download came from this repository's workflow:

```bash
gh attestation verify security-foundations-claude-skill.zip --repo LYNGMN/security-foundations-plugin
```

## Scope of the guidance

This project gives advisory guidance. It is not legal advice, not a certification opinion, and not a
substitute for a qualified security professional reviewing your environment.
