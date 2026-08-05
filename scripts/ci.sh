#!/usr/bin/env bash
# sparky tiered CI runner — the single spine behind the client hooks and
# the fake-remote update hook.
#
#   scripts/ci.sh [--server] <test|dev|main|parity>
#   scripts/ci.sh [--server] morph RECEIPT
#
# Tiers (escalating):
#   test   Test/compile + bounded changed-file hook gates
#          (--server: scoped validate — archive exports have no .git)
#   dev    + full test suite + scoped validate + exact fixture assessment
#   main   + full validate (incl. manifest envelopment) + bounded self-scan
#          assessment + determinism replay (scan twice, byte-diff topography)
#   morph  full tests + full validate + verification of an explicit morph
#          receipt through the production Lambda-backed CLI binding
#   parity manual-only: hadoop oracle census (never wired to a push)
#
# One batched sbt invocation per tier: sbt cold start dominates the budget,
# and sbt aborts the batch on the first failing command.
final_status=1

ci_finish() {
  command_status=$?
  if [ -n "${A:-}" ] && [ -d "$A" ]; then
    rm -rf -- "$A" || printf '%s\n' "CI WARN: failed to remove $A" >&2
  fi
  if [ -n "${B:-}" ] && [ -d "$B" ]; then
    rm -rf -- "$B" || printf '%s\n' "CI WARN: failed to remove $B" >&2
  fi
  if [ "$final_status" -ne 0 ]; then
    printf '%s\n' "CI FAIL[${TIER:-unresolved}]: accountable exit status=$command_status" >&2
  fi
  return "$command_status"
}

trap ci_finish EXIT

SERVER=0
if [ "${1:-}" = "--server" ]; then SERVER=1; shift; fi
TIER="${1:?usage: ci.sh [--server] <test|dev|main|morph|parity>}"
RECEIPT="${2:-}"
cd "$(dirname "$0")/.." || {
  printf '%s\n' "CI FAIL[$TIER]: repository root is unavailable" >&2
  exit 1
}

# hooks run with a stripped environment — re-resolve the pinned toolchain
if ! command -v sbt >/dev/null 2>&1; then
  # shellcheck disable=SC1091
  [ -s "$HOME/.sdkman/bin/sdkman-init.sh" ] && . "$HOME/.sdkman/bin/sdkman-init.sh" >/dev/null 2>&1 || true
fi
command -v sbt >/dev/null 2>&1 || { echo "CI FAIL[$TIER]: sbt not on PATH" >&2; exit 1; }

wire() { # wire <event> <msg> — optional telephone record, never a dependency
  command -v cheese_text >/dev/null 2>&1 && \
    cheese_text "$2" --scope sparky --event "ci_$1" --detail "tier=$TIER" \
      >/dev/null 2>&1 || true
}

fail() {
  echo "CI FAIL[$TIER]: $1" >&2
  wire fail "ci $TIER fail: $1"
  exit 1
}

SBT_CMDS=("Test/compile")
case "$TIER" in
  test)
    if [ "$SERVER" = 1 ]; then
      SBT_CMDS+=("cli/run validate --gates cpg-boundary,constants,magic")
    else
      SBT_CMDS+=("cli/run hook --changed-only --epochs 10")
    fi
    ;;
  dev)
    SBT_CMDS+=(
      "test"
      "cli/run validate --gates cpg-boundary,constants,magic"
      "cli/run assess --fixture"
    )
    ;;
  main)
    SBT_CMDS+=(
      "test"
      "cli/run validate"
      "cli/run assess --fixture"
      "cli/run assess --repo modules/semantic"
    )
    ;;
  morph)
    [ -n "$RECEIPT" ] || fail "morph tier requires an explicit receipt path: scripts/ci.sh morph RECEIPT"
    [ -f "$RECEIPT" ] || fail "morph receipt is not a file: $RECEIPT"
    SBT_CMDS+=(
      "test"
      "cli/run validate"
      "cli/run morph verify --receipt \"$RECEIPT\""
    )
    ;;
  parity)
    HADOOP=/data/opt/clean/hadoop
    BASELINE=audit/baselines/hadoop-census.json
    [ -d "$HADOOP" ] || { echo "CI SKIP[parity]: no corpus at $HADOOP"; exit 0; }
    [ -f "$BASELINE" ] || fail "no baseline at $BASELINE — record once: sbt \"cli/run assess --repo $HADOOP --baseline $BASELINE --record\""
    SBT_CMDS+=("cli/run assess --repo $HADOOP --baseline $BASELINE")
    ;;
  *)
    echo "CI FAIL: unknown tier '$TIER'" >&2
    exit 2
    ;;
esac

wire start "ci $TIER start"
echo "CI[$TIER] stages:"
printf '  %s\n' "${SBT_CMDS[@]}"

sbt -batch --no-colors "${SBT_CMDS[@]}" || fail "stage failed (see sbt output above)"

if [ "$TIER" = main ]; then
  # determinism replay: identical scans must emit byte-identical topography
  A=$(mktemp -d) || fail "first determinism workspace creation failed"
  B=$(mktemp -d) || fail "second determinism workspace creation failed"
  sbt -batch --no-colors \
    "cli/run scan --repo modules/semantic --ui $A" \
    "cli/run scan --repo modules/semantic --ui $B" >/dev/null \
    || fail "determinism replay scans failed"
  diff -q "$A/shape-statistics.json" "$B/shape-statistics.json" >/dev/null \
    || fail "nondeterministic topography: shape-statistics.json differs between identical scans"
  echo "CI stage PASS: determinism-replay"
fi

final_status=0
echo "CI PASS[$TIER]"
wire pass "ci $TIER pass"
