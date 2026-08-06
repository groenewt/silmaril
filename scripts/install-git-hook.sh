#!/usr/bin/env bash
# Install the repo-managed git bridge hooks via core.hooksPath:
#   pre-commit — staged-blob syntax gate + secret-material block + signing preflight
#   pre-push   — provenance commit policy on every outgoing range
#
#   scripts/install-git-hook.sh [--uninstall]
set -euo pipefail
cd "$(dirname "$0")/.."

if [ "${1:-}" = "--uninstall" ]; then
  git config --unset core.hooksPath || true
  printf '%s\n' "hooks uninstalled (core.hooksPath unset; .git/hooks is active again)"
  exit 0
fi

for hook in pre-commit pre-push; do
  if [ ! -x "hooks/$hook" ]; then
    printf 'ERROR: hooks/%s missing or not executable - refusing to install\n' "$hook" >&2
    exit 1
  fi
done

for existing in .git/hooks/*; do
  case "$existing" in *.sample) continue ;; esac
  if [ -e "$existing" ] || [ -L "$existing" ]; then
    printf 'note: %s will be shadowed while core.hooksPath is set\n' "$existing" >&2
  fi
done

git config core.hooksPath hooks
printf '%s\n' "pre-commit bridge installed (staged-blob syntax + secret block + signing preflight)"
printf '%s\n' "pre-push bridge installed (provenance commit policy on outgoing ranges)"
