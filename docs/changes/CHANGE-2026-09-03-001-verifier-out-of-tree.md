# Change Record

- **Date:** 2026-09-03
- **Type:** security / supply-chain — the Tier-3 required check (board card
  `zti:vac-demo`; closes vacuity-scout finding #6, CRITICAL).
- **ADR reference:** ADR-0004 (three-tier enforcement), ADR-0009 (open client);
  scout report `zticore/docs/proof/2026-09-02-vacuity-scout-report.md` #6.
- **What changed:**
  - `.github/workflows/zti-verify.yml` — the install step no longer runs
    `pip install .zti/zti-*.whl` (a wheel committed **inside** the PR tree it
    verifies). It now installs the `zti` verifier from PyPI, pinned to an exact
    version **and** artifact hash, written to `$RUNNER_TEMP` at run time and
    installed with `pip install --require-hashes --no-deps`. The verifier now
    comes from **outside** the tree under test.
  - `.zti/zti-0.1.0-py3-none-any.whl` — **removed** from the repo. The exhibit
    no longer ships an installable in-tree wheel. `.gitignore` now excludes
    `.zti/*.whl` so one cannot be re-vendored silently.
  - `README.md` — the "what's in this repo" and licensing prose that described
    installing "from the vendored wheel" is rewritten to the pinned-from-PyPI
    reality (the exhibit's own description must be true).
- **Why:** The scout showed a PR could vendor a stub `zti` wheel in `.zti/`;
  the old install ran that in-tree wheel, so `zti verify` exited 0 with no
  plane, no receipt, no secrets — the flagship red-PR exhibit defeated in-tree.
  Installing the verifier from a pinned external source removes the in-tree
  wheel as an install source entirely.
- **Design decision (settled in the round):** pinned-external from PyPI with
  `--require-hashes`, over a hash-pinned vendored wheel. A vendored wheel keeps
  the install source inside the tree; PyPI + hash puts it outside and makes a
  swapped artifact fail closed (hash mismatch). Pins: `zti-cli==0.1.0`
  (sha256 3316ba91…3a17) + its dependency `ztip==1.0.0.dev2`
  (sha256 4767a573…1ac9). Regenerate on a version bump.
- **Risk:** LOW — the gate gets stricter and every new failure mode is
  fail-closed: an unreachable index, a tampered artifact (hash mismatch), or a
  wrong pin all turn the required check red, never green. No receipt/plane
  logic changed. New dependency: CI network reach to PyPI (fails closed).
- **Residual (cannot be closed from the repo — operator GitHub-side config):**
  a PR that also edits `.github/workflows/zti-verify.yml` runs its **own** copy
  of the workflow and could repoint the install. Close it by running the gate
  from a pinned definition outside the PR — a repository ruleset / organization
  **required workflow** on the default branch — so the PR's copy cannot replace
  it. Not settable from here (`gh` unauthenticated on the barn).
- **Verified (reproduction against a real loopback plane — `python -m core`
  on 127.0.0.1; scratch venvs; no live demo host contacted):**
  - R0 baseline (the finding): OLD step `pip install .zti/zti-*.whl` + a stub
    wheel → `zti verify <no-receipt sha>` **exit 0** ("STUB zti: verified done
    (nothing checked)"). The attack reproduces.
  - R1 fix (a): FIXED step with the **same** stub still planted in `.zti/` →
    the pinned `zti` installs from PyPI, the stub is never the source →
    `zti verify` **exit 2** DONE_WITHOUT_RECEIPT. Stub code never runs. Defeated.
  - R2 control (b): real verifier + dead plane → **exit 3** PLANE_UNAVAILABLE.
  - R3 green (c): genuine passing receipt minted by the pinned-from-PyPI
    `zti receipt` → `zti verify` **exit 0** PASS. The pinned verifier is the
    real, working one.
  - Supply-chain: wrong hash → install **fails** ("PACKAGES DO NOT MATCH THE
    HASHES … someone may have tampered"); an unpinned/no-hash requirement is
    **refused** in `--require-hashes` mode; `pip check` clean (closure complete).
- **Adversarial round (class M, ADR-0005/0007):** wave 1 — two lenses
  (supply-chain/install-integrity + fail-closed/conformance): 1 finding
  confirmed (README + wiring-doc still described the vendored-wheel install),
  fixed. wave 2 — fresh-eyes over the whole changeset: clean. Converged at 2
  waves. Tally: raised 1 / confirmed 1 / refuted 0.
- **Follow-ups registered (not in scope here):** the "Developer workstation"
  manual CLI-install line in `zticore/docs/ENFORCEMENT-TIERS.md` and the
  launch/HN blurbs still show an unpinned `pip install "zti @ git+…"` — a
  workstation tool choice, not the gate; HN copy is hand-written-only. Left for
  a docs pass.
- **Files:** `.github/workflows/zti-verify.yml` (mod),
  `.zti/zti-0.1.0-py3-none-any.whl` (del), `.gitignore` (mod),
  `README.md` (mod), this record (new).
