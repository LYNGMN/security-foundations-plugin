# Standards Map

| Domain | Standard | Version | Applied mandate |
|---|---|---|---|
| Program structure | NIST CSF 2.0 | Feb 2024 | 6 functions, 22 categories, 106 subcategories; GV.SC supply chain |
| Management system | ISO/IEC 27001 | 2022 | 93 controls in 4 themes; supplier controls A.5.19–A.5.22 |
| Access architecture | CISA ZTMM | 2.0 | 5 pillars, 3 cross-cutting capabilities, traditional to optimal |
| Incident response | NIST SP 800-61r3 | Apr 2025 | Mapped to CSF 2.0 six functions |
| Identity | NIST SP 800-63B | Rev.4, 2025 | 8 chars within MFA, 15 as sole factor, accept 64+, no arbitrary rotation |
| AI risk | NIST AI RMF, AI 600-1 | 2023, 2024 | Human-AI configuration, overreliance, automation bias |
| Adversarial ML | NIST AI 100-2e2025 | 2025 | Evasion, poisoning, privacy, misuse |
| Agentic risk | OWASP Top 10 for Agentic Applications | 2026 (Dec 2025) | ASI01–ASI10 |
| LLM risk | OWASP Top 10 for LLM | 2025 | LLM01 prompt injection, LLM06 excessive agency |
| AI adversary tactics | MITRE ATLAS | v5.4.0, Feb 2026 | 16 tactics, 84 techniques, 56 sub-techniques; agent-focused techniques added in the Oct 2025, Nov 2025 and Feb 2026 releases |
| Supply chain | SLSA | v1.2, Nov 2025 | Build Track L1–L3, Source Track |
| SBOM | CISA SBOM minimum elements | 2025 | Supplier, component, PURL/CPE, dependency, author, hash, license, tool, generation context |
| VEX | CSAF | v2.0, ISO/IEC 20153:2025 | Exploitability statements |
| Secure development | NIST SSDF | SP 800-218r1 | PO, PS, PW, RV practice groups |
| Agent execution safety | Agent safety checklist (internal, not a published standard) | n/a | Separation of duties, human-in-the-loop, input/output validation, helper models, least agency, defensive technical controls |

## Agentic risk coverage

| Risk | Primary mitigation |
|---|---|
| ASI01 Goal hijack | Treat retrieved content as untrusted; constrain objectives |
| ASI02 Tool misuse | Schema validation; scoped tool permissions |
| ASI03 Identity abuse | Short-lived task-scoped tokens bound to a human subject |
| ASI04 Agentic supply chain | AIBOM; cryptographic verification of MCP servers |
| ASI05 Unexpected code execution | Ephemeral network-isolated sandbox |
| ASI06 Memory poisoning | Sanitize RAG and memory stores; tenant scoping; TTL |
| ASI07 Insecure inter-agent communication | Authenticated, integrity-protected messages between agents |
| ASI08 Cascading failures | Circuit breakers, retry policy, rate limits, blast-radius caps |
| ASI09 Human-agent trust exploitation | Approval UI showing diff, target, and blast radius |
| ASI10 Rogue agents | External kill switch; behavioral heartbeat monitoring |

## Verification notes

Cite a standard externally only after checking its current version at the source.

- Confirmed against the publisher's site when this package was built (Oct 2026): SLSA v1.2 (announced Nov 2025) and MITRE ATLAS v5.4.0 counts (16 tactics, 84 techniques, 56 sub-techniques, Feb 2026).
- Not independently re-checked in this build: all other rows. Treat versions and counts as starting points and re-verify before they appear in an audit report or board paper.
- No published framework named SHIELD could be found, so that row was replaced by a neutral internal checklist. Do not cite it as a standard.
