# W1 Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete workflow W1 of the approved rebuild DAG — full-capture discovery and
taxonomy mapping — by producing the two missing corpus maps, the taxonomy census, and the
Complete-Component-Account seed, all under zero-truncation and Praeriehund law.

**Architecture:** W1 is a documentation/mapping workflow, not a code workflow. Its "tests"
are executable coverage checks: for each map, a machine-generated full-tree inventory is
diffed against the map's coverage manifest — the check FAILS (red) before the map exists
and PASSES (green) only when every physical file is accounted for. Mapping fans out across
subagents partitioned by a complete inventory (never by eyeballed directory listings), a
synthesizer merges fragments into the ledger artifact, and a task reviewer gates each task
(spec compliance + quality) before the controller commits.

**Tech Stack:** Bash (find/sha256sum/diff for inventories and checks), Read tool
(sequential-window reads to EOF for oversized files), git (controller only), markdown
ledger artifacts under `ledger/W1/`.

## Global Constraints

Binding on every task, every subagent, every step. Sources: STRICTNESS_RULES.md, the
maintainer's verbatim rulings (TRANSCRIPT_VERBATIM.md), and the two doctrine documents.

1. **Doctrine reads first.** Every subagent's first actions, before ANY analysis:
   read `docs/praeriehund-demokratie-der-kategorien.md` IN FULL, then
   `docs/unary-byte-frame-law.md` IN FULL. Maintainer verbatim: *"the prairehund
   documentation plus urnary are strictly required for every agent/subagent to read."*
2. **Zero truncation.** Maintainer verbatim: *"ANY AND ALL 'truncations' and trees,
   finds, checkouts, outputs are strictly banned"* and *"FILE TREES ARE OUR TAXONOMY."*
   Concretely: no `-maxdepth`, no `head`/`tail`, no capped or sampled output, no
   `git ls-tree` in place of reading, no partial Read that does not continue to EOF.
   A file too large for one Read is read in sequential offset windows to its last line —
   that is a full read in passes, not a truncation. The only path exclusion anywhere is
   `*/.git/*` internals (git plumbing, protected by STRICTNESS rules — not corpus).
3. **Praeriehund honesty.** Quote verbatim, then interpret; mark every inference as
   inference. PROVISIONAL is reserved for genuinely unresolvable unknowns and always
   carries a documented gap; it is never a device to dodge resolvable work. Never
   force-fit; never fabricate; partial functors are declared partial.
4. **Read-to-EOF evidence.** Every per-file map entry quotes the file's final line (or
   for binary files states the final-bytes digest context) — cheap proof the read reached
   the end.
5. **Subagents never change git state.** No add/commit/checkout/reset/submodule/push —
   read-only git queries only. Subagents write ONLY to their assigned output paths
   (their fragment/report files in the SDD workspace, or their assigned `ledger/W1/`
   artifact). The controller alone commits, on branch
   `claude/custom-pgp-sign-git-thh37n`, pushing with `git push -u origin <branch>`.
6. **No model identifier** in any commit message or committed artifact. Commit trailers:
   `Signed-off-by: Claude <claude@silmaril.internal>`,
   `Co-Authored-By: Claude <noreply@anthropic.com>`,
   `Claude-Session: https://claude.ai/code/session_01PzjvWAy57mdKkATELTijVP`.
7. **The maintainer merges PRs; the agent never merges.**
8. **Escalation, not assumption.** A subagent that hits genuine ambiguity reports
   NEEDS_CONTEXT/BLOCKED to the controller rather than guessing; the controller escalates
   to the maintainer if it cannot resolve from documented answers. Maintainer verbatim:
   *"if it aint crystal fucking clear, you ask."*
9. **Interpretive-gate ban.** No brief may pre-load conclusions ("if you see X, that's
   Y"). Briefs name what to capture, never what to conclude.

---

### Task 1: Full-capture map of forge/base_templates

**Files:**
- Create: `ledger/W1/base_templates.md` (the map)
- Create: `ledger/W1/manifests/base_templates.manifest` (tab-separated: `sha256<TAB>bytes<TAB>path`, one line per file)
- Create: `ledger/W1/checks/coverage.sh` (shared acceptance check, used by Tasks 1–2)
- Workspace scratch: `.superpowers/sdd/2026-08-07-w1-completion/t1-*` (inventory, slices, fragments, reports)

**Interfaces:**
- Consumes: `forge/base_templates` working tree at commit `eb3d916b0db5c1429e0ce5abaac7b6b75aadea18`; doctrine docs; the AOB findings already committed in `ledger/W1/base_agents.md` (for cross-referencing macro grammar to AOB spec blocks — read, cite, do not re-derive).
- Produces: `ledger/W1/base_templates.md` — consumed by Task 3 (census), Task 4 (account), and W2 design. `ledger/W1/manifests/base_templates.manifest` — consumed by the coverage check and by Task 4 as byte anchors (the unary law's z-coordinate is the uint16 of the first two octets of `source_sha256`; the manifest is therefore coordinate evidence, not bookkeeping).

- [ ] **Step 1: Write the acceptance check (shared for Tasks 1–2)**

```bash
#!/usr/bin/env bash
# coverage.sh TREE_ROOT MANIFEST
# Exit 0 iff MANIFEST covers exactly the file set of TREE_ROOT (excluding .git plumbing).
# Manifest format: sha256<TAB>bytes<TAB>path (paths relative to repo root).
set -euo pipefail
root=$1; manifest=$2
diff <(find "$root" -type f -not -path "*/.git/*" | sort) \
     <(cut -f3 "$manifest" | sort)
echo "COVERAGE EXACT: $root == $manifest ($(wc -l < "$manifest" | tr -d ' ') files)"
```

Save as `ledger/W1/checks/coverage.sh`, `chmod +x`.

- [ ] **Step 2: Run the check — verify it FAILS (red)**

Run: `ledger/W1/checks/coverage.sh forge/base_templates ledger/W1/manifests/base_templates.manifest`
Expected: FAIL (manifest does not exist yet).

- [ ] **Step 3: Generate the complete inventory and partition (inventory-driven, never eyeballed)**

One partitioner subagent:
```bash
find forge/base_templates -type f -not -path "*/.git/*" | sort \
  > .superpowers/sdd/2026-08-07-w1-completion/t1-inventory.txt
# slice into contiguous slices of at most 40 files:
split -l 40 -d -a 3 .superpowers/sdd/2026-08-07-w1-completion/t1-inventory.txt \
  .superpowers/sdd/2026-08-07-w1-completion/t1-slice-
```
The partitioner returns the slice list (path + file count + total bytes per slice). Every
file in the inventory belongs to exactly one slice — no file is unassigned.

- [ ] **Step 4: Map every slice (one mapper subagent per slice, parallel)**

Each mapper: doctrine reads first (Global Constraint 1); then for EVERY file in its slice,
in order: (a) read the file IN FULL (sequential windows to EOF if oversized; binary files
— e.g. `templates/erl_crash.dump`, 2.8MB BEAM crash dump — get a full structural pass in
windows plus digest; never skipped); (b) append a manifest line
`sha256<TAB>bytes<TAB>path` to its fragment manifest; (c) write a per-file map entry to
its fragment file `.superpowers/sdd/2026-08-07-w1-completion/t1-frag-<slice>.md`
containing: path · bytes · sha256 · format · role/content account (for `.j2` templates:
every macro name and signature enumerated; for registries: what the registry binds; for
`_dispatch`: the type→macro seams verbatim; for `_urn`/`_canon`: the stamp and Dewey law
verbatim) · verbatim quotes for load-bearing claims · final-line quote (Global
Constraint 4) · cross-references to the AOB spec blocks of `ledger/W1/base_agents.md`
where the template names them (cite, never invent) · PROVISIONAL gap notes only where
genuinely unresolvable.

- [ ] **Step 5: Synthesize the map**

One synthesizer subagent: concatenates fragment manifests into
`ledger/W1/manifests/base_templates.manifest`; merges fragment maps into
`ledger/W1/base_templates.md` organized as: (1) corpus identity (repo, pinned SHA, size,
file count); (2) the taxonomy tree as found (full directory account — every one of the
directories and every root-level file, from the inventory, not from `ls`); (3) the macro
grammar (universal macros enumerated with signatures; `_registries` / `_dispatch` /
`_urn` / `_canon` / `semantic_render_target` accounts with verbatim seams); (4)
per-directory deep accounts merged from fragments; (5) cross-corpus references to the AOB
shape; (6) the honest-gap register (every PROVISIONAL with its documented gap); (7) the
coverage statement. Nothing in the map may contradict a fragment; conflicts are resolved
by re-reading the source file, and the resolution is recorded.

- [ ] **Step 6: Run the acceptance check — verify it PASSES (green)**

Run: `ledger/W1/checks/coverage.sh forge/base_templates ledger/W1/manifests/base_templates.manifest`
Expected: `COVERAGE EXACT` with the true file count.

- [ ] **Step 7: Task review (spec + quality), then controller commits**

Task reviewer (fresh subagent) receives the task brief, the synthesizer's report, and the
artifact paths; verdicts spec-compliance AND quality; spot-checks at least 5 fragment
entries against the source files on disk (do the quotes exist? is the final-line quote
real?). On clean review, the CONTROLLER commits `ledger/W1/base_templates.md`,
`ledger/W1/manifests/base_templates.manifest`, `ledger/W1/checks/coverage.sh`.

### Task 2: Full-capture map of the forge/base turtle tower

**Files:**
- Create: `ledger/W1/base_foundations.md` (the map)
- Create: `ledger/W1/manifests/base_tower.manifest` (same tab-separated format)
- Workspace scratch: `.superpowers/sdd/2026-08-07-w1-completion/t2-*`

**Interfaces:**
- Consumes: the ENTIRE `forge/base` tree including its nested submodule tower, cloned by
  the controller before dispatch: level-2 `external`(base_external @90af0bad),
  `forge/agents`(base_agents @672ba868 — embryonic, 4 files), `forge/bin`(base_bin
  @6525c556), `forge/core`(core @3f90564c), `forge/docs`(base_docs @1cf127f6),
  `forge/specs`(base_aobs @469bb24f), `forge/templates`(base_templates @2d84826c); plus
  level-3 under `forge/agents`: `core`, `bin`, `docs`(base_agents_docs). PDFs are read
  via the Read tool's `pages` parameter, every page; `.tex` sources read in full.
- Produces: `ledger/W1/base_foundations.md` — consumed by Task 3, Task 4, and W2 design
  (this is the category-theory foundation corpus: sheaf/semiring/lens skills, IV-turtles,
  V-polysemy). `ledger/W1/manifests/base_tower.manifest`.

- [ ] **Step 1: Run the acceptance check — verify it FAILS (red)**

Run: `ledger/W1/checks/coverage.sh forge/base ledger/W1/manifests/base_tower.manifest`
Expected: FAIL (manifest does not exist yet).

- [ ] **Step 2: Generate the complete tower inventory**

Partitioner subagent: `find forge/base -type f -not -path "*/.git/*" | sort` →
`t2-inventory.txt`; slice at most 40 files per slice (the tower is small — expect few
slices; PDFs get their own slice so the page-by-page reads have room).

- [ ] **Step 3: Map every slice (parallel mappers, same per-file protocol as Task 1 Step 4)**

Additional required content for this corpus: (a) the submodule graph AS FOUND — every
`.gitmodules` quoted verbatim, every pin recorded, and the version-skew facts stated
plainly (base pins `agents` @672ba868 and `templates` @2d84826c while silmaril's sibling
clones sit @d2b1217f and @eb3d916b — two co-existing versions of the same taxonomies;
record, do not editorialize); (b) for each foundations paper (I-fundamenta, II-en,
IV-turtles, V-polysemy): the full chapter/theorem account from the `.tex` source with the
PDF checked page-by-page for content the source alone does not carry; (c) for each
`skills/*/*.md` (compose/lift/parallel/kleisli/sheaf/generate/equilibrium/coalgebra/lens/
semiring): the full skill account — signature, law, examples, verbatim statements of the
laws; (d) `AGENT.md` in full.

- [ ] **Step 4: Synthesize `ledger/W1/base_foundations.md`**

Same synthesis discipline as Task 1 Step 5, with the tower graph (nesting levels, pins,
skew, URL-cycle cross-references) as its own top-level section.

- [ ] **Step 5: Run the acceptance check — verify it PASSES (green)**

Run: `ledger/W1/checks/coverage.sh forge/base ledger/W1/manifests/base_tower.manifest`
Expected: `COVERAGE EXACT`.

- [ ] **Step 6: Task review, then controller commits**

Same review protocol as Task 1 Step 7. On clean review the controller commits
`ledger/W1/base_foundations.md`, `ledger/W1/manifests/base_tower.manifest`.

### Task 3: Taxonomy census — every distinct taxonomy, whole trees

**Files:**
- Create: `ledger/W1/taxonomy_census.md`
- Create: `ledger/W1/trees/silmaril.tree`, `ledger/W1/trees/basicttl.tree`,
  `ledger/W1/trees/base_agents.tree`, `ledger/W1/trees/base_templates.tree`,
  `ledger/W1/trees/base_tower.tree`, `ledger/W1/trees/example_gippidy_01.tree`,
  `ledger/W1/trees/superpowers.tree` — each the COMPLETE `find -type f` output
  (sorted, `.git` plumbing excluded, no other exclusion, no depth caps). Maintainer
  verbatim: *"FILE TREES ARE OUR TAXONOMY"* — the trees are committed artifacts.
- Workspace scratch: `.superpowers/sdd/2026-08-07-w1-completion/t3-*`

**Interfaces:**
- Consumes: all five committed W1 maps (`sparky_substrate.md`, `corpus_v17.md`,
  `base_agents.md`, `base_templates.md`, `base_foundations.md`), the two manifests, and
  the seven tree files it generates.
- Produces: `ledger/W1/taxonomy_census.md` — the definitive enumeration of every distinct
  taxonomy in play, consumed by Task 4, by the W1→W2 adversarial panel, and by the W2
  brainstorming gate. `ledger/W1/trees/*` — consumed by Task 4 as the row universe.

- [ ] **Step 1: Write the acceptance check for the census**

```bash
#!/usr/bin/env bash
# census-check.sh — exit 0 iff every committed tree file is non-empty and every tree
# root named in the census exists, and every required census section is present.
set -euo pipefail
for t in silmaril basicttl base_agents base_templates base_tower example_gippidy_01 superpowers; do
  test -s "ledger/W1/trees/$t.tree" || { echo "MISSING TREE: $t"; exit 1; }
done
for section in "## Census rows" "## Axes" "## Projection families" "## Version-skew register" "## Honest-gap register"; do
  grep -qF "$section" ledger/W1/taxonomy_census.md || { echo "MISSING SECTION: $section"; exit 1; }
done
echo "CENSUS CHECK PASSED"
```

Save as `ledger/W1/checks/census-check.sh`, `chmod +x`; run; expected: FAIL (red).

- [ ] **Step 2: Generate the seven whole trees**

One tree subagent, seven `find ... -type f -not -path "*/.git/*" | sort` captures, one
per root: repo root (`.` excluding `basicttl/`, `forge/`, and `external/`, each of which
owns its own tree — exclusion here is partition, not truncation: every file appears in
exactly one tree, and Task 4's checks verify the union),
`basicttl/`, `forge/base_agents/`, `forge/base_templates/`, `forge/base/` (the whole
tower), `forge/example_gippidy_01/`, `external/skills/superpowers/`. Line counts recorded
in the subagent's report; no cap on any of them.

- [ ] **Step 3: Author the census**

One census subagent (doctrine reads first; reads all five maps IN FULL; reads all seven
trees IN FULL — trees are line-per-path files and are read to their last line). Required
sections, exactly these headings: `## Census rows` — one row per distinct taxonomy
(minimum: the silmaril repo file-tree itself; basicttl's internal ontology taxonomy; the
five corpus taxonomies; the superpowers skill taxonomy; the AOB `.aob.dir` taxonomy
inside base_agents golden; the `_specspec` W3C taxonomy; the corpus SHACL CorpusAtom
taxonomy; the v17 gippidy projection-family taxonomy; the base tower submodule-graph
taxonomy) with: root · what-it-is (one honest sentence) · ordered axes as evidenced ·
cardinality (file/atom counts from trees/manifests, exact) · source map citation.
`## Axes` — the axis systems found, with verbatim evidence per axis claim. `## Projection
families` — every materialization family found across the maps (the 11-target family,
the v17 family, the template render targets), each with its source citation.
`## Version-skew register` — every same-repo-different-pin fact (base tower vs siblings),
exact SHAs. `## Honest-gap register` — every PROVISIONAL carried forward from the five
maps plus any census-level unknowns, each with its documented gap and what would resolve
it. No census row may lack a source citation; no axis may be asserted without quoted
evidence — Global Constraint 9 applies (capture, don't conclude).

- [ ] **Step 4: Run the acceptance check — verify it PASSES (green)**

Run: `ledger/W1/checks/census-check.sh`
Expected: `CENSUS CHECK PASSED`.

- [ ] **Step 5: Task review, then controller commits**

Reviewer spot-checks: at least 3 census rows against their cited maps; at least 2
cardinalities against tree line counts (`wc -l` on the tree file must equal the census
figure). On clean review the controller commits the census, the checks, and all seven
trees.

### Task 4: Complete-Component-Account seed

**Files:**
- Create: `ledger/W1/component_account.md` (the account: method, family rulings, exception rows, statistics)
- Create: `ledger/W1/account/silmaril.csv`, `ledger/W1/account/forge.csv` (row universe = the tree files; columns: `path,component_family,disposition,successor_hint,inverse_evidence,provisional_gap`)
- Workspace scratch: `.superpowers/sdd/2026-08-07-w1-completion/t4-*`

**Interfaces:**
- Consumes: the seven trees (row universe), the census, the five maps, the two manifests,
  and the beacon files (JUNGLE_MAP.md, PLAN_FREEZE.md, STRICTNESS_RULES.md) for
  already-ruled dispositions (e.g. W3's ruling that committed generated artifacts are
  retired-with-inverse — cite the ruling, don't re-decide it).
- Produces: the seed account — consumed by W5 (reconciliation), W3 (retire-with-inverse
  evidence), and the panel. **Seed** means: every physical entry HAS a row now; family-
  uniform dispositions are ruled at family granularity with per-family justification in
  `component_account.md`; entries whose disposition genuinely cannot be decided before
  W2's design carry `disposition=provisional` WITH a stated gap — and per Global
  Constraint 3 that is reserved for the genuinely undecidable, never the tedious.

- [ ] **Step 1: Write the acceptance check**

```bash
#!/usr/bin/env bash
# account-check.sh — exit 0 iff every tree path has exactly one account row and every
# row's disposition is from the closed vocabulary.
set -euo pipefail
cat ledger/W1/trees/silmaril.tree ledger/W1/trees/basicttl.tree | sort > /tmp/w1ac-repo.paths
cat ledger/W1/trees/base_agents.tree ledger/W1/trees/base_templates.tree \
    ledger/W1/trees/base_tower.tree ledger/W1/trees/example_gippidy_01.tree \
    ledger/W1/trees/superpowers.tree | sort > /tmp/w1ac-forge.paths
tail -n +2 ledger/W1/account/silmaril.csv | cut -d, -f1 | sort | diff - /tmp/w1ac-repo.paths
tail -n +2 ledger/W1/account/forge.csv   | cut -d, -f1 | sort | diff - /tmp/w1ac-forge.paths
bad=$(tail -q -n +2 ledger/W1/account/*.csv | cut -d, -f3 | sort -u \
  | grep -vxE "reuse|migrate|split|merge|retire|conflict|provisional" || true)
test -z "$bad" || { echo "BAD DISPOSITIONS: $bad"; exit 1; }
echo "ACCOUNT CHECK PASSED: $(tail -q -n +2 ledger/W1/account/*.csv | wc -l | tr -d ' ') rows"
```

(`tail -n +2` here skips each CSV's header row — a format necessity, not an output cap.)
Save as `ledger/W1/checks/account-check.sh`, `chmod +x`; run; expected: FAIL (red).

- [ ] **Step 2: Build the account**

One account subagent (doctrine reads first; census and maps read IN FULL): derive
`component_family` per path from the census's taxonomy rows; rule dispositions per family
with justification quoting the governing source (map finding, beacon ruling, or doctrine);
enumerate every exception row individually in `component_account.md`; generate the CSVs
programmatically from the trees so no path can be dropped; fill `inverse_evidence` for
every `retire` (what byte-complete inverse exists or must exist — per Praeriehund, no
delete without inverse); fill `provisional_gap` for every `provisional`.

- [ ] **Step 3: Run the acceptance check — verify it PASSES (green)**

Run: `ledger/W1/checks/account-check.sh`
Expected: `ACCOUNT CHECK PASSED` with the true row count.

- [ ] **Step 4: Task review, then controller commits**

Reviewer spot-checks at least 5 family rulings against their cited sources and at least 5
individual rows against the files on disk. On clean review the controller commits the
account files and check.

### Task 5: W1 verification and closure (controller-run)

**Files:**
- Create: `ledger/W1/W1_VERIFICATION.md`

**Interfaces:**
- Consumes: everything W1 produced (five maps, manifests, trees, census, account, checks).
- Produces: the verification record — the artifact the adversarial panel attacks and the
  W2 gate consumes.

- [ ] **Step 1: Run ALL acceptance checks fresh** (coverage ×2, census-check,
  account-check) and capture full output. Per verification-before-completion: no claim
  without fresh evidence in this session.
- [ ] **Step 2: Phase audit** — walk W1's ten phases ①–⑩ from the approved plan; for each,
  name the artifact + commit that satisfies it, or state plainly that it is not satisfied
  and why. No "should"; artifacts and commits only.
- [ ] **Step 3: Write `ledger/W1/W1_VERIFICATION.md`** with the check outputs verbatim and
  the phase audit table. Controller commits.
- [ ] **Step 4: Adversarial triple panel (between-workflow, per ruling Q3).** The
  controller directly dispatches THREE adversarial subagents, each briefed to break W1
  (completeness attack: sample the manifests/trees against disk; honesty attack: hunt
  fabricated quotes, unread files, lazy PROVISIONALs; doctrine attack: hunt truncation
  and interpretive-gate violations). Each adversary spawns its own more-agreeable /
  ontology-grounded sub-subagents where its harness allows and says so where it does not.
  Findings return to the controller; real defects get fix-dispatch + re-review; verdicts
  and rulings are appended to `ledger/W1/W1_VERIFICATION.md` and committed.
- [ ] **Step 5: Push** `git push -u origin claude/custom-pgp-sign-git-thh37n` (retry ×4,
  backoff 2/4/8/16s on network failure). Then present the maintainer go/no-go for W1→W2
  together with the opening brainstorming question for W2's design gate. W2 remains
  frozen until the maintainer answers.
