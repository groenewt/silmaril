#!/usr/bin/env bash
# Active CI/CD validation — the green/red matrix.
#
# Proves every surface ACTUALLY enforces: local commit (pre-commit), local
# push (pre-push), fake-remote push (server update hook), and the
# topographic-assessment gate. Red paths run in a disposable worktree on
# throwaway branches; the real working tree is never touched. Every step
# asserts its expected exit code, and every red push asserts the remote ref
# did NOT move.
#
#   scripts/validate-cicd.sh
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT=$(pwd)
REMOTE=$(git remote get-url origin)

declare -a RESULTS=()
npass=0; nfail=0

check() { # check <surface/name> <expected-exit> <actual-exit>
  if [ "$2" = "$3" ]; then
    RESULTS+=("PASS  $1")
    npass=$((npass + 1))
  else
    RESULTS+=("FAIL  $1 (expected exit $2, got $3)")
    nfail=$((nfail + 1))
  fi
}

ref_sha() { git ls-remote "$REMOTE" "refs/heads/$1" | cut -f1; }

check_ref_unmoved() { # check_ref_unmoved <name> <branch> <sha-before>
  local now
  now=$(ref_sha "$2")
  if [ "$now" = "$3" ]; then
    RESULTS+=("PASS  $1 [ref $2 unmoved]")
    npass=$((npass + 1))
  else
    RESULTS+=("FAIL  $1 [ref $2 MOVED: $3 -> $now]")
    nfail=$((nfail + 1))
  fi
}

WT=$(mktemp -d "${TMPDIR:-/tmp}/sparky-cicd.XXXXXX")/wt
cleanup() {
  cd "$ROOT"
  git worktree remove --force "$WT" >/dev/null 2>&1 || true
  git branch -D ci-red ci-red-topo ci-red-joern >/dev/null 2>&1 || true
  git push --no-verify origin :ci-heartbeat >/dev/null 2>&1 || true
}
trap cleanup EXIT

echo "=== GREEN: test -> dev -> main promotion ==="

git worktree add "$WT" test >/dev/null 2>&1 || { echo "cannot add worktree"; exit 1; }
(
  cd "$WT"
  mkdir -p docs
  echo "ci heartbeat $(git rev-parse --short HEAD)" > docs/ci-heartbeat.md
  git add docs/ci-heartbeat.md
  git commit -q -m "docs: ci heartbeat (green-path proof)"
); check "green: pre-commit on test branch" 0 $?

( cd "$WT" && git push origin test ); check "green: push test (client+server test tier)" 0 $?

( cd "$WT" && git switch -q dev && git merge -q --no-edit test && git push origin dev )
check "green: promote dev (client+server dev tier)" 0 $?

( cd "$WT" && git switch -q main && git merge -q --no-edit dev && git push origin main )
check "green: promote main (client+server main tier + determinism)" 0 $?

echo "=== RED: enforcement on every surface ==="

TEST_SHA=$(ref_sha test)
DEV_SHA=$(ref_sha dev)

# R1 — magic literal caught by pre-commit
(
  cd "$WT" && git switch -q -c ci-red test
  mkdir -p modules/core/src/main/scala/highway/core
  printf 'package highway.core\nobject RedTest:\n  val ttlSeconds = 86400\n' \
    > modules/core/src/main/scala/highway/core/RedTest.scala
  git add modules/core/src/main/scala/highway/core/RedTest.scala
  git commit -q -m "red: magic literal"
); rc=$?; [ $rc -ne 0 ]; check "red: pre-commit rejects magic literal" 0 $?

# R2 — committed violation caught by pre-push (dev tier runs the magic gate)
(
  cd "$WT" && git commit -q --no-verify -m "red: magic literal (hook bypassed)" \
    && git push origin ci-red:dev
) >/dev/null 2>&1; rc=$?; [ $rc -ne 0 ]; check "red: pre-push rejects push to dev" 0 $?
check_ref_unmoved "red: pre-push rejection" dev "$DEV_SHA"

# R3 — client hooks bypassed entirely: the fake remote is the backstop
( cd "$WT" && git push --no-verify origin ci-red:test ) >/dev/null 2>&1
rc=$?; [ $rc -ne 0 ]; check "red: server update hook rejects --no-verify push" 0 $?
check_ref_unmoved "red: server rejection" test "$TEST_SHA"

# R4 — topography drift: mutate the typed fixture corpus without re-recording
(
  cd "$WT" && git switch -q -c ci-red-topo test
  f=modules/config/src/main/scala/highway/config/constants/fixtures/Source.scala
  # append a second class to the fixture body: census changes, baseline doesn't
  perl -0pi -e 's/\|\}\n(\s+\|\/\/ TODO tidy this up)/|}\n      |class Gadget { def spin(): Int = { return 1 } }\n$1/' "$f"
  git add "$f"
  git commit -q --no-verify -m "red: fixture topography mutated, baseline not re-recorded"
  git push --no-verify origin ci-red-topo:dev
) >/dev/null 2>&1; rc=$?; [ $rc -ne 0 ]
check "red: assess census drift rejects topography change" 0 $?
check_ref_unmoved "red: topography rejection" dev "$DEV_SHA"

# R5 — executable joern reference caught server-side
(
  cd "$WT" && git switch -q -c ci-red-joern test
  printf '#!/bin/sh\nexec joern-parse "$@"\n' > scripts/red-bridge.sh
  git add scripts/red-bridge.sh
  git commit -q --no-verify -m "red: joern bridge"
  git push --no-verify origin ci-red-joern:test
) >/dev/null 2>&1; rc=$?; [ $rc -ne 0 ]
check "red: CPG boundary rejects direct bridge script" 0 $?
check_ref_unmoved "red: CPG boundary rejection" test "$TEST_SHA"

# R6 — branch lifecycle: creation gated, deletion allowed (zero-sha guard)
( cd "$WT" && git switch -q test && git push origin test:ci-heartbeat ) >/dev/null 2>&1
check "green: topic-branch creation passes test tier" 0 $?
( cd "$WT" && git push origin :ci-heartbeat ) >/dev/null 2>&1
check "green: branch deletion passes (zero-sha guard)" 0 $?

# R7 — installed-binary surface (only when the dist + contract cmd exist)
if [ -x dist/sparky/bin/sparky ]; then
  SCRATCH=$(mktemp -d "${TMPDIR:-/tmp}/sparky-target.XXXXXX")
  (
    cd "$SCRATCH" && git init -q
    "$ROOT/dist/sparky/bin/sparky" contract install --repo . \
      --contract "$ROOT/contracts/git-contract.yaml" >/dev/null
    printf 'object T:\n  val ttl = 86400\n' > T.scala
    mkdir -p modules/x/src/main/scala && mv T.scala modules/x/src/main/scala/
    git add -A && git commit -q -m "red: magic literal in target repo"
  ) >/dev/null 2>&1; rc=$?; [ $rc -ne 0 ]
  check "red: installed binary enforces in target repo" 0 $?
  rm -rf "$SCRATCH"
else
  RESULTS+=("SKIP  installed-binary surface (no dist/sparky/bin/sparky)")
fi

echo
echo "=== SURFACE x {green,red} matrix ==="
printf '%s\n' "${RESULTS[@]}"
echo "----------------------------------------"
echo "PASS $npass  FAIL $nfail"
[ $nfail -eq 0 ]
