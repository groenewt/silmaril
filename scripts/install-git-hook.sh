#!/usr/bin/env bash
# Install the client-side git hooks:
#   pre-commit — sparky hook --changed-only (bounded test-tier gates)
#   pre-push   — scripts/ci.sh <tier of highest target branch>
set -euo pipefail
cd "$(dirname "$0")/.."
ln -sf ../../hooks/pre-commit .git/hooks/pre-commit
echo "pre-commit hook installed (test tier, changed-only)"
ln -sf ../../hooks/pre-push .git/hooks/pre-push
echo "pre-push hook installed (tier by target branch: main > dev > test)"
