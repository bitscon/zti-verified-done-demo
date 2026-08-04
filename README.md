# zti-verified-done-demo

**This repository will not accept "done" on anyone's word — including an
AI's.** Every merge requires a hash-sealed receipt proving the required
checks were independently re-run against the exact bytes being merged.

It is the live demo for [ZTI Core](https://zerotrustintelligence.io) —
**self-hosted** agent governance (you run the control plane on your own
servers; nothing here is a hosted service). The plane governing this repo is
our public showroom copy at `demo.zerotrustintelligence.io`.

## Watch it work — the two PRs

- **The honest PR** — the developer ran `zti receipt`: the gate re-ran the
  tests itself, minted a receipt bound to the staged content's tree hash,
  and the `zti-verify` required check is **green**. Mergeable.
- **The bypass PR** — the commit was made with `git commit --no-verify`
  (git's documented local escape hatch, deliberately left open). No receipt
  exists for that content, so `zti-verify` is **red**:
  `DONE_WITHOUT_RECEIPT`. The merge button is dead. That is the point.

## How it works

One contract — pytest must pass; `.github/` and `.zti/` are out of bounds —
enforced three times over the same content address (the git tree hash):

| Tier | Where | Blocks |
|---|---|---|
| 1 — runtime | agent-side hook | out-of-scope / irreversible actions, live |
| 2 — commit | git pre-commit gate (`zti install-hooks`) | committing without a passing receipt |
| 3 — merge | the `zti-verify` required check in this repo | merging around Tiers 1–2 |

A receipt is minted only by re-running the contract's checks — an agent
*claiming* success is never the input. Receipts are hash-sealed
([ZTIP](https://github.com/bitscon/ztip), the open protocol) and the plane
re-verifies the seal before storing anything. Change one byte after minting
and the tree hash no longer matches: no receipt, no merge.

Agent-neutral by construction: Tiers 2–3 read git content and receipts.
Claude Code, Cursor, Copilot, Codex, or a human in a hurry — same gate.

## What's in this repo

- `app.py` / `test_app.py` — the tiny real codebase under governance.
- `.github/workflows/zti-verify.yml` — the Tier-3 required check: installs
  the `zti` CLI from the vendored wheel and asks the plane whether a passing
  receipt covers the PR head's exact content.
- `.zti/` — the vendored CLI wheel and plane config. (The gate bearer key is
  **not** in this repo; it lives in Actions secrets.)

The sample code is free to copy. The vendored `zti` CLI wheel is part of the
commercial ZTI Core product — see
[zerotrustintelligence.io](https://zerotrustintelligence.io) for licensing
(free 30-day trial; runs entirely on your own infrastructure).
