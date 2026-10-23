# Failure Modes Catalog

## Assets
- Unregistered externally reachable services
- Legacy systems with no named owner
- Shadow IT and unapproved SaaS
- Dormant accounts and orphaned service principals

Detection: reconcile discovery against register; flag assets with no owner or no review date.

## Identity and access
- Standing admin rights
- Permissions without expiry
- Service accounts shared across teams
- Static secrets in repositories
- Default or hardcoded credentials

Detection: permission inventory with purpose and expiry; secret scanning with push protection.

## Supply chain
- Artifacts consumed without SBOM
- Unsigned or unverifiable provenance
- Build at L1 or L2 used for production
- Unverified package names (hallucinated dependencies)
- Patch applied fleet-wide without staging

Detection: admission control on provenance; lockfile integrity; package existence check.

## AI and agents
- Agent with write access to production
- Tool calls not attributable to a human
- Persistent memory without validation
- Inter-agent messages without authentication
- No kill switch outside the agent's edit surface
- Approval screens that hide the actual diff

Detection: tool-call audit with subject binding; memory store TTL; message authentication logs.

## Human
- Training measured by completion
- Simulations used punitively
- Reporting channel that punishes reporters
- No technical safety net behind human caution

Detection: reporting rate and time-to-report trends; simulation click and report correlation.

## Response
- Formatting before evidence capture
- Containment delayed for root-cause analysis
- Incident concealed or minimized
- Preventive measures tracked to publication, not closure

Detection: runbook order check; retrospective closure rate.
