#!/usr/bin/env bash

set -o errtrace

scala_cli_workspace_verify_fail() {
  local status=$1
  local line=$2
  printf 'scala-cli-workspace-verify FAIL status=%d at line %d\n' "$status" "$line" >&2
  exit "$status"
}

trap 'status=$?; scala_cli_workspace_verify_fail "$status" "$LINENO"' ERR

if [[ $# -lt 1 ]]; then
  printf 'usage: SCALA_CLI_WORKSPACE=/absolute/path %s <Scala input> [Scala CLI arguments...]\n' "$0" >&2
  exit 64
fi

repository=$(git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel)
workspace=${SCALA_CLI_WORKSPACE:?SCALA_CLI_WORKSPACE must name an absolute lane workspace}
case "$workspace" in
  /*) ;;
  *)
    printf 'SCALA_CLI_WORKSPACE must be absolute: %s\n' "$workspace" >&2
    exit 64
    ;;
esac
workspace=$(realpath -m "$workspace")
case "$workspace" in
  "$repository"|"$repository"/*)
    printf 'Scala CLI lane workspace must remain outside the SBT repository: %s\n' "$workspace" >&2
    exit 64
    ;;
esac
evidence="$workspace/.verification"
mkdir -p "$evidence"

source_state() {
  if [[ -f "$repository/.bsp/sbt.json" ]]; then
    sha256sum "$repository/.bsp/sbt.json"
  fi
  find "$repository/modules" -path '*/src/*' -type d \
    \( -name .bsp -o -name .scala-build \) -printf 'directory|%p\n' \
    > "$evidence/source.directories"
  sort "$evidence/source.directories"
  find "$repository/modules" -path '*/src/*' -type f \
    \( -path '*/.bsp/*' -o -path '*/.scala-build/*' \) -print0 \
    > "$evidence/source.files"
  sort -z "$evidence/source.files" > "$evidence/source.files.sorted"
  xargs -0 -r sha256sum < "$evidence/source.files.sorted"
}

workspace_state() {
  find "$workspace" -type f \
    \( -path '*/.bsp/scala-cli.json' -o -path '*/.scala-build/ide-*.json' \) \
    -print0 > "$evidence/workspace.files"
  sort -z "$evidence/workspace.files" > "$evidence/workspace.files.sorted"
  xargs -0 -r sha256sum < "$evidence/workspace.files.sorted"
}

source_state > "$evidence/source.before"

SCALA_CLI_WORKSPACE="$workspace" \
  "$repository/scripts/scala/cli/workspace/execute.sh" setup-ide \
  --bsp-directory "$workspace/.bsp" "$@"
workspace_state > "$evidence/workspace.first"

if [[ ! -s "$evidence/workspace.first" ]]; then
  printf 'Scala CLI produced no BSP or IDE metadata under %s\n' "$workspace" >&2
  exit 1
fi

SCALA_CLI_WORKSPACE="$workspace" \
  "$repository/scripts/scala/cli/workspace/execute.sh" setup-ide \
  --bsp-directory "$workspace/.bsp" "$@"
workspace_state > "$evidence/workspace.second"
source_state > "$evidence/source.after"

if ! cmp -s "$evidence/workspace.first" "$evidence/workspace.second"; then
  diff -u "$evidence/workspace.first" "$evidence/workspace.second" >&2 || true
  printf 'Scala CLI workspace metadata changed across identical projections\n' >&2
  exit 1
fi

if ! cmp -s "$evidence/source.before" "$evidence/source.after"; then
  diff -u "$evidence/source.before" "$evidence/source.after" >&2 || true
  printf 'Repository BSP or preserved source-root generated state changed\n' >&2
  exit 1
fi

printf 'Scala CLI workspace idempotent: %s\n' "$workspace"
