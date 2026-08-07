#!/usr/bin/env bash
# coverage.sh TREE_ROOT MANIFEST
# Exit 0 iff MANIFEST covers exactly the file set of TREE_ROOT (excluding .git plumbing).
# Manifest format: sha256<TAB>bytes<TAB>path (paths relative to repo root).
set -euo pipefail
root=$1; manifest=$2
diff <(find "$root" -type f -not -path "*/.git/*" | sort) \
     <(cut -f3 "$manifest" | sort)
echo "COVERAGE EXACT: $root == $manifest ($(wc -l < "$manifest" | tr -d ' ') files)"
