# AGENTS

## System Identity

zti-verified-done-demo is the public live demo of ZTI Core's three-tier
receipt enforcement (zticore ADR-0004). It is itself governed by the demo
plane at demo.zerotrustintelligence.io — this repo eats the dog food.

## Allowed Paths
- zti-verified-done-demo/

## Prohibited Actions
- Commit any credential: `.zti/gate.key`, gate bearer keys, the operator
  password, license tokens. The published contract additionally forbids
  writes to `.github/` and `.zti/` at the gate.
- Describe the product as hosted/SaaS anywhere in this repo — ZTI Core is
  self-hosted; the demo plane is a showroom copy (see
  zticore/docs/DEMO-PLANE-RUNBOOK.md).
- Merge to `main` without the `zti-verify` required check passing (that is
  the product; bypassing it in our own demo is the one unforgivable).

## Reporting Requirement
Every agent session must end with a list of all files created or modified.
