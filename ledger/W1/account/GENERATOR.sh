#!/usr/bin/env bash
# GENERATOR.sh — W1 Task 4 Complete-Component-Account SEED generator.
#
# Emits ledger/W1/account/silmaril.csv and forge.csv PROGRAMMATICALLY from the
# seven frozen trees so NO path is dropped and every path appears exactly once
# (the account-check diffs CSV column 1 against the sorted tree paths).
#
# Row universe split (matches ledger/W1/checks/account-check.sh):
#   silmaril.csv  <-  trees/silmaril.tree + trees/basicttl.tree
#   forge.csv     <-  trees/base_agents.tree + trees/base_templates.tree
#                     + trees/base_tower.tree + trees/example_gippidy_01.tree
#                     + trees/superpowers.tree
#
# Columns EXACTLY:
#   path,component_family,disposition,successor_hint,inverse_evidence,provisional_gap
#
# disposition vocabulary is CLOSED: reuse|migrate|split|merge|retire|conflict|provisional
# (Complete Component Account, docs/unary-byte-frame-law.md).
#
# CSV safety: tree paths contain NO commas (verified) and this generator emits
# NO comma inside any field (';' '/' '+' '-' used instead). The path column is
# the verbatim tree line so the check's `cut -d, -f1 | diff` matches exactly.
#
# Every disposition is RULED from a governing source. The rulings are quoted and
# justified per-family in ledger/W1/component_account.md. This script is the
# machine projection of those rulings onto the frozen row universe.

set -euo pipefail

TREES="$(cd "$(dirname "$0")/../trees" && pwd)"
OUT="$(cd "$(dirname "$0")" && pwd)"
HEADER='path,component_family,disposition,successor_hint,inverse_evidence,provisional_gap'

# ----------------------------------------------------------------------------
# The classifier. One awk program keyed on the verbatim path prefix classifies
# every line of every tree. Ordered first-match-wins within each tree family.
# Emits: path,family,disposition,successor_hint,inverse_evidence,provisional_gap
# ----------------------------------------------------------------------------
read -r -d '' CLASSIFY <<'AWK' || true
function pre(s){ return index(p,s)==1 }        # true iff p starts with s
function emit(fam,disp,succ,inv,gap){ print p "," fam "," disp "," succ "," inv "," gap; done_=1 }
BEGIN {
  # Load the 38 tracked mode-120000 symlinks into SL[path]=target (both passes).
  # getline-into-variable does not field-split, and paths/targets are comma-free
  # (verified), so the '\t' split is exact and CSV integrity is preserved.
  while ((getline __sl < SLFILE) > 0) {
    __t = index(__sl, "\t")
    if (__t > 0) SL[substr(__sl, 1, __t-1)] = substr(__sl, __t+1)
  }
  close(SLFILE)
}
{
  p=$0; done_=0

  # ======================= SYMLINK DECLARATIONS (FIRST RULE) ================
  # Every physical mode-120000 symlink emits its own row BEFORE any file-family
  # match, so a tracked link can never fold silently into a file family. The
  # row carries the real link target as inverse evidence. 37 links live under
  # forge/base_agents, 1 under external/skills/superpowers (=38 total).
  if (p in SL) {
    slroot="external/superpowers/symlink-declaration"
    if (pre("forge/base_agents/")) slroot="forge/base_agents/symlink-declaration"
    emit(slroot,"reuse","resolve to link target on consolidation", \
         "git-tracked mode-120000 symlink -> " SL[p],""); next }

  # ======================= SILMARIL TREE (paths start with ./) ==============
  if (pre("./")) {

    # --- Reserved-keyword `lambda` twins (LIVE package) -> MIGRATE ----------
    # RESOLVED (was provisional): the reserved-keyword `lambda` package is live-
    # wired into the engine by importlib -- 37 call-sites in scripts/python/pylib/
    # src (excl reference/) resolve 5 distinct entrypoint modules of the three twin
    # roots (12 direct IMPORTLIB.import_module(...) + 25 via the _value wrapper
    # whose body is IMPORTLIB.import_module(module_name).VALUE); every referenced
    # entrypoint exists on disk. So the prior "orphaned/unresolved" gap is DODGE-
    # DISSOLVED at the package level. Disposition is MIGRATE (not reuse): the
    # Python-invalid `lambda` spelling folds onto the lawful `lambda_` sibling
    # under the unary refactor (X) -- a transformation, matching successor_hint.
    # Per-row evidence is stated at PACKAGE granularity (each row is a member of
    # the live-wired package), NOT as if every row were itself a call-site.
    if (pre("./scripts/python/pylib/src/silmaril/sparky/lambda/") \
     || pre("./scripts/python/pylib/src/config/constants/lambda/") \
     || pre("./scripts/python/pylib/src/config/gate/external/python/lambda/")) {
      emit("silmaril/engine/sparky-reserved-keyword-lambda-twin","migrate","fold onto the lawful lambda_ sibling under the unary refactor (X)", \
           "member of the reserved-keyword lambda package that is live-wired into the engine via 37 importlib call-sites resolving 5 entrypoint modules in scripts/python/pylib/src excl reference (e.g. .../frame/library.py import_module silmaril.sparky.lambda...); transforms to the lambda_ sibling under X",""); next }

    # --- Legacy reference/ copy: aob/layout hyphenated constants -> PROVISIONAL
    if (pre("./scripts/python/pylib/reference/pylib/reference/config/constants/aob/layout/")) {
      emit("silmaril/engine/legacy-reference-aob-layout","provisional","","", \
           "aob/layout hyphenated projection constants (daedalus/icarus/ossie/yggdrasil): meaning unresolved; no live analogue found (sparky_substrate.md 2.4/5.5); Praeriehund name-the-gap"); next }

    # --- Legacy reference/ copy (orphaned 719-file legacy engine) -> RETIRE ---
    if (pre("./scripts/python/pylib/reference/")) {
      emit("silmaril/engine/legacy-reference-copy","retire","live scripts/python/pylib/src (sparky+config) superset", \
           "byte-complete predecessor/successor account MUST be recorded before deletion (sparky_substrate.md 2.4 RETIRE candidate: blocked until inverse recorded; cannot delete on orphaned observation alone); consumer closure evidenced empty (2.3: zero import hits repo-wide excl reference itself); successor superset = live src/silmaril/sparky+config mirror",""); next }

    # --- Live sparky engine src/ (lambda_ lawful sibling + all live ops) REUSE
    if (pre("./scripts/python/pylib/src/")) {
      emit("silmaril/engine/sparky-live-src","reuse","","",""); next }

    # --- Live engine build envelopes + tests + pylib receipts -> REUSE --------
    if (pre("./scripts/python/pylib/make/") || pre("./scripts/python/pylib/tests/")) {
      emit("silmaril/engine/build-and-verification","reuse","","",""); next }
    if (pre("./scripts/python/pylib/")) {   # pylib root receipts (Makefile/*.md/*.json)
      emit("silmaril/engine/live-receipts-config","reuse","","",""); next }

    # --- Python OUTSIDE the registered pylib tree -> MIGRATE ------------------
    # unary-byte-frame-law law-clause 14: Python under scripts/python is not
    # executable until integrated in the registered scripts/python/pylib tree.
    if (pre("./scripts/python/morphism_contracts/") || pre("./scripts/python/sparky_lambda/")) {
      emit("silmaril/engine/outside-pylib-python","migrate","integrate into registered scripts/python/pylib tree (unary-byte-frame-law clause 14)","",""); next }

    # --- Lawful Sparky-era shell launchers -> REUSE --------------------------
    if (pre("./scripts/source/discipline/")) {
      emit("silmaril/shell/lawful-launcher","reuse","","",""); next }

    # --- Scala-CLI driver shells (RED, need unary refactor) -> MIGRATE -------
    if (pre("./scripts/scala/")) {
      emit("silmaril/shell/scala-cli-driver","migrate","unary source/discipline/gate/shell launcher form (sparky_substrate.md 3.4)","",""); next }

    # --- Named script violators (explicit rulings) --------------------------
    if (p=="./scripts/ui-constructor.py") {
      emit("silmaril/scripts/ui-constructor-violation","migrate","sparky/morphism/ontology/ui render ops + forge/base_templates HEEx (JUNGLE_MAP: THE VIOLATION must be replaced with GeoSPARQL-driven renderer)","",""); next }
    if (p=="./scripts/ontology-depth-check.py") {
      emit("silmaril/scripts/depth-check","migrate","sparky/morphism/ontology/validation/depth family (sparky_substrate.md 3.2; JUNGLE_MAP: plan makes it blocking)","",""); next }

    # --- All other top-level shell violators -> MIGRATE ---------------------
    if (pre("./scripts/") && p ~ /\.sh$/) {
      emit("silmaril/shell/top-level-violator","migrate","unary source/discipline/gate/shell launchers (sparky_substrate.md 3.3; STRICTNESS Rule 2)","",""); next }

    # --- docs/: doctrine (the binding law) -> REUSE -------------------------
    if (p=="./docs/praeriehund-demokratie-der-kategorien.md" || p=="./docs/unary-byte-frame-law.md") {
      emit("silmaril/docs/doctrine","reuse","","",""); next }
    # --- docs/: hand-authored working/plan notes -> REUSE -------------------
    if (p=="./docs/README.md" || p=="./docs/pr2-review-addendum.md" || p=="./docs/pr2-socratic-followup.md" || pre("./docs/superpowers/")) {
      emit("silmaril/docs/working-notes","reuse","","",""); next }
    # --- docs/: committed GENERATED site artifacts -> RETIRE ----------------
    if (p=="./docs/architecture.html" || p=="./docs/index.html" || p=="./docs/provenance.html" || p=="./docs/folklore.html" || p=="./docs/_includes/build-status.html" || p=="./docs/assets/css/generated.css") {
      inv="regenerated byte-identical by the GeoSPARQL/render pipeline from basicttl ontology (JUNGLE_MAP: generated.css/build-status.html are generated; CI site + ui-constructor jobs regenerate-and-compare); STRICTNESS Rule 10 removes-from-branch"
      succ="GeoSPARQL-driven site render (forge/base_templates HEEx)"
      gap=""
      if (p=="./docs/folklore.html") succ="GeoSPARQL fable render; fable content dissolved-and-absorbed per PLAN_FREEZE Ruling 3"
      emit("silmaril/site/generated-artifact","retire",succ,inv,gap); next }
    # --- docs/: hand-authored Jekyll SCAFFOLD (to be rebuilt) -> RETIRE ------
    if (pre("./docs/")) {
      emit("silmaril/site/jekyll-scaffold","retire","forge/base_templates HEEx site renderer (JUNGLE_MAP CI: site Will be rebuilt as GeoSPARQL-driven generation)", \
           "hand-authored Jekyll apparatus superseded by the GeoSPARQL/base_templates render mechanism (PLAN_FREEZE Ruling B zero hand-authored HTML; Workflow 3); bytes recoverable from git history until the successor renderer is proven",""); next }

    # --- ontology/ generated render targets -> RETIRE ----------------------
    if (p=="./ontology/README.md") {
      emit("silmaril/ontology-dir/readme","reuse","","",""); next }
    if (p=="./ontology/ui-shapes.ttl") {
      emit("silmaril/ontology-dir/orphaned-generated","retire","morphism/ontology consolidation render (ui-shapes step to be established)", \
           "under the ontology/ generated block (JUNGLE_MAP) but flagged ORPHANED nothing-consumes-it: consumer closure trivially empty; the render step producing ui-shapes.ttl is NOT yet evidenced and MUST exist before deletion (Praeriehund no-delete-without-inverse)",""); next }
    if (pre("./ontology/")) {   # consolidated.ttl manifest.ttl shapes.ttl queries.sparql geosparql.sparql
      emit("silmaril/ontology-dir/generated-artifact","retire","morphism/ontology/consolidation render outputs (consolidated/render; manifest/render; shapes/constraint; query/protocol; geographic/query)", \
           "regenerated byte-identical by morphism/ontology/consolidation from basicttl/*.ttl source; CI ontology job regenerate-and-compare committed consolidated TTL IS the byte-complete inverse check (JUNGLE_MAP; STRICTNESS Rule 10; PLAN_FREEZE Workflow 3.1)",""); next }

    # --- keys/: generated trust manifest -> RETIRE; PGP roots -> REUSE -------
    if (p=="./keys/trust-manifest.txt") {
      emit("silmaril/keys/generated-manifest","retire","morphism/provenance trust-manifest render", \
           "derived byte-identical from basicttl/commit_signing_trust.ttl by the provenance/trust pipeline (JUNGLE_MAP: trust manifest derived from commit_signing_trust.ttl; morphism/provenance/commit/keyring); CI provenance job regenerates-and-checks; STRICTNESS Rule 10 removes-from-branch",""); next }
    if (pre("./keys/")) {
      emit("silmaril/keys/pgp-trust-root","reuse","","",""); next }

    # --- hooks/: git-hook shells -> MIGRATE; readme -> REUSE ----------------
    if (p=="./hooks/README.md") { emit("silmaril/hooks/readme","reuse","","",""); next }
    if (pre("./hooks/")) {
      emit("silmaril/hooks/git-hook","migrate","unary-conformant shell launcher form (STRICTNESS Rule 2; unary-byte-frame-law Bash frontier)","",""); next }

    # --- .github/ CI workflows -> MIGRATE ----------------------------------
    if (pre("./.github/")) {
      emit("silmaril/ci/workflow","migrate","Workflow 4 multi-engine CI/CD (Jena/SIS/Sedona/rdflib) (PLAN_FREEZE Workflow 4; JUNGLE_MAP CI jobs Will-be-removed/Will-change)","",""); next }

    # --- ledger/ audit record (this account included) -> REUSE -------------
    if (pre("./ledger/")) {
      emit("silmaril/ledger/audit-record","reuse","","",""); next }

    # --- root repo config + governance handoff docs -> REUSE ---------------
    if (p=="./.gitignore" || p=="./.gitmodules") {
      emit("silmaril/root/repo-config","reuse","","",""); next }
    # remaining ./<FILE> root files (README/JUNGLE_MAP/PLAN_FREEZE/STRICTNESS/SUBAGENT_FINDINGS/TRANSCRIPT)
    emit("silmaril/root/governance-doc","reuse","","",""); next
  }

  # ======================= BASICTTL TREE ===================================
  if (pre("basicttl/")) {
    if (p=="basicttl/folklore_provenance_fable.ttl") {
      emit("basicttl/fable-dissolve","merge","retype into existing ConcreteAnchor/DecompositionStep classes + fable-as-query into query library (PLAN_FREEZE Ruling 3)", \
           "content preserved by dissolve-and-absorb: retyped into existing individuals + query-library entry (PLAN_FREEZE Ruling 3 FABLE DISSOLVE AND ABSORB)",""); next }
    emit("basicttl/ontology-source","reuse","","",""); next
  }

  # ======================= FORGE: base_agents ==============================
  if (pre("forge/base_agents/")) {
    if (pre("forge/base_agents/golden/") || pre("forge/base_agents/r1_staging/")) {
      emit("forge/base_agents/universal-base-generics","migrate","owned universal base ontology via bind/morph (PLAN_FREEZE Workflow 5.1; Ruling A; Workflow 1.2)","",""); next }
    if (pre("forge/base_agents/corpus/")) {
      emit("forge/base_agents/corpus-projection","reuse","","",""); next }
    emit("forge/base_agents/upstream-reference","reuse","","",""); next
  }

  # ======================= FORGE: base_templates ===========================
  if (pre("forge/base_templates/")) {
    emit("forge/base_templates/render-engine","reuse","","",""); next }

  # ======================= FORGE: base (structural tower) ==================
  if (pre("forge/base/")) {
    emit("forge/base/structural-tower-and-foundations","reuse","","",""); next }

  # ======================= FORGE: example_gippidy_01 =======================
  if (pre("forge/example_gippidy_01/")) {
    if (p ~ /\.zip$/) {
      emit("forge/example_gippidy_01/v17-corpus-transport","migrate","imported/consolidated into owned v1 ontology AOB buildout: v17 algebra + projection family + native runners (PLAN_FREEZE Ruling A; Workflow 5.2/5.3)","",""); next }
    emit("forge/example_gippidy_01/transport-wrapper","reuse","","",""); next }

  # ======================= external: superpowers ===========================
  if (pre("external/skills/superpowers/")) {
    emit("external/superpowers/planning-methodology","reuse","","",""); next }

  # ======================= UNCLASSIFIED (must never happen) ================
  emit("UNCLASSIFIED","conflict","","","UNCLASSIFIED PATH - generator rule gap"); next
}
AWK

# The 38 tracked mode-120000 symlinks (path<TAB>target). Loaded into the awk
# classifier so every physical symlink gets an explicit symlink-declaration row
# carrying its real link target as inverse evidence (BOTH csv passes).
SLFILE="$OUT/symlinks.tsv"

# ---- silmaril.csv : silmaril.tree + basicttl.tree --------------------------
{
  printf '%s\n' "$HEADER"
  awk -v SLFILE="$SLFILE" "$CLASSIFY" "$TREES/silmaril.tree" "$TREES/basicttl.tree"
} > "$OUT/silmaril.csv"

# ---- forge.csv : the five forge trees -------------------------------------
{
  printf '%s\n' "$HEADER"
  awk -v SLFILE="$SLFILE" "$CLASSIFY" \
    "$TREES/base_agents.tree" \
    "$TREES/base_templates.tree" \
    "$TREES/base_tower.tree" \
    "$TREES/example_gippidy_01.tree" \
    "$TREES/superpowers.tree"
} > "$OUT/forge.csv"

printf 'GENERATED %s rows -> silmaril.csv ; %s rows -> forge.csv\n' \
  "$(($(wc -l < "$OUT/silmaril.csv") - 1))" \
  "$(($(wc -l < "$OUT/forge.csv") - 1))"
