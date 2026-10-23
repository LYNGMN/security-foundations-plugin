---
type: llm
focus: last_message
---

PASS if the response cites SLSA v1.2 and covers both the Source Track (branch protection, two-party review) and the Build Track, requiring Build L3 for production.
FAIL if it cites SLSA v1.0, omits the Source Track, or does not require L3 for production.
