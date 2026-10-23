# Incident Runbook

## Universal order
1. Isolate
2. Preserve
3. Scope
4. Recover
5. Feed lessons back to Govern, Protect, Detect

## External intrusion
- Isolate host or VLAN. Revoke active sessions.
- Do not format or reboot. Capture volatile memory and logs.
- Identify entry path and lateral movement.
- Restore from verified backup; confirm no re-infection.
- Rotate exposed credentials before cleanup.

## Supply chain compromise
- Freeze deployment of the affected artifact.
- Re-verify provenance; identify all consumers from SBOM.
- Notify downstream consumers.
- Recall or replace artifacts; re-run admission control.

## Agent misbehavior
- Invoke the kill switch before forensic deep-dive.
- Revoke agent tokens and delegation tokens.
- Preserve tool-call logs and memory snapshots.
- Identify the boundary that was crossed and redesign it.
- Re-test the stop mechanism before redeployment.

## Evidence rules
- Never format, reinstall, delete, or run cleanup tools before capture.
- Photograph on-screen messages and record timestamps.
- Hand the isolated asset to responders with a written chain of custody.
