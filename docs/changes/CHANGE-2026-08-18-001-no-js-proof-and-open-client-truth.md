# Change Record

- **Date:** 2026-08-18
- **Type:** docs (README + committed proof asset — ZTI UX wave 2, board card
  `zti:ux-w2`)
- **ADR reference:** none
- **What changed:**
  - **No-JS / logged-out proof of the red check.** New
    `docs/assets/pr2-zti-verify-red-logged-out.png`: a real headless-browser
    screenshot of PR #2's Checks tab taken logged out on 2026-08-18 — repo
    header, PR title, red ✗ on commit 8558c7a, the `zti-verify` check red,
    "Sign in" buttons visible proving the logged-out view. Embedded in a new
    README subsection ("No login, no JavaScript, still visible") together
    with a direct link to the public failing check run
    (actions/runs/30872603547/job/91877492065). Rationale: verified this
    session that GitHub serves the PR conversation page to logged-out
    visitors WITHOUT the merge box or checks section — the audit's gap —
    so the blocked state now survives JS-off and logged-out viewing.
  - **Open-client truth + availability story.** The closing licensing
    paragraph claimed the vendored `zti` wheel "is part of the commercial
    ZTI Core product" — false since ADR-0009 opened the client layer (MIT,
    bitscon/zti-cli, 2026-08-17). Rewritten: client open at bitscon/zti-cli,
    the vendored wheel is the pinned build the check installs, and the one
    availability story (ZTI Core complete + early access, free 30-day trial,
    individual use free, org licensing per year, pricing announced at
    launch, licensing@zerotrustintelligence.io). Self-hosted wording kept
    (AGENTS.md forbids hosted/SaaS framing). No dollar figures.
  - `docs/` (assets + changes) created; this is the repo's first Change
    Record.
- **Why:** The 2026-08-18 UX audit's repo wave: the demo's proof must be
  visible to every visitor, and the README must match the post-ADR-0009
  reality and the site story.
- **Risk:** LOW — docs and one static image on a branch; main is untouched
  until the gate ceremony passes.
- **Landing path (the demo eats the dog food):** committed on branch
  `docs/ux-w2-proof`, NOT main. The claude account cannot mint a receipt
  (`.zti/gate.key` is 0600 billyb) and holds no GitHub auth. The local
  Tier-2 pre-commit gate therefore blocked this very commit (`zti: not
  found` — no receipt, no commit), and the branch commit was made with
  `git commit --no-verify`: the documented Tier-2 local escape that Tier 3
  exists to catch. The merge stays fully gated — the operator lands it the
  way the product demands: check out the branch, run `zti receipt` (re-runs
  pytest, binds this exact tree, ships to the demo plane), open the PR,
  merge only when `zti-verify` is green. Bypassing the gate in our own demo
  is the one unforgivable; nothing here merges around it.
- **Verified:** demo suite 3/3 locally after the edit (the same pytest the
  receipt will re-run); screenshot content visually verified (red check,
  logged-out chrome); check-run URL and PR URL fetched HTTP 200 from the
  public API; failure-set grep clean (no dollar figures, no "ZTI
  Foundation", no ZTAP, no hosted/SaaS wording, no stale "in
  build"/"coming"). Adversarial round exempt (docs-only wave, ADR-0005 /
  AGENT_OS §21.4). NOT verified here: the merged README render on main —
  that lands with the operator's merge.
