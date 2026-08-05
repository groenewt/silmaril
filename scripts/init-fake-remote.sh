#!/usr/bin/env bash
# Initialize the "fake" remote: a local bare repository (sibling of the
# working repo, never inside it) whose update hook runs the tiered CI on
# every pushed ref — pushes are enforced server-side, not by convention.
#
#   scripts/init-fake-remote.sh [remote-dir]
set -euo pipefail
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
