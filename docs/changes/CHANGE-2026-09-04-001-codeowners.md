# Change Record

- **Date:** 2026-09-04
- **Type:** governance — close the residual left by
  CHANGE-2026-09-03-001 (a PR that edits the `zti-verify` workflow runs
  its own copy of the gate and could repoint the verifier install).
- **ADR reference:** none (demo repo; rationale in the 2026-09-03 record).
- **What changed:** root `CODEOWNERS` marking `/.github/` (and the file
  itself) as owner-territory. Root placement is deliberate: the published
  contract forbids writes under `.github/`, and GitHub honors a root
  CODEOWNERS.
- **Why:** on a personal GitHub account the org-level "required workflow"
  pin is unavailable; the equivalent control is a main-branch ruleset
  requiring a PR + the `zti-verify` status check + Code Owner review on
  gate-config paths + no force pushes. CODEOWNERS is the piece that must
  live in-tree; the ruleset is owner click-side config.
- **Risk:** LOW — adds a review requirement only; no code, no workflow,
  no contract change. The ruleset (not this file) does the enforcing.
- **Verified:** tests unaffected (`python3 -m pytest -q` green at mint —
  the receipt for this content proves it); CODEOWNERS syntax is two plain
  path→owner lines. Effective only once the operator activates the
  main-branch ruleset with "require review from Code Owners".
