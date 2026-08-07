#!/usr/bin/env bash
# account-check.sh — exit 0 iff ALL of:
#   (a) every tree path has exactly one account row  (col1 path-set == the trees);
#   (b) every disposition (col3) is from the closed vocabulary
#         reuse|migrate|split|merge|retire|conflict|provisional;
#   (c) the Complete-Component-Account invariants hold on EVERY row. SCOPE NOTE:
#       this is a SYNTACTIC gate over the six CSV columns. It enforces the PRESENCE
#       (non-emptiness) and closed-vocabulary shape the doctrine demands; it does
#       NOT and CANNOT assert the SEMANTIC content those columns point at.
#         - structural: exactly 6 comma-free fields (the col5/col6 tests below are
#           only trustworthy while no field carries a comma; GENERATOR.sh emits none);
#         - retire (col3) REQUIRES a NON-EMPTY inverse_evidence (col5). The doctrine
#             reads "a retirement requires ... a byte-complete inverse"; this check
#             enforces only that an inverse IS NAMED (col5 != ""). Whether that named
#             inverse is actually BYTE-COMPLETE is a semantic W3 gate this syntactic
#             check CANNOT assert -- do not read a green here as a completeness proof;
#         - provisional (col3) REQUIRES a NON-EMPTY provisional_gap (col6)
#             "an unresolved meaning remains provisional" -> the gap must be NAMED
#             (col6 != ""); this check does not judge whether the gap is well-posed;
#         - component_family (col2) is NEVER UNCLASSIFIED;
#         - disposition (col3) is NEVER conflict
#           (the generator's UNCLASSIFIED/conflict fallthrough must never have fired).
# (a)+(b) are the original checks and are unchanged; (c) is added hardening.
set -euo pipefail
cat ledger/W1/trees/silmaril.tree ledger/W1/trees/basicttl.tree | sort > /tmp/w1ac-repo.paths
cat ledger/W1/trees/base_agents.tree ledger/W1/trees/base_templates.tree \
    ledger/W1/trees/base_tower.tree ledger/W1/trees/example_gippidy_01.tree \
    ledger/W1/trees/superpowers.tree | sort > /tmp/w1ac-forge.paths
tail -n +2 ledger/W1/account/silmaril.csv | cut -d, -f1 | sort | diff - /tmp/w1ac-repo.paths
tail -n +2 ledger/W1/account/forge.csv   | cut -d, -f1 | sort | diff - /tmp/w1ac-forge.paths

# (b) closed disposition vocabulary (col3).
bad=$(tail -q -n +2 ledger/W1/account/*.csv | cut -d, -f3 | sort -u \
  | grep -vxE "reuse|migrate|split|merge|retire|conflict|provisional" || true)
test -z "$bad" || { echo "BAD DISPOSITIONS: $bad"; exit 1; }

# (c) doctrine invariants (header stripped; fields comma-free by construction).
inv=$(tail -q -n +2 ledger/W1/account/*.csv | awk -F, '
  NF!=6                       { print "MALFORMED(NF="NF"): " $0;            next }
  $2=="UNCLASSIFIED"          { print "UNCLASSIFIED component_family: " $1        }
  $3=="conflict"              { print "conflict disposition: " $1                 }
  $3=="retire"      && $5=="" { print "retire without inverse_evidence: " $1      }
  $3=="provisional" && $6=="" { print "provisional without provisional_gap: " $1  }
')
test -z "$inv" || { echo "INVARIANT VIOLATIONS:"; echo "$inv"; exit 1; }

echo "ACCOUNT CHECK PASSED: $(tail -q -n +2 ledger/W1/account/*.csv | wc -l | tr -d ' ') rows"
