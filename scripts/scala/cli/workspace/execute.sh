#!/usr/bin/env bash

set -o errtrace

scala_cli_workspace_execute_fail() {
  local status=$1
  local line=$2
  printf 'scala-cli-workspace-execute FAIL status=%d at line %d\n' "$status" "$line" >&2
  exit "$status"
}

trap 'status=$?; scala_cli_workspace_execute_fail "$status" "$LINENO"' ERR

if [[ $# -lt 1 ]]; then
  printf 'usage: SCALA_CLI_WORKSPACE=/absolute/path %s <compile|run|test|setup-ide> [arguments...]\n' "$0" >&2
  exit 64
fi

operation=$1
shift

case "$operation" in
  compile|run|test|setup-ide) ;;
  *)
    printf 'unsupported Scala CLI operation: %s\n' "$operation" >&2
    exit 64
    ;;
esac

workspace=${SCALA_CLI_WORKSPACE:?SCALA_CLI_WORKSPACE must name an absolute lane workspace}
case "$workspace" in
  /*) ;;
  *)
    printf 'SCALA_CLI_WORKSPACE must be absolute: %s\n' "$workspace" >&2
    exit 64
    ;;
esac

repository=$(git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel)
workspace=$(realpath -m "$workspace")
case "$workspace" in
  "$repository"|"$repository"/*)
    printf 'Scala CLI lane workspace must remain outside the SBT repository: %s\n' "$workspace" >&2
    exit 64
    ;;
esac

scala_cli_home=${SCALA_CLI_HOME:-"$workspace/.scala-cli"}
case "$scala_cli_home" in
  /*) ;;
  *)
    printf 'SCALA_CLI_HOME must be absolute: %s\n' "$scala_cli_home" >&2
    exit 64
    ;;
esac
scala_cli_home=$(realpath -m "$scala_cli_home")
case "$scala_cli_home" in
  "$repository"|"$repository"/*)
    printf 'Scala CLI home must remain outside the SBT repository: %s\n' "$scala_cli_home" >&2
    exit 64
    ;;
esac

scala_cli=${SCALA_CLI_BINARY:-$(command -v scala-cli)}
export SCALA_CLI_HOME="$scala_cli_home"
exec "$scala_cli" --power "$operation" --workspace "$workspace" "$@"
