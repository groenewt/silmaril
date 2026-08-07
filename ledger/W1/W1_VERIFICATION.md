# W1 VERIFICATION — remediated evidence record for the maintainer and the adversarial panel

Author: W1 VERIFICATION (R5 rewrite, updated to the **round-2 (R6) re-audit** verified state).
Frame date: `2026-08-07`. Branch: `claude/custom-pgp-sign-git-thh37n`. HEAD: `774dcc4e`.
Scope: read-only re-verification of the ten-phase W1 discovery **after the R1 remediation and its
round-2 (R6) re-audit** (which found, and this record documents as resolved, two defects the R1
remediation had itself re-introduced — see the Round-2 re-audit resolutions note below), and
the full three-angle adversarial-panel record with each finding's resolution. Doctrine read in full
first this turn (`docs/praeriehund-demokratie-der-kategorien.md` = **129 lines**;
`docs/unary-byte-frame-law.md` = **765 lines**) before any audit. Discipline: verbatim command
outputs pasted; every verdict cited to an artifact + commit-or-working-tree-edit or to a plainly
stated missing thing; inferences marked; PROVISIONAL reserved for the genuinely unresolvable with a
documented gap (never to dodge resolvable work); no interpretive gates; no force-fit; no
state-changing git (read-only queries only); the only file written is this one.

Authoritative pin confirmed live this session:
**`forge/base` @ `c4e828188a57d7a93c4f4972859dd0862ae6cce6`** (`git submodule status` →
`c4e828188a57d7a93c4f4972859dd0862ae6cce6 forge/base (heads/main)`). The `9e60c103…` value some
earlier notes asserted **does not exist in the repo**.

> **Honest status of THIS ledger's working tree (not clean — read this first).** The R1
> remediation **plus its round-2 (R6) re-audit fixes** live in the **working tree, uncommitted**:
> HEAD is still `774dcc4e` ("W1 Task 4: Complete-Component-Account seed (317,601 rows)"), the
> pre-remediation state. `git status --porcelain ledger/W1/` shows **13 tracked files modified**
> (the three regenerated trees `base_agents/silmaril/superpowers`, both account CSVs, `GENERATOR.sh`,
> the two hardened checks `coverage.sh`/`account-check.sh`, and the five corrected maps
> `base_templates/component_account/corpus_v17/sparky_substrate/taxonomy_census`) plus **3
> untracked files** (`W1_VERIFICATION.md` — this file; `account/symlinks.tsv`; and
> `checks/tree-disk-check.sh`). The round-2 fixes are folded into that same set (they re-touch
> `trees/silmaril.tree`, `account/silmaril.csv`, `checks/tree-disk-check.sh`, `sparky_substrate.md`,
> and `component_account.md`), so the porcelain shape is unchanged: 13 modified + 3 untracked.
> **Note the deliberate asymmetry the round-2 fix creates:** `account/symlinks.tsv` and
> `checks/tree-disk-check.sh` are still **untracked on disk** (git `??`) yet are now **carried in
> `silmaril.tree` and the account** — they are real, committed-*next* corpus, and the self-exclusion
> that R1 used to keep them out of the tree is removed. **The ledger working tree is therefore NOT
> clean.** The green state below is real but currently unpinned; it becomes durable only when this
> R1+R6 set is committed (a state-changing step this read-only author does not perform). Every claim
> in this record is scoped to the working-tree content it was measured against.

---

## Round-2 re-audit resolutions — two defects the R1 remediation itself re-introduced, both now RESOLVED

The R1 remediation (documented throughout this record) closed the original panel findings, but a
round-2 (R6) re-audit — read-only, this session — found that R1 had **re-introduced two defects of
the very classes it was fixing**. This note states both honestly and records their resolution. Both
are now closed and re-verified green (§A, run fresh this turn).

**R6 finding 1 — the stale-tree class came back, masked by a `tree-disk-check` self-exclusion
(CRITICAL, RESOLVED).** In fixing the original stale-`silmaril.tree` finding, R1 *created* two new
audit files — `account/symlinks.tsv` and `checks/tree-disk-check.sh` — and then **named-excluded
them from `silmaril.tree` and the account** (R1's Phase-10 "post-freeze control-plane" carve-out),
with the `tree-disk-check.sh` script carrying a matching **self-exclusion** so the drift check stayed
green despite two in-scope, self-created files being absent from the tree it was meant to bind. That
is the exact stale-tree class the fifth gate exists to make un-committable — reintroduced one layer
up. **Resolution:** `silmaril.tree` is now **regenerated as the final pre-commit step** (never frozen
early), so it carries `symlinks.tsv` AND `tree-disk-check.sh` as ordinary corpus (`silmaril.tree`
`6341` → **`6343`**; `ledger` region `24` → `26`; grand total `317647` → **`317649`**); each of the
two now also has an account row (`silmaril.csv` `36,575` → **`36,577`**). The **self-exclusion is
removed** from `tree-disk-check.sh` — it now binds **every** regular file and symlink under silmaril
scope, the audit apparatus (symlinks.tsv, GENERATOR.sh, the gate itself, the maps, the account)
included. §A.5 prints `OK  silmaril  6343 entries  (tree == disk)` with no carve-out, so the
recurrence is now un-committable-green: a future stale tree — including one masked by pruning the
audit's own files — fails the gate. (Recurrence fixed **at the source** — regenerate the tree last —
not by folding the two files away.)

**R6 finding 2 — the 66 `lambda`-twin account rows over-claimed their evidence
(IMPORTANT, RESOLVED).** R1 resolved the reserved-keyword `sparky/lambda/` twin from PROVISIONAL to
**`reuse`** and stamped every one of the 66 rows with a per-row "call-site" framing — as if each row
were itself an importlib call-site — which both **over-claimed** (a package member is not a call-site)
and **mis-dispositioned** (`reuse` says "keep as-is, no work pending", but the reserved keyword
`lambda` cannot survive the unary refactor — it MUST fold onto the lawful `lambda_` sibling, which is
pending work, i.e. a migration). **Resolution:** the 66 rows are now disposition **`migrate`** (was
`reuse`), successor_hint **"fold onto the lawful `lambda_` sibling under the unary refactor (X)"**,
and their evidence is now **package-level, not per-row**: *"member of the reserved-keyword lambda
package that is live-wired into the engine via 37 importlib call-sites resolving 5 entrypoint
modules in `scripts/python/pylib/src` (excl `reference`) … transforms to the `lambda_` sibling under
X."* The count of importlib call-sites is a **property of the package (37 call-sites → 5 entrypoint
modules)**, asserted once about the package the 66 rows belong to — not "37 call-sites" restamped on
each row. Disposition distribution moves accordingly: `reuse` `313433` → **`313369`** (−66 lambda
rows leaving `reuse`, +2 new ledger files entering `reuse`), `migrate` `3476` → **`3542`** (+66).
Provisional stays **27** (the 66 were already out of `provisional` after R1; this fix only corrects
where R1 put them). The twin is a live module — so it is not retired — but it is **not** finished
work, so it is `migrate`, not `reuse`.

Both fixes were re-verified on disk this session: all five checks green (§A), total `317649`
throughout, `account-check` still `PASSED 317649` with every invariant holding.

---

## A. The FIVE acceptance checks — re-run fresh this turn, output pasted verbatim

All five were executed by this author this turn from the repo root `/home/user/silmaril`. Each exited 0.

### A.1 `coverage.sh forge/base_templates … base_templates.manifest`

```
$ ./ledger/W1/checks/coverage.sh forge/base_templates ledger/W1/manifests/base_templates.manifest
COVERAGE EXACT: forge/base_templates == ledger/W1/manifests/base_templates.manifest (1118 files; sha256+bytes verified)
EXIT=0
```

### A.2 `coverage.sh forge/base … base_tower.manifest`

```
$ ./ledger/W1/checks/coverage.sh forge/base ledger/W1/manifests/base_tower.manifest
COVERAGE EXACT: forge/base == ledger/W1/manifests/base_tower.manifest (50 files; sha256+bytes verified)
EXIT=0
```

### A.3 `census-check.sh`

```
$ ./ledger/W1/checks/census-check.sh
CENSUS CHECK PASSED (317649 files across 7 trees)
EXIT=0
```

### A.4 `account-check.sh`

```
$ ./ledger/W1/checks/account-check.sh
ACCOUNT CHECK PASSED: 317649 rows
EXIT=0
```

### A.5 `tree-disk-check.sh` (the new fifth gate — binds the manifest-less trees to LIVE disk)

```
$ ./ledger/W1/checks/tree-disk-check.sh
OK  silmaril             6343 entries  (tree == disk)
OK  basicttl            30234 entries  (tree == disk)
--- bonus coverage: other five trees (files+symlinks, exclude .git) ---
OK  base_agents        279707 entries  (tree == disk)
OK  base_templates       1118 entries  (tree == disk)
OK  base_tower             50 entries  (tree == disk)
OK  example_gippidy_01     16 entries  (tree == disk)
OK  superpowers           181 entries  (tree == disk)
EXIT=0
```

**Result: coverage base_templates = EXACT 1118 (sha256+bytes verified); coverage base = EXACT 50
(sha256+bytes verified); census-check = PASSED 317649; account-check = PASSED 317649 rows;
tree-disk-check = all 7 trees OK (tree == disk), silmaril `6343`, with NO self-exclusion.** The
count is now **317649** everywhere. Lineage: `317601` (pre-remediation) → `317647` (R1: `+38`
tracked symlinks and `+8` in-scope ledger artifacts) → **`317649`** (round-2 R6 re-audit: `+2` —
`account/symlinks.tsv` and `checks/tree-disk-check.sh`, the two self-created audit files that R1
had left named-excluded from `silmaril.tree`, are now carried in the tree AND the account; see the
Round-2 re-audit resolutions note below). `silmaril.tree` therefore moves `6341` → **`6343`**.
What changed since the pre-remediation checks: `coverage.sh` now re-hashes sha256 and re-measures
bytes (not path-only); `account-check.sh` now rejects `UNCLASSIFIED`/`conflict`/
retire-without-inverse/provisional-without-gap; and `tree-disk-check.sh` is the fifth gate that
binds `silmaril.tree` + `basicttl.tree` (and, as bonus, the five corpus trees) to live disk **with
no self-exclusion**, so a stale tree — including one masked by pruning the audit's own files — can
no longer hide behind internally-consistent checks.

---

## B. What the partition actually IS, and independent corroboration (beyond the five checks)

**The partition scope, stated precisely (this corrects the earlier "physical universe" / "live
filesystem" overreach).** The seven trees are a **partition of a precisely-scoped set — NOT of "the
live filesystem" tout court.** The partitioned set is the **tracked-and-physical file-AND-symlink
set** of the six mapped corpus roots plus the silmaril repository tree:

1. the `silmaril` superproject working tree (`silmaril.tree`), **minus** `basicttl/`, `forge/`,
   `external/` (each owns its own tree);
2. `basicttl/` (`basicttl.tree`);
3. `forge/base_agents/` (`base_agents.tree`);
4. `forge/base_templates/` (`base_templates.tree`);
5. `forge/base/` — the base turtle tower (`base_tower.tree`);
6. `forge/example_gippidy_01/` (`example_gippidy_01.tree`);
7. `external/skills/superpowers/` (`superpowers.tree`).

Within this scope **every physical regular file OR tracked `mode-120000` symlink appears in exactly
one tree.** The partition **explicitly EXCLUDES two surfaces, both named per Präriehund** (never
folded silently), and the round-2 re-audit tightened the wording of both:

- **The `.git/` *directory trees*** — the internal object/ref plumbing, control-plane not corpus.
  **What is excluded is the `.git/` directory content, NOT everything named `.git`.** The **14 `.git`
  submodule-**gitlink** pointer files are *regular files* and ARE INCLUDED in the partition** — each
  is one line in a tree with an account row (`grep -E '/\.git$' trees/*.tree | wc -l` → **14**:
  `forge/base_agents/.git`, `forge/base_templates/.git`, `forge/base/.git`, the nine
  `forge/base/forge/**/.git` + `forge/base/external/.git` nested-submodule pointers,
  `forge/example_gippidy_01/.git`, `external/skills/superpowers/.git`; `find . -name .git -type f` →
  14, confirming each is a regular gitlink pointer, not a directory). The `tree-disk-check.sh` and
  `coverage.sh` prunes target the `.git`/`*/.git/*` **directory** paths, which is why the pointer
  *files* survive into the trees. So the exclusion is precisely: the `.git/` object stores are out;
  the gitlink pointer files that reference them are in.
- **The gitignored `.superpowers/` SDD scratch** — session tooling, **excluded by scope** (it is the
  observation apparatus of this very run, not the frozen subject universe). Verified read-only this
  turn: `git ls-files .superpowers` = **0 tracked**; **103 files on disk, all under
  `.superpowers/sdd/`**, and all 103 are gitignored by the **nested `.superpowers/sdd/.gitignore`
  (a single `*` rule)** — not by any top-level `.gitignore` line (`git check-ignore -v` attributes
  each hit to `.superpowers/sdd/.gitignore:1:*`; the `.superpowers/` directory itself matches no
  ignore rule). The scope decision (session scratch, out) is the reason it is excluded; the nested
  `*` gitignore is the corroborating mechanism. It is named-excluded in `tree-disk-check.sh`.

Corroboration this author computed:

1. **Tree line-counts (whole-tree `wc -l`, symlink-inclusive):** `base_agents` **279,707** ·
   `basicttl` **30,234** · `silmaril` **6,343** · `base_templates` **1,118** · `superpowers`
   **181** · `base_tower` **50** · `example_gippidy_01` **16**. `cat trees/*.tree | wc -l` =
   **317,649**.

2. **Tree ⇆ live disk is now bound and empty-drift for all seven trees** — no longer an ad-hoc
   `diff` of only three trees. `tree-disk-check.sh` (§A.5) diffs `silmaril.tree` and `basicttl.tree`
   against a fresh `find … \( -type f -o -type l \)` under the exact documented exclusions, and runs
   the same for the five corpus roots as bonus coverage: **all seven print `OK  … (tree == disk)`,
   exit 0.** The round-2 re-audit **removed the self-exclusion** the check had carried, so it now
   binds **every** regular file and symlink under silmaril scope — the audit apparatus itself
   (`symlinks.tsv`, `GENERATOR.sh`, `tree-disk-check.sh`, the maps, the account) included — which is
   exactly why `silmaril.tree` had to be regenerated last to carry those files (`6343`). `coverage.sh`
   additionally binds `base_templates` + `base` to their sha256+bytes manifests (§A.1–A.2). So every
   tree is a byte-path-and-symlink partition of its scoped root, not a stale snapshot — and this is
   now enforced by a committed-once gate with no carve-out, not a one-off command.

3. **The 38 tracked `mode-120000` symlinks are now INCLUDED** (they were dropped by an earlier
   `find -type f`): **37 in `base_agents`** (`git -C forge/base_agents ls-files -s | awk
   '$1=="120000"' | wc -l` → 37, incl. `forge/base_agents/.twin → …/cpg-highway/`, 23 `bin/*`
   operator-command links, the `golden/research`, `r1_staging/forge/_joern/apache__jena/*`, `.demo`,
   and `tmp/…/checkpoint.json` links) **+ 1 in `superpowers`** (`external/skills/superpowers/AGENTS.md
   → CLAUDE.md`). Each link's resolved target is recorded in `account/symlinks.tsv` (`path<TAB>target`,
   38 rows) and each emits an explicit `*/symlink-declaration` account row (disposition `reuse`,
   `inverse_evidence = git-tracked mode-120000 symlink -> <target>`).

4. **Forge submodule pins live** (read-only `git submodule status`): `forge/base` **c4e82818**
   (authoritative), `forge/base_agents` **d2b1217f**, `forge/base_templates` **eb3d916b**,
   `forge/example_gippidy_01` **f9be2559**, `external/skills/superpowers` **44c9b2d6**.

5. **Account shape and closed vocabulary:** header
   `path,component_family,disposition,successor_hint,inverse_evidence,provisional_gap` on both CSVs;
   data rows `silmaril.csv` **36,577** + `forge.csv` **281,072** = **317,649**; disposition
   distribution (`cut -d, -f3 | sort | uniq -c`) = `{reuse 313369, migrate 3542, retire 710,
   provisional 27, merge 1}` — all inside the doctrine's closed vocabulary, **zero `conflict`, zero
   `UNCLASSIFIED`** (`awk -F, '$2=="UNCLASSIFIED"||$3=="conflict"'` empty). Retire-without-inverse =
   **0**; provisional-without-gap = **0** (both now machine-enforced by `account-check.sh` (c)).

6. **Account is deterministically reproducible** from the frozen trees + `symlinks.tsv` +
   `account/GENERATOR.sh` (one `awk` classifier keyed on the verbatim path prefix, symlink test
   first). No path can be dropped or hand-edited: every tree path maps to exactly one row and every
   row to a real tree path (`account-check.sh` col-1 diffs empty).

7. **Every one of the seven narrative maps carries the phase-1 protocol in its own header**
   (doctrine-read-in-full + Präriehund/honesty + zero-truncation attestation) — see §C phase 1.

---

## C. Ten-phase audit

Verdicts use artifacts + commit-or-working-tree-edit only. Counts updated to the remediated
**317,649**. PARTIAL is stated where a genuine per-file/interior boundary exists; it is **not**
inflated to SATISFIED nor deflated from it (Phases 3 and 6).

### Phase 1 — seed the agent protocol (doctrine reads + zero-truncation + honesty) into every brief — **SATISFIED**

- **Evidence (the observable proxy — every brief's output carries the protocol):**
  `base_agents.md:4` "Framing law read in full first: `…praeriehund…` + `…unary-byte-frame-law…`";
  `base_templates.md:3` "Framing law read in full first … read all 1118 files IN FULL to EOF";
  `base_foundations.md:7-13` "every PDF paged through the Read tool's `pages` parameter, every page;
  every `.tex` read in full"; `corpus_v17.md:8` "Praeriehund discipline applied … no structure,
  descriptor, runner, or schema was truncated"; `sparky_substrate.md` header table "READ IN FULL
  (129 lines)/(765 lines)" (line counts corrected this turn to match `wc -l`);
  `taxonomy_census.md:6-15` "Doctrine read in full first … never a capped or sampled read";
  `component_account.md:24-26` "Doctrine read in full first … (129 lines) + (765 lines)".
- **Precise boundary (scope note, not a failure):** the *brief texts issued to the sub-agents* are
  not in the ledger; protocol adherence is verified from each artifact's own attestation, which is
  the observable output of that seeding. Every committed artifact evidences the protocol; none omits it.

### Phase 2 — full-clone forge/{base_agents,base_templates,base,example_gippidy_01} as whole trees — **SATISFIED**

- **Evidence:** four forge submodules present and whole (`base_agents` **279,707**; `base_templates`
  1,118; `base` 50; `example_gippidy_01` 16), plus `superpowers` **181**; seven `.tree` files.
  Every tree ⇆ live disk is **bound and empty-drift** by `tree-disk-check.sh` (§A.5, all 7 OK), and
  `coverage.sh` is sha256+bytes EXACT for base_templates/base (§A.1–A.2). `forge/base` pinned
  c4e82818. **Symlink inclusion:** the trees now carry the 38 tracked `mode-120000` symlinks
  (`base_agents` +37, `superpowers` +1) that a prior `find -type f` had dropped.
- **No boundary.** The whole trees are captured and independently proven equal to disk (files + symlinks).

### Phase 3 — map base_agents golden+r1_staging completely (the generics) — **PARTIAL**

- **What is SATISFIED:** `base_agents.md` (commit **b03ce89c**, unchanged this session) is a deep
  AOB-shape map that completely covers the *generics*: the golden contract (§A.1: 21 atlas_columns,
  ≥4 glossaries, 3-witness `_aob` triad, ≥2 claims, FORM-3 `s@p@o`, is:a→`type:type`, dewey_path),
  all seven r1_staging lanes (`_cpgplan/_joern/_spark/_specspec/_tools/_drilled/_critics`, §D), the
  three co-existing AOB representations (§A), the golden audits (`_audit_sparql.yml` FAIL 201/208,
  `_audit_contract.yml` 168/171, §D.7), the byte/tensor substrate (§B), glossary/polysemy (§C),
  projection family (§F), telephone twin (§G), ologs-of-ologs (§H). The whole **279,707**-entry tree
  is captured (Phase 2, symlink-inclusive) and every entry has an account row (Phase 9,
  account-check PASSED).
- **The exact boundary (why PARTIAL, honestly — NOT inflated):** there is **no per-file narrative
  map** of the golden (2,094 files) or r1_staging (1,300 files) atoms — let alone all 279,707 — of
  the kind base_templates received for its 1,118 files. The map is shape/exemplar/audit-level, not
  file-by-file. (Corroborating: `taxonomy_census.md` Row 9 records the prose "2,094 sealed atoms" is
  the golden *file* total while the computed `.aob.dir` atom-directory count is 217 golden / 458
  repo-wide.) This is a **maintainer decision, not a defect** — see §D.1 and the panel §P.5.

### Phase 4 — map base_templates AOB atom-yml macro grammar — **SATISFIED**

- **Evidence:** `base_templates.md` (last commit **124fba3f**; corrected in working tree this turn —
  two honesty fixes, see §P.2 Honesty) + `manifests/base_templates.manifest`. A genuine **full
  per-file map of all 1,118 files, each read to EOF**, every `sha256`+`bytes` pair recomputed against
  the working tree at zero mismatches (§8). Macro grammar mapped in full: `_universal_macros.j2` hub
  (§3.1, B1–B11), `_registries/` grammar owners (§3.2), `_dispatch/` (§3.3), `_urn/` mint (§3.4),
  `_canon/` Dewey law (§3.5), `semantic_render_target.j2` 25/21/46-column contract (§3.6),
  `_tensor/`, `_validate/urn_grammar` (§3.7). coverage.sh = EXACT 1118, sha256+bytes verified (§A.1).
- **No boundary.** Full per-file depth achieved.

### Phase 5 — map base category theory (sheaf/semiring/lens; LaTeX turtles/polysemy) — **SATISFIED**

- **Evidence:** `base_foundations.md` (commit **124fba3f**, unchanged this session) +
  `manifests/base_tower.manifest`. Full-capture map of all 50 files, **every PDF paged through and
  every `.tex` read in full**; all 50 digests independently recomputed. Category theory covered:
  `AGENT.md` (Σ,B,λ) bialgebra (§4.1), I-fundamenta Yoneda+Lambek (§4.2), II-en (§4.3), IV-turtles
  eleven strata (§4.4), V-polysemy functorial semantics incl. semirings/sheaves/lenses/Rosetta
  (§4.5), all ten `skills/**/*.md` incl. `federate/sheaf.md`, `provenance/semiring.md`,
  `optics/lens.md` (§4.7). coverage.sh = EXACT 50, sha256+bytes verified (§A.2). Records the
  license/version skew and the `9e60c103` non-existence.
- **No boundary.** Full per-file depth achieved; `III-*` absence recorded as found (not a gap).

### Phase 6 — map example_gippidy_01 v17 in full (projection family, Jena runners, split-ZIP reassembly, AOB atom-yml) — **PARTIAL**

- **What is SATISFIED (all four named deliverables, done in full):** `corpus_v17.md` (last commit
  **f15f578a**; corrected in working tree this turn — the ZIP count, see §P.2 Completeness/Honesty)
  actually **reassembled both split-ZIP payloads** (all 6 slice hashes + payload SHA-256 verified per
  family; §2), materialized the tree (509 members consolidated / 476 semantic-formats; §3), mapped
  the **projection family** in full (§3–4), mapped the **Jena 6.2.0 native runners** in full (§4.2),
  quoted the **split-ZIP reassembly recipe verbatim** (§2), mapped the **AOB atom-yml** schema
  (§6.1–6.2), and **brute-forced the coordinate rule over all 104,848 sqlite rows with 0 mismatches**
  (§5.2). The ZIP-file inventory is now stated correctly: **14** zip files (12 numbered slices + 2
  `-control.zip`; `find forge/example_gippidy_01 -name '*.zip' | wc -l` = 14, matching tree/census
  Row 7).
- **The exact boundary (why PARTIAL, honestly — NOT inflated):** the on-disk tree captures only the
  **16 outer transport files** (README + `.git` + 14 split-ZIP slices), and the account has exactly
  **16 gippidy rows** (2 reuse wrapper + 14 migrate slices). The **ZIP interiors — the ≈505
  materialized projection-plane members and the 104,848 per-identity carriers — are
  characterized/sampled in the scratchpad reassembly, not extracted per-file into the trees or
  account.** The map itself flags this: bulk data (1.68M rebindings, 29.4M turtle statements) was
  **sampled, never fully read** (§0/§9). This is a **maintainer decision, not a defect** — see §D.2
  and the panel §P.5.

### Phase 7 — map sparky/lambda-blotto + reference/pylib red receipts — **SATISFIED**

- **Evidence:** `sparky_substrate.md` (last commit **c189532b**; corrected in working tree this turn
  — the `lambda`-twin disposition is now the round-2 **MIGRATE with package-level evidence**, see
  §P.2 Doctrine and the Round-2 re-audit resolutions note). Live engine census (2,277 `.py`,
  three-root mirror PROCESS+APPLY+SLOTS / VALUE / DEPENDENCY, §1), `lambda_blotto/` 220 files (§1.1),
  the static conformance gate (§1.3), the edge cases (5 pickle de-mux, §1.4), `reference/pylib`
  legacy census (719 files, 398 `__init__.py`, orphaned, §2), the frozen RED-receipt target table
  (§4) plus a staleness reconciliation of the 2026-07-16 doc vs 2026-08-07 live (§4.1).
- **Lambda resolution (round-2 R6 state — supersedes the R1 `reuse` claim):** the reserved-keyword
  `sparky/lambda/` twin is a **live module** (a Python reserved keyword, so loaded only dynamically),
  reached from the engine via `importlib.import_module("silmaril.sparky.lambda.…")` string literals.
  R1 stamped its 66 account rows as **`reuse`** with a per-row "call-site" framing; the round-2
  re-audit corrected both errors. **It is now disposition `migrate`**, successor **"fold onto the
  lawful `lambda_` sibling under the unary refactor (X)"**, with evidence stated **once, at the
  package level**: *member of the reserved-keyword lambda package live-wired into the engine via
  **37 importlib call-sites resolving 5 entrypoint modules** in `scripts/python/pylib/src` (excl
  `reference`)* — the 37/5 is a property of the package, not "37 call-sites" restamped on each of the
  66 rows. `migrate` (not `reuse`) because the reserved keyword `lambda` cannot survive the unary
  refactor: it MUST fold onto `lambda_`, which is pending X-workflow work, not a keep-as-is. It is a
  live module, so it is **not** retired.
- **Boundary note (not a phase failure — honestly recorded by the map):** the two law-continuation
  docs `…-enforcement-proof.md` and `…-receipts.md` are **absent from this checkout** (§0); all §4
  census numbers rest on the single index law doc. A source-availability gap the map names.

### Phase 8 — taxonomy census — every distinct taxonomy — **SATISFIED**

- **Evidence:** `taxonomy_census.md` (last commit **a02090ff**; corrected in working tree this turn —
  the partition-scope claim de-overreached and the symlink inclusion recorded, see §P.2). 13 census
  rows (every distinct taxonomy, incl. the co-resident ones inside base_agents: `.aob.dir` Row 9,
  `_specspec` Row 10, CorpusAtom Row 11), plus `## Axes` (A1–A12), `## Projection families` (PF1–PF7),
  `## Version-skew register` (VS1–VS6), and `## Honest-gap register` (now **35** gaps — gap 35 records
  the symlink inclusion). All five census-check-required section headers present. census-check =
  PASSED **317649** (§A.3). Cardinalities computed over whole-tree files+symlinks, cited per row and
  updated to the symlink-inclusive totals (`base_agents` 279,707; `superpowers` 181; `silmaril` 6,343).
- **No boundary to the census itself.** (basicttl and superpowers being captured only via
  tree+census-row+account-row, with no dedicated *narrative* map, is recorded as census gaps 31/34 and
  carried to §D — it does not make the census incomplete.)

### Phase 9 — Complete-Component-Account seed (predecessor/successor row per physical entry + inverse) — **SATISFIED (seed scope)**

- **Evidence:** `component_account.md` (last commit **774dcc4e**; revised in working tree this turn —
  the R1 revision that dissolves the two panel-confirmed defects) + `account/{silmaril,forge}.csv` +
  `account/symlinks.tsv` + `account/GENERATOR.sh`. **Every one of the 317,649 physical entries (now
  including the 38 symlinks) has exactly one account row** (account-check PASSED, §A.4;
  deterministically regenerable, §B.6) with `disposition` (closed vocabulary), `successor_hint`,
  `inverse_evidence`, `provisional_gap`. Retire families carry consumer-closure + byte-complete-inverse
  grades (§6). Provisional rows number **27** — all in the genuinely-unresolvable
  `silmaril/engine/legacy-reference-aob-layout` family, each inherited from the census honest-gap
  register, not minted (§7). (Lineage: 93 provisional pre-R1 → R1 moved the 66 `lambda`-twin rows
  out, leaving 27; round-2 corrected *where* those 66 landed — **`migrate`**, not `reuse` — but the
  provisional total is unchanged at 27.) Disposition distribution is now
  `{reuse 313369, migrate 3542, retire 710, provisional 27, merge 1}`. The doctrine invariants
  (UNCLASSIFIED-never, conflict-never, retire⇒inverse, provisional⇒gap) are now machine-enforced by
  `account-check.sh` (c).
- **The exact boundary (scope, honestly):** this artifact is explicitly the **SEED**: it carries
  locator + family + disposition + successor + inverse + gap, **not** the doctrine's fuller per-row
  coordinate set (physical device/inode, byte revision, semantic-family progenitor, independent
  S:O:P towers). Two `inverse_evidence` values are **must-exist** (not yet built): the
  `ontology/ui-shapes.ttl` render step, and the `reference/` content-addressed
  predecessor/successor account. The phase asked for a *seed with predecessor/successor + inverse*,
  delivered for all 317,649 rows; the fuller coordinate set and the two must-exist inverses are
  downstream (W3/W5) — carried to §D.

### Phase 10 — ledger to distinct files — **SATISFIED**

- **Evidence:** distinct git-tracked files under `ledger/W1/`, one concern per file: seven narrative
  maps (`base_agents.md`, `base_templates.md`, `base_foundations.md`, `corpus_v17.md`,
  `sparky_substrate.md`, `taxonomy_census.md`, `component_account.md`), seven `trees/*.tree`, two
  `manifests/*.manifest`, **four** `checks/*.sh` (`coverage`, `census-check`, `account-check`,
  **`tree-disk-check`** — the new fifth gate), and **four** `account/` files (`GENERATOR.sh`, two
  CSVs, `symlinks.tsv`). This realizes STRICTNESS Rule 14 "Distinct Files for Distinct Concerns."
  **Every in-scope ledger artifact is now in the tree AND the account.** R1 pulled the 8 originally-
  dropped artifacts (`taxonomy_census.md`, `component_account.md`, `checks/census-check.sh`,
  `checks/account-check.sh`, `account/GENERATOR.sh`, `account/forge.csv`, `account/silmaril.csv`, and
  this `W1_VERIFICATION.md`) back in but then **named-excluded** the two audit files it created
  (`account/symlinks.tsv`, `checks/tree-disk-check.sh`) — the round-2 defect. **Round-2 fix:** those
  two are now **carried in `silmaril.tree` and the account too** (the self-exclusion removed;
  `silmaril.tree` regenerated last). So the full silmaril delta is now **`+10`** (`ledger` region
  `16 → 26`), not `+8` with a `−2` carve-out. No ledger artifact is named-excluded from the tree any
  longer; `tree-disk-check.sh` binds all of them to disk.
- **Boundary (honest):** the ledger working tree is **not clean** — the R1+R6 set is uncommitted (see
  the status box at the top). Rule 14 as to *distinct files* holds; durability requires the commit.

**Phase tally:** SATISFIED = 1, 2, 4, 5, 7, 8, 9-as-seed, 10 (eight). PARTIAL = 3, 6 (two).
UNSATISFIED = none.

---

## D. Depth boundaries carried to the maintainer (rule on these before W2)

Each is a genuine boundary the fresh evidence confirms; none blocks the five acceptance checks, but
each is a decision the maintainer/panel must own.

1. **base_agents per-file depth (Phase 3 PARTIAL).** golden (2,094) + r1_staging (1,300) — indeed
   all 279,707 — are whole-tree-captured + fully account-rowed + deeply shape-mapped, but **not**
   narrated per-file the way base_templates' 1,118 were. Rule: require a per-file narrative pass, or
   accept shape-depth as sufficient for the generics. **(Maintainer decision, not a defect.)**

2. **gippidy ZIP-interior depth (Phase 6 PARTIAL).** The 16 outer transport files are captured +
   accounted; the reassembled interior (≈505 materialized members; 104,848 per-identity carriers)
   was characterized/sampled and hash-verified but **not** extracted per-file into the trees/account.
   Rule: require interior extraction-and-accounting, or accept the v17-map characterization.
   **(Maintainer decision, not a defect.)**

3. **basicttl and superpowers lack dedicated narrative maps.** `basicttl` (30,234) and
   `external/skills/superpowers` (181) are fully tree-captured, census-rowed (Rows 3/8), and
   account-rowed, but have **no dedicated discovery map** (census gaps 31/34). Rule: commission
   narrative maps, or accept tree+census+account coverage.

4. **The 35 census honest-gap register — resolution ownership.** Many gaps are cross-tree or
   out-of-checkout and cannot be closed inside W1: the two absent law-continuation docs, the absent
   `primitives.ttl` SPECIES catalog, the sbt Scala engine not in this tree, etc. Rule: assign each
   gap an owner (W2 design / live probe / external fetch).

5. **The two must-exist retire inverses (Phase 9 / account §6).** `ontology/ui-shapes.ttl` (render
   step not yet evidenced) and the whole `reference/` tree (retire rows; content-addressed
   predecessor/successor account must be recorded first). Per Präriehund/doctrine, **no deletion
   until these inverses exist** — W3's hard gate.

6. **The AOB-expansion disagreement remains OPEN (census gap 30) — resolved to honest-provisional,
   NOT force-fit.** `corpus_v17.md` §6 now marks the expansion `[inference]` *Atom-of-Being* (not
   asserted); `base_templates.md` §Orientation now marks it `[inference]` *Atom-Oriented-Bundle* (not
   asserted); `base_foundations.md` §6.1 marks it genuinely unresolved. Rule: pick a canonical
   expansion (the ledger will not guess).

7. **`forge.csv` exceeds GitHub's 50 MB soft-warning.** Measured this turn: **`account/forge.csv` =
   55,460,429 bytes = 52.89 MiB** — over GitHub's 50 MiB (52,428,800) soft warning by ~2.89 MiB
   (grew by the 38 symlink rows from the earlier 55,451,778; unchanged by round-2, which touched only
   `silmaril.csv`). `account/silmaril.csv` = **5,166,263 bytes = 4.93 MiB** (round-2: +2 ledger rows
   and the reworded lambda evidence), well under. Pushes fine (soft warning, not the 100 MB hard
   limit); the panel should decide whether to split/compress/relocate `forge.csv` or accept the warning.

8. **Phase-1 brief text is not in the ledger.** Protocol adherence is verified via each artifact's
   own doctrine-read/honesty/zero-truncation attestation (§C phase 1). Rule: accept the output-proxy,
   or require the briefs be archived.

9. **The R1+R6 remediation is uncommitted.** The green state (R1 plus the round-2 re-audit fixes)
   lives in the working tree on top of HEAD `774dcc4e`. Rule: commit the R1+R6 set (13 modified + 3
   untracked) so the checks' green becomes pinned; this read-only author does not perform the commit.

---

## E. Verification statement

On fresh read-only evidence gathered this turn, I assert only the following:

1. **All FIVE acceptance checks pass fresh and green:** coverage `forge/base_templates` = EXACT 1118
   (sha256+bytes verified); coverage `forge/base` = EXACT 50 (sha256+bytes verified); census-check =
   PASSED 317649 across 7 trees; account-check = PASSED 317649 rows; tree-disk-check = all 7 trees
   `OK (tree == disk)` (§A, each exit 0, output pasted verbatim).

2. **The seven trees are a byte-path-and-symlink-exact partition of a precisely-scoped set —
   totalling 317,649** — namely the tracked-and-physical file-and-symlink set of the six mapped
   corpus roots plus the silmaril repository tree, **EXCLUDING the `.git/` object-store directory
   trees and the gitignored `.superpowers/sdd/` SDD scratch** (§B). The exclusion is precise: only
   the `.git/` *directories* are out — **the 14 `.git` submodule-gitlink *pointer files* (regular
   files) ARE included**, each with a tree line and account row; and `.superpowers/` is excluded by
   scope (session scratch), its 103 files all gitignored by the nested `.superpowers/sdd/.gitignore`
   `*` rule. It is **not** "the live filesystem" tout court. Tree ⇆ disk is bound and empty-drift for
   **every** tree by `tree-disk-check.sh` — now **with no self-exclusion**, so the audit apparatus
   itself is bound too (files + symlinks, under the documented exclusions) — and `forge/base` is
   pinned at the authoritative `c4e828188a57d7a93c4f4972859dd0862ae6cce6` (`9e60c103…` does not exist).

3. **The 317,649-row Complete-Component-Account seed is deterministically reproducible** from the
   frozen trees + `symlinks.tsv` + `GENERATOR.sh`; every disposition is inside the closed vocabulary
   (`{reuse 313369, migrate 3542, retire 710, provisional 27, merge 1}`, zero conflict/UNCLASSIFIED);
   every physical entry — including all 38 symlinks — maps to exactly one row; and the doctrine
   invariants (UNCLASSIFIED-never, conflict-never, retire⇒inverse, provisional⇒gap) are
   machine-enforced (§A.4/§B.5–B.6).

4. **The ledger working tree is NOT clean** — the R1+R6 remediation is uncommitted at HEAD
   `774dcc4e` (13 tracked modified + 3 untracked: `W1_VERIFICATION.md` (this file),
   `account/symlinks.tsv`, `checks/tree-disk-check.sh` — the latter two still `??` on disk yet now
   carried in `silmaril.tree`). I do **not** claim a clean working tree. The unchanged maps verify at
   their commits (`base_agents.md` b03ce89c; `base_foundations.md` 124fba3f); the five corrected maps,
   three regenerated trees, both CSVs, `GENERATOR.sh`, and the two hardened checks carry uncommitted
   R1+R6 edits on top of `774dcc4e`.

5. **Eight phases are SATISFIED (1, 2, 4, 5, 7, 8, 9-as-seed, 10) and two are PARTIAL (3, 6)** at the
   precise, stated boundaries in §C. **No phase is UNSATISFIED.** I do **not** assert per-file
   narrative depth for base_agents (Phase 3), per-file interior extraction for gippidy's 104,848
   identities (Phase 6), the full doctrine per-row coordinate set for the account (Phase 9 is a
   seed), or that the two must-exist retire inverses / the 35 named gaps / the AOB expansion are
   resolved — those are the open boundaries in §D.

I assert nothing beyond what the fresh evidence in §A and §B supports.

*Silmaril · GraphAtlas — "Inspizierbar. Revidierbar. Föderiert." · Nihil occultum, tantum textum.*

---

## Adversarial triple panel

Author: W1 PANEL SYNTHESIZER. Frame date: `2026-08-07`. Doctrine read in full first this turn.
Every disk fact below was re-verified read-only this session (commands + outputs above); no
state-changing git was run.

**Correction of the prior panel record (P.0 of the earlier draft).** The earlier synthesis was
crippled: **only the `completeness` angle's finding payload reached the synthesizer, truncated at
its final observation** — the `honesty` and `doctrine` angles were **lost to truncation**, and the
earlier panel therefore adjudicated one angle in full and could speak for neither of the other two.
That gap is now **CLOSED**: all three angles' CONFIRMED findings are carried below **with their
resolutions**. The earlier `sub_survives = 0 / sub_total = 0` ambiguity that the prior draft (rightly,
under Präriehund) refused to launder into a GO is **moot** — every finding below was independently
CONFIRMED on disk this session, and each has a concrete fix in the working tree; the panel adjudicates
on that direct evidence, not on an absent sub-subagent metric.

Severity legend: **CRITICAL** = false universal claim or a whole class of entries with no honest
row; **IMPORTANT** = a real class silently excluded, or a check that cannot catch a live violation;
**MINOR** = check over-promises / cosmetic count, no live violation. All fixes below sit in the
working tree on top of HEAD `774dcc4e` (uncommitted; see the status box) unless a commit is cited.

### Angle 1 — COMPLETENESS (every in-scope physical entry has an honest row)

- **CRITICAL — `silmaril.tree` was stale; ≥8 in-scope committed ledger artifacts absent; three
  universal claims false.** The earlier `silmaril.tree` (6,333) omitted 8 in-scope ledger files
  (`taxonomy_census.md`, `component_account.md`, `checks/census-check.sh`, `checks/account-check.sh`,
  `account/GENERATOR.sh`, `account/forge.csv`, `account/silmaril.csv`, `W1_VERIFICATION.md`), so the
  account claimed "every physical entry has exactly one row" while these had none — and no acceptance
  check bound `silmaril.tree` to disk. **RESOLVED (R1):** `silmaril.tree` regenerated to **6,341**
  (the `+8`, `ledger` region 16 → 24), each of the 8 now carrying a tree line **and** an account row;
  **`tree-disk-check.sh` added** (the new fifth gate) diffing `silmaril.tree` + `basicttl.tree`
  against live disk under the documented exclusions — both print `OK (tree == disk)`, exit 0
  (§A.5). The 103 `.superpowers/` files are ruled **OUT-and-NAMED** (gitignored SDD scratch;
  `git ls-files .superpowers` = 0; named-excluded in the check). **ROUND-2 (R6) ADDENDUM — R1's fix
  was itself incomplete:** R1 created two audit files (`account/symlinks.tsv`,
  `checks/tree-disk-check.sh`) and then named-excluded them from `silmaril.tree`, with a matching
  self-exclusion in the check — reintroducing the stale-tree class one layer up. **Now RESOLVED:**
  `silmaril.tree` regenerated **last** carries both (**6,341 → 6,343**, region 24 → 26), each with an
  account row, and the check's **self-exclusion is removed** so it binds every file including the
  audit apparatus (§A.5 `OK  silmaril  6343`). Fix location: `trees/silmaril.tree`,
  `account/silmaril.csv`, `checks/tree-disk-check.sh` (working tree).

- **IMPORTANT — 38 tracked/physical symlinks excluded from every tree, census, and account.** An
  earlier `find … -type f` (and every tree's generation) silently dropped symbolic links: 37 in
  `base_agents` (incl. `.twin`, the JEPA/telephone bridge the base_agents map itself leans on) + 1
  in `superpowers` — in no tree, no census cardinality, no account row, while the account claimed a
  row for "every physical entry." **RESOLVED:** the trees were regenerated symlink-inclusive
  (`base_agents` 279,670 → **279,707**, `superpowers` 180 → **181**); `account/symlinks.tsv` (38
  rows, `path<TAB>target`) records each resolved link-target; `GENERATOR.sh`'s **first** classifier
  rule emits an explicit `*/symlink-declaration` account row per symlink (disposition `reuse`,
  inverse = the real link target); census gap **35** names the inclusion; the `-type f` boundary is
  now **named**, not folded into a completeness claim (Präriehund). Fix location: three regenerated
  trees, `account/symlinks.tsv`, `GENERATOR.sh`, both CSVs, `taxonomy_census.md` gap 35.

- **MINOR — gippidy ZIP inventory said "13 zip files", disk has 14.** `corpus_v17.md` §2 stated
  "13 zip files total"; the tree/census Row 7 count 14. **RESOLVED:** corrected to **14** (12
  numbered slices + 2 `-control.zip`; verified `find forge/example_gippidy_01 -name '*.zip' | wc -l`
  = 14). Fix location: `corpus_v17.md` §2. (No live-count elsewhere depended on the wrong figure.)

### Angle 2 — HONESTY (no claim broader than what was demonstrated; every citation lands)

- **CRITICAL — "partition of the physical universe / live filesystem" over-declared the total, and
  "diff empty for every tree" was demonstrated for only three.** `taxonomy_census.md` claimed the
  seven trees partition "the physical universe" and `W1_VERIFICATION.md §B.2/§E.2` claimed "diff
  empty for every tree" while only 3 trees had actually been diffed. **RESOLVED:** the census now
  reads "**partition of a precisely-scoped set — not of 'the physical universe'**" and states the
  exact scope (tracked-and-physical file-and-symlink set of the six mapped roots + the silmaril repo
  tree, **excluding `.git` and gitignored `.superpowers/`**); this verification doc's §B/§E carry the
  same scoped statement; and the "tree ⇆ disk empty-drift for **every** tree" claim is now **true**
  because `tree-disk-check.sh` actually binds all seven (§A.5), not because a universal was asserted
  on three. Fix location: `taxonomy_census.md` partition paragraph; this doc §B/§E; `tree-disk-check.sh`.

- **IMPORTANT — false "verified working-tree HEAD" in base_templates.md.** The map claimed
  "submodule **AND superproject** `git rev-parse HEAD` both equal the pin `eb3d916b`" — false: the
  superproject's own HEAD is a silmaril commit (e.g. `774dcc4e`), it records the pin only through its
  **gitlink**. **RESOLVED:** the map (Overview row + §7 resolution 1) now states the submodule's OWN
  HEAD equals the pin, and the superproject records that same pin via `git ls-tree HEAD
  forge/base_templates` → `160000 commit eb3d916b…` while its own `git rev-parse HEAD` is a silmaril
  commit — the exact, true relationship. Fix location: `base_templates.md` (working tree).

- **MINOR — misattributed citation in base_templates.md.** The determinism law *"Key order in the
  dict IS the byte order"* was attributed to `atlas_typedef.j2`; the verbatim string actually lives
  in `_registries/atlas_entity.j2:40` (`grep` → single corpus hit there). **RESOLVED:** the map now
  attributes the string to `atlas_entity.j2:40` and notes `atlas_typedef.j2`'s own `j_object` comment
  states the rule in different words. Fix location: `base_templates.md` (working tree).

- **MINOR — wrong doctrine line counts in sparky_substrate.md.** The header table read
  praeriehund "130 lines" / unary "766 lines"; `wc -l` = **129** / **765**. **RESOLVED:** corrected
  to 129 / 765 (matches `wc -l` this turn). Fix location: `sparky_substrate.md` header table.

- **IMPORTANT — `census-check.sh` was self-referential (green rested only on internal cross-checks).**
  `census-check.sh` tests only that trees are non-empty + census sections present; `account-check.sh`
  diffs the CSV against the **trees themselves**; nothing bound the trees to live disk — so a stale
  `silmaril.tree` stayed green behind every check (this is how the CRITICAL completeness finding
  hid). **RESOLVED:** `tree-disk-check.sh` is the new fifth gate that binds trees to live disk;
  green no longer rests only on internal consistency. Fix location: `checks/tree-disk-check.sh` (new).

- **MINOR — `coverage.sh` "EXACT" was path-coverage, not content-integrity.** The old check diffed
  only the path column (`cut -f3`); a corrupted sha256 or byte count would still print `COVERAGE
  EXACT`. No live violation (manifests were content-honest). **RESOLVED:** `coverage.sh` now
  re-hashes every file's sha256 (col1, `sha256sum -c --strict`) and re-measures bytes (col2), failing
  on any mismatch; output now reads "… sha256+bytes verified" (§A.1–A.2). Fix location: `checks/coverage.sh`.

- **IMPORTANT — `account-check.sh` did not enforce the doctrine invariants (UNCLASSIFIED / conflict /
  retire⇒inverse / provisional⇒gap).** The old check tested only col-1 path-set and col-3 vocabulary;
  a stray `UNCLASSIFIED` family, a `conflict` disposition, a retire without inverse, or a provisional
  without a named gap would all pass. Current data satisfied them anyway (no live violation), but the
  gate could not catch a future one. **RESOLVED:** `account-check.sh` (c) now rejects `NF!=6`,
  `component_family==UNCLASSIFIED`, `disposition==conflict`, `retire && inverse==""`, and `provisional
  && gap==""`. Fix location: `checks/account-check.sh`.

### Angle 3 — DOCTRINE (Präriehund honesty; PROVISIONAL only for the genuinely unresolvable)

- **IMPORTANT — AOB expansion force-fit in TWO maps (violates "name the gap, don't force-fit").**
  `corpus_v17.md` §6 asserted the acronym as **"Atom-of-Being"** and `base_templates.md` §Orientation
  asserted it as **"Atom-Oriented-Bundle"** — each stated as fact though neither corpus spells it
  (`grep -rE 'Atom.of.Being' forge/example_gippidy_01` = 0; `grep -rE 'Atom-Oriented|Oriented.Bundle'
  forge/base_templates` = 0), and the two maps **contradict each other**. This is the Sykophant move
  the doctrine names: pressing an unknown into a confident bin. **RESOLVED (both):** each expansion is
  now marked `[inference] … not asserted as fact`, each cites its 0-hit grep, and **census gap 30
  holds the cross-map disagreement open** for the maintainer to rule — the honest *partiell*
  functor, not a fabricated identity. Fix location: `corpus_v17.md` §6, `base_templates.md`
  §Orientation, `taxonomy_census.md` gap 30. **(Two force-fits, both resolved.)**

- **IMPORTANT — `lambda`-twin marked PROVISIONAL to dodge resolvable work (violates "PROVISIONAL only
  for the genuinely unresolvable").** `sparky_substrate.md` §1.4 and the account (66 rows) had held
  the reserved-keyword `sparky/lambda/` twin PROVISIONAL — "live-reachable via importlib or orphaned
  dead weight unresolved" — when the resolving evidence was **a grep the map itself named**. A
  provisional gap must document a *genuine* unresolvable, not park tedious-but-doable verification.
  **RESOLVED (R1) — then CORRECTED (round-2 R6):** the twin is a live module (a Python reserved
  keyword, loaded **only** dynamically via `importlib.import_module("silmaril.sparky.lambda.…")`
  string literals), so the provisional dodge is dissolved and the 66 rows leave `provisional`
  (provisional total 93 → **27**, only the genuinely-unresolvable
  `silmaril/engine/legacy-reference-aob-layout` family remains). **But R1's landing was itself wrong
  twice, and the round-2 re-audit fixed both:** (1) R1 stamped the rows `reuse` — implying no work
  pending — when the reserved keyword `lambda` MUST fold onto the lawful `lambda_` sibling under the
  unary refactor (X); that is a **migration**, so the 66 rows are now disposition **`migrate`** with
  successor "fold onto the lawful `lambda_` sibling under the unary refactor (X)"; (2) R1's evidence
  was framed per-row as if each of the 66 rows were itself a call-site; the round-2 evidence is
  **package-level, stated once**: *member of the reserved-keyword lambda package live-wired via
  **37 importlib call-sites resolving 5 entrypoint modules** in `pylib/src` (excl `reference`)* — the
  37/5 is a property of the package the rows belong to, not restamped on each row. Disposition thus
  moves `reuse` `313433` → **`313369`** / `migrate` `3476` → **`3542`** (see §B.5). Fix location:
  `sparky_substrate.md` §1.4 + gap 3, `component_account.md` round-2 revision, both CSVs.

### The two PARTIAL depth boundaries — maintainer decisions, NOT defects (the panel does not wave them through)

Distinct from every finding above, these two are **scope decisions the panel deliberately does NOT
launder into either a pass or a fail** — they are the honest Präriehund *ehrlich markierte* boundary,
disclosed by the record (§C Phase 3/6, §D.1–2), corrupting no claimed number:

- **base_agents per-file narrative depth (Phase 3 PARTIAL).** All 279,707 entries are
  whole-tree-captured, fully account-rowed, and deeply *shape*-mapped; golden (2,094) + r1_staging
  (1,300) are **not** narrated per-file the way base_templates' 1,118 were. Not inflated to SATISFIED.

- **gippidy ZIP interiors (Phase 6 PARTIAL).** The 16 outer transport files are captured and
  accounted; the reassembled interior (~505 materialized members; 104,848 per-identity carriers) was
  characterized, sampled, and hash-verified — **not** extracted per-file. Not inflated to SATISFIED.

The maintainer must **rule**: require the per-file narrative pass + the interior
extraction-and-accounting, or sign a decision that shape-depth + whole-tree capture + full account
rows (base_agents) and executed hash-verified reassembly + the full 104,848-row coordinate
brute-force (gippidy) are **sufficient** and per-file interior depth is out of W1 scope. That ruling
is the maintainer's to sign; the panel neither grants it nor overrides it.

### Panel recommendation — **GO** (W1 as a green-certified deliverable, on the R1+R6 content)

All three adversary angles are now on record and adjudicated. Every CONFIRMED finding — one CRITICAL
per angle at its worst (stale `silmaril.tree`; "physical-universe" over-declaration), the IMPORTANT
class-exclusions and check-strength gaps (38 symlinks; false HEAD; self-referential census-check;
unenforced account invariants; AOB force-fit ×2; `lambda`-twin dodge), and the MINOR cosmetic/count
items (13-vs-14 zips; misattributed citation; line counts; coverage path-only) — **is resolved**, and
each fix was independently re-verified on disk this session. **The round-2 (R6) re-audit then found
two defects R1 had itself re-introduced — (1) the stale-tree class returned, masked by a
`tree-disk-check` self-exclusion that hid two absent self-created audit files, and (2) the 66
`lambda`-twin rows over-claimed their evidence and were mis-dispositioned `reuse`; BOTH are now
RESOLVED** (`silmaril.tree` regenerated last → 6343, self-exclusion removed, total 317649; the 66
rows are `migrate` with package-level 37-call-sites→5-entrypoints evidence — see the Round-2 re-audit
resolutions note and Angle 1/Angle 3 addenda). **No Critical or Important finding survives
unaddressed**, so under the rule "GO only if no Critical/Important finding survives unaddressed" the
panel returns **GO**. The two PARTIAL depth boundaries (Phases 3, 6) are honest maintainer decisions,
not blockers, and remain the maintainer's to sign.

**One operational condition on the GO (honest, not a finding):** the entire R1+R6 remediation
currently lives in the **working tree, uncommitted** on top of HEAD `774dcc4e` (13 modified + 3
untracked; see the status box). The green is real and re-verified, but it is not yet pinned to a
commit. The panel's GO is on the R1+R6 *content*; making it durable is the single remaining step —
committing the set — which this read-only author does not perform.

*Silmaril · GraphAtlas — full three-angle panel synthesis. "Inspizierbar. Revidierbar. Föderiert." ·
Nihil occultum, tantum textum.*
