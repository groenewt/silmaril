#!/usr/bin/env bash
# tree-disk-check.sh — bind the two manifest-LESS, self-repo trees to LIVE disk.
#
# coverage.sh binds base_templates + base to their sha256 manifests; the other
# five trees have no manifest. This gate closes panel finding P.2 (silmaril.tree
# was stale by 111 files while all four green checks stayed green) by diffing
# silmaril.tree and basicttl.tree against a fresh files+symlinks find under the
# SAME documented exclusions used to generate them. ANY drift fails — both
# on-disk-not-in-tree (additions) AND in-tree-not-on-disk (deletions).
#
# Documented exclusions (Praeriehund: NAME every boundary, never fold it):
#   silmaril : root '.', files+symlinks, exclude .git basicttl forge external
#              .superpowers. .superpowers is gitignored SDD control-plane
#              scaffolding, ruled OUT-but-NAMED per W1_VERIFICATION.md P.4 fix (1).
#   basicttl : root 'basicttl', files+symlinks, exclude .git.
#   (The five forge/external roots run below as a bonus coverage line: files+
#    symlinks, exclude .git — they are already disk-bound via manifest or scope.)
#
# NO self-exclusion. Every regular file and symlink under silmaril scope — the
# audit apparatus included (symlinks.tsv, GENERATOR.sh, this gate itself, the
# maps, the account) — is real committed corpus and MUST appear in silmaril.tree.
# silmaril.tree is REGENERATED as the final pre-commit step (never frozen early),
# so it always carries these files; this gate then binds it to disk with no
# exclusion, which is exactly what makes a future stale-tree drift impossible to
# commit green. (An earlier revision pruned symlinks.tsv and this file to mask a
# recurrence — that fold is removed; the recurrence is fixed at the source by
# regenerating the tree last.)
set -euo pipefail

work=$(mktemp -d); trap 'rm -rf "$work"' EXIT
status=0

emit() {  # NAME  TREE  LISTFILE
  local name=$1 tree=$2 list=$3 d
  d=$(diff <(sort "$list") <(sort "$tree")) || true
  if [ -n "$d" ]; then
    printf 'DRIFT %s (< on-disk-not-in-tree | > in-tree-not-on-disk):\n%s\n' "$name" "$d"
    status=1
  else
    printf 'OK  %-18s %6s entries  (tree == disk)\n' "$name" "$(wc -l < "$tree" | tr -d ' ')"
  fi
}

# ---- silmaril : whole repo minus documented exclusions + named control-plane --
find . -path ./.git         -prune -o \
       -path ./basicttl     -prune -o \
       -path ./forge        -prune -o \
       -path ./external     -prune -o \
       -path ./.superpowers -prune -o \
       \( -type f -o -type l \) -print > "$work/silmaril.list"
emit silmaril ledger/W1/trees/silmaril.tree "$work/silmaril.list"

# ---- basicttl : submodule-free, symlink-inclusive -----------------------------
find basicttl -path '*/.git/*' -prune -o \( -type f -o -type l \) -print > "$work/basicttl.list"
emit basicttl ledger/W1/trees/basicttl.tree "$work/basicttl.list"

# ---- BONUS: the other five trees' roots (already disk-bound elsewhere) ---------
echo "--- bonus coverage: other five trees (files+symlinks, exclude .git) ---"
bonus() {  # NAME  ROOT
  find "$2" -path '*/.git/*' -prune -o \( -type f -o -type l \) -print > "$work/$1.list"
  emit "$1" "ledger/W1/trees/$1.tree" "$work/$1.list"
}
bonus base_agents        forge/base_agents
bonus base_templates     forge/base_templates
bonus base_tower         forge/base
bonus example_gippidy_01 forge/example_gippidy_01
bonus superpowers        external/skills/superpowers

exit $status
