#!/usr/bin/env bash
# Initialize the "fake" remote: a local bare repository (sibling of the
# working repo, never inside it) whose update hook enforces the commit-signing
# policy (hooks/remote-update -> the typed provenance pipeline) on every pushed
# ref — pushes are enforced server-side, not by convention.
#
#   scripts/init-fake-remote.sh [remote-dir]
set -euo pipefail
# Refuse to repoint a real (non-local) origin: this script replaces origin with
# a local bare repository and would silently disconnect the repo from GitHub.
# Set SILMARIL_FAKE_REMOTE_FORCE=1 to proceed anyway.
if git remote get-url origin >/dev/null 2>&1; then
  case "$(git remote get-url origin)" in
    /*|file://*) ;;
    *) [ "${SILMARIL_FAKE_REMOTE_FORCE:-0}" = "1" ] || { printf '%s\n' "refusing: origin is a real remote ($(git remote get-url origin)); set SILMARIL_FAKE_REMOTE_FORCE=1 to override" >&2; exit 64; } ;;
  esac
fi
cd "$(dirname "$0")/.."
REPO_ROOT=$(pwd)
REMOTE="${1:-$(dirname "$REPO_ROOT")/sparky-remote.git}"

if [ ! -d "$REMOTE" ]; then
  git init -q --bare "$REMOTE"
  echo "fake remote created: $REMOTE"
fi

# copy, not symlink: the remote must keep enforcing even if the working
# tree moves; re-run this script to refresh the hook after edits
install -m 0755 hooks/remote-update "$REMOTE/hooks/update"
echo "update hook installed: $REMOTE/hooks/update"

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE"
else
  git remote add origin "$REMOTE"
fi
echo "origin -> $REMOTE"
