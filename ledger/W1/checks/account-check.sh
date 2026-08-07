#!/usr/bin/env bash
# account-check.sh — exit 0 iff every tree path has exactly one account row and every
# disposition is from the closed vocabulary.
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
