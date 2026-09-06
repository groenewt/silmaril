#!/usr/bin/env bash
# census-check.sh — exit 0 iff every committed tree file is non-empty and every required
# census section is present. Trees are the whole-taxonomy artifacts; the census cites them.
set -euo pipefail
for t in silmaril basicttl base_agents base_templates base_tower example_gippidy_01 superpowers; do
  test -s "ledger/W1/trees/$t.tree" || { echo "MISSING/EMPTY TREE: $t"; exit 1; }
done
for section in "## Census rows" "## Axes" "## Projection families" "## Version-skew register" "## Honest-gap register"; do
  grep -qF "$section" ledger/W1/taxonomy_census.md || { echo "MISSING SECTION: $section"; exit 1; }
done
echo "CENSUS CHECK PASSED ($(cat ledger/W1/trees/*.tree | wc -l | tr -d ' ') files across 7 trees)"
