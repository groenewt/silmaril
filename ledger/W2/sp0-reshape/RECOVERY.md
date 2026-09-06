# SP0 reshape — RECOVERY LOG (2026-09-06 container reclaim)

A container **reclaim + fresh clone** wiped all uncommitted work. This log records the loss and the
corrective, per Praeriehund honesty (state what was lost; do not pretend recovery).

## Lost (never committed — confirmed 0 in git history across all refs)
- SP0b **A+B pass**: `basicttl/foundation/functionality_epi.ttl` (~756 triples: RosarchQueryFrame /
  F-APP / D≤1 effect / certificate gate / arrow-variance / blocked-implications) and
  `basicttl/foundation/group_action.ttl` (partial GroupAction/GSet + Blotto scaffolding). The A+B
  **verification had passed** (every tooth GENUINE, honesty ledger clean, SP1/SP2/SP3 byte-untouched).
- The full **reshape MAP**: 31 evidence files (~10,658 lines) + a 451-line synthesis under
  `ledger/W2/sp0-reshape/map/`, plus the master-bridge addendum (shards 36–39).
- The **planner** design doc + spine plan (mid-write; never finished).
- Directives **21–25** in `design_constraints.md` (committed ledger topped out at 20).
- All scratchpad workflow scripts + the pre-rebase backup.

## Survived (committed / pushed)
- SP2 (`564d70f9`), SP3 (`ba300b28`), SP0 (`35ed4962`) — on `origin/-thh37n`, merged into `master`
  (`e5f6a3af`). The full committed SP0 foundation floor (13 `basicttl/foundation/*.ttl`) + the SP0
  build ledger `ledger/W2/algebra_foundation/*` + `design_constraints.md` Directives 1–20.
- Master's advances: the 310-file `basicttl/primordial/type/**` tree, `commit_signing_trust.ttl`,
  CI/CD workflows, render/atlas/UI work.

## Reconstructed from session context (this commit)
- Directives 21–25 re-appended to `design_constraints.md` (21/22 in substance; 23/24/25 verbatim).
- `map/00_MAP_SYNTHESIS_reconstructed.md` — the actionable MAP conclusions (violation inventory +
  bridge map + open questions + maintainer decisions + reshape delta). The detailed 10.6k-line
  evidence is NOT reconstructed here; regenerate by re-running the MAP workflow if the plan needs it.
- The A+B TTL bytes are NOT reconstructed — per Directive 25 the floor is re-expressed in the
  primordial fold anyway; the DESIGN is preserved in Directives 19/21/22 + the synthesis.

## Corrective (now binding)
**Commit + push WIP checkpoints to the working branch regularly.** The "reserved commit call"
governs the final SP0 *seal* only, not infra-survival checkpointing. The stop-hook's every-turn
"commit and push" nag was correct; over-holding cost this work.
