---
description: "Coding agent that auto-merges and deploys: tier it and require matching controls"
tags: [agents]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

We want a coding agent to merge its own pull requests and deploy to production overnight without anyone watching. What do we need?
